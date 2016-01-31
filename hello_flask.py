#! /usr/bin/env python

import flask


#Create the application
APP = flask.Flask(__name__)

@APP.route('/')
def index():
    """Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')

@APP.route('/hello/<name>/')
def hello(name):
    """Greet whoever comes to visit the page
    """
    return flask.render_template('hello.html', name=name)


if __name__ == '__main__':
    APP.debug = True
    APP.run()

