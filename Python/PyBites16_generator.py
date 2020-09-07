"""
Write a generator that returns special dates for PyBites:

Every year mark counting from PYBITES_BORN date (so 19th of Dec 2017, 19th of Dec 2018, etc)
Every 100 days mark counting from PYBITES_BORN (29th of March 2017, 7th of July 2017, etc)
See the tests for more details how your code will be tested: as this is a beginner's challenge 
we only calculate a few years ahead, leaving the next leap year (2020) out of this challenge.
"""
from datetime import date, timedelta

def special_pybites():
    year = timedelta(365)
    hundred = timedelta(100)
    bd_day = date(2017, 3, 29)
    special_date = date(2017, 3, 29)
    hundred_sd = special_date
    while True:
        yield special_date
        if hundred_sd + hundred > bd_day + year: #in case birthday happens before n*100 days
            bd_day += year
            special_date = bd_day 
        else: #birthday is after n*100 days
            hundred_sd += hundred
            special_date = hundred_sd