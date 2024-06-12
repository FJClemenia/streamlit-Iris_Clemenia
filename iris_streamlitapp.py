import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset from a CSV file
df = pd.read_csv('iris.csv')

# Create a Streamlit app
st.title("Iris Dataset App")
st.write("This app allows you to visualize the Iris dataset and view statistics for each species.")

# Display the dataset
st.write("Dataset:")
st.write(df)

# Create a dropdown menu for selecting the species
species = st.selectbox("Select a species:", df['species'].unique())

# Filter the dataset by the selected species
species_df = df[df['species'] == species]

# Calculate the statistics for the selected species
stats = species_df.describe()

# Display the statistics
st.write("Statistics for", species)
st.write(stats)

# Create a scatter plot for the averages of each feature for the selected species
fig, ax = plt.subplots(figsize=(8, 8))
sns.scatterplot(x='sepal_length', y='sepal_width', data=species_df)
ax.set_title(f"Averages for {species}")
st.pyplot(fig)

# Create a scatter plot for the averages of each feature for the selected species
fig, ax = plt.subplots(figsize=(8, 8))
sns.scatterplot(x='petal_length', y='petal_width', data=species_df)
ax.set_title(f"Averages for {species}")
st.pyplot(fig)

# Create a scatter plot for the averages of each feature for the selected species
fig, ax = plt.subplots(figsize=(8, 8))
sns.scatterplot(x='sepal_length', y='petal_length', data=species_df)
ax.set_title(f"Averages for {species}")
st.pyplot(fig)

# Create a scatter plot for the averages of each feature for the selected species
fig, ax = plt.subplots(figsize=(8, 8))
sns.scatterplot(x='sepal_width', y='petal_width', data=species_df)
ax.set_title(f"Averages for {species}")
st.pyplot(fig)