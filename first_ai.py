import numpy as np

def sigoid(x):
    return 1 / (1 + np.exp(-x))

def sigoid_deri(x):
    return x *(1 - x)

training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])
    
training_outputs = np.array([[0,1,1,0]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3, 1)) - 1

print("Randon starting synaptic weigts: ")
print(synaptic_weights)

for i in range(1):
    
    input_layer = training_inputs
    
    outputs = sigoid(np.dot(input_layer, synaptic_weights))
    
    error =  training_outputs - outputs
     
    adjustmets = error * sigoid_deri(outputs)
    
    synaptic_weights += np.dot(input_layer.T, adjustmets)
    
print("Synaptic weights after training: ")
print(synaptic_weights )
print("Outputs after: ")
print(outputs)
