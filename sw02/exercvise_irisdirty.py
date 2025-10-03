
import pandas as pd

url = "https://raw.githubusercontent.com/DJCordhose/ml-examples/master/datasets/Iris/iris_dirty.csv"
iris_df = pd.read_csv(url, header=None)

print(iris_df.shape)
print(iris_df.info()) # like str() in R
print(iris_df.describe())

