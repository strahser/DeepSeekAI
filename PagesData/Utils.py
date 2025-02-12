from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import seaborn as sns  # For better plot styling
import io
import base64


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
        return grouped_df
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
        return grouped_df
    except KeyError as e:
        print(f"Error: Column not found: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def plot_family_name_distribution(df: pd.DataFrame) -> Optional[plt.Figure]:
    """Creates a distribution plot of quantity by Family Name."""
    try:
        if "Family Name" not in df.columns:
            raise KeyError("Column 'Family Name' not found in DataFrame")
        if "Quantity" not in df.columns:
            raise KeyError("Column 'Quantity' not found in DataFrame")
        family_quantities = df.groupby("Family Name")["Quantity"].sum()
        fig, ax = plt.subplots(figsize=(10, 6))
        family_quantities.plot(kind="bar", ax=ax)
        ax.set_title("Distribution of Quantity by Family Name")
        ax.set_xlabel("Family Name")
        ax.set_ylabel("Sum of Quantity")
        ax.tick_params(axis='x', rotation=45, labelsize=10)
        plt.tight_layout()
        return fig
    except KeyError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def plot_category_distribution(df: pd.DataFrame) -> Optional[plt.Figure]:
    """Creates a distribution plot of quantity by Category."""
    try:
        if "Category" not in df.columns:
            raise KeyError("Column 'Category' not found in DataFrame")
        if "Quantity" not in df.columns:
            raise KeyError("Column 'Quantity' not found in DataFrame")
        category_quantities = df.groupby("Category")["Quantity"].sum()
        fig, ax = plt.subplots(figsize=(10, 6))
        category_quantities.plot(kind="bar", ax=ax)
        ax.set_title("Distribution of Quantity by Category")
        ax.set_xlabel("Category")
        ax.set_ylabel("Sum of Quantity")
        ax.tick_params(axis='x', rotation=45, labelsize=10)
        plt.tight_layout()
        return fig
    except KeyError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

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
general_columns = ["Category","Area","Family Name","Quantity"]

neural_network_responses = {
    "Group data by category and area and sum the quantity": aggregate_by_category_area,
    "Aggregate quantity by family name": aggregate_by_family_name,
    "Create a distribution plot of quantity by family name": plot_family_name_distribution,
    "Generate a distribution plot of quantity by category": plot_category_distribution,
}