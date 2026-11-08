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
 / [DiffusionGemma](https://keras.io/keras_hub/api/models/diffusion_gemma/)
 / DiffusionGemmaImageConverter

DiffusionGemmaImageConverter
============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/diffusion_gemma/diffusion_gemma_image_converter.py#L10)

### `DiffusionGemmaImageConverter` class

Copied!

`keras_hub.layers.DiffusionGemmaImageConverter(     patch_size=16, max_soft_tokens=280, pooling_kernel_size=3, **kwargs )`

Preprocess raw images for Gemma4 vision inputs.

Resizes images using aspect-ratio-preserving scaling to the nearest valid resolution (a multiple of `patch_size * pooling_kernel_size`), then applies optional per-channel rescaling and offset. The output is a dict with keys `"pixel_values"` (the flattened patch tensor) and `"pixel_position_ids"` (2-D (x, y) position indices for each patch).

**Arguments**

*   **patch\_size**: int. Size of each square patch in pixels. Defaults to `16`.
*   **max\_soft\_tokens**: int. Maximum number of pooled soft tokens per image. Controls the target resolution: the image is scaled so that the total number of patches after pooling does not exceed this value. Defaults to `280`.
*   **pooling\_kernel\_size**: int. Spatial pooling kernel size applied after the vision encoder. Used together with `patch_size` to compute valid target dimensions. Defaults to `3`.
*   **\*\*kwargs**: Additional keyword arguments forwarded to [`keras_hub.layers.ImageConverter`](https://keras.io/keras_hub/api/preprocessing_layers/image_converter#imageconverter-class)
    , e.g. `scale`, `offset`.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/image_converter.py#L287)

### `from_preset` method

Copied!

`DiffusionGemmaImageConverter.from_preset(preset, **kwargs)`

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
| [diffusion\_gemma\_26b\_a4b\_it](https://www.kaggle.com/models/keras/diffusion-gemma/keras/diffusion_gemma_26b_a4b_it/1) | 25.82B | DiffusionGemma 26B MoE instruction-tuned model. 25.8B total parameters (3.8B active), 30 layers, 128 experts. |

* * *

[DiffusionGemmaImageConverter](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_image_converter/#diffusiongemmaimageconverter)

[`DiffusionGemmaImageConverter` class](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_image_converter/#diffusiongemmaimageconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/diffusion_gemma/diffusion_gemma_image_converter/#frompreset-method)