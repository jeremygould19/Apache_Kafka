#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 11:52:10 2018

@author: jeremygould
"""

from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
print("running kafka producer")
producer.send('sample', b'Hello, World!')
producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')
