"""
Content:
- insert new values, columns and rows in DataFrames
"""

import pandas
df1 = pandas.read_csv("traffic.csv")

# Adding und Update Columns and Rows
# add a new column with the name 'Status' (inplace operation!)

# we have to fill a new column with 10 values!!!  
# e.g. ["F","S", "A", "B", "F","S", "A", "B", "A", "C"]

df1["Status"] = __FILL_HERE__

# create a new column with the name 'Test' and content 't' (all cells)
# hint: single values are extended automatically to the size of the dataframe
__FILL_HERE__ = __FILL_HERE__

# remember 'shape' give us back the dimensionality of the DataFrame
print(df1.shape)

# the result is a tuple!   
# Note:  at position '0' of this tuple => number of rows (=10)
#        at position '1' of this tuple => number of columns (=8)

# get the number or rows (index) 

__FILL_HERE__

# get the number or columns 

__FILL_HERE__

############
# Exercise:
############

# One value in the DataFrame is wrong:
# on Index 7 the Clicks-value is wrong. Change the value 40 to 42!
# use 'iat' or 'iloc'
# print the first values of df1
print(df1.head(10))
# print all column-names
print( __FILL_HERE__ )
# print all index-name
print( __FILL_HERE__ )

__FILL_HERE__ = __FILL_HERE__    


###############
# Exercise
###############

#  conatenate 2 DataFrames,

# try to insert a row with 'concat()'-method

# reread the original values from our CSV-File 
df1 = pandas.read_csv("traffic.csv")

# prepare the 'new line to insert' as DataFrame: 
# get the column names of DataFrame df1
column_names = __FILL_HERE__     
print("column_names: ", column_names)

# line to insert
insert_line1 = [11, 1200 , 15, "Switzerland", 30, "Friday"]

# create a new DataFrame with the same column_names as fd1 ...
df_to_add = pd.DataFrame([insert_line1],columns=column_names )
# NOTE: insert_line1 is in brackets because the first level a list of lists is expected for multiple rows!

# use 'concat()'' to 'glue' the two DataFrames together: 
df2 = pd.concat([df1, df_to_add])

# NOTE: the index has not been changed! -> fix that with reset_index()
df3 = __FILL_HERE__

