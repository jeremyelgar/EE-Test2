FROM python:3.12-slim

ARG USER=process

RUN addgroup --system $USER && adduser --system --group $USER
WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

USER $USER

COPY src/main.py /usr/src/app/

ENTRYPOINT ["python3", "main.py"]
