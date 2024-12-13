import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
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
            "summary_statistics": df.describe(include='all').fillna('').to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
            "unique_values": {col: df[col].nunique() for col in df.columns},
            "most_frequent_values": {col: df[col].mode().iloc[0] if not df[col].mode().empty else None for col in df.columns},
        }
        if len(df.select_dtypes(include=['number']).columns) > 1:
            summary["correlation_matrix"] = df.select_dtypes(include=['number']).corr().to_dict()
        return df, summary
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        sys.exit(1)

# Function to dynamically interact with the language model
def query_llm(prompt):
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
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error querying the language model: {e}")
        sys.exit(1)

# Function to preprocess the dataset
def preprocess_dataset(df):
    try:
        numeric_df = df.select_dtypes(include=['number']).dropna()
        return numeric_df
    except Exception as e:
        print(f"Error during preprocessing: {e}")
        sys.exit(1)

# Function for missing data analysis
def analyze_missing_data(df):
    return df.isnull().sum().to_dict()

# Function for outlier detection
def detect_outliers(df):
    try:
        numeric_df = preprocess_dataset(df)
        iso = IsolationForest(contamination=0.05, random_state=42)
        numeric_df['outliers'] = iso.fit_predict(numeric_df)
        return numeric_df[numeric_df['outliers'] == -1], numeric_df[numeric_df['outliers'] == 1]
    except Exception as e:
        print(f"Error detecting outliers: {e}")
        return None, None

# Function for clustering
def perform_clustering(df, n_clusters=3):
    try:
        numeric_df = preprocess_dataset(df)
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        numeric_df['cluster'] = kmeans.fit_predict(numeric_df)
        return numeric_df
    except Exception as e:
        print(f"Error performing clustering: {e}")
        return df

# Function for hypothesis testing
def hypothesis_testing(df, column1, column2):
    try:
        stat, p_value = ttest_ind(df[column1].dropna(), df[column2].dropna())
        return {"t_statistic": stat, "p_value": p_value}
    except Exception as e:
        print(f"Error performing hypothesis testing: {e}")
        return None

# Function for time series analysis
def time_series_analysis(df, column):
    try:
        decomposition = seasonal_decompose(df[column], model='additive', period=12)
        result = {
            "trend": decomposition.trend,
            "seasonal": decomposition.seasonal,
            "residual": decomposition.resid
        }
        return result
    except Exception as e:
        print(f"Error during time series analysis: {e}")
        return None
# Function to generate visualizations based on the analyses
def generate_visualizations(df, outliers=None, time_series_result=None, clustered_df=None):
    visuals = []

    # Correlation Matrix Heatmap
    try:
        numeric_df = preprocess_dataset(df)
        correlation_matrix = numeric_df.corr()
        heatmap = sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
        heatmap.set_title("Correlation Matrix of All Numerical Variables")
        correlation_matrix_path = "correlation_matrix.png"
        heatmap.get_figure().savefig(correlation_matrix_path)
        heatmap.get_figure().clf()  # Clear the figure
        visuals.append(correlation_matrix_path)
    except Exception as e:
        print(f"Error generating correlation matrix heatmap: {e}")

    # Missing Values Visualization
    # Missing Values Visualization
    try:
        missing_data = df.isnull().sum()
        barplot = sns.barplot(
            x=missing_data.index,
            y=missing_data.values,
            hue=missing_data.index,  # Fix for deprecation warning
            palette="Blues_d",
            dodge=False,
            legend=False
        )
        barplot.set_title("Missing Values per Column")
        barplot.set_ylabel("Number of Missing Values")
        barplot.set_xticks(range(len(missing_data.index)))  # Explicitly set ticks
        barplot.set_xticklabels(missing_data.index, rotation=45, horizontalalignment='right')  # Fix for tick warning
        barplot.get_figure().savefig("missing_values.png")
        barplot.get_figure().clf()  # Clear the figure
        visuals.append("missing_values.png")
    except Exception as e:
        print(f"Error generating missing values bar chart: {e}")


    # Outliers Visualization (if detected)
    if outliers is not None:
        try:
            scatter = sns.scatterplot(x=outliers.index, y=outliers.iloc[:, 0], color="red", label="Outliers")
            scatter.set_title("Detected Outliers")
            scatter.set_xlabel("Index")
            scatter.set_ylabel("Values")
            outliers_path = "outliers.png"
            scatter.get_figure().savefig(outliers_path)
            scatter.get_figure().clf()  # Clear the figure
            visuals.append(outliers_path)
        except Exception as e:
            print(f"Error generating outliers scatter plot: {e}")

    # Time Series Analysis (if performed)
    if time_series_result is not None:
        try:
            trend = sns.lineplot(data=time_series_result['trend'], label="Trend", color="blue")
            seasonal = sns.lineplot(data=time_series_result['seasonal'], label="Seasonal", color="orange")
            residual = sns.lineplot(data=time_series_result['residual'], label="Residual", color="green")
            trend.set_title("Time Series Decomposition")
            trend.set_xlabel("Time")
            trend.set_ylabel("Values")
            time_series_path = "time_series_analysis.png"
            trend.get_figure().savefig(time_series_path)
            trend.get_figure().clf()  # Clear the figure
            visuals.append(time_series_path)
        except Exception as e:
            print(f"Error generating time series analysis plot: {e}")

    # Cluster Analysis Visualization
    if clustered_df is not None:
        try:
            cluster_plot = sns.scatterplot(
                x=clustered_df.iloc[:, 0],
                y=clustered_df.iloc[:, 1],
                hue=clustered_df['cluster'],
                palette="viridis",
                s=100
            )
            cluster_plot.set_title("Clustering Results")
            cluster_plot.set_xlabel(clustered_df.columns[0])
            cluster_plot.set_ylabel(clustered_df.columns[1])
            cluster_path = "cluster_analysis.png"
            cluster_plot.get_figure().savefig(cluster_path)
            cluster_plot.get_figure().clf()  # Clear the figure
            visuals.append(cluster_path)
        except Exception as e:
            print(f"Error generating clustering plot: {e}")

    return visuals

#Function to craft context-rich prompts for the LLM
def create_llm_prompt(summary, visuals):
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

    # Formatting for the Insights
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

    # Combining both prompts into a final one
    return data_description + "\n\n" + insights_prompt


# write_markdown function
def write_markdown_v2(summary, visuals, insights):
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

    with open("README.md", "w") as f:
        f.write(content)


# Main execution flow with the revised approach
def main_v2():
    if len(sys.argv) != 2:
        print("Usage: python autolysis.py <dataset.csv>")
        sys.exit(1)

    dataset_path = sys.argv[1]

    # Load and summarize the dataset
    df, summary = load_and_summarize_csv(dataset_path)

    # Perform missing data analysis
    summary['missing_data_analysis'] = analyze_missing_data(df)

    # Detect outliers
    outliers, inliers = detect_outliers(df)
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
    prompt = create_llm_prompt(summary, [])
    insights = query_llm(prompt)

   # Generate visualizations
    visuals = generate_visualizations(df, outliers=outliers, time_series_result= summary['time_series_analysis'], clustered_df=clustered_df)

    # Write results to Markdown
    write_markdown_v2(summary, visuals, insights)

    print("Analysis complete. Output saved to README.md and visualization files.")

if __name__ == "__main__":
    main_v2()