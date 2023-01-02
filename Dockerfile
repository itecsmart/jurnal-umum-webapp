FROM python:3.9-slim-buster

WORKDIR /app

RUN apt update && apt install -y python3 libpq-dev make nano\
    libtiff5-dev libjpeg62-turbo-dev zlib1g-dev libfreetype6-dev \
    liblcms2-dev libwebp-dev gcc g++ libmagic-dev libffi-dev


RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt
EXPOSE 5000

COPY . .


CMD [ "python", "src/app.py"]