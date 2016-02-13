"""
Author: Brent Magnusson
Date Created: 1/31/2016

Purpose: Generate plots of energy consumption using the Smart Grid, Smart City
    dataset.

Notes:
    -Tested on Python 3.4.3.
    -Developed using iPython notebook. Converted to .py at the end.
"""
import numpy as np
import pandas as pd
from bokeh.charts import Bar, output_file, save
from datetime import datetime
import json

import urllib.request


def convert_to_datetime(t):
    return datetime.strptime(t, "%Y-%m-%d %H:%M:%S")


def get_hour_from_timeseries(ts):
    return ts.hour


def get_and_save_han(customer_id):
    limit = 32000
    # TODO figure out how to speed up query so we can get all data
    limit = 5000
    han_url = "http://data.gov.au/api/action/datastore_search?resource_id" \
              "=63d2b1cd-f453-4440-8bb7-ed083326f5ae&q=%s&limit=%s" % (
                  customer_id, limit)
    # Get data from sgsc website, then convert to dataframe
    han_json = urllib.request.urlopen(han_url).read().decode("utf-8")
    han_dict = json.loads(han_json)
    han = pd.DataFrame.from_dict(han_dict['result']['records'])
    # Get a datetime column and then a separate hour column
    han['READING_DATETIME'] = pd.to_datetime(han.READING_TIME)
    han["HOUR"] = han.READING_DATETIME.apply(get_hour_from_timeseries)
    han['READING_DELTA'] = np.zeros(len(han.index))
    # Sort by date so that we can iterate as a timeseries
    han = han.sort('READING_DATETIME')
    han = han.reset_index()
    # TODO figure out better way to deal with data. MongoDB perhaps?
    han.to_pickle('data/han')
    plug_list = han.PLUG_NAME.unique().tolist()
    return plug_list


def prepare_han2(plug):
    han = pd.read_pickle('data/han')
    han2 = han[han.PLUG_NAME == plug]
    # The readings are an aggregate value, so we need to calculate the increase
    # in the kWh from the previous reading.
    y = han2.READING_VALUE.as_matrix()
    y_delta = np.zeros(len(y))
    y_delta[0] = y[0]
    for i in range(1, len(y)):
        delta = float(y[i]) - float(y[i - 1])
        if delta >= 0:
            y_delta[i] = delta
        else:
            # Some of the meters were reset to zero during the trial period
            y_delta[i] = y[i]
    y_delta[0] = 0.0
    han2["READING_DELTA"] = y_delta
    return han2


def static_bar_plot(plug):
    han2 = prepare_han2(plug)
    start_time = han2.head(1).READING_TIME.as_matrix()[0][:-9]
    end_time = han2.tail(1).READING_TIME.as_matrix()[0][:-9]
    customer = han2.CUSTOMER_ID.unique()[0]
    plug = han2.PLUG_NAME.unique()[0]
    output_file("templates/plot.html")
    p = Bar(han2, 'HOUR', values='READING_DELTA',
            title="Total Energy Used from %s to %s" % (start_time, end_time),
            ylabel="kWh, %s at site %s" % (plug, customer))
    save(p)
