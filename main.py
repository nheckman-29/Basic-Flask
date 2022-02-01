import flask

#Single web app object. Stores metadata, cookies, name
app = flask.Flask(__name__)

shows = ['The Office', 'The Flash', 'Royal Pains', 'Black Mirror', 'Twin Peaks']
pictures = ['prison-mike.jpg', 'barry-allen.jpeg', 'royal-pains.jpg', 'black-mirror.png','twin-peaks.jpg']

#Decorator to specify where app is routed to
@app.route("/")
#Send down index.html from templates folder. Must be templates folder
def index():
    return flask.render_template(
        'index.html',
        name = "Nathan",
        shows = shows,
        len = len(shows),
        pictures = pictures
    )

app.run(debug=True)