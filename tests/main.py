from flask import Flask, render_template
from availability import Availability
import json

app = Flask(__name__)
#app = Flask(__name__, template_folder='tpl')
#app.register_error_handler(404, not_found)

@app.errorhandler(404)
def no_found(e):
    return render_template('404.html'), 404

@app.route("/<int:days>/<int:hours>/<int:minutes>")
def avail(days, hours, minutes):
    av = Availability(days, hours, minutes)
    return json.dumps(av.service(out_dict=True))

@app.route("/period/<string:period>/<int:days>/<int:hours>/<int:minutes>")
def period_avail(period, days, hours, minutes):
    plist = ('daily', 'weekly', 'monthly', 'yearly')
    av = Availability(days, hours, minutes)
    if period in plist and isinstance(period, str):
        return json.dumps(av.service(period=period, out_dict=True))
    else:
        return json.dumps({"error":"period not properly set, must be of : "
                            + str(plist)})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
