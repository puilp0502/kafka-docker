import sys
import os
import json
import time
import binascii
from tqdm import tqdm
from confluent_kafka import Producer


TOPIC = "test-topic"
MSG_COUNT = 2 ** 22

def main(acks):
    producer_config = {
        "bootstrap.servers": "kafka-01:9092",
        "acks": acks,
        "enable.idempotence": "true",
        "linger.ms": "1000",
        "compression.type": "zstd",
    }
    payload_data = binascii.hexlify(os.urandom(2048)).decode('ascii')
    payload = json.dumps({"data": payload_data})
    p = Producer(**producer_config) 
    try:
        start = time.time()
        for i in tqdm(range(MSG_COUNT)): 
            while True:
                try:
                    p.produce(TOPIC, payload, key=str(i))
                except BufferError:
                    p.poll()
                    time.sleep(0.005)
                    continue
                else:
                    break
    except KeyboardInterrupt:
        pass
    finally:
        p.flush()
        end = time.time()

    print(f"MPPS: {i/(end - start)}")

if __name__ == "__main__":
    print(sys.argv[1])
    main(sys.argv[1])

