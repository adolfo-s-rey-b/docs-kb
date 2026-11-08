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
 / ContrastiveSampler

ContrastiveSampler
==================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/samplers/contrastive_sampler.py#L9)

### `ContrastiveSampler` class

Copied!

`keras_hub.samplers.ContrastiveSampler(k=5, alpha=0.6, **kwargs)`

Contrastive Sampler class.

This sampler implements contrastive search algorithm. In short, the sampler chooses the token having the max "score" as the next token. The "score" is a weighted sum between token's probability and max similarity against previous tokens. By using this joint score, contrastive sampler reduces the behavior of duplicating seen tokens.

**Arguments**

*   **k**: int, the `k` value of top-k. Next token will be chosen from k tokens.
*   **alpha**: float, the weight of minus max similarity in joint score computation. The larger the value of `alpha`, the score relies more on the similarity than the token probability.

**Call arguments**

{{call\_args}}

**Examples**

Copied!

`causal_lm = keras_hub.models.GPT2CausalLM.from_preset("gpt2_base_en")  # Pass by name to compile. causal_lm.compile(sampler="contrastive") causal_lm.generate(["Keras is a"])  # Pass by object to compile. sampler = keras_hub.samplers.ContrastiveSampler(k=5) causal_lm.compile(sampler=sampler) causal_lm.generate(["Keras is a"])`

* * *

[ContrastiveSampler](https://keras.io/keras_hub/api/samplers/contrastive_sampler/#contrastivesampler)

[`ContrastiveSampler` class](https://keras.io/keras_hub/api/samplers/contrastive_sampler/#contrastivesampler-class)