""" Scraping ICU bed counts for Corona patients from divi.de """

from divi import io, mongodb_upload, scraper

URL = "https://www.divi.de/images/register/report2v.html"

# get script data from data source
script_tag = scraper.scrape_script_tag(URL)
# extract ICU report from script tag
icu_report = scraper.extract_icu_report(script_tag)
# extract relevant data from ICU report
status, source, dataset, states = scraper.fields_from_report(icu_report)
# compile metadata
meta = io.metadata_to_dict(source=source, status=status, dataset=dataset)
# save result to JSON
io.results_to_json(meta, states)
# upload to mongodb
try:
    mongodb_upload.insertData(states, meta)
except:
    pass
