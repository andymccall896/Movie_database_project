####### Trying to extract a movie list of names to search for
#####https://towardsdatascience.com/how-to-create-simple-keyword-based-movie-recommender-models-from-scratch-afde718636c9'
######https://datasets.imdbws.com/

name_basics = pd.read_csv(r'C:/Users/andym/Desktop/Datafancy/Movie API/name.basics1.tsv.gz', sep='\t', header=0)

title_basics = pd.read_csv(r'C:/Users/andym/Desktop/Datafancy/Movie API/title.basics.tsv.gz', sep='\t', header=0)
title_basics["titleType"].unique()
title_basics_movie["startYear"].unique()
title_basics_movie = title_basics[title_basics['titleType'] == 'movie']
title_basics_movie = title_basics_movie[title_basics_movie["startYear"] != '//N']
title_basics_movie = title_basics_movie[title_basics_movie["startYear"] != '/N']

title_basics_movie = title_basics_movie[title_basics_movie["startYear"] != '\\N']
title_basics_movie = title_basics_movie[title_basics_movie["startYear"] != '\N']


#title_basics_movie['startYear'] = title_basics_movie['startYear'].replace(r'\N','', regex=True)
#title_basics_movie['startYear'] = title_basics_movie['startYear'].replace('\\','', regex=True)
#title_basics_movie = title_basics_movie[title_basics_movie["startYear"] != '']

#title_basics_movie['startYear'].rstrip("\N")
#title_basics_movie.to_csv(r"C:/Users/andym/Desktop/Datafancy/Movie API/testing.csv")


#title_basics_movie["startYear"].unique()

#title_basics_movie.drop(index = ['//N','/N'])

title_basics_movie['startYear'] = pd.to_numeric(title_basics_movie['startYear'])
title_basics_movie_2015_2020 = title_basics_movie[(title_basics_movie.startYear >= 2015) & (title_basics_movie.startYear<= 2021)]

title_basics_movie_2015_2020['primaryTitle'].iloc[0:40]


total_movielist = []

for id,i in enumerate(title_basics_movie_2015_2020['primaryTitle'].iloc[0:1000]):
    total_movielist.append(movie.search(i))

total_movielist_collapsed = []
for i in total_movielist:
    for g in i:
        total_movielist_collapsed.append(g)

    print(len(total_movielist_collapsed))

#total_movielist_df = pd.DataFrame(columns = pd.DataFrame(dict(total_movielist_collapsed[0])).columns)
total_movielist_df = []

################################################################################
##### we might need to check and see if there is a problem with number of columns
for id,i in enumerate(total_movielist_collapsed):
    if len(i) <= 13:
        pass
    else:
        total_movielist_df.append(pd.DataFrame(dict(i)))
total_movielist_df = pd.concat(total_movielist_df)

total_movielist_df.shape
total_movielist_df.columns




#len(empty[1])
#dict(total_movielist_collapsed[0])['adult']
#dict(total_movielist_collapsed[219])
#dict(empty[641])
#641
#total_movielist_df = pd.DataFrame(columns= [list(flatten(total_movielist))[0]])
##### There is duplications from the genre ID
##### Might need to figure out how to reorganise the the columns so I can start appending datasets together
#pd.DataFrame(dict(total_movielist_collapsed[0]))
#pd.DataFrame(dict(total_movielist_collapsed[2935]))
#pd.DataFrame(dict(total_movielist_collapsed[219]))
#d.DataFrame(dict(total_movielist_collapsed[2953]))
#pd.DataFrame(dict(total_movielist_collapsed[2936]))
#lst = [[] for i in range(len(total_movielist))]
#len(lst)

#for idd,i in enumerate(total_movielist):
#    for id,p in enumerate(i):
#        lst[idd].append(p.adult)
#        lst[idd].append(p.backdrop_path)
#        lst[idd].append(p.genre_ids)
#        lst[idd].append(p.id)
#        lst[idd].append(p.original_language)
#        lst[idd].append(p.original_title)
#        lst[idd].append(p.overview)
#        lst[idd].append(p.popularity)
#        lst[idd].append(p.poster_path)
#        lst[idd].append(p.release_date)
#        lst[idd].append(p.title)
#        lst[idd].append(p.video)
#        lst[idd].append(p.vote_average)
#        lst[idd].append(p.vote_count)

