""" Utils for scraping """

import json
import re
import requests

from bs4 import BeautifulSoup


def scrape_html_body(url: str) -> str:
    """ Scrape script tag """
    headers = requests.utils.default_headers()
    header_user_agent = (
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
    )
    headers.update({"User-Agent": header_user_agent})
    req = requests.get(url, headers)
    body = BeautifulSoup(req.content, "html.parser").body
    return str(body)


def extract_icu_report(body: str) -> dict:
    """ extract icu report """
    start_string = r'vegaEmbed\("#right", '
    end_string = r', {"renderer": "canvas", "actions": false}\);'
    result = re.search(f'{start_string}(.*){end_string}', str(body)).group(1)
    icu_report = json.loads(result)
    return icu_report


def fields_from_report(icu_report) -> (str, str, str, dict):
    """ parse report to dict """
    status = icu_report["layer"][0]["title"]["subtitle"][0]
    source = icu_report["layer"][0]["title"]["subtitle"][1]
    # get dataset
    dataset_key = list(icu_report["datasets"].keys())[0]
    states = icu_report["datasets"][dataset_key]
    for state in states:
        del state["geometry"]
    return status, source, dataset_key, states
