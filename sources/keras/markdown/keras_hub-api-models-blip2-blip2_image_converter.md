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
 / BLIP2ImageConverter

BLIP2ImageConverter
===================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/blip2/blip2_image_converter.py#L6)

### `BLIP2ImageConverter` class

Copied!

`keras_hub.layers.BLIP2ImageConverter(     image_size=(224, 224),     crop_to_aspect_ratio=False,     interpolation="bicubic",     antialias=True,     **kwargs )`

A preprocessing layer for images used by the BLIP-2 model.

This converter resizes, normalizes, and rescales images to the format expected by the BLIP-2 vision encoder (EVA-CLIP). Preprocessing is always performed in float32 regardless of the global Keras dtype policy.

Preprocessing steps: 1. **Resizing**: Images are stretched to `(224, 224)` (default) using antialiased bicubic interpolation, matching HuggingFace's `BlipImageProcessor` (a plain resize, no aspect-ratio crop). 2. **Normalization**: Pixel values are normalized using EVA-CLIP channel statistics (mean and standard deviation per channel).

**Arguments**

*   **image\_size**: `(int, int)` tuple or `None`. The output spatial size of the image, not including the channels axis. Defaults to `(224, 224)`.
*   **crop\_to\_aspect\_ratio**: bool. If `True`, resize without aspect ratio distortion. Defaults to `False` to match HuggingFace, which stretches the image to the target size.
*   **interpolation**: string. The interpolation method used during resizing. Defaults to `"bicubic"`.
*   **antialias**: bool. Whether to use an antialiasing filter when downsampling. Defaults to `True` to match HuggingFace's PIL bicubic resize.
*   **\*\*kwargs**: Standard Keras layer arguments.

**Example**

Copied!

`converter = keras_hub.layers.BLIP2ImageConverter() images = np.random.randint(0, 256, (1, 500, 500, 3)) processed = converter(images)  # shape: (1, 224, 224, 3)`

**References**

*   [Li et al., 2023](https://arxiv.org/abs/2301.12597)
    

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/image_converter.py#L287)

### `from_preset` method

Copied!

`BLIP2ImageConverter.from_preset(preset, **kwargs)`

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
| [blip2\_opt\_2.7b](https://www.kaggle.com/models/keras/blip2/keras/blip2_opt_2.7b/1) | 3.74B | BLIP-2 model using OPT-2.7B as the frozen language model. |
| [blip2\_flan\_t5\_xl](https://www.kaggle.com/models/keras/blip2/keras/blip2_flan_t5_xl/1) | 3.94B | BLIP-2 model using Flan-T5-XL (~3B) as the frozen language model. |
| [blip2\_opt\_6.7b](https://www.kaggle.com/models/keras/blip2/keras/blip2_opt_6.7b/1) | 7.75B | BLIP-2 model using OPT-6.7B as the frozen language model. |
| [blip2\_flan\_t5\_xxl](https://www.kaggle.com/models/keras/blip2/keras/blip2_flan_t5_xxl/1) | 12.23B | BLIP-2 model using Flan-T5-XXL (~11B) as the frozen language model. |

* * *

[BLIP2ImageConverter](https://keras.io/keras_hub/api/models/blip2/blip2_image_converter/#blip2imageconverter)

[`BLIP2ImageConverter` class](https://keras.io/keras_hub/api/models/blip2/blip2_image_converter/#blip2imageconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/blip2/blip2_image_converter/#frompreset-method)