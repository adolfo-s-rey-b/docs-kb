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
 / SmolVLM2VideoConverter

SmolVLM2VideoConverter
======================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/smolvlm2/smolvlm2_video_converter.py#L18)

### `SmolVLM2VideoConverter` class

Copied!

`keras_hub.layers.SmolVLM2VideoConverter(     max_image_size=512,     size=2048,     num_frames=64,     fps=1,     interpolation="lanczos3",     antialias=True,     **kwargs )`

Video converter for SmolVLM2 models.

This layer processes video inputs by uniformly sampling frames and passing each frame through `SmolVLM2ImageConverter` with `do_image_splitting=False`.

Each frame is resized to `(max_image_size, max_image_size)`, rescaled, and normalized — identical to an unsplit single image.

For a single video, the output is a dict with: - `"pixel_values"`: float32 tensor of shape `(num_frames, max_image_size, max_image_size, 3)`. - `"num_frames"`: int32 scalar. Number of sampled frames. - `"frames_indices"`: int32 tensor of shape `(num_frames,)`. Index of each sampled frame in the input video.

A batch of videos `(batch, T, H, W, 3)` returns the same dict with a leading batch axis on every entry, and a list of videos returns a list of dicts. Videos in a list may differ in shape. Pixel values are uint8 or float32 in `[0, 255]`.

**Arguments**

*   **max\_image\_size**: int. Side length of each frame after resizing. Default 512 (from HF's `max_image_size.longest_edge`).
*   **size**: int. Longest edge for initial resize before squaring. Default 2048 (from HF's `video_sampling.video_size`).
*   **num\_frames**: int. Maximum number of frames to sample. Frames are sampled uniformly over the clip. Default 64 (from HF's `video_sampling.max_frames`).
*   **fps**: int or float. HF's `video_sampling.fps`, kept so the config round-trips. It does not affect sampling or timestamps: `SmolVLM2CausalLMPreprocessor` computes timestamps from the source frame rate in `video_metadata`, and falls back to 24 fps like HF. Default 1.

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/video_converter.py#L35)

### `from_preset` method

Copied!

`SmolVLM2VideoConverter.from_preset(preset, **kwargs)`

Instantiate a `keras_hub.layers.VideoConverter` from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'gemma4_2b_it'`
2.  a Kaggle Models handle like `'kaggle://user/gemma4/keras/gemma4_2b_it'`
3.  a Hugging Face handle like `'hf://google/gemma-4-2b-it'`
4.  a path to a local preset directory like `'./gemma4_2b_it'`

You can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.VideoConverter.from_preset()`, or from a model class like `keras_hub.models.Gemma4VideoConverter.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.

**Examples**

Copied!

`# Load a video converter from a preset. converter = keras_hub.layers.VideoConverter.from_preset(     "hf://google/gemma-4-2b-it" )`

| Preset | Parameters | Description |
| --- | --- | --- |
| [smolvlm2\_256m\_video\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_256m_video_instruct/1) | 256.48M | 256 million parameter SmolVLM2 vision-language model with a 30-layer SmolLM2 text decoder and a 12-layer SigLIP vision encoder (512x512 images). Instruction-tuned for image and video understanding. |
| [smolvlm2\_500m\_video\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_500m_video_instruct/1) | 507.48M | 500 million parameter SmolVLM2 vision-language model with a 32-layer SmolLM2 text decoder and a 12-layer SigLIP vision encoder (512x512 images). Instruction-tuned for image and video understanding. |
| [smolvlm2\_2.2b\_instruct](https://www.kaggle.com/models/keras/smolvlm2/keras/smolvlm2_2.2b_instruct/1) | 2.25B | 2.2 billion parameter SmolVLM2 vision-language model with a 24-layer SmolLM2 text decoder and a 27-layer SigLIP vision encoder (384x384 images). Instruction-tuned for image and video understanding. |

* * *

[SmolVLM2VideoConverter](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_video_converter/#smolvlm2videoconverter)

[`SmolVLM2VideoConverter` class](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_video_converter/#smolvlm2videoconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/smolvlm2/smolvlm2_video_converter/#frompreset-method)