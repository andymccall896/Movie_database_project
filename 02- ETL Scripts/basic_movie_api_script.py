
###########################################
### Trying to checkout the tmdbv3api package and extract data 
###https://pypi.org/project/tmdbv3api/
import pandas as pd
from tmdbv3api import TMDb
tmdb = TMDb()
tmdb.api_key = '9e7c7a17fab891aa31bde9cdbada3930'

from tmdbv3api import Movie

movie = Movie()

recommendations = movie.recommendations(movie_id=111)

for recommendation in recommendations:
    print(recommendation.title)
    print(recommendation.overview)



movie = Movie()
popular = movie.popular()

movie.now_playing()
movie.keywords('Shark')
movie.language('en')
movie.release_dates
import json
json.dumps(popular[0])

movie = tmdb.Movies(603)

tmdb.Movies(603).info()

type(popular[0])


movie.search()

movie_df = pd.DataFrame()
for p in popular:
    print(p.id)
    print(p.title)
    print(p.overview)
    print(p.poster_path)

pd.DataFrame(popular)



discover = Discover()
movie = discover.discover_movies({
    'certification_country': 'US',
    'certification.lte': 'G',
    'sort_by': 'popularity.desc'
})




total_movielist = []
#dsadas = []
#movie = Movie()
#die = movie.search('Die hard')
#die['title']