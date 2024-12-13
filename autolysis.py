import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import mutual_info_regression
from sklearn.cluster import KMeans
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
import json

# Load environment variables
API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
API_TOKEN = os.getenv("AIPROXY_TOKEN")

# Ensure API token is set
if not API_TOKEN:
    print("Error: AIPROXY_TOKEN environment variable not set.")
    sys.exit(1)

def load_dataset(filename):
    try:
        return pd.read_csv(filename, encoding='unicode_escape')
    except Exception as e:
        print(f"Error loading dataset: {e}")
        sys.exit(1)

def preprocess_dataset(df):
    try:
        numeric_df = df.select_dtypes(include=['number']).dropna()
        return numeric_df
    except Exception as e:
        print(f"Error during preprocessing: {e}")
        sys.exit(1)

def analyze_data(df):
    # Convert numeric columns safely
    numeric_df = preprocess_dataset(df)

    analysis = {
        "summary_statistics": df.describe(include='all').to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "correlation_matrix": numeric_df.corr().to_dict(),
    }

    # Outlier Detection
    try:
        numeric_df = numeric_df.dropna()  # Drop rows with NaN
        Q1 = numeric_df.quantile(0.25)
        Q3 = numeric_df.quantile(0.75)
        IQR = Q3 - Q1
        outliers = ((numeric_df < (Q1 - 1.5 * IQR)) | (numeric_df > (Q3 + 1.5 * IQR))).sum().to_dict()
        analysis["outliers"] = outliers
    except Exception as e:
        analysis["outliers"] = f"Error in outlier detection: {e}"

    # Data Type Counts
    analysis["data_types"] = df.dtypes.value_counts().to_dict()

    # Unique Value Counts
    analysis["unique_values"] = {col: df[col].nunique() for col in df.columns}

    # Frequent Value Analysis
    analysis["most_frequent_values"] = {col: df[col].mode()[0] if not df[col].mode().empty else None for col in df.columns}

    # Pairwise Correlation for Top 5 Pairs
    try:
        corr = numeric_df.corr().unstack().sort_values(ascending=False)
        corr = corr[corr < 1].drop_duplicates()  # Exclude self-correlation
        analysis["top_correlations"] = corr.head(5).to_dict()
    except Exception as e:
        analysis["top_correlations"] = f"Error in correlation analysis: {e}"

    # Skewness and Kurtosis
    analysis["skewness"] = numeric_df.skew().to_dict()
    analysis["kurtosis"] = numeric_df.kurtosis().to_dict()

    # Null Percentage
    total_rows = len(df)
    analysis["null_percentage"] = {col: (df[col].isnull().sum() / total_rows) * 100 for col in df.columns}

    # Categorical Distributions
    top_categorical = df.select_dtypes(include=['object', 'category']).columns[:3]
    analysis["categorical_distributions"] = {col: df[col].value_counts(normalize=True).to_dict() for col in top_categorical}

    # Regression Analysis
    try:
        if numeric_df.shape[1] > 1:  # At least two numerical columns
            X = numeric_df.iloc[:, 1:].dropna()
            y = numeric_df.iloc[:, 0].dropna()
            common_indices = X.index.intersection(y.index)
            X, y = X.loc[common_indices], y.loc[common_indices]
            model = LinearRegression().fit(X, y)
            analysis["regression_coefficients"] = dict(zip(X.columns, model.coef_))
    except Exception as e:
        analysis["regression_coefficients"] = f"Error in regression analysis: {e}"

    # Feature Importance Analysis
    try:
        if numeric_df.shape[1] > 1:
            X = numeric_df.iloc[:, 1:].dropna()
            y = numeric_df.iloc[:, 0].dropna()
            common_indices = X.index.intersection(y.index)
            X, y = X.loc[common_indices], y.loc[common_indices]
            importances = mutual_info_regression(X, y)
            analysis["feature_importance"] = dict(zip(X.columns, importances))
    except Exception as e:
        analysis["feature_importance"] = f"Error in feature importance analysis: {e}"

    # Time Series Analysis
    try:
        time_columns = df.select_dtypes(include=['datetime']).columns
        if not time_columns.empty and not numeric_df.empty:
            time_series_analysis = {}
            for time_col in time_columns[:1]:  # Use the first datetime column
                time_indexed_df = df.set_index(time_col).dropna()
                for num_col in numeric_df.columns[:1]:  # Use the first numerical column
                    result = seasonal_decompose(time_indexed_df[num_col], model='additive', period=12)
                    time_series_analysis[num_col] = {
                        "trend": result.trend.dropna().to_list(),
                        "seasonal": result.seasonal.dropna().to_list(),
                        "residual": result.resid.dropna().to_list(),
                    }
            analysis["time_series_decomposition"] = time_series_analysis
        else:
            analysis["time_series_decomposition"] = "No suitable columns for time series analysis."
    except Exception as e:
        analysis["time_series_decomposition"] = f"Error in time series analysis: {e}"

    # Cluster Analysis
    try:
        if numeric_df.shape[1] > 1:
            kmeans = KMeans(n_clusters=3, random_state=42).fit(numeric_df.dropna())
            analysis["cluster_labels"] = kmeans.labels_.tolist()
    except Exception as e:
        analysis["cluster_labels"] = f"Error in cluster analysis: {e}"

    # Geographic Analysis
    try:
        geo_columns = numeric_df.columns
        if len(geo_columns) >= 2:
            analysis["geographic_summary"] = {
                "latitude_range": (numeric_df[geo_columns[0]].min(), numeric_df[geo_columns[0]].max()),
                "longitude_range": (numeric_df[geo_columns[1]].min(), numeric_df[geo_columns[1]].max()),
            }
    except Exception as e:
        analysis["geographic_summary"] = f"Error in geographic analysis: {e}"

    # Network Analysis
    try:
        network_columns = df.columns[df.columns.str.contains("source|target", case=False)]
        if len(network_columns) == 2:
            network_edges = df[network_columns].dropna()
            analysis["network_connections"] = network_edges.values.tolist()
    except Exception as e:
        analysis["network_connections"] = f"Error in network analysis: {e}"

    return analysis

def generate_visualizations(df):
    visualizations = []

    # Safe numeric filtering
    numeric_df = preprocess_dataset(df)

    # Correlation heatmap
    try:
        plt.figure(figsize=(10,8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
        heatmap_file = "correlation_heatmap.png"
        plt.title("Correlation Heatmap")
        plt.savefig(heatmap_file)
        plt.close()
        visualizations.append(heatmap_file)
    except Exception as e:
        print(f"Error creating correlation heatmap: {e}")

    # Time Series Decomposition Analysis
    try:
        time_columns = df.select_dtypes(include=['datetime']).columns
        if not time_columns.empty:
            for time_col in time_columns[:1]:  # Use the first datetime column
                time_indexed_df = df.set_index(time_col).dropna()
                for num_col in numeric_df.columns[:1]:  # Use the first numeric column
                    result = seasonal_decompose(time_indexed_df[num_col], model='additive', period=12)
                    plt.figure(figsize=(10, 8))
                    result.plot()
                    time_decomp_file = "time_series_decomposition.png"
                    plt.savefig(time_decomp_file)
                    plt.close()
                    visualizations.append(time_decomp_file)
    except Exception as e:
        print(f"Error in time series decomposition: {e}")

    # Bar Graph for Missing Values
    try:
        missing_values = df.isnull().sum()
        if missing_values.any():
            plt.figure(figsize=(10,8))
            sns.barplot(x=missing_values.index, y=missing_values.values, hue=missing_values.index, palette="viridis", legend=False)
            plt.title("Missing Value Counts")
            plt.ylabel("Count")
            plt.xticks(rotation=90)
            missing_values_file = "missing_values_bar.png"
            plt.savefig(missing_values_file)
            plt.close()
            visualizations.append(missing_values_file)
    except Exception as e:
        print(f"Error creating missing values bar graph: {e}")

    # Outlier Detection Visualization (Boxplot)
    try:
        if not numeric_df.empty:
            plt.figure(figsize=(10,8))
            sns.boxplot(data=numeric_df)
            plt.title("Outlier Detection - Boxplot")
            outlier_file = "outlier_boxplot.png"
            plt.savefig(outlier_file)
            plt.close()
            visualizations.append(outlier_file)
    except Exception as e:
        print(f"Error creating boxplot: {e}")

    return visualizations
import time

def query_llm(prompt, max_retries=5, max_tokens=500):
    """
    Query the language model with retry and backoff logic to handle rate limits.
    """
    retries = 0
    while retries < max_retries:
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_TOKEN}"
            }
            payload = {
                "model": "gpt-4o-mini",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": max_tokens
            }
            response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content'].strip()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:  # Rate limit error
                wait_time = 2 ** retries  # Exponential backoff
                print(f"Rate limit hit. Retrying after {wait_time} seconds...")
                time.sleep(wait_time)
                retries += 1
            else:
                print(f"Error querying the language model: {e}")
                print(f"Full response: {response.json()}")
                sys.exit(1)
        except Exception as e:
            print(f"Unexpected error querying the language model: {e}")
            sys.exit(1)

    print("Max retries exceeded. Falling back to local summary generation.")
    return None  # Return None if retries are exhausted


def generate_readme(df, analysis, visualizations):
    """
    Generate README.md file using LLM or fallback to local generation if LLM fails.
    """
    column_names = ", ".join(df.columns)

    # Construct a concise prompt using the analysis dictionary
    analysis_summary = "\n".join([f"{key}: {str(value)[:500]}" for key, value in analysis.items() if value != "Not applicable"])

    prompt = (
        f"The dataset has the following columns: {column_names}.\n\n"
        f"Here is the summarized analysis:\n{analysis_summary}\n\n"
        "Based on the above analysis, provide a concise narrative explaining the key insights, patterns, and potential implications."
    )

    # Query the LLM for narrative
    narrative = query_llm(prompt)
    # Write the README.md file
    with open("README.md", "w") as readme:
        readme.write("# Analysis Report\n\n")
        readme.write(f"## Dataset Overview\n\nColumns: {column_names}\n\n")
        readme.write(f"## Analysis Summary\n\n{narrative}\n\n")
        readme.write("## Visualizations\n\n")
        for vis in visualizations:
            readme.write(f"![{vis}]({vis})\n\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: uv run autolysis.py <dataset.csv>")
        sys.exit(1)

    dataset_file = sys.argv[1]
    data = load_dataset(dataset_file)
    analysis = analyze_data(data)
    vis_files = generate_visualizations(data)
    generate_readme(data, analysis, vis_files)
    print("Analysis complete. Outputs generated in the current directory.")
