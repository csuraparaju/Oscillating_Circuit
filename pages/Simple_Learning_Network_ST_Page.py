import streamlit as st
import altair as alt
from Learning_Circuit import LearningNetwork
from PIL import Image
import numpy as np
import random
import time
from stvis import pv_static
from pyvis import network as net
import pandas as pd

def app():
    st.title("Simple Learning Circuit - Population Simulations")
    st.markdown("***")

    st.subheader("Taking Things to the Next Level")
    msg1 = """
    Up until this point, we've been simulating the behaviors of relatively small circuits. For example,
    the reverberating circuit consisted of 5 neurons in total, and the oscillating circuit had 8 neurons.
    However, most circuits in the brain have a lot more neurons than that. For example, a simple classical 
    conditioning circuit (as seen in Pavlov's dog) has about 650 neurons (13 nuclei total). 
    """
    st.write(msg1)

    msg2 = """
    So, let's scale our simulations. We'll start by simulating the classical conditioning circuit
    with a population of about 1000 neurons. However, instead of teaching dogs to salivate at the sound 
    of a bell, we'll teach the computer to recognize different colors at our command. 
    """
    st.write(msg2)

    st.subheader("Circuit Description")
    msg3 = """
    The general structure of the circuit is described in the graph below. Notice that the actual structure
    is quite simple (hence why it's called a simple learning circuit). However, recall that we will have 
    numerous clusters of this circuit. When brought together, these clusters give rise to the learning behavior we see
    in a brain. 

    When you click on any edge, you may notice that we are using weighted, directed graphs to represent the circuit structure.
    One of the biggest characteristics of learning is that neurons build up stronger and stronger connections to each other
    if they are activated multiple times. When we use a weighted graph, we can represent the strength of the connections between
    neurons as weight, which is just a decimal value between 0 and 1. A weight that is closer to 1 indicates that it is stronger, while
    a weight that is closer to 0 indicates a weaker connection. 
    """

    st.write(msg3)

    graph = net.Network(height='500px', width='700px', bgcolor='#222222', font_color='white',directed =True)
    graph.toggle_physics(False)
    graph.add_node("Input 1", label="Input 1 (Conditioned Stimulus)", color='#698B22')
    graph.add_node("Input 2", label="Input 2 (Conditioned Stimulus)", color='#698B22')
    graph.add_node("Input 3", label="Input 3 (Unconditioned Stimulus)", color='#FF6961')
    graph.add_node("Output 1", label="Output Neuron", color='#93CAED')


    graph.add_edge("Input 1", "Output 1", color='#FFFFFF', title="Weight 0.98")
    graph.add_edge("Input 2", "Output 1", color='#FFFFFF', title="Weight 0.98")
    graph.add_edge("Input 3", "Output 1", color='#FFFFFF', title="Weight 0.21")
    graph.add_edge("Output 1", "Output 1", color='#FFFFFF')


    pv_static(graph)

    st.subheader("Modelling the Circuit")
    msg4 = """
    Now that we're dealing with a large population of neurons, we cannot simply model the behavior of each 
    and every neuron. Instead, we simulate the behavior of the entire population as a whole by using probabilistic models. 
    In our case, we will use the Integral Equation. In brief, this equation states that the activity of
    dynamic neurons at time $t$ (written as $A(t)$ )depends on the fraction of active neurons at earlier times $t'$ multiplied by 
    the probability of observing a spike at $t$ given that a spike happened at $t'$. In mathematical terms, this can be 
    represented as: $A(t)=\int_{-\infty}^{t} P_I(t|t')\cdot A(t')dt'$. Again, since computers cannot do infinite summations,
    I chose to compute this neuron activity as a function of time in discrete chunks, with a chosen $\Delta t = 0.1s$ $\sum_{t=0}^{n} (P_I(t|t')\cdot A(t'))\cdot \Delta t$

    The integral equation is a very powerful tool, and can be used to predict the activity in a homogeneous population of 
    integrate-and-fire neurons, much like the neurons used in our simulations . In each time step, the fraction of neurons that fire 
    is calculated as $A(t)\cdot \Delta t$. 
    Once we calculate this value, we keep track of this and move onto the next time $t'$. Thus, $A(t)$ becomes part of the observed history and we can evaluate the fraction of neurons in the next 
    time step $t+ \Delta t$. Previous reseach has shown that the Integral Equation accurately predicts the activity of a simulation of around 4000 independent integrate-and-fire neurons, which is perfect for our purposes.

    While running the simulation, we can ensure that the circut is actually learning by examining how long it takes 
    for a neuron to fire when it receives the same stimulus it has before. This is because as a circuit learns, 
    the connections between neurons will be more and more active, and cause it to strengthen. As a result, it takes the neuron 
    less time to fire when it recieves a stimulus it has before, indicating that it is learning. Below is a plot of one such occurance
    that is observed in the simulation of the circuit.
    """

    st.write(msg4)


    chart_iter = np.arange(10)
    source = pd.DataFrame({'Time needed to fire': LearningNetwork.get_graph_data(), 'Learning iteration for circuit': chart_iter })


    chart = alt.Chart(source).mark_line(point=True).encode(
        x='Learning iteration for circuit',
        y='Time needed to fire',
    ).interactive().properties(
        width=500,
        height=500
        # title='Proportion of time needed for a neuron to fire after each iteration of learning'
    ).configure_mark(
    opacity=1,
    color='orange',
    )

    st.markdown("###### Neuron Activity as seen from time needed(in $ms$) to fire after each iteration of learning")
    st.altair_chart(chart, use_container_width=True)
    
    

    st.markdown("#### Putting the Circuit to the Test")

    msg5 = """
    Now that we have modelled the behavior of the population, we can put it to the test by teaching the circuit 
    how to differentiate between different colors in solid images. Currently, this circuit learned to only recognize
    red, blue, green, and purple. 
    """

    st.write(msg5)

    st.markdown("** Upload an image of a solid color and let the circuit recognize what color it is! **")



    uploaded_file = st.file_uploader(label='File Uploader', type=['jpg', 'png', 'jpeg'])
    image = None
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True)
    else:
        st.write('Make sure you upload a picture!')

    result = st.button('Run the simulation!')
    
    if result:
        st.markdown('#### The circuit is using the picture as input and analyzing it, hang tight!')

        my_bar = st.progress(0)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)
    

        rgbCode = LearningNetwork.run_sim(image)
        red_tuple = (235, 50, 35, 255)
        green_tuple = (55, 125, 34, 255)
        blue_tuple = (0, 33, 245, 255)
        purple_tuple = (117, 26, 124, 255)


        if rgbCode == red_tuple:
            st.markdown('#### The image is of the color: red.')
        elif rgbCode == green_tuple:
            st.markdown('#### The image is of the color: green.')
        elif rgbCode == blue_tuple:
            st.markdown('#### The image is of the color: blue.')
        elif rgbCode == purple_tuple:
            st.markdown('#### The image is of the color: purple.')
        else:
            st.markdown('#### Sorry, this circuit can only recognize red, blue, green and purple for now!')
    
