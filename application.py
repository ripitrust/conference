from flask import Flask , render_template

application = Flask(__name__)


@application.route('/index')
def index_page():
    return render_template('index.html')


@application.route('/home')
def home_page():
    return render_template('home.html')

@application.route('/mbs')
def mbs_page():
    return render_template('mbs.html')

@application.route('/deluxe')
def deluxe_page():
    return render_template('deluxe.html')

@application.route('/premium')
def premium_page():
    return render_template('premium.html')

@application.route('/suite')
def suite_page():
    return render_template('suite.html')

@application.route('/stay')
def stay_page():
    return render_template('stay.html')


@application.route('/events')
def event_page():
    return render_template('events.html')



@application.route('/foods')
def food_page():
    return render_template('foods.html')


@application.route('/places')
def place_page():
    return render_template('places.html')


@application.route('/test')
def experiment_page():

    return render_template('experiment.html')



if __name__ == '__main__':

    application.run(host="0.0.0.0", port=20000, debug=True)
