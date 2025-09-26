"""
Content:
- loc 
- iloc 
"""

# intro in pandas: Slicing DataFrame's

import pandas
df1 = pandas.read_csv("traffic.csv")

# slicing a DataFrame

#########
# loc
#########

# loc is 'label based' 
# NOTE: that contrary to usual python slices, both the start and the stop are included!

df13 = df1.loc[ __FILL_HERE__ ]    # loc [ 'row_label_slice'  , 'column_label_slice'  ]

# slicing from 'Country' to 'Days'

df14 = df1.loc[ __FILL_HERE__ ]

# NOTE: 'loc' is NOT an inplace operation
# check yourself: df1 is NOT changed!

# select only one 'value'
# index = 3 / column = "Clicks"

df15 = df1.loc[ __FILL_HERE__ ]

# select ALL rows from "Clicks"
df16 = df1.loc[ __FILL_HERE__ ]

# NOTE: if the result is only one column or one row => the type is changed and the result is now a 'Series' object!
# check yourself: 

__FILL_HERE__

#########
# iloc
#########

# index-loc => iloc, look for index (=rows)!
# iloc is 'position based' 

df17 = df1.iloc[  __FILL_HERE__  ]

# we can also slice one index (=row)  Note: index '0'  is row '1'! 
# e.g. index = 6 / columns = 1 bis 4 

df18 = df1.iloc[ __FILL_HERE__ ]

# question: What is the 'type' of the result in the last cell?

__FILL_HERE__

# ... and we can also select only one value:

df19 = __FILL_HERE__

# is there also a 'mean' command in DataFrames?
# use 'dir' to find out   

dir(df1)

