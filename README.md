# EmoGator

The EmoGator dataset consists of 31,130 non-speech vocal bursts (for example: laughter, sighs, moans, and groans) in 30 categories. 

This is not a complete release at this point, but I'm providing all the data now; hopefully with the information provided the dataset put to use almost immediately.

## Naming Convention

mp3 files are in data/mp3.

There were 357 contributors, 30 vocal burst categories, and 3 instances of each category, providing a balanced dataset with 90 samples for each contributor.

The files are named as follows:

NNNNNN-EE-I.mp3

NNNNNN: contributor ID (000001-000357)
EE - Emotion Category (01-30)
I - Instance (1,2, or 3)

MP3 files were collected at different sample rates, usually near 44100Hz, but dependent on submitter's computer hardware.

The 30 emotion categories are:

['Adoration', 'Amusement', 'Anger', 'Awe', 'Confusion', 'Contempt', 'Contentment', 'Desire', 'Disappointment', 'Disgust', 'Distress', 'Ecstasy', 'Elation', 'Embarrassment', 'Fear', 'Guilt', 'Interest', 'Neutral', 'Pain', 'Pride', 'Realization', 'Relief', 'Romantic Love', 'Sadness', 'Serenity', 'Shame', 'Surprise (Negative)', 'Surprise (Positive)', 'Sympathy', 'Triumph']

The file data/category_names.pt provides a python list with these categories. Note that the samples are labled 01-30, but the categores in the python list are 0-29. A simple:

 __import torch
 category_names=torch.load('data/category-names.pt')__ 

will bring them in.

For now, I've included some utilities in code/utils. 

__duration__ is a bash script that pulls the duration (in seconds) for each mp3 file and displays it; it requires ffmpeg.

__renumber.py__ was used to renumber the samples so they were sequential; you shouldn't need it, and since the data is already sequentially renumbered, it won't do anything. (Just there for completeness, really)

__sum_duration.py__ uses duration to list the duration of each mp3 file, along with a total at the end.

__summary.py__ displays a list of submitter ids and instances for each; just a sanity check to make sure we had 90 samples of each.

More to come!

Paper: https://arxiv.org/abs/2301.00508

