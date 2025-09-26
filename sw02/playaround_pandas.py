import pandas as pd

lst = [1,2,3,4,5,6]
print(lst[2:5]) # Excludes last element

print(type(lst))


ddf = {'a': [1,2,3,4,5], 'b': [11,22,33,44,55], 'c': [111,222,333,444,555], 'd': [1111,2222,3333,4444,5555]}
ddf = pd.DataFrame(ddf)
print(type(ddf))

# Label Based search
print(ddf)
print(ddf.loc[1:3, 'b':'c'])
print(ddf.loc[1:3, ])

#Index Based search
print(ddf.iloc[1:3, 1:2]) # this excludes the last index like in list