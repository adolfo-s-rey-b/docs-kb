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
 / [Blip2](https://keras.io/keras_hub/api/models/blip2/)
 / BLIP2Backbone model

BLIP2Backbone model
===================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/blip2/blip2_backbone.py#L7)

### `BLIP2Backbone` class

Copied!

`keras_hub.models.BLIP2Backbone(     vision_encoder, qformer, language_model, dtype=None, **kwargs )`

BLIP-2 core network.

BLIP-2 is a vision-language model that connects a frozen image encoder and a frozen large language model (LLM) through a lightweight trainable Querying Transformer (Q-Former). The Q-Former distills visual information into a fixed number of query embeddings which are then fed as a soft visual prompt to the language model.

The forward pass follows three stages: 1. A `BLIP2VisionEncoder` (ViT) maps raw images to patch features. 2. A `BLIP2QFormer` cross-attends learned query tokens against those patch features and produces a compact set of visual embeddings. 3. A language model (OPT or Flan-T5) receives the query embeddings prepended to its token sequence and generates text.

When `vision_encoder` is `None` the backbone operates in text-only mode: the Q-Former is bypassed and the language model receives only token ids.

For a higher-level text-generation interface see [`keras_hub.models.BLIP2CausalLM`](https://keras.io/keras_hub/api/models/blip2/blip2_causal_lm#blip2causallm-class)
.

**Arguments**

*   **vision\_encoder**: A `keras_hub.models.BLIP2VisionEncoder` instance. Pass `None` for a text-only backbone.
*   **qformer**: A `keras_hub.models.BLIP2QFormer` instance. Pass `None` when `vision_encoder` is `None`.
*   **language\_model**: The language model instance (e.g. `BLIP2CustomOPT` or `BLIP2FlanT5`).
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. Dtype used for model computations and weights. Defaults to `None` (Keras global default).
*   **\*\*kwargs**: Additional keyword arguments forwarded to the base `Backbone` / [`keras.Model`](https://keras.io/api/models/model#model-class)
    .

**Example**

Copied!

`# Text-only (no vision encoder) backbone = keras_hub.models.BLIP2Backbone(     vision_encoder=None,     qformer=None,     language_model=my_opt, ) output = backbone({"token_ids": token_ids, "padding_mask": mask})  # Full vision-language backbone backbone = keras_hub.models.BLIP2Backbone.from_preset("blip2_opt_2.7b") output = backbone({     "images": images,           # (B, H, W, 3)     "token_ids": token_ids,     # (B, seq_len)     "padding_mask": mask,       # (B, seq_len) })`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`BLIP2Backbone.from_preset(preset, load_weights=True, **kwargs)`

Instantiate a [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as a one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a ModelScope handle like `'modelscope://user/bert_base_en'`
5.  a path to a local preset directory like `'./bert_base_en'`

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.Backbone.from_preset()`, or from a model class like `keras_hub.models.GemmaBackbone.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

For any `Backbone` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

`# Load a Gemma backbone with pre-trained weights. model = keras_hub.models.Backbone.from_preset(     "gemma_2b_en", )  # Load a Bert backbone with a pre-trained config and random weights. model = keras_hub.models.Backbone.from_preset(     "bert_base_en",     load_weights=False, )`

| Preset | Parameters | Description |
| --- | --- | --- |
| [blip2\_opt\_2.7b](https://www.kaggle.com/models/keras/blip2/keras/blip2_opt_2.7b/1) | 3.74B | BLIP-2 model using OPT-2.7B as the frozen language model. |
| [blip2\_flan\_t5\_xl](https://www.kaggle.com/models/keras/blip2/keras/blip2_flan_t5_xl/1) | 3.94B | BLIP-2 model using Flan-T5-XL (~3B) as the frozen language model. |
| [blip2\_opt\_6.7b](https://www.kaggle.com/models/keras/blip2/keras/blip2_opt_6.7b/1) | 7.75B | BLIP-2 model using OPT-6.7B as the frozen language model. |
| [blip2\_flan\_t5\_xxl](https://www.kaggle.com/models/keras/blip2/keras/blip2_flan_t5_xxl/1) | 12.23B | BLIP-2 model using Flan-T5-XXL (~11B) as the frozen language model. |

* * *

[BLIP2Backbone model](https://keras.io/keras_hub/api/models/blip2/blip2_backbone/#blip2backbone-model)

[`BLIP2Backbone` class](https://keras.io/keras_hub/api/models/blip2/blip2_backbone/#blip2backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/blip2/blip2_backbone/#frompreset-method)