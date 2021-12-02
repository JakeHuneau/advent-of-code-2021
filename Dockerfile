FROM python:latest

ENV day 0

COPY . ./

CMD python advent_of_code.py ${day}