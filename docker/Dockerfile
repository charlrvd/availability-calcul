FROM python:3

LABEL version="1.0"
LABEL maintainer="charlrvd"
LABEL description="Small app to calculate availability based on downtime input"

ADD . /
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "main:app"]
