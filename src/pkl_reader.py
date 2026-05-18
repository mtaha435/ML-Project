import pickle
import pandas as pd

file_path = 'data/epoched_train.pkl'

with open(file_path, "rb") as f:
    df = pickle.load(f)

df.to_csv('train_data.csv',index=False)
'''
print(df.shape)
print(df.columns)
print(df.head)'''