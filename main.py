import pandas as pd
# here we are loding/activating the pandas library as pd. Moving forward, if we have to use any functions from the pandas library
# we can simply use pd, insted of writing pandas as in whole.
df = pd.read_csv("https://query.data.world/s/mcnmncx7l5q4clmnqwl27lmeg4nvql")
# here we have loaded the data in to the variable df
df.head()
#top 5 rows of the data
df.tail()
#bottom 5 rows of the data
#How to extract one column from the dataframe?
df['Churn']
# we write the namne of the column within the square brackets
df[df['gender']=='Male']
# filter data on one condition.
df[(df['gender']=='Male') & (df['Churn'] == 'Yes')]
# filter data on more than one condition
#How to group and aggregate the data
df.groupby('gender').agg({'tenure':'mean'})
# here we have grouped the data gender wise to find the average tenure
# Value Counts Function
# Return the count of various categories/values in a column in descending order of the count
df['gender'].value_counts()


