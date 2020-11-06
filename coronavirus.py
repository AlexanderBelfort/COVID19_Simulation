#data visualisation
import matplotlib.pyplot as plt
import matplotlib.animation as ani

#math function on arrays
import numpy as np

#RGB tuples to represent infecton status

GREY = (0.77, 0.77, 0.77)
RED = (0.96, 0.15, 0.15)
GREEN = (0, 0.85, 0.03)
BLACK = (0, 0, 0)

COVID19_PARAMS = {
    "r0" : 2.28,
    "incubation": 5,
    "percent_mild": 0.8,
    "mild_recovery": (7, 14),
    "percent_severe": 0.2,
    "severe_recovery": (21, 42),
    "sever_death": (14, 56),
    "fatality_rate": 0.034,
    "serial_interval": 7
}