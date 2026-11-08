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
 / [SmolVLM2](https://keras.io/keras_hub/api/models/smolvlm2/)
 / SmolVLM2ImageConverter

SmolVLM2ImageConverter
======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/smolvlm2/smolvlm2_image_converter.py#L187)

### `SmolVLM2ImageConverter` class

Copied!

`keras_hub.layers.SmolVLM2ImageConverter(     max_image_size=512,     size=2048,     do_image_splitting=True,     interpolation="lanczos3",     antialias=True,     **kwargs )`

Image converter for SmolVLM2 models.

This layer processes images through the same pipeline as HuggingFace's `SmolVLMImageProcessor`:

1.  Resize so the longest edge matches `size` (default 2048).
2.  Snap to multiples of `max_image_size` (default 512).
3.  Split into sub-image crops + a global view.
4.  Rescale and normalize.

The output is a dict with: - `"pixel_values"`: float32 tensor of shape `(num_sub_images, max_image_size, max_image_size, 3)`. - `"rows"`: int. Number of rows of sub-image crops. - `"cols"`: int. Number of columns of sub-image crops.

**Arguments**

*   **max\_image\_size**: int. Side length of each sub-image crop. Default 512 (from HF's `max_image_size.longest_edge`).
*   **size**: int. The longest edge is resized to this before splitting. Default 2048 (from HF's `size.longest_edge`).
*   **do\_image\_splitting**: bool. Whether to split into sub-images. Set `False` for video frames. Default `True`.
*   **interpolation**: str. Resize filter. Default `"lanczos3"`, which matches HF's PIL LANCZOS. `"lanczos5"` and the filters `ops.image.resize` accepts are also supported.
*   **antialias**: bool. Whether to antialias when downsampling. Default `True`.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/image_converter.py#L287)

### `from_preset` method

Copied!

`SmolVLM2ImageConverter.from_preset(preset, **kwargs)`

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
| [smolvlm2\_256m\_video\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_256m_video_instruct/1) | 256.48M | 256 million parameter SmolVLM2 vision-language model with a 30-layer SmolLM2 text decoder and a 12-layer SigLIP vision encoder (512x512 images). Instruction-tuned for image and video understanding. |
| [smolvlm2\_500m\_video\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_500m_video_instruct/1) | 507.48M | 500 million parameter SmolVLM2 vision-language model with a 32-layer SmolLM2 text decoder and a 12-layer SigLIP vision encoder (512x512 images). Instruction-tuned for image and video understanding. |
| [smolvlm2\_2.2b\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_2.2b_instruct/1) | 2.25B | 2.2 billion parameter SmolVLM2 vision-language model with a 24-layer SmolLM2 text decoder and a 27-layer SigLIP vision encoder (384x384 images). Instruction-tuned for image and video understanding. |

* * *

[SmolVLM2ImageConverter](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_image_converter/#smolvlm2imageconverter)

[`SmolVLM2ImageConverter` class](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_image_converter/#smolvlm2imageconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_image_converter/#frompreset-method)