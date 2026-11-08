None

[KerasHub: Pretrained Models](https://keras.io/keras_hub/)

[Getting started](https://keras.io/keras_hub/getting_started/)
 [Developer guides](https://keras.io/keras_hub/guides/)
 [API documentation](https://keras.io/keras_hub/api/)
 [Modeling API](https://keras.io/keras_hub/api/base_classes/)
 [Model Architectures](https://keras.io/keras_hub/api/models/)
 [Tokenizers](https://keras.io/keras_hub/api/tokenizers/)
 [Preprocessing Layers](https://keras.io/keras_hub/api/preprocessing_layers/)
 [Modeling Layers](https://keras.io/keras_hub/api/modeling_layers/)
 [Samplers](https://keras.io/keras_hub/api/samplers/)
 [Metrics](https://keras.io/keras_hub/api/metrics/)
 [Pretrained models list](https://keras.io/keras_hub/presets/)

► [KerasHub: Pretrained Models](https://keras.io/keras_hub/)
 / [API documentation](https://keras.io/keras_hub/api/)
 / [Samplers](https://keras.io/keras_hub/api/samplers/)
 / RandomSampler

RandomSampler
=============

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/samplers/random_sampler.py#L8)

### `RandomSampler` class

Copied!

`keras_hub.samplers.RandomSampler(seed=None, **kwargs)`

Random Sampler class.

This sampler implements random sampling. Briefly, random sampler randomly selects a token from the entire distribution of the tokens, with selection chance determined by the probability of each token.

**Arguments**

*   **seed**: int. The random seed. Defaults to `None`.

**Call arguments**

{{call\_args}}

**Examples**

Copied!

`causal_lm = keras_hub.models.GPT2CausalLM.from_preset("gpt2_base_en")  # Pass by name to compile. causal_lm.compile(sampler="random") causal_lm.generate(["Keras is a"])  # Pass by object to compile. sampler = keras_hub.samplers.RandomSampler(temperature=0.7) causal_lm.compile(sampler=sampler) causal_lm.generate(["Keras is a"])`

* * *

[RandomSampler](https://keras.io/keras_hub/api/samplers/random_sampler/#randomsampler)

[`RandomSampler` class](https://keras.io/keras_hub/api/samplers/random_sampler/#randomsampler-class)