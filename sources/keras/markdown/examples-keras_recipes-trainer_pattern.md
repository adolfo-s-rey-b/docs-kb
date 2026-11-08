None

[Code examples](https://keras.io/examples/)

[Computer Vision](https://keras.io/examples/vision/)
 [Natural Language Processing](https://keras.io/examples/nlp/)
 [Structured Data](https://keras.io/examples/structured_data/)
 [Timeseries](https://keras.io/examples/timeseries/)
 [Generative Deep Learning](https://keras.io/examples/generative/)
 [Audio Data](https://keras.io/examples/audio/)
 [Reinforcement Learning](https://keras.io/examples/rl/)
 [Graph Data](https://keras.io/examples/graph/)
 [Quick Keras Recipes](https://keras.io/examples/keras_recipes/)
 [Parameter-efficient fine-tuning of Gemma with LoRA and QLoRA](https://keras.io/examples/keras_recipes/parameter_efficient_finetuning_of_gemma_with_lora_and_qlora/)
 [Float8 training and inference with a simple Transformer model](https://keras.io/examples/keras_recipes/float8_training_and_inference_with_transformer/)
 [Keras debugging tips](https://keras.io/examples/keras_recipes/debugging_tips/)
 [Customizing the convolution operation of a Conv2D layer](https://keras.io/examples/keras_recipes/subclassing_conv_layers/)
 [Trainer pattern](https://keras.io/examples/keras_recipes/trainer_pattern/)
 [Endpoint layer pattern](https://keras.io/examples/keras_recipes/endpoint_layer_pattern/)
 [Reproducibility in Keras Models](https://keras.io/examples/keras_recipes/reproducibility_recipes/)
 [Writing Keras Models With TensorFlow NumPy](https://keras.io/examples/keras_recipes/tensorflow_numpy_models/)
 [Simple custom layer example: Antirectifier](https://keras.io/examples/keras_recipes/antirectifier/)
 [Packaging Keras models for wide distribution using Functional Subclassing](https://keras.io/examples/keras_recipes/packaging_keras_models_for_wide_distribution/)
 [Approximating non-Function Mappings with Mixture Density Networks](https://keras.io/examples/keras_recipes/approximating_non_function_mappings/)
 [Serving TensorFlow models with TFServing](https://keras.io/examples/keras_recipes/tf_serving/)
 [Estimating required sample size for model training](https://keras.io/examples/keras_recipes/sample_size_estimate/)
 [Memory-efficient embeddings for recommendation systems](https://keras.io/examples/keras_recipes/memory_efficient_embeddings/)
 [Creating TFRecords](https://keras.io/examples/keras_recipes/creating_tfrecords/)
 [Probabilistic Bayesian Neural Networks](https://keras.io/examples/keras_recipes/bayesian_neural_networks/)
 [Knowledge distillation recipes](https://keras.io/examples/keras_recipes/better_knowledge_distillation/)
 [Evaluating and exporting scikit-learn metrics in a Keras callback](https://keras.io/examples/keras_recipes/sklearn_metric_callbacks/)
 [How to train a Keras model on TFRecord files](https://keras.io/examples/keras_recipes/tfrecord/)

► [Code examples](https://keras.io/examples/)
 / [Quick Keras Recipes](https://keras.io/examples/keras_recipes/)
 / Trainer pattern

Trainer pattern
===============

**Author:** [nkovela1](https://nkovela1.github.io/)
  
**Date created:** 2022/09/19  
**Last modified:** 2022/09/26  
**Description:** Guide on how to share a custom training step across multiple Keras models.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/keras_recipes/ipynb/trainer_pattern.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/keras_recipes/trainer_pattern.py)

* * *

Introduction
------------

This example shows how to create a custom training step using the "Trainer pattern", which can then be shared across multiple Keras models. This pattern overrides the `train_step()` method of the [`keras.Model`](https://keras.io/api/models/model#model-class)
 class, allowing for training loops beyond plain supervised learning.

The Trainer pattern can also easily be adapted to more complex models with larger custom training steps, such as [this end-to-end GAN model](https://keras.io/guides/custom_train_step_in_tensorflow/#wrapping-up-an-endtoend-gan-example)
, by putting the custom training step in the Trainer class definition.

* * *

Setup
-----

Copied!

`import os  os.environ["KERAS_BACKEND"] = "tensorflow"  import tensorflow as tf import keras  # Load MNIST dataset and standardize the data mnist = keras.datasets.mnist (x_train, y_train), (x_test, y_test) = mnist.load_data() x_train, x_test = x_train / 255.0, x_test / 255.0`

* * *

Define the Trainer class
------------------------

A custom training and evaluation step can be created by overriding the `train_step()` and `test_step()` method of a `Model` subclass:

Copied!

``class MyTrainer(keras.Model):     def __init__(self, model):         super().__init__()         self.model = model         # Create loss and metrics here.         self.loss_fn = keras.losses.SparseCategoricalCrossentropy()         self.accuracy_metric = keras.metrics.SparseCategoricalAccuracy()      @property     def metrics(self):         # List metrics here.         return [self.accuracy_metric]      def train_step(self, data):         x, y = data         with tf.GradientTape() as tape:             y_pred = self.model(x, training=True)  # Forward pass             # Compute loss value             loss = self.loss_fn(y, y_pred)          # Compute gradients         trainable_vars = self.trainable_variables         gradients = tape.gradient(loss, trainable_vars)          # Update weights         self.optimizer.apply_gradients(zip(gradients, trainable_vars))          # Update metrics         for metric in self.metrics:             metric.update_state(y, y_pred)          # Return a dict mapping metric names to current value.         return {m.name: m.result() for m in self.metrics}      def test_step(self, data):         x, y = data          # Inference step         y_pred = self.model(x, training=False)          # Update metrics         for metric in self.metrics:             metric.update_state(y, y_pred)         return {m.name: m.result() for m in self.metrics}      def call(self, x):         # Equivalent to `call()` of the wrapped keras.Model         x = self.model(x)         return x``

* * *

Define multiple models to share the custom training step
--------------------------------------------------------

Let's define two different models that can share our Trainer class and its custom `train_step()`:

Copied!

`# A model defined using Sequential API model_a = keras.models.Sequential(     [         keras.layers.Flatten(input_shape=(28, 28)),         keras.layers.Dense(256, activation="relu"),         keras.layers.Dropout(0.2),         keras.layers.Dense(10, activation="softmax"),     ] )  # A model defined using Functional API func_input = keras.Input(shape=(28, 28, 1)) x = keras.layers.Flatten(input_shape=(28, 28))(func_input) x = keras.layers.Dense(512, activation="relu")(x) x = keras.layers.Dropout(0.4)(x) func_output = keras.layers.Dense(10, activation="softmax")(x)  model_b = keras.Model(func_input, func_output)`

* * *

Create Trainer class objects from the models
--------------------------------------------

Copied!

`trainer_1 = MyTrainer(model_a) trainer_2 = MyTrainer(model_b)`

* * *

Compile and fit the models to the MNIST dataset
-----------------------------------------------

Copied!

`trainer_1.compile(optimizer=keras.optimizers.SGD()) trainer_1.fit(     x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test) )  trainer_2.compile(optimizer=keras.optimizers.Adam()) trainer_2.fit(     x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test) )`

`Epoch 1/5 ... Epoch 4/5  938/938 ━━━━━━━━━━━━━━━━━━━━ 1s 1ms/step - sparse_categorical_accuracy: 0.9770 - val_sparse_categorical_accuracy: 0.9770 Epoch 5/5  938/938 ━━━━━━━━━━━━━━━━━━━━ 1s 2ms/step - sparse_categorical_accuracy: 0.9805 - val_sparse_categorical_accuracy: 0.9789  <keras.src.callbacks.history.History at 0x7efe405fe560>`

* * *

Relevant Chapters from Deep Learning with Python
------------------------------------------------

*   [Chapter 7: A deep dive on Keras](https://deeplearningwithpython.io/chapters/chapter07_deep-dive-keras)
    

[Trainer pattern](https://keras.io/examples/keras_recipes/trainer_pattern/#trainer-pattern)

[Introduction](https://keras.io/examples/keras_recipes/trainer_pattern/#introduction)

[Setup](https://keras.io/examples/keras_recipes/trainer_pattern/#setup)

[Define the Trainer class](https://keras.io/examples/keras_recipes/trainer_pattern/#define-the-trainer-class)

[Define multiple models to share the custom training step](https://keras.io/examples/keras_recipes/trainer_pattern/#define-multiple-models-to-share-the-custom-training-step)

[Create Trainer class objects from the models](https://keras.io/examples/keras_recipes/trainer_pattern/#create-trainer-class-objects-from-the-models)

[Compile and fit the models to the MNIST dataset](https://keras.io/examples/keras_recipes/trainer_pattern/#compile-and-fit-the-models-to-the-mnist-dataset)

[Relevant Chapters from Deep Learning with Python](https://keras.io/examples/keras_recipes/trainer_pattern/#relevant-chapters-from-deep-learning-with-python)