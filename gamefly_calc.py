#!/usr/bin/env python

from datetime import datetime, timedelta
from dateutil.parser import parse as parse_date


class GameRental(object):

def __init__(self, rental_date, total_cost, monthly_fee=7):
    if not isinstance(rental_date, date):
        rental_date = parse_date(rental_date)
    self.rental_date = rental_date
    self.total_cost = total_cost
    self.daily_cost = _get_daily_cost(monthly_fee)
    
@property
def current_cost(self):
    return _get_current_cost()

def _get_daily_cost(self, monthly_cost):
    return monthly_cost / 30
        
def _get_current_cost(self):
    total_days = (datetime.today() - self.rental_date).days
    return self.daily_cost * total_days
    
def _get_max_rental_time(self, daily_cost, total_cost):
    return total_cost // daily_cost
    
def _get_max_rental_date(self, max_time, rental_date=None):
    rental_date = rental_date or datetime.today()
    if not isinstance(rental_date, date):
        rental_date = parse_date(rental_date)
    return rental_date + timedelta(max_time)
    
def _get_remaining_days(self, max_rental_date):
    if not isinstance(max_rental_date, date):
        rental_date = parse_date(max_rental_date)
    return (max_rental_date - datetime.today()).days
