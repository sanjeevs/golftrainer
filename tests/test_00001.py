from golftrainer import factory
from golftrainer import golf_data_frame_builder as df_builder
import os

def test_load():
    json_fname = os.path.join("data", "00001.json")
    golf_data = factory.create_golf_data(json_fname)
    assert golf_data.video_spec.height == 768
    assert golf_data.video_spec.width == 432
    assert golf_data.num_frames == 136 
    assert golf_data.mp_result.landmarks[0] == "nose"
    assert len(golf_data.mp_result.norm_points) == 136
    