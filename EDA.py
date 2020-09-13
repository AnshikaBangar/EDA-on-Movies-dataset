import pandas as pd
from pandas import Series
#opening the csv file
filepath=r"C:\tmdb-movies(1).csv"
moviedata = pd.read_csv (filepath)
moviedata
moviedata.info()
#dropping duplicate columns if any
moviedata.drop_duplicates(inplace=True)
moviedata.info()
moviedata = moviedata[moviedata.budget >0]
#dropping null values 
moviedata.dropna(subset=['budget'], inplace=True)  
moviedata.info()
#keeping the required columns
md = moviedata[['budget','revenue','original_title','cast','runtime','genres','release_year','production_companies']]
md.head()
md.describe()
#movie with third highest budget
md.nlargest(3, 'budget').iloc[-1]
#movie with third lowest budget
md.nsmallest(3, 'budget').iloc[-1]
#movie with most earned revenue
md.nlargest(1, 'revenue')
#movie with least earned revenue
md.nsmallest(1, 'revenue')
#average runtime of movies in 2006
grouped_df = md.groupby('release_year').mean()['runtime']
print(grouped_df.loc[[2006]])
#splitting the production comanies
s = md['production_companies'].str.split('|').apply(Series, 1).stack()
s.index = s.index.droplevel(-1)
s.name = 'production_companies'
del md['production_companies']
md_production_companies_split= md.join(s)
md_production_companies_split.head()
#zipping original_title and production_companies in a dictionary
mydict = dict(zip(md.original_title,md_production_companies_split["production_companies"]))
mydict
