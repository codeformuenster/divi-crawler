""" Utils for scraping """

import json
import re
import requests

from bs4 import BeautifulSoup


def scrape_script_tag(url: str) -> str:
    """ Scrape script tag """
    headers = requests.utils.default_headers()
    header_user_agent = (
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
    )
    headers.update({"User-Agent": header_user_agent})
    req = requests.get(url, headers)
    script_tag = BeautifulSoup(req.content, "html.parser").body.script
    return str(script_tag)


def extract_icu_report(script_tag: str) -> dict:
    """ extract icu report """
    start_string = '{"config"'
    end_string = "]}}"
    result = re.search(f"({start_string}(.*){end_string})", script_tag).group(1)
    icu_report = json.loads(result)
    return icu_report


def fields_from_report(icu_report) -> (str, str, str, dict):
    """ parse report to dict """
    status = icu_report["vconcat"][0]["layer"][0]["title"]["subtitle"][0]
    source = icu_report["vconcat"][0]["layer"][0]["title"]["subtitle"][1]
    dataset = list(icu_report["datasets"].keys())[0]
    states = icu_report["datasets"][dataset]
    for state in states:
        del state["geometry"]
    return status, source, dataset, states
