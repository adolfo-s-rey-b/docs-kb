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
 / [Tuners](https://keras.io/keras_tuner/api/tuners/)
 / Hyperband Tuner

Hyperband Tuner
===============

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/tuners/hyperband.py#L332)

### `Hyperband` class

Copied!

`keras_tuner.Hyperband(     hypermodel=None,     objective=None,     max_epochs=100,     factor=3,     hyperband_iterations=1,     seed=None,     hyperparameters=None,     tune_new_entries=True,     allow_new_entries=True,     max_retries_per_trial=0,     max_consecutive_failed_trials=3,     **kwargs )`

Variation of HyperBand algorithm.

**Reference**

Li, Lisha, and Kevin Jamieson. ["Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization." Journal of Machine Learning Research 18 (2018): 1-52](http://jmlr.org/papers/v18/16-558.html)
.

**Arguments**

*   **hypermodel**: Instance of `HyperModel` class (or callable that takes hyperparameters and returns a `Model` instance). It is optional when `Tuner.run_trial()` is overriden and does not use `self.hypermodel`.
*   **objective**: A string, [`keras_tuner.Objective`](https://keras.io/keras_tuner/api/tuners/objective#objective-class)
     instance, or a list of [`keras_tuner.Objective`](https://keras.io/keras_tuner/api/tuners/objective#objective-class)
    s and strings. If a string, the direction of the optimization (min or max) will be inferred. If a list of [`keras_tuner.Objective`](https://keras.io/keras_tuner/api/tuners/objective#objective-class)
    , we will minimize the sum of all the objectives to minimize subtracting the sum of all the objectives to maximize. The `objective` argument is optional when `Tuner.run_trial()` or `HyperModel.fit()` returns a single float as the objective to minimize.
*   **max\_epochs**: Integer, the maximum number of epochs to train one model. It is recommended to set this to a value slightly higher than the expected epochs to convergence for your largest Model, and to use early stopping during training (for example, via [`tf.keras.callbacks.EarlyStopping`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/EarlyStopping)
    ). Defaults to 100.
*   **factor**: Integer, the reduction factor for the number of epochs and number of models for each bracket. Defaults to 3.
*   **hyperband\_iterations**: Integer, at least 1, the number of times to iterate over the full Hyperband algorithm. One iteration will run approximately `max_epochs * (math.log(max_epochs, factor) ** 2)` cumulative epochs across all trials. It is recommended to set this to as high a value as is within your resource budget. Defaults to 1.
*   **seed**: Optional integer, the random seed.
*   **hyperparameters**: Optional HyperParameters instance. Can be used to override (or register in advance) hyperparameters in the search space.
*   **tune\_new\_entries**: Boolean, whether hyperparameter entries that are requested by the hypermodel but that were not specified in `hyperparameters` should be added to the search space, or not. If not, then the default value for these parameters will be used. Defaults to True.
*   **allow\_new\_entries**: Boolean, whether the hypermodel is allowed to request hyperparameter entries not listed in `hyperparameters`. Defaults to True.
*   **max\_retries\_per\_trial**: Integer. Defaults to 0. The maximum number of times to retry a `Trial` if the trial crashed or the results are invalid.
*   **max\_consecutive\_failed\_trials**: Integer. Defaults to 3. The maximum number of consecutive failed `Trial`s. When this number is reached, the search will be stopped. A `Trial` is marked as failed when none of the retries succeeded.
*   **\*\*kwargs**: Keyword arguments relevant to all `Tuner` subclasses. Please see the docstring for `Tuner`.

* * *

[Hyperband Tuner](https://keras.io/keras_tuner/api/tuners/hyperband/#hyperband-tuner)

[`Hyperband` class](https://keras.io/keras_tuner/api/tuners/hyperband/#hyperband-class)