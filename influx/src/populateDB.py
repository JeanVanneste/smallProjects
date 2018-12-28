# -*- coding: utf-8 -*-

from influxdb import InfluxDBClient
import random
import math

def getRandomPulse():
    pulse = math.ceil(random.gauss(70,5))
    return pulse

def sendQuery():
    

if __name__ == "__main__":
    for i in range(0,10):
        print(getRandomPulse())
