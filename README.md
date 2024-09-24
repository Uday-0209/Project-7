# condition-monitering-of-the-ball-screw
This project was developed to detect faults in the ball screw and coupling of the test rig. The model is based on vibration data. By analyzing changes in vibration and its features, the model predicts whether the system's vibration is 'Good' or 'Bad,' and also assesses the condition of the coupling

The methodology followed to develop this model is as follows:

1) Initially, we acquired vibration data from the test rig when it was installed with a good ball screw and coupling.
2) The same process was followed for the test rig with a dented and damaged ball screw, as well as a broken and cracked coupling.
3) Data was acquired for different feed rates, ranging from 1000 to 20000 (100 rpm to 2000 rpm), with a sample rate of 10,000 Hz for 5-second intervals.
4) Initially, the model was developed for a single channel, where the sensor was placed along the ball screw axis in the test rig.
5) A second model was developed for 3-channel data, where sensors were placed under the nut of the test rig.
6) The data was processed, downsampled, and plotted in STFT format. After applying PCA, the data was stacked and labeled according to its characteristics, such as 'Good' or 'Bad' and 'Coupling in good condition' or 'Coupling in bad condition.'
7) A LabVIEW program was developed to provide both frontend and backend support. In the backend, after plotting the data as STFT, it was pushed to a Python node for analysis. The node analyzed and predicted the condition of the system's vibration.
8) A basic Logistic Regression model was used, achieving an accuracy of 92%.
9) The model also performed well in real-time system monitoring.

Here is images of labview frontend and backend for single channel analyzer:
![Fault prediction for single channel](https://github.com/user-attachments/assets/cbfa9eb7-910f-4191-8189-d169af239baf)

In the above images you can see the condtion of the system vibration and condition of the coupling been given.

![producer and consumer vibration ml single channel backend1](https://github.com/user-attachments/assets/37ef1b8e-3c6d-4bb2-bd36-47e33f211e41)

![producer and consumer vibration ml single channel backend2](https://github.com/user-attachments/assets/6e50d316-daa6-4cbc-b6bd-524240445f1f)
