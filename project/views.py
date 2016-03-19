from flask import render_template
from app import app
from analysis import *

@app.route('/')
def home():
    yes_working, not_working = working()
    working_chart = [['Yes', yes_working], ['No', not_working]]
    metro_average = metro()
    temperatureF_average = temperatureF()
    temperatureC_average = temperatureC()
    sunny_days = weather()
    coffees = coffee()
    report = reports()
    activity_dict = activities()
    list_of_ten = music()
    honorable_mentions = {'Bubble T. Paris': 'http://www.bubbletparis.com', 'Coutume Instituutti': 'https://www.facebook.com/coutumeinstituutti', 'Fondation Louis Vuitton': 'http://www.fondationlouisvuitton.fr/content/flvinternet/en.html'}
    return render_template('index.html',
        working_chart=working_chart,
        metro_average=metro_average,
        temperatureF_average=temperatureF_average,
        temperatureC_average=temperatureC_average,
        sunny_days=sunny_days,
        coffees=coffees,
        report=report,
        activity_dict=activity_dict,
        list_of_ten=list_of_ten,
        honorable_mentions=honorable_mentions,)

@app.route('/about/index.html')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")