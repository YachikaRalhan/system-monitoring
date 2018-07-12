
FROM python:2.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app

EXPOSE 8089

CMD ["python", "flaskApp.py"]
