import streamlit as st 
from Diverging_Circuit import DivergingNetwork
from stvis import pv_static
from pyvis import network as net



def app():
    
    mainContainer = st.container()
    with mainContainer: 
        st.title("Foundational Neural Circuits", anchor=None)
        st.markdown("***")

        st.subheader("Introduction to Neural Circuits")

        msg1 = """
        The brain is a computer. Granted, it can do complicated things that traditional 
        computers can't do like think, feel, or learn. But at the end of the day, it is 
        a computer. And much like traditional computers, it functions using circuits. There 
        are many different types of circuits in the brain, ranging from ones with a few neuron 
        to ones that span across an entire organ. To learn more about these mysterious computer 
        like circuits in the brain, we will build simulations and to learn what's really going on. 
        """

        st.write(msg1)

        st.subheader("Diverging Circuit")


        msg2 = """
        Perhaps one of the simplest circuit to exist in the brain is a diverging circuit. 
        In brief, it is a circuit consisting of one input neuron that 
        activates thousands, if not millions, of other neurons. For example, a diverging circuit of 
        sensory neurons is often observed to stimulate various parts of the brain, all with one input neuron.
        A singular visual images would need response from a wide variety of outputs such as the 
        amount of light to open or close the pupil, or to interpret words, or identify the emotions behind a 
        facial expression; a diverging circuit would thus send the same signal to multiple locations in the brain.
        """

        st.write (msg2)

        msg3 = """  
        Below is a diagrammatic graph representation of how such a circuit would look like in the brain. Notice that
        a singular input neuron activates many other neurons, layer by layer.

        """
        st.write(msg3)

        graph_div = net.Network(height='500px', width='700px', bgcolor='#222222', font_color='white',directed =True)
        graph_div.toggle_physics(False)
        graph_div.add_node("Input Neuron", label="Input", color='#FFA500')
        graph_div.add_node("Interneuron 1", label="Interneuron", color='#FF6961')
        graph_div.add_node("Interneuron 2", label="Interneuron", color='#FF6961')
        graph_div.add_node("Interneuron 3", label="Interneuron", color='#A7C7E7')
        graph_div.add_node("Interneuron 4", label="Interneuron", color='#A7C7E7')
        graph_div.add_node("Interneuron 5", label="Interneuron", color='#A7C7E7')
        graph_div.add_node("Interneuron 6", label="Interneuron", color='#A7C7E7')
        graph_div.add_node("Output 1", label="Output 1", color='#fdfd96')
        graph_div.add_node("Output 2", label="Output 2", color='#fdfd96')
        graph_div.add_node("Output 3", label="Output 3", color='#fdfd96')
        graph_div.add_node("Output 4", label="Output 4", color='#fdfd96')
        graph_div.add_node("Output 5", label="Output 5", color='#fdfd96')
        graph_div.add_node("Output 6", label="Output 6", color='#fdfd96')
        graph_div.add_node("Output 7", label="Output 7", color='#fdfd96')
        graph_div.add_node("Output 8", label="Output 8", color='#fdfd96')

        graph_div.add_edge("Input Neuron", "Interneuron 1", color='#FFFFFF')
        graph_div.add_edge("Input Neuron", "Interneuron 2", color='#FFFFFF')
        graph_div.add_edge("Interneuron 1", "Interneuron 3", color='#FFFFFF')
        graph_div.add_edge("Interneuron 1", "Interneuron 4", color='#FFFFFF')
        graph_div.add_edge("Interneuron 2", "Interneuron 5", color='#FFFFFF')
        graph_div.add_edge("Interneuron 2", "Interneuron 6", color='#FFFFFF')
        graph_div.add_edge("Interneuron 3", "Output 1", color='#FFFFFF')
        graph_div.add_edge("Interneuron 3", "Output 2", color='#FFFFFF')
        graph_div.add_edge("Interneuron 4", "Output 3", color='#FFFFFF')
        graph_div.add_edge("Interneuron 4", "Output 4", color='#FFFFFF')
        graph_div.add_edge("Interneuron 5", "Output 5", color='#FFFFFF')
        graph_div.add_edge("Interneuron 5", "Output 6", color='#FFFFFF')
        graph_div.add_edge("Interneuron 6", "Output 7", color='#FFFFFF')
        graph_div.add_edge("Interneuron 6", "Output 8", color='#FFFFFF')

        pv_static(graph_div)  

        st.markdown("***")

        st.subheader("Converging Circuit")

        msg5 = """
        The converging circuit is a circuit that can be thought as the opposite of a diverging circuit.
        In brief, it consists of thousands of input neurons sending signals to activate a singular output neuron. 
        In the human body, most converging circuits are found in the neuromuscular system. Considering breathing, for 
        instance. One does not have to think about breathing, making it an involuntary process. However, we also have 
        the ability to hold and control our breathing (which is voluntary). The only way that is possible is through a converging circuit,
        which will allow stimulus for the diaphragm by either a voluntary or involuntary neuron. 
        """

        st.write(msg5)

        msg6 = """
        Below is a diagrammatic representation of how such a circuit would look like in the brain. Notice that
        many neurons all end up activating the same output neuron. 
        """

        st.write(msg6)

        graph_con = net.Network(height='500px', width='700px', bgcolor='#222222', font_color='white',directed =True)
        graph_con.toggle_physics(False)

        graph_con.add_node("Input 1", label="Input 1", color='#FFA500')
        graph_con.add_node("Input 2", label="Input 2", color='#FFA500')
        graph_con.add_node("Input 3", label="Input 3", color='#FFA500')
        graph_con.add_node("Input 4", label="Input 4", color='#FFA500')
        graph_con.add_node("Input 5", label="Input 5", color='#FFA500')
        graph_con.add_node("Input 6", label="Input 6", color='#FFA500')
        graph_con.add_node("Input 7", label="Input 7", color='#FFA500')
        graph_con.add_node("Input 8", label="Input 8", color='#FFA500')
        graph_con.add_node("Inter 1", label="Interneuron 1", color='#A7C7E7')
        graph_con.add_node("Inter 2", label="Interneuron 2", color='#A7C7E7')
        # graph_con.add_node("Inter 3", label="Interneuron 3", color='#A7C7E7')
        # graph_con.add_node("Inter 4", label="Interneuron 4", color='#A7C7E7')
        graph_con.add_node("Output", label="Output", color='#fdfd96')

        graph_con.add_edge("Input 1", "Inter 1", color='#FFFFFF')
        graph_con.add_edge("Input 2", "Inter 1", color='#FFFFFF')
        graph_con.add_edge("Input 3", "Inter 1", color='#FFFFFF')
        graph_con.add_edge("Input 4", "Inter 1", color='#FFFFFF')
        graph_con.add_edge("Input 5", "Inter 2", color='#FFFFFF')
        graph_con.add_edge("Input 6", "Inter 2", color='#FFFFFF')
        graph_con.add_edge("Input 7", "Inter 2", color='#FFFFFF')
        graph_con.add_edge("Input 8", "Inter 2", color='#FFFFFF')
        graph_con.add_edge("Inter 1", "Output", color='#FFFFFF')
        graph_con.add_edge("Inter 2", "Output", color='#FFFFFF')
        # graph_con.add_edge("Inter 1", "Output", color='#FFFFFF')
        # graph_con.add_edge("Inter 2", "Output", color='#FFFFFF')
        # graph_con.add_edge("Inter 3", "Output", color='#FFFFFF')
        # graph_con.add_edge("Inter 4", "Output", color='#FFFFFF')


        pv_static(graph_con)  










