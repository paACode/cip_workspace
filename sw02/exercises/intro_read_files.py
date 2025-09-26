"""
Content:
- read different formats with paratmers
- handle index
- altering data frames
- dimensions of data frames
- read from web directly
"""

# intro in pandas: Read files

import pandas

# we read from a CSV-File ...

df1 = pandas.read_csv("traffic.csv")

# we read from a Excel-File "traffic.xlsx":
df2 = __FILL_HERE__

# we read from a JSON-File "traffic.json"
df3 = __FILL_HERE__

# first line: header or no header?  Documentation look for parameter 'header'!

df4 = __FILL_HERE__

# what's wrong?
df4 = pandas.read_csv("traffic.csv", header = True)

# ok: header = 2   or  header = [1,2,5] ... let's try:

df5 = pandas.read_csv("traffic.csv", header = 2)

# try to use => header = [ 2, 4, 5]
df6 = __FILL_HERE__

# we go back to df2
# 'Date' should be the 'index'  (row labels!!)

df2 = pandas.read_excel("traffic.xlsx")

# set a new index e.g. the column "Date":   (use 'set_index()')

__FILL_HERE__

# or put the column 'Day' as index:  (use 'set_index()')

__FILL_HERE__

# what is the dimensionality of a DataFrame
# important command if we get some new data from e.g. an API
# give out the  dimensionality of the DataFrame   (have a look in the docu for 'shape')

__FILL_HERE__

# distinguish between altering the existing dataframe, creating a new reference and creating a new object! (documentation .copy(), 'deepcopy') 

df7 = df2.set_index("Day")
__FILL_HERE__                       # print out: df7
__FILL_HERE__                       # print an empty line
__FILL_HERE__                       # print out: df2     => compare with df7 ...! 

# open a csv-file with different delimiter  e.g. ','   or ';'
# standard - delimiter for csv-files is ','

# open the file "traffic-commas.txt" with standard delimiter ',': 

df8 = pandas.read_csv(__FILL_HERE__)

# open the file "traffic-semi-colons.txt" with not-standard delimiter ';'

df9 = pandas.read_csv(__FILL_HERE__)

# download some data from different CSV-API's

# for example: 
# http://www.sharecsv.com/s/9096d32f98aa0ac671a1cca16fa43be8/SalesJan2009.csv
# https://www.who.int/tb/country/data/download/en/
# https://extranet.who.int/tme/generateCSV.asp?ds=notifications    # a bigger data source

# read data from a online link direct (!) in a DataFrame: 

# https://www.who.int/tb/country/data/download/en/   # start site
# look for 'Global Tuberculosis Report' and 'Case notifications[2Mb] '

df11 = pandas.read_csv(__FILL_HERE__)

# get some data from a 'json-source' 'direct' in a Dataframe as an example: 
# try to get 'Chuck Norris'-joke from e.g. 'http://api.icndb.com/jokes/random/10'

df12 = pandas.read_json(__FILL_HERE__)

# Recommend :try out yourself: 

# https://next.json-generator.com/api/json/get/4yIPxvyGt
