# GenVision
Final Project for CS 6243: Machine Learning; Facial Detection to predict whether a given input image is male or female

# Network Architecture
![Alt text](https://raw.githubusercontent.com/JosephARocha/GenVision/master/GenVisionArchitecture.PNG "Screen shot showing current release")</br>
We used a simple Convolutional Neural Network for our learning model. The network is divided into three convolutional network stacks. Each stack contains two convolutional layers with Rectifier Linear Unit (ReLU) activation functions and a 2x2 max pooling layer to protect our model against overfitting by ensuring only important features get propagated further into the network. On the first network stack, each two dimensional convolutional layer has 128 output filters. The second network stack has 64 output filters, and the third has 32 output filters. The third stack feeds into a 16 neuron fully connected layer with  a ReLU activation function, and then it’s output is sent to a single neuron with a sigmoid activation function.



# Demo
![Alt text](https://raw.githubusercontent.com/JosephARocha/GenVision/master/GenVision.PNG "Screen shot showing current release")

You can try it out at http://JosephRocha.io/GenVision
