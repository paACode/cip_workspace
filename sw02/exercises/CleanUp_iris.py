# Example for Data Cleaning
# https://github.com/DJCordhose/ml-examples

import pandas as pd

pd.set_option('display.precision', 3)
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_colwidth', 30)

# Get and Load the Data

url = "https://raw.githubusercontent.com/DJCordhose/ml-examples/master/datasets/Iris/iris_dirty.csv"
columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
df = pd.read_csv(url, header = None, names=columns )

# what is the expected output of the following code?
# some examples: 
# df.iloc[5:10]              
# df.iloc[5:10,[1,3]]        
# df.iloc[:,1:5]             
# df.iloc[:,[1,3,4]]         
# df.iloc[[2,4,7]]          
# df.iloc[[2,4,7],[1,3,4]]  

# check your guesses!

###################
# Get an overview
###################

# use count to count the entries for each column
df.count()

# use sample to take n arbitrary rows
df.sample(3)

# use describe() to find a statistical summary on the numerical columns
df.describe()

# why are there only 3 columns?
# use info() to get information about data types and nan values
df.info()
# does that explain the result of df.describe()?

# use value_counts to see how many elements belong to each unique value of the column 'class'

df["class"].value_counts()

# why is there only 1 entry for Iris-setsoa?

###################
# Groupby unique values of columns
###################

# Each unique value gets a columns, the aggregation function 'count' tells you what the values are. (try also other aggregation functions as: mean, max, min, std, etc.)
df.groupby('class').count()


###################
# Find NaN values
###################

# find rows with at least one NaN elemnt
df[df.isnull().any(axis=1)]     # explain the result of this line => show below step by step!

# Let's explore this command step by step:
df.isnull()

df.isnull().any(axis=1)         # Question: is 'any' element 'True' in axis=1??  Output as Series !
df.isnull().any(axis=0)

# NOTE: you can also use isna() instaed of isnull() -> equivalent
df.isna().any(axis=1)

# Now find out where the values are, which are NaN
df.loc[df.isna().any(axis=1)]    

df.iloc[81:84]                 # here we see our NaN value!!!

###################
# Replace NaN values
###################

df_iris_versicolor = df[df['class']  == 'Iris-versicolor']

print(df_iris_versicolor["sepal width"].mean())
print("-"*40)
print(df["sepal width"].fillna(999).loc[81:84])
print("-"*40)
print(df["sepal width"].fillna(2.999 ).loc[81:84])                     # random value 2.999!

# create a new column with NaNs filled by mean value

df["sepal_width2"] = df["sepal width"].fillna(df_iris_versicolor["sepal width"].mean())
df[81:84]

df.info()             # one more column is visible with one less NaN value

# HINT: use rolling() to replace nan values with means of custom window sizes, e.g. the 5 elements before, instead of the entire column!

###################
# Remove duplicates
###################

df.duplicated()
df[df.duplicated()] # shows only lines already existing once
df[df.duplicated(keep=False)]    # show all values - not only the duplicated!

# drop_duplicates() is an inplace-Operation => values are dropped for ever! Therefore BE CAREFUL!
# For testing, it is better to first create a new data frame (e.g. df_dup_free).

df_dup_free = df.drop_duplicates()          # Records 34,37 and 100 are droped
df_dup_free[df_dup_free.duplicated()]       # show all duplicated rows => NOW nothing!!!
df_dup_free[28:39]                          # show the deleted rows  34 and 37 

# HINT: keep metainformat as e.g. how many rows will be removed etc.

# Let's drop the duplicate row 100: 
print(df.index[[100]])
iris_test = df.drop(df.index[[100]])
print(iris_test.iloc[98:102])

# now let's do it with our original dataframe:

df.drop(df.index[100], inplace = True)
df[90:105]                       # row 100 is deleted!!!!

###################
# Handle typos
###################

df["class"].value_counts()
# there is a simple 'Typo' on one value: Iris-setsoa is wrong!

df.replace({"class": {"Iris-setsoa": "Iris-setosa"}}, inplace=True)
df["class"].value_counts()

df.groupby('class').count()

###################
# Handle data types
###################

df.info()
# some entry caused "petal width" to be read in as object type
df.head()
# now it's clear that the "mm" is responsible for that

# we use replace in combination with a type cast to create a new clean petal_width_2 column
df["petal_width2"] = df["petal width"].replace("mm", "", regex=True).astype(dtype=float,errors="ignore")

df.loc[66:70]                    # 15 mm != 15 cm  =>  15mm == 1.5 cm

# Be carefule, the other columns seem to be measured in cm! (not mm)
df["petal_width2"]= df["petal_width2"]/10          
df.loc[66:70]
df.info()

# NOTE: The 'stage' phases (xxx_xxx_2) could possibly be skipped
#                 But ALWAYS be careful so that there is no confusion and you can still 
#                 understand the original values at the end.
#                 Remove and rename if you want

#                 You can rename the original colmns with a "_"-prefix
# df.rename(columns={"sepal width": "_sepal width", 
#                    "petal width": "_petal width",
#                    "sepal length": "_sepal length",
#                    "petal length": "_petal length",
#                                                  }, inplace=True)

# df.rename(columns={"sepal_width2": "sepal_width", 
#                    "petal_width2": "petal_width"}, inplace=True)


###################
# Outliers
###################

# We look for outliers!
df.describe()

# you find potential outliers already by comparing the stat values from df.describe()
# For example: the max value of sepal length is 58, with a mean of ~6 and a std of ~4

df[df["sepal length"] > 10]
df["sepal_length2"] = df["sepal length"]

# set the value 58.0 to None in 'sepal_length2'
df.loc[df["sepal_length2"] > 10, "sepal_length2"] = None     # perhaps 5.8 would be better ... or mean ... or? 

df.describe()                  # show the 'max'-values, count, mean, std. 

# Alternatively, we can replace the value with the mean of all entries belonging to the same class
# show all values with 'Iris-virginica' in column "sepal_length2"
df[df['class']  == 'Iris-virginica']["sepal_length2"]    

# calculate the mean-value of all 'Iris-virginica'-valus in column "sepal_length2"

vsl_mean = df[df['class']  == 'Iris-virginica']["sepal_length2"].mean()
df["sepal_length2"] = df["sepal_length2"].fillna(vsl_mean)   # fill all NaN-Values with the vsl_mean

df[df["sepal length"] > 10]

# again, if you want, rename and keep the column naming consistent
# df.rename(columns={"sepal_length2": "sepal_length"}, inplace=True)

df.describe()
df.info()

###################
# Renaming and reordering and saving
###################

# At the moment we only have one column untouched. Pragmatically, we will add a new one and split our dataframe into an original and a cleaned one.
# there are other ways of doing that!

df['petal_length2'] = df['petal length']
df_clean = df[df.columns[4:]]
df_clean.columns = list(map(lambda x: x.replace("2",""), df_clean.columns)) # replace all the '2's with empty string in columns names
# reorder
reordered_cols = ['sepal_width', 'sepal_length', 'petal_width', 'petal_length', 'class']
df_clean = df_clean[reordered_cols]

# quickly check 
print("-------------------------")
print("\nSUMMARY cleaned:\n\n")
print(df_clean.describe())
print("\n")
print(df_clean.info())

# save to new file if you want
# df_clean.to_csv("iris_clean.csv", index=False)
