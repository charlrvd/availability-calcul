from availability import Availability
import main
import unittest

## test class
class TestAvailabilityClass(unittest.TestCase):
    def setUp(self):
        self.avail = Availability(0,0,0)
        self.avail_x = Availability(0,5,15)

    def test_100(self):
        avail_dict_100_res = {"monthly": 100.0, "yearly": 100.0, "daily": 100.0, "weekly": 100.0}
        avail_100_res = (100.0, 100.0, 100.0, 100.0)
        self.assertEqual(self.avail.service(out_dict=True), avail_dict_100_res)
        self.assertEqual(self.avail.service(), avail_100_res)

    def test_daily_100(self):
        avail_daily = {"daily": 100.0}
        avail_daily_t = (100.0)
        self.assertEqual(self.avail.service(period='daily', out_dict=True), avail_daily)
        self.assertEqual(self.avail.service(period='daily'), avail_daily_t)

    def test_weekly_100(self):
        avail_weekly = {"weekly": 100.0}
        avail_weekly_t = (100.0)
        self.assertEqual(self.avail.service(period='weekly', out_dict=True), avail_weekly)
        self.assertEqual(self.avail.service(period='weekly'), avail_weekly_t)

    def test_monthly_100(self):
        avail_monthly = {"monthly": 100.0}
        avail_monthly_t = (100.0)
        self.assertEqual(self.avail.service(period='monthly', out_dict=True), avail_monthly)
        self.assertEqual(self.avail.service(period='monthly'), avail_monthly_t)

    def test_yearly_100(self):
        avail_yearly = {"yearly": 100.0}
        avail_yearly_t = (100.0)
        self.assertEqual(self.avail.service(period='yearly', out_dict=True), avail_yearly)
        self.assertEqual(self.avail.service(period='yearly'), avail_yearly_t)

## test flask app


if __name__ == '__main__':
    unittest.main()
