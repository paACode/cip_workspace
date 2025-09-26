import numpy as np

# curl https://swapi.dev/api/planets | sed 's/,/\n/g'
import pandas as pd
import requests as re
import pandas as pd

url = "https://swapi.dev/api/planets"

data = re.get(url, )

dd = data.json()
dd_df = pd.DataFrame(dd)

results_df = dd_df["results"]

print(dd_df)

print(type(dd_df.loc[0, "results"]))


# Search for specific planet
#curl https://swapi.dev/api/planets/?search=Haruun Kal | sed 's/,/\n/g'

haruun =re.get(url,params={"search": "Haruun Kal"})
haruun_dd = haruun.json()
print(haruun_dd)
haruun_lst = haruun_dd["results"]
haruun_df =pd.DataFrame(haruun_lst)
print(haruun_df)
print(haruun_df.loc[:, "population"])