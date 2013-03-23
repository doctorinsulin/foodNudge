#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import with_statement
from flask import Flask, render_template, jsonify, g
from forms import FoodSelectForm
import os
import sqlite3
from contextlib import closing

# configuration
DATABASE = 'nudgeDB.db'
DEBUG = True
SECRET_KEY = '1111'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template('base.html', body='hello, world!')


@app.route('/foods')
def available_foods():
    """
    Return a JSON list of all the foods which we have calorie counts
    available for.

    TODO: get_db function
    TODO: make sure this works!
    """
    db = get_db()
    cur = db.execute('SELECT x FROM Foods')
    food_entries = cur.fetchall()
    foods = [row[0] for row in food_entries]
    return jsonify(foods)


@app.route('/<food>/kcal')
def calories_for_food(food):
    """
    URL endpoint to query the number of kcal in a single food item.
    """
    # query the DB
    cursor = g.db.execute('SELECT calories FROM Foods WHERE name=?', food)
    calories = cursor.fetchone()[0]

    # return the number
    return jsonify(calories)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    g.db.close()


@app.route('/entries')
def show_entries():
    cur = g.db.execute('select title, calories from food_items')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('base.html', body=entries)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    init_db()
    # app.run(host='0.0.0.0', port=port)
    app.run(debug=True)
