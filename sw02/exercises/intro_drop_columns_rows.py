"""
Content:
- drop content
"""

# intro in pandas: drop rows and colums in a DataFrame's
import pandas
df1 = pandas.read_csv("traffic.csv")

# to delete a row or a column use 'drop' command
# Example: delete 'day'-column

df20 = __FILL_HERE__            # axis parameter '1' = columns //  '0' = index (=rows)

# Example: delete the fifth row (fourth index)

df21 = __FILL_HERE__

# remember all 'drop'-commands are NOT inplace 
# instead of use words like 'Day' to delete a column
# we can also use the parameter 'columns'

# like above:
# df1.drop("Day",1)                         # parameter '1' = columns //  '0' = index (=rows)

df22 = __FILL_HERE__         

# use .columns for all column-names as a list
__FILL_HERE__

# use .index for all index-names in a list: 
__FILL_HERE__

#############
# Exercise
#############
# change the index[5] of df1 to 'myTest'  with the command 'rename()'
# print the DataFrame 
# print now the name of index[5]

df23 = __FILL_HERE__
index_5 = __FILL_HERE__

# print df23

#################
# Example (simple)
#################

df1 = pandas.read_csv("traffic.csv")

# drop the third row of df1 and save the result in an new DataFrame df25
df25 = __FILL_HERE__

# drop the first, third and the ninth row of df1 and save the result in df25
# and drop the 'Country' and 'Day' columns as well
# in one line of code  (admittedly: that is NOT always useful!)
