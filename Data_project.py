# Importing the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ignore harmless warnings
import warnings
warnings.filterwarnings('ignore')


# Correct way to load your CSV file:
file_path = "/Users/siddheshkalgaonkar/Desktop/learnbay_Data_Analyst/Madhuri/flipkart_product_dataset/test.csv"  # Or use a raw string: r"path"
try:
    data = pd.read_csv(file_path)
    print(data.head())  # Print the first few rows to verify it loaded correctly
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e: # Catch other potential errors (e.g., bad CSV format)
    print(f"An error occurred while reading the CSV: {e}")

print(data.describe())


#******************************************************************************
print("check for null values")
print(data.isnull().sum())                  # Number of missing values in each columns
print(round(data.isnull().mean()*100, 2))

#**********************************************************************
print("Remove the missing values")

print(data.dropna(inplace=True))

# percetage missing values after removing it
print(round(data.isnull().mean()*100, 2))

#**************************************************************************************
data.info()

#*************************************************************************************
#"""
#How does the product rating (Rating) correlate with the number of reviews (noreviews1)
# and the star ratings (star_5f, star_4f, etc.)?
 #Are there products with high ratings but few reviews, or vice-versa?
#"""#

# correaltion Coefficient value
# syntax
# var = data['x'].corr(data['y'])
s_corr = data['Rating'].corr(data['noreviews1'])
print('Correlation Coefficient Value:', round(s_corr,2))

# scatter plot b/w two variables
sns.scatterplot(data=data,
                x = 'Rating',
                y = 'noreviews1', color='g')
print(plt.show())


# Correlation with star ratings
star_ratings = ['star_5f', 'star_4f', 'star_3f', 'star_2f', 'star_1f']
for star_rating in star_ratings:
    corr_star = data['Rating'].corr(data[star_rating])
    print(f"Correlation Rating vs. {star_rating}: {corr_star:.2f}")
    sns.scatterplot(x='Rating', y=star_rating, data=data)
    plt.title(f'Rating vs. {star_rating}')
    print(plt.show())

#***********************************************************************
#Is there a relationship between the actual price (actprice1) and the product rating?
# Are more expensive products generally rated higher?

# correaltion Coefficient value
# syntax
# var = data['x'].corr(data['y'])
s_corr = data['actprice1'].corr(data['Rating'])
print('Correlation Coefficient Value:', round(s_corr,2))

# scatter plot b/w two variables
sns.scatterplot(data=data,
                x = 'Rating',
                y = 'actprice1', color='y')
print(plt.show())

#***********************************************************************************
# 2D Histogram/Heatmap (if you have enough data)
plt.figure(figsize=(10,8)) #Adjust figure size for better readability
plt.hist2d(data['actprice1'], data['Rating'], bins=(20, 10), cmap=plt.cm.Reds) #Adjust number of bins as needed
plt.colorbar(label='Frequency')
plt.xlabel('Rating')
plt.ylabel('Actual Price')
plt.title('2D Histogram of Price vs. Rating')
print(plt.show())