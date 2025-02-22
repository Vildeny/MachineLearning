#!/usr/bin/env python
# coding: utf-8

# <!-- HTML file automatically generated from DocOnce source (https://github.com/doconce/doconce/)
# doconce format html week41.do.txt --no_mako -->
# <!-- dom:TITLE: Week 41 Neural networks and constructing a neural network code -->

# # Week 41 Neural networks and constructing a neural network code
# **Morten Hjorth-Jensen**, Department of Physics, University of Oslo and Department of Physics and Astronomy and Facility for Rare Isotope Beams, Michigan State University
# 
# Date: **Week 41**

# ## Plan for week 41
# 
# **Material for the active learning sessions on Tuesday and Wednesday.**
# 
#   * Exercise on writing your own stochastic gradient and gradient descent codes. This exercise continues next week with studies of automatic differentiation
# 
#   * One lecture at the beginning of each session on the material from weeks 39 and 40 and how to write your own gradient descent code
# 
#   * Discussion of project 2
# 
#   * Your task before the sessions: revisit the material from weeks 39 and 40 and in particular the material from week 40 on stochastic gradient descent
# 
#   
# 
# **Material for the lecture on Thursday October 12, 2023.**
# 
#   * Neural Networks, setting up the basic steps, from the simple perceptron model to the multi-layer perceptron model.
# 
#   * Building our own Feed-forward Neural Network
# 
#   * [Video of lecture notes](https://youtu.be/5-RRTO9uDvI)
# 
#   * [Whiteboard notes](https://github.com/CompPhysics/MachineLearning/blob/master/doc/HandWrittenNotes/2023/NotesOct12.pdf)
# 
#   * Readings and Videos:
# 
#     * These lecture notes
# 
#     * For neural networks we recommend Goodfellow et al chapter 6.
# 
#     * [Neural Networks demystified](https://www.youtube.com/watch?v=bxe2T-V8XRs&list=PLiaHhY2iBX9hdHaRr6b7XevZtgZRa1PoU&ab_channel=WelchLabs)
# 
#     * [Building Neural Networks from scratch](https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&ab_channel=sentdex)
# 
#     * [Video on Neural Networks](https://www.youtube.com/watch?v=CqOfi41LfDw)
# 
#     * [Video on the back propagation algorithm](https://www.youtube.com/watch?v=Ilg3gGewQ5U)
# 
# I also  recommend Michael Nielsen's intuitive approach to the neural networks and the universal approximation theorem, see the slides at <http://neuralnetworksanddeeplearning.com/chap4.html>.

# ## Lecture Thursday October 12

# ## Introduction to Neural networks
# 
# Artificial neural networks are computational systems that can learn to
# perform tasks by considering examples, generally without being
# programmed with any task-specific rules. It is supposed to mimic a
# biological system, wherein neurons interact by sending signals in the
# form of mathematical functions between layers. All layers can contain
# an arbitrary number of neurons, and each connection is represented by
# a weight variable.

# ## Artificial neurons
# 
# The field of artificial neural networks has a long history of
# development, and is closely connected with the advancement of computer
# science and computers in general. A model of artificial neurons was
# first developed by McCulloch and Pitts in 1943 to study signal
# processing in the brain and has later been refined by others. The
# general idea is to mimic neural networks in the human brain, which is
# composed of billions of neurons that communicate with each other by
# sending electrical signals.  Each neuron accumulates its incoming
# signals, which must exceed an activation threshold to yield an
# output. If the threshold is not overcome, the neuron remains inactive,
# i.e. has zero output.
# 
# This behaviour has inspired a simple mathematical model for an artificial neuron.

# <!-- Equation labels as ordinary links -->
# <div id="artificialNeuron"></div>
# 
# $$
# \begin{equation}
#  y = f\left(\sum_{i=1}^n w_ix_i\right) = f(u)
# \label{artificialNeuron} \tag{1}
# \end{equation}
# $$

# Here, the output $y$ of the neuron is the value of its activation function, which have as input
# a weighted sum of signals $x_i, \dots ,x_n$ received by $n$ other neurons.
# 
# Conceptually, it is helpful to divide neural networks into four
# categories:
# 1. general purpose neural networks for supervised learning,
# 
# 2. neural networks designed specifically for image processing, the most prominent example of this class being Convolutional Neural Networks (CNNs),
# 
# 3. neural networks for sequential data such as Recurrent Neural Networks (RNNs), and
# 
# 4. neural networks for unsupervised learning such as Deep Boltzmann Machines.
# 
# In natural science, DNNs and CNNs have already found numerous
# applications. In statistical physics, they have been applied to detect
# phase transitions in 2D Ising and Potts models, lattice gauge
# theories, and different phases of polymers, or solving the
# Navier-Stokes equation in weather forecasting.  Deep learning has also
# found interesting applications in quantum physics. Various quantum
# phase transitions can be detected and studied using DNNs and CNNs,
# topological phases, and even non-equilibrium many-body
# localization. Representing quantum states as DNNs quantum state
# tomography are among some of the impressive achievements to reveal the
# potential of DNNs to facilitate the study of quantum systems.
# 
# In quantum information theory, it has been shown that one can perform
# gate decompositions with the help of neural. 
# 
# The applications are not limited to the natural sciences. There is a
# plethora of applications in essentially all disciplines, from the
# humanities to life science and medicine.

# ## Neural network types
# 
# An artificial neural network (ANN), is a computational model that
# consists of layers of connected neurons, or nodes or units.  We will
# refer to these interchangeably as units or nodes, and sometimes as
# neurons.
# 
# It is supposed to mimic a biological nervous system by letting each
# neuron interact with other neurons by sending signals in the form of
# mathematical functions between layers.  A wide variety of different
# ANNs have been developed, but most of them consist of an input layer,
# an output layer and eventual layers in-between, called *hidden
# layers*. All layers can contain an arbitrary number of nodes, and each
# connection between two nodes is associated with a weight variable.
# 
# Neural networks (also called neural nets) are neural-inspired
# nonlinear models for supervised learning.  As we will see, neural nets
# can be viewed as natural, more powerful extensions of supervised
# learning methods such as linear and logistic regression and soft-max
# methods we discussed earlier.

# ## Feed-forward neural networks
# 
# The feed-forward neural network (FFNN) was the first and simplest type
# of ANNs that were devised. In this network, the information moves in
# only one direction: forward through the layers.
# 
# Nodes are represented by circles, while the arrows display the
# connections between the nodes, including the direction of information
# flow. Additionally, each arrow corresponds to a weight variable
# (figure to come).  We observe that each node in a layer is connected
# to *all* nodes in the subsequent layer, making this a so-called
# *fully-connected* FFNN.

# ## Convolutional Neural Network
# 
# A different variant of FFNNs are *convolutional neural networks*
# (CNNs), which have a connectivity pattern inspired by the animal
# visual cortex. Individual neurons in the visual cortex only respond to
# stimuli from small sub-regions of the visual field, called a receptive
# field. This makes the neurons well-suited to exploit the strong
# spatially local correlation present in natural images. The response of
# each neuron can be approximated mathematically as a convolution
# operation.  (figure to come)
# 
# Convolutional neural networks emulate the behaviour of neurons in the
# visual cortex by enforcing a *local* connectivity pattern between
# nodes of adjacent layers: Each node in a convolutional layer is
# connected only to a subset of the nodes in the previous layer, in
# contrast to the fully-connected FFNN.  Often, CNNs consist of several
# convolutional layers that learn local features of the input, with a
# fully-connected layer at the end, which gathers all the local data and
# produces the outputs. They have wide applications in image and video
# recognition.

# ## Recurrent neural networks
# 
# So far we have only mentioned ANNs where information flows in one
# direction: forward. *Recurrent neural networks* on the other hand,
# have connections between nodes that form directed *cycles*. This
# creates a form of internal memory which are able to capture
# information on what has been calculated before; the output is
# dependent on the previous computations. Recurrent NNs make use of
# sequential information by performing the same task for every element
# in a sequence, where each element depends on previous elements. An
# example of such information is sentences, making recurrent NNs
# especially well-suited for handwriting and speech recognition.

# ## Other types of networks
# 
# There are many other kinds of ANNs that have been developed. One type
# that is specifically designed for interpolation in multidimensional
# space is the radial basis function (RBF) network. RBFs are typically
# made up of three layers: an input layer, a hidden layer with
# non-linear radial symmetric activation functions and a linear output
# layer (''linear'' here means that each node in the output layer has a
# linear activation function). The layers are normally fully-connected
# and there are no cycles, thus RBFs can be viewed as a type of
# fully-connected FFNN. They are however usually treated as a separate
# type of NN due the unusual activation functions.

# ## Multilayer perceptrons
# 
# One uses often so-called fully-connected feed-forward neural networks
# with three or more layers (an input layer, one or more hidden layers
# and an output layer) consisting of neurons that have non-linear
# activation functions.
# 
# Such networks are often called *multilayer perceptrons* (MLPs).

# ## Why multilayer perceptrons?
# 
# According to the *Universal approximation theorem*, a feed-forward
# neural network with just a single hidden layer containing a finite
# number of neurons can approximate a continuous multidimensional
# function to arbitrary accuracy, assuming the activation function for
# the hidden layer is a **non-constant, bounded and
# monotonically-increasing continuous function**.
# 
# Note that the requirements on the activation function only applies to
# the hidden layer, the output nodes are always assumed to be linear, so
# as to not restrict the range of output values.

# ## Illustration of a single perceptron model and a multi-perceptron model
# 
# <!-- dom:FIGURE: [figures/nns.png, width=600 frac=0.8]  In a) we show a single perceptron model while in b) we dispay a network with two  hidden layers, an input layer and an output layer. -->
# <!-- begin figure -->
# 
# <img src="figures/nns.png" width="600"><p style="font-size: 0.9em"><i>Figure 1: In a) we show a single perceptron model while in b) we dispay a network with two  hidden layers, an input layer and an output layer.</i></p>
# <!-- end figure -->

# ## Examples of XOR, OR and AND gates
# 
# Let us first try to fit various gates using standard linear
# regression. The gates we are thinking of are the classical XOR, OR and
# AND gates, well-known elements in computer science. The tables here
# show how we can set up the inputs $x_1$ and $x_2$ in order to yield a
# specific target $y_i$.

# In[1]:


"""
Simple code that tests XOR, OR and AND gates with linear regression
"""

import numpy as np
# Design matrix
X = np.array([ [1, 0, 0], [1, 0, 1], [1, 1, 0],[1, 1, 1]],dtype=np.float64)
print(f"The X.TX  matrix:{X.T @ X}")
Xinv = np.linalg.pinv(X.T @ X)
print(f"The invers of X.TX  matrix:{Xinv}")

# The XOR gate 
yXOR = np.array( [ 0, 1 ,1, 0])
ThetaXOR  = Xinv @ X.T @ yXOR
print(f"The values of theta for the XOR gate:{ThetaXOR}")
print(f"The linear regression prediction  for the XOR gate:{X @ ThetaXOR}")


# The OR gate 
yOR = np.array( [ 0, 1 ,1, 1])
ThetaOR  = Xinv @ X.T @ yOR
print(f"The values of theta for the OR gate:{ThetaOR}")
print(f"The linear regression prediction  for the OR gate:{X @ ThetaOR}")


# The OR gate 
yAND = np.array( [ 0, 0 ,0, 1])
ThetaAND  = Xinv @ X.T @ yAND
print(f"The values of theta for the AND gate:{ThetaAND}")
print(f"The linear regression prediction  for the AND gate:{X @ ThetaAND}")


# What is happening here?

# ## Does Logistic Regression do a better Job?

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')

"""
Simple code that tests XOR and OR gates with linear regression
and logistic regression
"""

import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import numpy as np

# Design matrix
X = np.array([ [1, 0, 0], [1, 0, 1], [1, 1, 0],[1, 1, 1]],dtype=np.float64)
print(f"The X.TX  matrix:{X.T @ X}")
Xinv = np.linalg.pinv(X.T @ X)
print(f"The invers of X.TX  matrix:{Xinv}")

# The XOR gate 
yXOR = np.array( [ 0, 1 ,1, 0])
ThetaXOR  = Xinv @ X.T @ yXOR
print(f"The values of theta for the XOR gate:{ThetaXOR}")
print(f"The linear regression prediction  for the XOR gate:{X @ ThetaXOR}")


# The OR gate 
yOR = np.array( [ 0, 1 ,1, 1])
ThetaOR  = Xinv @ X.T @ yOR
print(f"The values of theta for the OR gate:{ThetaOR}")
print(f"The linear regression prediction  for the OR gate:{X @ ThetaOR}")


# The OR gate 
yAND = np.array( [ 0, 0 ,0, 1])
ThetaAND  = Xinv @ X.T @ yAND
print(f"The values of theta for the AND gate:{ThetaAND}")
print(f"The linear regression prediction  for the AND gate:{X @ ThetaAND}")

# Now we change to logistic regression


# Logistic Regression
logreg = LogisticRegression()
logreg.fit(X, yOR)
print("Test set accuracy with Logistic Regression for OR gate: {:.2f}".format(logreg.score(X,yOR)))

logreg.fit(X, yXOR)
print("Test set accuracy with Logistic Regression for XOR gate: {:.2f}".format(logreg.score(X,yXOR)))


logreg.fit(X, yAND)
print("Test set accuracy with Logistic Regression for AND gate: {:.2f}".format(logreg.score(X,yAND)))


# Not exactly impressive, but somewhat better.

# ## Adding Neural Networks

# In[3]:



# and now neural networks with Scikit-Learn and the XOR

from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
X, yXOR = make_classification(n_samples=100, random_state=1)
FFNN = MLPClassifier(random_state=1, max_iter=300).fit(X, yXOR)
FFNN.predict_proba(X)
print(f"Test set accuracy with Feed Forward Neural Network  for XOR gate:{FFNN.score(X, yXOR)}")


# ## Mathematical model
# 
# The output $y$ is produced via the activation function $f$

# $$
# y = f\left(\sum_{i=1}^n w_ix_i + b_i\right) = f(z),
# $$

# This function receives $x_i$ as inputs.
# Here the activation $z=(\sum_{i=1}^n w_ix_i+b_i)$. 
# In an FFNN of such neurons, the *inputs* $x_i$ are the *outputs* of
# the neurons in the preceding layer. Furthermore, an MLP is
# fully-connected, which means that each neuron receives a weighted sum
# of the outputs of *all* neurons in the previous layer.

# ## Mathematical model
# 
# First, for each node $i$ in the first hidden layer, we calculate a weighted sum $z_i^1$ of the input coordinates $x_j$,

# <!-- Equation labels as ordinary links -->
# <div id="_auto1"></div>
# 
# $$
# \begin{equation} z_i^1 = \sum_{j=1}^{M} w_{ij}^1 x_j + b_i^1
# \label{_auto1} \tag{2}
# \end{equation}
# $$

# Here $b_i$ is the so-called bias which is normally needed in
# case of zero activation weights or inputs. How to fix the biases and
# the weights will be discussed below.  The value of $z_i^1$ is the
# argument to the activation function $f_i$ of each node $i$, The
# variable $M$ stands for all possible inputs to a given node $i$ in the
# first layer.  We define  the output $y_i^1$ of all neurons in layer 1 as

# <!-- Equation labels as ordinary links -->
# <div id="outputLayer1"></div>
# 
# $$
# \begin{equation}
#  y_i^1 = f(z_i^1) = f\left(\sum_{j=1}^M w_{ij}^1 x_j  + b_i^1\right)
# \label{outputLayer1} \tag{3}
# \end{equation}
# $$

# where we assume that all nodes in the same layer have identical
# activation functions, hence the notation $f$. In general, we could assume in the more general case that different layers have different activation functions.
# In this case we would identify these functions with a superscript $l$ for the $l$-th layer,

# <!-- Equation labels as ordinary links -->
# <div id="generalLayer"></div>
# 
# $$
# \begin{equation}
#  y_i^l = f^l(u_i^l) = f^l\left(\sum_{j=1}^{N_{l-1}} w_{ij}^l y_j^{l-1} + b_i^l\right)
# \label{generalLayer} \tag{4}
# \end{equation}
# $$

# where $N_l$ is the number of nodes in layer $l$. When the output of
# all the nodes in the first hidden layer are computed, the values of
# the subsequent layer can be calculated and so forth until the output
# is obtained.

# ## Mathematical model
# 
# The output of neuron $i$ in layer 2 is thus,

# <!-- Equation labels as ordinary links -->
# <div id="_auto2"></div>
# 
# $$
# \begin{equation}
#  y_i^2 = f^2\left(\sum_{j=1}^N w_{ij}^2 y_j^1 + b_i^2\right) 
# \label{_auto2} \tag{5}
# \end{equation}
# $$

# <!-- Equation labels as ordinary links -->
# <div id="outputLayer2"></div>
# 
# $$
# \begin{equation} 
#  = f^2\left[\sum_{j=1}^N w_{ij}^2f^1\left(\sum_{k=1}^M w_{jk}^1 x_k + b_j^1\right) + b_i^2\right]
# \label{outputLayer2} \tag{6}
# \end{equation}
# $$

# where we have substituted $y_k^1$ with the inputs $x_k$. Finally, the ANN output reads

# <!-- Equation labels as ordinary links -->
# <div id="_auto3"></div>
# 
# $$
# \begin{equation}
#  y_i^3 = f^3\left(\sum_{j=1}^N w_{ij}^3 y_j^2 + b_i^3\right) 
# \label{_auto3} \tag{7}
# \end{equation}
# $$

# <!-- Equation labels as ordinary links -->
# <div id="_auto4"></div>
# 
# $$
# \begin{equation} 
#  = f_3\left[\sum_{j} w_{ij}^3 f^2\left(\sum_{k} w_{jk}^2 f^1\left(\sum_{m} w_{km}^1 x_m + b_k^1\right) + b_j^2\right)
#   + b_1^3\right]
# \label{_auto4} \tag{8}
# \end{equation}
# $$

# ## Mathematical model
# 
# We can generalize this expression to an MLP with $l$ hidden
# layers. The complete functional form is,

# <!-- Equation labels as ordinary links -->
# <div id="completeNN"></div>
# 
# $$
# \begin{equation}
# y^{l+1}_i = f^{l+1}\left[\!\sum_{j=1}^{N_l} w_{ij}^3 f^l\left(\sum_{k=1}^{N_{l-1}}w_{jk}^{l-1}\left(\dots f^1\left(\sum_{n=1}^{N_0} w_{mn}^1 x_n+ b_m^1\right)\dots\right)+b_k^2\right)+b_1^3\right] 
# \label{completeNN} \tag{9}
# \end{equation}
# $$

# which illustrates a basic property of MLPs: The only independent
# variables are the input values $x_n$.

# ## Mathematical model
# 
# This confirms that an MLP, despite its quite convoluted mathematical
# form, is nothing more than an analytic function, specifically a
# mapping of real-valued vectors $\hat{x} \in \mathbb{R}^n \rightarrow
# \hat{y} \in \mathbb{R}^m$.
# 
# Furthermore, the flexibility and universality of an MLP can be
# illustrated by realizing that the expression is essentially a nested
# sum of scaled activation functions of the form

# <!-- Equation labels as ordinary links -->
# <div id="_auto5"></div>
# 
# $$
# \begin{equation}
#  f(x) = c_1 f(c_2 x + c_3) + c_4
# \label{_auto5} \tag{10}
# \end{equation}
# $$

# where the parameters $c_i$ are weights and biases. By adjusting these
# parameters, the activation functions can be shifted up and down or
# left and right, change slope or be rescaled which is the key to the
# flexibility of a neural network.

# ### Matrix-vector notation
# 
# We can introduce a more convenient notation for the activations in an A NN. 
# 
# Additionally, we can represent the biases and activations
# as layer-wise column vectors $\hat{b}_l$ and $\hat{y}_l$, so that the $i$-th element of each vector 
# is the bias $b_i^l$ and activation $y_i^l$ of node $i$ in layer $l$ respectively. 
# 
# We have that $\mathrm{W}_l$ is an $N_{l-1} \times N_l$ matrix, while $\hat{b}_l$ and $\hat{y}_l$ are $N_l \times 1$ column vectors. 
# With this notation, the sum becomes a matrix-vector multiplication, and we can write
# the equation for the activations of hidden layer 2 (assuming three nodes for simplicity) as

# <!-- Equation labels as ordinary links -->
# <div id="_auto6"></div>
# 
# $$
# \begin{equation}
#  \hat{y}_2 = f_2(\mathrm{W}_2 \hat{y}_{1} + \hat{b}_{2}) = 
#  f_2\left(\left[\begin{array}{ccc}
#     w^2_{11} &w^2_{12} &w^2_{13} \\
#     w^2_{21} &w^2_{22} &w^2_{23} \\
#     w^2_{31} &w^2_{32} &w^2_{33} \\
#     \end{array} \right] \cdot
#     \left[\begin{array}{c}
#            y^1_1 \\
#            y^1_2 \\
#            y^1_3 \\
#           \end{array}\right] + 
#     \left[\begin{array}{c}
#            b^2_1 \\
#            b^2_2 \\
#            b^2_3 \\
#           \end{array}\right]\right).
# \label{_auto6} \tag{11}
# \end{equation}
# $$

# ### Matrix-vector notation  and activation
# 
# The activation of node $i$ in layer 2 is

# <!-- Equation labels as ordinary links -->
# <div id="_auto7"></div>
# 
# $$
# \begin{equation}
#  y^2_i = f_2\Bigr(w^2_{i1}y^1_1 + w^2_{i2}y^1_2 + w^2_{i3}y^1_3 + b^2_i\Bigr) = 
#  f_2\left(\sum_{j=1}^3 w^2_{ij} y_j^1 + b^2_i\right).
# \label{_auto7} \tag{12}
# \end{equation}
# $$

# This is not just a convenient and compact notation, but also a useful
# and intuitive way to think about MLPs: The output is calculated by a
# series of matrix-vector multiplications and vector additions that are
# used as input to the activation functions. For each operation
# $\mathrm{W}_l \hat{y}_{l-1}$ we move forward one layer.

# ### Activation functions
# 
# A property that characterizes a neural network, other than its
# connectivity, is the choice of activation function(s).  As described
# in, the following restrictions are imposed on an activation function
# for a FFNN to fulfill the universal approximation theorem
# 
#   * Non-constant
# 
#   * Bounded
# 
#   * Monotonically-increasing
# 
#   * Continuous

# ### Activation functions, Logistic and Hyperbolic ones
# 
# The second requirement excludes all linear functions. Furthermore, in
# a MLP with only linear activation functions, each layer simply
# performs a linear transformation of its inputs.
# 
# Regardless of the number of layers, the output of the NN will be
# nothing but a linear function of the inputs. Thus we need to introduce
# some kind of non-linearity to the NN to be able to fit non-linear
# functions Typical examples are the logistic *Sigmoid*

# $$
# f(x) = \frac{1}{1 + e^{-x}},
# $$

# and the *hyperbolic tangent* function

# $$
# f(x) = \tanh(x)
# $$

# ### Relevance
# 
# The *sigmoid* function are more biologically plausible because the
# output of inactive neurons are zero. Such activation function are
# called *one-sided*. However, it has been shown that the hyperbolic
# tangent performs better than the sigmoid for training MLPs.  has
# become the most popular for *deep neural networks*

# In[4]:


"""The sigmoid function (or the logistic curve) is a 
function that takes any real number, z, and outputs a number (0,1).
It is useful in neural networks for assigning weights on a relative scale.
The value z is the weighted sum of parameters involved in the learning algorithm."""

import numpy
import matplotlib.pyplot as plt
import math as mt

z = numpy.arange(-5, 5, .1)
sigma_fn = numpy.vectorize(lambda z: 1/(1+numpy.exp(-z)))
sigma = sigma_fn(z)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(z, sigma)
ax.set_ylim([-0.1, 1.1])
ax.set_xlim([-5,5])
ax.grid(True)
ax.set_xlabel('z')
ax.set_title('sigmoid function')

plt.show()

"""Step Function"""
z = numpy.arange(-5, 5, .02)
step_fn = numpy.vectorize(lambda z: 1.0 if z >= 0.0 else 0.0)
step = step_fn(z)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(z, step)
ax.set_ylim([-0.5, 1.5])
ax.set_xlim([-5,5])
ax.grid(True)
ax.set_xlabel('z')
ax.set_title('step function')

plt.show()

"""Sine Function"""
z = numpy.arange(-2*mt.pi, 2*mt.pi, 0.1)
t = numpy.sin(z)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(z, t)
ax.set_ylim([-1.0, 1.0])
ax.set_xlim([-2*mt.pi,2*mt.pi])
ax.grid(True)
ax.set_xlabel('z')
ax.set_title('sine function')

plt.show()

"""Plots a graph of the squashing function used by a rectified linear
unit"""
z = numpy.arange(-2, 2, .1)
zero = numpy.zeros(len(z))
y = numpy.max([zero, z], axis=0)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(z, y)
ax.set_ylim([-2.0, 2.0])
ax.set_xlim([-2.0, 2.0])
ax.grid(True)
ax.set_xlabel('z')
ax.set_title('Rectified linear unit')

plt.show()


# ## The multilayer  perceptron (MLP)
# 
# The multilayer perceptron is a very popular, and easy to implement approach, to deep learning. It consists of
# 1. A neural network with one or more layers of nodes between the input and the output nodes.
# 
# 2. The multilayer network structure, or architecture, or topology, consists of an input layer, one or more hidden layers, and one output layer.
# 
# 3. The input nodes pass values to the first hidden layer, its nodes pass the information on to the second and so on till we reach the output layer.
# 
# As a convention it is normal to call  a  network with one layer of input units, one layer of hidden
# units and one layer of output units as  a two-layer network. A network with two layers of hidden units is called a three-layer network etc etc.
# 
# For an MLP network there is no direct connection between the output nodes/neurons/units and  the input nodes/neurons/units.
# Hereafter we will call the various entities of a layer for nodes.
# There are also no connections within a single layer.
# 
# The number of input nodes does not need to equal the number of output
# nodes. This applies also to the hidden layers. Each layer may have its
# own number of nodes and activation functions.
# 
# The hidden layers have their name from the fact that they are not
# linked to observables and as we will see below when we define the
# so-called activation $\hat{z}$, we can think of this as a basis
# expansion of the original inputs $\hat{x}$. The difference however
# between neural networks and say linear regression is that now these
# basis functions (which will correspond to the weights in the network)
# are learned from data. This results in  an important difference between
# neural networks and deep learning approaches on one side and methods
# like logistic regression or linear regression and their modifications on the other side.

# ## From one to many layers, the universal approximation theorem
# 
# A neural network with only one layer, what we called the simple
# perceptron, is best suited if we have a standard binary model with
# clear (linear) boundaries between the outcomes. As such it could
# equally well be replaced by standard linear regression or logistic
# regression. Networks with one or more hidden layers approximate
# systems with more complex boundaries.
# 
# As stated earlier, 
# an important theorem in studies of neural networks, restated without
# proof here, is the [universal approximation
# theorem](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.441.7873&rep=rep1&type=pdf).
# 
# It states that a feed-forward network with a single hidden layer
# containing a finite number of neurons can approximate continuous
# functions on compact subsets of real functions. The theorem thus
# states that simple neural networks can represent a wide variety of
# interesting functions when given appropriate parameters. It is the
# multilayer feedforward architecture itself which gives neural networks
# the potential of being universal approximators.

# ## Deriving the back propagation code for a multilayer perceptron model
# 
# As we have seen now in a feed forward network, we can express the final output of our network in terms of basic matrix-vector multiplications.
# The unknowwn quantities are our weights $w_{ij}$ and we need to find an algorithm for changing them so that our errors are as small as possible.
# This leads us to the famous [back propagation algorithm](https://www.nature.com/articles/323533a0).
# 
# The questions we want to ask are how do changes in the biases and the
# weights in our network change the cost function and how can we use the
# final output to modify the weights?
# 
# To derive these equations let us start with a plain regression problem
# and define our cost function as

# $$
# {\cal C}(\hat{W})  =  \frac{1}{2}\sum_{i=1}^n\left(y_i - t_i\right)^2,
# $$

# where the $t_i$s are our $n$ targets (the values we want to
# reproduce), while the outputs of the network after having propagated
# all inputs $\hat{x}$ are given by $y_i$.  Below we will demonstrate
# how the basic equations arising from the back propagation algorithm
# can be modified in order to study classification problems with $K$
# classes.

# ## Definitions
# 
# With our definition of the targets $\hat{t}$, the outputs of the
# network $\hat{y}$ and the inputs $\hat{x}$ we
# define now the activation $z_j^l$ of node/neuron/unit $j$ of the
# $l$-th layer as a function of the bias, the weights which add up from
# the previous layer $l-1$ and the forward passes/outputs
# $\hat{a}^{l-1}$ from the previous layer as

# $$
# z_j^l = \sum_{i=1}^{M_{l-1}}w_{ij}^la_i^{l-1}+b_j^l,
# $$

# where $b_k^l$ are the biases from layer $l$.  Here $M_{l-1}$
# represents the total number of nodes/neurons/units of layer $l-1$. The
# figure here illustrates this equation.  We can rewrite this in a more
# compact form as the matrix-vector products we discussed earlier,

# $$
# \hat{z}^l = \left(\hat{W}^l\right)^T\hat{a}^{l-1}+\hat{b}^l.
# $$

# With the activation values $\hat{z}^l$ we can in turn define the
# output of layer $l$ as $\hat{a}^l = f(\hat{z}^l)$ where $f$ is our
# activation function. In the examples here we will use the sigmoid
# function discussed in our logistic regression lectures. We will also use the same activation function $f$ for all layers
# and their nodes.  It means we have

# $$
# a_j^l = f(z_j^l) = \frac{1}{1+\exp{-(z_j^l)}}.
# $$

# ## Derivatives and the chain rule
# 
# From the definition of the activation $z_j^l$ we have

# $$
# \frac{\partial z_j^l}{\partial w_{ij}^l} = a_i^{l-1},
# $$

# and

# $$
# \frac{\partial z_j^l}{\partial a_i^{l-1}} = w_{ji}^l.
# $$

# With our definition of the activation function we have that (note that this function depends only on $z_j^l$)

# $$
# \frac{\partial a_j^l}{\partial z_j^{l}} = a_j^l(1-a_j^l)=f(z_j^l)(1-f(z_j^l)).
# $$

# ## Derivative of the cost function
# 
# With these definitions we can now compute the derivative of the cost function in terms of the weights.
# 
# Let us specialize to the output layer $l=L$. Our cost function is

# $$
# {\cal C}(\hat{W^L})  =  \frac{1}{2}\sum_{i=1}^n\left(y_i - t_i\right)^2=\frac{1}{2}\sum_{i=1}^n\left(a_i^L - t_i\right)^2,
# $$

# The derivative of this function with respect to the weights is

# $$
# \frac{\partial{\cal C}(\hat{W^L})}{\partial w_{jk}^L}  =  \left(a_j^L - t_j\right)\frac{\partial a_j^L}{\partial w_{jk}^{L}},
# $$

# The last partial derivative can easily be computed and reads (by applying the chain rule)

# $$
# \frac{\partial a_j^L}{\partial w_{jk}^{L}} = \frac{\partial a_j^L}{\partial z_{j}^{L}}\frac{\partial z_j^L}{\partial w_{jk}^{L}}=a_j^L(1-a_j^L)a_k^{L-1},
# $$

# ## Bringing it together, first back propagation equation
# 
# We have thus

# $$
# \frac{\partial{\cal C}(\hat{W^L})}{\partial w_{jk}^L}  =  \left(a_j^L - t_j\right)a_j^L(1-a_j^L)a_k^{L-1},
# $$

# Defining

# $$
# \delta_j^L = a_j^L(1-a_j^L)\left(a_j^L - t_j\right) = f'(z_j^L)\frac{\partial {\cal C}}{\partial (a_j^L)},
# $$

# and using the Hadamard product of two vectors we can write this as

# $$
# \hat{\delta}^L = f'(\hat{z}^L)\circ\frac{\partial {\cal C}}{\partial (\hat{a}^L)}.
# $$

# This is an important expression. The second term on the right handside
# measures how fast the cost function is changing as a function of the $j$th
# output activation.  If, for example, the cost function doesn't depend
# much on a particular output node $j$, then $\delta_j^L$ will be small,
# which is what we would expect. The first term on the right, measures
# how fast the activation function $f$ is changing at a given activation
# value $z_j^L$.
# 
# Notice that everything in the above equations is easily computed.  In
# particular, we compute $z_j^L$ while computing the behaviour of the
# network, and it is only a small additional overhead to compute
# $f'(z^L_j)$.  The exact form of the derivative with respect to the
# output depends on the form of the cost function.
# However, provided the cost function is known there should be little
# trouble in calculating

# $$
# \frac{\partial {\cal C}}{\partial (a_j^L)}
# $$

# With the definition of $\delta_j^L$ we have a more compact definition of the derivative of the cost function in terms of the weights, namely

# $$
# \frac{\partial{\cal C}(\hat{W^L})}{\partial w_{jk}^L}  =  \delta_j^La_k^{L-1}.
# $$

# ## Derivatives in terms of $z_j^L$
# 
# It is also easy to see that our previous equation can be written as

# $$
# \delta_j^L =\frac{\partial {\cal C}}{\partial z_j^L}= \frac{\partial {\cal C}}{\partial a_j^L}\frac{\partial a_j^L}{\partial z_j^L},
# $$

# which can also be interpreted as the partial derivative of the cost function with respect to the biases $b_j^L$, namely

# $$
# \delta_j^L = \frac{\partial {\cal C}}{\partial b_j^L}\frac{\partial b_j^L}{\partial z_j^L}=\frac{\partial {\cal C}}{\partial b_j^L},
# $$

# That is, the error $\delta_j^L$ is exactly equal to the rate of change of the cost function as a function of the bias.

# ## Bringing it together
# 
# We have now three equations that are essential for the computations of the derivatives of the cost function at the output layer. These equations are needed to start the algorithm and they are
# 
# **The starting equations.**

# <!-- Equation labels as ordinary links -->
# <div id="_auto8"></div>
# 
# $$
# \begin{equation}
# \frac{\partial{\cal C}(\hat{W^L})}{\partial w_{jk}^L}  =  \delta_j^La_k^{L-1},
# \label{_auto8} \tag{13}
# \end{equation}
# $$

# and

# <!-- Equation labels as ordinary links -->
# <div id="_auto9"></div>
# 
# $$
# \begin{equation}
# \delta_j^L = f'(z_j^L)\frac{\partial {\cal C}}{\partial (a_j^L)},
# \label{_auto9} \tag{14}
# \end{equation}
# $$

# and

# <!-- Equation labels as ordinary links -->
# <div id="_auto10"></div>
# 
# $$
# \begin{equation}
# \delta_j^L = \frac{\partial {\cal C}}{\partial b_j^L},
# \label{_auto10} \tag{15}
# \end{equation}
# $$

# An interesting consequence of the above equations is that when the
# activation $a_k^{L-1}$ is small, the gradient term, that is the
# derivative of the cost function with respect to the weights, will also
# tend to be small. We say then that the weight learns slowly, meaning
# that it changes slowly when we minimize the weights via say gradient
# descent. In this case we say the system learns slowly.
# 
# Another interesting feature is that is when the activation function,
# represented by the sigmoid function here, is rather flat when we move towards
# its end values $0$ and $1$ (see the above Python codes). In these
# cases, the derivatives of the activation function will also be close
# to zero, meaning again that the gradients will be small and the
# network learns slowly again.
# 
# We need a fourth equation and we are set. We are going to propagate
# backwards in order to the determine the weights and biases. In order
# to do so we need to represent the error in the layer before the final
# one $L-1$ in terms of the errors in the final output layer.

# ## Final back propagating equation
# 
# We have that (replacing $L$ with a general layer $l$)

# $$
# \delta_j^l =\frac{\partial {\cal C}}{\partial z_j^l}.
# $$

# We want to express this in terms of the equations for layer $l+1$. Using the chain rule and summing over all $k$ entries we have

# $$
# \delta_j^l =\sum_k \frac{\partial {\cal C}}{\partial z_k^{l+1}}\frac{\partial z_k^{l+1}}{\partial z_j^{l}}=\sum_k \delta_k^{l+1}\frac{\partial z_k^{l+1}}{\partial z_j^{l}},
# $$

# and recalling that

# $$
# z_j^{l+1} = \sum_{i=1}^{M_{l}}w_{ij}^{l+1}a_i^{l}+b_j^{l+1},
# $$

# with $M_l$ being the number of nodes in layer $l$, we obtain

# $$
# \delta_j^l =\sum_k \delta_k^{l+1}w_{kj}^{l+1}f'(z_j^l),
# $$

# This is our final equation.
# 
# We are now ready to set up the algorithm for back propagation and learning the weights and biases.

# ## Setting up the Back propagation algorithm
# 
# The four equations  provide us with a way of computing the gradient of the cost function. Let us write this out in the form of an algorithm.
# 
# First, we set up the input data $\hat{x}$ and the activations
# $\hat{z}_1$ of the input layer and compute the activation function and
# the pertinent outputs $\hat{a}^1$.
# 
# Secondly, we perform then the feed forward till we reach the output
# layer and compute all $\hat{z}_l$ of the input layer and compute the
# activation function and the pertinent outputs $\hat{a}^l$ for
# $l=2,3,\dots,L$.
# 
# Thereafter we compute the ouput error $\hat{\delta}^L$ by computing all

# $$
# \delta_j^L = f'(z_j^L)\frac{\partial {\cal C}}{\partial (a_j^L)}.
# $$

# Then we compute the back propagate error for each $l=L-1,L-2,\dots,2$ as

# $$
# \delta_j^l = \sum_k \delta_k^{l+1}w_{kj}^{l+1}f'(z_j^l).
# $$

# Finally, we update the weights and the biases using gradient descent for each $l=L-1,L-2,\dots,2$ and update the weights and biases according to the rules

# $$
# w_{jk}^l\leftarrow  = w_{jk}^l- \eta \delta_j^la_k^{l-1},
# $$

# $$
# b_j^l \leftarrow b_j^l-\eta \frac{\partial {\cal C}}{\partial b_j^l}=b_j^l-\eta \delta_j^l,
# $$

# The parameter $\eta$ is the learning parameter discussed in connection with the gradient descent methods.
# Here it is convenient to use stochastic gradient descent (see the examples below) with mini-batches with an outer loop that steps through multiple epochs of training.

# ## Setting up the Back propagation algorithm
# 
# The four equations  above  provide us with a way of computing the gradient of the cost function. Let us write this out in the form of an algorithm.
# 
# First, we set up the input data $\boldsymbol{x}$ and the activations
# $\boldsymbol{z}_1$ of the input layer and compute the activation function and
# the pertinent outputs $\boldsymbol{a}^1$.
# 
# Secondly, we perform then the feed forward till we reach the output
# layer and compute all $\boldsymbol{z}_l$ of the input layer and compute the
# activation function and the pertinent outputs $\boldsymbol{a}^l$ for
# $l=2,3,\dots,L$.
# 
# Thereafter we compute the ouput error $\boldsymbol{\delta}^L$ by computing all

# $$
# \delta_j^L = f'(z_j^L)\frac{\partial {\cal C}}{\partial (a_j^L)}.
# $$

# Then we compute the back propagate error for each $l=L-1,L-2,\dots,2$ as

# $$
# \delta_j^l = \sum_k \delta_k^{l+1}w_{kj}^{l+1}f'(z_j^l).
# $$

# Finally, we update the weights and the biases using gradient descent for each $l=L-1,L-2,\dots,2$ and update the weights and biases according to the rules

# $$
# w_{jk}^l\leftarrow  = w_{jk}^l- \eta \delta_j^la_k^{l-1},
# $$

# $$
# b_j^l \leftarrow b_j^l-\eta \frac{\partial {\cal C}}{\partial b_j^l}=b_j^l-\eta \delta_j^l,
# $$

# The parameter $\eta$ is the learning parameter discussed in connection with the gradient descent methods.
# Here it is convenient to use stochastic gradient descent (see the examples below) with mini-batches with an outer loop that steps through multiple epochs of training.

# ## Setting up the Back propagation algorithm
# 
# The four equations  derived discussed above provide us with a way of computing the gradient of the cost function. Let us write this out in the form of an algorithm.
# 
# First, we set up the input data $\boldsymbol{x}$ and the activations
# $\boldsymbol{z}_1$ of the input layer and compute the activation function and
# the pertinent outputs $\boldsymbol{a}^1$.
# 
# Secondly, we perform then the feed forward till we reach the output
# layer and compute all $\boldsymbol{z}_l$ of the input layer and compute the
# activation function and the pertinent outputs $\boldsymbol{a}^l$ for
# $l=2,3,\dots,L$.
# 
# Thereafter we compute the ouput error $\boldsymbol{\delta}^L$ by computing all

# $$
# \delta_j^L = f'(z_j^L)\frac{\partial {\cal C}}{\partial (a_j^L)}.
# $$

# Then we compute the back propagate error for each $l=L-1,L-2,\dots,2$ as

# $$
# \delta_j^l = \sum_k \delta_k^{l+1}w_{kj}^{l+1}f'(z_j^l).
# $$

# Finally, we update the weights and the biases using gradient descent for each $l=L-1,L-2,\dots,2$ and update the weights and biases according to the rules

# $$
# w_{jk}^l\leftarrow  = w_{jk}^l- \eta \delta_j^la_k^{l-1},
# $$

# $$
# b_j^l \leftarrow b_j^l-\eta \frac{\partial {\cal C}}{\partial b_j^l}=b_j^l-\eta \delta_j^l,
# $$

# The parameter $\eta$ is the learning parameter discussed in connection with the gradient descent methods.
# Here it is convenient to use stochastic gradient descent (see the examples below) with mini-batches with an outer loop that steps through multiple epochs of training.

# ## Setting up a Multi-layer perceptron model for classification
# 
# We are now gong to develop an example based on the MNIST data
# base. This is a classification problem and we need to use our
# cross-entropy function we discussed in connection with logistic
# regression. The cross-entropy defines our cost function for the
# classificaton problems with neural networks.
# 
# In binary classification with two classes $(0, 1)$ we define the
# logistic/sigmoid function as the probability that a particular input
# is in class $0$ or $1$.  This is possible because the logistic
# function takes any input from the real numbers and inputs a number
# between 0 and 1, and can therefore be interpreted as a probability. It
# also has other nice properties, such as a derivative that is simple to
# calculate.
# 
# For an input $\boldsymbol{a}$ from the hidden layer, the probability that the input $\boldsymbol{x}$
# is in class 0 or 1 is just. We let $\theta$ represent the unknown weights and biases to be adjusted by our equations). The variable $x$
# represents our activation values $z$. We have

# $$
# P(y = 0 \mid \boldsymbol{x}, \boldsymbol{\theta}) = \frac{1}{1 + \exp{(- \boldsymbol{x}})} ,
# $$

# and

# $$
# P(y = 1 \mid \boldsymbol{x}, \boldsymbol{\theta}) = 1 - P(y = 0 \mid \boldsymbol{x}, \boldsymbol{\theta}) ,
# $$

# where $y \in \{0, 1\}$  and $\boldsymbol{\theta}$ represents the weights and biases
# of our network.

# ## Defining the cost function
# 
# Our cost function is given as (see the Logistic regression lectures)

# $$
# \mathcal{C}(\boldsymbol{\theta}) = - \ln P(\mathcal{D} \mid \boldsymbol{\theta}) = - \sum_{i=1}^n
# y_i \ln[P(y_i = 0)] + (1 - y_i) \ln [1 - P(y_i = 0)] = \sum_{i=1}^n \mathcal{L}_i(\boldsymbol{\theta}) .
# $$

# This last equality means that we can interpret our *cost* function as a sum over the *loss* function
# for each point in the dataset $\mathcal{L}_i(\boldsymbol{\theta})$.  
# The negative sign is just so that we can think about our algorithm as minimizing a positive number, rather
# than maximizing a negative number.  
# 
# In *multiclass* classification it is common to treat each integer label as a so called *one-hot* vector:  
# 
# $y = 5 \quad \rightarrow \quad \boldsymbol{y} = (0, 0, 0, 0, 0, 1, 0, 0, 0, 0) ,$ and
# 
# $y = 1 \quad \rightarrow \quad \boldsymbol{y} = (0, 1, 0, 0, 0, 0, 0, 0, 0, 0) ,$ 
# 
# i.e. a binary bit string of length $C$, where $C = 10$ is the number of classes in the MNIST dataset (numbers from $0$ to $9$)..  
# 
# If $\boldsymbol{x}_i$ is the $i$-th input (image), $y_{ic}$ refers to the $c$-th component of the $i$-th
# output vector $\boldsymbol{y}_i$.  
# The probability of $\boldsymbol{x}_i$ being in class $c$ will be given by the softmax function:

# $$
# P(y_{ic} = 1 \mid \boldsymbol{x}_i, \boldsymbol{\theta}) = \frac{\exp{((\boldsymbol{a}_i^{hidden})^T \boldsymbol{w}_c)}}
# {\sum_{c'=0}^{C-1} \exp{((\boldsymbol{a}_i^{hidden})^T \boldsymbol{w}_{c'})}} ,
# $$

# which reduces to the logistic function in the binary case.  
# The likelihood of this $C$-class classifier
# is now given as:

# $$
# P(\mathcal{D} \mid \boldsymbol{\theta}) = \prod_{i=1}^n \prod_{c=0}^{C-1} [P(y_{ic} = 1)]^{y_{ic}} .
# $$

# Again we take the negative log-likelihood to define our cost function:

# $$
# \mathcal{C}(\boldsymbol{\theta}) = - \log{P(\mathcal{D} \mid \boldsymbol{\theta})}.
# $$

# See the logistic regression lectures for a full definition of the cost function.
# 
# The back propagation equations need now only a small change, namely the definition of a new cost function. We are thus ready to use the same equations as before!

# ## Example: binary classification problem
# 
# As an example of the above, relevant for project 2 as well, let us consider a binary class. As discussed in our logistic regression lectures, we defined a cost function in terms of the parameters $\beta$ as

# $$
# \mathcal{C}(\boldsymbol{\beta}) = - \sum_{i=1}^n \left(y_i\log{p(y_i \vert x_i,\boldsymbol{\beta})}+(1-y_i)\log{1-p(y_i \vert x_i,\boldsymbol{\beta})}\right),
# $$

# where we had defined the logistic (sigmoid) function

# $$
# p(y_i =1\vert x_i,\boldsymbol{\beta})=\frac{\exp{(\beta_0+\beta_1 x_i)}}{1+\exp{(\beta_0+\beta_1 x_i)}},
# $$

# and

# $$
# p(y_i =0\vert x_i,\boldsymbol{\beta})=1-p(y_i =1\vert x_i,\boldsymbol{\beta}).
# $$

# The parameters $\boldsymbol{\beta}$ were defined using a minimization method like gradient descent or Newton-Raphson's method. 
# 
# Now we replace $x_i$ with the activation $z_i^l$ for a given layer $l$ and the outputs as $y_i=a_i^l=f(z_i^l)$, with $z_i^l$ now being a function of the weights $w_{ij}^l$ and biases $b_i^l$. 
# We have then

# $$
# a_i^l = y_i = \frac{\exp{(z_i^l)}}{1+\exp{(z_i^l)}},
# $$

# with

# $$
# z_i^l = \sum_{j}w_{ij}^l a_j^{l-1}+b_i^l,
# $$

# where the superscript $l-1$ indicates that these are the outputs from layer $l-1$.
# Our cost function at the final layer $l=L$ is now

# $$
# \mathcal{C}(\boldsymbol{W}) = - \sum_{i=1}^n \left(t_i\log{a_i^L}+(1-t_i)\log{(1-a_i^L)}\right),
# $$

# where we have defined the targets $t_i$. The derivatives of the cost function with respect to the output $a_i^L$ are then easily calculated and we get

# $$
# \frac{\partial \mathcal{C}(\boldsymbol{W})}{\partial a_i^L} = \frac{a_i^L-t_i}{a_i^L(1-a_i^L)}.
# $$

# In case we use another activation function than the logistic one, we need to evaluate other derivatives.

# ## The Softmax function
# In case we employ the more general case given by the Softmax equation, we need to evaluate the derivative of the activation function with respect to the activation $z_i^l$, that is we need

# $$
# \frac{\partial f(z_i^l)}{\partial w_{jk}^l} =
# \frac{\partial f(z_i^l)}{\partial z_j^l} \frac{\partial z_j^l}{\partial w_{jk}^l}= \frac{\partial f(z_i^l)}{\partial z_j^l}a_k^{l-1}.
# $$

# For the Softmax function we have

# $$
# f(z_i^l) = \frac{\exp{(z_i^l)}}{\sum_{m=1}^K\exp{(z_m^l)}}.
# $$

# Its derivative with respect to $z_j^l$ gives

# $$
# \frac{\partial f(z_i^l)}{\partial z_j^l}= f(z_i^l)\left(\delta_{ij}-f(z_j^l)\right),
# $$

# which in case of the simply binary model reduces to  having $i=j$.

# ## Developing a code for doing neural networks with back propagation
# 
# One can identify a set of key steps when using neural networks to solve supervised learning problems:  
# 
# 1. Collect and pre-process data  
# 
# 2. Define model and architecture  
# 
# 3. Choose cost function and optimizer  
# 
# 4. Train the model  
# 
# 5. Evaluate model performance on test data  
# 
# 6. Adjust hyperparameters (if necessary, network architecture)

# ## Collect and pre-process data
# 
# Here we will be using the MNIST dataset, which is readily available through the **scikit-learn**
# package. You may also find it for example [here](http://yann.lecun.com/exdb/mnist/).  
# The *MNIST* (Modified National Institute of Standards and Technology) database is a large database
# of handwritten digits that is commonly used for training various image processing systems.  
# The MNIST dataset consists of 70 000 images of size $28\times 28$ pixels, each labeled from 0 to 9.  
# The scikit-learn dataset we will use consists of a selection of 1797 images of size $8\times 8$ collected and processed from this database.  
# 
# To feed data into a feed-forward neural network we need to represent
# the inputs as a design/feature matrix $X = (n_{inputs}, n_{features})$.  Each
# row represents an *input*, in this case a handwritten digit, and
# each column represents a *feature*, in this case a pixel.  The
# correct answers, also known as *labels* or *targets* are
# represented as a 1D array of integers 
# $Y = (n_{inputs}) = (5, 3, 1, 8,...)$.
# 
# As an example, say we want to build a neural network using supervised learning to predict Body-Mass Index (BMI) from
# measurements of height (in m)  
# and weight (in kg). If we have measurements of 5 people the design/feature matrix could be for example:  
# 
# $$ X = \begin{bmatrix}
# 1.85 & 81\\
# 1.71 & 65\\
# 1.95 & 103\\
# 1.55 & 42\\
# 1.63 & 56
# \end{bmatrix} ,$$  
# 
# and the targets would be:  
# 
# $$ Y = (23.7, 22.2, 27.1, 17.5, 21.1) $$  
# 
# Since each input image is a 2D matrix, we need to flatten the image
# (i.e. "unravel" the 2D matrix into a 1D array) to turn the data into a
# design/feature matrix. This means we lose all spatial information in the
# image, such as locality and translational invariance. More complicated
# architectures such as Convolutional Neural Networks can take advantage
# of such information, and are most commonly applied when analyzing
# images.

# In[5]:


# import necessary packages
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets


# ensure the same random numbers appear every time
np.random.seed(0)

# display images in notebook
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = (12,12)


# download MNIST dataset
digits = datasets.load_digits()

# define inputs and labels
inputs = digits.images
labels = digits.target

print("inputs = (n_inputs, pixel_width, pixel_height) = " + str(inputs.shape))
print("labels = (n_inputs) = " + str(labels.shape))


# flatten the image
# the value -1 means dimension is inferred from the remaining dimensions: 8x8 = 64
n_inputs = len(inputs)
inputs = inputs.reshape(n_inputs, -1)
print("X = (n_inputs, n_features) = " + str(inputs.shape))


# choose some random images to display
indices = np.arange(n_inputs)
random_indices = np.random.choice(indices, size=5)

for i, image in enumerate(digits.images[random_indices]):
    plt.subplot(1, 5, i+1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title("Label: %d" % digits.target[random_indices[i]])
plt.show()


# ## Train and test datasets
# 
# Performing analysis before partitioning the dataset is a major error, that can lead to incorrect conclusions.  
# 
# We will reserve $80 \%$ of our dataset for training and $20 \%$ for testing.  
# 
# It is important that the train and test datasets are drawn randomly from our dataset, to ensure
# no bias in the sampling.  
# Say you are taking measurements of weather data to predict the weather in the coming 5 days.
# You don't want to train your model on measurements taken from the hours 00.00 to 12.00, and then test it on data
# collected from 12.00 to 24.00.

# In[6]:


from sklearn.model_selection import train_test_split

# one-liner from scikit-learn library
train_size = 0.8
test_size = 1 - train_size
X_train, X_test, Y_train, Y_test = train_test_split(inputs, labels, train_size=train_size,
                                                    test_size=test_size)

# equivalently in numpy
def train_test_split_numpy(inputs, labels, train_size, test_size):
    n_inputs = len(inputs)
    inputs_shuffled = inputs.copy()
    labels_shuffled = labels.copy()
    
    np.random.shuffle(inputs_shuffled)
    np.random.shuffle(labels_shuffled)
    
    train_end = int(n_inputs*train_size)
    X_train, X_test = inputs_shuffled[:train_end], inputs_shuffled[train_end:]
    Y_train, Y_test = labels_shuffled[:train_end], labels_shuffled[train_end:]
    
    return X_train, X_test, Y_train, Y_test

#X_train, X_test, Y_train, Y_test = train_test_split_numpy(inputs, labels, train_size, test_size)

print("Number of training images: " + str(len(X_train)))
print("Number of test images: " + str(len(X_test)))


# ## Define model and architecture
# 
# Our simple feed-forward neural network will consist of an *input* layer, a single *hidden* layer and an *output* layer. The activation $y$ of each neuron is a weighted sum of inputs, passed through an activation function. In case of the simple perceptron model we have 
# 
# $$ z = \sum_{i=1}^n w_i a_i ,$$
# 
# $$ y = f(z) ,$$
# 
# where $f$ is the activation function, $a_i$ represents input from neuron $i$ in the preceding layer
# and $w_i$ is the weight to input $i$.  
# The activation of the neurons in the input layer is just the features (e.g. a pixel value).  
# 
# The simplest activation function for a neuron is the *Heaviside* function:
# 
# $$ f(z) = 
# \begin{cases}
# 1,  &  z > 0\\
# 0,  & \text{otherwise}
# \end{cases}
# $$
# 
# A feed-forward neural network with this activation is known as a *perceptron*.  
# For a binary classifier (i.e. two classes, 0 or 1, dog or not-dog) we can also use this in our output layer.  
# This activation can be generalized to $k$ classes (using e.g. the *one-against-all* strategy), 
# and we call these architectures *multiclass perceptrons*.  
# 
# However, it is now common to use the terms Single Layer Perceptron (SLP) (1 hidden layer) and  
# Multilayer Perceptron (MLP) (2 or more hidden layers) to refer to feed-forward neural networks with any activation function.  
# 
# Typical choices for activation functions include the sigmoid function, hyperbolic tangent, and Rectified Linear Unit (ReLU).  
# We will be using the sigmoid function $\sigma(x)$:  
# 
# $$ f(x) = \sigma(x) = \frac{1}{1 + e^{-x}} ,$$
# 
# which is inspired by probability theory (see logistic regression) and was most commonly used until about 2011. See the discussion below concerning other activation functions.

# ## Layers
# 
# * Input 
# 
# Since each input image has 8x8 = 64 pixels or features, we have an input layer of 64 neurons.  
# 
# * Hidden layer
# 
# We will use 50 neurons in the hidden layer receiving input from the neurons in the input layer.  
# Since each neuron in the hidden layer is connected to the 64 inputs we have 64x50 = 3200 weights to the hidden layer.  
# 
# * Output
# 
# If we were building a binary classifier, it would be sufficient with a single neuron in the output layer,
# which could output 0 or 1 according to the Heaviside function. This would be an example of a *hard* classifier, meaning it outputs the class of the input directly. However, if we are dealing with noisy data it is often beneficial to use a *soft* classifier, which outputs the probability of being in class 0 or 1.  
# 
# For a soft binary classifier, we could use a single neuron and interpret the output as either being the probability of being in class 0 or the probability of being in class 1. Alternatively we could use 2 neurons, and interpret each neuron as the probability of being in each class.  
# 
# Since we are doing multiclass classification, with 10 categories, it is natural to use 10 neurons in the output layer. We number the neurons $j = 0,1,...,9$. The activation of each output neuron $j$ will be according to the *softmax* function:  
# 
# $$ P(\text{class $j$} \mid \text{input $\boldsymbol{a}$}) = \frac{\exp{(\boldsymbol{a}^T \boldsymbol{w}_j)}}
# {\sum_{c=0}^{9} \exp{(\boldsymbol{a}^T \boldsymbol{w}_c)}} ,$$  
# 
# i.e. each neuron $j$ outputs the probability of being in class $j$ given an input from the hidden layer $\boldsymbol{a}$, with $\boldsymbol{w}_j$ the weights of neuron $j$ to the inputs.  
# The denominator is a normalization factor to ensure the outputs (probabilities) sum up to 1.  
# The exponent is just the weighted sum of inputs as before:  
# 
# $$ z_j = \sum_{i=1}^n w_ {ij} a_i+b_j.$$  
# 
# Since each neuron in the output layer is connected to the 50 inputs from the hidden layer we have 50x10 = 500
# weights to the output layer.

# ## Weights and biases
# 
# Typically weights are initialized with small values distributed around zero, drawn from a uniform
# or normal distribution. Setting all weights to zero means all neurons give the same output, making the network useless.  
# 
# Adding a bias value to the weighted sum of inputs allows the neural network to represent a greater range
# of values. Without it, any input with the value 0 will be mapped to zero (before being passed through the activation). The bias unit has an output of 1, and a weight to each neuron $j$, $b_j$:  
# 
# $$ z_j = \sum_{i=1}^n w_ {ij} a_i + b_j.$$  
# 
# The bias weights $\boldsymbol{b}$ are often initialized to zero, but a small value like $0.01$ ensures all neurons have some output which can be backpropagated in the first training cycle.

# In[7]:


# building our neural network

n_inputs, n_features = X_train.shape
n_hidden_neurons = 50
n_categories = 10

# we make the weights normally distributed using numpy.random.randn

# weights and bias in the hidden layer
hidden_weights = np.random.randn(n_features, n_hidden_neurons)
hidden_bias = np.zeros(n_hidden_neurons) + 0.01

# weights and bias in the output layer
output_weights = np.random.randn(n_hidden_neurons, n_categories)
output_bias = np.zeros(n_categories) + 0.01


# ## Feed-forward pass
# 
# Denote $F$ the number of features, $H$ the number of hidden neurons and $C$ the number of categories.  
# For each input image we calculate a weighted sum of input features (pixel values) to each neuron $j$ in the hidden layer $l$:  
# 
# $$ z_{j}^{l} = \sum_{i=1}^{F} w_{ij}^{l} x_i + b_{j}^{l},$$
# 
# this is then passed through our activation function  
# 
# $$ a_{j}^{l} = f(z_{j}^{l}) .$$  
# 
# We calculate a weighted sum of inputs (activations in the hidden layer) to each neuron $j$ in the output layer:  
# 
# $$ z_{j}^{L} = \sum_{i=1}^{H} w_{ij}^{L} a_{i}^{l} + b_{j}^{L}.$$  
# 
# Finally we calculate the output of neuron $j$ in the output layer using the softmax function:  
# 
# $$ a_{j}^{L} = \frac{\exp{(z_j^{L})}}
# {\sum_{c=0}^{C-1} \exp{(z_c^{L})}} .$$

# ## Matrix multiplications
# 
# Since our data has the dimensions $X = (n_{inputs}, n_{features})$ and our weights to the hidden
# layer have the dimensions  
# $W_{hidden} = (n_{features}, n_{hidden})$,
# we can easily feed the network all our training data in one go by taking the matrix product  
# 
# $$ X W^{h} = (n_{inputs}, n_{hidden}),$$ 
# 
# and obtain a matrix that holds the weighted sum of inputs to the hidden layer
# for each input image and each hidden neuron.    
# We also add the bias to obtain a matrix of weighted sums to the hidden layer $Z^{h}$:  
# 
# $$ \boldsymbol{z}^{l} = \boldsymbol{X} \boldsymbol{W}^{l} + \boldsymbol{b}^{l} ,$$
# 
# meaning the same bias (1D array with size equal number of hidden neurons) is added to each input image.  
# This is then passed through the activation:  
# 
# $$ \boldsymbol{a}^{l} = f(\boldsymbol{z}^l) .$$  
# 
# This is fed to the output layer:  
# 
# $$ \boldsymbol{z}^{L} = \boldsymbol{a}^{L} \boldsymbol{W}^{L} + \boldsymbol{b}^{L} .$$
# 
# Finally we receive our output values for each image and each category by passing it through the softmax function:  
# 
# $$ output = softmax (\boldsymbol{z}^{L}) = (n_{inputs}, n_{categories}) .$$

# In[8]:


# setup the feed-forward pass, subscript h = hidden layer

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def feed_forward(X):
    # weighted sum of inputs to the hidden layer
    z_h = np.matmul(X, hidden_weights) + hidden_bias
    # activation in the hidden layer
    a_h = sigmoid(z_h)
    
    # weighted sum of inputs to the output layer
    z_o = np.matmul(a_h, output_weights) + output_bias
    # softmax output
    # axis 0 holds each input and axis 1 the probabilities of each category
    exp_term = np.exp(z_o)
    probabilities = exp_term / np.sum(exp_term, axis=1, keepdims=True)
    
    return probabilities

probabilities = feed_forward(X_train)
print("probabilities = (n_inputs, n_categories) = " + str(probabilities.shape))
print("probability that image 0 is in category 0,1,2,...,9 = \n" + str(probabilities[0]))
print("probabilities sum up to: " + str(probabilities[0].sum()))
print()

# we obtain a prediction by taking the class with the highest likelihood
def predict(X):
    probabilities = feed_forward(X)
    return np.argmax(probabilities, axis=1)

predictions = predict(X_train)
print("predictions = (n_inputs) = " + str(predictions.shape))
print("prediction for image 0: " + str(predictions[0]))
print("correct label for image 0: " + str(Y_train[0]))


# ## Choose cost function and optimizer
# 
# To measure how well our neural network is doing we need to introduce a cost function.  
# We will call the function that gives the error of a single sample output the *loss* function, and the function
# that gives the total error of our network across all samples the *cost* function.
# A typical choice for multiclass classification is the *cross-entropy* loss, also known as the negative log likelihood.  
# 
# In *multiclass* classification it is common to treat each integer label as a so called *one-hot* vector:  
# 
# $$ y = 5 \quad \rightarrow \quad \boldsymbol{y} = (0, 0, 0, 0, 0, 1, 0, 0, 0, 0) ,$$  
# 
# $$ y = 1 \quad \rightarrow \quad \boldsymbol{y} = (0, 1, 0, 0, 0, 0, 0, 0, 0, 0) ,$$  
# 
# i.e. a binary bit string of length $C$, where $C = 10$ is the number of classes in the MNIST dataset.  
# 
# Let $y_{ic}$ denote the $c$-th component of the $i$-th one-hot vector.  
# We define the cost function $\mathcal{C}$ as a sum over the cross-entropy loss for each point $\boldsymbol{x}_i$ in the dataset.
# 
# In the one-hot representation only one of the terms in the loss function is non-zero, namely the
# probability of the correct category $c'$  
# (i.e. the category $c'$ such that $y_{ic'} = 1$). This means that the cross entropy loss only punishes you for how wrong
# you got the correct label. The probability of category $c$ is given by the softmax function. The vector $\boldsymbol{\theta}$ represents the parameters of our network, i.e. all the weights and biases.

# ## Optimizing the cost function
# 
# The network is trained by finding the weights and biases that minimize the cost function. One of the most widely used classes of methods is *gradient descent* and its generalizations. The idea behind gradient descent
# is simply to adjust the weights in the direction where the gradient of the cost function is large and negative. This ensures we flow toward a *local* minimum of the cost function.  
# Each parameter $\theta$ is iteratively adjusted according to the rule  
# 
# $$ \theta_{i+1} = \theta_i - \eta \nabla \mathcal{C}(\theta_i) ,$$
# 
# where $\eta$ is known as the *learning rate*, which controls how big a step we take towards the minimum.  
# This update can be repeated for any number of iterations, or until we are satisfied with the result.  
# 
# A simple and effective improvement is a variant called *Batch Gradient Descent*.  
# Instead of calculating the gradient on the whole dataset, we calculate an approximation of the gradient
# on a subset of the data called a *minibatch*.  
# If there are $N$ data points and we have a minibatch size of $M$, the total number of batches
# is $N/M$.  
# We denote each minibatch $B_k$, with $k = 1, 2,...,N/M$. The gradient then becomes:  
# 
# $$ \nabla \mathcal{C}(\theta) = \frac{1}{N} \sum_{i=1}^N \nabla \mathcal{L}_i(\theta) \quad \rightarrow \quad
# \frac{1}{M} \sum_{i \in B_k} \nabla \mathcal{L}_i(\theta) ,$$
# 
# i.e. instead of averaging the loss over the entire dataset, we average over a minibatch.  
# 
# This has two important benefits:  
# 1. Introducing stochasticity decreases the chance that the algorithm becomes stuck in a local minima.  
# 
# 2. It significantly speeds up the calculation, since we do not have to use the entire dataset to calculate the gradient.  
# 
# The various optmization  methods, with codes and algorithms,  are discussed in our lectures on [Gradient descent approaches](https://compphysics.github.io/MachineLearning/doc/pub/Splines/html/Splines-bs.html).

# ## Regularization
# 
# It is common to add an extra term to the cost function, proportional
# to the size of the weights.  This is equivalent to constraining the
# size of the weights, so that they do not grow out of control.
# Constraining the size of the weights means that the weights cannot
# grow arbitrarily large to fit the training data, and in this way
# reduces *overfitting*.
# 
# We will measure the size of the weights using the so called *L2-norm*, meaning our cost function becomes:  
# 
# $$  \mathcal{C}(\theta) = \frac{1}{N} \sum_{i=1}^N \mathcal{L}_i(\theta) \quad \rightarrow \quad
# \frac{1}{N} \sum_{i=1}^N  \mathcal{L}_i(\theta) + \lambda \lvert \lvert \boldsymbol{w} \rvert \rvert_2^2 
# = \frac{1}{N} \sum_{i=1}^N  \mathcal{L}(\theta) + \lambda \sum_{ij} w_{ij}^2,$$  
# 
# i.e. we sum up all the weights squared. The factor $\lambda$ is known as a regularization parameter.
# 
# In order to train the model, we need to calculate the derivative of
# the cost function with respect to every bias and weight in the
# network.  In total our network has $(64 + 1)\times 50=3250$ weights in
# the hidden layer and $(50 + 1)\times 10=510$ weights to the output
# layer ($+1$ for the bias), and the gradient must be calculated for
# every parameter.  We use the *backpropagation* algorithm discussed
# above. This is a clever use of the chain rule that allows us to
# calculate the gradient efficently.

# ## Matrix  multiplication
# 
# To more efficently train our network these equations are implemented using matrix operations.  
# The error in the output layer is calculated simply as, with $\boldsymbol{t}$ being our targets,  
# 
# $$ \delta_L = \boldsymbol{t} - \boldsymbol{y} = (n_{inputs}, n_{categories}) .$$  
# 
# The gradient for the output weights is calculated as  
# 
# $$ \nabla W_{L} = \boldsymbol{a}^T \delta_L   = (n_{hidden}, n_{categories}) ,$$
# 
# where $\boldsymbol{a} = (n_{inputs}, n_{hidden})$. This simply means that we are summing up the gradients for each input.  
# Since we are going backwards we have to transpose the activation matrix.  
# 
# The gradient with respect to the output bias is then  
# 
# $$ \nabla \boldsymbol{b}_{L} = \sum_{i=1}^{n_{inputs}} \delta_L = (n_{categories}) .$$  
# 
# The error in the hidden layer is  
# 
# $$ \Delta_h = \delta_L W_{L}^T \circ f'(z_{h}) = \delta_L W_{L}^T \circ a_{h} \circ (1 - a_{h}) = (n_{inputs}, n_{hidden}) ,$$  
# 
# where $f'(a_{h})$ is the derivative of the activation in the hidden layer. The matrix products mean
# that we are summing up the products for each neuron in the output layer. The symbol $\circ$ denotes
# the *Hadamard product*, meaning element-wise multiplication.  
# 
# This again gives us the gradients in the hidden layer:  
# 
# $$ \nabla W_{h} = X^T \delta_h = (n_{features}, n_{hidden}) ,$$  
# 
# $$ \nabla b_{h} = \sum_{i=1}^{n_{inputs}} \delta_h = (n_{hidden}) .$$

# In[9]:


# to categorical turns our integer vector into a onehot representation
from sklearn.metrics import accuracy_score

# one-hot in numpy
def to_categorical_numpy(integer_vector):
    n_inputs = len(integer_vector)
    n_categories = np.max(integer_vector) + 1
    onehot_vector = np.zeros((n_inputs, n_categories))
    onehot_vector[range(n_inputs), integer_vector] = 1
    
    return onehot_vector

#Y_train_onehot, Y_test_onehot = to_categorical(Y_train), to_categorical(Y_test)
Y_train_onehot, Y_test_onehot = to_categorical_numpy(Y_train), to_categorical_numpy(Y_test)

def feed_forward_train(X):
    # weighted sum of inputs to the hidden layer
    z_h = np.matmul(X, hidden_weights) + hidden_bias
    # activation in the hidden layer
    a_h = sigmoid(z_h)
    
    # weighted sum of inputs to the output layer
    z_o = np.matmul(a_h, output_weights) + output_bias
    # softmax output
    # axis 0 holds each input and axis 1 the probabilities of each category
    exp_term = np.exp(z_o)
    probabilities = exp_term / np.sum(exp_term, axis=1, keepdims=True)
    
    # for backpropagation need activations in hidden and output layers
    return a_h, probabilities

def backpropagation(X, Y):
    a_h, probabilities = feed_forward_train(X)
    
    # error in the output layer
    error_output = probabilities - Y
    # error in the hidden layer
    error_hidden = np.matmul(error_output, output_weights.T) * a_h * (1 - a_h)
    
    # gradients for the output layer
    output_weights_gradient = np.matmul(a_h.T, error_output)
    output_bias_gradient = np.sum(error_output, axis=0)
    
    # gradient for the hidden layer
    hidden_weights_gradient = np.matmul(X.T, error_hidden)
    hidden_bias_gradient = np.sum(error_hidden, axis=0)

    return output_weights_gradient, output_bias_gradient, hidden_weights_gradient, hidden_bias_gradient

print("Old accuracy on training data: " + str(accuracy_score(predict(X_train), Y_train)))

eta = 0.01
lmbd = 0.01
for i in range(1000):
    # calculate gradients
    dWo, dBo, dWh, dBh = backpropagation(X_train, Y_train_onehot)
    
    # regularization term gradients
    dWo += lmbd * output_weights
    dWh += lmbd * hidden_weights
    
    # update weights and biases
    output_weights -= eta * dWo
    output_bias -= eta * dBo
    hidden_weights -= eta * dWh
    hidden_bias -= eta * dBh

print("New accuracy on training data: " + str(accuracy_score(predict(X_train), Y_train)))


# ## Improving performance
# 
# As we can see the network does not seem to be learning at all. It seems to be just guessing the label for each image.  
# In order to obtain a network that does something useful, we will have to do a bit more work.  
# 
# The choice of *hyperparameters* such as learning rate and regularization parameter is hugely influential for the performance of the network. Typically a *grid-search* is performed, wherein we test different hyperparameters separated by orders of magnitude. For example we could test the learning rates $\eta = 10^{-6}, 10^{-5},...,10^{-1}$ with different regularization parameters $\lambda = 10^{-6},...,10^{-0}$.  
# 
# Next, we haven't implemented minibatching yet, which introduces stochasticity and is though to act as an important regularizer on the weights. We call a feed-forward + backward pass with a minibatch an *iteration*, and a full training period
# going through the entire dataset ($n/M$ batches) an *epoch*.
# 
# If this does not improve network performance, you may want to consider altering the network architecture, adding more neurons or hidden layers.  
# Andrew Ng goes through some of these considerations in this [video](https://youtu.be/F1ka6a13S9I). You can find a summary of the video [here](https://kevinzakka.github.io/2016/09/26/applying-deep-learning/).

# ## Full object-oriented implementation
# 
# It is very natural to think of the network as an object, with specific instances of the network
# being realizations of this object with different hyperparameters. An implementation using Python classes provides a clean structure and interface, and the full implementation of our neural network is given below.

# In[10]:


class NeuralNetwork:
    def __init__(
            self,
            X_data,
            Y_data,
            n_hidden_neurons=50,
            n_categories=10,
            epochs=10,
            batch_size=100,
            eta=0.1,
            lmbd=0.0):

        self.X_data_full = X_data
        self.Y_data_full = Y_data

        self.n_inputs = X_data.shape[0]
        self.n_features = X_data.shape[1]
        self.n_hidden_neurons = n_hidden_neurons
        self.n_categories = n_categories

        self.epochs = epochs
        self.batch_size = batch_size
        self.iterations = self.n_inputs // self.batch_size
        self.eta = eta
        self.lmbd = lmbd

        self.create_biases_and_weights()

    def create_biases_and_weights(self):
        self.hidden_weights = np.random.randn(self.n_features, self.n_hidden_neurons)
        self.hidden_bias = np.zeros(self.n_hidden_neurons) + 0.01

        self.output_weights = np.random.randn(self.n_hidden_neurons, self.n_categories)
        self.output_bias = np.zeros(self.n_categories) + 0.01

    def feed_forward(self):
        # feed-forward for training
        self.z_h = np.matmul(self.X_data, self.hidden_weights) + self.hidden_bias
        self.a_h = sigmoid(self.z_h)

        self.z_o = np.matmul(self.a_h, self.output_weights) + self.output_bias

        exp_term = np.exp(self.z_o)
        self.probabilities = exp_term / np.sum(exp_term, axis=1, keepdims=True)

    def feed_forward_out(self, X):
        # feed-forward for output
        z_h = np.matmul(X, self.hidden_weights) + self.hidden_bias
        a_h = sigmoid(z_h)

        z_o = np.matmul(a_h, self.output_weights) + self.output_bias
        
        exp_term = np.exp(z_o)
        probabilities = exp_term / np.sum(exp_term, axis=1, keepdims=True)
        return probabilities

    def backpropagation(self):
        error_output = self.probabilities - self.Y_data
        error_hidden = np.matmul(error_output, self.output_weights.T) * self.a_h * (1 - self.a_h)

        self.output_weights_gradient = np.matmul(self.a_h.T, error_output)
        self.output_bias_gradient = np.sum(error_output, axis=0)

        self.hidden_weights_gradient = np.matmul(self.X_data.T, error_hidden)
        self.hidden_bias_gradient = np.sum(error_hidden, axis=0)

        if self.lmbd > 0.0:
            self.output_weights_gradient += self.lmbd * self.output_weights
            self.hidden_weights_gradient += self.lmbd * self.hidden_weights

        self.output_weights -= self.eta * self.output_weights_gradient
        self.output_bias -= self.eta * self.output_bias_gradient
        self.hidden_weights -= self.eta * self.hidden_weights_gradient
        self.hidden_bias -= self.eta * self.hidden_bias_gradient

    def predict(self, X):
        probabilities = self.feed_forward_out(X)
        return np.argmax(probabilities, axis=1)

    def predict_probabilities(self, X):
        probabilities = self.feed_forward_out(X)
        return probabilities

    def train(self):
        data_indices = np.arange(self.n_inputs)

        for i in range(self.epochs):
            for j in range(self.iterations):
                # pick datapoints with replacement
                chosen_datapoints = np.random.choice(
                    data_indices, size=self.batch_size, replace=False
                )

                # minibatch training data
                self.X_data = self.X_data_full[chosen_datapoints]
                self.Y_data = self.Y_data_full[chosen_datapoints]

                self.feed_forward()
                self.backpropagation()


# ## Evaluate model performance on test data
# 
# To measure the performance of our network we evaluate how well it does it data it has never seen before, i.e. the test data.  
# We measure the performance of the network using the *accuracy* score.  
# The accuracy is as you would expect just the number of images correctly labeled divided by the total number of images. A perfect classifier will have an accuracy score of $1$.  
# 
# $$ \text{Accuracy} = \frac{\sum_{i=1}^n I(\tilde{y}_i = y_i)}{n} ,$$  
# 
# where $I$ is the indicator function, $1$ if $\tilde{y}_i = y_i$ and $0$ otherwise.

# In[11]:


epochs = 100
batch_size = 100

dnn = NeuralNetwork(X_train, Y_train_onehot, eta=eta, lmbd=lmbd, epochs=epochs, batch_size=batch_size,
                    n_hidden_neurons=n_hidden_neurons, n_categories=n_categories)
dnn.train()
test_predict = dnn.predict(X_test)

# accuracy score from scikit library
print("Accuracy score on test set: ", accuracy_score(Y_test, test_predict))

# equivalent in numpy
def accuracy_score_numpy(Y_test, Y_pred):
    return np.sum(Y_test == Y_pred) / len(Y_test)

#print("Accuracy score on test set: ", accuracy_score_numpy(Y_test, test_predict))


# ## Adjust hyperparameters
# 
# We now perform a grid search to find the optimal hyperparameters for the network.  
# Note that we are only using 1 layer with 50 neurons, and human performance is estimated to be around $98\%$ ($2\%$ error rate).

# In[12]:


eta_vals = np.logspace(-5, 1, 7)
lmbd_vals = np.logspace(-5, 1, 7)
# store the models for later use
DNN_numpy = np.zeros((len(eta_vals), len(lmbd_vals)), dtype=object)

# grid search
for i, eta in enumerate(eta_vals):
    for j, lmbd in enumerate(lmbd_vals):
        dnn = NeuralNetwork(X_train, Y_train_onehot, eta=eta, lmbd=lmbd, epochs=epochs, batch_size=batch_size,
                            n_hidden_neurons=n_hidden_neurons, n_categories=n_categories)
        dnn.train()
        
        DNN_numpy[i][j] = dnn
        
        test_predict = dnn.predict(X_test)
        
        print("Learning rate  = ", eta)
        print("Lambda = ", lmbd)
        print("Accuracy score on test set: ", accuracy_score(Y_test, test_predict))
        print()


# ## Visualization

# In[13]:


# visual representation of grid search
# uses seaborn heatmap, you can also do this with matplotlib imshow
import seaborn as sns

sns.set()

train_accuracy = np.zeros((len(eta_vals), len(lmbd_vals)))
test_accuracy = np.zeros((len(eta_vals), len(lmbd_vals)))

for i in range(len(eta_vals)):
    for j in range(len(lmbd_vals)):
        dnn = DNN_numpy[i][j]
        
        train_pred = dnn.predict(X_train) 
        test_pred = dnn.predict(X_test)

        train_accuracy[i][j] = accuracy_score(Y_train, train_pred)
        test_accuracy[i][j] = accuracy_score(Y_test, test_pred)

        
fig, ax = plt.subplots(figsize = (10, 10))
sns.heatmap(train_accuracy, annot=True, ax=ax, cmap="viridis")
ax.set_title("Training Accuracy")
ax.set_ylabel("$\eta$")
ax.set_xlabel("$\lambda$")
plt.show()

fig, ax = plt.subplots(figsize = (10, 10))
sns.heatmap(test_accuracy, annot=True, ax=ax, cmap="viridis")
ax.set_title("Test Accuracy")
ax.set_ylabel("$\eta$")
ax.set_xlabel("$\lambda$")
plt.show()


# ## scikit-learn implementation
# 
# **scikit-learn** focuses more
# on traditional machine learning methods, such as regression,
# clustering, decision trees, etc. As such, it has only two types of
# neural networks: Multi Layer Perceptron outputting continuous values,
# *MPLRegressor*, and Multi Layer Perceptron outputting labels,
# *MLPClassifier*. We will see how simple it is to use these classes.
# 
# **scikit-learn** implements a few improvements from our neural network,
# such as early stopping, a varying learning rate, different
# optimization methods, etc. We would therefore expect a better
# performance overall.

# In[14]:


from sklearn.neural_network import MLPClassifier
# store models for later use
DNN_scikit = np.zeros((len(eta_vals), len(lmbd_vals)), dtype=object)

for i, eta in enumerate(eta_vals):
    for j, lmbd in enumerate(lmbd_vals):
        dnn = MLPClassifier(hidden_layer_sizes=(n_hidden_neurons), activation='logistic',
                            alpha=lmbd, learning_rate_init=eta, max_iter=epochs)
        dnn.fit(X_train, Y_train)
        
        DNN_scikit[i][j] = dnn
        
        print("Learning rate  = ", eta)
        print("Lambda = ", lmbd)
        print("Accuracy score on test set: ", dnn.score(X_test, Y_test))
        print()


# ## Visualization

# In[15]:


# optional
# visual representation of grid search
# uses seaborn heatmap, could probably do this in matplotlib
import seaborn as sns

sns.set()

train_accuracy = np.zeros((len(eta_vals), len(lmbd_vals)))
test_accuracy = np.zeros((len(eta_vals), len(lmbd_vals)))

for i in range(len(eta_vals)):
    for j in range(len(lmbd_vals)):
        dnn = DNN_scikit[i][j]
        
        train_pred = dnn.predict(X_train) 
        test_pred = dnn.predict(X_test)

        train_accuracy[i][j] = accuracy_score(Y_train, train_pred)
        test_accuracy[i][j] = accuracy_score(Y_test, test_pred)

        
fig, ax = plt.subplots(figsize = (10, 10))
sns.heatmap(train_accuracy, annot=True, ax=ax, cmap="viridis")
ax.set_title("Training Accuracy")
ax.set_ylabel("$\eta$")
ax.set_xlabel("$\lambda$")
plt.show()

fig, ax = plt.subplots(figsize = (10, 10))
sns.heatmap(test_accuracy, annot=True, ax=ax, cmap="viridis")
ax.set_title("Test Accuracy")
ax.set_ylabel("$\eta$")
ax.set_xlabel("$\lambda$")
plt.show()


# ## Testing our code for the XOR, OR and AND gates
# 
# Last week we discussed three different types of gates, the so-called
# XOR, the OR and the AND gates.  Their inputs and outputs can be
# summarized using the following tables, first for the OR gate with
# inputs $x_1$ and $x_2$ and outputs $y$:
# 
# <table class="dotable" border="1">
# <thead>
# <tr><th align="center">$x_1$</th> <th align="center">$x_2$</th> <th align="center">$y$</th> </tr>
# </thead>
# <tbody>
# <tr><td align="center">   0        </td> <td align="center">   0        </td> <td align="center">   0      </td> </tr>
# <tr><td align="center">   0        </td> <td align="center">   1        </td> <td align="center">   1      </td> </tr>
# <tr><td align="center">   1        </td> <td align="center">   0        </td> <td align="center">   1      </td> </tr>
# <tr><td align="center">   1        </td> <td align="center">   1        </td> <td align="center">   1      </td> </tr>
# </tbody>
# </table>

# ## The AND and XOR Gates
# 
# The AND gate is defined as
# 
# <table class="dotable" border="1">
# <thead>
# <tr><th align="center">$x_1$</th> <th align="center">$x_2$</th> <th align="center">$y$</th> </tr>
# </thead>
# <tbody>
# <tr><td align="center">   0        </td> <td align="center">   0        </td> <td align="center">   0      </td> </tr>
# <tr><td align="center">   0        </td> <td align="center">   1        </td> <td align="center">   0      </td> </tr>
# <tr><td align="center">   1        </td> <td align="center">   0        </td> <td align="center">   0      </td> </tr>
# <tr><td align="center">   1        </td> <td align="center">   1        </td> <td align="center">   1      </td> </tr>
# </tbody>
# </table>
# 
# And finally we have the XOR gate
# 
# <table class="dotable" border="1">
# <thead>
# <tr><th align="center">$x_1$</th> <th align="center">$x_2$</th> <th align="center">$y$</th> </tr>
# </thead>
# <tbody>
# <tr><td align="center">   0        </td> <td align="center">   0        </td> <td align="center">   0      </td> </tr>
# <tr><td align="center">   0        </td> <td align="center">   1        </td> <td align="center">   1      </td> </tr>
# <tr><td align="center">   1        </td> <td align="center">   0        </td> <td align="center">   1      </td> </tr>
# <tr><td align="center">   1        </td> <td align="center">   1        </td> <td align="center">   0      </td> </tr>
# </tbody>
# </table>

# ## Representing the Data Sets
# 
# Our design matrix is defined by the input values $x_1$ and $x_2$. Since we have four possible outputs, our design matrix reads

# $$
# \boldsymbol{X}=\begin{bmatrix} 0 & 0 \\
#                        0 & 1 \\
# 		       1 & 0 \\
# 		       1 & 1 \end{bmatrix},
# $$

# while the vector of outputs is $\boldsymbol{y}^T=[0,1,1,0]$ for the XOR gate, $\boldsymbol{y}^T=[0,0,0,1]$ for the AND gate and $\boldsymbol{y}^T=[0,1,1,1]$ for the OR gate.

# ## Setting up the Neural Network
# 
# We define first our design matrix and the various output vectors for the different gates.

# In[16]:


"""
Simple code that tests XOR, OR and AND gates with linear regression
"""

# import necessary packages
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def feed_forward(X):
    # weighted sum of inputs to the hidden layer
    z_h = np.matmul(X, hidden_weights) + hidden_bias
    # activation in the hidden layer
    a_h = sigmoid(z_h)
    
    # weighted sum of inputs to the output layer
    z_o = np.matmul(a_h, output_weights) + output_bias
    # softmax output
    # axis 0 holds each input and axis 1 the probabilities of each category
    probabilities = sigmoid(z_o)
    return probabilities

# we obtain a prediction by taking the class with the highest likelihood
def predict(X):
    probabilities = feed_forward(X)
    return np.argmax(probabilities, axis=1)

# ensure the same random numbers appear every time
np.random.seed(0)

# Design matrix
X = np.array([ [0, 0], [0, 1], [1, 0],[1, 1]],dtype=np.float64)

# The XOR gate
yXOR = np.array( [ 0, 1 ,1, 0])
# The OR gate
yOR = np.array( [ 0, 1 ,1, 1])
# The AND gate
yAND = np.array( [ 0, 0 ,0, 1])

# Defining the neural network
n_inputs, n_features = X.shape
n_hidden_neurons = 2
n_categories = 2
n_features = 2

# we make the weights normally distributed using numpy.random.randn

# weights and bias in the hidden layer
hidden_weights = np.random.randn(n_features, n_hidden_neurons)
hidden_bias = np.zeros(n_hidden_neurons) + 0.01

# weights and bias in the output layer
output_weights = np.random.randn(n_hidden_neurons, n_categories)
output_bias = np.zeros(n_categories) + 0.01

probabilities = feed_forward(X)
print(probabilities)


predictions = predict(X)
print(predictions)


# Not an impressive result, but this was our first forward pass with randomly assigned weights. Let us now add the full network with the back-propagation algorithm discussed above.

# ## The Code using Scikit-Learn

# In[17]:


# import necessary packages
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns

# ensure the same random numbers appear every time
np.random.seed(0)

# Design matrix
X = np.array([ [0, 0], [0, 1], [1, 0],[1, 1]],dtype=np.float64)

# The XOR gate
yXOR = np.array( [ 0, 1 ,1, 0])
# The OR gate
yOR = np.array( [ 0, 1 ,1, 1])
# The AND gate
yAND = np.array( [ 0, 0 ,0, 1])

# Defining the neural network
n_inputs, n_features = X.shape
n_hidden_neurons = 2
n_categories = 2
n_features = 2

eta_vals = np.logspace(-5, 1, 7)
lmbd_vals = np.logspace(-5, 1, 7)
# store models for later use
DNN_scikit = np.zeros((len(eta_vals), len(lmbd_vals)), dtype=object)
epochs = 100

for i, eta in enumerate(eta_vals):
    for j, lmbd in enumerate(lmbd_vals):
        dnn = MLPClassifier(hidden_layer_sizes=(n_hidden_neurons), activation='logistic',
                            alpha=lmbd, learning_rate_init=eta, max_iter=epochs)
        dnn.fit(X, yXOR)
        DNN_scikit[i][j] = dnn
        print("Learning rate  = ", eta)
        print("Lambda = ", lmbd)
        print("Accuracy score on data set: ", dnn.score(X, yXOR))
        print()

sns.set()
test_accuracy = np.zeros((len(eta_vals), len(lmbd_vals)))
for i in range(len(eta_vals)):
    for j in range(len(lmbd_vals)):
        dnn = DNN_scikit[i][j]
        test_pred = dnn.predict(X)
        test_accuracy[i][j] = accuracy_score(yXOR, test_pred)

fig, ax = plt.subplots(figsize = (10, 10))
sns.heatmap(test_accuracy, annot=True, ax=ax, cmap="viridis")
ax.set_title("Test Accuracy")
ax.set_ylabel("$\eta$")
ax.set_xlabel("$\lambda$")
plt.show()

