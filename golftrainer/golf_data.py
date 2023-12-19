from dataclasses import dataclass
from typing import List, Union
import pandas as pd

@dataclass
class VideoSpec:
    height: int
    width: int
    num_frames: int
    fps: int
    scale: int
    rotate: str

@dataclass
class VideoInput:
    fname: str
    size: int

@dataclass
class PoseResult:
    poses: List[str]
    handed: str

@dataclass
class MpResult:
    landmarks: List[str]
    norm_points: List[List[float]]

@dataclass
class ClubHeadResult:
    norm_points: List[List[float]]
    algos: List[str]

@dataclass
class GolfData:
    version: float
    video_spec: VideoSpec
    video_input: VideoInput
    num_frames: int
    pose_result: PoseResult
    club_head_result: ClubHeadResult
    mp_result: MpResult

    def mp_4d_names(self):
        return [ 
                f'{name}_{coord}' 
                for name in self.mp_result.landmarks 
                for coord in ['x', 'y', 'z', 'v']
        ]

    def mp_data_frame(self):
        return pd.DataFrame(self.mp_result.norm_points, columns=self.mp_4d_names())

    def col_names(self):
        cols  = [
                f'{name}_{coord}' 
                for name in self.mp_result.landmarks 
                for coord in ['x', 'y']
        ]
        cols.append("club_head_x")
        cols.append("club_head_y")
        return cols

    def norm_data_frame(self):
        rows = []
        for idx, points in enumerate(self.mp_result.norm_points):
            # Process norm_points
            new_list = [points[i:i + 2] for i in range(0, len(points), 4)]
            flattened_list = [coord for pair in new_list for coord in pair]

            # Add the club head position
            if idx < len(self.club_head_result.norm_points):
                if self.club_head_result.norm_points[idx]:
                    club_head = self.club_head_result.norm_points[idx][:2]
                else:  
                    club_head = (0, 0)
            else:
                # If no, use (0, 0) as a default value
                club_head = (0, 0)
            flattened_list.extend(club_head)
            rows.append(flattened_list)
        return pd.DataFrame(rows, columns=self.col_names())

    def screen_data_frame(self, scale_pcnt=100):
        ''' Scale with origin at left top of the screen. '''
        norm_frame = self.norm_data_frame()
        scaled_df = norm_frame.copy()
    
        width = self.video_spec.width * scale_pcnt/100
        height = self.video_spec.height * scale_pcnt/100

        for i in range(len(norm_frame.columns)):
            if i % 2 == 0: #Even is x value
                scaled_df.iloc[:, i] = (norm_frame.iloc[:, i] * width).astype(int)
            else:
                scaled_df.iloc[:, i] = (norm_frame.iloc[:, i] * height).astype(int)
        
        return scaled_df

    def cart_data_frame(self, scale_pcnt=100):
        ''' Scale with origin at the left bottom of the screen. '''
        norm_frame = self.norm_data_frame()
        scaled_df = norm_frame.copy()
        width = self.video_spec.width * scale_pcnt/100
        height = self.video_spec.height * scale_pcnt/100

        for i  in range(len(norm_frame.columns)):
            if i % 2 == 0: 
                # even is x-value, does not change
                scaled_df.iloc[:, i] = (norm_frame.iloc[:, i] * width).astype(int)
            else:
                # odd is y-value, inverting the y-axis
                scaled_df.iloc[:, i] = ((1 - norm_frame.iloc[:, i]) * height).astype(int)
                
        return scaled_df