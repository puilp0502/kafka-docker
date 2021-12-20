import sys
import os
import json
import time
import binascii
from tqdm import tqdm
from confluent_kafka import Consumer


TOPIC = "test-topic"
MSG_COUNT = 2 ** 22

def msggen(c):
    while True:
        yield c.poll()

def main():
    consumer_config = {
        "bootstrap.servers": "localhost:9091",
        "group.id": "consumer-01",
        "enable.auto.commit": False,
        "auto.offset.reset": "earliest",
    }
    c = Consumer(**consumer_config) 
    c.subscribe([TOPIC])
    for msg in tqdm(msggen(c)):
        pass
        # Do something
        # c.commit()

if __name__ == "__main__":
    main()

