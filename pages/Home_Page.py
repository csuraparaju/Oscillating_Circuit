import streamlit
from PIL import Image




def app():
    streamlit.title("Modelling Neural Circuits in the Human Brain")
    streamlit.markdown("#### An independent study project by [Krish Suraparaju](https://krishsuraparaju.me/) with guidance from [Dr. Elizabeth Ryder](https://www.wpi.edu/people/faculty/ryder)")
    streamlit.markdown("***")

    streamlit.write("Intrigued by the brain, I wanted to learn more about the physiology of its functionality. Working with Dr. Elizabeth Ryder, a professor of Computational Biology at WPI, I realized that simulating its functions is an excellent way to eliminate the mysteries and get a better understanding of the brain. This website showcases all the simulations I've done so far, while also presenting the information I learned in a clear and concise manner in the hopes that it will be of use to others.")

    image = Image.open('./images/connectome.jpeg')
    
    col1, col2, col3 = streamlit.columns([1,6,1])

    with col1:
        streamlit.write("")

    with col2:
        streamlit.image(image)

    with col3:
        streamlit.write("")

    msg2 = """
    Explore the simulations by clicking on the different pages showcased on the 
    left navigation bar. Currently, I've simulated an oscillating circuit and am working on 
    building a simple learning circuit. In brief, an oscillating circuit is used to express 
    harmonic firings of two neurons (one fires when the other doesn't and vice versa), while 
    a learning circuit consists of neurons strengething or weakening their connections 
    to others, based on feedback they receive from their inputs. 
    """
    streamlit.write(msg2)


