from kafka import KafkaProducer
import time
import csv
import sys
import argparse

def main():
    
    parser = argparse.ArgumentParser(description='A simple Kafka Producer')
    
    parser.add_argument('-s', '--source', dest='source_file', default='/home/rpirrone/data/passengers.csv')
    parser.add_argument('-b', '--bootstrap-server', dest='bootstrap_servers', default='localhost:9092')
    parser.add_argument('-t', '--topic', dest='topic', default='titanic')
    parser.add_argument('-i', '--interval', dest='interval', default=1)

    args = parser.parse_args()
    
    print("Kafka producer application started ...")
    
    kafka_producer_obj = KafkaProducer(bootstrap_servers=args.bootstrap_servers)
    
    message = None
    
    with open(args.source_file, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for messages in reader:
            key = messages[0]
            message = ','.join(messages[1:])
            print(key, message)
            kafka_producer_obj.send(args.topic, \
                key = bytes(key, 'utf-8'), \
                value = bytes(message,'utf-8'))
            time.sleep(float(args.interval))

if __name__ == "__main__":
    main()