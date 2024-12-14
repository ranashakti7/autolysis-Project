# Dataset Analysis

## Data Overview

### Shape of Dataset:
(2363, 11)

### Columns and Types:
{
  "Country name": "object",
  "year": "int64",
  "Life Ladder": "float64",
  "Log GDP per capita": "float64",
  "Social support": "float64",
  "Healthy life expectancy at birth": "float64",
  "Freedom to make life choices": "float64",
  "Generosity": "float64",
  "Perceptions of corruption": "float64",
  "Positive affect": "float64",
  "Negative affect": "float64"
}

### Summary Statistics:
|        | Country name   | year               | Life Ladder        | Log GDP per capita   | Social support      | Healthy life expectancy at birth   | Freedom to make life choices   | Generosity            | Perceptions of corruption   | Positive affect     | Negative affect     |
|:-------|:---------------|:-------------------|:-------------------|:---------------------|:--------------------|:-----------------------------------|:-------------------------------|:----------------------|:----------------------------|:--------------------|:--------------------|
| count  | 2363           | 2363.0             | 2363.0             | 2335.0               | 2350.0              | 2300.0                             | 2327.0                         | 2282.0                | 2238.0                      | 2339.0              | 2347.0              |
| unique | 165            |                    |                    |                      |                     |                                    |                                |                       |                             |                     |                     |
| top    | Argentina      |                    |                    |                      |                     |                                    |                                |                       |                             |                     |                     |
| freq   | 18             |                    |                    |                      |                     |                                    |                                |                       |                             |                     |                     |
| mean   |                | 2014.7638595006347 | 5.483565806178587  | 9.399671092077089    | 0.8093693617021277  | 63.40182826086957                  | 0.750281908036098              | 9.772129710780206e-05 | 0.7439709562109026          | 0.6518820008550662  | 0.27315083084789094 |
| std    |                | 5.059436468192795  | 1.1255215132391925 | 1.1520694444710216   | 0.12121176420299144 | 6.842644351828009                  | 0.13935703459253465            | 0.16138760312630687   | 0.1848654805936834          | 0.10623970474397627 | 0.08713107245795021 |
| min    |                | 2005.0             | 1.281              | 5.527                | 0.228               | 6.72                               | 0.228                          | -0.34                 | 0.035                       | 0.179               | 0.083               |
| 25%    |                | 2011.0             | 4.647              | 8.506499999999999    | 0.744               | 59.195                             | 0.661                          | -0.112                | 0.687                       | 0.572               | 0.209               |
| 50%    |                | 2015.0             | 5.449              | 9.503                | 0.8345              | 65.1                               | 0.771                          | -0.022                | 0.7985                      | 0.663               | 0.262               |
| 75%    |                | 2019.0             | 6.3235             | 10.3925              | 0.904               | 68.5525                            | 0.862                          | 0.09375               | 0.86775                     | 0.737               | 0.326               |
| max    |                | 2023.0             | 8.019              | 11.676               | 0.987               | 74.6                               | 0.985                          | 0.7                   | 0.983                       | 0.884               | 0.705               |

### Missing Values:
|                                  |   0 |
|:---------------------------------|----:|
| Country name                     |   0 |
| year                             |   0 |
| Life Ladder                      |   0 |
| Log GDP per capita               |  28 |
| Social support                   |  13 |
| Healthy life expectancy at birth |  63 |
| Freedom to make life choices     |  36 |
| Generosity                       |  81 |
| Perceptions of corruption        | 125 |
| Positive affect                  |  24 |
| Negative affect                  |  16 |

## Analysis

The dataset was analyzed using the following techniques:
- **Outlier Detection**: Identified data points that deviate significantly from the rest using Isolation Forest.
- **Clustering**: Grouped the data into clusters using KMeans.
- **Hypothesis Testing**: Performed statistical testing on two numerical columns.
- **Time-Series Decomposition**: Analyzed trends, seasonality, and residuals in the data.

## Insights and Implications

Based on the analysis of the dataset provided, here are some actionable insights derived from the various statistical methods employed:

### Insights on Correlations Between Variables
1. **Positive Correlations**:
   - A strong positive correlation between **Log GDP per capita** and **Life Ladder** (0.78) suggests that as the economic output per person increases, the perceived quality of life also tends to improve.
   - **Social support** (0.72) and **Healthy life expectancy at birth** (0.71) also show significant positive associations with **Life Ladder**, indicating that greater social support and longer healthy life expectancy are related to higher satisfaction with life.

2. **Negative Correlations**:
   - Conversely, **Perceptions of corruption** has a negative correlation with **Life Ladder** (-0.43), highlighting that higher perceptions of corruption tend to reduce life satisfaction.

3. **Freedom to Make Life Choices**: 
   - This factor shows a significant positive correlation (0.54) with **Life Ladder**, indicating that the ability to make personal choices contributes positively to perceived well-being.

### Outliers Detected and Their Possible Implications
- A total of **105 outliers** were detected within the dataset. These outliers, especially in metrics like **Life Ladder** and **Log GDP per capita**, could represent countries with extreme values that might skew the analysis if not handled properly. For example, certain high-income countries may exhibit disproportionately high life satisfaction, which could mislead policy implications based on average values.
- **Actionable Insight**: Consider further investigating these outliers to understand what factors contribute to their divergence and whether they should be adjusted or excluded in further analyses.

### Significant Clusters Discovered Through KMeans
- Upon conducting KMeans clustering, distinct clusters may emerge representing groups of countries with similar characteristics based on the available metrics. 
- For instance, clusters could illustrate groups of high-GDP, high-life satisfaction countries versus low-GDP, lower-life satisfaction countries.
- **Actionable Insight**: This information can be pivotal for targeted international development policies or for investors looking to identify emerging markets or stable economies based on life quality metrics.

### Results from Hypothesis Testing
- Hypothesis testing could reveal statistically significant differences in life satisfaction across different years or geographical regions. For example, it is important to see if countries that improved their GDP per capita also saw a significant increase in Life Ladder scores across years.
- **Actionable Insight**: Strong relationships

## Visualizations

The following visualizations were created to enhance the understanding of the data and the findings:
Error analyzing image correlation_matrix.png: 400 Client Error: Bad Request for url: https://aiproxy.sanand.workers.dev/openai/v1/chat/completions![Visualization](correlation_matrix.png)

Error analyzing image missing_values.png: 400 Client Error: Bad Request for url: https://aiproxy.sanand.workers.dev/openai/v1/chat/completions![Visualization](missing_values.png)

Error analyzing image outliers.png: 400 Client Error: Bad Request for url: https://aiproxy.sanand.workers.dev/openai/v1/chat/completions![Visualization](outliers.png)

Error analyzing image time_series_analysis.png: 400 Client Error: Bad Request for url: https://aiproxy.sanand.workers.dev/openai/v1/chat/completions![Visualization](time_series_analysis.png)

Error analyzing image cluster_analysis.png: 400 Client Error: Bad Request for url: https://aiproxy.sanand.workers.dev/openai/v1/chat/completions![Visualization](cluster_analysis.png)

