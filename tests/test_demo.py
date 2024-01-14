from golftrainer import factory
import os

def test_load():
    json_fname = os.path.join("data", "00001.json")
    gd = factory.create_golf_data(json_fname)
    assert gd.version == 1.0
    assert gd.video_spec.height == 768
    assert gd.video_spec.width == 432
    assert gd.num_frames == 136 
    assert gd.mp_result.landmarks[0] == "nose"
    assert len(gd.mp_result.norm_points) == 136
    

def test_data_frame():
    json_fname = "data/00001.json"
    gd = factory.create_golf_data(json_fname)
    df = gd.screen_data_frame()
    num_rows, num_cols = df.shape
    assert num_rows == gd.num_frames
    assert num_cols == len(gd.mp_result.landmarks) * 2 + 2
