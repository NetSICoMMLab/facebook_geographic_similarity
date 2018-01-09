import unicodecsv
import json
observations = []
for blob in str.split(open("fbdata.json").read(), "\n"):
  observations.append(json.loads(blob))

from collections import Counter
co_appearance_in_photos = Counter()
for observation in observations:
  for photo in observation["photos"]["data"]:
    for alter in set([p["id"] for p in photo["tags"]["data"] if "id" in p.keys()])-set([observation["id"]]):
      co_appearance_in_photos.update([observation["id"]+"->"+alter])


f = open("edgelist_co_appearance_photos.csv", "w")
w = unicodecsv.writer(f, encoding='utf-8')
for key in co_appearance_in_photos.keys():
    source, target = str.split(str(key), "->")
    weight = co_appearance_in_photos[key]
    w.writerow([source,target,weight])

f.close()