# Social Media Engagement & Sentiment Analysis

## Overview

This project performs **exploratory data analysis (EDA)** on a dataset of ~732 social media posts (primarily from platforms like Instagram, Twitter/X, and Facebook). The focus is on understanding how **sentiment** influences **engagement** (measured by likes and retweets), along with temporal patterns and basic correlations.

Key questions explored:
- Do positive emotions (joy, excitement, gratitude) drive more likes/retweets?
- What is the relationship between likes and retweets?
- How are likes and retweets distributed?
- Are there any temporal trends (year, month, day, hour)?

## Dataset Summary

- **Total posts**: 732
- **Key columns**: Retweets, Likes, Year, Month, Day, Hour, Sentiment, Text, User, Platform, etc.
- **Time range**: Mostly 2010–2023 (median year: 2021)
- **Median engagement**: 22 retweets, 43 likes
- **Top sentiments**: Positive (45), Joy (44), Excitement (37), Contentment (19), Neutral (18), Gratitude (18), ...

## Visualizations Included

1. **Boxplot**: Likes distribution by top sentiments  
   → Excitement, Gratitude, and Joy show higher median likes and more variability.

2. **Scatter Plot**: Likes vs Retweets  
   → Strong positive linear relationship (correlation ~1.00 in matrix – almost perfect collinearity in this sample).

3. **Correlation Heatmap**  
   → Very high correlation between Likes and Retweets (~1.00). Weak or no correlation with temporal features.

4. **Histograms**: Distribution of Likes and Retweets  
   → Both roughly unimodal, Likes centered ~40–50, Retweets ~20–25.

## Key Insights

- Posts with **joy**, **excitement**, and **gratitude** tend to receive more likes than neutral or negative posts.
- Likes and retweets are extremely highly correlated (almost 1:1 in many cases).
- No strong temporal patterns (year/month/day/hour show very low correlation with engagement).
- Most common hour of posting: around 4 PM (median 16:00).
- Example top post (mode): "A compassionate rain, tears of empathy falling..." with Positive sentiment, 22 retweets, 45 likes.

## Technologies Used

- **Python** 3.10+
- **pandas** – data manipulation & summary statistics
- **numpy** – numerical operations
- **matplotlib** + **seaborn** – all visualizations (boxplots, scatter, heatmap, histograms)
