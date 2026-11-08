None

[Getting started](https://keras.io/getting_started/)

[About Keras](https://keras.io/getting_started/about/)
 [Introduction to Keras for engineers](https://keras.io/getting_started/intro_to_keras_for_engineers/)
 [Keras 3 benchmarks](https://keras.io/getting_started/benchmarks/)
 [The Keras ecosystem](https://keras.io/getting_started/ecosystem/)
 [Frequently Asked Questions](https://keras.io/getting_started/faq/)

► [Getting started](https://keras.io/getting_started/)
 / The Keras ecosystem

The Keras ecosystem
===================

The Keras project isn't limited to the core Keras API for building and training neural networks. It spans a wide range of related initiatives that cover every step of the machine learning workflow.

* * *

KerasHub
--------

[KerasHub Documentation](https://keras.io/keras_hub/)
 - [KerasHub GitHub repository](https://github.com/keras-team/keras-hub)

KerasHub is a pretrained modeling library that aims to be simple, flexible, and fast. The library provides Keras implementations of popular model architectures, paired with a collection of pretrained checkpoints. Models can be used with text, image, and audio data for generation, classification, and many other built-in tasks.

* * *

KerasRS
-------

[KerasRS Documentation](https://keras.io/keras_rs/)
 - [KerasRS GitHub repository](https://github.com/keras-team/keras-rs)

Keras Recommenders is a library for building recommender systems on top of Keras. It provides a collection of building blocks which help with the full workflow of creating a recommender system.

* * *

KerasTuner
----------

[KerasTuner Documentation](https://keras.io/keras_tuner/)
 - [KerasTuner GitHub repository](https://github.com/keras-team/keras-tuner)

KerasTuner is an easy-to-use, scalable hyperparameter optimization framework that solves the pain points of hyperparameter search. Easily configure your search space with a define-by-run syntax, then leverage one of the available search algorithms to find the best hyperparameter values for your models. KerasTuner comes with Bayesian Optimization, Hyperband, and Random Search algorithms built-in, and is also designed to be easy for researchers to extend in order to experiment with new search algorithms.

* * *

AutoKeras
---------

[AutoKeras Documentation](https://autokeras.com/)
 - [AutoKeras GitHub repository](https://github.com/keras-team/autokeras)

AutoKeras is an AutoML system based on Keras. It is developed by [DATA Lab](http://faculty.cs.tamu.edu/xiahu/index.html)
 at Texas A&M University. The goal of AutoKeras is to make machine learning accessible for everyone. It provides high-level end-to-end APIs such as [`ImageClassifier`](https://autokeras.com/tutorial/image_classification/)
 or [`TextClassifier`](https://autokeras.com/tutorial/text_classification/)
 to solve machine learning problems in a few lines, as well as [flexible building blocks](https://autokeras.com/tutorial/customized/)
 to perform architecture search.

Copied!

`import autokeras as ak  clf = ak.ImageClassifier() clf.fit(x_train, y_train) results = clf.predict(x_test)`

* * *

BayesFlow
---------

[BayesFlow documentation](https://bayesflow.org/)
 - [BayesFlow](https://github.com/bayesflow-org/bayesflow)

A Python library for amortized Bayesian workflows using generative neural networks, built on Keras 3, featuring:

*   A user-friendly API for rapid Bayesian workflows
*   A rich collection of neural network architectures
*   Multi-backend support via Keras 3: You can use PyTorch, TensorFlow, or JAX

* * *

NEAT
----

[NEAT documentation](https://neat-cylu.vercel.app/)
 - [NEAT GitHub repository](https://github.com/ItCodinTime/NEAT)

NEAT (Nash-Equilibrium Adaptive Training) is a Keras-first optimizer library for conflict-aware neural network training. It provides a Keras 3 optimizer usable with `model.compile(...)`, plus a NumPy reference engine for validating the update rule.

Features include:

*   Keras-compatible optimizer API
*   Nash-inspired conflict-aware gradient correction
*   Optional native CPU acceleration
*   Player-aware training utilities
*   Training diagnostics for conflict and update alignment

Copied!

`import keras from neat_optim import NEAT  model.compile(   optimizer=NEAT(learning_rate=1e-3),   loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True), )`

[The Keras ecosystem](https://keras.io/getting_started/ecosystem/#the-keras-ecosystem)

[KerasHub](https://keras.io/getting_started/ecosystem/#kerashub)

[KerasRS](https://keras.io/getting_started/ecosystem/#kerasrs)

[KerasTuner](https://keras.io/getting_started/ecosystem/#kerastuner)

[AutoKeras](https://keras.io/getting_started/ecosystem/#autokeras)

[BayesFlow](https://keras.io/getting_started/ecosystem/#bayesflow)

[NEAT](https://keras.io/getting_started/ecosystem/#neat)