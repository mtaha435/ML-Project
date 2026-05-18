# Split the data into testing/training
'''We are going to have 7/9 subjects purely for training and
2/9 subjects purely for testing, this makes it so the model doesn't 
benefit from adapting to the noise of any particular subject.
'''
import numpy as np
import pandas as pd

df = pd.read_csv('data/train/')