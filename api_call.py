# import urllib library
from urllib.request import urlopen
# import json
import json
# store the URL in url as
# parameter for urlopen

#Question 1 - The /site/{city} endpoint of the API returns an asset hierarchy given a location ( i.e., city).
# How many assets (in total) does the API returns across all sites? Hint: You can use keyword all as city to get all assets
url = "https://ice-cream-factory.inso-internal.cognite.ai/site"
response = urlopen(url)
data_json = json.loads(response.read())
#print(data_json)
site_names =[]
for d in data_json:
    #print(d["name"])
    site_names.append(d["name"])
print(site_names)
print(len(site_names))

#Question 2 - Filtering the /site/{city} endpoint of the API to city oslo,
# how many child assets does the api return?
# Hint: child assets do not include the asset for the city itself, but only the sub assets.
url = "https://ice-cream-factory.inso-internal.cognite.ai/site/oslo"
response = urlopen(url)
data_json = json.loads(response.read())
child_eid =[]
for d in data_json:
    if d.get('parent_external_id', None) =='oslo':
        #print(d['external_id'])
        child_eid.append(d['external_id'])
print(child_eid)
print(len(child_eid))

#Question 3 - The /timeseries/entity_matching endpoint returns the metadata for availble timeseries relevant for entity_matching (following chapters will explain more details on entity matching).
# Each timeseries has a type as part of the metadata. How many different type are there and what are the types?

url = "https://ice-cream-factory.inso-internal.cognite.ai/timeseries/entity_matching"
response = urlopen(url)
data_json = json.loads(response.read())
types =[]
for d in data_json:
    if d.get('metadata', None):
        #print(d['external_id'])
        types.append(d['metadata']['type'])
print(set(types))

# Question 4 - The /timeseries/oee endpoint returns the metadata for availble timeseries relevant for entity_matching (following chapters will explain more details on oee).
# Each timeseries has a type as part of the metadata. How many different type are there and what are the types?

url = "https://ice-cream-factory.inso-internal.cognite.ai/timeseries/oee"
response = urlopen(url)
data_json = json.loads(response.read())
types =[]
for d in data_json:
    if d.get('metadata', None):
        #print(d['external_id'])
        types.append(d['metadata']['type'])
