## Importing the library
import pandas as pd

## Importing the dataset
dataset = pd.read_csv("synthetic_dataset.csv")
print(dataset.head())

## Removing duplicates
dataset.info()
print(dataset.duplicated())
print(dataset.duplicated().sum())
dataset[dataset.duplicated()]

dataset.drop_duplicates(inplace = True)
dataset.info()

dataset.duplicated().sum()

## Taking care of null values
print(dataset.isnull().sum())

dataset.dropna(inplace = True)

dataset.info()
print(dataset.isnull().sum())

## Taking care of inconsistent data formats
dataset['Category'] = dataset['Category'].str.strip()
dataset['Stock'] = dataset['Stock'].str.strip()
dataset['Price'] = dataset['Price'].round(2)
dataset['Rating'] = dataset['Rating'].round(2)
dataset['Discount'] = dataset['Discount'].round(2)
print(dataset.head())