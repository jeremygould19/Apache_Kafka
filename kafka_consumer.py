# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from kafka import KafkaConsumer
consumer = KafkaConsumer('sample', bootstrap_servers=['localhost:9092'])
for message in consumer:
    print (message)
