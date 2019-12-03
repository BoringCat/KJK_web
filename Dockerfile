FROM python:3-alpine

RUN mkdir /app\
 && pip install -U flask tornado

WORKDIR /app
COPY *.py /app/
COPY web/index.html /app/web/

ENTRYPOINT [ "python", "/app/app.py" ]