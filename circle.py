import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Create a Streamlit app
st.title("Colorful Pattern with Streamlit")
# Get user input for the number of repetitions
repetitions = st.slider("Number of Repetitions", 1, 100, 10)


# Function to generate the colorful pattern
def generate_pattern(repetitions):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_facecolor("black")
    colors = ["red", "yellow", "green", "blue", "orange"]

    for _ in range(repetitions):
        for i, col in enumerate(colors):
            angle = i * (360 / len(colors))
            x = 0.5 * np.cos(np.radians(angle))
            y = 0.5 * np.sin(np.radians(angle))
            circle = plt.Circle(
                (x, y), 0.05, color=col, fill=False, linewidth=2, alpha=0.7
            )
            ax.add_patch(circle)

    ax.set_xlim(-0.6, 0.6)
    ax.set_ylim(-0.6, 0.6)
    ax.axis("off")  # Turn off the axes
    st.pyplot(fig)


# Button to generate the pattern
if st.button("Generate Pattern"):
    generate_pattern(repetitions)
