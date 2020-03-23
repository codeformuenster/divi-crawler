""" Utils for saving data. """

import calendar
import json
from datetime import datetime


def metadata_to_dict(source: str, status: str, dataset: str) -> dict:
    """ Compile dictionary of metadata """
    meta = {}
    meta["source"] = source
    meta["status"] = status
    meta["dataset"] = dataset
    # add ISO timestamp
    utc_date = datetime.utcnow()
    iso_utc = utc_date.strftime("%Y%m%dT%H%M%SZ")
    meta["iso_timestamp"] = iso_utc
    # add UNIX timestamp
    unix_utc = calendar.timegm(utc_date.utctimetuple())
    meta["unix_timestmap"] = unix_utc
    return meta


def results_to_json(meta: dict, states: dict):
    """ save result to JSON """
    # compile results dict
    result = {}
    result["meta"] = meta
    result["states"] = states
    utc_date = datetime.utcnow()
    iso_utc = utc_date.strftime("%Y%m%dT%H%M%SZ")
    # save to json
    filename = "data/icu-beds-" + str(iso_utc) + ".json"
    with open(filename, "w", encoding="utf8") as outfile:
        json.dump(result, outfile, indent=4, ensure_ascii=False)
