from Neuron_Essentials import Neuron, SignalType, NeuronType
import pandas as pd
import numpy as np


def run_sim(runTime):

    nrn1 = [-39.95669640552794, -39.78765004501495, -39.13022405432472, -37.02429684470145, -31.496478551237022, -19.702852360771175, 0.4667385288586595, 27.388903360285745, 53.73581678628326, 68.90548171240849, 65.68683830675556, 45.66808613785454, 18.00216664473536, -7.1982992627124265, -24.505573698685073, -33.88661661273688, -37.98527972223925, -39.445406371434, -39.872484790870494, -39.97551071573893, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0]
    nrn2 = [-40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -39.95669640552794, -39.78765004501495, -39.13022405432472, -37.02429684470145, -31.496478551237022, -19.702852360771175, 0.4667385288586595, 27.388903360285745, 53.73581678628326, 68.90548171240849, 65.68683830675556, 45.66808613785454, 18.00216664473536, -7.1982992627124265, -24.505573698685073, -33.88661661273688, -37.98527972223925, -39.445406371434, -39.872484790870494, -39.97551071573893]

    return nrn1, nrn2
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

   









