import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

print(data)

last_name = r'Love'
first_name = r'Kenneth'

#print(re.match(last_name, data))
#print(re.search(first_name, data))

#print(re.findall(r'\(?\d{3}\)? \d{3}-\d{4}', data))
#print(re.findall(r'\w*, \w*', data))
#print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
#print(re.findall(r'\b[trehous]{9}\b', data, re.I))


#print(re.findall(r'''
#                 \b@[-\w\d.]* #  find a word boundary, an @ and then any number of chars
#                 [^.gov\t]+  #  ignore 1+ instances of the letters 'g', 'o', or 'v' and a tab
#                 \b #  match another word boundary
#                 ''', data, re.VERBOSE|re.I))

#print(re.findall(r"""
#        \b[-\w]*, #  find a word boundary, +1 hyphens ot characters and a comma
#        \s #  Find 1 whitespace
#        [-\w ]* #  1+ hyphens and chars and explicit spaces
#        [^\t\n] #  ignore tabs and new lines
#""", data, re.X))

line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+)) \t #  last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t #  email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #  phone
    (?P<job>[-\w\s]+,\s[-\w\s.]+)\t? # job and company
    (?P<twitter>@[\w\d]+)?$ #twitter
''', re.X|re.M)

#print (line.search(data).groupdict())

#for match in line.finditer(data):
#    print('{first} {last} <{email}>'.format(**match.groupdict()))

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'''
    ^(?P<name>(?P<last_name>[-\w ]*),\s(?P<first_name>[-\w ]+)):\s #  last and first names
    (?P<score>\d+)$ #  score
''', string, re.X|re.M)

#print(players)

class Player:
  last_name = ''
  first_name = ''
  score = 0

  def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])

#string = 'Perotto, Pier Giorgio'

#names = re.match(r'''
#    ([\w ]+)
#    ,\s
#    ([\w ]+)
#''', string, re.X|re.M)

#print(names)
#print(line.groupdict())

#string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
#Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
#McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
#Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

#contacts = re.search(r'''
#    (?P<email>[-\w\d.+]+@[-\w\d.]+),\s #  email
#    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})? #  phone
#''', string, re.X|re.M)

#twitters = re.findall(r'''
#    (@[\w\d]+)$ #twitter
#''', string, re.X|re.M)

#print(contacts.groupdict())
#print(twitters)

