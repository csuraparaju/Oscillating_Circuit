from Neuron import *
from SignalType import *
from NeuronType import *
import pandas as pd
import streamlit
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

    
    
    # time = [i for i in range(0,len(outBot.voltagePotentialHistory))]
    # time = [i/1000 for i in time]

    topNrn = outTop.voltagePotentialHistory[:len(outBot.voltagePotentialHistory)]  # y axis
    bottomNrn = outBot.voltagePotentialHistory  # z axis

    return topNrn, bottomNrn

    # #Plot the results
    # time = [i for i in range(0, len(outBot.voltagePotentialHistory))]  # x axis
    # time = [i/1000 for i in time]  # x axis in milliseconds
    # topNrn = outTop.voltagePotentialHistory[:len(outBot.voltagePotentialHistory)]  # y axis
    # bottomNrn = outBot.voltagePotentialHistory  # z axis

    # ax = plt.gca()
    # ax.set_ylim([-0.045, 0.08])
    
    # plt.title("Membrane Potentials of Output Neurons in an Oscillating Circuit")
    # plt.xlabel(xlabel="Time (ms)")
    # plt.ylabel(ylabel="Membrane Potential (mV)")
    # plt.plot(time, topNrn, color="red", label="Top Output Neuron")
    # plt.plot(time, bottomNrn, color="blue", label="Bottom Output Neuron")
    
    
    # plt.show()



if __name__ == "__main__":

    streamlit.title("Oscillating Circuit Simulation.", anchor=None)
    streamlit.text("The circuit is modeled using a graph. Each node in the graph represents a neuron.\nVisualization of the graph is shown below. The plot is the voltage potential of the\noutput neurons.")
    streamlit.text("Enter the number of milliseconds to run the simulation for (Ex. 4): ")

    user_input = streamlit.text_input("", 0)
    first, second = run_sim(int(user_input))

    first_np = np.array(first)
    second_np = np.array(second)
    
    
    chart_data = pd.DataFrame(np.column_stack((first_np, second_np)), columns=['Output Neuron One', 'Output Neuron Two'])



    streamlit.line_chart(chart_data)





