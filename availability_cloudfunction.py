from calendar import monthrange
from datetime import date
import json
import re

class Availability:
    def __init__(self,d,h,m):
        self.days = d
        self.hours = h
        self.minutes = m
        self.day = 60*60*24
        self.week = self.day*7
        self.current_date = date.today()
        # tuple, (weekday of first day of the month, number of days)
        self.current_month = monthrange(self.current_date.year,
                                        self.current_date.month)
        self.month = self.current_month[1]*self.day
        self.yeardays = date(self.current_date.year + 1, 
                             1, 1) - date(self.current_date.year, 
                             1, 1)
        self.year = self.yeardays.days*self.day

    def seconds_downtime(self):
        """return the downtime in seconds"""
        down_minutes = self.minutes*60
        down_hours = self.hours*60*60
        down_days = self.days*24*60*60
        return down_minutes + down_hours + down_days

    def period_uptime(self, period):
        """return specified period uptime in percent"""
        if not isinstance(period, int):
            raise TypeError("period should be an integer")
        if period <= 0:
            raise ValueError("period cannot be 0 or negative value")
        res_percent = 100 - (100 * self.seconds_downtime())/period
        if res_percent < 0:
            return 0
        return float("{0:.3f}".format(res_percent))

    def service(self, period='none', out_dict=False):
        """
        optionnal argument {period}
        can take 4 different possibility:
        daily / weekly / monthly / yearly
        if none,
        return a tuple of all the sla
        order is: (daily, weekly, monthly, yearly)
        optionnal argument {out_dict}
        if set to True, will return value in a dict
        """
        if period == 'daily':
            if out_dict:
                return {'daily': self.period_uptime(self.day)}
            return self.period_uptime(self.day)
        elif period == 'weekly':
            if out_dict:
                return {'weekly': self.period_uptime(self.week)}
            return self.period_uptime(self.week)
        elif period == 'monthly':
            if out_dict:
                return {'monthly': self.period_uptime(self.month)}
            return self.period_uptime(self.month)
        elif period == 'yearly':
            if out_dict:
                return {'yearly': self.period_uptime(self.year)}
            return self.period_uptime(self.year)
        else:
            if out_dict:
                return {'daily': self.period_uptime(self.day),
                        'weekly': self.period_uptime(self.week),
                        'monthly': self.period_uptime(self.month),
                        'yearly': self.period_uptime(self.year)}
            return (self.period_uptime(self.day),
                    self.period_uptime(self.week),
                    self.period_uptime(self.month),
                    self.period_uptime(self.year))

def calc_avail(message, period='none'):
    down_regex = re.compile(r'^(\d+)d(\d+)h(\d+)m$')
    if not down_regex.match(message):
        return json.dumps({"error": "does not match format XdYhZm"})
    avail_match = down_regex.search(message)
    av = Availability(int(avail_match.group(1)),
                      int(avail_match.group(2)),
                      int(avail_match.group(3)))
    if period != 'none':
        return json.dumps(av.service(out_dict=True, period=period))
    return json.dumps(av.service(out_dict=True))

def avail(request):
    """Responds to any HTTP request.
    Args:
        downtime (format must be XdYhZm where
                                d is days
                                h is hours
                                m is minutes of downtime)
        Optionnal:
            period (can be 'daily', 'weekly', 'monthly', 'yearly')
    Returns:
        return a json of the service uptime in %
    """
    request_json = request.get_json()
    if request.args and 'downtime' in request.args:
        if 'period' in request.args:
            return calc_avail(request.args.get('downtime'), period=request.args.get('period'))
        return calc_avail(request.args.get('downtime'))
    elif request_json and 'downtime' in request_json:
        if 'period' in request_json:
            return calc_avail(request_json['downtime'], period=request_json['period'])
        return calc_avail(request_json['downtime'])
    else:
        return json.dumps({"error":help(avail)})

