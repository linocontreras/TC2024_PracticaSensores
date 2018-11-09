#!/usr/bin/python

import sys
import Adafruit_DHT
from flask import Flask
from flask import jsonify
def data():
    file = open("/sys/bus/w1/devices/28-0417a2e7e0ff/w1_slave", "r")
    temp = float(file.read()[-6:])/1000
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 24)
    file.close()
    return temp, temperature, humidity

app = Flask(__name__)
@app.route('/temp')
def temp():
    t1, t2, h = data()
    return jsonify( temp = t1 )

@app.route('/hum')
def hum():
    t1, t2, h = data()
    return jsonify( hum = h )

@app.route('/all')
def all():
    t1, t2, h = data()
    return jsonify( temp1 = t1, temp2 = t2, hum = h )
