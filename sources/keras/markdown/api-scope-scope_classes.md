None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Scope classes](https://keras.io/api/scope/scope_classes/)
 [Context Managers](https://keras.io/api/scope/context_managers/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Scope](https://keras.io/api/scope/)
 / Scope classes

Scope classes
=============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/symbolic_scope.py#L5)

### `SymbolicScope` class

Copied!

`keras.SymbolicScope()`

Scope to indicate the symbolic stage.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/stateless_scope.py#L5)

### `StatelessScope` class

Copied!

`keras.StatelessScope(     state_mapping=None, collect_losses=False, initialize_variables=True )`

Scope to prevent any update to Keras Variables.

The values of variables to be used inside the scope should be passed via the `state_mapping` argument, a list of tuples `(k, v)` where `k` is a `Variable` and `v` is the intended value for this variable (a backend tensor).

Updated values can be collected on scope exit via `value = scope.get_current_value(variable)`. No updates will be applied in-place to any variables for the duration of the scope.

**Example**

Copied!

`state_mapping = [(k, ops.ones(k.shape, k.dtype)) for k in model.weights] with keras.StatelessScope(state_mapping) as scope:     outputs = model.some_function(inputs)  # All model variables remain unchanged. Their new values can be # collected via: for k in model.weights:     new_value = scope.get_current_value(k)     print(f"New value for {k}: {new_value})`

* * *

[Scope classes](https://keras.io/api/scope/scope_classes/#scope-classes)

[`SymbolicScope` class](https://keras.io/api/scope/scope_classes/#symbolicscope-class)

[`StatelessScope` class](https://keras.io/api/scope/scope_classes/#statelessscope-class)