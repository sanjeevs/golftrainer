import pandas as pd
import math

def vec_angle_clockwise_degrees(v1, v2):
    """Calculate angle between two vectors in degrees."""
    dot_product = sum(v1_i * v2_i for v1_i, v2_i in zip(v1, v2))
    magnitude_v1 = math.sqrt(sum(v1_i**2 for v1_i in v1))
    magnitude_v2 = math.sqrt(sum(v2_i**2 for v2_i in v2))
    if magnitude_v1 == 0 or magnitude_v2 == 0:
        degrees =  0
    else:
        cos_angle = dot_product / (magnitude_v1 * magnitude_v2)
        if abs(cos_angle) > 1:
            angle = 0   # Clamp it at 0 if outside the domain of cos
        else:
            angle = math.acos(cos_angle)

        degrees = math.degrees(angle)
        rotation = v1[0] * v2[1] - v1[1] * v2[0]
        if rotation > 0:
            '''positive for counter clockwise'''
            degrees = 180 - degrees

    return int(degrees)

def unity_vectors(df):
    """ Return the unity vectors from a  list of points. """
    if len(df) <= 1:
        return []
    else:
        return [(df.iloc[i+1]['x'] - df.iloc[i]['x'], df.iloc[i+1]['y'] - df.iloc[i]['y']) 
                for i in range(len(df) - 1)]

def unity_vec_angles(unity_vectors):
    ''' 
    Return the angle between the vectors. To keep the length the same as vectors,
    we assume that the first angle is 0.
    '''
    if len(unity_vectors) == 0:
        return []
    else:
        return [0] + [vec_angle_clockwise_degrees(unity_vectors[i], unity_vectors[i+1]) 
                   for i in range(len(unity_vectors) -1)]

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

def moving_average(values, period):
    """
    Calculates the moving average for a list of numbers.
    
    Parameters:
    - values: A list of numerical values.
    - period: The number of values to include in the moving average calculation.
    
    Returns:
    - A list of moving averages.
    """
    moving_averages = []  # List to store the moving averages
    
    # Check if period is greater than the list length
    if period > len(values) or period <= 0:
        print("Error: Period must be greater than 0 and less than or equal to the length of the values list.")
        return []
    
    # Calculate the moving averages
    for i in range(len(values) - period + 1):
        window = values[i:i + period]  # Create the window for the current moving average
        window_average = sum(window) / period  # Calculate the average of the window
        moving_averages.append(window_average)  # Add the average to the list of moving averages
    
    return moving_averages


def find_y_incr_decr_ranges(df):
    # Create a copy of the DataFrame to avoid modifying the original
    df_copy = df.copy()

    # Calculate the difference between successive 'y' values in the copy
    df_copy['y_diff'] = df_copy['y'].diff()

    # Initialize lists to store the ranges
    increasing_ranges = []
    decreasing_ranges = []
    current_range = {'start': None, 'end': None, 'type': None}

    for i, diff in enumerate(df_copy['y_diff']):
        if diff >= 0:
            if current_range['type'] == 'increasing':
                current_range['end'] = i + 1  # Adjust to include the end row in the range
            else:
                if current_range['type'] == 'decreasing':
                    decreasing_ranges.append((current_range['start'], current_range['end']))
                current_range = {'start': i, 'end': i + 1, 'type': 'increasing'}
        elif diff < 0:
            if current_range['type'] == 'decreasing':
                current_range['end'] = i + 1
            else:
                if current_range['type'] == 'increasing':
                    increasing_ranges.append((current_range['start'], current_range['end']))
                current_range = {'start': i, 'end': i + 1, 'type': 'decreasing'}

    # Add the last range found
    if current_range['type'] == 'increasing':
        increasing_ranges.append((current_range['start'], current_range['end']))
    elif current_range['type'] == 'decreasing':
        decreasing_ranges.append((current_range['start'], current_range['end']))

    # Return the ranges without altering the original DataFrame
    return increasing_ranges, decreasing_ranges
