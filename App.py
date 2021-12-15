import pandas as pd
import numpy as np
from Network import *
import streamlit 
from stvis import pv_static
from pyvis import network as net



if __name__ == "__main__":

    mainContainer = streamlit.container()

    with mainContainer: 

        streamlit.title("Neural Circuit Simulations", anchor=None)
        streamlit.markdown("Demos by Krish Suraparaju of various circuits found in the brain")

        streamlit.markdown("***")


        streamlit.subheader("Introduction to Neural Circuits")

        
        IntroMsgOne = """
         The brain is a computer. Granted, it can do complicated things that traditional computers can't do like think,
         feel, or learn. But at the end of the day, it is a computer. And much like traditional computers, it functions 
         using circuits. There are many different types of circuits in the brain, ranging from ones with a 
         few neuron to ones that span across the entire organ. To learn more about these mysterious
         computer like circuits in the brain, we will build simulations and try to understand what's really going
         on. Let's start with a simple oscillator in the brain. Most prominant 
         in the neuromotor system, these circuits help the body with coordination. For example, when walking, the 
         brain needs to ensure that the right half of the body is not moving when the left half is and vice versa.
        """

        IntroMsgTwo = """ 
        This simulation builds a small model of this oscillating circuit in python using a Graph data structure. Basically, different nodes
        of the Graph represent different neurons, and the edges between these nodes represent the neuron synapses. 
        Two input neurons give continuous activating signals to two excitatory neurons, which turn 
        on other neurons when activated.
        Along with their respective output neurons, the excitatory neurons are connected to two inhibitory neurons as well.
        Unlike excitatory neurons, inhibitory neurons send a negative signal when they are told to turn on.
        This means that the output of this circuit can be seen as an oscillating pattern. Explore the figure below to see how exactly the connections
        of each neuron give rise to this nature. 
        
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

        streamlit.markdown("***")


        streamlit.subheader("Modeling the circuit")

        huxleyMsg = r'''
        
        One of the best ways to visualize the activity of a neuron is to examine its voltage potential,
        which is the amount of electrical energy that a neuron is holding in its membrane. 
        When a neuron fires, its voltage potential increases until it reaches a threshold, at which point it decreases
        back to its resting potential. For this simulation, I decided to model the current flowing through the neuron as a 
        function of its potential, mainly using the Hodgkin-Huxley equations: 
        $I_m(t)=C_m\frac{dV_m(t)}{dt}$, where $C_m$ is the membrane capacitance of the neuron, $dV_m(t)$ is 
        the differential change in potential across the membrane, and $I_m$ is the current flowing through the neuron.
        In order to get the voltage potentials, we need to solve the above equation for $V_m(t)$. 
        '''

        streamlit.write(huxleyMsg)

        integrateMsg = r'''

        If we re-arrange the above equation, we can see that: $\int{\frac{I_m(t)}{C_m}}dt = V_m(t)$.
        Because computers can't deal with infinite summations, I decided to solve this integral by summing discrete 
        values of time. I arbitrarily chose a time step, $dt$, of 0.1 seconds. 
        So in order to obtain the voltage potential values, I summed outputs of $I_m(t)$ for each time step:
        $V_m(t) = \sum_{i=0}^{n}{I_m(i) \cdot dt}$.

        
        '''

        streamlit.write(integrateMsg)

        # GraphComponent.drawGraph()


        streamlit.markdown("***")

        streamlit.subheader("Run the Simulation")
        simOptionMsg = r'''
        In order to view the results of this simulation, enter the number of iterations you want the 
        network to run for in the box below. The data will be graphed on the plot, with the y-axis 
        representing the voltage potential of the neuron in $mV$, and x-axis representing the time 
        of simulation in $ms$. Notice that it takes about 18 $ms$ for a neuron to fully fire in 
        this simulation. 
        This is how long it takes for an average real life neuron to fire. The line represented in
        orange is the activity of one of the output neuron, while the line represented in blue is the 
        activity of the other. Notice that when one fires, the other does not and vice versa. 
        This is the oscillating pattern that we wanted to simulate.
        
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



        chart_data = pd.DataFrame(np.column_stack((nrn1_np, nrn2_np)), columns=['Output 1', 'Output 2'])

        streamlit.line_chart(chart_data, width=700, height=450)

