from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)
            
    num_classes = W.shape[1]
    num_train = X.shape[0]
    loss = 0.0
    for i in range(num_train):
        scores = X[i].dot(W)
        score_sum = np.sum(np.exp(scores[:]))
        loss += np.log(score_sum) - scores[y[i]]
        for j in range(num_classes):
            if j!=y[i]:
                dW[:,j]+=X[i]*np.exp(scores[j])/score_sum
            else :
                dW[:,j]+=X[i]*(np.exp(scores[j])/score_sum -1)
    loss /= num_train
    dW /= num_train
    loss += 0.5 * reg * np.sum(W*W)
    dW += reg * W

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW



def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    num_classes = W.shape[1]
    num_train = X.shape[0]
    scores = X.dot(W)
    score_sum = np.sum(np.exp(scores[:,:]),axis=1).reshape(num_train,1)
    loss += np.sum(np.log(score_sum[:]))-np.sum(scores[np.arange(num_train), y])
    
    margin = np.exp(scores)
    margin /= score_sum
    margin[np.arange(num_train), y] -= 1
    dW = np.dot(X.T,margin)
    
    loss /= num_train
    dW /= num_train
    loss += 0.5 * reg * np.sum(W*W)
    dW += reg * W
    return loss, dW
