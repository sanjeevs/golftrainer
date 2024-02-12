'''
Plotting utilities for various parts of a swing.
'''
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation
import numpy as np

from golftrainer import geom

def create_club_head_y(club_df):
    plt.plot(club_df['y'], linestyle='-', color='b')
    plt.title("Club Head Y Position")
    plt.xlabel("Frame Idx")
    plt.ylabel("y_pos")
    incr_ranges, decr_ranges = geom.find_y_incr_decr_ranges(club_df)
    for r in incr_ranges:
        plt.axvline(r[1], color='r')
    for r in decr_ranges:
        plt.axvline(r[1], color='y')


def animate_data_frames(data_frames, legends, text_data=None):
    # Set up the figure and axis for animation
    
    if not isinstance(data_frames, list):
        data_frames = [data_frames]

    if not isinstance(legends, list):
        legends = [legends]

    max_width = max(df.shape[0] for df in data_frames)
    max_height = max(df['y'].max() for df in data_frames)

    #fig, ax = plt.subplots(figsize=(max_width, max_height / max_width * 6))
    fig, ax = plt.subplots()
    ax.set_xlim(0, max_width + 10)  # Screen width
    ax.set_ylim(0, max_height + 10)  # Screen height

    # Colors for each line
    colors = plt.cm.jet(np.linspace(0, 1, len(data_frames)))

    # Create a line object for each data frame and initialize a data store for each
    lines = [ax.plot([], [], lw=2, label=legend, color=color)[0] for _, legend, color in zip(data_frames, legends, colors)]
    data_store = [[[], []] for _ in data_frames]  # Store for x and y data for each line
    frame_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
    # Create text objects for displaying (x, y) values
    xy_texts = [ax.text(0, 0, '', color=color) for color in colors]

    # Handle additional text data if provided
    extra_texts = []
    if text_data:
        for idx, (key, _) in enumerate(text_data.items()):
            text = ax.text(0.02, 0.85 - idx*0.05, '', transform=ax.transAxes)
            extra_texts.append(text)

    # Initialize function for the animation
    def init():
        for line in lines:
            line.set_data([], [])
        frame_text.set_text('')
        for text in xy_texts + extra_texts:
            text.set_text('')
        return lines + xy_texts + extra_texts

    # Update function for each frame
    def update(frame):
        for line, df, data, xy_text in zip(lines, data_frames, data_store, xy_texts):
            x, y = df.iloc[frame]['x'], df.iloc[frame]['y']
            data[0].append(x)
            data[1].append(y)
            line.set_data(data[0], data[1])
            xy_text.set_position((x, y))
            xy_text.set_text(f'({x:.0f}, {y:.0f})')
            
        # Update the frame index text
        frame_text.set_text(f'Frame: {frame}')
        # Update additional text data if provided
        if text_data:
            for text, (key, values) in zip(extra_texts, text_data.items()):
                text.set_text(f'{key}: {values[frame]:.02f}')

        return lines + xy_texts + extra_texts

    # Create animation
    ani = FuncAnimation(fig, update, frames=min(map(len, data_frames)), init_func=init, blit=True)

    # Adding legend
    ax.legend()

    # Show the plot
    #plt.show()
    return ani