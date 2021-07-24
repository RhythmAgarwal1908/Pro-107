import pandas as pd 
import csv
import plotly.express as px
df=pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())
as_index=False
fig = px.scatter(df, x="student_id", y="level",
	         color="attempt",size="attempt")
fig.show()
