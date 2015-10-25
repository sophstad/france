from flask import render_template
from app import app
from analysis import *

@app.route('/')
def home():
    yes_working, not_working = working()
    working_chart = [['Yes', yes_working], ['No', not_working]]
    metro_average = metro()
    temperature_average = temperature()
    sunny_days = weather()
    activity_dict = activities()
    music_dict = {'Alvvays': 38, 'Todd Terje': 19, 'Real Estate': 21, 'Kelela': 18, 'The War on Drugs': 12, 'Rae Sremmurd': 16, "D'Angelo": 12, 'Vince Staples': 25, 'Mac DeMarco': 14, 'Majical Cloudz': 18, 'Kanye West': 12, 'Shabazz Palaces': 36, 'Tame Impala': 51, 'Nosaj Thing': 15, 'Django Django': 15, 'Super Social Jeez': 12, 'Sufjan Stevens': 43, 'Unknown Mortal Orchestra': 12, 'A$AP Rocky': 37, 'Young Fathers': 10, 'Drake': 61, 'Father': 64}
    return render_template('index.html',
        working_chart=working_chart,
        metro_average=metro_average,
        temperature_average=temperature_average,
        sunny_days=sunny_days,
        activity_dict=activity_dict,
        music_dict=music_dict)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")