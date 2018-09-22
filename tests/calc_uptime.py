import re
from availability import Availability
import json

# used to match time format like XdYhZm
down_reg = re.compile(r'^(\d+)d(\d+)h(\d+)m$')
format_match = False

print('Enter downtime')
print('Use format XdYhZm')
print('\tWhere X is number of day, Y number of Hours and Z number of minutes')
print('\tWith X,Y,Z are integer and 0 as minimum or none value')
while not format_match:
    downtime = str(input('>'))
    if down_reg.match(downtime):
        format_match = True
    else:
        print('Format entered not compatible !')

downtime_match = down_reg.search(downtime)
#print(type(downtime_match.group(1)))
down = Availability(int(downtime_match.group(1)),
                    int(downtime_match.group(2)),
                    int(downtime_match.group(3)))

daily = down.service(period='daily')
print(daily)
weekly = down.service(period='weekly')
print(weekly)
monthly = down.service(period='monthly', out_dict=True)
print(monthly)
fullsla = down.service(out_dict=True)
print(json.dumps(fullsla))
#err_test = down.period_uptime(-32)
#err_test = down.period_uptime('fail')
#err_test = down.period_uptime(5.43)
