import bottle
import json
import backend
import os.path
import cache # This assumes that your functions from parts 2 & 3 are in a file named cache.py

def load_data():
   csv_file = 'cached_data.csv'
   if not os.path.isfile(csv_file):
       query_str = "?$limit=10000"
       url = "https://data.buffalony.gov/resource/5c88-nfii.json" + query_str
       data = cache.get_data(url)
       data = cache.minimize_dictionaries(data, ['tow_date', 'tow_description', 'police_district'])
       cache.write_cache(data, csv_file)

load_data()

@bottle.route('/')
def index():
  return bottle.static_file('index.html', root='')

@bottle.route('/myCode.js')
def java_script():
  return bottle.static_file('myCode.js', root='')

@bottle.route('/scatter')
def loadscatter():
  tows = cache.read_cache('cached_data.csv')
  day = backend.count_by_day(tows)
  return json.dumps(day)

@bottle.route('/pie')
def loadpie():
  tows = cache.read_cache('cached_data.csv')
  district_a = backend.get_matches(tows,'police_district','District A')
  district_b = backend.get_matches(tows,'police_district','District B')
  district_c = backend.get_matches(tows,'police_district','District C')
  district_d = backend.get_matches(tows,'police_district','District D')
  district_e = backend.get_matches(tows,'police_district','District E')
  districts = [district_a,district_b,district_c,district_d,district_e]
  total = len(district_a+district_b+district_c+district_d+district_e)
  lst = []
  for i in districts:
    lst.append(len(i)/total)
  return json.dumps(lst)

@bottle.route('/line')
def loadline():
  tows = cache.read_cache('cached_data.csv')
  descriptions = ['ILLEGAL VEHICLE', 'ACCIDENT', 'ABANDONED VEHICLE', 'STOLEN VEHICLE', 'ILLEGALLY PARKED', 'IMPOUNDED', 'GONE ON ARRIVAL']
  lst = []
  for things in descriptions:
    matches = backend.get_matches(tows,'tow_description',things)
    lst.append(backend.count_by_month(matches))
  return json.dumps(lst)

bottle.run(host='0.0.0.0', port=8080)