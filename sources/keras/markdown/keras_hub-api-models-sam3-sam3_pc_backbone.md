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
 / [Segment Anything Model 3](https://keras.io/keras_hub/api/models/sam3/)
 / SAM3PromptableConceptBackbone model

SAM3PromptableConceptBackbone model
===================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/sam3/sam3_pc_backbone.py#L13)

### `SAM3PromptableConceptBackbone` class

Copied!

`keras_hub.models.SAM3PromptableConceptBackbone(     vision_encoder,     text_encoder,     geometry_encoder,     detr_encoder,     detr_decoder,     mask_decoder,     dtype=None,     **kwargs )`

A backbone for the Segment Anything Model 3 (SAM3).

SAM3 is a multi-modal model that supports text and geometry prompts (boxes) to perform object segmentation. It consists of a vision encoder, a text encoder, a geometry encoder for processing box prompts, and a DETR-based encoder-decoder architecture to fuse multi-modal features and predict segmentation masks.

**Arguments**

*   **vision\_encoder**: `keras_hub.layers.SAM3VisionEncoder`. A feature extractor for the input images.
*   **text\_encoder**: `keras_hub.layers.SAM3TextEncoder`. A Keras layer to compute embeddings for text prompts.
*   **geometry\_encoder**: `keras_hub.layers.SAM3GeometryEncoder`. A Keras layer to compute embeddings for geometry (box) prompts.
*   **detr\_encoder**: `keras_hub.layers.SAM3DetrEncoder`. A transformer-based encoder that fuses vision and prompt features.
*   **detr\_decoder**: `keras_hub.layers.SAM3DetrDecoder`. A transformer-based decoder that predicts object queries.
*   **mask\_decoder**: `keras_hub.layers.SAM3MaskDecoder`. A Keras layer to generate segmentation masks given the object queries and fused features.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for the models computations and weights. Note that some computations, such as softmax and layer normalization will always be done in float32 precision regardless of dtype. Defaults to `bfloat16`.

**Example**

Copied!

`import numpy as np import keras_hub  vision_encoder = keras_hub.layers.SAM3VisionEncoder(     image_shape=(224, 224, 3),     patch_size=14,     num_layers=2,     hidden_dim=32,     intermediate_dim=128,     num_heads=2,     fpn_hidden_dim=32,     fpn_scale_factors=[4.0, 2.0, 1.0, 0.5],     pretrain_image_shape=(112, 112, 3),     window_size=2,     global_attn_indexes=[1, 2], ) text_encoder = keras_hub.layers.SAM3TextEncoder(     vocabulary_size=1024,     embedding_dim=32,     hidden_dim=32,     num_layers=2,     num_heads=2,     intermediate_dim=128, ) geometry_encoder = keras_hub.layers.SAM3GeometryEncoder(     num_layers=3,     hidden_dim=32,     intermediate_dim=128,     num_heads=2,     roi_size=7, ) detr_encoder = keras_hub.layers.SAM3DetrEncoder(     num_layers=3,     hidden_dim=32,     intermediate_dim=128,     num_heads=2, ) detr_decoder = keras_hub.layers.SAM3DetrDecoder(     image_shape=(224, 224, 3),     patch_size=14,     num_layers=2,     hidden_dim=32,     intermediate_dim=128,     num_heads=2,     num_queries=100, ) mask_decoder = keras_hub.layers.SAM3MaskDecoder(     num_upsampling_stages=3,     hidden_dim=32,     num_heads=2, ) backbone = keras_hub.models.SAM3PromptableConceptBackbone(     vision_encoder=vision_encoder,     text_encoder=text_encoder,     geometry_encoder=geometry_encoder,     detr_encoder=detr_encoder,     detr_decoder=detr_decoder,     mask_decoder=mask_decoder, ) input_data = {     "pixel_values": np.ones((2, 224, 224, 3), dtype="float32"),     "token_ids": np.ones((2, 32), dtype="int32"),     "padding_mask": np.ones((2, 32), dtype="bool"),     "boxes": np.zeros((2, 1, 5), dtype="float32"),     "box_labels": np.zeros((2, 1), dtype="int32"), } outputs = backbone(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`SAM3PromptableConceptBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [sam3\_pcs](https://www.kaggle.com/models/keras/sam3/keras/sam3_pcs/1) | 30.00M | 30 million parameter Promptable Concept Segmentation (PCS) SAM model. |

* * *

[SAM3PromptableConceptBackbone model](https://keras.io/keras_hub/api/models/sam3/sam3_pc_backbone/#sam3promptableconceptbackbone-model)

[`SAM3PromptableConceptBackbone` class](https://keras.io/keras_hub/api/models/sam3/sam3_pc_backbone/#sam3promptableconceptbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/sam3/sam3_pc_backbone/#frompreset-method)