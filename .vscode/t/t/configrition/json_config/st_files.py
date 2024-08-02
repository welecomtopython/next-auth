
import time
import sys
import os

import numpy as np


def find_max_extension():
    # List all files in the current working directory
    dir = os.listdir(os.getcwd())

    # Extract the file extensions from the list of files
    exic = list(map(lambda x: x.split('.')[-1], dir))


    # Create a NumPy array with the file extensions
    lis = np.array(exic)

    # Get the unique elements (extensions) and their corresponding counts in the array
    unique, counts = np.unique(lis, return_counts=True)

    # Find the index of the maximum count
    most_frequent_index = np.argmax(counts)

    # Retrieve the most frequent element (extension) and its count based on the index
    most_frequent_element = unique[most_frequent_index]
    count = counts[most_frequent_index]

    # Print the most frequent element (extension) and its count


    # Print the unique extensions and their counts for debugging purposes


    return  {
        'maxextensions':count,
        'extension':most_frequent_element,
        'Unique extensions:':unique,
        "All extensions:" : exic,
        'files':dir

    }



def loading_animation(status=True):
    duration =1
    while status:
        # Characters to display in the loading animation
        animation = ["Loading   ", "Loading.  ", "Loading.. ", "Loading..."]

        # End time for the loading animation
        end_time = time.time() + duration

        # Loop until the duration has passed
        while time.time() < end_time:
            for frame in animation:
                # Print the current frame and flush the output buffer
                sys.stdout.write("\r" + frame)
                sys.stdout.flush()
                # Sleep for a short interval to create the animation effect
                time.sleep(0.5)

        # Clear the loading message after completion
        sys.stdout.write("\r" + " " * len(animation[-1]) + "\r")
        sys.stdout.flush()
        duration +=1


a=True

while a:

    loading_animation(a)

    time.sleep(5)

    a=False


