FROM alpine

RUN apk update && apk add python3

RUN apk add py3-pip

RUN pip3 install flask

WORKDIR first-flask-project

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]