import pandas as pd
import os
from model_training import train_model

def save_new_data(user_input_to_save):
    if os.path.exists("data/new_data.csv"):
        new_data_df = pd.read_csv("data/new_data.csv")
        new_data_df = pd.concat([new_data_df, pd.DataFrame([user_input_to_save])], ignore_index=True)
        new_data_df.to_csv("data/new_data.csv", index=False)
    else:
        pd.DataFrame([user_input_to_save]).to_csv("data/new_data.csv", index=False)

def combine_and_retrain():
    base_df = pd.read_csv("data/train.csv")

    if os.path.exists("data/new_data.csv"):
        new_data_df = pd.read_csv("data/new_data.csv")
        combined_df = pd.concat([base_df, new_data_df], ignore_index=True)
    else:
        combined_df = base_df

    combined_df.to_csv("data/combined_train.csv", index=False)
    train_model('data/combined_train.csv')
