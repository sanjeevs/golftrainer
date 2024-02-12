from golftrainer import geom
import pandas as pd 

def test_angle90():
    points = [(2,1), (2,4), (5,4)]
    df = pd.DataFrame(points, columns=('x', 'y'))
    vectors = geom.unity_vectors(df)
    assert len(vectors) == 2
    angle = geom.vec_angle_clockwise_degrees(vectors[0], vectors[1])
    assert int(angle) == 90
    assert geom.unity_vec_angles(vectors) == [0, 90]


def test_angle0():
    points = [(2,1), (3,4), (5,4)]
    df = pd.DataFrame(points, columns=('x', 'y'))
    vectors = geom.unity_vectors(df)
    angle = geom.vec_angle_clockwise_degrees(vectors[0], vectors[1])
    assert angle == 71
    assert geom.unity_vec_angles(vectors) == [0, 71]


def test_angle1():
    points = [(2,1), (3,4), (5,6)]
    df = pd.DataFrame(points, columns=('x', 'y'))
    vectors = geom.unity_vectors(df)
    angle = geom.vec_angle_clockwise_degrees(vectors[0], vectors[1])
    assert angle == 26
    assert geom.unity_vec_angles(vectors) == [0, 26]

def test_angle2():
    points = [(5,6), (3,4), (2,1)]
    df = pd.DataFrame(points, columns=('x', 'y'))
    vectors = geom.unity_vectors(df)
    assert vectors[0] == (-2, -2)
    assert vectors[1] == (-1, -3)
    angle = geom.vec_angle_clockwise_degrees(vectors[0], vectors[1])
    assert angle == 153
    assert geom.unity_vec_angles(vectors) == [0, 153]

def test_angle3():
    points = [(5,6), (6,6), (5,6)]
    df = pd.DataFrame(points, columns=('x', 'y'))
    vectors = geom.unity_vectors(df)
    assert vectors == [(1, 0), (-1, 0)]
    angle = geom.vec_angle_clockwise_degrees(vectors[0], vectors[1])
    assert angle == 180
    assert geom.unity_vec_angles(vectors) == [0, 180]