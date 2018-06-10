# execute the 2nd line to run the script
# python .\average_ratings.py .\movie_list.txt .\movie_ratings.csv output.csv
import sys
import pandas as pd
import difflib
import numpy as np

movie_list = sys.argv[1]
movie_ratings = sys.argv[2]
output_file = sys.argv[3]

movie_title = open(movie_list).read().split('\n')
df = pd.DataFrame(data=movie_title, columns=['title'])  #about 50 movies
movie_and_ratings = pd.read_csv(movie_ratings) # two columns: title, rating

def get_average(movie):
    matched_movies = pd.Series(data=difflib.get_close_matches(movie, movie_and_ratings['title'], n=30))
    average_rating = movie_and_ratings[movie_and_ratings['title'].isin(matched_movies)]['rating'].mean()
    return round(average_rating, 2)

df['ratings'] = df['title'].apply(get_average)

#get rid of the movies that have no ratings 
df = df[np.isnan(df['ratings'])==False]
df.to_csv(output_file)