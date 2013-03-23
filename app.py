#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request
from forms import FoodSelectForm
import os

app = Flask(__name__)


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
    db = get_db()
    calories = 0
    cursor = db.execute('SELECT calories FROM Foods WHERE name=?', food)
    calories = cursor.fetchone()[0]

    # return the number
    return jsonify(calories)



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
    app.run(debug=True)
