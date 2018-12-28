# -*- coding: utf-8 -*-

from influxdb import InfluxDBClient
import random
import math
import time

def getRandomPulse():
    pulse = math.ceil(random.gauss(70,5))
    return pulse

def sendQuery():
    # Setting all db variables
    host = 'localhost'
    port = 8086
    user = 'jean'
    password = 'students'
    dbname = 'IoT_lab'

    #Creating queries
    device1 = "heartSwatch,device=device_1 pulse="+str(getRandomPulse())
    device2 = "heartSwatch,device=device_2 pulse="+str(getRandomPulse())
    #print(device1)
    #print(device2)

    client = InfluxDBClient(host, port, user, password, dbname)

    client.write([device1],{'db':dbname}, protocol='line')
    client.write([device2],{'db':dbname}, protocol='line')

    client = None

if __name__ == "__main__":
    while (True):
        sendQuery()
        time.sleep(60)
