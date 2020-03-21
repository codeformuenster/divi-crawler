import calendar
import json
import re
from datetime import datetime

import pytz
import requests
from bs4 import BeautifulSoup

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


start_string = '{"config"'
end_string = "]}}"
result = re.search(start_string + "(.*)" + end_string, str(script_tag)).group(1)
full_result = start_string + result + end_string


icu_report = json.loads(full_result)
states = icu_report["datasets"]["data-aa709d382b996f70e1574ebd862b7ad1"]

for state in states:
    del state["geometry"]


mytz = pytz.timezone("Europe/Berlin")
dt = mytz.normalize(mytz.localize(datetime.now(), is_dst=True))
unix_utc = calendar.timegm(dt.utctimetuple())

filename = "data/icu-beds-" + str(unix_utc) + ".json"


with open(filename, "w", encoding="utf8") as outfile:
    json.dump(states, outfile, indent=4, ensure_ascii=False)
