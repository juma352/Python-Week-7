import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def load_data(file_path):
    df = pd.read_csv(file_path)
    print("Data loaded successfully.")
    return df

def explore_data(df):
    print("First 5 rows of the dataset:")
    print(df.head())
    print("\nData types:")
    print(df.dtypes)
    print("\nMissing values per column:")
    print(df.isnull().sum())

def basic_analysis(df):
    print("\nBasic statistics of numerical columns:")
    print(df.describe())
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    if len(categorical_cols) > 0:
        group_col = categorical_cols[0]
        print(f"\nMean of numerical columns grouped by '{group_col}':")
        grouped = df.groupby(group_col).mean(numeric_only=True)
        print(grouped)
    else:
        print("\nNo categorical columns to group by.")

        #Number of unique values in each column
    print("\nNumber of unique values in each column:")
    unique_counts = df.nunique()
    print(unique_counts)

    #Get the number of latest manufacturing year
    if 'Manufacturing_year' in df.columns:
        latest_year = df['Manufacturing_year'].max()
        print(f"\nLatest manufacturing year: {latest_year}")
    else:
        print("\n'Manufacturing_year' column not found in the dataset.")

def create_visualizations(df):
    sns.set(style="whitegrid")
    plt.figure(figsize=(14, 12))

    # Price distribution with KDE
    plt.subplot(3, 2, 1)
    sns.histplot(df['Price'], bins=30, kde=True, color='skyblue')
    plt.title('Price Distribution')
    plt.xlabel('Price')
    plt.ylabel('Count')

    # Count plot of Fuel type
    plt.subplot(3, 2, 2)
    sns.countplot(x='Fuel type', data=df, palette='Set2')
    plt.title('Count of Fuel Types')
    plt.xlabel('Fuel Type')
    plt.ylabel('Count')

    # Average Price by Transmission type
    plt.subplot(3, 2, 3)
    sns.barplot(x='Transmission', y='Price', data=df, errorbar=None, palette='Set1')
    plt.title('Average Price by Transmission Type')
    plt.xlabel('Transmission')
    plt.ylabel('Average Price')

    # Scatter plot KM driven vs Price colored by Ownership
    plt.subplot(3, 2, 4)
    sns.scatterplot(x='KM driven', y='Price', hue='Ownership', data=df, palette='Set1')
    plt.title('KM Driven vs Price by Ownership')
    plt.xlabel('KM Driven')
    plt.ylabel('Price')
    plt.legend(title='Ownership')

    # Count plot of Ownership
    plt.subplot(3, 2, 5)
    sns.countplot(x='Ownership', data=df, palette='Set3')
    plt.title('Count of Ownership')
    plt.xlabel('Ownership')
    plt.ylabel('Count')

    # Histogram of Imperfections
    plt.subplot(3, 2, 6)
    sns.histplot(df['Imperfections'], bins=20, color='coral', edgecolor='black')
    plt.title('Distribution of Imperfections')
    plt.xlabel('Imperfections')
    plt.ylabel('Count')

    plt.tight_layout()
    plt.show()

def main():
    file_path = 'cars24data.csv'
    df = load_data(file_path)
    explore_data(df)
    basic_analysis(df)
    create_visualizations(df)

if __name__ == "__main__":
    main()
