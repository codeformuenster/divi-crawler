"""
automatic commit of daily parkleitsystem and waiting time data .csv file
"""
import os
import sys

sys.path.append(".")
import config as cfg

GIT_URL = "https://" + cfg.token + "@github.com/codeformuenster/divi-crawler.git"

# pull latest changes from remote
os.system(f"git pull {GIT_URL}")
# add and commit new data
os.system("git add data/")
os.system('git commit -m "add scraped data"')
# push to remote
os.system(f"git push {GIT_URL}")
