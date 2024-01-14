import pandas as pd
import math

def calculate_angle(v1, v2):
    """Calculate angle between two vectors in degrees."""
    if hasattr(calculate_angle, 'call_count'):
        calculate_angle.call_count += 1
    else:
        calculate_angle.call_count = 1
    dot_product = sum(v1_i * v2_i for v1_i, v2_i in zip(v1, v2))
    magnitude_v1 = math.sqrt(sum(v1_i**2 for v1_i in v1))
    magnitude_v2 = math.sqrt(sum(v2_i**2 for v2_i in v2))
    if magnitude_v1 == 0 or magnitude_v2 == 0:
        angle =  0
    else:
        cos_angle = dot_product / (magnitude_v1 * magnitude_v2)
        if abs(cos_angle) > 1:
            angle = 0   # Clamp it at 0 if outside the domain of cos
        else:
            angle = math.acos(cos_angle)
    return math.degrees(angle)

def get_vectors(df):
    return [(df.iloc[i+1]['x'] - df.iloc[i]['x'], df.iloc[i+1]['y'] - df.iloc[i]['y']) 
           for i in range(len(df) - 1)]

def get_angles(vectors):
    return [0] + [calculate_angle(vectors[i], vectors[i+1]) if i < len(vectors) - 1 else None 
                   for i in range(len(vectors))]
def distance(df, i, j):
    '''compute the distance using the x and y columns from index i to j'''
    x1, y1 = df.loc[i, 'x'], df.loc[i, 'y']
    x2, y2 = df.loc[j, 'x'], df.loc[j, 'y']
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def speed(df, fps, i=None, j=None):
    if i is None:
        i = 0
    if j is None:
        j = len(df) - 1
    num_frames = j - i
    time_secs = num_frames/fps
    return distance(df, i, j) / time_secs