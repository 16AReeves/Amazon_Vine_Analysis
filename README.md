# Amazon_Vine_Analysis
---
## Module 16: Using Hadoop, PySpark, SQL, Postgres, and AWS to analyze big data
---
### Overview
---
#### The purpose of this analysis was to learn to use google colab, PySpark, Hadoop, and AWS to analyze large datasets. Data was transformed and loaded into PostgresSQL for analysis and storage. This analysis looks at amazon reviews of video games and analyzes the differences between amazon's paid review program (Vine) versus unpaid reviews. 
---
### Results
---
#### Below are the results for the total review counts, total 5-star reviews, and percentage of 5-star reviews:
Amazon Vine Reviews | Amazon Unpaid Reviews
--- | --- |
![vine_paid_reviews](https://user-images.githubusercontent.com/98365963/175837759-5d3e3722-7339-4855-81c2-10a610bbfd8d.PNG) | ![amazon_unpaid_reviews](https://user-images.githubusercontent.com/98365963/175837765-392000ed-45cd-4d7b-bb6e-967893d965a6.PNG)
* #### The total number of vine paid reviews were 94 versus 40471 unpaid reviews overall. 
* #### The total number of 5-star vine paid reviews were 48 versus 15663 unpaid 5-star reviews overall.
* #### The percentage of great 5-star vine reviews were 51% versus 39% unpaid 5-star reviews. 
---
### Summary
---
#### There is a small positivity bias for paid reviews versus unpaid reviews; however, the number of unpaid reviews far outway the number of paid. From the video game data, it seems if the game was given for free or if the review is paid then people are 50% likely to give a 5-star review. Otherwise, if the game was completely paid for by the consumer, then the review seems to be more honest with only 39% of people giving the game a 5-star rating. 
#### Another analysis for this dataset would be to split the reviews by individual products, and determining the total reviews per product along with percentage of 5-star reviews per product. This analysis only looks for the total reviews given based on the data, and doesn't look at individual products reviews. This could give more insight if Amazon's paid vine review program truly impacts each products review rating; while overall, it seems to impact it slightly.  
