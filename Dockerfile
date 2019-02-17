FROM python
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r /app/requirements.txt

CMD ["/bin/bash", "start.sh"]
