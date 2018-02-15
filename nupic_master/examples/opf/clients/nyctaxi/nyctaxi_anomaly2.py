# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2016, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

"""
A simple client to create a HTM anomaly detection model for nyctaxi dataset.
The script prints out all records that have an abnormally high anomaly
score.
"""

import csv
import datetime
import logging
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as FA
import time 

taxi_list = []
err_list = []
err_index = []
index_list = []
start_index = 0
fig = plt.figure()
from pkg_resources import resource_filename

from nupic.frameworks.opf.model_factory import ModelFactory

import model_params

_LOGGER = logging.getLogger(__name__)

_INPUT_DATA_FILE = resource_filename(
  "nupic.datafiles", "extra/nyctaxi/nycTaxi.csv"
)
_OUTPUT_PATH = "anomaly_scores_with_increment.csv"

_ANOMALY_THRESHOLD = 0.9

# minimum metric value of nycTaxi.csv
_INPUT_MIN = 8

# maximum metric value of nycTaxi.csv
_INPUT_MAX = 39197


def _setRandomEncoderResolution(minResolution=0.001):
  """
  Given model params, figure out the correct resolution for the
  RandomDistributed encoder. Modifies params in place.
  """
  encoder = (
    model_params.MODEL_PARAMS["modelParams"]["sensorParams"]["encoders"]["value"]
  )

  if encoder["type"] == "RandomDistributedScalarEncoder":
    rangePadding = abs(_INPUT_MAX - _INPUT_MIN) * 0.2
    minValue = _INPUT_MIN - rangePadding
    maxValue = _INPUT_MAX + rangePadding
    resolution = max(minResolution,
                     (maxValue - minValue) / encoder.pop("numBuckets")
                    )
    encoder["resolution"] = resolution


def createModel():
  _setRandomEncoderResolution()
  return ModelFactory.create(model_params.MODEL_PARAMS)

def animate(i):
  plt.plot(index_list, taxi_list,'k', err_index, err_list, 'bo')

fin = open ('nycTaxi.csv') 
reader = csv.reader(fin)
headers = reader.next()
model = createModel()
model.enableInference({'predictedField': 'value'})

def runNYCTaxiAnomaly(i):
  global start_index
  fig.clf()
  record = reader.next()
  modelInput = dict(zip(headers, record))
  modelInput["value"] = float(modelInput["value"])
      
  modelInput["timestamp"] = datetime.datetime.strptime(
  modelInput["timestamp"], "%Y-%m-%d %H:%M:%S")
  result = model.run(modelInput)
  anomalyScore = result.inferences['anomalyScore']
  taxi_list.append(modelInput["value"])
  index_list.append(start_index)


  if anomalyScore > _ANOMALY_THRESHOLD:
    err_list.append(modelInput['value'])
    err_index.append(start_index)
  start_index += 1
  plt.plot(index_list, taxi_list,'k', err_index, err_list, 'bo')
      

  print "Anomaly scores have been written to",_OUTPUT_PATH

if __name__ == "__main__":
  ani = FA(fig, runNYCTaxiAnomaly, interval = 500)
  plt.show()
