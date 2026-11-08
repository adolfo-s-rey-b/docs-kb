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
 / [Mistral3](https://keras.io/keras_hub/api/models/mistral3/)
 / Mistral3ImageConverter

Mistral3ImageConverter
======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/mistral3/mistral3_image_converter.py#L208)

### `Mistral3ImageConverter` class

Copied!

`keras_hub.layers.Mistral3ImageConverter(     longest_edge=1540,     patch_size=14,     spatial_merge_size=2,     image_mean=None,     image_std=None,     rescale_factor=None,     **kwargs )`

Converts raw images into `Mistral3Backbone`'s multimodal inputs.

Each image is resized so its longest edge is at most `longest_edge` pixels (aspect ratio preserved), then rounded up to a `patch_size` multiple, matching HF's `PixtralImageProcessor`. Since every image in a call can resize to a different shape, resizing runs in a Python loop over `inputs` (a list of variable-size images) rather than through the base class's single-`Resizing`\-layer `call()`.

The TensorFlow path ([`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
) resizes every image in a call to one shape. A dense batch tensor has one image size, so this path needs batches of same-size images. The Python path resizes each image on its own and pads the batch to the largest image.

**Arguments**

*   **longest\_edge**: int. The maximum size of an image's longer side after resizing. Defaults to `1540`.
*   **patch\_size**: int. The vision encoder's patch size. Defaults to `14`.
*   **spatial\_merge\_size**: int. The number of patches merged together per side by the multimodal projector's patch merger. Resized image dimensions are rounded up to a multiple of `patch_size * spatial_merge_size`. Defaults to `2`.
*   **image\_mean**: list of 3 floats or `None`. The per-channel mean, in `[0, 1]` pixel units. Defaults to the CLIP mean.
*   **image\_std**: list of 3 floats or `None`. The per-channel standard deviation, in `[0, 1]` pixel units. Defaults to the CLIP standard deviation.
*   **rescale\_factor**: float or `None`. The factor that maps `[0, 255]` pixels to `[0, 1]`. Defaults to `1 / 255`.

The converter normalizes with `(x - mean / rescale_factor) / (std / rescale_factor)` in `float32`. HF's `PixtralImageProcessor` uses the same arithmetic, so the output pixels are identical.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/image_converter.py#L287)

### `from_preset` method

Copied!

`Mistral3ImageConverter.from_preset(preset, **kwargs)`

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
| [ministral\_3\_3b\_base\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_3b_base_2512_en/1) | 3.85B | 3 billion parameter, 26-layer, pretrained Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_3b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_3b_instruct_2512_en/1) | 3.85B | 3 billion parameter, 26-layer, instruction-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_3b\_reasoning\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_3b_reasoning_2512_en/1) | 3.85B | 3 billion parameter, 26-layer, reasoning-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [shieldstral\_1.0\_3b\_en](https://www.kaggle.com/models/keras/shieldstral/keras/shieldstral_1.0_3b_en/1) | 3.85B | 3 billion parameter, 26-layer Shieldstral model with a Pixtral vision encoder. The model checks text and image content against a safety policy written in natural language. The model returns one safety score for each input. |
| [ministral\_3\_8b\_base\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_8b_base_2512_en/1) | 8.92B | 8 billion parameter, 34-layer, pretrained Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_8b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_8b_instruct_2512_en/1) | 8.92B | 8 billion parameter, 34-layer, instruction-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_8b\_reasoning\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_8b_reasoning_2512_en/1) | 8.92B | 8 billion parameter, 34-layer, reasoning-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_14b\_base\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_14b_base_2512_en/1) | 13.95B | 14 billion parameter, 40-layer, pretrained Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_14b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_14b_instruct_2512_en/1) | 13.95B | 14 billion parameter, 40-layer, instruction-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [ministral\_3\_14b\_reasoning\_2512\_en](https://www.kaggle.com/models/keras/ministral3/keras/ministral_3_14b_reasoning_2512_en/1) | 13.95B | 14 billion parameter, 40-layer, reasoning-tuned Ministral 3 model with a Pixtral vision encoder for image input. |
| [mistral\_small\_3.1\_24b\_base\_2503\_en](https://www.kaggle.com/models/keras/mistral3/keras/mistral_small_3.1_24b_base_2503_en/1) | 24.01B | 24 billion parameter, 40-layer, pretrained Mistral3 model with a Pixtral vision encoder for image input. |
| [mistral\_small\_3.1\_24b\_instruct\_2503\_en](https://www.kaggle.com/models/keras/mistral3/keras/mistral_small_3.1_24b_instruct_2503_en/1) | 24.01B | 24 billion parameter, 40-layer, instruction-tuned Mistral3 model with a Pixtral vision encoder for image input. |
| [mistral\_small\_3.2\_24b\_instruct\_2506\_en](https://www.kaggle.com/models/keras/mistral3/keras/mistral_small_3.2_24b_instruct_2506_en/1) | 24.01B | 24 billion parameter, 40-layer, instruction-tuned Mistral3 model with a Pixtral vision encoder for image input. An updated version of mistral\_small\_3.1\_24b\_instruct\_2503\_en with improved instruction-following and reduced repetition. |
| [devstral\_small\_2\_24b\_instruct\_2512\_en](https://www.kaggle.com/models/keras/devstral2/keras/devstral_small_2_24b_instruct_2512_en/1) | 24.01B | 24 billion parameter, 40-layer, instruction-tuned Devstral Small 2 model for agentic software engineering, with a Pixtral vision encoder for image input. |
| [magistral\_small\_2509\_en](https://www.kaggle.com/models/keras/magistral/keras/magistral_small_2509_en/1) | 24.01B | 24 billion parameter, 40-layer, reasoning-tuned Magistral Small model with a Pixtral vision encoder for image input. |

* * *

[Mistral3ImageConverter](https://keras.io/keras_hub/api/models/mistral3/mistral3_image_converter/#mistral3imageconverter)

[`Mistral3ImageConverter` class](https://keras.io/keras_hub/api/models/mistral3/mistral3_image_converter/#mistral3imageconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/mistral3/mistral3_image_converter/#frompreset-method)