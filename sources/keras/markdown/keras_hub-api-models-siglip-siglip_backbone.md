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
 / [SigLIP](https://keras.io/keras_hub/api/models/siglip/)
 / SigLIPBackbone model

SigLIPBackbone model
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/siglip/siglip_backbone.py#L11)

### `SigLIPBackbone` class

Copied!

`keras_hub.models.SigLIPBackbone(vision_encoder, text_encoder, dtype=None, **kwargs)`

SigCLIP core network with hyperparameters.

This backbone implements the base architecture for the Sigmoid loss in the Language-Image Pre-training (SigLIP) model. Unlike standard contrastive learning with softmax normalization, the sigmoid loss operates solely on image-text pairs and does not require a global view of the pairwise similarities for normalization. It includes vision and text encoders. This backbone outputs the final logit scores corresponding to each image and token input.

The default constructor gives a fully customizable, randomly initialized SigLIP model with any number of layers, heads, and embedding dimensions. To load preset architectures and weights, use the `from_preset` constructor.

**Arguments**

*   **vision\_encoder**: The SigLIP vision encoder for encoding the input images.
*   **text\_encoder**: The SigLIP text encoder for encoding the input tokens.
*   **projection\_dim**: int. The size of the projection layer.
*   **dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for the models computations and weights. Note that some computations, such as softmax and layer normalization will always be done a float32 precision regardless of dtype.

**Example**

Copied!

`input_data = {     "images": np.ones(shape=(1, 224, 224, 3), dtype="float32"),     "token_ids": np.ones(shape=(1, 64), dtype="int32"), }  # Pretrained SigLIP model. model = keras_hub.models.SigLIPBackbone.from_preset(     "siglip_base_patch16_224" ) model(input_data)  # Randomly initialized SigLIP model with custom config. vision_encoder = keras_hub.models.SigLIPVisionEncoder(     patch_size=32,     hidden_dim=768,     num_layers=8,     num_heads=8,     intermediate_dim=2048,     image_shape=(384, 384, 3), ) text_encoder = keras_hub.models.SigLIPTextEncoder(     vocabulary_size=32000,     embedding_dim=768,     hidden_dim=768,     num_layers=8,     num_heads=8,     intermediate_dim=2048, ) model = keras_hub.models.SigLIPBackbone(     vision_encoder=vision_encoder,     text_encoder=text_encoder, ) model(input_data)`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/backbone.py#L120)

### `from_preset` method

Copied!

`SigLIPBackbone.from_preset(preset, load_weights=True, **kwargs)`

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
| [siglip\_base\_patch16\_224](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_224/1) | 203.16M | 200 million parameter, image size 224, pre-trained on WebLi. |
| [siglip\_base\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_256/1) | 203.20M | 200 million parameter, image size 256, pre-trained on WebLi. |
| [siglip\_base\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_384/1) | 203.45M | 200 million parameter, image size 384, pre-trained on WebLi. |
| [siglip\_base\_patch16\_512](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_512/1) | 203.79M | 200 million parameter, image size 512, pre-trained on WebLi. |
| [siglip\_base\_patch16\_256\_multilingual](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_256_multilingual/1) | 370.63M | 370 million parameter, image size 256, pre-trained on WebLi. |
| [siglip2\_base\_patch16\_224](https://www.kaggle.com/models/keras/siglip/keras/siglip2_base_patch16_224/1) | 375.19M | 375 million parameter, patch size 16, image size 224, pre-trained on WebLi. |
| [siglip2\_base\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_base_patch16_256/1) | 375.23M | 375 million parameter, patch size 16, image size 256, pre-trained on WebLi. |
| [siglip2\_base\_patch32\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_base_patch32_256/1) | 376.86M | 376 million parameter, patch size 32, image size 256, pre-trained on WebLi. |
| [siglip2\_base\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_base_patch16_384/1) | 376.86M | 376 million parameter, patch size 16, image size 384, pre-trained on WebLi. |
| [siglip\_large\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip_large_patch16_256/1) | 652.15M | 652 million parameter, image size 256, pre-trained on WebLi. |
| [siglip\_large\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip_large_patch16_384/1) | 652.48M | 652 million parameter, image size 384, pre-trained on WebLi. |
| [siglip\_so400m\_patch14\_224](https://www.kaggle.com/models/keras/siglip/keras/siglip_so400m_patch14_224/1) | 877.36M | 877 million parameter, image size 224, shape-optimized version, pre-trained on WebLi. |
| [siglip\_so400m\_patch14\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip_so400m_patch14_384/1) | 877.96M | 877 million parameter, image size 384, shape-optimized version, pre-trained on WebLi. |
| [medsiglip\_900m\_448](https://www.kaggle.com/models/keras/medsiglip/keras/medsiglip_900m_448/1) | 878.30M | A 900 million parameter variant of SigLIP trained to encode medical images and text into a common embedding space. MedSigLIP contains a vision encoder and a text encoder, and supports 448x448 image resolution with up to 64 text tokens. |
| [siglip2\_large\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_large_patch16_256/1) | 881.53M | 881 million parameter, patch size 16, image size 256, pre-trained on WebLi. |
| [siglip2\_large\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_large_patch16_384/1) | 881.86M | 881 million parameter, patch size 16, image size 384, pre-trained on WebLi. |
| [siglip2\_large\_patch16\_512](https://www.kaggle.com/models/keras/siglip/keras/siglip2_large_patch16_512/1) | 882.31M | 882 million parameter, patch size 16, image size 512, pre-trained on WebLi. |
| [siglip\_so400m\_patch16\_256\_i18n](https://www.kaggle.com/models/keras/siglip/keras/siglip_so400m_patch16_256_i18n/1) | 1.13B | 1.1 billion parameter, image size 256, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch14\_224](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch14_224/1) | 1.14B | 1.1 billion parameter, patch size 14, image size 224, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch16_256/1) | 1.14B | 1.1 billion parameter, patch size 16, image size 256, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch14\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch14_384/1) | 1.14B | 1.1 billion parameter, patch size 14, image size 224, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch16_384/1) | 1.14B | 1.1 billion parameter, patch size 16, image size 384, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch16\_512](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch16_512/1) | 1.14B | 1.1 billion parameter, patch size 16, image size 512, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_giant\_opt\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_giant_opt_patch16_256/2) | 1.87B | 1.8 billion parameter, patch size 16, image size 256, pre-trained on WebLi. |
| [siglip2\_giant\_opt\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_giant_opt_patch16_384/1) | 1.87B | 1.8 billion parameter, patch size 16, image size 384, pre-trained on WebLi. |

* * *

[SigLIPBackbone model](https://keras.io/keras_hub/api/models/siglip/siglip_backbone/#siglipbackbone-model)

[`SigLIPBackbone` class](https://keras.io/keras_hub/api/models/siglip/siglip_backbone/#siglipbackbone-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/siglip/siglip_backbone/#frompreset-method)