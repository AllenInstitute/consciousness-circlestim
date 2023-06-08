"""
modified flashes.py to create a white circle that periodically appears on a grey screen
"""

# Import necessary libraries 
from psychopy import monitors, visual
from camstim import Stimulus, SweepStim
from camstim import Window, Warp
import os

# Define monitor parameters 
dist = 15.0
wid = 52.0

# # create a monitor
monitor = monitors.Monitor("testMonitor", distance=dist, width=wid) #"Gamma1.Luminance50"

# Create display window
window = Window(fullscr=True,
                # monitor= 'Gamma1.Luminance50',          # MS 
               monitor = monitor,
               screen=0,
)

# Create a stimulus using a circle mask  
circle = Stimulus(visual.GratingStim(window,
                    pos=(0, 0),
                    units='deg',
                    size=(80, 80),
                    mask="circle",
                    texRes=256,
                    sf=0,
                    phase = 0, 
                    ),
    sweep_params={
               'Contrast': ([1], 0),
                'Color': ([1], 1), 
               },
    sweep_length=0.25,
    start_time=5.0,
    blank_length=4.1,
    blank_sweeps=0,
    runs=120,
    shuffle=False,
    save_sweep_table=True,
    )

params = {

}

# Create SweepStim instance
ss = SweepStim(window,
               stimuli=[circle],
               pre_blank_sec=0,
               post_blank_sec=0,
               params=params,
               )

# Run the SweepStim instance
ss.run()