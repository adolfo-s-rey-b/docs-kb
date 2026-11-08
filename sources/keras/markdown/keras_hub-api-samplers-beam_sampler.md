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
 / BeamSampler

BeamSampler
===========

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/samplers/beam_sampler.py#L10)

### `BeamSampler` class

Copied!

`keras_hub.samplers.BeamSampler(num_beams=5, return_all_beams=False, **kwargs)`

Beam Sampler class.

This sampler implements beam search algorithm. At each time-step, beam search keeps the beams (sequences) of the top `num_beams` highest accumulated probabilities, and uses each one of the beams to predict candidate next tokens.

**Arguments**

*   **num\_beams**: int. The number of beams that should be kept at each time-step. `num_beams` should be strictly positive.
*   **return\_all\_beams**: bool. When set to `True`, the sampler will return all beams and their respective probabilities score.

**Call arguments**

{{call\_args}}

**Examples**

Copied!

`causal_lm = keras_hub.models.GPT2CausalLM.from_preset("gpt2_base_en")  # Pass by name to compile. causal_lm.compile(sampler="beam") causal_lm.generate(["Keras is a"])  # Pass by object to compile. sampler = keras_hub.samplers.BeamSampler(num_beams=5) causal_lm.compile(sampler=sampler) causal_lm.generate(["Keras is a"])`

* * *

[BeamSampler](https://keras.io/keras_hub/api/samplers/beam_sampler/#beamsampler)

[`BeamSampler` class](https://keras.io/keras_hub/api/samplers/beam_sampler/#beamsampler-class)