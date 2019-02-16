FROM python

RUN mkdir /app
COPY . /app
RUN pip install -r /app/requirements.txt

CMD ["/usr/local/bin/gunicorn", "--config", "/app/gunicorn.conf", "app"]
