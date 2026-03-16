import numpy as np
import pandas as pd

def load_data(path) :
    df = pd.read_csv(path)
    
    data = df.values
    
    x = data[:, :9]
    y = data[:, 9]
    y = y.reshape(-1,1)
    
    return x, y

def init_parameters() :
    W1 = np.random.randn(9,64) * np.sqrt(2/9)
    b1 = np.zeros((1,64))

    W2 = np.random.randn(64,32) * np.sqrt(2/64)
    b2 = np.zeros((1,32))

    W3 = np.random.randn(32,1) * np.sqrt(2/32)
    b3 = np.zeros((1,1))
    
    params = {
        "W1": W1,
        "b1": b1,
        "W2": W2,
        "b2": b2,
        "W3": W3,
        "b3": b3
    }

    return params

def forward(X, params):

    W1 = params["W1"]
    b1 = params["b1"]

    W2 = params["W2"]
    b2 = params["b2"]

    W3 = params["W3"]
    b3 = params["b3"]

    Z1 = X @ W1 + b1
    A1 = relu(Z1)

    Z2 = A1 @ W2 + b2
    A2 = relu(Z2)

    y_hat = A2 @ W3 + b3

    cache = {
        "Z1": Z1, "A1": A1,
        "Z2": Z2, "A2": A2,
        "y_hat": y_hat
    }

    return y_hat, cache

def relu(Z):
    return np.maximum(0, Z)

def relu_derivative(Z):
    return (Z > 0).astype(float)

def compute_loss(y_hat, y):

    n = y.shape[0]

    loss = np.mean((y_hat - y) ** 2)

    return loss

def backward(X, y, y_hat, params, cache):

    n = X.shape[0]

    W2 = params["W2"]
    W3 = params["W3"]

    A1 = cache["A1"]
    A2 = cache["A2"]
    Z1 = cache["Z1"]
    Z2 = cache["Z2"]

    # output gradient
    dy = (2/n) * (y_hat - y)

    # layer 3
    dW3 = A2.T @ dy
    db3 = np.sum(dy, axis=0, keepdims=True)

    dA2 = dy @ W3.T

    # layer 2
    dZ2 = dA2 * relu_derivative(Z2)

    dW2 = A1.T @ dZ2
    db2 = np.sum(dZ2, axis=0, keepdims=True)

    dA1 = dZ2 @ W2.T

    # layer 1
    dZ1 = dA1 * relu_derivative(Z1)

    dW1 = X.T @ dZ1
    db1 = np.sum(dZ1, axis=0, keepdims=True)

    grads = {
        "dW1": dW1, "db1": db1,
        "dW2": dW2, "db2": db2,
        "dW3": dW3, "db3": db3
    }

    return grads

def update_parameters(params, grads, lr):

    params["W1"] -= lr * grads["dW1"]
    params["b1"] -= lr * grads["db1"]

    params["W2"] -= lr * grads["dW2"]
    params["b2"] -= lr * grads["db2"]

    params["W3"] -= lr * grads["dW3"]
    params["b3"] -= lr * grads["db3"]

    return params

def train(X, y, epochs=5000, lr=0.01):

    params = init_parameters()

    for epoch in range(epochs):

        # forward
        y_hat, cache = forward(X, params)

        # loss
        loss = compute_loss(y_hat, y)

        # backward
        grads = backward(X, y, y_hat, params, cache)

        # update
        params = update_parameters(params, grads, lr)

        if epoch % 500 == 0:
            print("Epoch:", epoch, "Loss:", loss)

    return params

def predict(X, params):

    y_hat, _ = forward(X, params)

    return y_hat

def test_model(params, path):

    X_test, y_test = load_data(path)

    y_pred = predict(X_test, params)

    loss = compute_loss(y_pred, y_test)

    print("Test Loss:", loss)

    return loss


X_train, y_train = load_data("train.csv")

params = train(X_train, y_train, epochs=5000, lr=0.01)

test_model(params, "test.csv")