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
 / [Model Architectures](https://keras.io/keras_hub/api/models/)
 / [MuseGlimmer](https://keras.io/keras_hub/api/models/muse_glimmer/)
 / MuseGlimmerCausalLM model

MuseGlimmerCausalLM model
=========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/muse_glimmer/muse_glimmer_causal_lm.py#L23)

### `MuseGlimmerCausalLM` class

Copied!

`keras_hub.models.MuseGlimmerCausalLM(backbone, preprocessor=None, **kwargs)`

An end-to-end MuseGlimmer model for causal language modeling.

Predicts the next token given previous tokens (and, optionally, interleaved image/video features routed through the backbone's vision encoder). Applies MuseGlimmer's Gemma-style tanh logit softcap, with the extra `output_multiplier` pre-scale: `T * tanh((logits * output_multiplier) / T)`.

**Arguments**

*   **backbone**: A [`keras_hub.models.MuseGlimmerBackbone`](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_backbone#museglimmerbackbone-class)
     instance.
*   **preprocessor**: A [`keras_hub.models.MuseGlimmerCausalLMPreprocessor`](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_causal_lm_preprocessor#museglimmercausallmpreprocessor-class)
     or `None`.

**Example**

Copied!

`muse_glimmer_lm = keras_hub.models.MuseGlimmerCausalLM.from_preset(     "muse_glimmer_30b" )  # Generate text. muse_glimmer_lm.generate("What is Keras?", max_length=64)  # Generate with a different sampler. muse_glimmer_lm.compile(sampler="top_k") muse_glimmer_lm.generate("What is Keras?", max_length=64)  # Speculative decoding with the DFlash assistant. The output matches # plain greedy decoding when the sampler is greedy. assistant = keras_hub.models.MuseGlimmerAssistantCausalLM.from_preset(     "muse_glimmer_30b_assistant" ) muse_glimmer_lm.compile(sampler="greedy") muse_glimmer_lm.generate(     "What is Keras?", max_length=64, assistant_model=assistant )`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`MuseGlimmerCausalLM.from_preset(preset, load_weights=True, **kwargs)`

Instantiate a [`keras_hub.models.Task`](https://keras.io/keras_hub/api/base_classes/task#task-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Task` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from a task specific base class like `keras_hub.models.CausalLM.from_preset()`, or from a model class like `keras_hub.models.BertTextClassifier.from_preset()`. If calling from the a base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, saved weights will be loaded into the model architecture. If `False`, all weights will be randomly initialized.

**Examples**

Copied!

`# Load a Gemma generative task. causal_lm = keras_hub.models.CausalLM.from_preset(     "gemma_2b_en", )  # Load a Bert classification task. model = keras_hub.models.TextClassifier.from_preset(     "bert_base_en",     num_classes=2, )`

| Preset | Parameters | Description |
| --- | --- | --- |
| [muse\_glimmer\_30b\_assistant](https://www.kaggle.com/models/keras/museglimmer/keras/muse_glimmer_30b_assistant/1) | 2.56B | MuseGlimmer 30B DFlash Assistant model: 5-layer speculative-decoding drafter for the 30B model. Drafts a 16-token block-diffusion denoised block per forward pass, conditioned on the target model's hidden states. This model must NOT be used standalone. It is designed exclusively as a draft model used from the target model's generation loop. |
| [muse\_glimmer\_30b](https://www.kaggle.com/models/keras/museglimmer/keras/muse_glimmer_30b/1) | 29.78B | 30B-parameter dense causal decoder with an attached windowed-attention perception encoder, distilled from Muse Spark for local agentic use. |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/muse_glimmer/muse_glimmer_causal_lm.py#L659)

### `generate` method

Copied!

`MuseGlimmerCausalLM.generate(     inputs,     max_length=None,     stop_token_ids="auto",     strip_prompt=False,     assistant_model=None, )`

Generate text, optionally accelerated by a DFlash assistant.

**Arguments**

*   **assistant\_model**: optional [`keras_hub.models.MuseGlimmerAssistantCausalLM`](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_assistant_causal_lm#museglimmerassistantcausallm-class)
    . When set, `generate()` performs DFlash speculative decoding: the assistant drafts a whole candidate block per cycle and this (target) model verifies it in one parallel forward pass via `keras_hub.samplers.SpeculativeSampler`. The assistant's own `block_size - 1` becomes the sampler's `num_speculative_tokens`. A greedy compiled `sampler` gives greedy acceptance. Any other compiled `sampler` becomes the `base_sampler` for rejection sampling. The model tracks the assistant only during the call. It keeps a weak reference to the assistant and the compiled function for the next call. Defaults to `None` (plain autoregressive decoding with the compiled `sampler`).

* * *

### `backbone` property

Copied!

`keras_hub.models.MuseGlimmerCausalLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.MuseGlimmerCausalLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[MuseGlimmerCausalLM model](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_causal_lm/#museglimmercausallm-model)

[`MuseGlimmerCausalLM` class](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_causal_lm/#museglimmercausallm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_causal_lm/#frompreset-method)

[`generate` method](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_causal_lm/#generate-method)

[`backbone` property](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_causal_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_causal_lm/#preprocessor-property)