from golftrainer import factory
from golftrainer import golf_data_frame_builder as df_builder

json_data = """
{
    "video_spec": {
        "height": 768,
        "width": 432,
        "num_frames": 1,
        "fps": 30,
        "scale": 100,
        "rotate": ""
    },
    "video_input": {
        "fname": "test1.mov",
        "size": 18923
    },
    "num_frames": 1,
    "pose_result": {
        "poses": [
            "RhStart"
        ],
        "handed": "Unknown"
    },
    "club_head_result": {
        "norm_points": [
            [
                0.7546296296296297,
                0.734375
            ]
        ],
        "algos": [
            "Label"
        ]
    },
    "mp_result": {
        "landmarks": [
            "nose",
            "left_eye_inner",
            "left_eye",
            "left_eye_outer",
            "right_eye_inner",
            "right_eye",
            "right_eye_outer",
            "left_ear",
            "right_ear",
            "mouth_left",
            "mouth_right",
            "left_shoulder",
            "right_shoulder",
            "left_elbow",
            "right_elbow",
            "left_wrist",
            "right_wrist",
            "left_pinky",
            "right_pinky",
            "left_index",
            "right_index",
            "left_thumb",
            "right_thumb",
            "left_hip",
            "right_hip",
            "left_knee",
            "right_knee",
            "left_ankle",
            "right_ankle",
            "left_heel",
            "right_heel",
            "left_foot_index",
            "right_foot_index"
        ],
        "norm_points": [
            [
                0.45863062143325806,
                0.3661975860595703,
                0.12614630162715912,
                0.9975948929786682,
                0.45920422673225403,
                0.3572676479816437,
                0.12335512042045593,
                0.9982975125312805,
                0.4568693935871124,
                0.35659489035606384,
                0.12326707690954208,
                0.9983774423599243,
                0.454563170671463,
                0.3558994233608246,
                0.12312024086713791,
                0.998634397983551,
                0.46338844299316406,
                0.3581920862197876,
                0.07945127040147781,
                0.99847012758255,
                0.463850736618042,
                0.3582695722579956,
                0.07927587628364563,
                0.9983654618263245,
                0.46436190605163574,
                0.3583643436431885,
                0.07898645848035812,
                0.9987230896949768,
                0.44013190269470215,
                0.3567873537540436,
                0.11032243818044662,
                0.9974455833435059,
                0.45478159189224243,
                0.36068451404571533,
                -0.08331935852766037,
                0.9984656572341919,
                0.4472264051437378,
                0.3738296926021576,
                0.12863515317440033,
                0.9978908896446228,
                0.45011547207832336,
                0.37388965487480164,
                0.07193774729967117,
                0.9986521601676941,
                0.3653787672519684,
                0.392925888299942,
                0.24378003180027008,
                0.9969086050987244,
                0.4152315855026245,
                0.4067727029323578,
                -0.2924339473247528,
                0.9999754428863525,
                0.32340776920318604,
                0.4738546311855316,
                0.25164732336997986,
                0.016680097207427025,
                0.4166150987148285,
                0.48626336455345154,
                -0.260283887386322,
                0.9800035357475281,
                0.3070394694805145,
                0.5279031991958618,
                0.17738857865333557,
                0.011164293624460697,
                0.4613264799118042,
                0.555598795413971,
                -0.04179566353559494,
                0.7901973128318787,
                0.29768645763397217,
                0.5449895858764648,
                0.18450666964054108,
                0.013078340329229832,
                0.4716939926147461,
                0.5735800862312317,
                -0.05354275181889534,
                0.730597734451294,
                0.2990829646587372,
                0.5436312556266785,
                0.16175530850887299,
                0.012955317273736,
                0.47557175159454346,
                0.5738845467567444,
                -0.03443075716495514,
                0.717094361782074,
                0.30446144938468933,
                0.5377213358879089,
                0.16280733048915863,
                0.014436870813369751,
                0.46984541416168213,
                0.5680651664733887,
                -0.02762756682932377,
                0.6432913541793823,
                0.24780654907226562,
                0.5126863718032837,
                0.19247747957706451,
                0.9982929825782776,
                0.2583158612251282,
                0.5163936018943787,
                -0.19246338307857513,
                0.9996728897094727,
                0.3217400908470154,
                0.5951215028762817,
                0.35627084970474243,
                0.1745770424604416,
                0.34058424830436707,
                0.6100032329559326,
                -0.09235919266939163,
                0.9792245030403137,
                0.3162862956523895,
                0.6956855654716492,
                0.5494100451469421,
                0.373791366815567,
                0.31863176822662354,
                0.7163334488868713,
                0.001678059808909893,
                0.9799025654792786,
                0.3017665147781372,
                0.7160186171531677,
                0.5647397041320801,
                0.38621360063552856,
                0.29757675528526306,
                0.7388376593589783,
                0.005328497849404812,
                0.9541183710098267,
                0.39773106575012207,
                0.7128636240959167,
                0.5276219844818115,
                0.5492114424705505,
                0.4114198088645935,
                0.7326139807701111,
                -0.09730588644742966,
                0.9676955342292786
            ]
        ]
    }
}
"""

def test_load1():
    golf_data = factory.create_golf_data_s(json_data)
    assert golf_data.video_spec.height == 768
    assert golf_data.mp_result.landmarks[0] == "nose"
    assert len(golf_data.mp_result.norm_points) == 1

def test_mp_norm_df():
    gd = factory.create_golf_data_s(json_data)

    builder = df_builder.GolfDataFrameBuilder(gd)
    df = builder.mp_norm_frame()
    exp_cols = len(gd.mp_result.landmarks) * 4
    assert df.shape[1] == exp_cols
    assert df.columns[0] == "nose_x"


def test_tracker_screen_df():
    gd = factory.create_golf_data_s(json_data)
    
    builder = df_builder.GolfDataFrameBuilder(gd)
    df = builder.tracker_screen_frame()
    exp_cols = len(gd.mp_result.landmarks) * 2 + 2
    assert df.shape[1] == exp_cols
    assert df.shape[0] == 1
    assert df.columns[0] == "nose_x"
    assert df.columns[-1] == "club_head_y"
    assert df.iloc[0, -2] == int(0.7546296296296297 * gd.video_spec.width)
    assert df.iloc[0, -1] == int(0.734375 * gd.video_spec.height)
  
def test_tracker_cart_df():
    gd = factory.create_golf_data_s(json_data)
    
    builder = df_builder.GolfDataFrameBuilder(gd)
    df = builder.tracker_cart_frame()
    exp_cols = len(gd.mp_result.landmarks) * 2 + 2
    assert df.shape[1] == exp_cols
    assert df.shape[0] == 1
    assert df.columns[0] == "nose_x"
    assert df.columns[-1] == "club_head_y"
    assert df.iloc[0, -2] == int(0.7546296296296297 * gd.video_spec.width)
    assert df.iloc[0, -1] == (gd.video_spec.height - int(0.734375 * gd.video_spec.height))
  
