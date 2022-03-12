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

    streamlit.write("The brain is a computer. Granted, it can do complicated things that traditional computers can't do like think, feel, or learn. But at the end of the day, it is a computer. And much like traditional computers, it functions using circuits. There are many different types of circuits in the brain, ranging from ones with a few neuron to ones that span across the entire organ. To learn more about these mysterious computer like circuits in the brain, we will build simulations and try to understand what's really going on.")


