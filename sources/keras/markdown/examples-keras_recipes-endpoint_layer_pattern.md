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
 / Endpoint layer pattern

Endpoint layer pattern
======================

**Author:** [fchollet](https://twitter.com/fchollet)
  
**Date created:** 2019/05/10  
**Last modified:** 2023/11/22  
**Description:** Demonstration of the "endpoint layer" pattern (layer that handles loss management).

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/keras_recipes/ipynb/endpoint_layer_pattern.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/keras_recipes/endpoint_layer_pattern.py)

* * *

Setup
-----

Copied!

`import os  os.environ["KERAS_BACKEND"] = "tensorflow"  import tensorflow as tf import keras import numpy as np`

* * *

Usage of endpoint layers in the Functional API
----------------------------------------------

An "endpoint layer" has access to the model's targets, and creates arbitrary losses in `call()` using `self.add_loss()` and `Metric.update_state()`. This enables you to define losses and metrics that don't match the usual signature `fn(y_true, y_pred, sample_weight=None)`.

Note that you could have separate metrics for training and eval with this pattern.

Copied!

``class LogisticEndpoint(keras.layers.Layer):     def __init__(self, name=None):         super().__init__(name=name)         self.loss_fn = keras.losses.BinaryCrossentropy(from_logits=True)         self.accuracy_metric = keras.metrics.BinaryAccuracy(name="accuracy")      def call(self, logits, targets=None, sample_weight=None):         if targets is not None:             # Compute the training-time loss value and add it             # to the layer using `self.add_loss()`.             loss = self.loss_fn(targets, logits, sample_weight)             self.add_loss(loss)              # Log the accuracy as a metric (we could log arbitrary metrics,             # including different metrics for training and inference.)             self.accuracy_metric.update_state(targets, logits, sample_weight)          # Return the inference-time prediction tensor (for `.predict()`).         return tf.nn.softmax(logits)  inputs = keras.Input((764,), name="inputs") logits = keras.layers.Dense(1)(inputs) targets = keras.Input((1,), name="targets") sample_weight = keras.Input((1,), name="sample_weight") preds = LogisticEndpoint()(logits, targets, sample_weight) model = keras.Model([inputs, targets, sample_weight], preds)  data = {     "inputs": np.random.random((1000, 764)),     "targets": np.random.random((1000, 1)),     "sample_weight": np.random.random((1000, 1)), }  model.compile(keras.optimizers.Adam(1e-3)) model.fit(data, epochs=2)``

`Epoch 1/2  27/32 ━━━━━━━━━━━━━━━━[37m━━━━  0s 2ms/step - loss: 0.3664     WARNING: All log messages before absl::InitializeLog() is called are written to STDERR I0000 00:00:1700705222.380735 3351467 device_compiler.h:186] Compiled cluster using XLA!  This line is logged at most once for the lifetime of the process.   32/32 ━━━━━━━━━━━━━━━━━━━━ 2s 31ms/step - loss: 0.3663 Epoch 2/2  32/32 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - loss: 0.3627   <keras.src.callbacks.history.History at 0x7f13401b1e10>`

* * *

Exporting an inference-only model
---------------------------------

Simply don't include `targets` in the model. The weights stay the same.

Copied!

`inputs = keras.Input((764,), name="inputs") logits = keras.layers.Dense(1)(inputs) preds = LogisticEndpoint()(logits, targets=None, sample_weight=None) inference_model = keras.Model(inputs, preds)  inference_model.set_weights(model.get_weights())  preds = inference_model.predict(np.random.random((1000, 764)))`

 `32/32 ━━━━━━━━━━━━━━━━━━━━ 0s 6ms/step`

* * *

Usage of loss endpoint layers in subclassed models
--------------------------------------------------

Copied!

``class LogReg(keras.Model):     def __init__(self):         super().__init__()         self.dense = keras.layers.Dense(1)         self.logistic_endpoint = LogisticEndpoint()      def call(self, inputs):         # Note that all inputs should be in the first argument         # since we want to be able to call `model.fit(inputs)`.         logits = self.dense(inputs["inputs"])         preds = self.logistic_endpoint(             logits=logits,             targets=inputs["targets"],             sample_weight=inputs["sample_weight"],         )         return preds  model = LogReg() data = {     "inputs": np.random.random((1000, 764)),     "targets": np.random.random((1000, 1)),     "sample_weight": np.random.random((1000, 1)), }  model.compile(keras.optimizers.Adam(1e-3)) model.fit(data, epochs=2)``

`Epoch 1/2  32/32 ━━━━━━━━━━━━━━━━━━━━ 1s 9ms/step - loss: 0.3529 Epoch 2/2  32/32 ━━━━━━━━━━━━━━━━━━━━ 0s 1ms/step - loss: 0.3509   <keras.src.callbacks.history.History at 0x7f132c1d1450>`

* * *

Relevant Chapters from Deep Learning with Python
------------------------------------------------

*   [Chapter 7: A deep dive on Keras](https://deeplearningwithpython.io/chapters/chapter07_deep-dive-keras)
    

[Endpoint layer pattern](https://keras.io/examples/keras_recipes/endpoint_layer_pattern/#endpoint-layer-pattern)

[Setup](https://keras.io/examples/keras_recipes/endpoint_layer_pattern/#setup)

[Usage of endpoint layers in the Functional API](https://keras.io/examples/keras_recipes/endpoint_layer_pattern/#usage-of-endpoint-layers-in-the-functional-api)

[Exporting an inference-only model](https://keras.io/examples/keras_recipes/endpoint_layer_pattern/#exporting-an-inferenceonly-model)

[Usage of loss endpoint layers in subclassed models](https://keras.io/examples/keras_recipes/endpoint_layer_pattern/#usage-of-loss-endpoint-layers-in-subclassed-models)

[Relevant Chapters from Deep Learning with Python](https://keras.io/examples/keras_recipes/endpoint_layer_pattern/#relevant-chapters-from-deep-learning-with-python)