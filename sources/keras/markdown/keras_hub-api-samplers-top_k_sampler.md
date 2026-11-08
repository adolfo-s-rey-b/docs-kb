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
 / TopKSampler

TopKSampler
===========

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/samplers/top_k_sampler.py#L8)

### `TopKSampler` class

Copied!

`keras_hub.samplers.TopKSampler(k=5, seed=None, **kwargs)`

Top-K Sampler class.

This sampler implements top-k search algorithm. Briefly, top-k algorithm randomly selects a token from the tokens of top K probability, with selection chance determined by the probability.

**Arguments**

*   **k**: int, the `k` value of top-k.
*   **seed**: int. The random seed. Defaults to `None`.

**Call arguments**

{{call\_args}}

**Examples**

Copied!

`causal_lm = keras_hub.models.GPT2CausalLM.from_preset("gpt2_base_en")  # Pass by name to compile. causal_lm.compile(sampler="top_k") causal_lm.generate(["Keras is a"])  # Pass by object to compile. sampler = keras_hub.samplers.TopKSampler(k=5, temperature=0.7) causal_lm.compile(sampler=sampler) causal_lm.generate(["Keras is a"])`

* * *

[TopKSampler](https://keras.io/keras_hub/api/samplers/top_k_sampler/#topksampler)

[`TopKSampler` class](https://keras.io/keras_hub/api/samplers/top_k_sampler/#topksampler-class)