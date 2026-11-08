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
 / Errors

Errors
======

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/errors.py#L19)

### `FailedTrialError` class

Copied!

`keras_tuner.errors.FailedTrialError()`

Raise this error to mark a `Trial` as failed.

When this error is raised in a `Trial`, the `Tuner` would not retry the `Trial` but directly mark it as `"FAILED"`.

**Example**

Copied!

`class MyHyperModel(keras_tuner.HyperModel):     def build(self, hp):         # Build the model         ...         if too_slow(model):             # Mark the Trial as "FAILED" if the model is too slow.             raise keras_tuner.FailedTrialError("Model is too slow.")         return model`

* * *

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/errors.py#L43)

### `FatalError` class

Copied!

`keras_tuner.errors.FatalError()`

A fatal error during search to terminate the program.

It is used to terminate the KerasTuner program for errors that need users immediate attention. When this error is raised in a `Trial`, it will not be caught by KerasTuner.

* * *

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/errors.py#L55)

### `FatalValueError` class

Copied!

`keras_tuner.errors.FatalValueError()`

A fatal error during search to terminate the program.

It is a subclass of `FatalError` and `ValueError`.

It is used to terminate the KerasTuner program for errors that need users immediate attention. When this error is raised in a `Trial`, it will not be caught by KerasTuner.

* * *

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/errors.py#L69)

### `FatalTypeError` class

Copied!

`keras_tuner.errors.FatalTypeError()`

A fatal error during search to terminate the program.

It is a subclass of `FatalError` and `TypeError`.

It is used to terminate the KerasTuner program for errors that need users immediate attention. When this error is raised in a `Trial`, it will not be caught by KerasTuner.

* * *

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/errors.py#L83)

### `FatalRuntimeError` class

Copied!

`keras_tuner.errors.FatalRuntimeError()`

A fatal error during search to terminate the program.

It is a subclass of `FatalError` and `RuntimeError`.

It is used to terminate the KerasTuner program for errors that need users immediate attention. When this error is raised in a `Trial`, it will not be caught by KerasTuner.

* * *

[Errors](https://keras.io/keras_tuner/api/errors/#errors)

[`FailedTrialError` class](https://keras.io/keras_tuner/api/errors/#failedtrialerror-class)

[`FatalError` class](https://keras.io/keras_tuner/api/errors/#fatalerror-class)

[`FatalValueError` class](https://keras.io/keras_tuner/api/errors/#fatalvalueerror-class)

[`FatalTypeError` class](https://keras.io/keras_tuner/api/errors/#fataltypeerror-class)

[`FatalRuntimeError` class](https://keras.io/keras_tuner/api/errors/#fatalruntimeerror-class)