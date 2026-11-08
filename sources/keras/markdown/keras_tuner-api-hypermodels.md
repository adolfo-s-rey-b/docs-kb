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
 / KerasTuner HyperModels

KerasTuner HyperModels
======================

The `HyperModel` base class makes the search space better encapsulated for sharing and reuse. A `HyperModel` subclass only needs to implement a `build(self, hp)` method, which creates a [`keras.Model`](https://keras.io/api/models/model#model-class)
 using the `hp` argument to define the hyperparameters and returns the model instance. A simple code example is shown as follows.

Copied!

`class MyHyperModel(kt.HyperModel):   def build(self, hp):     model = keras.Sequential()     model.add(keras.layers.Dense(         hp.Choice('units', [8, 16, 32]),         activation='relu'))     model.add(keras.layers.Dense(1, activation='relu'))     model.compile(loss='mse')     return model`

You can pass a `HyperModel` instance to the `Tuner` as the search space.

Copied!

`tuner = kt.RandomSearch(     MyHyperModel(),     objective='val_loss',     max_trials=5)`

There are also some built-in `HyperModel` subclasses (e.g. `HyperResNet`, `HyperXception`) for the users to directly use so that the users don't need to write their own search spaces.

Copied!

`tuner = kt.RandomSearch(     HyperResNet(input_shape=(28, 28, 1), classes=10),     objective='val_loss',     max_trials=5)`

### [The base HyperModel class](https://keras.io/keras_tuner/api/hypermodels/base_hypermodel/)

*   [HyperModel class](https://keras.io/keras_tuner/api/hypermodels/base_hypermodel/#hypermodel-class)
    
*   [build method](https://keras.io/keras_tuner/api/hypermodels/base_hypermodel/#build-method)
    

### [HyperEfficientNet](https://keras.io/keras_tuner/api/hypermodels/hyper_efficientnet/)

*   [HyperEfficientNet class](https://keras.io/keras_tuner/api/hypermodels/hyper_efficientnet/#hyperefficientnet-class)
    

### [HyperImageAugment](https://keras.io/keras_tuner/api/hypermodels/hyper_image_augment/)

*   [HyperImageAugment class](https://keras.io/keras_tuner/api/hypermodels/hyper_image_augment/#hyperimageaugment-class)
    

### [HyperResNet](https://keras.io/keras_tuner/api/hypermodels/hyper_resnet/)

*   [HyperResNet class](https://keras.io/keras_tuner/api/hypermodels/hyper_resnet/#hyperresnet-class)
    

### [HyperXception](https://keras.io/keras_tuner/api/hypermodels/hyper_xception/)

*   [HyperXception class](https://keras.io/keras_tuner/api/hypermodels/hyper_xception/#hyperxception-class)
    

[KerasTuner HyperModels](https://keras.io/keras_tuner/api/hypermodels/#kerastuner-hypermodels)

[The base HyperModel class](https://keras.io/keras_tuner/api/hypermodels/#the-base-hypermodel-class)

[HyperEfficientNet](https://keras.io/keras_tuner/api/hypermodels/#hyperefficientnet)

[HyperImageAugment](https://keras.io/keras_tuner/api/hypermodels/#hyperimageaugment)

[HyperResNet](https://keras.io/keras_tuner/api/hypermodels/#hyperresnet)

[HyperXception](https://keras.io/keras_tuner/api/hypermodels/#hyperxception)