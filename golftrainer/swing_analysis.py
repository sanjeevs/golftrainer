'''
Analyze the golf data
'''
from golftrainer import geom
import numpy as np 


class SwingAnalysis:

    def __init__(self, golf_data):
        self.gd = golf_data
        self.df = self.gd.cart_data_frame()
        self.ch = self.gd.point_xy_data_frame(self.df, "club_head")
        

    def swing_phases(self, ext_angle=100):
        """Returns a dict that represents the index of the various phases."""
        angles = geom.unity_vec_angles(geom.unity_vectors(self.ch))
    
        indices = [index for index, value in enumerate(angles) if value > ext_angle]

        phases = ["Backswing", "TransitA", "TransitB", "Downswing", "Finish"]
        phase_dict = {phase: None for phase in phases}

        # Update the phase ranges based on the indices
        if indices:
            phase_dict["Backswing"] = [0, indices[0]] if len(indices) > 0 else [0, None]

        if len(indices) > 1:
            phase_dict["TransitA"] = [indices[0], indices[1]]

        if len(indices) > 2:
            phase_dict["TransitB"] = [indices[1], indices[2]]

        if len(indices) > 3:
            phase_dict["Downswing"] = [indices[2], indices[3]]

        if len(indices) > 4:
            phase_dict["Finish"] = [indices[4], self.gd.num_frames]

        return phase_dict

    
    def ch_backswing_df(self, phase_dict):
        (start, stop) = phase_dict["Backswing"]
        return self.ch[start:stop].reset_index(drop=True)

    def ch_downswing_df(self, phase_dict):
        (start, stop) = phase_dict["Downswing"]
        return self.ch[start:stop].reset_index(drop=True)

    def impact_frame_idx(self, phase_dict):
        backswing_df = self.ch_backswing_df(phase_dict)
        ball_pos = (backswing_df.iloc[0]['x'], backswing_df.iloc[1]['y'])

        distances = np.sqrt((self.ch['x'] - ball_pos[0])**2 + (self.ch['y'] - ball_pos[1])**2)
        # The impact must occur after the backswing.
        backswing_idx = phase_dict["Backswing"][1]
        impact_idx = distances[backswing_idx:].idxmin()
        return impact_idx

        
