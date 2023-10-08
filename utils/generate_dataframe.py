import pandas as pd
import re
import random
import demoji
import os

root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the path to the CSV file relative to the root folder
csv_file = os.path.join(root_folder, "data", "reviews.csv")

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Randomly select 50 records
random.seed(42)  # Set a seed for reproducibility
num_records_to_select = 30
selected_indices = random.sample(range(len(df)), num_records_to_select)
selected_df = df.iloc[selected_indices]

# Preprocess the content column


def preprocess_text(text):
    # Replace tabs, multiple spaces, and newlines with single spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove links from the review
    text = re.sub(r'http\S+', '', text)

    text = demoji.replace(text, '')

    return text


def generate_dataframe():
    selected_df['content'] = selected_df['content'].apply(preprocess_text)
    return selected_df


# Print the preprocessed DataFrame
print(selected_df)
