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
 / Packaging Keras models for wide distribution using Functional Subclassing

Packaging Keras models for wide distribution using Functional Subclassing
=========================================================================

**Author:** Martin Görner  
**Date created:** 2023-12-13  
**Last modified:** 2023-12-13  
**Description:** When sharing your deep learning models, package them using the Functional Subclassing pattern.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/keras_recipes/ipynb/packaging_keras_models_for_wide_distribution.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/keras_recipes/packaging_keras_models_for_wide_distribution.py)

* * *

Introduction
------------

Keras is the ideal framework for sharing your cutting-edge deep learning models, in a library of pre-trained (or not) models. Millions of ML engineers are fluent in the familiar Keras API, making your models accessible to a global community, whatever their preferred backend (Jax, PyTorch or TensorFlow).

One of the benefits of the Keras API is that it lets users programmatically inspect or edit a model, a feature that is necessary when creating new architectures or workflows based on a pre-trained model.

When distributing models, the Keras team recommends packaging them using the **Functional Subclassing** pattern. Models implemented in this way combine two benefits:

*   They can be instantiated in the normal pythonic way:  
    `model = model_collection_xyz.AmazingModel()`

*   They are Keras functional models which means that they have a programmatically accessible graph of layers, for introspection or model surgery.

This guide explains [how to use](https://keras.io/examples/keras_recipes/packaging_keras_models_for_wide_distribution/#functional-subclassing-model)
 the Functional Subclassing pattern, and showcases its benefits for [programmatic model introspection](https://keras.io/examples/keras_recipes/packaging_keras_models_for_wide_distribution/#model-introspection)
 and [model surgery](https://keras.io/examples/keras_recipes/packaging_keras_models_for_wide_distribution/#model-surgery)
. It also shows two other best practices for sharable Keras models: [configuring models](https://keras.io/examples/keras_recipes/packaging_keras_models_for_wide_distribution/#unconstrained-inputs)
 for the widest range of supported inputs, for example images of various sizes, and [using dictionary inputs](https://keras.io/examples/keras_recipes/packaging_keras_models_for_wide_distribution/#model-with-dictionary-inputs)
 for clarity in more complex models.

* * *

Setup
-----

Copied!

`import keras import tensorflow as tf  # only for tf.data  print("Keras version", keras.version()) print("Keras is running on", keras.config.backend())`

`Keras version 3.0.1 Keras is running on tensorflow`

* * *

Dataset
-------

Let's load an MNIST dataset so that we have something to train with.

Copied!

`# tf.data is a great API for putting together a data stream. # It works whether you use the TensorFlow, PyTorch or Jax backend, # as long as you use it in the data stream only and not inside of a model.  BATCH_SIZE = 256  (x_train, train_labels), (x_test, test_labels) = keras.datasets.mnist.load_data()  train_data = tf.data.Dataset.from_tensor_slices((x_train, train_labels)) train_data = train_data.map(     lambda x, y: (tf.expand_dims(x, axis=-1), y) )  # 1-channel monochrome train_data = train_data.batch(BATCH_SIZE) train_data = train_data.cache() train_data = train_data.shuffle(5000, reshuffle_each_iteration=True) train_data = train_data.repeat()  test_data = tf.data.Dataset.from_tensor_slices((x_test, test_labels)) test_data = test_data.map(     lambda x, y: (tf.expand_dims(x, axis=-1), y) )  # 1-channel monochrome test_data = test_data.batch(10000) test_data = test_data.cache()  STEPS_PER_EPOCH = len(train_labels) // BATCH_SIZE EPOCHS = 5`

* * *

Functional Subclassing Model
----------------------------

The model is wrapped in a class so that end users can instantiate it normally by calling the constructor `MnistModel()` rather than calling a factory function.

Copied!

`class MnistModel(keras.Model):     def __init__(self, **kwargs):         # Keras Functional model definition. This could have used Sequential as         # well. Sequential is just syntactic sugar for simple functional models.          # 1-channel monochrome input         inputs = keras.layers.Input(shape=(None, None, 1), dtype="uint8")         # pixel format conversion from uint8 to float32         y = keras.layers.Rescaling(1 / 255.0)(inputs)          # 3 convolutional layers         y = keras.layers.Conv2D(             filters=16, kernel_size=3, padding="same", activation="relu"         )(y)         y = keras.layers.Conv2D(             filters=32, kernel_size=6, padding="same", activation="relu", strides=2         )(y)         y = keras.layers.Conv2D(             filters=48, kernel_size=6, padding="same", activation="relu", strides=2         )(y)          # 2 dense layers         y = keras.layers.GlobalAveragePooling2D()(y)         y = keras.layers.Dense(48, activation="relu")(y)         y = keras.layers.Dropout(0.4)(y)         outputs = keras.layers.Dense(             10, activation="softmax", name="classification_head"  # 10 classes         )(y)          # A Keras Functional model is created by calling keras.Model(inputs, outputs)         super().__init__(inputs=inputs, outputs=outputs, **kwargs)`

Let's instantiate and train this model.

Copied!

`model = MnistModel()  model.compile(     optimizer="adam",     loss="sparse_categorical_crossentropy",     metrics=["sparse_categorical_accuracy"], )  history = model.fit(     train_data,     steps_per_epoch=STEPS_PER_EPOCH,     epochs=EPOCHS,     validation_data=test_data, )`

`Epoch 1/5  234/234 ━━━━━━━━━━━━━━━━━━━━ 9s 33ms/step - loss: 1.8916 - sparse_categorical_accuracy: 0.2933 - val_loss: 0.4278 - val_sparse_categorical_accuracy: 0.8864 Epoch 2/5  234/234 ━━━━━━━━━━━━━━━━━━━━ 7s 31ms/step - loss: 0.5723 - sparse_categorical_accuracy: 0.8201 - val_loss: 0.2703 - val_sparse_categorical_accuracy: 0.9248 Epoch 3/5  234/234 ━━━━━━━━━━━━━━━━━━━━ 7s 31ms/step - loss: 0.4063 - sparse_categorical_accuracy: 0.8772 - val_loss: 0.2010 - val_sparse_categorical_accuracy: 0.9400 Epoch 4/5  234/234 ━━━━━━━━━━━━━━━━━━━━ 7s 31ms/step - loss: 0.3391 - sparse_categorical_accuracy: 0.8996 - val_loss: 0.1869 - val_sparse_categorical_accuracy: 0.9427 Epoch 5/5  234/234 ━━━━━━━━━━━━━━━━━━━━ 7s 31ms/step - loss: 0.2989 - sparse_categorical_accuracy: 0.9120 - val_loss: 0.1513 - val_sparse_categorical_accuracy: 0.9557`

* * *

Unconstrained inputs
--------------------

Notice, in the model definition above, that the input is specified with undefined dimensions: `Input(shape=(None, None, 1)`

This allows the model to accept any image size as an input. However, this only works if the loosely defined shape can be propagated through all the layers and still determine the size of all weights.

*   So if you have a model architecture that can handle different input sizes with the same weights (like here), then your users will be able to instantiate it without parameters:  
    `model = MnistModel()`

*   If on the other hand, the model must provision different weights for different input sizes, you will have to ask your users to specify the size in the constructor:  
    `model = ModelXYZ(input_size=...)`

* * *

Model introspection
-------------------

Keras maintains a programmatically accessible graph of layers for every model. It can be used for introspection and is accessed through the `model.layers` or `layer.layers` attribute. The utility function `model.summary()` also uses this mechanism internally.

Copied!

`model = MnistModel()  # Model summary works model.summary()  # Recursively walking the layer graph works as well def walk_layers(layer):     if hasattr(layer, "layers"):         for layer in layer.layers:             walk_layers(layer)     else:         print(layer.name)  print("\nWalking model layers:\n") walk_layers(model)`

Model: "mnist\_model\_1"

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape              ┃    Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ input\_layer\_1 (InputLayer)      │ (None, None, None, 1)     │          0 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ rescaling\_1 (Rescaling)         │ (None, None, None, 1)     │          0 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ conv2d\_3 (Conv2D)               │ (None, None, None, 16)    │        160 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ conv2d\_4 (Conv2D)               │ (None, None, None, 32)    │     18,464 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ conv2d\_5 (Conv2D)               │ (None, None, None, 48)    │     55,344 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ global\_average\_pooling2d\_1      │ (None, 48)                │          0 │
│ (GlobalAveragePooling2D)        │                           │            │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ dense\_1 (Dense)                 │ (None, 48)                │      2,352 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ dropout\_1 (Dropout)             │ (None, 48)                │          0 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ classification\_head (Dense)     │ (None, 10)                │        490 │
└─────────────────────────────────┴───────────────────────────┴────────────┘

 Total params: 76,810 (300.04 KB)

 Trainable params: 76,810 (300.04 KB)

 Non-trainable params: 0 (0.00 B)

`Walking model layers:`

`input_layer_1 rescaling_1 conv2d_3 conv2d_4 conv2d_5 global_average_pooling2d_1 dense_1 dropout_1 classification_head`

* * *

Model surgery
-------------

End users might want to instantiate the model from your library but modify it before use. Functional models have a programmatically accessible graph of layers. Edits are possible by slicing and splicing the graph and creating a new functional model.

The alternative is to fork the model code and make the modifications but that forces users to then maintain their fork indefinitely.

Example: instantiate the model but change the classification head to do a binary classification, "0" or "not 0", instead of the original 10-way digits classification.

Copied!

`model = MnistModel()  input = model.input # cut before the classification head y = model.get_layer("classification_head").input  # add a new classification head output = keras.layers.Dense(     1,  # single class for binary classification     activation="sigmoid",     name="binary_classification_head", )(y)  # create a new functional model binary_model = keras.Model(input, output)  binary_model.summary()`

Model: "functional\_1"

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape              ┃    Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ input\_layer\_2 (InputLayer)      │ (None, None, None, 1)     │          0 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ rescaling\_2 (Rescaling)         │ (None, None, None, 1)     │          0 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ conv2d\_6 (Conv2D)               │ (None, None, None, 16)    │        160 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ conv2d\_7 (Conv2D)               │ (None, None, None, 32)    │     18,464 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ conv2d\_8 (Conv2D)               │ (None, None, None, 48)    │     55,344 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ global\_average\_pooling2d\_2      │ (None, 48)                │          0 │
│ (GlobalAveragePooling2D)        │                           │            │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ dense\_2 (Dense)                 │ (None, 48)                │      2,352 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ dropout\_2 (Dropout)             │ (None, 48)                │          0 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ binary\_classification\_head      │ (None, 1)                 │         49 │
│ (Dense)                         │                           │            │
└─────────────────────────────────┴───────────────────────────┴────────────┘

 Total params: 76,369 (298.32 KB)

 Trainable params: 76,369 (298.32 KB)

 Non-trainable params: 0 (0.00 B)

We can now train the new model as a binary classifier.

Copied!

`# new dataset with 0 / 1 labels (1 = digit '0', 0 = all other digits) bin_train_data = train_data.map(     lambda x, y: (x, tf.cast(tf.math.equal(y, tf.zeros_like(y)), dtype=tf.uint8)) ) bin_test_data = test_data.map(     lambda x, y: (x, tf.cast(tf.math.equal(y, tf.zeros_like(y)), dtype=tf.uint8)) )  # appropriate loss and metric for binary classification binary_model.compile(     optimizer="adam", loss="binary_crossentropy", metrics=["binary_accuracy"] )  history = binary_model.fit(     bin_train_data,     steps_per_epoch=STEPS_PER_EPOCH,     epochs=EPOCHS,     validation_data=bin_test_data, )`

`Epoch 1/5  234/234 ━━━━━━━━━━━━━━━━━━━━ 9s 33ms/step - binary_accuracy: 0.8926 - loss: 0.3635 - val_binary_accuracy: 0.9235 - val_loss: 0.1777 Epoch 2/5  234/234 ━━━━━━━━━━━━━━━━━━━━ 7s 31ms/step - binary_accuracy: 0.9411 - loss: 0.1620 - val_binary_accuracy: 0.9766 - val_loss: 0.0748 Epoch 3/5  234/234 ━━━━━━━━━━━━━━━━━━━━ 7s 31ms/step - binary_accuracy: 0.9751 - loss: 0.0794 - val_binary_accuracy: 0.9884 - val_loss: 0.0414 Epoch 4/5  234/234 ━━━━━━━━━━━━━━━━━━━━ 7s 31ms/step - binary_accuracy: 0.9848 - loss: 0.0480 - val_binary_accuracy: 0.9915 - val_loss: 0.0292 Epoch 5/5  234/234 ━━━━━━━━━━━━━━━━━━━━ 7s 31ms/step - binary_accuracy: 0.9910 - loss: 0.0326 - val_binary_accuracy: 0.9917 - val_loss: 0.0286`

* * *

Model with dictionary inputs
----------------------------

In more complex models, with multiple inputs, structuring the inputs as a dictionary can improve readability and usability. This is straightforward to do with a functional model:

Copied!

`class MnistDictModel(keras.Model):     def __init__(self, **kwargs):         #         # The input is a dictionary         #         inputs = {             "image": keras.layers.Input(                 shape=(None, None, 1),  # 1-channel monochrome                 dtype="uint8",                 name="image",             )         }          # pixel format conversion from uint8 to float32         y = keras.layers.Rescaling(1 / 255.0)(inputs["image"])          # 3 conv layers         y = keras.layers.Conv2D(             filters=16, kernel_size=3, padding="same", activation="relu"         )(y)         y = keras.layers.Conv2D(             filters=32, kernel_size=6, padding="same", activation="relu", strides=2         )(y)         y = keras.layers.Conv2D(             filters=48, kernel_size=6, padding="same", activation="relu", strides=2         )(y)          # 2 dense layers         y = keras.layers.GlobalAveragePooling2D()(y)         y = keras.layers.Dense(48, activation="relu")(y)         y = keras.layers.Dropout(0.4)(y)         outputs = keras.layers.Dense(             10, activation="softmax", name="classification_head"  # 10 classes         )(y)          # A Keras Functional model is created by calling keras.Model(inputs, outputs)         super().__init__(inputs=inputs, outputs=outputs, **kwargs)`

We can now train the model on inputs structured as a dictionary.

Copied!

`model = MnistDictModel()  # reformat the dataset as a dictionary dict_train_data = train_data.map(lambda x, y: ({"image": x}, y)) dict_test_data = test_data.map(lambda x, y: ({"image": x}, y))  model.compile(     optimizer="adam",     loss="sparse_categorical_crossentropy",     metrics=["sparse_categorical_accuracy"], )  history = model.fit(     dict_train_data,     steps_per_epoch=STEPS_PER_EPOCH,     epochs=EPOCHS,     validation_data=dict_test_data, )`

`Epoch 1/5  234/234 ━━━━━━━━━━━━━━━━━━━━ 9s 34ms/step - loss: 1.8702 - sparse_categorical_accuracy: 0.3175 - val_loss: 0.4505 - val_sparse_categorical_accuracy: 0.8779 Epoch 2/5  234/234 ━━━━━━━━━━━━━━━━━━━━ 8s 32ms/step - loss: 0.5991 - sparse_categorical_accuracy: 0.8131 - val_loss: 0.2582 - val_sparse_categorical_accuracy: 0.9245 Epoch 3/5  234/234 ━━━━━━━━━━━━━━━━━━━━ 7s 32ms/step - loss: 0.3916 - sparse_categorical_accuracy: 0.8846 - val_loss: 0.1938 - val_sparse_categorical_accuracy: 0.9422 Epoch 4/5  234/234 ━━━━━━━━━━━━━━━━━━━━ 8s 33ms/step - loss: 0.3109 - sparse_categorical_accuracy: 0.9089 - val_loss: 0.1450 - val_sparse_categorical_accuracy: 0.9566 Epoch 5/5  234/234 ━━━━━━━━━━━━━━━━━━━━ 8s 32ms/step - loss: 0.2775 - sparse_categorical_accuracy: 0.9197 - val_loss: 0.1316 - val_sparse_categorical_accuracy: 0.9608`

* * *

Relevant Chapters from Deep Learning with Python
------------------------------------------------

*   [Chapter 18: Best practices for the real world](https://deeplearningwithpython.io/chapters/chapter18_best-practices-for-the-real-world)
    

[Packaging Keras models for wide distribution using Functional Subclassing](https://keras.io/examples/keras_recipes/packaging_keras_models_for_wide_distribution/#packaging-keras-models-for-wide-distribution-using-functional-subclassing)

[Introduction](https://keras.io/examples/keras_recipes/packaging_keras_models_for_wide_distribution/#introduction)

[Setup](https://keras.io/examples/keras_recipes/packaging_keras_models_for_wide_distribution/#setup)

[Dataset](https://keras.io/examples/keras_recipes/packaging_keras_models_for_wide_distribution/#dataset)

[Functional Subclassing Model](https://keras.io/examples/keras_recipes/packaging_keras_models_for_wide_distribution/#functional-subclassing-model)

[Unconstrained inputs](https://keras.io/examples/keras_recipes/packaging_keras_models_for_wide_distribution/#unconstrained-inputs)

[Model introspection](https://keras.io/examples/keras_recipes/packaging_keras_models_for_wide_distribution/#model-introspection)

[Model surgery](https://keras.io/examples/keras_recipes/packaging_keras_models_for_wide_distribution/#model-surgery)

[Model with dictionary inputs](https://keras.io/examples/keras_recipes/packaging_keras_models_for_wide_distribution/#model-with-dictionary-inputs)

[Relevant Chapters from Deep Learning with Python](https://keras.io/examples/keras_recipes/packaging_keras_models_for_wide_distribution/#relevant-chapters-from-deep-learning-with-python)