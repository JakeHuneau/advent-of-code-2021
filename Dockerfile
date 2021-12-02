FROM python:latest

ENV day 0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . ./

CMD python advent_of_code.py ${day}