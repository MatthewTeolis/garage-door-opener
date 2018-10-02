FROM resin/raspberry-pi-python:2-slim

WORKDIR /home
COPY . .

EXPOSE 8081

RUN pip install -r requirements.txt

CMD ["python", "server.py"]