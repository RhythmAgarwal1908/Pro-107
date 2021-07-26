import pandas as pd 
import csv
import plotly.express as px
df=pd.read_csv("data.csv")
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
print(mean)
as_index=False
fig = px.scatter(df, x="student_id", y="level",
	         color="attempt",size="attempt")
fig.show()
