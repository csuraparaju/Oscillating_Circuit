from Neuron_Essentials import Neuron, SignalType, NeuronType
from PIL import Image
import numpy as np
import pandas as pd
import math



def run_sim(image):
    img = image
    colors = img.getcolors(256)
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        
        return most_present
    except TypeError:
        raise Exception("Too many colors in the image")

#For future references, this data was generated using 1.5^(-x), but some of the values are changed with random noise. 
def get_graph_data():
    data = [1.0, 0.6666666666666666, 0.621, 0.2962962962962963, 0.2353086419753085, 0.13168724279835392, 0.0877914951989026, 0.09852766346593507, 0.03901844231062338, 0.03601229487374892]
    return data


    






    
