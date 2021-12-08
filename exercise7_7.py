import json
import urllib.request
from collections import Counter
import var_dump as vd
url = "https://liukastumisvaroitus-api.beze.io/api/v1/warnings"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
dontslip = json.loads(raw_data)

#vd.var_dump(dontslip)
print(Counter(dontslip))
