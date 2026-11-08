None

[KerasTuner: Hyperparam Tuning](https://keras.io/keras_tuner/)

[Getting started](https://keras.io/keras_tuner/getting_started/)
 [Developer guides](https://keras.io/keras_tuner/guides/)
 [API documentation](https://keras.io/keras_tuner/api/)
 [HyperParameters](https://keras.io/keras_tuner/api/hyperparameters/)
 [Tuners](https://keras.io/keras_tuner/api/tuners/)
 [Oracles](https://keras.io/keras_tuner/api/oracles/)
 [HyperModels](https://keras.io/keras_tuner/api/hypermodels/)
 [Errors](https://keras.io/keras_tuner/api/errors/)

► [KerasTuner: Hyperparam Tuning](https://keras.io/keras_tuner/)
 / [API documentation](https://keras.io/keras_tuner/api/)
 / [HyperModels](https://keras.io/keras_tuner/api/hypermodels/)
 / HyperResNet

HyperResNet
===========

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/applications/resnet.py#L24)

### `HyperResNet` class

Copied!

`keras_tuner.applications.HyperResNet(     include_top=True, input_shape=None, input_tensor=None, classes=None, **kwargs )`

A ResNet hypermodel.

Models built by `HyperResNet` take images with shape (height, width, channels) as input. The output are one-hot encoded with the length matching the number of classes specified by the `classes` argument.

**Arguments**

*   **include\_top**: Boolean, whether to include the fully-connected layer at the top of the network.
*   **input\_shape**: Optional shape tuple, e.g. `(256, 256, 3)`. One of `input_shape` or `input_tensor` must be specified.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model. One of `input_shape` or `input_tensor` must be specified.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified.
*   **\*\*kwargs**: Additional keyword arguments that apply to all hypermodels. See [`keras_tuner.HyperModel`](https://keras.io/keras_tuner/api/hypermodels/base_hypermodel#hypermodel-class)
    .

* * *

[HyperResNet](https://keras.io/keras_tuner/api/hypermodels/hyper_resnet/#hyperresnet)

[`HyperResNet` class](https://keras.io/keras_tuner/api/hypermodels/hyper_resnet/#hyperresnet-class)