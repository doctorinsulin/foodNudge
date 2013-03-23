#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html', body='hello, world!')
