import pandas as pd
import plotly.express as px
import math
import streamlit as st
import random
import time
import plotly.graph_objects as go
import numpy as np

import streamlit as st
import plotly.express as px
import time
import pandas as pd

# Step 1: Create the Plotly figure with all frames
st.set_page_config(page_title='SPINNY',layout='wide',initial_sidebar_state='collapsed')
st.markdown(f"<h1 style='text-align: center; color: Purple;margin:0; padding:0;'>FIGHT THIS OUT!</h1><BR><BR>", unsafe_allow_html=True)

st.markdown("""
<style>
    .centered-triangle {
        position: fixed;
        top: 23%;
        left: 50%;
        transform: translate(-50%, -50%) rotate(180deg);
        width: 0;
        height: 0;
        border-left: 10px solid transparent;
        border-right: 10px solid transparent;
        border-bottom: 20px solid #000; /* Adjust color as needed */
        z-index: 9999;
    }
</style>
<div class="centered-triangle"></div>
""", unsafe_allow_html=True)
labels = ['Rock Paper Scissors','Draw Straws','Odd/Even','Coin Flip','Palm Up/Down','Paper BBall','tic-tac-toe','Pool/Foosball','Spin Again!','#1-10']
values = [10] * len(labels)
def get_plotly_fig(rotation_angle):
    fig = go.Figure(
    data=[
        go.Pie(
            labels=labels, 
            values=values,
            textinfo='label', 
            rotation=rotation_angle,
            showlegend=False
        )
    ])
    # Remove the default animation controls
    fig.layout.updatemenus = [
        {
            "buttons": [],
            "showactive": False,
        }
    ]
    fig.update_layout(width = 600,
        height = 500,
        margin=dict(l=0, r=0, t=0, b=0))
    return fig

# Function to execute after the animation completes
def animation_complete_action():
    st.write("### Spin Complete!")
    st.balloons()
    # Any other Python logic you want to run
    print("Animation finished. Python function was executed.")

# Initialize session state for animation tracking
if "animation_running" not in st.session_state:
    st.session_state.animation_running = False
if "current_frame" not in st.session_state:
    st.session_state.current_frame = 0

# Create an empty container for the plot
plot_container = st.empty()
fig = get_plotly_fig(0)
plot_container.plotly_chart(fig,key = 'a',use_container_width=True)
# Create a container for the buttons
_,button_col, _ = st.columns([6,1.8, 5])
with button_col:
    start_button = st.button("▶️ SPIN!")

# Check if the button was clicked
if start_button:
    st.session_state.animation_running = True
    st.session_state.current_frame = 0

# Animation loop
if st.session_state.animation_running:
    # fig = get_plotly_fig()
    frames = []
    n =  random.randint(20, len(labels)*10)
    # # n=32
    # st.write(n)
    degree = 360/len(labels)

    # st.write(n)
    for i in range(1,n): # 36 frames for a full 360-degree rotation (10 degrees per frame)
        rotation_angle = i * (degree/2)
        fig = get_plotly_fig(rotation_angle)
        plot_container.plotly_chart(fig,key = i,use_container_width=True)
        time.sleep(0.05)

        # Advance the counter (for session_state keeping consistency)
        st.session_state.current_frame += 1

    # When we exit the loop, the animation is finished
    st.session_state.animation_running = False
    st.session_state.current_frame = 0

    # Final frame (full rotation) – already rendered by the loop
    var = math.floor(n/2)
    if var > len(labels):
        index = var%len(labels)
    else:
        index = var
    st.success('Spin Complete!: '+str(labels[index]))
    st.balloons()
    # print("Animation finished. Python function was executed.")

else:
    # Show a static pie when the animation is not running
    fig = get_plotly_fig(0)


# # Sample data
# labels = ['Rock Paper Scissors','Draw Straws','Odd/Even','Coin Flip','Palm Up/Down','Paper BBall','tic-tac-toe','Pool/Foosball','Spin Again!','#1-10']
# values = [10] * len(labels)

# frames = []
# n =  random.randint(20, len(labels)*10)
# # # n=32
# # st.write(n)
# degree = 360/len(labels)

# # st.write(n)
# for i in range(n): # 36 frames for a full 360-degree rotation (10 degrees per frame)
#     rotation_angle = i * (degree/2)
#     frame = go.Frame(data=[go.Pie(labels=labels, values=values, rotation=rotation_angle,showlegend=False)])
#     frames.append(frame)
# st.markdown(f"<h1 style='text-align: center; color: Purple;margin:0; padding:0;'>FIGHT THIS OUT!</h1><BR><BR>", unsafe_allow_html=True)

# st.markdown("""
# <style>
#     .centered-triangle {
#         position: fixed;
#         top: 23%;
#         left: 50%;
#         transform: translate(-50%, -50%) rotate(180deg);
#         width: 0;
#         height: 0;
#         border-left: 10px solid transparent;
#         border-right: 10px solid transparent;
#         border-bottom: 20px solid #000; /* Adjust color as needed */
#         z-index: 9999;
#     }
# </style>
# <div class="centered-triangle"></div>
# """, unsafe_allow_html=True)

# fig = go.Figure(
#     data=[
#         go.Pie(
#             labels=labels, 
#             values=values,
#             textinfo='label', 
#             rotation=0,
#             showlegend=False
#         )
#     ],
#     layout=go.Layout(
#         updatemenus=[
#             dict(
#                 type="buttons",
#                 # Position: center horizontally, bottom of the plotting area
#                 x=0.5,
#                 y=-0.1,
#                 xanchor="center",
#                 yanchor="bottom",
#                 pad=dict(t=0, l=0, r=0, b=0),
#                 bgcolor="red", 
#                 # Button style
#                 buttons=[
#                     dict(
#                         label="SPIN!",
#                         method="animate",
#                         args=[
#                             None, 
#                             {
#                                 "frame": {"duration": 120, "redraw": True},
#                                 "fromcurrent": True, 
#                                 "transition": {"duration": 120, "easing": "linear"}
#                             }
#                         ],
#                     )
#                 ],
#                 font=dict(color='red')
#             )
#         ],
#         width = 600,
#         height = 600,
#         margin=dict(l=0, r=0, t=0, b=0),
#     ),
#     frames=frames
# )
# fig.update_traces(domain=dict(x=[0, 1], y=[0, 1]))
# st.plotly_chart(fig,use_container_width=True)
# var = math.floor(n/2)
# if var > len(labels):
#     index = var%len(labels)
# else:
#     index = var
# # A button to trigger the calculation after the animation is perceived to be done
# if st.button("Refresh Spin"):
#     st.session_state.animation_started = True
#     st.session_state.final_index = index
# st.balloons()
