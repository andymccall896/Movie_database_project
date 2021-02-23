###https://monashdatafluency.github.io/python-web-scraping/section-3-API-based-scraping/

import wikipedia
import wikipedia
import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import json
import wptools
import wikipedia
import pandas as pd
import re
from tmdbv3api import TMDb
tmdb = TMDb()
tmdb.api_key = '9e7c7a17fab891aa31bde9cdbada3930'
from tmdbv3api import Movie
from itertools import chain

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
