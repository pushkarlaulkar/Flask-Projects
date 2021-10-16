FROM ubuntu

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y python3

RUN apt-get install -y python3-pip

RUN pip3 install flask flask-sqlalchemy flask-wtf email_validator flask-bcrypt flask-login Pillow flask-mail

WORKDIR notes-app

COPY . .

EXPOSE 5000

CMD ["python3", "main.py"]