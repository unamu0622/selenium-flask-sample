FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /opt/app
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

# gnupg
RUN apt-get update \
  && apt-get install -my wget gnupg

# google-chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list && \
apt-get update && \
apt-get install -y google-chrome-stable

CMD gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
