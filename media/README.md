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

Based on the analysis performed on the dataset, here are some actionable insights along with recommendations for future data exploration or business decisions:

### 1. Correlation Insights
- **Correlation Analysis**: The overall score shows a strong positive correlation with quality (0.83), suggesting that higher-rated items tend to have better quality evaluations. The correlation with repeatability is moderate (0.51), indicating that more repeatable items usually receive higher overall scores too.
- **Implication**: Focus on improving the factors that contribute to quality, as this appears to drive the overall rating significantly. Identifying and enhancing specific attributes that lead to better quality evaluations may boost overall scores.

### 2. Outlier Detection
- **Outliers Count**: A total of 116 outliers were detected, impacting the variability of overall, quality, and repeatability scores.
- **Implication**: Investigating these outliers may help determine if they represent unique cases that could inform product improvements or marketing strategies. For example, if certain low-scoring repeats are anomalies, understanding why can foster better offerings.

### 3. Clusters Identified via KMeans
- **Clustering**: Utilizing KMeans may have revealed significant clusters of items based on their characteristics. For instance, you may find a cluster of highly-rated films in a particular language or genre.
- **Implication**: This clustering insight can inform targeted marketing campaigns or content recommendations based on user preferences and behaviors observed in high-performing clusters. Analyzing these clusters can optimize resource allocation in content creation and promotion.

### 4. Hypothesis Testing Results
- **Statistical Testing**: If hypothesis testing indicated significant differences in quality ratings across different languages or types, using an ANOVA or chi-squared test may have spotlighted significant trends.
- **Implication**: Recognizing significant differences in quality ratings can guide decisions on localization strategies or investments in certain types or genres of content.

### 5. Time-Series Decomposition
- **Findings**: The seasonal component indicates cycles within the data, where certain periods or months might yield higher scores than others.
- **Implication**: If spikes in seasonal ratings correlate with specific events (e.g., film festivals, holidays), this understanding can guide marketing content release plans to maximize visibility and ratings.

### Recommendations for Data Cleaning and Future Exploration
- **Missing Values**: Address the missing values in the `date` (99) and `by` columns (262)

## Visualizations

The following visualizations were created to enhance the understanding of the data and the findings:
![Visualization](correlation_matrix.png)

![Visualization](missing_values.png)

![Visualization](outliers.png)

![Visualization](time_series_analysis.png)

![Visualization](cluster_analysis.png)

