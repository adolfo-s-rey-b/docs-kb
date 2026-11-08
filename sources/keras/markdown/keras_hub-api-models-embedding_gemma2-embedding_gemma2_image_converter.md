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
 / [EmbeddingGemma2](https://keras.io/keras_hub/api/models/embedding_gemma2/)
 / EmbeddingGemma2ImageConverter

EmbeddingGemma2ImageConverter
=============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/embedding_gemma2/embedding_gemma2_image_converter.py#L10)

### `EmbeddingGemma2ImageConverter` class

Copied!

`keras_hub.layers.EmbeddingGemma2ImageConverter(     patch_size=16, max_soft_tokens=280, pooling_kernel_size=3, **kwargs )`

EmbeddingGemma2 image converter.

This converter is a subclass of `Gemma4ImageConverter` and shares the same functionality.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/image_converter.py#L287)

### `from_preset` method

Copied!

`EmbeddingGemma2ImageConverter.from_preset(preset, **kwargs)`

Instantiate a [`keras_hub.layers.ImageConverter`](https://keras.io/keras_hub/api/preprocessing_layers/image_converter#imageconverter-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'pali_gemma_3b_224'`
2.  a Kaggle Models handle like `'kaggle://user/paligemma/keras/pali_gemma_3b_224'`
3.  a Hugging Face handle like `'hf://user/pali_gemma_3b_224'`
4.  a path to a local preset directory like `'./pali_gemma_3b_224'`

You can run `cls.presets.keys()` to list all built-in presets available on the class.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

``batch = np.random.randint(0, 256, size=(2, 512, 512, 3))  # Resize images for `"pali_gemma_3b_224"`. converter = keras_hub.layers.ImageConverter.from_preset(     "pali_gemma_3b_224" ) converter(batch) # # Output shape (2, 224, 224, 3)  # Resize images for `"pali_gemma_3b_448"` without cropping. converter = keras_hub.layers.ImageConverter.from_preset(     "pali_gemma_3b_448",     crop_to_aspect_ratio=False, ) converter(batch) # # Output shape (2, 448, 448, 3)``

| Preset | Parameters | Description |
| --- | --- | --- |
| [embedding\_gemma2](https://www.kaggle.com/models/keras/embedding-gemma2/keras/embedding_gemma2/1) | 744.37M | EmbeddingGemma 2: 744M-parameter, 24-layer multimodal embedding model built on Gemma 4. Embeds text, images, video and audio into a 768-dimensional space. |

* * *

[EmbeddingGemma2ImageConverter](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_image_converter/#embeddinggemma2imageconverter)

[`EmbeddingGemma2ImageConverter` class](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_image_converter/#embeddinggemma2imageconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/embedding_gemma2/embedding_gemma2_image_converter/#frompreset-method)