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
 / MuseGlimmerAssistantCausalLM model

MuseGlimmerAssistantCausalLM model
==================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/muse_glimmer/muse_glimmer_assistant_causal_lm.py#L10)

### `MuseGlimmerAssistantCausalLM` class

Copied!

`keras_hub.models.MuseGlimmerAssistantCausalLM(     backbone, block_size=16, mask_token_id=None, **kwargs )`

A DFlash block-diffusion drafter for speculative decoding.

Drafts an entire `block_size`\-token block of denoised hidden states in one forward pass, conditioned on hidden states pulled from several layers of the separate, larger MuseGlimmer target model. The target model then verifies the block in parallel. Origin: DFlash (arXiv:2602.06036).

Unlike a standard causal-LM drafter, this model has no vocabulary and no LM head. It predicts continuous denoised block hidden states, not discrete tokens. It must NOT be used standalone — `call()` and `generate_step()` both raise `NotImplementedError`. Pass this model as `assistant_model` to `keras_hub.models.MuseGlimmerCausalLM.generate()` for end-to-end speculative decoding — that path calls `call_with_cache()`, which persists the context stream across drafting cycles (matches `modeling_muse_glimmer_assistant.py`'s real `forward()`, which is likewise always called with a real `DFlashCache` from the actual speculative-decoding driver, `DFlashTokenCandidateGenerator.get_candidates()` — its cache-free mode exists on the base class but is never exercised in practice).

**Arguments**

*   **backbone**: A [`keras_hub.models.MuseGlimmerBackbone`](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_backbone#museglimmerbackbone-class)
     configured with the drafter's own dimensions and `use_bidirectional_attention=True`, `context_projection_layer_ids` set to the target model's `target_layer_ids`, `use_external_embeddings=True`, `enable_qk_scale_and_gate=False`, `qk_norm_with_scale=True`, `use_sandwich_norm=False`, and `use_centered_norm=False`.
*   **block\_size**: int. Number of denoised-block positions drafted per forward pass. Defaults to `16`.
*   **mask\_token\_id**: int. Token id used to fill the noise/mask positions of the block, one anchor token followed by `block_size - 1` copies of this id, before embedding via the target model's own token embedding table. Required for speculative decoding via `MuseGlimmerCausalLM.generate(assistant_model=...)`.

**Example**

Copied!

`target = keras_hub.models.MuseGlimmerCausalLM.from_preset(     "muse_glimmer_30b" ) assistant = keras_hub.models.MuseGlimmerAssistantCausalLM.from_preset(     "muse_glimmer_30b_assistant" ) # The assistant drafts each block. The target verifies the block. target.generate(     "What is Keras?", max_length=64, assistant_model=assistant )`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`MuseGlimmerAssistantCausalLM.from_preset(preset, load_weights=True, **kwargs)`

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

### `backbone` property

Copied!

`keras_hub.models.MuseGlimmerAssistantCausalLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

[MuseGlimmerAssistantCausalLM model](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_assistant_causal_lm/#museglimmerassistantcausallm-model)

[`MuseGlimmerAssistantCausalLM` class](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_assistant_causal_lm/#museglimmerassistantcausallm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_assistant_causal_lm/#frompreset-method)

[`backbone` property](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_assistant_causal_lm/#backbone-property)