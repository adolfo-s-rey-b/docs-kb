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
 / TopPSampler

TopPSampler
===========

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/samplers/top_p_sampler.py#L8)

### `TopPSampler` class

Copied!

`keras_hub.samplers.TopPSampler(p=0.1, k=None, seed=None, **kwargs)`

Top-P Sampler class.

This sampler implements top-p search algorithm. Top-p search selects tokens from the smallest subset of output probabilities that sum to greater than `p`. Put in another way, top-p will first order token predictions by likelihood, and ignore all tokens after the cumulative probability of selected tokens exceeds `p`, then select a token from the remaining tokens.

**Arguments**

*   **p**: float, the `p` value of top-p.
*   **k**: int. If set, this argument defines a heuristic "top-k" cutoff applied before the "top-p" sampling. All logits not in the top `k` will be discarded, and the remaining logits will be sorted to find a cutoff point for `p`. Setting this arg can significantly speed sampling up by reducing the number of tokens to sort. Defaults to `None`.
*   **seed**: int. The random seed. Defaults to `None`.

**Call arguments**

{{call\_args}}

**Examples**

Copied!

`causal_lm = keras_hub.models.GPT2CausalLM.from_preset("gpt2_base_en")  # Pass by name to compile. causal_lm.compile(sampler="top_p") causal_lm.generate(["Keras is a"])  # Pass by object to compile. sampler = keras_hub.samplers.TopPSampler(p=0.1, k=1_000) causal_lm.compile(sampler=sampler) causal_lm.generate(["Keras is a"])`

* * *

[TopPSampler](https://keras.io/keras_hub/api/samplers/top_p_sampler/#toppsampler)

[`TopPSampler` class](https://keras.io/keras_hub/api/samplers/top_p_sampler/#toppsampler-class)