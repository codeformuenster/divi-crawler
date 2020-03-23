FROM python:3.7-slim
LABEL MAINTAINER="Code for Münster <muenster@codefor.de>"

RUN apt-get update && \
    apt-get install -y gcc git

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt
COPY setup.py /usr/src/app/setup.py
COPY divi /usr/src/app/divi

RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

COPY . /usr/src/app

RUN git config --global user.name "Code for Münster"
RUN git config --global user.email "muenster@codefor.de"
