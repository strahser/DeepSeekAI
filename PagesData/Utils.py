from typing import Optional

import pandas as pd
import streamlit as st
import seaborn as sns
import io
import base64
import time
import random
import matplotlib.pyplot as plt


def create_network_test(df, user_prompt):
    time.sleep(random.uniform(1, 4))
    try:
        selected_function = neural_network_responses.get(user_prompt)
        if selected_function:
            result = selected_function(df)
            return result
        else:
            return "No matching function found for the given prompt."
    except Exception as e:
        return f"Error during network test: {e}"


def create_and_embed_plot(df, plot_type, column1, column2=None):  # Added handling for different plot types
    """Creates a plot based on the DataFrame and returns an HTML img tag embedding the plot."""
    plt.figure()  # Important to create a new figure for each plot
    if plot_type == "bar":
        sns.barplot(x=column1, y=column2, data=df)
        plt.xlabel(column1)  # add labels
        plt.ylabel(column2)
        plt.title(f"Bar Plot of {column2} vs {column1}")

    elif plot_type == "scatter":
        sns.scatterplot(x=column1, y=column2, data=df)
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.title(f"Scatter Plot of {column2} vs {column1}")
    elif plot_type == 'pie':
        # Ensure column1 has counts or frequencies for each category.  This is a simplified example.
        counts = df[column1].value_counts()
        plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
        plt.title(f"Pie Chart of {column1}")
    else:
        return "Error: Invalid plot type."

    # Save the plot to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()  # Close the plot to free memory

    # Embed the image in HTML
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f'<img src="" alt="Chart">'


def debug_sample(df):
    df_group1 = df.groupby(['Category'])['Area'].count()
    df_group1 = df_group1[df_group1 != 0]
    st.write(df_group1)


# Function definitions (from previous answers)
def aggregate_by_category_area(df: pd.DataFrame) -> Optional[pd.DataFrame]:
    """Groups DataFrame by category and area."""
    try:
        grouped_df = df.groupby(["Category", "Area"])["Quantity"].sum().reset_index()
        return grouped_df.to_html()
    except KeyError as e:
        print(f"Error: Column not found: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def aggregate_by_family_name(df: pd.DataFrame) -> Optional[pd.DataFrame]:
    """Groups DataFrame by Family Name."""
    try:
        grouped_df = df.groupby("Family Name")["Quantity"].sum().reset_index()
        return grouped_df.to_html()
    except KeyError as e:
        print(f"Error: Column not found: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# 1. Area Distribution

def area_distribution(df):
    """
    Displays a histogram of the area distribution of elements.

    Args:
        df (pd.DataFrame): DataFrame containing the 'Area' column.
    """

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['Area'].dropna(), bins=30, color='green', edgecolor='black', alpha=0.7)
    ax.set_title('Area Distribution of Elements')
    ax.set_xlabel('Area (sq. m)')
    ax.set_ylabel('Number of Elements')
    ax.grid(True)
    return fig


# 2. Top Families by Element Count
def family_name_distribution(df):
    """
    Displays a bar chart of the top 10 families by the number of elements.

    Args:
        df (pd.DataFrame): DataFrame containing the 'Family Name' column.
    """

    top_families = df['Family Name'].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(12, 6))
    top_families.plot(kind='bar', ax=ax, color='purple')
    ax.set_title('Top 10 Families by Number of Elements')
    ax.set_xlabel('Family')
    ax.set_ylabel('Number of Elements')
    ax.tick_params(axis='x', rotation=45)
    return fig


def plot_aggregate_by_category_area(df: pd.DataFrame) -> Optional[plt.Figure]:
    """Groups DataFrame by category and area and returns a bar chart."""
    try:
        grouped_df = df.groupby(["Category", "Area"])["Quantity"].sum().reset_index()

        # Create a combined Category-Area column for plotting
        grouped_df["Category-Area"] = grouped_df["Category"] + "-" + grouped_df["Area"]

        fig, ax = plt.subplots(figsize=(12, 6))  # Adjust figure size for better readability
        ax.bar(grouped_df["Category-Area"], grouped_df["Quantity"])  # Create bar chart

        ax.set_xlabel("Category - Area")
        ax.set_ylabel("Sum of Quantity")
        ax.set_title("Quantity by Category and Area")
        ax.tick_params(axis='x', rotation=45, ha='right')  # Rotate x-axis labels
        plt.tight_layout()

        return fig

    except KeyError as e:
        print(f"Error: Column not found: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def plot_aggregate_by_family_name(df: pd.DataFrame) -> Optional[plt.Figure]:
    """Groups DataFrame by Family Name and returns a bar chart."""
    try:
        grouped_df = df.groupby("Family Name")["Quantity"].sum().reset_index()

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(grouped_df["Family Name"], grouped_df["Quantity"])

        ax.set_xlabel("Family Name")
        ax.set_ylabel("Sum of Quantity")
        ax.set_title("Quantity by Family Name")
        ax.tick_params(axis='x', rotation=45, ha='right')  # Rotate x-axis labels
        plt.tight_layout()

        return fig

    except KeyError as e:
        print(f"Error: Column not found: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


general_columns = ["Category", "Area", "Family Name", "Quantity"]

neural_network_responses = {
    "Group data by category and area and sum the quantity": aggregate_by_category_area,
    "Aggregate quantity by family name": aggregate_by_family_name,
    "Create area Distribution": area_distribution,
    "Generate top families by element count": family_name_distribution,
}
