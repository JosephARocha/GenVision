# GenVision
Final Project for CS 6243: Machine Learning; Facial Detection to predict whether a given input image is male or female

# Network Architecture
![Alt text](https://raw.githubusercontent.com/JosephARocha/GenVision/master/GenVisionArchitecture.PNG "Screen shot showing current release")</br>
We used a simple Convolutional Neural Network for our learning model. The network is divided into three convolutional network stacks. Each stack contains two convolutional layers with Rectifier Linear Unit (ReLU) activation functions and a 2x2 max pooling layer to protect our model against overfitting by ensuring only important features get propagated further into the network. On the first network stack, each two dimensional convolutional layer has 128 output filters. The second network stack has 64 output filters, and the third has 32 output filters. The third stack feeds into a 16 neuron fully connected layer with  a ReLU activation function, and then it’s output is sent to a single neuron with a sigmoid activation function.

# Training and Accuracy
We trained our network for 30 epochs during a period of approximately 5 hours using a Graphical Processing Unit. With our training data we got an accuracy of 81% with a loss of 0.4122. During the validation, we found an accuracy of 92.2% with a loss of 0.2101. During training we found that the model would increase in accuracy until approximately 91% then the model would diverge to 50%. Upon testing we discovered that the model would always predict male. 
To rectify this we introduced a set learning rate of 0.001 with a decay of 0.000066. The model was then trained for 15 epochs during a period of approximately 2.5 hours which resulted in a final validation __accuracy of 95.2%__ with a loss of 0.1392. 


# Demo
![Alt text](https://raw.githubusercontent.com/JosephARocha/GenVision/master/GenVision.PNG "Screen shot showing current release")

You can try it out at http://JosephRocha.io/GenVision </br>
The paper can be read at: TBD
