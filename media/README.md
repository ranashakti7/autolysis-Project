# Dataset Analysis

## Data Overview

### Shape of Dataset:
(2652, 8)

### Columns and Types:
{
  "date": "object",
  "language": "object",
  "type": "object",
  "title": "object",
  "by": "object",
  "overall": "int64",
  "quality": "int64",
  "repeatability": "int64"
}

### Summary Statistics:
|        | date      | language   | type   | title             | by                | overall            | quality            | repeatability      |
|:-------|:----------|:-----------|:-------|:------------------|:------------------|:-------------------|:-------------------|:-------------------|
| count  | 2553      | 2652       | 2652   | 2652              | 2390              | 2652.0             | 2652.0             | 2652.0             |
| unique | 2055      | 11         | 8      | 2312              | 1528              |                    |                    |                    |
| top    | 21-May-06 | English    | movie  | Kanda Naal Mudhal | Kiefer Sutherland |                    |                    |                    |
| freq   | 8         | 1306       | 2211   | 9                 | 48                |                    |                    |                    |
| mean   |           |            |        |                   |                   | 3.0475113122171944 | 3.2092760180995477 | 1.4947209653092006 |
| std    |           |            |        |                   |                   | 0.7621797580962717 | 0.7967426636666686 | 0.598289430580212  |
| min    |           |            |        |                   |                   | 1.0                | 1.0                | 1.0                |
| 25%    |           |            |        |                   |                   | 3.0                | 3.0                | 1.0                |
| 50%    |           |            |        |                   |                   | 3.0                | 3.0                | 1.0                |
| 75%    |           |            |        |                   |                   | 3.0                | 4.0                | 2.0                |
| max    |           |            |        |                   |                   | 5.0                | 5.0                | 3.0                |

### Missing Values:
|               |   0 |
|:--------------|----:|
| date          |  99 |
| language      |   0 |
| type          |   0 |
| title         |   0 |
| by            | 262 |
| overall       |   0 |
| quality       |   0 |
| repeatability |   0 |

## Analysis

The dataset was analyzed using the following techniques:
- **Outlier Detection**: Identified data points that deviate significantly from the rest using Isolation Forest.
- **Clustering**: Grouped the data into clusters using KMeans.
- **Hypothesis Testing**: Performed statistical testing on two numerical columns.
- **Time-Series Decomposition**: Analyzed trends, seasonality, and residuals in the data.

## Insights and Implications

### Actionable Insights from Data Analysis

Based on the analysis of the dataset, several insights can be derived regarding correlations, outliers, clusters, and trends. Here are the highlights:

#### 1. Correlation Insights

- **Strong Correlation Between Overall and Quality**: The correlation coefficient of 0.83 suggests a strong relationship between the overall ratings and quality scores. This implies that as the quality rating improves, so does the overall rating. Businesses should focus on quality improvement as it directly impacts customer satisfaction.

- **Moderate Correlation Between Overall and Repeatability**: The correlation of 0.51 indicates a moderate relationship between overall satisfaction and repeatability. This suggests that having a repeatable experience may contribute positively to the overall perception of the dataset's subjects (e.g., movies, products). 

- **Quality vs. Repeatability Weak Correlation**: The weak correlation (0.31) indicates that although quality impacts overall satisfaction, it does not significantly affect repeatability. This might suggest that consumers can find value in the content even if the quality varies.

#### 2. Outliers Detected

- **116 Outliers**: The presence of outliers could be significant in understanding anomalies or exceptional cases that deviate from the norm in ratings. 
  - **Implications**:
    - Investigate these outliers to understand their characteristics and whether they are due to a unique content quality or perhaps fraudulent reviews.
    - Cleaning the dataset by assessing whether to keep or remove outliers could provide more robustness to any predictive modeling approaches.

#### 3. Clustering Insights

- **Significant Clusters from KMeans**: Depending on how many clusters were generated, finding distinct groups in the data may reveal particular audiences or trends in content categorization.
  - **Recommendations**: Visual outputs (like scatter plots or cluster centers) should be employed to better understand these groups and strategize targeted marketing or content creation tailored to these distinct segments.

#### 4. Hypothesis Testing Results

- **Statistical Significance**: If hypothesis tests were undertaken on the means of overall ratings across different languages or types, significant differences could indicate preferences that businesses may exploit for targeted campaigns. Ensure to report p-values and confidence intervals for any statistical claims.

#### 5. Time-Series Analysis Findings

- **Seasonal Patterns**: The seasonal decomposition suggests fluctuations that could indicate popular trends over time or possibly periods of low activity. 
  - **Recommendation**: Further analyze

## Visualizations

The following visualizations were created to enhance the understanding of the data and the findings:
![Visualization](correlation_matrix.png)

![Visualization](missing_values.png)

![Visualization](outliers.png)

![Visualization](time_series_analysis.png)

![Visualization](cluster_analysis.png)

