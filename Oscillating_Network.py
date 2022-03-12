from Neuron import *
from SignalType import *
from NeuronType import *
import pandas as pd
import numpy as np


def run_sim(runTime):
    # First row in graph
    inpTop = Neuron(NeuronType.INPUT, runTime)
    excTop = Neuron(NeuronType.EXCITATORY, runTime)
    outTop = Neuron(NeuronType.OUTPUT, runTime)
    
    # Second row in graph
    leftInh = Neuron(NeuronType.INHIBITORY, runTime)
    rightInh = Neuron(NeuronType.INHIBITORY, runTime)

    # Third row in graph
    inpBot = Neuron(NeuronType.INPUT, runTime)
    excBot = Neuron(NeuronType.EXCITATORY, runTime)
    outBot = Neuron(NeuronType.OUTPUT, runTime)

    # Connect the neurons

    # First row
    inpTop.addSynapse(excTop)
    excTop.addSynapse(outTop)
    excTop.addSynapse(rightInh)

    # Second row
    leftInh.addSynapse(excTop)
    rightInh.addSynapse(excBot)

    # Third row
    inpBot.addSynapse(excBot)
    excBot.addSynapse(outBot)
    excBot.addSynapse(leftInh)

    # Send signals

    for i in range(0,3):
        inpTop.sendSynapseSignal(SignalType.POSITIVE)
        excTop.sendSynapseSignal(SignalType.POSITIVE)

    
    time = [i/1000 for i in range(0,len(outBot.voltagePotentialHistory))]
    topNrn = [i*1000 for i in outTop.voltagePotentialHistory[:len(outBot.voltagePotentialHistory)]]
    bottomNrn = [i*1000 for i in outBot.voltagePotentialHistory]

    return time, topNrn, bottomNrn









