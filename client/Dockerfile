FROM python:3.8

WORKDIR /app
RUN apt-get update && apt-get install iproute2 iputils-ping -y
RUN pip install tqdm confluent_kafka

ENTRYPOINT ["/bin/sleep", "365d"]
