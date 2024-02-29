This is some practice with tensorflow for [CS50's Traffic](https://cs50.harvard.edu/ai/2024/projects/5/traffic/). The model predicts which traffic sign is in an image. I wrote all the load_data and get_model functions. I started with 1 convolutional layer, 1 max-pooling layer and a 128 unit hidden layer with a dropout rate of 0.2 ([see this commit](https://github.com/chrismenke45/traffic-cs50/tree/68189010654c5c2dc0b9ec970889c00304ff9728)). I then tweaked the model in a variety of ways to see if I could improve its accuracy or the speed at which the model is made. Results can be seen in the graph below (made with the matplotlib library):<br>
![Figure_1](https://github.com/chrismenke45/traffic-cs50/assets/86500980/05d7babc-db62-40b9-b866-245de5c57dca)
<br>
Summary of different models:
- Model 1:
    1. 1 Convolutional Layer - learn 32 filters using 3x3 kernal
    2. 1 Max-Pooling layer using 2x2 pool size
    3. Flatten units
    4. 1 hidden layer with 128 units and dropout of 0.2
    5. Output layer
- Model 2:
    1. 1 Convolutional Layer - learn 32 filters using 3x3 kernal
    2. 1 Max-Pooling layer using 2x2 pool size
    3. Flatten units
    4. 2 hidden layers with 128 units and dropout of 0.2
    5. Output layer
- Model 3:
    1. 1 Convolutional Layer - learn 32 filters using 3x3 kernal
    2. 1 Max-Pooling layer using 2x2 pool size
    3. Flatten units
    4. 3 hidden layers with 128 units and dropout of 0.2
    5. Output layer
- Model 4:
    1. 1 Convolutional Layer - learn 32 filters using 3x3 kernal
    2. 1 Max-Pooling layer using 2x2 pool size
    3. Flatten units
    4. 1 hidden layer with 128 units and dropout of 0.5
    5. Output layer
- Model 5:
    1. 1 Convolutional Layer - learn 32 filters using 3x3 kernal
    2. 1 Max-Pooling layer using 2x2 pool size
    3. 1 Convolutional Layer - learn 32 filters using 3x3 kernal
    4. 1 Max-Pooling layer using 2x2 pool size
    5. Flatten units
    6. 1 hidden layer with 128 units and dropout of 0.2
    7. Output layer
- Model 6:
    1. 1 Convolutional Layer - learn 32 filters using 3x3 kernal
    2. 1 Max-Pooling layer using 2x2 pool size
    3. 1 Convolutional Layer - learn 32 filters using 3x3 kernal
    4. 1 Max-Pooling layer using 2x2 pool size
    5. 1 Convolutional Layer - learn 32 filters using 3x3 kernal
    6. 1 Max-Pooling layer using 2x2 pool size
    7. Flatten units
    8. 1 hidden layer with 128 units and dropout of 0.2
    9. Output layer
<br>
As seen in the graph, adding additional hidden layers did not help with accuracy, but adding additional convolutional and max-pooling layers did. 
