import os
import sys
import pandas as pd
import seaborn as sns
import requests
import json
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import cross_val_score
from scipy.stats import ttest_ind
from statsmodels.tsa.seasonal import seasonal_decompose

# Setup AI Proxy API
API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
API_TOKEN = os.getenv("AIPROXY_TOKEN")

# Function to load and summarize CSV file
def load_and_summarize_csv(file_path):
    try:
        df = pd.read_csv(file_path, encoding='unicode_escape')
        summary = {
            "shape": df.shape,
            "columns": df.columns.tolist(),
            "types": df.dtypes.astype(str).to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
        }
        if len(df.select_dtypes(include=['number']).columns) > 1:
            summary["correlation_matrix"] = df.select_dtypes(include=['number']).corr().to_dict()
        return df, summary
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        sys.exit(1)

# Function to preprocess the dataset
def preprocess_dataset(df):
    try:
        numeric_df = df.select_dtypes(include=['number']).dropna()
        return numeric_df
    except Exception as e:
        print(f"Error during preprocessing: {e}")
        sys.exit(1)

# Function to dynamically interact with the language model
def query_llm(summary):
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_TOKEN}"
        }
        prompt = f"""
        Dataset Analysis Summary:
        - Shape: {summary.get('shape')}
        - Columns and Types: {summary.get('types')}
        - Missing Values: {summary.get('missing_values')}
        - Correlation Matrix: {json.dumps(summary.get('correlation_matrix', {}))}
        
        Provide actionable insights from this analysis. Highlight correlations, clusters, or trends and recommend improvements for future analyses.
        """
        payload = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt.strip()}],
            "max_tokens": 300
        }
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error querying the language model: {e}")
        return "Insights could not be generated due to API errors."

# Function to generate visualizations
def generate_visualizations(df, summary):
    visuals = []

    # Correlation Matrix Heatmap
    try:
        numeric_df = preprocess_dataset(df)
        if not numeric_df.empty:
            correlation_matrix = numeric_df.corr()
            sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5).get_figure().savefig("correlation_matrix.png")
            visuals.append("correlation_matrix.png")
    except Exception as e:
        print(f"Error generating correlation matrix heatmap: {e}")

    # Missing Values Visualization
    try:
        missing_data = pd.Series(summary['missing_values'])
        missing_data.plot(kind='bar', color='skyblue', title='Missing Values').get_figure().savefig("missing_values.png")
        visuals.append("missing_values.png")
    except Exception as e:
        print(f"Error generating missing values visualization: {e}")

    return visuals

# Function to write the analysis report to README.md
def write_readme(summary, insights, visuals):
    content = f"""
    # Dataset Analysis Report

    ## Data Overview
    - **Shape**: {summary['shape']}
    - **Columns and Types**: {json.dumps(summary['types'], indent=2)}
    - **Missing Values**: {json.dumps(summary['missing_values'], indent=2)}

    ## Insights
    {insights}

    ## Visualizations
    """
    for visual in visuals:
        content += f"![Visualization]({visual})\n\n"

    with open("README.md", "w") as f:
        f.write(content)

# Main Function
def main():
    if len(sys.argv) != 2:
        print("Usage: python autolysis.py <dataset.csv>")
        sys.exit(1)

    dataset_path = sys.argv[1]

    # Load and summarize the dataset
    df, summary = load_and_summarize_csv(dataset_path)

    # Query LLM for insights
    insights = query_llm(summary)

    # Generate visualizations
    visuals = generate_visualizations(df, summary)

    # Write the report
    write_readme(summary, insights, visuals)
    print("Analysis complete. Output saved to README.md and visualizations.")

if __name__ == "__main__":
    main()
