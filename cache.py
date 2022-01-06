#Part 2
import csv
#Function 1
def read_csv_header(csv):
  header = next(csv)
  return header

#Function 2
def read_data(csv,key):
  lst = []
  for a in csv:
    dict = {}
    for b in range(len(key)):
      dict[key[b]] = a[b]
    lst.append(dict)
  return lst

#Function 3
def write_csv_header(csv,dict):
  lst = []
  for row in dict.items():
    for a in dict.keys():
      csv.writerow(a)
      lst.append(a)
    return lst

#Function 4
def write_dictionaries_to_csv(csv,dict,key):
  csv.writerow(key)
  for a in dict:
    lst = []
    for b in key:
      lst.append(a[b])
    csv.writerow(lst)

#Part 3
import urllib.request
import json
#Function 1
def get_data(string):
  url = urllib.request.urlopen(string)
  content = url.read().decode()
  blob = json.loads(content)
  return blob

#Function 2
def minimize_dictionaries(dl,sl):
  result = []
  for a in dl:
    dict = {}
    for b in a:
      for c in sl:
        if b == c:
          dict[b] = a.get(b,("District_A"))
    result.append(dict)
  return result

#Function 3
def write_cache(dl,filename):
  with open(filename,'w') as f:
    writer = csv.writer(f)
    keys = dl[0].keys()
    writer.writerow(keys)
    for a in dl:
      lst = []
      for b in keys:
        lst.append(a.get(b))
      writer.writerow(lst)

#Function 4
def read_cache(filename):
  lst = []
  with open(filename,'r') as f:
    reader = csv.DictReader(f)
    for a in reader:
      lst.append(a)
  return lst