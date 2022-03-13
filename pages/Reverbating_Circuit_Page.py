import streamlit as st 
from Diverging_Circuit import DivergingNetwork
from stvis import pv_static
from pyvis import network as net



def app():
    
    mainContainer = st.container()
    with mainContainer:
        st.title("Foundational Neural Circuits", anchor=None)
        st.markdown("***")

        st.subheader("Reverberating Circuits")

        msg1 = """
        Reverberating circuits differ from Converging/Diverging in that they have neurons 
        with branches that go backward to stimulate the neuron earlier in the circuit. 
        Recall that neurons only send messages one way, so such a circuit requires
        a place for an axon to backtrack to a dendrite of an earlier axon. For example,
        a reverberating circuit in the body would be used to control a particular repetitive action, such
        as breathing. Furthermore, homeostatic mehcanisms such as the regulation of blood glucose levels, body 
        temperature, and thirst are controlled by reverberating circuits.
        
        In higher levels of the brain, reverberating circuits are often seen to control consciousness, 
        for without a constant restimulation through the circuit, there would be no continuity to
        our consciousness. Additionally, some of these circuits require specific circumstances to break the circuit, 
        such as as when we fall asleep. 
        """

        st.write(msg1)

        msg2 = """
        Below is a diagramtic graph representation of how such a circuit would look like in the brain. Notice that
        the output neuron connects back to the input neuron, forming a circular loop. 
        """

        st.write(msg2)

        graph_rev = net.Network(height='500px', width='700px', bgcolor='#222222', font_color='white',directed =True)
        graph_rev.toggle_physics(False)

        graph_rev.add_node("Input", label="Input", color='#FFA500')
        graph_rev.add_node("Interneuron 1", label="Interneuron", color='#FF6961')
        graph_rev.add_node("Interneuron 2", label="Interneuron", color='#FF6961')
        graph_rev.add_node("Interneuron 3", label="Interneuron", color='#FF6961')
        graph_rev.add_node("Output", label="Output", color='#A7C7E7')

        graph_rev.add_edge("Input", "Interneuron 1", color='#FFFFFF' )
        graph_rev.add_edge("Interneuron 1", "Interneuron 2", color='#FFFFFF' )
        graph_rev.add_edge("Interneuron 2", "Output", color='#FFFFFF' )
        graph_rev.add_edge("Output", "Interneuron 3", color='#FFFFFF' )
        graph_rev.add_edge("Interneuron 3", "Input", color='#FFFFFF' )

        pv_static(graph_rev, "Reverberating Circuit")  

        msg3 = """
        Although this circuit doesn't look as complicated as the Diverging/Converging circuits, it is 
        perhaps the most important building block of other complicated circuits in the brain. The circular, 
        feedback nature allows the circuit a way to regulate itself, proving a powerful mechanism for 
        responding to external stimuli.
        """

        st.write(msg3)

        st.markdown("***")

        st.subheader("Next Steps")

        msg4 = """
        Now that we've become familiar with some fundamental circuits of the brain, we can begin 
        to model more complicated ones. Specifically, we will focus on making an Oscillating Circuit,
        which achieves a harmonic oscillation of two neurons.
        """

        st.write(msg4)





