FROM python:3.7-slim
LABEL MAINTAINER="Code for Münster <muenster@codefor.de>"

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN apt-get update && \
    apt-get install -y gcc git
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

RUN git config --global user.name "Code for Münster"
RUN git config --global user.email "muenster@codefor.de"

CMD ["python", "scripts/divi-icu-beds.py", "&&", "python", "scripts/autocommit.py"]
