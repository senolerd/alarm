FROM python:latest
RUN apt update && pip install --upgrade pip 
COPY . /wwww
WORKDIR /www
EXPOSE 5000
CMD ./run.sh
