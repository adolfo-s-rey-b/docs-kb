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
 / MuseGlimmerImageConverter

MuseGlimmerImageConverter
=========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/muse_glimmer/muse_glimmer_image_converter.py#L324)

### `MuseGlimmerImageConverter` class

Copied!

`keras_hub.layers.MuseGlimmerImageConverter(     patch_size=14,     patch_temporal=2,     merge_size=2,     max_image_tokens=4096,     image_mean=None,     image_std=None,     interpolation="lanczos3",     antialias=True,     **kwargs )`

Image preprocessor for MuseGlimmer.

The converter takes one unbatched image. The image has the shape `(height, width, 3)` for `data_format="channels_last"` and `(3, height, width)` for `data_format="channels_first"`. The converter resizes an image to a patch-grid-aligned size. It extracts `patch_size x patch_size` patches. It duplicates each patch along the temporal axis (`patch_temporal`). It flattens each patch to the vector that `MuseGlimmerVisionPatchEmbedder` expects.

**Arguments**

*   **patch\_size**: int. Spatial patch size in pixels. Defaults to `14`.
*   **patch\_temporal**: int. Temporal patch size. Defaults to `2`.
*   **merge\_size**: int. Spatial merge (pixel-shuffle) factor. Defaults to `2`.
*   **max\_image\_tokens**: int. Maximum number of merged vision tokens per image. Defaults to `4096`.
*   **image\_mean**: float, list of floats, or `None`. Per-channel mean in pixel units `[0, 255]`. The converter computes `(image - image_mean) / image_std` in float32. Defaults to `None`.
*   **image\_std**: float, list of floats, or `None`. Per-channel standard deviation in pixel units `[0, 255]`. Set it together with `image_mean`. Defaults to `None`.
*   **interpolation**: string. Resize interpolation method. Defaults to `"lanczos3"`.
*   **antialias**: bool. If `True`, the resize filters the image to avoid aliasing. Defaults to `True`.

**Example**

Convert one image to patches.

Copied!

`converter = keras_hub.layers.MuseGlimmerImageConverter(     patch_size=2, patch_temporal=2, merge_size=1, max_image_tokens=4 ) outputs = converter(np.ones((8, 8, 3), dtype="float32")) outputs["patches"].shape  # (4, 24) outputs["grid_thw"]  # [1, 2, 2]`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/image_converter.py#L287)

### `from_preset` method

Copied!

`MuseGlimmerImageConverter.from_preset(preset, **kwargs)`

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
| [muse\_glimmer\_30b\_assistant](https://www.kaggle.com/models/keras/museglimmer/keras/muse_glimmer_30b_assistant/1) | 2.56B | MuseGlimmer 30B DFlash Assistant model: 5-layer speculative-decoding drafter for the 30B model. Drafts a 16-token block-diffusion denoised block per forward pass, conditioned on the target model's hidden states. This model must NOT be used standalone. It is designed exclusively as a draft model used from the target model's generation loop. |
| [muse\_glimmer\_30b](https://www.kaggle.com/models/keras/museglimmer/keras/muse_glimmer_30b/1) | 29.78B | 30B-parameter dense causal decoder with an attached windowed-attention perception encoder, distilled from Muse Spark for local agentic use. |

* * *

[MuseGlimmerImageConverter](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_image_converter/#museglimmerimageconverter)

[`MuseGlimmerImageConverter` class](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_image_converter/#museglimmerimageconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_image_converter/#frompreset-method)