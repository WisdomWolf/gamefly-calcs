#!/usr/bin/env python

from datetime import datetime, date, timedelta
from datetime import time as datetime_time
from dateutil.parser import parse as parse_date
from repr_base import ReprBase

games_list = []


class GameRental(ReprBase):

    dollar_attrs = ['total_cost', 'daily_cost', 'current_cost']

    def __init__(self, name, rental_date, total_cost, monthly_fee=7):
        if not isinstance(rental_date, datetime) and not isinstance(rental_date, date):
            rental_date = parse_date(rental_date)
        elif not isinstance(rental_date, datetime):
            rental_date = datetime.combine(rental_date, datetime_time())
        self.name = name
        self.rental_date = rental_date
        self.total_cost = float(total_cost)
        self.daily_cost = _get_daily_cost(float(monthly_fee))
    
    def __str__(self):
        return f'{self.name:25.25} ${self.current_cost:>5}\t{self.remaining_days:2} days remaining.'
    
    @property
    def current_cost(self):
        return round(self._get_current_cost(), 2)
            
    def _get_current_cost(self):
        total_days = (datetime.today() - self.rental_date).days
        return self.daily_cost * total_days
        
    @property
    def max_rental_time(self):
        return self._get_max_rental_time()
        
    def _get_max_rental_time(self):
        return self.total_cost // self.daily_cost
        
    @property
    def max_rental_date(self):
        return self._get_max_rental_date()    
        
    def _get_max_rental_date(self):
        return self.rental_date + timedelta(self.max_rental_time)
        
    @property
    def remaining_days(self):
        return self._get_remaining_days()
        
    def _get_remaining_days(self):
        return (self.max_rental_date - datetime.today()).days


def _get_daily_cost(monthly_cost):
        daily_cost = monthly_cost / 30
        if 15 < monthly_cost < 22:
            return daily_cost / 1
        elif 22 < monthly_cost < 29:
            return daily_cost / 2
        elif 29 < daily_cost < 36:
            return daily_cost / 3
        elif 36 < daily_cost < 37:
            return daily_cost / 4
        else:
            raise ValueError('Invalid Monthly Cost')
        
        
def display_game_list(games):
    for game in games:
        print(game)


def add_game():
    import inspect
    init_params = inspect.getargspec(GameRental.__init__).args
    init_kwargs = {param: input(f'{param}: ') for param in init_params if param != 'self'}
    game = GameRental(**init_kwargs)
    games_list.append(game)
    print(f'added {game.name} to list successfully.')
 
