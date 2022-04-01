#!/usr/bin/env python3  

import argparse
import numpy as np
import pandas as pd
from Game import Game
import cv2
import time
from pathlib import Path

__author__ = "Michael McCulloch"
__version__ = "0.1.1"


def main():
    # With the rendered graph in focus press ESC key to exit the program.
    CLOSE_KEY = 27

    # Wait this many milliseconds
    WAIT_TIME = 200

    # This is only useful when you are watching the rendered output
    # without saving, otherwise why slow down the process of rendering.
    SLEEP_TIME = 0.1

    parser = argparse.ArgumentParser(description='Read in a file for use in network graphing and analysis')
    parser.add_argument('--input-file', help='File to process')
    parser.add_argument('--start', type=int, default=0, help='The first timestamp of interest')
    parser.add_argument('--stop', type=int, help='The last timestampt of interest')
    parser.add_argument('--save', action='store_true', help='Create video output')
    parser.add_argument('--output-file', type=str, help='Filename for output a video')
    parser.add_argument('--codec', type=str, default='XVID', help='Video codec to use for video output')
    parser.add_argument('--ext', type=str, default='avi', help='File extension for video output')

    
    args = parser.parse_args()

    if not args.input_file:
        print('Please provide a filename')
    else:
        game = Game(args.input_file)

        # Make sure start and stop are integers, regardless of whether they are
        # provided on the commandline.
        start = args.start or 0
        stop = args.stop or len(game.state)


        if args.save:
            if args.output_file:
                output_file = args.output_file
            else:
                output_file = Path(f"{args.input_file}_{start}-{stop}.{args.ext}").name

            for timestamp in range(start, stop):
                content = np.frombuffer(game.render(timestamp), dtype='uint8')
                img = cv2.imdecode(content, cv2.IMREAD_ANYCOLOR)

                if start == timestamp:
                    height, width, layers = img.shape
                    out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*f"{args.codec}"), 1, (width, height))
    
                out.write(img)

            out.release()

        else:
            for timestamp in range(start, stop):
                content = np.frombuffer(game.render(timestamp), dtype='uint8')
                img = cv2.imdecode(content, cv2.IMREAD_ANYCOLOR)
                cv2.imshow('image',img)

                # https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1
                k = cv2.waitKey(WAIT_TIME) & 0xFF

                if k == CLOSE_KEY:
                    break
                time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()
