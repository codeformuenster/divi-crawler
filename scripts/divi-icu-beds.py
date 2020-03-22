import calendar
import json
import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup

import mongoDBUpload

# Set headers
headers = requests.utils.default_headers()
headers.update(
    {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
    }
)

url = "https://www.divi.de/images/register/report2v.html"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, "html.parser")
script_tag = soup.body.script


# Get icu report
start_string = '{"config"'
end_string = "]}}"
result = re.search(start_string + "(.*)" + end_string, str(script_tag)).group(1)
full_result = start_string + result + end_string
icu_report = json.loads(full_result)

status = icu_report["vconcat"][0]["layer"][0]["title"]["subtitle"][0]
source = icu_report["vconcat"][0]["layer"][0]["title"]["subtitle"][1]
dataset = list(icu_report["datasets"].keys())[0]
states = icu_report["datasets"][dataset]

for state in states:
    del state["geometry"]

result = {}

meta = {}
meta["source"] = source
meta["status"] = status


# Add timestamp
utc_date = datetime.utcnow()
unix_utc = calendar.timegm(utc_date.utctimetuple())
iso_utc = utc_date.strftime("%Y%m%dT%H%M%SZ")

meta["unix_timestmap"] = unix_utc
meta["iso_timestamp"] = iso_utc

try:
    mongoDBUpload.insertData(states, meta)
except:
    pass

result["meta"] = meta
result["states"] = states

filename = "data/icu-beds-" + str(iso_utc) + ".json"

with open(filename, "w", encoding="utf8") as outfile:
    json.dump(result, outfile, indent=4, ensure_ascii=False)
