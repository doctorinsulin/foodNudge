#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wtforms import Form, SelectField


class FoodSelectForm(Form):
    """
    WTForms class, allowing the selection of up to 3 foods.
    The foods available must be defined in the handler, as in
    <http://wtforms.simplecodes.com/docs/1.0.3/fields.html#wtforms.fields.SelectField>
    """
    food1 = SelectField(u'food1')
    food2 = SelectField(u'food2')
    food3 = SelectField(u'food3')
