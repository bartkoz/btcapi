FROM python:3.8.7-slim

ENV PYTHONUNBUFFERED 1
ENV PIPENV_SYSTEM 1
ENV PYTHONPATH /opt/app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gettext \
    python3-gdal \
    build-essential \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev shared-mime-info \
    git \
&& rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

COPY requirements.txt /opt/app/
WORKDIR /opt/app
RUN pip install -r requirements.txt

COPY . /opt/app
