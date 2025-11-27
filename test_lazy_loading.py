import streamlit as st
import time

st.title("Lazy Loading Test")

@st.cache_resource
def heavy_computation():
    """Simulate heavy model loading"""
    time.sleep(3)  # Simulate 3 second load time
    return "Model loaded successfully!"

st.write("UI loads immediately!")
st.write("Click button to trigger heavy computation:")

if st.button("Load Heavy Resource"):
    with st.spinner("Loading..."):
        result = heavy_computation()
        st.success(result)

st.write("This text appears immediately without waiting for heavy computation")