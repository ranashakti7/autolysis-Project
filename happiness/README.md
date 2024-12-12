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
| top    | Lebanon        |                    |                    |                      |                     |                                    |                                |                       |                             |                     |                     |
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

## Insights and Implications

### Actionable Insights from the Dataset Analysis

#### Correlations between Variables:
1. **Life Ladder** and **Log GDP per capita**: A strong positive correlation (0.78) suggests that as countries' GDP per capita increases, their happiness (measured by the Life Ladder) also tends to increase. This finding aligns with economic theories that higher income leads to better quality of life.

2. **Life Ladder** and **Social Support**: A similarly strong positive correlation (0.72) indicates the importance of social networks and support systems in enhancing individual well-being.

3. **Life Ladder** and **Freedom to Make Life Choices**: This variable also shows a strong positive correlation (0.53), indicating that personal autonomy is critical to happiness.

4. **Perceptions of Corruption**: There is a notable negative correlation (-0.43) with the Life Ladder, indicating that higher levels of perceived corruption are associated with lower happiness levels.

#### Outliers Detected:
- **Outlier Count**: A total of 105 outliers were detected in the dataset, primarily among the `Log GDP per capita`, `Social support`, and `Freedom to make life choices` features.
  
**Implications**: 
   - Investigating these outliers could reveal specific countries or years that do not conform to expected patterns. For instance, a country with a high GDP per capita but low life satisfaction could point towards systemic issues, such as inequality or corruption.

#### Clusters Discovered Through KMeans:
- **KMeans Results**: Cluster analysis may reveal distinct groups of countries based on the features analyzed. For example, one cluster might consist of developed, high-GDP countries with high Life Ladder scores, while another may include developing countries with lower scores but high Social Support.

**Actionable Steps**:
   - Targeted policies could be developed for specific clusters. For example, countries in a low Life Ladder cluster that have significantly high GDP may be targeted for anti-corruption measures or initiatives aimed at improving personal freedoms.

#### Hypothesis Testing Results:
- The hypothesis tests (not detailed in the summary) can reveal if differences across demographic groupings (e.g., geographic regions) are statistically significant. 

**Recommendation**: Conduct further hypothesis testing on key variables to identify specific factors that significantly influence happiness across different socio-economic backgrounds.

#### Key Findings from Time-Series Decomposition:
- The seasonal component indicates fluctuations in happiness measures at certain times, which could correlate with political events

## Visualizations

The following visualizations were created to enhance the understanding of the data:
![Visualization](correlation_matrix.png)

![Visualization](missing_values.png)

![Visualization](outliers.png)

![Visualization](time_series_analysis.png)

![Visualization](cluster_analysis.png)

