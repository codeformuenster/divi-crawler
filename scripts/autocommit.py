"""
automatic commit of daily parkleitsystem and waiting time data .csv file
"""
import os
import config as cfg

os.system("git add data/")

os.system('git commit -m "add scraped data"')

os.system(
    "git push https://" + cfg.token + "@github.com/codeformuenster/divi-crawler.git"
)
