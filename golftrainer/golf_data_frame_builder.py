import pandas as pd

'''
Construct a data frame for basic usage.
'''

class GolfDataFrameBuilder:
    def __init__(self, golf_data):
        self.gd = golf_data
        self.mp_col_names = [f'{name}_{coord}' 
                for name in self.gd.mp_result.landmarks 
                for coord in ['x', 'y', 'z', 'v']]
        self.tracker_col_names = [f'{name}_{coord}' 
                for name in self.gd.mp_result.landmarks 
                for coord in ['x', 'y']]
        self.tracker_col_names.append("club_head_x")
        self.tracker_col_names.append("club_head_y")

    def mp_norm_frame(self):
        ''' Returns the x, y, z, v coordinate of each mediapipe point. '''
        df = pd.DataFrame(self.gd.mp_result.norm_points, columns=self.mp_col_names)
        return df

    def tracker_norm_frame(self):
        ''' Get the (x, y) coord of all the points. '''
        rows = []
        for idx in range(len(self.gd.mp_result.norm_points)):
            entry = self.gd.mp_result.norm_points[idx]
            row = []
            for i in range(len(entry)):
                if i % 4 == 0 or i % 4 == 1:
                    row.append(entry[i])

            row.append(self.gd.club_head_result.norm_points[idx][0])
            row.append(self.gd.club_head_result.norm_points[idx][1])    
            rows.append(row)
        return pd.DataFrame(rows, columns=self.tracker_col_names)

    def tracker_screen_frame(self, scale_pcnt=100):
        ''' Scale with origin at left top of the screen. '''
        norm_frame = self.tracker_norm_frame()
        scaled_df = norm_frame.copy()
    
        width = self.gd.video_spec.width * scale_pcnt/100
        height = self.gd.video_spec.height * scale_pcnt/100

        for i in range(len(norm_frame.columns)):
            if i % 2 == 0: #Even is x value
                scaled_df.iloc[:, i] = (norm_frame.iloc[:, i] * width).astype(int)
            else:
                scaled_df.iloc[:, i] = (norm_frame.iloc[:, i] * height).astype(int)
        
        return scaled_df

    def tracker_cart_frame(self, scale_pcnt=100):
        ''' Scale with origin at the left bottom of the screen. '''
        norm_frame = self.tracker_norm_frame()
        scaled_df = norm_frame.copy()
        width = self.gd.video_spec.width * scale_pcnt/100
        height = self.gd.video_spec.height * scale_pcnt/100

        for i  in range(len(norm_frame.columns)):
            if i % 2 == 0: 
                # even is x-value, does not change
                scaled_df.iloc[:, i] = (norm_frame.iloc[:, i] * width).astype(int)
            else:
                # odd is y-value, inverting the y-axis
                scaled_df.iloc[:, i] = ((1 - norm_frame.iloc[:, i]) * height).astype(int)
                
        return scaled_df
