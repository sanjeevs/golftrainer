from golftrainer import geom
import pandas as pd 

def test_angle90():
    points = [(2,1), (2,4), (5,4)]
    df = pd.DataFrame(points, columns=('x', 'y'))
    vectors = geom.get_vectors(df)
    assert len(vectors) == 2
    angle = geom.calculate_angle(vectors[0], vectors[1])
    assert int(angle) == 90

def test_angle0():
    points = [(2,1), (3,4), (5,4)]
    df = pd.DataFrame(points, columns=('x', 'y'))
    vectors = geom.get_vectors(df)
    angle = geom.calculate_angle(vectors[0], vectors[1])
    assert int(angle) == 71

def test_angle1():
    points = [(2,1), (3,4), (5,6)]
    df = pd.DataFrame(points, columns=('x', 'y'))
    vectors = geom.get_vectors(df)
    angle = geom.calculate_angle(vectors[0], vectors[1])
    assert int(angle) == 26

def test_angle2():
    points = [(5,6), (3,4), (2,1)]
    df = pd.DataFrame(points, columns=('x', 'y'))
    vectors = geom.get_vectors(df)
    angle = geom.calculate_angle(vectors[0], vectors[1])
    assert int(angle) == 26

def test_angle3():
    points = [(5,6), (6,6), (5,6)]
    df = pd.DataFrame(points, columns=('x', 'y'))
    vectors = geom.get_vectors(df)
    angle = geom.calculate_angle(vectors[0], vectors[1])
    assert int(angle) == 26

def test_fail1():
    points = [(359, 221), (358, 221), (359, 221), (358, 221), 
            (357, 221), (356, 219), (357, 219), (356, 219)]
    df = pd.DataFrame(points, columns=('x', 'y'))
    vectors = geom.get_vectors(df)
    assert len(vectors) == 7
    angle = geom.calculate_angle(vectors[3], vectors[4]) #63
    angle = geom.calculate_angle(vectors[4], vectors[5]) #116
    angle = geom.calculate_angle(vectors[5], vectors[6]) #180
    