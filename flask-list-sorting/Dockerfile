# Please run below commands in the same order to create a docker container
# 1- docker build --tag sort-api .
# 2- docker run -d -p 8000:5000 sort-api
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
