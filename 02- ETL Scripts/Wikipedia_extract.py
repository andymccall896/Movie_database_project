
#page = wikipedia.page("goodfellas")
#goodfellas.summary
#goodfellas.content
#wikipedia.search("goodfellas")
#page = wptools.page('goodfellas')
#page.get_parse() 
#type(page.data['infobox'])
#pd.DataFrame.from_dict(page.data['infobox'].index)
#typeewq,ewq= zip(*page.data['infobox'].items())
#pd.DataFrame(typeewq,ewq)


title_basics_movie_2015_2020.columns 
title_basics_movie_2015_2020['originalTitle'].iloc[10]

page.data['infobox']

page = wptools.page()
page.get_query()
page = wptools.page('Mariette in Ecstasy')
page.data['infobox']
page.get_parse()
pafe.parse




wptools_list = []
for i in title_basics_movie_2015_2020['originalTitle']:
      wptools.page(i)
   wptools_list.append(page.data['infobox'])   







page.get_parse()

list(page.data['infobox'])[1]

info_box_df = pd.DataFrame(dict(page.data['infobox']).items(),columns = ['one','two'])

info_box_df.iloc[:,0]
info_box_df['one']

tuple(list(info_box_df['one']) , list(info_box_df['two']))


info_box_df.pivot_table(index = info_box_df.index,columns = ['one'],values=['two'])

info_box_df.pivot(index = info_box_df.index,columns = ['one'])
info_box_df.index

empty = [[]]

for id,i in enumerate(page.data['infobox'].items()):
    empty.append(i)

pd.DataFrame(empty).pivot(columns = 0,values = 1)

df = pd.DataFrame(empty,columns = ['one','two'])

pd.pivot_table(df,columns = ['one'] ,values = ['two'] )

df.pivot(df,columns = ['one'] ,values = ['two'] )

pd.DataFrame(df.set_index('one').T).columns


dsad, dsa = page.data['infobox'].items()

len(list(page.data['infobox']))

for i in page.data['infobox']:
        print(i)