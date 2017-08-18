#!/usr/bin/env python

from datetime import datetime, timedelta
from dateutil.parser import parse as parse_date


def get_daily_cost(monthly_cost):
    return monthly_cost / 30
    
    
def get_current_cost(daily_cost, rental_date):
    if not isinstance(rental_date, date):
        rental_date = parse_date(rental_date)
    total_days = (datetime.today() - rental_date).days
    return daily_cost * total_days
    
   
def get_max_rental_time(daily_cost, total_cost):
    return total_cost // daily_cost
    
    
def get_max_rental_date(max_time, rental_date=None):
    rental_date = rental_date or datetime.today()
    if not isinstance(rental_date, date):
        rental_date = parse_date(rental_date)
    return rental_date + timedelta(max_time)
    
    
def get_remaining_days(max_rental_date):
    if not isinstance(max_rental_date, date):
        rental_date = parse_date(max_rental_date)
    return (max_rental_date - datetime.today()).days