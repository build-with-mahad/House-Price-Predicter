import pandas as pd

#load Dataset
df = pd.read_csv("HousePricePrediction.csv")

#Display the first 10 rows
print(df.head(10))

#Display the shape of dataset i.e  ROWS or COLUMNS
print(df.shape)

#Display the Data types of Columns
print(df.dtypes)

#Generate Statisticql Summary of numerical features
print("Statistical Info:\n",df[["MSSubClass","LotArea","OverallCond","YearBuilt","YearRemodAdd","BsmtFinSF2","TotalBsmtSF","SalePrice"]]
      .describe())

#Identify Missing Values
print(df.isna().sum())

#Handle Missing Values
df["MSZoning"] = df["MSZoning"].fillna(df["MSZoning"].mode()[0])
df["Exterior1st"] = df["Exterior1st"].fillna(df["Exterior1st"].mode()[0])
df["BsmtFinSF2"] = df["BsmtFinSF2"].fillna(df["BsmtFinSF2"].mean())
df["TotalBsmtSF"] = df["TotalBsmtSF"].fillna(df["TotalBsmtSF"].median())
df["SalePrice"] = df["SalePrice"].fillna(df["SalePrice"].median())

#Again check if there is another column value is missing
print(df.isna().sum())

#check duplicate rows
print(df[df.duplicated()])

#Delete the Duplicate records
df.drop_duplicates(inplace=True)

#Delete the column
df.drop(columns="Id",inplace=True)

#Final Display of Dataset
print(df.info())