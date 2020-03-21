# divi-crawler

Web crawler for data at divi.de
(Deutsche interdisziplinäre Vereinigung fir Intensiv- und Notfallmedizin).

## Setup instructions

1. Install development dependencies for Python 3.7:

    ``` bash
    python3.7 -m pip install -r requirements.txt
    ```

2. Call the crawler script:

    ``` bash
    python3.7 scripts/divi-icu-beds.py
    ```

## Steps for commiting the .json file into the "data" folder on GitHub

1. Run Setup Instructions above.

2. Generate a "personal access token" on GitHub:

    At your GitHub account: "Settings" -> "Developer Settings" -> "Personal access tokens" -> "Generate new token".

3. Generate a file "config.py"  

    (like [config.py.example](https://github.com/codeformuenster/divi-crawler/blob/master/config.py.example))
    and copy your personal access token into the file.

    **Note: Treat your personal access token like a password and NEVER check in your config.py.**

4. Call the auto_commit script:

    ``` bash
    python3.7 scripts/autocommit.py
    ```
