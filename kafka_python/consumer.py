from kafka import KafkaConsumer
import time
import sys
import argparse

def main():    

    parser = argparse.ArgumentParser(description='A simple Kafka Consumer')
    
    parser.add_argument('-b', '--bootstrap-server', dest='bootstrap_servers', default='localhost:9092')
    parser.add_argument('-t', '--topic', dest='topic', default='titanic')
    
    args = parser.parse_args()
    print("Kafka consumer application started ...")

    consumer = KafkaConsumer(args.topic,\
                                bootstrap_servers=args.bootstrap_servers,\
                                auto_offset_reset='latest',\
                                enable_auto_commit=True)
    
    print('Reading messages from kafka topic about to start ...')
    
    message_list = []
    
    for message in consumer:
        print('Key: ', message.key)
        output_message = message.value
        print(type(message.value))
        print('Message received: ',output_message)
        message_list.append(output_message)
        time.sleep(1)

if __name__ == "__main__":
    main()
