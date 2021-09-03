FROM ubuntu

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y python3

RUN apt-get install -y python3-pip

RUN pip3 install flask flask-sqlalchemy flask-wtf email_validator flask-bcrypt flask-login Pillow flask-mail

WORKDIR full-featured-web-app

COPY . .

EXPOSE 5000

CMD ["python3", "run.py"]

#FROM alpine
#
#RUN apk update && apk add python3 && apk add py3-pip
#
#RUN pip3 install flask flask-sqlalchemy flask-wtf email_validator flask-bcrypt flask-login Pillow
#
#WORKDIR full-featured-web-app
#
#COPY . .
#
#EXPOSE 5000
#
#CMD ["python3", "run.py"]