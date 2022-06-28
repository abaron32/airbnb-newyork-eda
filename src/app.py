## Cleaning pipeline

#1# Importing libraries

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns
import plotly.express as px

#2# Reading dataset

data = pd.read_csv('/workspace/airbnb-newyork-eda/data/raw/AB_NYC_2019.csv')

# Data dictionary: https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit#gid=982310896
# Not all the variables in the dictionary are in the dataset


#3# Convert the variables to the right type

for var in ["neighbourhood", "neighbourhood_group", "room_type", "host_id"]:
  data[var] = pd.Categorical(data[var])

data["last_review"] = data["last_review"].astype("datetime64")


#4# Check if there are duplicates

data_duplicates = data['id'].duplicated().sum()
print(f'It seems that there are {data_duplicates} duplicated listings in the dataset according to the feature id.')


#5# Remove irrelevant columns

drop_cols = ['id','host_name']
data = data.drop(drop_cols, axis=1)


#6# Dropping data with price=0

data = data[data['price']!=0]


#7# Create new features

data['last_review_2'] = data['last_review'].dt.to_period('M')
data['last_review_month'] = data['last_review'].dt.month
data['last_review_year'] = data['last_review'].dt.year


#8# Deal with missing values

#Replace the missing value with '0' of the 'reviews_per_month' feature using 'fillna' method
data['reviews_per_month'] = data['reviews_per_month'].fillna(0)


#9# Encoding categorical variables

# Encoding the 'room_type' column
data['room_type'] = data['room_type'].map({'Entire home/apt' : 0, 'Private room': 1, 'Shared room': 2})

# Encoding the 'neighbourhood_group' column
data['neighbourhood_group'] = data['neighbourhood_group'].map({'Bronx' : 0, 'Brooklyn': 1, 'Manhattan': 2, 'Queens': 3, 'Staten Island': 4})


#10# Save the processed dataframe

data.to_csv('/workspace/airbnb-newyork-eda/data/processed/data_processed.csv')