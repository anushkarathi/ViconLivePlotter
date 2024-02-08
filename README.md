# ViconLivePlotter
This repo contains the code for various live-feedback scripts for the lab's Vicon system, written in python. If you make another cool GUI or script, please contribute it back!

## Contents
- `AMTI_BalanceBoard.py` creates a figure with two bar charts that scale with the force on AMTI plates 2 and 3. The bars change color to try to promote symmetric loading on the two plates. This is useful in sit/stand training for prostheses. 

## Installation
Follow vicon sdk install guide here: https://docs.vicon.com/display/DSSDK112/Vicon+DataStream+SDK+Quick+Start+Guide+for+Python

Note: Make sure you're installing as admin on windows or it will error. 

## Other Resources
The full SDK documentation is helpful when adding functionality to the vicon sdk wrapper. It is available here: https://docs.vicon.com/spaces/viewspace.action?key=DSSDK112&preview=/178095318/178095321/Vicon%20DataStream%20SDK%20Developer%27s%20Guide.pdf