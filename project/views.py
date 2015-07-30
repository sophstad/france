from flask import render_template
from app import app
from analysis import *

@app.route('/')
def home():
    yesWorking, notWorking = working()
    workingChart = [['Yes', yesWorking], ['No', notWorking]]
    metroAverage = metro()
    temperatureAverage = temperature()
    return render_template('index.html',
        workingChart=workingChart,
        metroAverage=metroAverage,
        temperatureAverage=temperatureAverage)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")