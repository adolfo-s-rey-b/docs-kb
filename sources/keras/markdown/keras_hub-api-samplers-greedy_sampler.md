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
 / GreedySampler

GreedySampler
=============

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/samplers/greedy_sampler.py#L7)

### `GreedySampler` class

Copied!

`keras_hub.samplers.GreedySampler(**kwargs)`

Greedy sampler class.

This sampler is implemented on greedy search, i.e., always picking up the token of the largest probability as the next token.

**Examples**

Copied!

`causal_lm = keras_hub.models.GPT2CausalLM.from_preset("gpt2_base_en")  # Pass by name to compile. causal_lm.compile(sampler="greedy") causal_lm.generate(["Keras is a"])  # Pass by object to compile. sampler = keras_hub.samplers.GreedySampler() causal_lm.compile(sampler=sampler) causal_lm.generate(["Keras is a"])`

* * *

[GreedySampler](https://keras.io/keras_hub/api/samplers/greedy_sampler/#greedysampler)

[`GreedySampler` class](https://keras.io/keras_hub/api/samplers/greedy_sampler/#greedysampler-class)