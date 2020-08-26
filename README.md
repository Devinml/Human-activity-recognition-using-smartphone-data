# Human Activity Recognition
## Background
The modern-day smartphone is a pretty incredible piece of equipment that is fitted with a wide range of sophisticated measurement sensors. And when it comes to sensor data, there are many tools available to analyze that data. Being formally trained as an engineer, when I see acceleration data, I might take a different approach than a typical Data Scientist and in this project, I want to show the advantages that might hold. This project uses a UCI data repository of smartphone data to label an activity the activities are outlined below, and I will show how a model can be improved by implementing power spectral density analysis with statistics; can aid in the classifying of human activity. 
1. Walking           
2. Walking Upstairs  
3. Walking Downstairs
4. Sitting           
5. Standing          
6. Laying    
## The Data
Each row of data contained acceleration in the X, Y, and Z direction as well as angular accelerations about XYZ, from a Samsung Galaxy SII internal accelerometer and gyroscope. The data was collected at 50 Hz (50 times a second) for 30 subjects doing the previous 6 activities. Each experiment lasted approximately 15 minutes and the data was manually labeled. This led to 1122773 rows of data.

Note: The orientation of the phone was kept the same during all experiments but it is unclear in the data set which direction the XYZ axis were in relation to the phone. These pictures help as a contextual understanding of the acceleration directions but should not be used as an actual interpretation.
<p align="center">
  <img src="imgs/phone_acc_gyro.jpeg" >
</p>

## EDA
### Statistical Analysis
When looking at the data it becomes clear that there is an underlying signal in the data, especially when comparing the laying down signal to the rest of the data. It is also obvious that the standing and sitting signals have a much smaller standard deviation.<p align="center">
  <img src="imgs/X_acc_box.png" >
</p>

When we look at the angular acceleration, the immediate observation is that the static movements immediately fall out as they are not affected by gravity unlike the X, Y, or Z accelerometer measurements. It is clear that if the model was trying to label acceleration that came from standing it basically has to take a 50 50 guess because the X acceleration is very low for lying down and the standard deviations for the dynamic movements are much higher. 

<p align="center">
  <img src="imgs/gyroX_acc_box.png" >
</p>

### Power Spectral Density Analysis 
Power spectral density analysis is simply trying to find out what frequencies are in your data and how often they appear, where frequency is how often something happens, and is usually measured in Hz (Hertz). Let's take a look at raw acceleration data and see how this might be helpful. 

<p align="center">
  <img src="imgs/raw_acc_X.png" >
</p>

At first pass, it doesn't look like there isn't much of a difference between these two plots, besides that the peaks of the walking downstairs dataset seem to be higher. Power spectral density allows us to break down the signal and see what underlying frequencies are present and the strength of the signal at that frequency. 

<p align="center">
  <img src="imgs/gyroY_Up_walk.png" >
</p>

I broke up my into 3 sections in which the peaks most notable seperable and which would capture most of the peaks.
<p align="left">
  <img src="imgs/gyroY_down_integral.png" ><img src="imgs/gyroY_walk_integral.png" >
</p>

## Data Prep

I prepared 3 data sets to train a model on by taking subsamples of my original dataset, to avoid problems in calculating the spectral density calculations. The data was broken up by participants and activity and I took 120 samples of that data and made a new row of data from calculating the statistics and the integral of the intensity bands of those 120 points. This led to 3 data sets:
1. Stats Dataset: where mean and standard deviation were captured for each window of data evaluated at each column. 
2. Spectral Density Dataset: where for each window of data evaluated at each column. 
3. Spectra Density and Stats Dataset: This combines the stats dataset and the spectral Density Dataset.
<p align="center">
  <img src="imgs/4cuj4u.gif" >
</p>