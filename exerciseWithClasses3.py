
import pandas as pd

df=pd.read_csv("measures.txt", sep=";")

print(df)
print(df.describe())
while True:
    city=input("Enter a city name or stop")
    if city=="stop": break
    if city in df["City name"].values:
        res=df.loc[df["City name"] == city].mean()
        print(f"mean temperatures for {city} is {res.temperature}")
    else:
        print(f"{city} is unknown")