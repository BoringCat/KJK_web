FROM python:3-alpine

RUN set -xe\
 && pip install -U flask tornado

WORKDIR /app
COPY *.py /app/

RUN set -xe\
 && python -m compileall .\
 && rm -rf *.py\
 && for n in __pycache__/*.pyc; do mv $n `echo ${n/__pycache__\/} | sed 's/\.cpy.*\././g'`; done\
 && rm -rf __pycache__/

ENTRYPOINT [ "python", "/app/app.py" ]