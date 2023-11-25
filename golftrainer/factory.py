''' Create various objects. '''
import json
from golftrainer import golf_data as gd

def create_golf_data(json_data):
    parsed_data = json.loads(json_data)

    # Creating an instance of GolfData from the parsed data
    inst = gd.GolfData(
        video_spec=gd.VideoSpec(**parsed_data["video_spec"]),
        video_input=gd.VideoInput(**parsed_data["video_input"]),
        num_frames=parsed_data["num_frames"],
        pose_result=gd.PoseResult(**parsed_data["pose_result"]),
        club_head_result=gd.ClubHeadResult(**parsed_data["club_head_result"]),
        mp_result=parsed_data["mp_result"]
    )

    return inst
