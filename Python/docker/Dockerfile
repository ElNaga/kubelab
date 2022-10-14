FROM python:3.8

COPY . .

RUN pip install flask
EXPOSE 8080
CMD [ "flask","--app","main", "run", "--host=0.0.0.0"]