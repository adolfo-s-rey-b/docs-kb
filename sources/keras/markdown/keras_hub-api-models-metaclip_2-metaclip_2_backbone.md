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
 / [MetaCLIP 2](https://keras.io/keras_hub/api/models/metaclip_2/)
 / MetaCLIP2Backbone model

MetaCLIP2Backbone model
=======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/metaclip_2/metaclip_2_backbone.py#L14)

### `MetaCLIP2Backbone` class

Copied!

`keras_hub.models.MetaCLIP2Backbone(     vision_encoder, text_encoder, projection_dim, dtype=None, name=None, **kwargs )`

MetaCLIP 2 core network with hyperparameters.

This backbone implements the base architecture for Meta's Contrastive Language-Image Pretraining 2 (MetaCLIP 2) model. It includes a vision and text encoder along with corresponding projection layers. This backbone will output the final logit scores corresponding to each image and token input. These values are cosine similarities between the corresponding image and text features.

MetaCLIP 2 uses the same architecture as CLIP but is trained on a larger and more diverse dataset using improved data curation techniques. It uses `quick_gelu` activation by default.

The default constructor gives a fully customizable, randomly initialized MetaCLIP 2 model with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

**Arguments**

*   **vision\_encoder**: The MetaCLIP 2 vision encoder for encoding input images.
*   **text\_encoder**: The MetaCLIP 2 text encoder for encoding input tokens.
*   **projection\_dim**: int. The size of the projection layer.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for the models computations and weights. Note that some computations, such as softmax and layer normalization will always be done at float32 precision regardless of dtype.

**Example**

Copied!

`input_data = {     "images": np.ones(shape=(1, 224, 224, 3), dtype="float32"),     "token_ids": np.ones(shape=(1, 77), dtype="int32"), }  # Pretrained MetaCLIP 2 model. model = keras_hub.models.MetaCLIP2Backbone.from_preset(     "metaclip_2_vit_huge_patch14_224" ) model(input_data)  # Randomly initialized MetaCLIP 2 model with custom config. vision_encoder = keras_hub.models.MetaCLIP2VisionEncoder(     patch_size=14,     hidden_dim=1280,     num_layers=32,     num_heads=16,     intermediate_dim=5120,     image_shape=(224, 224, 3), ) text_encoder = keras_hub.models.MetaCLIP2TextEncoder(     vocabulary_size=901629,     embedding_dim=1024,     hidden_dim=1024,     num_layers=24,     num_heads=16,     intermediate_dim=4096, ) model = keras_hub.models.MetaCLIP2Backbone(     vision_encoder=vision_encoder,     text_encoder=text_encoder,     projection_dim=1024, ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`MetaCLIP2Backbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [metaclip\_2\_vit\_huge\_patch14\_224](https://www.kaggle.com/models/keras/metaclip2/keras/metaclip_2_vit_huge_patch14_224/1) | 1.86B | 2 billion parameter, 32-layer for vision and 24-layer for text, patch size of 14, image resolution 224x224. MetaCLIP 2 worldwide huge model (ViT-H-14-quickgelu-worldwide) trained on 29B seen pairs with QuickGELU activation. |
| [metaclip\_2\_vit\_huge\_patch14\_378](https://www.kaggle.com/models/keras/metaclip2/keras/metaclip_2_vit_huge_patch14_378/1) | 1.86B | 2 billion parameter, 32-layer for vision and 24-layer for text, patch size of 14, image resolution 378x378. MetaCLIP 2 worldwide huge model (ViT-H-14-378-worldwide) trained on 29B seen pairs. |
| [metaclip\_2\_vit\_giant\_patch14\_224](https://www.kaggle.com/models/keras/metaclip2/keras/metaclip_2_vit_giant_patch14_224/1) | 3.63B | 4 billion parameter, 40-layer for vision and 24-layer for text, patch size of 14, image resolution 224x224. MetaCLIP 2 worldwide giant model (ViT-bigG-14-worldwide) trained on 29B seen pairs. |
| [metaclip\_2\_vit\_giant\_patch14\_378](https://www.kaggle.com/models/keras/metaclip2/keras/metaclip_2_vit_giant_patch14_378/1) | 3.63B | 4 billion parameter, 40-layer for vision and 24-layer for text, patch size of 14, image resolution 378x378. MetaCLIP 2 worldwide giant model (ViT-bigG-14-378-worldwide) trained on 29B seen pairs. |

* * *

[MetaCLIP2Backbone model](https://keras.io/keras_hub/api/models/metaclip_2/metaclip_2_backbone/#metaclip2backbone-model)

[`MetaCLIP2Backbone` class](https://keras.io/keras_hub/api/models/metaclip_2/metaclip_2_backbone/#metaclip2backbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/metaclip_2/metaclip_2_backbone/#frompreset-method)