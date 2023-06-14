"""
modified flashes.py to create a white circle that periodically appears on a grey screen
"""

# Import necessary libraries 
from psychopy import monitors, visual
from camstim import Stimulus, SweepStim
from camstim import Window, Warp
import os
import argparse
import logging
import yaml

if __name__ == "__main__":
    parser = argparse.ArgumentParser("mtrain")
    parser.add_argument("json_path", nargs="?", type=str, default="")

    args, _ = parser.parse_known_args() # <- this ensures that we ignore other arguments that might be needed by camstim
    
    # print args
    if args.json_path == "":
        logging.warning("No json path provided, using default parameters. THIS IS NOT THE EXPECTED BEHAVIOR FOR PRODUCTION RUNS")
        json_params = {}
    else:
        with open(args.json_path, 'r') as f:
            # we use the yaml package here because the json package loads as unicode, which prevents using the keys as parameters later
            json_params = yaml.load(f)
            logging.info("Loaded json parameters from mtrain")
            # end of mtrain part

    # Copied monitor and window setup from:
    # https://github.com/AllenInstitute/openscope-glo-stim/blob/main/test-scripts/cohort-1-test-12min-drifting.py

    dist = 15.0
    wid = 52.0

    # mtrain should be providing : Gamma1.Luminance50
    monitor_name = json_params.get('monitor_name', "testMonitor")

    # create a monitor
    if monitor_name == 'testMonitor':
        monitor = monitors.Monitor(monitor_name, distance=dist, width=wid)
    else:
        monitor = monitor_name

    # Create display window
    window = Window(fullscr=True, # Will return an error due to default size. Ignore.
                    monitor=monitor,  # Will be set to a gamma calibrated profile by MPE
                    screen=0,
                    warp=Warp.Spherical
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