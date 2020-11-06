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

#dictionary for covid information
COVID19_PARAMS = {
    "r0" : 2.28,
    "incubation": 5,
    "percent_mild": 0.8,
    "mild_recovery": (7, 14),
    "percent_severe": 0.2,
    "severe_recovery": (21, 42),
    "severe_death": (14, 56),
    "fatality_rate": 0.034,
    "serial_interval": 7
}

class Virus():
    def __init__(self, params):

        #circular plot showing the virus spreading 
        #from the center outwards
        #theta and r to specify points within a circle


        self.fig = plt.figure()
        self.axes = self.fig.add_subplot(111, projection="polar")

        self.axes.grid(False)
        self.axes.set_xticklabels([])
        self.axes.set_yticklabels([])
        self.axes.set_ylim(0, 1)

        #annotations 
        self.day_text = self.axes.annotate("Day 0", xy=[np.pi / 2, 1], ha="center", va="bottom")

        self.infected_text = self.axes.annotate("Infected: 0", xy=[3 * np.pi / 2, 1], ha="center", va="bottom", color=RED)

        self.deaths_text = self.axes.annotate("\nDeaths: 0", xy=[3 * np.pi / 2, 1], ha="center", va="bottom", color=BLACK)
    
        self.recovered_text = self.axes.annotate("\nRecovered: 0", xy=[3 * np.pi / 2, 1], ha="center", va="bottom", color=GREEN)

        #member vars
        self.day = 0
        self.total_num_infected = 0
        self.num_currently_infected = 0
        self.num_recovered = 0
        self.num_deaths = 0

        #measure of contagiousness
        self.r0 = params["r0"] 

        #rates 
        self.percent_mild = params["percent_mild"]
        self.percent_severe = params["percent_severe"]
        self.fatality_rate = params["fatality_rate"]
        self.serial_interval = params["serial_interval"]

        #intervals
        self.mild_fast = params["incubation"] + params["mild_recovery"][0]

        self.mild_slow = params["incubation"] + params["mild_recovery"][1]

        self.severe_fast = params["incubation"] + params["severe_recovery"][0]

        self.severe_slow = params["incubation"] + params["severe_recovery"][1]

        self.death_fast = params["incubation"] + params["severe_death"][0]

        self.death_slow = params["incubation"] + params["severe_death"][1]
        
        #track all cases for a year
        #populate lists theta and r values
        #with symptomps throughout the year
        self.mild = {i: {"thetas": [], "rs": []} for i in range(self.mild_fast, 365)}

        self.severe = {"recovery": {i: {"thetas": [], "rs": []} for i in range(self.severe_fast, 365)},
        "death": {i: {"thetas": [], "rs": []} for i in range(self.death_fast, 365)}}

        self.exposed_before = 0
        self.exposed_after = 1


        self.initial_population()


    #create initial population for the plot
    def initial_population(self):

        population = 4500
        self.num_currently_infected = 1
        self.total_num_infected = 1

        indices = np.arange(0, population) + 0.5

        #keep track of people in the population
        self.thetas = np.pi * (1 + 5**0.5) * indices
        self.rs = np.sqrt(indices / population)

        self.plot = self.axes.scatter(self.thetas, self.rs, s=5, color=GREY)

        #create PATIENT 0
        self.axes.scatter(self.thetas[0], self.rs[0], s=5, color=RED)
        self.mild[self.mild_fast]["thetas"].append(self.thetas[0])
        self.mild[self.mild_fast]["rs"].append(self.rs[0])


Virus(COVID19_PARAMS)
plt.show()