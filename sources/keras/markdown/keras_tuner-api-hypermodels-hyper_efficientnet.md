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
 / HyperEfficientNet

HyperEfficientNet
=================

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/applications/efficientnet.py#L46)

### `HyperEfficientNet` class

Copied!

`keras_tuner.applications.HyperEfficientNet(     input_shape=None, input_tensor=None, classes=None, augmentation_model=None, **kwargs )`

An EfficientNet hypermodel.

Models built by `HyperEfficientNet` take images with shape (height, width, channels) as input. The output are one-hot encoded with the length matching the number of classes specified by the `classes` argument.

**Arguments**

*   **input\_shape**: Optional shape tuple, e.g. `(256, 256, 3)`. One of `input_shape` or `input_tensor` must be specified.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model. One of `input_shape` or `input_tensor` must be specified.
*   **classes**: Optional number of classes to classify images into, only to be specified if `include_top` is True, and if no `weights` argument is specified.
*   **augmentation\_model**: Optional `Model` or `HyperModel` instance for image augmentation.
*   **\*\*kwargs**: Additional keyword arguments that apply to all hypermodels. See [`keras_tuner.HyperModel`](https://keras.io/keras_tuner/api/hypermodels/base_hypermodel#hypermodel-class)
    .

* * *

[HyperEfficientNet](https://keras.io/keras_tuner/api/hypermodels/hyper_efficientnet/#hyperefficientnet)

[`HyperEfficientNet` class](https://keras.io/keras_tuner/api/hypermodels/hyper_efficientnet/#hyperefficientnet-class)