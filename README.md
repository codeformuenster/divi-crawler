# divi-crawler

Web crawler for data at divi.de
(Deutsche interdisziplinäre Vereinigung fir Intensiv- und Notfallmedizin).

## Steps for running the crawler

* Install dependencies, i.e. the python package BeautifulSoup:

  ```bash
  pip3 install bs4 requests pytz calendar
  ```

* Call the read_parkleitsystem_data script:

  ```bash
  python3.7 todo.py
  ```

## Steps for commiting the .csv file into the "data" folder on GitHub

* Generate a "personal access token" on GitHub:
  
  Go to your GitHub account "Settings", then "Developer Settings", "Personal access tokens" and "Generate new token".

* Generate a file "config.py"
  (like [config.dist.py](https://github.com/codeformuenster/parking-decks-muenster/blob/master/config.dist.py)) and copy your personal access token into the file. <br\>
  **Note: Treat your personal access token like a password and NEVER check in your config.py.**

* Switch the remote URL of your cloned parking-decks-muenster repository to HTTPS (if cloned with SSH):
  
  command is ``git remote set-url``; see [this explanation](https://help.github.com/en/articles/changing-a-remotes-url#switching-remote-urls-from-ssh-to-https))

* Call the auto_commit script:

  ```bash
  python3 auto_commit.py
  ```
