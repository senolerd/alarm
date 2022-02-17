FROM python:latest
RUN apt update && pip install --upgrade pip
WORKDIR /www
COPY . /wwww/alarm/alarm-backend
RUN pip install -r requirements.txt
EXPOSE 5000
CMD gunicorn run:app --bind 0.0.0.0:80 --access-logfile=logs/$(date +%m-%d-%Y)_access.log --error-logfile=logs/$(date +%m-%d-%Y)_error.log
