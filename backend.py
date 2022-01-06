#Part 1
#Function 1
def get_matches(dic,string1,value):
  empty = []
  for s in dic:
    x = s.get(string1)
    if x == value:
      empty.append(s)
  return empty

#Function 2
def list_descriptions(dic):
  empty = []
  for s in dic:
    x = s.get('tow_description')
    if x not in empty:
      empty.append(x)
  return empty  

#Function 3
def count_by_month(dic):
  empty = []
  empty_month = []
  for s in dic:
    x = s.get('tow_date')
    month = int(x[5]+x[6])
    empty_month.append(month)
  for d in range(12):
    count = 0
    for months in empty_month:
      if months == (d + 1):
        count = count + 1
    empty.append(count)
  return empty
  
#Function 4
def count_by_day(dic):
  empty = []
  empty_day = []
  for s in dic:
    x = s.get('tow_date')
    day = int(x[8]+x[9])
    empty_day.append(day)
  for d in range(31):
    count = 0
    for days in empty_day:
      if days == (d + 1):
        count = count + 1
    empty.append(count)
  return empty