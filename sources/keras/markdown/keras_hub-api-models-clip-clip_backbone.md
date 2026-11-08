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
 / [CLIP](https://keras.io/keras_hub/api/models/clip/)
 / CLIPBackbone model

CLIPBackbone model
==================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/clip/clip_backbone.py#L10)

### `CLIPBackbone` class

Copied!

`keras_hub.models.CLIPBackbone(     vision_encoder, text_encoder, projection_dim, dtype=None, name=None, **kwargs )`

CLIP core network with hyperparameters.

This backbone implements the base architecture for Contrastive Language-Image Pretraining (CLIP) model. It includes a vision and text encoders and the corresponding projection layers. This backbone will output the final logit scores corresponding to each image and token input. These values are cosine similarities between the corresponding image and text features.

The default constructor gives a fully customizable, randomly initialized CLIP model with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

**Arguments**

*   **vision\_encoder**: The CLIP vision encoder for encoding the input images.
*   **text\_encoder**: The CLIP text encoder for encoding the input tokens.
*   **projection\_dim**: int. The size of the projection layer.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for the models computations and weights. Note that some computations, such as softmax and layer normalization will always be done a float32 precision regardless of dtype.

**Example**

Copied!

`input_data = {     "images": np.ones(shape=(1, 224, 224, 3), dtype="float32"),     "token_ids": np.ones(shape=(1, 12), dtype="int32"), }  # Pretrained CLIP model. model = keras_hub.models.CLIPBackbone.from_preset("clip_vit_base_patch32") model(input_data)  # Randomly initialized CLIP model with custom config. vision_encoder = keras_hub.models.CLIPVisionEncoder(     patch_size=32,     hidden_dim=768,     num_layers=8,     num_heads=8,     intermediate_dim=2048,     image_shape=(384, 384, 3), ) text_encoder = keras_hub.models.CLIPTextEncoder(     vocabulary_size=49408,     embedding_dim=768,     hidden_dim=768,     num_layers=8,     num_heads=8,     intermediate_dim=2048, ) model = keras_hub.models.CLIPBackbone(     vision_encoder=vision_encoder,     text_encoder=text_encoder,     projection_dim=256, ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`CLIPBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [clip\_vit\_base\_patch16](https://www.kaggle.com/models/keras/clip/keras/clip_vit_base_patch16/3) | 149.62M | 150 million parameter, 12-layer for vision and 12-layer for text, patch size of 16, CLIP model. |
| [clip\_vit\_base\_patch32](https://www.kaggle.com/models/keras/clip/keras/clip_vit_base_patch32/3) | 151.28M | 151 million parameter, 12-layer for vision and 12-layer for text, patch size of 32, CLIP model. |
| [clip\_vit\_b\_32\_laion2b\_s34b\_b79k](https://www.kaggle.com/models/keras/clip/keras/clip_vit_b_32_laion2b_s34b_b79k/3) | 151.28M | 151 million parameter, 12-layer for vision and 12-layer for text, patch size of 32, Open CLIP model. |
| [clip\_vit\_large\_patch14](https://www.kaggle.com/models/keras/clip/keras/clip_vit_large_patch14/3) | 427.62M | 428 million parameter, 24-layer for vision and 12-layer for text, patch size of 14, CLIP model. |
| [clip\_vit\_large\_patch14\_336](https://www.kaggle.com/models/keras/clip/keras/clip_vit_large_patch14_336/3) | 427.94M | 428 million parameter, 24-layer for vision and 12-layer for text, patch size of 14, image size of 336, CLIP model. |
| [clip\_vit\_h\_14\_laion2b\_s32b\_b79k](https://www.kaggle.com/models/keras/clip/keras/clip_vit_h_14_laion2b_s32b_b79k/3) | 986.11M | 986 million parameter, 32-layer for vision and 24-layer for text, patch size of 14, Open CLIP model. |
| [clip\_vit\_g\_14\_laion2b\_s12b\_b42k](https://www.kaggle.com/models/keras/clip/keras/clip_vit_g_14_laion2b_s12b_b42k/3) | 1.37B | 1.4 billion parameter, 40-layer for vision and 24-layer for text, patch size of 14, Open CLIP model. |
| [clip\_vit\_bigg\_14\_laion2b\_39b\_b160k](https://www.kaggle.com/models/keras/clip/keras/clip_vit_bigg_14_laion2b_39b_b160k/3) | 2.54B | 2.5 billion parameter, 48-layer for vision and 32-layer for text, patch size of 14, Open CLIP model. |

* * *

[CLIPBackbone model](https://keras.io/keras_hub/api/models/clip/clip_backbone/#clipbackbone-model)

[`CLIPBackbone` class](https://keras.io/keras_hub/api/models/clip/clip_backbone/#clipbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/clip/clip_backbone/#frompreset-method)