import pandas as pd
import numpy as np
from Network import *
import streamlit
from pyvis import network as net
from stvis import pv_static

if __name__ == "__main__":

    streamlit.title("Neural Oscillator Circuit Simulation", anchor=None)

    displayText1 = "This is a simple simulation of an oscillating circuit in the brain. The circuit\nconsists of eight neurons: two inputs, and two outputs, and four oscillators.\nA graph representation of this circuit is shown below."

    streamlit.text(displayText1)


    graph = net.Network(height='350px', width='700px', bgcolor='#222222', font_color='white')
    graph.add_node("Input 1", label="Input 1", color='#698B22') 
    graph.add_node("Excitatory 1", label="Excitatory 1", color='#93CAED')
    graph.add_node("Output 1", label="Output 1", color='#698B22')
    graph.add_node("Inhibitory 1", label="Inhibitory 1", color='#FFA500')
    graph.add_node("Excitatory 2", label="Excitatory 2", color='#93CAED')
    graph.add_node("Output 2", label="Output 2", color='#698B22')
    graph.add_node("Inhibitory 2", label="Inhibitory 2", color='#FFA500')
    graph.add_node("Input 2", label="Input 2", color='#698B22')
   
    graph.add_edge("Input 1", "Excitatory 1", color='#FFFFFF')
    graph.add_edge("Excitatory 1", "Output 1", color='#FFFFFF')
    graph.add_edge("Excitatory 1", "Inhibitory 1", color='#FFFFFF')
    graph.add_edge("Inhibitory 2", "Inhibitory 2", color='#FFFFFF')
    graph.add_edge("Inhibitory 2", "Excitatory 1", color='#FFFFFF')
    graph.add_edge("Inhibitory 1", "Excitatory 2", color='#FFFFFF')
    graph.add_edge("Inhibitory 1", "Inhibitory 1", color='#FFFFFF')
    graph.add_edge("Input 2", "Excitatory 2", color='#FFFFFF')
    graph.add_edge("Excitatory 2", "Output 2", color='#FFFFFF')
    graph.add_edge("Excitatory 2", "Inhibitory 2", color='#FFFFFF')


    pv_static(graph)    
  

    displayText2 = "Add the number of milliseconds to run the simulator. When the simulation is complete,\nthe voltage spike trains of each output neuron will be shown below."
    streamlit.text(displayText2)

    user_input = streamlit.number_input("", min_value=4, max_value=100, value=4)
    first, second = run_sim(user_input)

    first_np = np.array(first)
    second_np = np.array(second)
    
    chart_data = pd.DataFrame(np.column_stack((first_np, second_np)), columns=['Output Neuron One', 'Output Neuron Two'])

    streamlit.line_chart(chart_data, width=700, height=450)

