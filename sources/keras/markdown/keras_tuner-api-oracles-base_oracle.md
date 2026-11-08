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
 / [Oracles](https://keras.io/keras_tuner/api/oracles/)
 / The base Oracle class

The base Oracle class
=====================

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/engine/oracle.py#L251)

### `Oracle` class

Copied!

`keras_tuner.Oracle(     objective=None,     max_trials=None,     hyperparameters=None,     allow_new_entries=True,     tune_new_entries=True,     seed=None,     max_retries_per_trial=0,     max_consecutive_failed_trials=3, )`

Implements a hyperparameter optimization algorithm.

In a parallel tuning setting, there is only one `Oracle` instance. The workers would communicate with the centralized `Oracle` instance with gPRC calls to the `Oracle` methods.

`Trial` objects are often used as the communication packet through the gPRC calls to pass information between the worker `Tuner` instances and the `Oracle`. For example, `Oracle.create_trial()` returns a `Trial` object, and `Oracle.end_trial()` accepts a `Trial` in its arguments.

New copies of the same `Trial` instance are reconstructed as it going through the gRPC calls. The changes to the `Trial` objects in the worker `Tuner`s are synced to the original copy in the `Oracle` when they are passed back to the `Oracle` by calling `Oracle.end_trial()`.

**Arguments**

*   **objective**: A string, [`keras_tuner.Objective`](https://keras.io/keras_tuner/api/tuners/objective#objective-class)
     instance, or a list of [`keras_tuner.Objective`](https://keras.io/keras_tuner/api/tuners/objective#objective-class)
    s and strings. If a string, the direction of the optimization (min or max) will be inferred. If a list of [`keras_tuner.Objective`](https://keras.io/keras_tuner/api/tuners/objective#objective-class)
    , we will minimize the sum of all the objectives to minimize subtracting the sum of all the objectives to maximize. The `objective` argument is optional when `Tuner.run_trial()` or `HyperModel.fit()` returns a single float as the objective to minimize.
*   **max\_trials**: Integer, the total number of trials (model configurations) to test at most. Note that the oracle may interrupt the search before `max_trial` models have been tested if the search space has been exhausted.
*   **hyperparameters**: Optional `HyperParameters` instance. Can be used to override (or register in advance) hyperparameters in the search space.
*   **tune\_new\_entries**: Boolean, whether hyperparameter entries that are requested by the hypermodel but that were not specified in `hyperparameters` should be added to the search space, or not. If not, then the default value for these parameters will be used. Defaults to True.
*   **allow\_new\_entries**: Boolean, whether the hypermodel is allowed to request hyperparameter entries not listed in `hyperparameters`. Defaults to True.
*   **seed**: Int. Random seed.
*   **max\_retries\_per\_trial**: Integer. Defaults to 0. The maximum number of times to retry a `Trial` if the trial crashed or the results are invalid.
*   **max\_consecutive\_failed\_trials**: Integer. Defaults to 3. The maximum number of consecutive failed `Trial`s. When this number is reached, the search will be stopped. A `Trial` is marked as failed when none of the retries succeeded.

* * *

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/engine/oracle.py#L91)

### `wrapped_func` function

Copied!

`keras_tuner.Oracle.create_trial()`

* * *

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/engine/oracle.py#L91)

### `wrapped_func` function

Copied!

`keras_tuner.Oracle.end_trial()`

* * *

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/engine/oracle.py#L663)

### `get_best_trials` method

Copied!

`Oracle.get_best_trials(num_trials=1)`

Returns the best `Trial`s.

* * *

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/engine/oracle.py#L692)

### `get_state` method

Copied!

`Oracle.get_state()`

Returns the current state of this object.

This method is called during `save`.

**Returns**

A dictionary of serializable objects as the state.

* * *

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/engine/oracle.py#L714)

### `set_state` method

Copied!

`Oracle.set_state(state)`

Sets the current state of this object.

This method is called during `reload`.

**Arguments**

*   **state**: A dictionary of serialized objects as the state to restore.

* * *

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/engine/oracle.py#L423)

### `score_trial` method

Copied!

`Oracle.score_trial(trial)`

Score a completed `Trial`.

This method can be overridden in subclasses to provide a score for a set of hyperparameter values. This method is called from `end_trial` on completed `Trial`s.

**Arguments**

*   **trial**: A completed `Trial` object.

* * *

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/engine/oracle.py#L395)

### `populate_space` method

Copied!

`Oracle.populate_space(trial_id)`

Fill the hyperparameter space with values for a trial.

This method should be overridden in subclasses and called in `create_trial` in order to populate the hyperparameter space with values.

**Arguments**

*   **trial\_id**: A string, the ID for this Trial.

**Returns**

A dictionary with keys "values" and "status", where "values" is a mapping of parameter names to suggested values, and "status" should be one of "RUNNING" (the trial can start normally), "IDLE" (the oracle is waiting on something and cannot create a trial), or "STOPPED" (the oracle has finished searching and no new trial should be created).

* * *

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/engine/oracle.py#L91)

### `wrapped_func` function

Copied!

`keras_tuner.Oracle.update_trial()`

* * *

[The base Oracle class](https://keras.io/keras_tuner/api/oracles/base_oracle/#the-base-oracle-class)

[`Oracle` class](https://keras.io/keras_tuner/api/oracles/base_oracle/#oracle-class)

[`wrapped_func` function](https://keras.io/keras_tuner/api/oracles/base_oracle/#wrappedfunc-function)

[`wrapped_func` function](https://keras.io/keras_tuner/api/oracles/base_oracle/#wrappedfunc-function)

[`get_best_trials` method](https://keras.io/keras_tuner/api/oracles/base_oracle/#getbesttrials-method)

[`get_state` method](https://keras.io/keras_tuner/api/oracles/base_oracle/#getstate-method)

[`set_state` method](https://keras.io/keras_tuner/api/oracles/base_oracle/#setstate-method)

[`score_trial` method](https://keras.io/keras_tuner/api/oracles/base_oracle/#scoretrial-method)

[`populate_space` method](https://keras.io/keras_tuner/api/oracles/base_oracle/#populatespace-method)

[`wrapped_func` function](https://keras.io/keras_tuner/api/oracles/base_oracle/#wrappedfunc-function)