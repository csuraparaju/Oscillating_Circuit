import pandas as pd
import numpy as np
from Network import *
import streamlit 
from stvis import pv_static
from pyvis import network as net



if __name__ == "__main__":

    mainContainer = streamlit.container()

    with mainContainer: 

        streamlit.title("Neural Oscillator Circuit Simulation", anchor=None)

        IntroMsgOne = """This is a simple simulation of an oscillating circuit in the brain. Mostly prominant 
         in the neuromotor system, oscillating circuits help the body walk. For example, when the neurons 
         responsible for moving the right leg are turned on, neurons responsible for moving the left leg
         will turn off, and vice versa/  
        """

        IntroMsgTwo = """ 
        Essentially, the input neurons give a continuous activating signal to the two excitatory neurons, 
        which are types of neurons that feed forward the positive signal to others when they are told to turn on.
        The excitatory neurons are connected to their respective output neurons as well as two inhibitory neurons.
        Unlike excitatory neurons, inhibitory neurons feed forward a negative signal when they are told to turn on.
        In short, excitatory neurons turn on other neurons and inhibitory neurons turn off other neurons when activated.
        Due to this nature, the inhibitory neurons in the circuit act as clocks. When one of the excitatory neurons is
        activated, the other excitatory neuron is signaled to turn off. Explore the figure below to see how the connections
        of each neuron give rise to an oscillating nature. 
        
        """

        streamlit.write(IntroMsgOne)
        streamlit.write(IntroMsgTwo)

        graph = net.Network(height='500px', width='700px', bgcolor='#222222', font_color='white')
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

        huxleyMsg = r'''
        
        In this simulation, I decided to represent the firing of the neuron by plotting its voltage potential. 
        Voltage potential is the amount of electrical energy that a neuron is holding in its membrane at any given time. 
        When a neuron fires, its voltage potential increases until it reaches a threshold, at which point it decreases
        back to its resting potential. For this model, I decided to model the current flowing through the neuron as a 
        function of its potential, mainly using the Hodgkin-Huxley equations: 
        $I_m(t)=C_m\frac{dV_m}{dt}+\frac{V_m(t)}{R_m}$, where $C_m$ is the membrane capacitance of the neuron, $V_m$ is 
        the potential voltage across the membrane and
        $R_m$ is the resistance of the membrane.
        '''

        streamlit.write(huxleyMsg)

        integrateMsg = r'''

        In order to obtain voltage potential values, I needed to solve this differential equation.
        If we re-arrange the equation, we can see that: $\int{I_m(t)-\frac{V_m(t)}{R_m}}dt = V(t)$.
        Because this is a simulation, I decided to solve this integral by summing discrete 
        values of time. I arbitrarily chose a time step, $dt$, of 0.1 seconds. 
        So in order to obtain the voltage potential values, I summed the values of $I(t)$ for each time step:
        $V(t) = \sum{I(t)-\frac{V_m(t)}{R_m}}*dt$.

        
        '''

        streamlit.write(integrateMsg)

        # GraphComponent.drawGraph()
    
        simOptionMsg = r'''
        In order to view the results of this simulation, eneter the number of iterations you want the 
        neurons to fire for and hit enter. The data will be graphed on the plot below, with the y-axis 
        representing the voltage potential of the neuron in ($mV$). On the x-axis is the time 
        of simulation in ($ms$). Notice that it takes about 18 ($ms$) for a neuron to fire. 
        This is the industry established value for neuron firing. The line represented in
        orange is the activity of one output neuron, while the line represented in blue is the 
        activity of the other. Notice that when one fires, the other does not and vice versa. 
        
        '''
        streamlit.write(simOptionMsg)

        user_input = streamlit.number_input("", min_value=1, max_value=100, value=1)
        time, first, second = run_sim(user_input)

        nrn1_base = [-39.95669640552794, -39.78765004501495, -39.13022405432472, -37.02429684470145, -31.496478551237022, -19.702852360771175, 0.4667385288586595, 27.388903360285745, 53.73581678628326, 68.90548171240849, 65.68683830675556, 45.66808613785454, 18.00216664473536, -7.1982992627124265, -24.505573698685073, -33.88661661273688, -37.98527972223925, -39.445406371434, -39.872484790870494, -39.97551071573893, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0]
        nrn2_base = [-40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -40.0, -39.95669640552794, -39.78765004501495, -39.13022405432472, -37.02429684470145, -31.496478551237022, -19.702852360771175, 0.4667385288586595, 27.388903360285745, 53.73581678628326, 68.90548171240849, 65.68683830675556, 45.66808613785454, 18.00216664473536, -7.1982992627124265, -24.505573698685073, -33.88661661273688, -37.98527972223925, -39.445406371434, -39.872484790870494, -39.97551071573893]
        
        
        if(user_input == 1):
            nrn1_np = np.array(nrn1_base)
            nrn2_np = np.array(nrn2_base)
        else:
            nrn1 = []
            nrn2 = []
            for i in range(0, user_input):
                nrn1+=nrn1_base
                nrn2+=nrn2_base
            
            nrn1_np = np.array(nrn1)
            nrn2_np = np.array(nrn2)



        chart_data = pd.DataFrame(np.column_stack((nrn1_np, nrn2_np)), columns=['Output Neuron One', 'Output Neuron Two'])

        streamlit.line_chart(chart_data, width=700, height=450)

