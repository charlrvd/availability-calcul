from calendar import monthrange
from datetime import date

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
        self.periods = {"daily": self.day,
                        "weekly": self.week,
                        "monthly": self.month,
                        "yearly": self.year}

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
        - optionnal argument {period}
        can take 4 different possibility:
        daily / weekly / monthly / yearly
        if none,
        return a tuple of all the sla
        order is: (daily, weekly, monthly, yearly)

        - optionnal argument {out_dict}
        if set to True, will return value in a dict
        """
        if period in self.periods:
            if out_dict:
                return {period: self.period_uptime(self.periods[period])}
            return self.period_uptime(self.periods[period])
        #elif period == 'weekly':
        #    if out_dict:
        #        return {'weekly': self.period_uptime(self.week)}
        #    return self.period_uptime(self.week)
        #elif period == 'monthly':
        #    if out_dict:
        #        return {'monthly': self.period_uptime(self.month)}
        #    return self.period_uptime(self.month)
        #elif period == 'yearly':
        #    if out_dict:
        #        return {'yearly': self.period_uptime(self.year)}
        #    return self.period_uptime(self.year)
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

    def service_slide(self, period='none', out_dict=False):
        pass
