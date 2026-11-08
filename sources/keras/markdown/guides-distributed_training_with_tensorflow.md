None

[Developer guides](https://keras.io/guides/)

[The Functional API](https://keras.io/guides/functional_api/)
 [The Sequential model](https://keras.io/guides/sequential_model/)
 [Making new layers & models via subclassing](https://keras.io/guides/making_new_layers_and_models_via_subclassing/)
 [Training & evaluation with the built-in methods](https://keras.io/guides/training_with_built_in_methods/)
 [Customizing \`fit()\` with JAX](https://keras.io/guides/custom_train_step_in_jax/)
 [Customizing \`fit()\` with TensorFlow](https://keras.io/guides/custom_train_step_in_tensorflow/)
 [Customizing \`fit()\` with PyTorch](https://keras.io/guides/custom_train_step_in_torch/)
 [Writing a custom training loop in JAX](https://keras.io/guides/writing_a_custom_training_loop_in_jax/)
 [Writing a custom training loop in TensorFlow](https://keras.io/guides/writing_a_custom_training_loop_in_tensorflow/)
 [Writing a custom training loop in PyTorch](https://keras.io/guides/writing_a_custom_training_loop_in_torch/)
 [Serialization & saving](https://keras.io/guides/serialization_and_saving/)
 [Customizing saving & serialization](https://keras.io/guides/customizing_saving_and_serialization/)
 [Writing your own callbacks](https://keras.io/guides/writing_your_own_callbacks/)
 [Transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
 [Distributed training with JAX](https://keras.io/guides/distributed_training_with_jax/)
 [Distributed training with TensorFlow](https://keras.io/guides/distributed_training_with_tensorflow/)
 [Distributed training with PyTorch](https://keras.io/guides/distributed_training_with_torch/)
 [Distributed training with Keras 3](https://keras.io/guides/distribution/)
 [Migrating Keras 2 code to Keras 3](https://keras.io/guides/migrating_to_keras_3/)
 [How to use Keras with NNX backend](https://keras.io/guides/keras_nnx_guide/)
 [Orbax Checkpointing in Keras](https://keras.io/guides/orbax_checkpoint/)
 [Quantization in Keras](https://keras.io/guides/quantization_overview/)
 [8-bit integer quantization in Keras](https://keras.io/guides/int8_quantization_in_keras/)
 [4-bit integer quantization in Keras](https://keras.io/guides/int4_quantization_in_keras/)
 [GPTQ quantization in Keras](https://keras.io/guides/gptq_quantization_in_keras/)
 [AWQ quantization in Keras](https://keras.io/guides/awq_quantization_in_keras/)
 [Writing quantization-compatible layers in Keras](https://keras.io/guides/writing_quantization_compatible_layers/)
 [Customizing quantization in Keras](https://keras.io/guides/customizing_quantization/)
 [Exporting Keras models to LiteRT](https://keras.io/guides/litert_export/)
 [Define a Custom TPU/GPU Kernel](https://keras.io/guides/define_custom_kernel/)

► [Developer guides](https://keras.io/guides/)
 / Multi-GPU distributed training with TensorFlow

Multi-GPU distributed training with TensorFlow
==============================================

**Author:** [fchollet](https://twitter.com/fchollet)
  
**Date created:** 2020/04/28  
**Last modified:** 2023/06/29  
**Description:** Guide to multi-GPU training for Keras models with TensorFlow.

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/guides/ipynb/distributed_training_with_tensorflow.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/guides/distributed_training_with_tensorflow.py)

* * *

Introduction
------------

There are generally two ways to distribute computation across multiple devices:

**Data parallelism**, where a single model gets replicated on multiple devices or multiple machines. Each of them processes different batches of data, then they merge their results. There exist many variants of this setup, that differ in how the different model replicas merge results, in whether they stay in sync at every batch or whether they are more loosely coupled, etc.

**Model parallelism**, where different parts of a single model run on different devices, processing a single batch of data together. This works best with models that have a naturally-parallel architecture, such as models that feature multiple branches.

This guide focuses on data parallelism, in particular **synchronous data parallelism**, where the different replicas of the model stay in sync after each batch they process. Synchronicity keeps the model convergence behavior identical to what you would see for single-device training.

Specifically, this guide teaches you how to use the [`tf.distribute`](https://www.tensorflow.org/api_docs/python/tf/distribute)
 API to train Keras models on multiple GPUs, with minimal changes to your code, on multiple GPUs (typically 2 to 16) installed on a single machine (single host, multi-device training). This is the most common setup for researchers and small-scale industry workflows.

* * *

Setup
-----

Copied!

`import os  os.environ["KERAS_BACKEND"] = "tensorflow"  import tensorflow as tf import keras`

* * *

Single-host, multi-device synchronous training
----------------------------------------------

In this setup, you have one machine with several GPUs on it (typically 2 to 16). Each device will run a copy of your model (called a **replica**). For simplicity, in what follows, we'll assume we're dealing with 8 GPUs, at no loss of generality.

**How it works**

At each step of training:

*   The current batch of data (called **global batch**) is split into 8 different sub-batches (called **local batches**). For instance, if the global batch has 512 samples, each of the 8 local batches will have 64 samples.
*   Each of the 8 replicas independently processes a local batch: they run a forward pass, then a backward pass, outputting the gradient of the weights with respect to the loss of the model on the local batch.
*   The weight updates originating from local gradients are efficiently merged across the 8 replicas. Because this is done at the end of every step, the replicas always stay in sync.

In practice, the process of synchronously updating the weights of the model replicas is handled at the level of each individual weight variable. This is done through a **mirrored variable** object.

**How to use it**

To do single-host, multi-device synchronous training with a Keras model, you would use the [`tf.distribute.MirroredStrategy` API](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy)
. Here's how it works:

*   Instantiate a `MirroredStrategy`, optionally configuring which specific devices you want to use (by default the strategy will use all GPUs available).
*   Use the strategy object to open a scope, and within this scope, create all the Keras objects you need that contain variables. Typically, that means **creating & compiling the model** inside the distribution scope. In some cases, the first call to `fit()` may also create variables, so it's a good idea to put your `fit()` call in the scope as well.
*   Train the model via `fit()` as usual.

Importantly, we recommend that you use [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 objects to load data in a multi-device or distributed workflow.

Schematically, it looks like this:

Copied!

``# Create a MirroredStrategy. strategy = tf.distribute.MirroredStrategy() print('Number of devices: {}'.format(strategy.num_replicas_in_sync))  # Open a strategy scope. with strategy.scope():     # Everything that creates variables should be under the strategy scope.     # In general this is only model construction & `compile()`.     model = Model(...)     model.compile(...)      # Train the model on all available devices.     model.fit(train_dataset, validation_data=val_dataset, ...)      # Test the model on all available devices.     model.evaluate(test_dataset)``

Here's a simple end-to-end runnable example:

Copied!

``def get_compiled_model():     # Make a simple 2-layer densely-connected neural network.     inputs = keras.Input(shape=(784,))     x = keras.layers.Dense(256, activation="relu")(inputs)     x = keras.layers.Dense(256, activation="relu")(x)     outputs = keras.layers.Dense(10)(x)     model = keras.Model(inputs, outputs)     model.compile(         optimizer=keras.optimizers.Adam(),         loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),         metrics=[keras.metrics.SparseCategoricalAccuracy()],     )     return model  def get_dataset():     batch_size = 32     num_val_samples = 10000      # Return the MNIST dataset in the form of a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset).     (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()      # Preprocess the data (these are Numpy arrays)     x_train = x_train.reshape(-1, 784).astype("float32") / 255     x_test = x_test.reshape(-1, 784).astype("float32") / 255     y_train = y_train.astype("float32")     y_test = y_test.astype("float32")      # Reserve num_val_samples samples for validation     x_val = x_train[-num_val_samples:]     y_val = y_train[-num_val_samples:]     x_train = x_train[:-num_val_samples]     y_train = y_train[:-num_val_samples]     return (         tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(batch_size),         tf.data.Dataset.from_tensor_slices((x_val, y_val)).batch(batch_size),         tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(batch_size),     )  # Create a MirroredStrategy. strategy = tf.distribute.MirroredStrategy() print("Number of devices: {}".format(strategy.num_replicas_in_sync))  # Open a strategy scope. with strategy.scope():     # Everything that creates variables should be under the strategy scope.     # In general this is only model construction & `compile()`.     model = get_compiled_model()      # Train the model on all available devices.     train_dataset, val_dataset, test_dataset = get_dataset()     model.fit(train_dataset, epochs=2, validation_data=val_dataset)      # Test the model on all available devices.     model.evaluate(test_dataset)``

`INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0',) Number of devices: 1 Epoch 1/2  1563/1563 ━━━━━━━━━━━━━━━━━━━━ 7s 4ms/step - loss: 0.3830 - sparse_categorical_accuracy: 0.8884 - val_loss: 0.1361 - val_sparse_categorical_accuracy: 0.9574 Epoch 2/2  1563/1563 ━━━━━━━━━━━━━━━━━━━━ 9s 3ms/step - loss: 0.1068 - sparse_categorical_accuracy: 0.9671 - val_loss: 0.0894 - val_sparse_categorical_accuracy: 0.9724  313/313 ━━━━━━━━━━━━━━━━━━━━ 1s 2ms/step - loss: 0.0988 - sparse_categorical_accuracy: 0.9673`

* * *

Using callbacks to ensure fault tolerance
-----------------------------------------

When using distributed training, you should always make sure you have a strategy to recover from failure (fault tolerance). The simplest way to handle this is to pass `ModelCheckpoint` callback to `fit()`, to save your model at regular intervals (e.g. every 100 batches or every epoch). You can then restart training from your saved model.

Here's a simple example:

Copied!

`# Prepare a directory to store all the checkpoints. checkpoint_dir = "./ckpt" if not os.path.exists(checkpoint_dir):     os.makedirs(checkpoint_dir)  def make_or_restore_model():     # Either restore the latest model, or create a fresh one     # if there is no checkpoint available.     checkpoints = [checkpoint_dir + "/" + name for name in os.listdir(checkpoint_dir)]     if checkpoints:         latest_checkpoint = max(checkpoints, key=os.path.getctime)         print("Restoring from", latest_checkpoint)         return keras.models.load_model(latest_checkpoint)     print("Creating a new model")     return get_compiled_model()  def run_training(epochs=1):     # Create a MirroredStrategy.     strategy = tf.distribute.MirroredStrategy()      # Open a strategy scope and create/restore the model     with strategy.scope():         model = make_or_restore_model()          callbacks = [             # This callback saves a SavedModel every epoch             # We include the current epoch in the folder name.             keras.callbacks.ModelCheckpoint(                 filepath=checkpoint_dir + "/ckpt-{epoch}.keras",                 save_freq="epoch",             )         ]         model.fit(             train_dataset,             epochs=epochs,             callbacks=callbacks,             validation_data=val_dataset,             verbose=2,         )  # Running the first time creates the model run_training(epochs=1)  # Calling the same function again will resume from where we left off run_training(epochs=1)`

`INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0',) Creating a new model 1563/1563 - 7s - 4ms/step - loss: 0.2275 - sparse_categorical_accuracy: 0.9320 - val_loss: 0.1373 - val_sparse_categorical_accuracy: 0.9571 INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0',) Restoring from ./ckpt/ckpt-1.keras 1563/1563 - 6s - 4ms/step - loss: 0.0944 - sparse_categorical_accuracy: 0.9717 - val_loss: 0.0972 - val_sparse_categorical_accuracy: 0.9710`

* * *

[`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 performance tips
---------------------------------------------------------------------------------

When doing distributed training, the efficiency with which you load data can often become critical. Here are a few tips to make sure your [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 pipelines run as fast as possible.

**Note about dataset batching**

When creating your dataset, make sure it is batched with the global batch size. For instance, if each of your 8 GPUs is capable of running a batch of 64 samples, you call use a global batch size of 512.

**Calling `dataset.cache()`**

If you call `.cache()` on a dataset, its data will be cached after running through the first iteration over the data. Every subsequent iteration will use the cached data. The cache can be in memory (default) or to a local file you specify.

This can improve performance when:

*   Your data is not expected to change from iteration to iteration
*   You are reading data from a remote distributed filesystem
*   You are reading data from local disk, but your data would fit in memory and your workflow is significantly IO-bound (e.g. reading & decoding image files).

**Calling `dataset.prefetch(buffer_size)`**

You should almost always call `.prefetch(buffer_size)` after creating a dataset. It means your data pipeline will run asynchronously from your model, with new samples being preprocessed and stored in a buffer while the current batch samples are used to train the model. The next batch will be prefetched in GPU memory by the time the current batch is over.

That's it!

[Multi-GPU distributed training with TensorFlow](https://keras.io/guides/distributed_training_with_tensorflow/#multigpu-distributed-training-with-tensorflow)

[Introduction](https://keras.io/guides/distributed_training_with_tensorflow/#introduction)

[Setup](https://keras.io/guides/distributed_training_with_tensorflow/#setup)

[Single-host, multi-device synchronous training](https://keras.io/guides/distributed_training_with_tensorflow/#singlehost-multidevice-synchronous-training)

[Using callbacks to ensure fault tolerance](https://keras.io/guides/distributed_training_with_tensorflow/#using-callbacks-to-ensure-fault-tolerance)

[`tf.data` performance tips](https://keras.io/guides/distributed_training_with_tensorflow/#tfdata-performance-tips)