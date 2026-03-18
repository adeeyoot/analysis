## Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## Importing the dataset
dataset = pd.read_csv("Sentiment dataset.csv")
print(dataset.head())

## Basic cleaning
dataset = dataset.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'])
print(dataset.head())

dataset['Sentiment'] = dataset['Sentiment'].str.strip()
dataset['User'] = dataset['Sentiment'].str.strip()
dataset['Platform'] = dataset['Platform'].str.strip()
dataset['Country'] = dataset['Country'].str.strip()

print(dataset.info())
print(dataset.isnull().sum())

## Summary statistics - numerical columns
num_cols = ['Retweets', 'Likes', 'Year', 'Month', 'Day', 'Hour']
print("\nSummary Statistics:")
print(dataset[num_cols].describe().round(2))

print("\nMedians:")
print(dataset[num_cols].median().round(2))

print("\nMode:")
print(dataset.mode().iloc[0])

## Sentiment distribution
print("\n Top 15 Sentiments")
sentiment_counts = dataset['Sentiment'].value_counts().head(15)
print(sentiment_counts)

plt.figure(figsize=(12, 6))
sentiment_counts.plot(kind='bar', color='skyblue')
plt.title('Top 15 Sentiment Categories')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

## Distributions of Likes & Retweets
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
sns.histplot(dataset['Likes'], kde=True, bins=30, color='teal')
plt.title('Distribution of Likes')
plt.xlabel('Likes')

plt.subplot(1, 2, 2)
sns.histplot(dataset['Retweets'], kde=True, bins=30, color='coral')
plt.title('Distribution of Retweets')
plt.xlabel('Retweets')

plt.tight_layout()
plt.show()

## Likes by Sentiment (boxplot - top sentiments)
top_sentiments = dataset['Sentiment'].value_counts().head(8).index

plt.figure(figsize=(12, 6))
sns.boxplot(x='Sentiment', y='Likes', data=dataset[dataset['Sentiment'].isin(top_sentiments)],
            order=top_sentiments, palette='Set2')
plt.title('Likes Distribution by Top Sentiments')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

## Likes vs Retweets scatter plot (colored by Sentiment)
plt.figure()
plt.scatter(dataset['Likes'], dataset['Retweets'], c = dataset["Likes"], cmap = "viridis")
plt.title("Likes vs Retweets")
plt.xlabel("Likes")
plt.ylabel("Retweets")
plt.colorbar()
plt.show()


## Correlation heatmap
plt.figure(figsize=(8, 6))
corr = dataset[num_cols].corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()