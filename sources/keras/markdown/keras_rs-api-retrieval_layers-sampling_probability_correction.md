None

[KerasRS](https://keras.io/keras_rs/)

[API documentation](https://keras.io/keras_rs/api/)
 [Embedding Layers](https://keras.io/keras_rs/api/embedding_layers/)
 [Feature Interaction Layers](https://keras.io/keras_rs/api/feature_interaction_layers/)
 [Retrieval Layers](https://keras.io/keras_rs/api/retrieval_layers/)
 [Losses](https://keras.io/keras_rs/api/losses/)
 [Metrics](https://keras.io/keras_rs/api/metrics/)
 [Examples](https://keras.io/keras_rs/examples/)

► [KerasRS](https://keras.io/keras_rs/)
 / [API documentation](https://keras.io/keras_rs/api/)
 / [Retrieval Layers](https://keras.io/keras_rs/api/retrieval_layers/)
 / SamplingProbabilityCorrection layer

SamplingProbabilityCorrection layer
===================================

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/retrieval/sampling_probability_correction.py#L10)

### `SamplingProbabilityCorrection` class

Copied!

`keras_rs.layers.SamplingProbabilityCorrection(epsilon: float = 1e-06, **kwargs: Any)`

Sampling probability correction.

Corrects the logits to reflect the sampling probability of negatives.

**Arguments**

*   **epsilon**: float. Small float added to sampling probability to avoid taking the log of zero. Defaults to 1e-6.
*   **\*\*kwargs**: Args to pass to the base class.

**Example**

Copied!

`# Create the layer. sampling_probability_correction = (     keras_rs.layers.SamplingProbabilityCorrection() )  # Correct the logits based on the provided candidate sampling probability. logits = sampling_probability_correction(logits, probabilities)`

* * *

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/retrieval/sampling_probability_correction.py#L39)

### `call` method

Copied!

`SamplingProbabilityCorrection.call(logits: Any, candidate_sampling_probability: Any)`

Corrects input logits to account for candidate sampling probability.

**Arguments**

*   **logits**: The logits tensor to correct, typically `[batch_size, num_candidates]` but can have more dimensions or be 1D as `[num_candidates]`.
*   **candidate\_sampling\_probability**: The sampling probability with the same shape as `logits`.

**Returns**

The corrected logits with the same shape as the input logits.

* * *

[SamplingProbabilityCorrection layer](https://keras.io/keras_rs/api/retrieval_layers/sampling_probability_correction/#samplingprobabilitycorrection-layer)

[`SamplingProbabilityCorrection` class](https://keras.io/keras_rs/api/retrieval_layers/sampling_probability_correction/#samplingprobabilitycorrection-class)

[`call` method](https://keras.io/keras_rs/api/retrieval_layers/sampling_probability_correction/#call-method)