#!/usr/bin/env python
# -*- coding: utf-8 -*-


def walking_distance_to_burn(kcal, bodyweight_kg):
    """
    Returns the approximate distance in km that you need to walk in order
    to burn the given number of kcal, based on your bodyweight.
    """

    miles = (float(kcal) / (1.18 * float(bodyweight_kg)))
    km = (1.6 * float(miles))
    return km


def walking(kcal, bodyweight_kg):
    """
    Returns the string:
    "it takes <km> kilometres to walk off <kcal> calories"
    """
    km = walking_distance_to_burn(kcal, bodyweight_kg)
    return ("it takes {: .2f}{} of {} to burn off {} calories".format(km,
            "km", "walking", kcal, bodyweight_kg))
