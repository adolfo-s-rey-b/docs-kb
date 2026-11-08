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
 / BayesianOptimization Tuner

BayesianOptimization Tuner
==========================

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/tuners/bayesian.py#L307)

### `BayesianOptimization` class

Copied!

`keras_tuner.BayesianOptimization(     hypermodel=None,     objective=None,     max_trials=10,     num_initial_points=None,     alpha=0.0001,     beta=2.6,     seed=None,     hyperparameters=None,     tune_new_entries=True,     allow_new_entries=True,     max_retries_per_trial=0,     max_consecutive_failed_trials=3,     **kwargs )`

BayesianOptimization tuning with Gaussian process.

**Arguments**

*   **hypermodel**: Instance of `HyperModel` class (or callable that takes hyperparameters and returns a `Model` instance). It is optional when `Tuner.run_trial()` is overridden and does not use `self.hypermodel`.
*   **objective**: A string, [`keras_tuner.Objective`](https://keras.io/keras_tuner/api/tuners/objective#objective-class)
     instance, or a list of [`keras_tuner.Objective`](https://keras.io/keras_tuner/api/tuners/objective#objective-class)
    s and strings. If a string, the direction of the optimization (min or max) will be inferred. If a list of [`keras_tuner.Objective`](https://keras.io/keras_tuner/api/tuners/objective#objective-class)
    , we will minimize the sum of all the objectives to minimize subtracting the sum of all the objectives to maximize. The `objective` argument is optional when `Tuner.run_trial()` or `HyperModel.fit()` returns a single float as the objective to minimize.
*   **max\_trials**: Integer, the total number of trials (model configurations) to test at most. Note that the oracle may interrupt the search before `max_trial` models have been tested if the search space has been exhausted. Defaults to 10.
*   **num\_initial\_points**: Optional number of randomly generated samples as initial training data for Bayesian optimization. If left unspecified, a value of 3 times the dimensionality of the hyperparameter space is used.
*   **alpha**: Float, the value added to the diagonal of the kernel matrix during fitting. It represents the expected amount of noise in the observed performances in Bayesian optimization. Defaults to 1e-4.
*   **beta**: Float, the balancing factor of exploration and exploitation. The larger it is, the more explorative it is. Defaults to 2.6.
*   **seed**: Optional integer, the random seed.
*   **hyperparameters**: Optional `HyperParameters` instance. Can be used to override (or register in advance) hyperparameters in the search space.
*   **tune\_new\_entries**: Boolean, whether hyperparameter entries that are requested by the hypermodel but that were not specified in `hyperparameters` should be added to the search space, or not. If not, then the default value for these parameters will be used. Defaults to True.
*   **allow\_new\_entries**: Boolean, whether the hypermodel is allowed to request hyperparameter entries not listed in `hyperparameters`. Defaults to True.
*   **max\_retries\_per\_trial**: Integer. Defaults to 0. The maximum number of times to retry a `Trial` if the trial crashed or the results are invalid.
*   **max\_consecutive\_failed\_trials**: Integer. Defaults to 3. The maximum number of consecutive failed `Trial`s. When this number is reached, the search will be stopped. A `Trial` is marked as failed when none of the retries succeeded.
*   **\*\*kwargs**: Keyword arguments relevant to all `Tuner` subclasses. Please see the docstring for `Tuner`.

* * *

[BayesianOptimization Tuner](https://keras.io/keras_tuner/api/tuners/bayesian/#bayesianoptimization-tuner)

[`BayesianOptimization` class](https://keras.io/keras_tuner/api/tuners/bayesian/#bayesianoptimization-class)