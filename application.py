from flask import Flask , render_template

app = Flask(__name__)


@app.route('/index')
def home_page():
    return render_template('index.html')


@app.route('/events')
def event_page():
    return render_template('events.html')



@app.route('/foods')
def food_page():
    return render_template('foods.html')


@app.route('/places')
def place_page():
    return render_template('places.html')


@app.route('/test')
def experiment_page():

    return render_template('experiment.html')



if __name__ == '__main__':

    app.run(host="0.0.0.0", port=20000, debug=True)
