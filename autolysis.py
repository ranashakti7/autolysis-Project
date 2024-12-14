"""
Autolysis.py

This module provides an automated pipeline for analyzing datasets, generating insights,
and creating visualizations. It includes functions for:
- Outlier detection
- Clustering
- Hypothesis testing
- Time series analysis
- Visualizations for correlation matrices, missing values, outliers, clustering results, and more

The results are summarized and saved as a Markdown file, accompanied by relevant visualizations.
"""
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pandas",              # For data manipulation and analysis.
#   "matplotlib",          # For generating visualizations.
#   "seaborn",             # For advanced statistical visualizations.
#   "requests",            # For making API calls.
#   "scikit-learn",        # For machine learning operations (IsolationForest, KMeans, etc.).
#   "scipy",               # For statistical tests (e.g., t-tests).
#   "statsmodels",         # For time series analysis (e.g., seasonal decomposition).
#   "tabulate"
# ]
# ///

# autolysis.py
# Python script for data analysis and visualization.

import os
import sys
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
from scipy.stats import ttest_ind
from statsmodels.tsa.seasonal import seasonal_decompose

# Setup AI Proxy API
API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
API_TOKEN = os.getenv("AIPROXY_TOKEN")

# Function to load and summarize CSV file
def load_and_summarize_csv(file_path):
    """Load a CSV file and summarize its contents."""
    try:
        df = pd.read_csv(file_path, encoding='unicode_escape')

        summary = {
            "shape": df.shape,
            "columns": df.columns.tolist(),
            "types": df.dtypes.astype(str).to_dict(),
            "summary_statistics": df.describe(include='all').fillna('').to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
            "unique_values": {
                col: df[col].nunique() for col in df.columns
            },
            "most_frequent_values": {
                col: (df[col].mode().iloc[0] if not df[col].mode().empty else None)
                for col in df.columns
            },
        }

        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 1:
            summary["correlation_matrix"] = df[numeric_cols].corr().to_dict()

        return df, summary

    except (FileNotFoundError, pd.errors.ParserError) as e:
        print(f"Error loading CSV file: {e}")
        sys.exit(1)

# Function to dynamically interact with the language model
def query_llm(prompt):
    """Send a query to the language model and return the response."""
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_TOKEN}"
        }
        payload = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 500
        }
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload), timeout=10)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except (requests.exceptions.RequestException, KeyError) as e:
        print(f"Error querying the language model: {e}")
        sys.exit(1)
# Function to preprocess the dataset
def preprocess_dataset(df):
    """Filter numeric columns and drop rows with missing values."""
    try:
        return df.select_dtypes(include=['number']).dropna()
    except KeyError as e:
        print(f"Error during preprocessing: {e}")
        sys.exit(1)

# Function for missing data analysis
def analyze_missing_data(df):
    """Analyze missing data in the dataset."""
    return df.isnull().sum().to_dict()

# Function for outlier detection
def detect_outliers(df):
    """Identify outliers using the Isolation Forest algorithm."""
    try:
        numeric_df = preprocess_dataset(df)
        iso = IsolationForest(contamination=0.05, random_state=42)
        numeric_df['outliers'] = iso.fit_predict(numeric_df)
        return numeric_df[numeric_df['outliers'] == -1]
    except ValueError as e:
        print(f"Error detecting outliers: {e}")
        return None
# Function for clustering
def perform_clustering(df, n_clusters=3):
    """Perform clustering using KMeans."""
    try:
        numeric_df = preprocess_dataset(df)
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        numeric_df['cluster'] = kmeans.fit_predict(numeric_df)
        return numeric_df
    except ValueError as e:
        print(f"Error performing clustering: {e}")
        return df

# Function for hypothesis testing
def hypothesis_testing(df, column1, column2):
    """Conduct a t-test between two columns."""
    try:
        stat, p_value = ttest_ind(df[column1].dropna(), df[column2].dropna())
        return {"t_statistic": stat, "p_value": p_value}
    except (KeyError, ValueError) as e:
        print(f"Error performing hypothesis testing: {e}")
        return None

# Function for time series analysis
def time_series_analysis(df, column):
    """Perform time series decomposition on a specified column."""
    try:
        decomposition = seasonal_decompose(df[column], model='additive', period=12)
        return {
            "trend": decomposition.trend,
            "seasonal": decomposition.seasonal,
            "residual": decomposition.resid
        }
    except ValueError as e:
        print(f"Error during time series analysis: {e}")
        return None

# Functions to generate visualizations based on the analyses

def generate_correlation_heatmap(df, visuals):
    """Generate and save a correlation matrix heatmap."""
    try:
        numeric_df = preprocess_dataset(df)
        correlation_matrix = numeric_df.corr()
        plt.figure(figsize=(12, 10))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
        correlation_matrix_path = 'correlation_matrix.png'
        plt.title('Correlation Matrix of All Numerical Variables')
        plt.savefig(correlation_matrix_path)
        plt.close()
        visuals.append(correlation_matrix_path)
    except ValueError as e:
        print(f"Error generating correlation matrix heatmap: {e}")


def generate_missing_values_chart(df, visuals):
    """Generate and save a bar chart for missing values."""
    try:
        missing_data = df.isnull().sum()
        if missing_data.sum() > 0:
            plt.figure(figsize=(12, 6))
            missing_data.plot(kind='bar', color='skyblue')
            plt.title('Missing Values per Column')
            plt.ylabel('Number of Missing Values')
            missing_values_path = 'missing_values.png'
            plt.savefig(missing_values_path)
            plt.close()
            visuals.append(missing_values_path)
    except ValueError as e:
        print(f"Error generating missing values bar chart: {e}")


def generate_outliers_plot(outliers, visuals):
    """Generate and save a scatter plot for outliers."""
    if outliers is not None:
        try:
            plt.figure(figsize=(12, 6))
            plt.scatter(outliers.index, outliers.iloc[:, 0], color='red', label='Outliers')
            plt.title('Detected Outliers')
            plt.xlabel('Index')
            plt.ylabel('Values')
            outliers_path = 'outliers.png'
            plt.legend()
            plt.savefig(outliers_path)
            plt.close()
            visuals.append(outliers_path)
        except ValueError as e:
            print(f"Error generating outliers scatter plot: {e}")


def generate_time_series_plot(time_series_result, visuals):
    """Generate and save a time series decomposition plot."""
    if time_series_result is not None:
        try:
            plt.figure(figsize=(12, 6))
            plt.plot(time_series_result['trend'], label='Trend', color='blue')
            plt.plot(time_series_result['seasonal'], label='Seasonal', color='orange')
            plt.plot(time_series_result['residual'], label='Residual', color='green')
            plt.title('Time Series Decomposition')
            plt.xlabel('Time')
            plt.ylabel('Values')
            time_series_path = 'time_series_analysis.png'
            plt.legend()
            plt.savefig(time_series_path)
            plt.close()
            visuals.append(time_series_path)
        except ValueError as e:
            print(f"Error generating time series analysis plot: {e}")


def generate_cluster_plot(clustered_df, visuals):
    """Generate and save a scatter plot for clustering analysis."""
    if clustered_df is not None:
        try:
            plt.figure(figsize=(12, 6))
            sns.scatterplot(
                x=clustered_df.iloc[:, 0],
                y=clustered_df.iloc[:, 1],
                hue=clustered_df['cluster'],
                palette='viridis',
                s=100
            )
            plt.title('Clustering Results')
            plt.xlabel(clustered_df.columns[0])
            plt.ylabel(clustered_df.columns[1])
            cluster_path = 'cluster_analysis.png'
            plt.legend()
            plt.savefig(cluster_path)
            plt.close()
            visuals.append(cluster_path)
        except Exception as e:
            print(f"Error generating clustering plot: {e}")


def generate_visualizations(df, outliers=None, time_series_result=None, clustered_df=None):
    """
    Create and save visualizations for the data analysis.
    
    Args:
        df (pd.DataFrame): The dataset for analysis.
        outliers (pd.DataFrame, optional): Dataframe of outliers if detected.
        time_series_result (dict, optional): Time series decomposition results.
        clustered_df (pd.DataFrame, optional): Clustered dataframe with cluster labels.
    
    Returns:
        list: A list of file paths to the saved visualizations.
    """
    visuals = []

    generate_correlation_heatmap(df, visuals)
    generate_missing_values_chart(df, visuals)
    generate_outliers_plot(outliers, visuals)
    generate_time_series_plot(time_series_result, visuals)
    generate_cluster_plot(clustered_df, visuals)

    return visuals

# Function to craft context-rich prompts for the LLM
def create_llm_prompt(summary):
    """
    Generate a prompt for querying a large language model (LLM) based on dataset analysis summary.
    
    Args:
        summary (dict): A dictionary containing dataset analysis results, including types, 
                        summary statistics, missing values, outlier count, correlation matrix, 
                        and time-series analysis results.

    Returns:
        str: A formatted prompt string to provide to the LLM.
    """
    data_description = f"""The dataset contains the following columns and types:
    {json.dumps(summary['types'], indent=2)}

    Summary statistics of the dataset are:
    {pd.DataFrame(summary['summary_statistics']).to_markdown()}

    Missing values in the dataset:
    {pd.Series(summary['missing_values']).to_markdown()}

    Outlier count: {summary.get('outlier_count', 'N/A')}
    
    Correlation matrix of numerical features:
    {json.dumps(summary.get('correlation_matrix', {}))}

    Time series analysis results:
    {summary.get('time_series_analysis', 'N/A')}
    
    The dataset was analyzed using multiple techniques, including:
    - Outlier detection using Isolation Forest
    - KMeans clustering for pattern discovery
    - Hypothesis testing on numerical columns
    - Time-series decomposition of the first numeric column

    Please provide actionable insights from this analysis. Highlight any interesting correlations, clusters, or trends you find. Additionally, suggest implications for future data exploration or business decisions.
    """

    insights_prompt = f"""Based on the analysis performed on the dataset, here are some insights:
    - Insights on correlations between variables
    - Outliers detected and their possible implications
    - Significant clusters discovered through KMeans
    - Results from hypothesis testing (statistical significance)
    - Key findings from time-series decomposition

    Also, please make sure to:
    - Include recommendations on data cleaning and potential improvements.
    - Emphasize the most significant findings with explanations on how they might impact the overall data trends.

    Include visualizations in your analysis to help reinforce key findings.
    """

    return data_description + "\n\n" + insights_prompt

def write_markdown_v2(summary, visuals, insights):
    """
    Write dataset analysis results and insights into a Markdown file.

    Args:
        summary (dict): A dictionary containing dataset summary and analysis results.
        visuals (list): A list of file paths to visualizations created during the analysis.
        insights (str): Key insights derived from the analysis.
    """
    content = f"""# Dataset Analysis

## Data Overview

### Shape of Dataset:
{summary['shape']}

### Columns and Types:
{json.dumps(summary['types'], indent=2)}

### Summary Statistics:
{pd.DataFrame(summary['summary_statistics']).to_markdown()}

### Missing Values:
{pd.Series(summary['missing_values']).to_markdown()}

## Analysis

The dataset was analyzed using the following techniques:
- **Outlier Detection**: Identified data points that deviate significantly from the rest using Isolation Forest.
- **Clustering**: Grouped the data into clusters using KMeans.
- **Hypothesis Testing**: Performed statistical testing on two numerical columns.
- **Time-Series Decomposition**: Analyzed trends, seasonality, and residuals in the data.

## Insights and Implications

{insights}

## Visualizations

The following visualizations were created to enhance the understanding of the data and the findings:
"""
    for visual in visuals:
        content += f"![Visualization]({visual})\n\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

def main_v2():
    """
    Main function to execute the dataset analysis workflow.
    
    Steps include:
    - Loading and summarizing the dataset
    - Performing missing data analysis, outlier detection, clustering, hypothesis testing,
      and time-series analysis
    - Querying an LLM for insights
    - Generating visualizations
    - Writing results to a Markdown file
    """
    if len(sys.argv) != 2:
        print("Usage: python autolysis.py <dataset.csv>")
        sys.exit(1)

    dataset_path = sys.argv[1]

    # Load and summarize the dataset
    df, summary = load_and_summarize_csv(dataset_path)

    # Perform missing data analysis
    summary['missing_data_analysis'] = analyze_missing_data(df)

    # Detect outliers
    outliers = detect_outliers(df)
    if outliers is not None:
        summary['outlier_count'] = len(outliers)

    # Perform clustering
    clustered_df = perform_clustering(df)

    # Hypothesis testing (example on first two numeric columns)
    numeric_columns = df.select_dtypes(include=['number']).columns
    if len(numeric_columns) >= 2:
        col1, col2 = numeric_columns[:2]
        summary['hypothesis_test'] = hypothesis_testing(df, col1, col2)

    # Time series analysis (example on the first numeric column)
    if len(numeric_columns) >= 1:
        time_series_col = numeric_columns[0]
        summary['time_series_analysis'] = time_series_analysis(df, time_series_col)

    # Query the LLM for insights with the revised prompt
    prompt = create_llm_prompt(summary)
    insights = query_llm(prompt)

    # Generate visualizations
    visuals = generate_visualizations(
        df,
        outliers=outliers,
        time_series_result=summary['time_series_analysis'],
        clustered_df=clustered_df
    )
    # Write results to Markdown
    write_markdown_v2(summary, visuals, insights)

    print("Analysis complete. Output saved to README.md and visualization files.")

if __name__ == "__main__":
    main_v2()
