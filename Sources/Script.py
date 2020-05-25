""" Following import are libs needed to use the hardware
import time
import busio
import adafruit_ccs811
from board import *
"""

#We will use flask as server
from flask import Flask, url_for, render_template
import random

app = Flask(__name__)
""" This Part of the code is the code to be run with the hardware
i2c_bus = busio.I2C(SCL, SDA)
ccs = adafruit_ccs811.CCS811(i2c_bus)
@app.route('/sensor')
def get_airqual():
    return (ccs811.eco2, ccs811.tvoc, ccs811.temperature)
"""
#this code is used for the demonstration using fake datas
#This will call the following function when the front url is calling on "/home"
@app.route('/home')
def mainPage():
    return render_template('MainPage.html')

@app.route('/sensor')
def get_sensor_value():
    co2 = random.randint(0,800)
    tvoc = random.randint(1,500)
    temp = random.randint(-20,40)
    return str('{"co2": "' + str(co2) + '", "tvoc": ' + str(tvoc) + ', "temp": ' + str(temp) + '}')