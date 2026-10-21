import sys

import pandas as pd

print("argument",sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2], "passengers_num": [3, 4]})
df['momth']= month
print(df.head())

df.to_parquet(f"output_month : {month}.parquet")

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")

print(f"Hello, World! , month = {month}")