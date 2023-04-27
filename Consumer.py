from kafka import KafkaConsumer
import json


if __name__ == '__main__':
    consumer = KafkaConsumer('registered_user',
                             bootstrap_servers='localhost:9092',
                             auto_offset_reset='earliest',
                             group_id='consumer-grp-a')
    for msg in consumer:
        print('{}'.format(json.loads(msg.value)))