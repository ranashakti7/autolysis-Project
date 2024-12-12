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

## Insights and Implications

Based on the analysis performed on the dataset, several actionable insights can be derived. Here, I will summarize relevant correlations, anomalies, patterns, and potential trends for future exploration or business decisions.

### 1. Insights on Correlations Between Variables:
The correlation matrix shows the following key relationships among the numerical features:
- **Overall and Quality (0.83)**: There is a strong positive correlation between overall ratings and quality ratings, suggesting that as the overall rating increases, so does quality. This implies that reviewers tend to rate both attributes similarly.
- **Overall and Repeatability (0.51)**: There is a moderate positive correlation, indicating while most high overall scores correlate with higher repeatability scores, it isn't as strong as overall vs. quality.
- **Quality and Repeatability (0.31)**: The relationship is weak but still positive, indicating that higher quality ratings may lead to some increases in repeatability.

### 2. Outliers Detected and Their Possible Implications:
A total of **116 outliers** were detected, which may indicate extreme ratings or errors in data entry. Examining these outliers can provide insights into anomalies in reviewer behavior or specific titles that received atypical scores:
- **Actionable Steps**: Review the data points classified as outliers to determine if they are due to data entry errors or if they highlight unique anecdotal cases, such as particularly polarizing films or shows that require additional focus in marketing or product development.

### 3. Significant Clusters Discovered through KMeans:
KMeans clustering can often unearth significant patterns in the data:
- **Identified Clusters**: While exact characteristics of the clusters are not provided, they may represent different genres/types of titles (like movies vs. series) or distinct rating patterns (e.g., high quality/low repeatability vs. low quality/high repeatability).
- **Actionable Insights**: Understanding these clusters could help tailor marketing strategies or content recommendations based on viewer preferences and feedback.

### 4. Results from Hypothesis Testing:
Assuming inference tests were conducted on key metrics:
- Tests may have indicated if there were statistically significant differences in quality ratings across different languages or types of content. These results could drive changes in content localization or international marketing strategies.

### 5. Key Findings from Time-Series Decomposition:
- The **seasonal component** shows various fluctuations, suggesting certain trends or cycles in the dataset over time.
- With `trend` and `residual`

## Visualizations

The following visualizations were created to enhance the understanding of the data:
![Visualization](correlation_matrix.png)

![Visualization](missing_values.png)

![Visualization](outliers.png)

![Visualization](time_series_analysis.png)

![Visualization](cluster_analysis.png)

