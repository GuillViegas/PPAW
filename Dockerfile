FROM python:3.8

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /candle_app/ppaw 

COPY app/requirements.txt /candle_app/

ADD app/src /candle_app/
ADD ppaw /candle_app/ppaw/

WORKDIR /candle_app
RUN pip install -r requirements.txt
RUN pip install ppaw/