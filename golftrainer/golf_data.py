from dataclasses import dataclass
from typing import List, Union

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
class ClubHeadResult:
    norm_points: List[List[float]]
    algos: List[str]

@dataclass
class GolfData:
    video_spec: VideoSpec
    video_input: VideoInput
    num_frames: int
    pose_result: PoseResult
    club_head_result: ClubHeadResult
    mp_result: List[List[float]]
