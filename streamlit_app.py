import streamlit as st

# Show title and description.
st.title("Convolutional Neural Network Facial Recognition Application")

st.write(
    "This is a complex facial recognition application that uses a Convolutional Neural Network to identify different faces, "
    "using a database of images of the same person with multiple different angles, emotions, and facial expressions throughout their lifetime. "
    "This is a great tool for security and law enforcement to identify people in a crowd or within a large database of images. "
    "It can also be used with cameras on smart devices to increase security and privacy when accessing confidential information."
)


st.header('Scrolling Columns')

cols = st.columns(3)

cols[0].write('A short column')
cols[1].write('Meow' + ' meow'*1000)
cols[2].write('Another short column')

css='''
<style>
    section.main>div {
        padding-bottom: 1rem;
    }
    [data-testid="column"]>div>div>div>div>div {
        overflow: auto;
        height: 70vh;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)