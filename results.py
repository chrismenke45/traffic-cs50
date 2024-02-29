import matplotlib.pyplot as plt
model_accuracy = []
model_build_time = []
# Results of different Models

# 1 :
#   1 Convolutional Layer - learn 32 filters using 3x3 kernal
#   1 Max-Pooling layer using 2x2 pool size
#   Flatten units
#   1 hidden layer with 128 units and dropout of 0.2
#   Output layer
model_accuracy.append([0.7675, 0.9237, 0.8347])
model_build_time.append([114, 111, 109])
# 2 :
#   1 Convolutional Layer - learn 32 filters using 3x3 kernal
#   1 Max-Pooling layer using 2x2 pool size
#   Flatten units
#   2 hidden layers with 128 units and dropout of 0.2
#   Output layer
model_accuracy.append([0.6942, 0.7249, 0.8609])
model_build_time.append([112, 129, 150])
# 3 :
#   1 Convolutional Layer - learn 32 filters using 3x3 kernal
#   1 Max-Pooling layer using 2x2 pool size
#   Flatten units
#   3 hidden layers with 128 units and dropout of 0.2
#   Output layer
model_accuracy.append([0.5409, 0.6971, 0.4813])
model_build_time.append([114, 114, 168])

# 4 :
#   1 Convolutional Layer - learn 32 filters using 3x3 kernal
#   1 Max-Pooling layer using 2x2 pool size
#   Flatten units
#   1 hidden layer with 128 units and dropout of 0.5
#   Output layer
model_accuracy.append([0.4813, 0.2935])
model_build_time.append([168, 115])

# 5 :
#   1 Convolutional Layer - learn 32 filters using 3x3 kernal
#   1 Max-Pooling layer using 2x2 pool size
#   1 Convolutional Layer - learn 32 filters using 3x3 kernal
#   1 Max-Pooling layer using 2x2 pool size
#   Flatten units
#   1 hidden layer with 128 units and dropout of 0.2
#   Output layer
model_accuracy.append([0.9506, 0.9617, 0.9483])
model_build_time.append([118, 159, 131])

# 6 :
#   1 Convolutional Layer - learn 32 filters using 3x3 kernal
#   1 Max-Pooling layer using 2x2 pool size
#   1 Convolutional Layer - learn 32 filters using 3x3 kernal
#   1 Max-Pooling layer using 2x2 pool size
#   1 Convolutional Layer - learn 32 filters using 3x3 kernal
#   1 Max-Pooling layer using 2x2 pool size
#   Flatten units
#   1 hidden layer with 128 units and dropout of 0.2
#   Output layer
model_accuracy.append([0.9549, 0.9208, .9363])
model_build_time.append([142, 138, 139])

markers = ["*", "+", "^", "o", "x", "s"]
for index in range(len(model_accuracy)):
    label = "Model #" + str(index + 1)
    plt.scatter(model_build_time[index], model_accuracy[index], marker=markers[index], label=label)
plt.legend()
plt.xlabel('Time to train model (s)')
plt.ylabel('Accuracy')
plt.title('Model Accuracy vs Training Time')
plt.show()
