# Dataset Analysis

## Data Overview

### Shape of Dataset:
(10000, 23)

### Columns and Types:
{
  "book_id": "int64",
  "goodreads_book_id": "int64",
  "best_book_id": "int64",
  "work_id": "int64",
  "books_count": "int64",
  "isbn": "object",
  "isbn13": "float64",
  "authors": "object",
  "original_publication_year": "float64",
  "original_title": "object",
  "title": "object",
  "language_code": "object",
  "average_rating": "float64",
  "ratings_count": "int64",
  "work_ratings_count": "int64",
  "work_text_reviews_count": "int64",
  "ratings_1": "int64",
  "ratings_2": "int64",
  "ratings_3": "int64",
  "ratings_4": "int64",
  "ratings_5": "int64",
  "image_url": "object",
  "small_image_url": "object"
}

### Summary Statistics:
|        | book_id            | goodreads_book_id   | best_book_id      | work_id            | books_count        | isbn      | isbn13             | authors      | original_publication_year   | original_title   | title          | language_code   | average_rating      | ratings_count      | work_ratings_count   | work_text_reviews_count   | ratings_1         | ratings_2         | ratings_3          | ratings_4         | ratings_5         | image_url                                                                                | small_image_url                                                                        |
|:-------|:-------------------|:--------------------|:------------------|:-------------------|:-------------------|:----------|:-------------------|:-------------|:----------------------------|:-----------------|:---------------|:----------------|:--------------------|:-------------------|:---------------------|:--------------------------|:------------------|:------------------|:-------------------|:------------------|:------------------|:-----------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| count  | 10000.0            | 10000.0             | 10000.0           | 10000.0            | 10000.0            | 9300      | 9415.0             | 10000        | 9979.0                      | 9415             | 10000          | 8916            | 10000.0             | 10000.0            | 10000.0              | 10000.0                   | 10000.0           | 10000.0           | 10000.0            | 10000.0           | 10000.0           | 10000                                                                                    | 10000                                                                                  |
| unique |                    |                     |                   |                    |                    | 9300      |                    | 4664         |                             | 9274             | 9964           | 25              |                     |                    |                      |                           |                   |                   |                    |                   |                   | 6669                                                                                     | 6669                                                                                   |
| top    |                    |                     |                   |                    |                    | 439023483 |                    | Stephen King |                             |                  | Selected Poems | eng             |                     |                    |                      |                           |                   |                   |                    |                   |                   | https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png | https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png |
| freq   |                    |                     |                   |                    |                    | 1         |                    | 60           |                             | 5                | 4              | 6341            |                     |                    |                      |                           |                   |                   |                    |                   |                   | 3332                                                                                     | 3332                                                                                   |
| mean   | 5000.5             | 5264696.5132        | 5471213.5801      | 8646183.4246       | 75.7127            |           | 9755044298883.463  |              | 1981.987674115643           |                  |                |                 | 4.002191000000001   | 54001.2351         | 59687.3216           | 2919.9553                 | 1345.0406         | 3110.885          | 11475.8938         | 19965.6966        | 23789.8056        |                                                                                          |                                                                                        |
| std    | 2886.8956799071675 | 7575461.863589611   | 7827329.890719961 | 11751060.824080039 | 170.47072765025834 |           | 442861920665.57336 |              | 152.57666516754668          |                  |                |                 | 0.25442748053872905 | 157369.95643554674 | 167803.7852374182    | 6124.378131569911         | 6635.626262783459 | 9717.123578396993 | 28546.449183182456 | 51447.35838380058 | 79768.88561077163 |                                                                                          |                                                                                        |
| min    | 1.0                | 1.0                 | 1.0               | 87.0               | 1.0                |           | 195170342.0        |              | -1750.0                     |                  |                |                 | 2.47                | 2716.0             | 5510.0               | 3.0                       | 11.0              | 30.0              | 323.0              | 750.0             | 754.0             |                                                                                          |                                                                                        |
| 25%    | 2500.75            | 46275.75            | 47911.75          | 1008841.0          | 23.0               |           | 9780316192995.0    |              | 1990.0                      |                  |                |                 | 3.85                | 13568.75           | 15438.75             | 694.0                     | 196.0             | 656.0             | 3112.0             | 5405.75           | 5334.0            |                                                                                          |                                                                                        |
| 50%    | 5000.5             | 394965.5            | 425123.5          | 2719524.5          | 40.0               |           | 9780451528640.0    |              | 2004.0                      |                  |                |                 | 4.02                | 21155.5            | 23832.5              | 1402.0                    | 391.0             | 1163.0            | 4894.0             | 8269.5            | 8836.0            |                                                                                          |                                                                                        |
| 75%    | 7500.25            | 9382225.25          | 9636112.5         | 14517748.25        | 67.0               |           | 9780830777175.0    |              | 2011.0                      |                  |                |                 | 4.18                | 41053.5            | 45915.0              | 2744.25                   | 885.0             | 2353.25           | 9287.0             | 16023.5           | 17304.5           |                                                                                          |                                                                                        |
| max    | 10000.0            | 33288638.0          | 35534230.0        | 56399597.0         | 3455.0             |           | 9790007672390.0    |              | 2017.0                      |                  |                |                 | 4.82                | 4780653.0          | 4942365.0            | 155254.0                  | 456191.0          | 436802.0          | 793319.0           | 1481305.0         | 3011543.0         |                                                                                          |                                                                                        |

### Missing Values:
|                           |    0 |
|:--------------------------|-----:|
| book_id                   |    0 |
| goodreads_book_id         |    0 |
| best_book_id              |    0 |
| work_id                   |    0 |
| books_count               |    0 |
| isbn                      |  700 |
| isbn13                    |  585 |
| authors                   |    0 |
| original_publication_year |   21 |
| original_title            |  585 |
| title                     |    0 |
| language_code             | 1084 |
| average_rating            |    0 |
| ratings_count             |    0 |
| work_ratings_count        |    0 |
| work_text_reviews_count   |    0 |
| ratings_1                 |    0 |
| ratings_2                 |    0 |
| ratings_3                 |    0 |
| ratings_4                 |    0 |
| ratings_5                 |    0 |
| image_url                 |    0 |
| small_image_url           |    0 |

## Insights and Implications

Based on the comprehensive analysis of the dataset encompassing various metrics and relationships among the features, we can distill several actionable insights:

### Insights on Correlations Between Variables
1. **Ratings and Work Metrics**: There is a strong negative correlation between `ratings_count`, `work_ratings_count`, and `work_text_reviews_count` with `average_rating`. Particularly, as the number of ratings increases, the average rating tends to decrease, indicating potential hype or bias during voting.
   
2. **Books Count and Original Publication Year**: A negative correlation of -0.32 exists between `books_count` and `original_publication_year`, implying that more recent books tend to have a higher count. This might suggest a shift in author popularity or the influence of marketing strategies over time.

3. **Higher Ratings and Fewer Low Ratings**: The correlation matrix shows that ratings 1 through 5 are all positively correlated with one another. This suggests that when a book has high ratings (i.e., 4s and 5s), it likely has fewer low ratings (1s and 2s). 

### Outliers Detected and Their Possible Implications
- **Outlier Count**: The detection of 470 outliers suggests a notable deviation from normal behavior, especially in fields pertaining to ratings, reviews, or book counts. These outliers could represent exceptionally popular books, possibly linked with authors who have large followings or significant marketing budgets.
  
- **Impact on Analysis**: Outliers could distort analytical models. It is advisable to consider their removal when conducting regression analyses or clustering, to aid in refining the accuracy of models.

### Significant Clusters Discovered Through KMeans
- **Marketing Strategy**: KMeans clustering may reveal segments of books with similar characteristics, such as those receiving high ratings and substantial review counts versus those with low ratings. This could inform marketing strategies, suggesting a focus on promoting highly rated books more aggressively or exploring those with low ratings to enhance their visibility.

### Results from Hypothesis Testing
- **Statistical Significance**: If hypothesis tests reveal that certain variables (like author reputation, original publication year, or language) significantly affect the average rating, this could guide strategic decisions around author contracts and targeting specific demographics or regions for marketing campaigns.

### Key Findings from Time-Series Decomposition
- **No Identified Trends**: The time-series analysis returned NaN values for trends and residuals, indicating that there may not be a discernible

## Visualizations

The following visualizations were created to enhance the understanding of the data:
![Visualization](correlation_matrix.png)

![Visualization](missing_values.png)

![Visualization](outliers.png)

![Visualization](time_series_analysis.png)

![Visualization](cluster_analysis.png)

