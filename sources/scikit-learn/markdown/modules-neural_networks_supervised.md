[Skip to main content](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/neural_networks_supervised.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/neural_networks_supervised.html)
[1.8.0](https://scikit-learn.org/1.8/modules/neural_networks_supervised.html)
[1.7.2](https://scikit-learn.org/1.7/modules/neural_networks_supervised.html)
[1.6.1](https://scikit-learn.org/1.6/modules/neural_networks_supervised.html)
[1.5.2](https://scikit-learn.org/1.5/modules/neural_networks_supervised.html)
[1.4.2](https://scikit-learn.org/1.4/modules/neural_networks_supervised.html)

Collapse Sidebar Expand Sidebar

1.17. Neural network models (supervised)[#](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#neural-network-models-supervised "Link to this heading")

=============================================================================================================================================================================

Warning

This implementation is not intended for large-scale applications. In particular, scikit-learn offers no GPU support. For much faster, GPU-based implementations, as well as frameworks offering much more flexibility to build deep learning architectures, see [Related Projects](https://scikit-learn.org/stable/related_projects.html#related-projects)
.

1.17.1. Multi-layer Perceptron[#](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#multi-layer-perceptron "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

**Multi-layer Perceptron (MLP)** is a supervised learning algorithm that learns a function f:Rm→Ro by training on a dataset, where m is the number of dimensions for input and o is the number of dimensions for output. Given a set of features X\={x1,x2,...,xm} and a target y, it can learn a non-linear function approximator for either classification or regression. It is different from logistic regression, in that between the input and the output layer, there can be one or more non-linear layers, called hidden layers. Figure 1 shows a one hidden layer MLP with scalar output.

[![../_images/multilayerperceptron_network.png](https://scikit-learn.org/stable/_images/multilayerperceptron_network.png)](https://scikit-learn.org/stable/_images/multilayerperceptron_network.png)

**Figure 1 : One hidden layer MLP.**[#](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#id3 "Link to this image")

The leftmost layer, known as the input layer, consists of a set of neurons {xi|x1,x2,...,xm} representing the input features. Each neuron in the hidden layer transforms the values from the previous layer with a weighted linear summation w1x1+w2x2+...+wmxm, followed by a non-linear activation function g(⋅):R→R - like the hyperbolic tan function. The output layer receives the values from the last hidden layer and transforms them into output values.

The module contains the public attributes `coefs_` and `intercepts_`. `coefs_` is a list of weight matrices, where weight matrix at index i represents the weights between layer i and layer i+1. `intercepts_` is a list of bias vectors, where the vector at index i represents the bias values added to layer i+1.

Advantages and disadvantages of Multi-layer Perceptron[#](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#advantages-and-disadvantages-of-multi-layer-perceptron "Link to this dropdown")

The advantages of Multi-layer Perceptron are:

*   Capability to learn non-linear models.
    
*   Capability to learn models in real-time (on-line learning) using `partial_fit`.
    

The disadvantages of Multi-layer Perceptron (MLP) include:

*   MLP with hidden layers has a non-convex loss function where there exists more than one local minimum. Therefore, different random weight initializations can lead to different validation accuracy.
    
*   MLP requires tuning a number of hyperparameters such as the number of hidden neurons, layers, and iterations.
    
*   MLP is sensitive to feature scaling.
    

Please see [Tips on Practical Use](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#mlp-tips)
 section that addresses some of these disadvantages.

1.17.2. Classification[#](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#classification "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

Class [`MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
 implements a multi-layer perceptron (MLP) algorithm that trains using [Backpropagation](http://ufldl.stanford.edu/tutorial/supervised/MultiLayerNeuralNetworks/#backpropagation_algorithm)
.

MLP trains on two arrays: array X of size (n\_samples, n\_features), which holds the training samples represented as floating point feature vectors; and array y of size (n\_samples,), which holds the target values (class labels) for the training samples:

\>>> from sklearn.neural\_network import MLPClassifier
\>>> X \= \[\[0., 0.\], \[1., 1.\]\]
\>>> y \= \[0, 1\]
\>>> clf \= MLPClassifier(solver\='lbfgs', alpha\=1e-5,
...                     hidden\_layer\_sizes\=(5, 2), random\_state\=1)
...
\>>> clf.fit(X, y)
MLPClassifier(alpha=1e-05, hidden\_layer\_sizes=(5, 2), random\_state=1,
              solver='lbfgs')

Copy to clipboard

After fitting (training), the model can predict labels for new samples:

\>>> clf.predict(\[\[2., 2.\], \[\-1., \-2.\]\])
array(\[1, 0\])

Copy to clipboard

MLP can fit a non-linear model to the training data. `clf.coefs_` contains the weight matrices that constitute the model parameters:

\>>> \[coef.shape for coef in clf.coefs\_\]
\[(2, 5), (5, 2), (2, 1)\]

Copy to clipboard

Currently, [`MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
 supports only the Cross-Entropy loss function, which allows probability estimates by running the `predict_proba` method.

MLP trains using Backpropagation. More precisely, it trains using some form of gradient descent and the gradients are calculated using Backpropagation. For classification, it minimizes the Cross-Entropy loss function, giving a vector of probability estimates P(y|x) per sample x:

\>>> clf.predict\_proba(\[\[2., 2.\], \[1., 2.\]\])
array(\[\[1.967e-04, 9.998e-01\],\
       \[1.967e-04, 9.998e-01\]\])

Copy to clipboard

[`MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
 supports multi-class classification by applying [Softmax](https://en.wikipedia.org/wiki/Softmax_activation_function)
 as the output function.

Further, the model supports [multi-label classification](https://scikit-learn.org/stable/modules/multiclass.html#multiclass)
 in which a sample can belong to more than one class. For each class, the raw output passes through the logistic function. Values larger or equal to `0.5` are rounded to `1`, otherwise to `0`. For a predicted output of a sample, the indices where the value is `1` represent the assigned classes of that sample:

\>>> X \= \[\[0., 0.\], \[1., 1.\]\]
\>>> y \= \[\[0, 1\], \[1, 1\]\]
\>>> clf \= MLPClassifier(solver\='lbfgs', alpha\=1e-5,
...                     hidden\_layer\_sizes\=(15,), random\_state\=1)
...
\>>> clf.fit(X, y)
MLPClassifier(alpha=1e-05, hidden\_layer\_sizes=(15,), random\_state=1,
              solver='lbfgs')
\>>> clf.predict(\[\[1., 2.\]\])
array(\[\[1, 1\]\])
\>>> clf.predict(\[\[0., 0.\]\])
array(\[\[0, 1\]\])

Copy to clipboard

See the examples below and the docstring of [`MLPClassifier.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier.fit "sklearn.neural_network.MLPClassifier.fit")
 for further information.

Examples

*   [Compare Stochastic learning strategies for MLPClassifier](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_training_curves.html#sphx-glr-auto-examples-neural-networks-plot-mlp-training-curves-py)
    
*   See [Visualization of MLP weights on MNIST](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mnist_filters.html#sphx-glr-auto-examples-neural-networks-plot-mnist-filters-py)
     for visualized representation of trained weights.
    

1.17.3. Regression[#](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#regression "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

Class [`MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
 implements a multi-layer perceptron (MLP) that trains using backpropagation with no activation function in the output layer, which can also be seen as using the identity function as activation function. Therefore, it uses the square error as the loss function, and the output is a set of continuous values.

[`MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
 also supports multi-output regression, in which a sample can have more than one target.

1.17.4. Regularization[#](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#regularization "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

Both [`MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
 and [`MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
 use parameter `alpha` for regularization (L2 regularization) term which helps in avoiding overfitting by penalizing weights with large magnitudes. Following plot displays varying decision function with value of alpha.

[![../_images/sphx_glr_plot_mlp_alpha_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_alpha_001.png)](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html)

See the examples below for further information.

Examples

*   [Varying regularization in Multi-layer Perceptron](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html#sphx-glr-auto-examples-neural-networks-plot-mlp-alpha-py)
    

1.17.5. Algorithms[#](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#algorithms "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

MLP trains using [Stochastic Gradient Descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent)
, [Adam](https://arxiv.org/abs/1412.6980)
, or [L-BFGS](https://en.wikipedia.org/wiki/Limited-memory_BFGS)
. Stochastic Gradient Descent (SGD) updates parameters using the gradient of the loss function with respect to a parameter that needs adaptation, i.e.

w←w−η\[α∂R(w)∂w+∂Loss∂w\]

where η is the learning rate which controls the step-size in the parameter space search. Loss is the loss function used for the network.

More details can be found in the documentation of [SGD](https://scikit-learn.org/stable/modules/sgd.html)

Adam is similar to SGD in a sense that it is a stochastic optimizer, but it can automatically adjust the amount to update parameters based on adaptive estimates of lower-order moments.

With SGD or Adam, training supports online and mini-batch learning.

L-BFGS is a solver that approximates the Hessian matrix which represents the second-order partial derivative of a function. Further it approximates the inverse of the Hessian matrix to perform parameter updates. The implementation uses the Scipy version of [L-BFGS](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin_l_bfgs_b.html)
.

If the selected solver is ‘L-BFGS’, training does not support online nor mini-batch learning.

1.17.6. Complexity[#](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#complexity "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

Suppose there are n training samples, m features, k hidden layers, each containing h neurons - for simplicity, and o output neurons. The time complexity of backpropagation is O(i⋅n⋅(m⋅h+(k−1)⋅h⋅h+h⋅o)), where i is the number of iterations. Since backpropagation has a high time complexity, it is advisable to start with smaller number of hidden neurons and few hidden layers for training.

Mathematical formulation[#](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#mathematical-formulation "Link to this dropdown")

Given a set of training examples {(x1,y1),(x2,y2),…,(xn,yn)} where xi∈Rn and yi∈{0,1}, a one hidden layer one hidden neuron MLP learns the function f(x)\=W2g(W1Tx+b1)+b2 where W1∈Rm and W2,b1,b2∈R are model parameters. W1,W2 represent the weights of the input layer and hidden layer, respectively; and b1,b2 represent the bias added to the hidden layer and the output layer, respectively. g(⋅):R→R is the activation function, set by default as the hyperbolic tan. It is given as,

g(z)\=ez−e−zez+e−z

For binary classification, f(x) passes through the logistic function g(z)\=1/(1+e−z) to obtain output values between zero and one. A threshold, set to 0.5, would assign samples of outputs larger or equal 0.5 to the positive class, and the rest to the negative class.

If there are more than two classes, f(x) itself would be a vector of size (n\_classes,). Instead of passing through logistic function, it passes through the softmax function, which is written as,

softmax(z)i\=exp⁡(zi)∑l\=1kexp⁡(zl)

where zi represents the i th element of the input to softmax, which corresponds to class i, and K is the number of classes. The result is a vector containing the probabilities that sample x belongs to each class. The output is the class with the highest probability.

In regression, the output remains as f(x); therefore, output activation function is just the identity function.

MLP uses different loss functions depending on the problem type. The loss function for classification is Average Cross-Entropy, which in binary case is given as,

Loss(y^,y,W)\=−1n∑i\=0n(yiln⁡yi^+(1−yi)ln⁡(1−yi^))+α2n||W||22

where α||W||22 is an L2-regularization term (aka penalty) that penalizes complex models; and α\>0 is a non-negative hyperparameter that controls the magnitude of the penalty.

For regression, MLP uses the Mean Square Error loss function; written as,

Loss(y^,y,W)\=12n∑i\=0n||y^i−yi||22+α2n||W||22

Starting from initial random weights, multi-layer perceptron (MLP) minimizes the loss function by repeatedly updating these weights. After computing the loss, a backward pass propagates it from the output layer to the previous layers, providing each weight parameter with an update value meant to decrease the loss.

In gradient descent, the gradient ∇LossW of the loss with respect to the weights is computed and deducted from W. More formally, this is expressed as,

Wi+1\=Wi−ϵ∇LossWi

where i is the iteration step, and ϵ is the learning rate with a value larger than 0.

The algorithm stops when it reaches a preset maximum number of iterations; or when the improvement in loss is below a certain, small number.

1.17.7. Tips on Practical Use[#](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#tips-on-practical-use "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

*   Multi-layer Perceptron is sensitive to feature scaling, so it is highly recommended to scale your data. For example, scale each attribute on the input vector X to \[0, 1\] or \[-1, +1\], or standardize it to have mean 0 and variance 1. Note that you must apply the _same_ scaling to the test set for meaningful results. You can use [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
     for standardization.
    
    \>>> from sklearn.preprocessing import StandardScaler
    \>>> scaler \= StandardScaler()
    \>>> \# Don't cheat - fit only on training data
    \>>> scaler.fit(X\_train)
    \>>> X\_train \= scaler.transform(X\_train)
    \>>> \# apply same transformation to test data
    \>>> X\_test \= scaler.transform(X\_test)
    
    Copy to clipboard
    
    An alternative and recommended approach is to use [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
     in a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
    
*   Finding a reasonable regularization parameter α is best done using [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    , usually in the range `10.0 ** -np.arange(1, 7)`.
    
*   Empirically, we observed that `L-BFGS` converges faster and with better solutions on small datasets. For relatively large datasets, however, `Adam` is very robust. It usually converges quickly and gives pretty good performance. `SGD` with momentum or nesterov’s momentum, on the other hand, can perform better than those two algorithms if learning rate is correctly tuned.
    

1.17.8. More control with warm\_start[#](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#more-control-with-warm-start "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you want more control over stopping criteria or learning rate in SGD, or want to do additional monitoring, using `warm_start=True` and `max_iter=1` and iterating yourself can be helpful:

\>>> X \= \[\[0., 0.\], \[1., 1.\]\]
\>>> y \= \[0, 1\]
\>>> clf \= MLPClassifier(hidden\_layer\_sizes\=(15,), random\_state\=1, max\_iter\=1, warm\_start\=True)
\>>> for i in range(10):
...     clf.fit(X, y)
...     \# additional monitoring / inspection
MLPClassifier(...

Copy to clipboard

References[#](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#references "Link to this dropdown")

*   [“Learning representations by back-propagating errors.”](https://www.iro.umontreal.ca/~pift6266/A06/refs/backprop_old.pdf)
     Rumelhart, David E., Geoffrey E. Hinton, and Ronald J. Williams.
    
*   [“Stochastic Gradient Descent”](https://leon.bottou.org/projects/sgd)
     L. Bottou - Website, 2010.
    
*   [“Backpropagation”](http://ufldl.stanford.edu/wiki/index.php/Backpropagation_Algorithm)
     Andrew Ng, Jiquan Ngiam, Chuan Yu Foo, Yifan Mai, Caroline Suen - Website, 2011.
    
*   [“Efficient BackProp”](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)
     Y. LeCun, L. Bottou, G. Orr, K. Müller - In Neural Networks: Tricks of the Trade 1998.
    
*   [“Adam: A method for stochastic optimization.”](https://arxiv.org/abs/1412.6980)
     Kingma, Diederik, and Jimmy Ba (2014)
    

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)