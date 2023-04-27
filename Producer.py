from kafka import KafkaProducer
import json
from data import get_registered_user
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


def get_partition(key_bytes, all_patitions, available_partitions):
    return 0


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer,
                         # partitioner=get_partition
                         )

if __name__ == '__main__':
    for i in range(20):
        usr = get_registered_user()
        producer.send(topic='registered_user',
                      value=usr)
        print(usr)
