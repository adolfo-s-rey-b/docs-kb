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
 / MuseGlimmerVideoConverter

MuseGlimmerVideoConverter
=========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/muse_glimmer/muse_glimmer_video_converter.py#L81)

### `MuseGlimmerVideoConverter` class

Copied!

`keras_hub.layers.MuseGlimmerVideoConverter(     patch_size=14,     patch_temporal=2,     merge_size=2,     fps=2.0,     source_fps=24.0,     num_frames=96,     max_video_frame_tokens=144,     interpolation="lanczos3",     antialias=True,     image_mean=None,     image_std=None,     **kwargs )`

Video preprocessor for MuseGlimmer.

Per the model card, video is not handled by a distinct encoder. Each frame goes through the same patch/merge pipeline as a still image (see HF's `get_video_features` == `get_image_features` pass-through).

The converter samples about `fps` frames per second, up to `num_frames`, spread evenly across the video, as HF does. A video array has no frame rate, so the converter assumes `source_fps`. To override it for one video, call `converter(video, source_fps=30.0)`.

**Arguments**

*   **patch\_size**: int. Spatial patch size in pixels. Defaults to `14`.
*   **patch\_temporal**: int. Temporal patch size (frames grouped per temporal patch). Defaults to `2`.
*   **merge\_size**: int. Spatial merge factor. Defaults to `2`.
*   **fps**: float. Target number of sampled frames per second of video. Defaults to `2.0`.
*   **source\_fps**: float. Frame rate of the input videos. Defaults to `24.0`.
*   **num\_frames**: int. Maximum number of sampled frames. Defaults to `96`.
*   **max\_video\_frame\_tokens**: int. Maximum merged vision tokens per frame. Defaults to `144`.
*   **image\_mean**: float, list of floats, or `None`. Per-channel mean in pixel units `[0, 255]`. The converter computes `(frame - image_mean) / image_std` in float32. Defaults to `None`.
*   **image\_std**: float, list of floats, or `None`. Per-channel standard deviation in pixel units `[0, 255]`. Set it together with `image_mean`. Defaults to `None`.
*   **interpolation**: string. Resize interpolation method for frames. Defaults to `"lanczos3"`.
*   **antialias**: bool. If `True`, the resize filters each frame to avoid aliasing. Defaults to `True`.

**Example**

Convert one video of 4 frames to patches.

Copied!

`converter = keras_hub.layers.MuseGlimmerVideoConverter(     patch_size=2,     patch_temporal=2,     merge_size=1,     fps=2.0,     source_fps=2.0,     num_frames=4,     max_video_frame_tokens=4, ) outputs = converter(np.ones((4, 8, 8, 3), dtype="float32")) outputs["patches"].shape  # (8, 24) outputs["grid_thw"]  # [2, 2, 2]`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/video_converter.py#L35)

### `from_preset` method

Copied!

`MuseGlimmerVideoConverter.from_preset(preset, **kwargs)`

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
| [muse\_glimmer\_30b\_assistant](https://www.kaggle.com/models/keras/museglimmer/keras/muse_glimmer_30b_assistant/1) | 2.56B | MuseGlimmer 30B DFlash Assistant model: 5-layer speculative-decoding drafter for the 30B model. Drafts a 16-token block-diffusion denoised block per forward pass, conditioned on the target model's hidden states. This model must NOT be used standalone. It is designed exclusively as a draft model used from the target model's generation loop. |
| [muse\_glimmer\_30b](https://www.kaggle.com/models/keras/museglimmer/keras/muse_glimmer_30b/1) | 29.78B | 30B-parameter dense causal decoder with an attached windowed-attention perception encoder, distilled from Muse Spark for local agentic use. |

* * *

[MuseGlimmerVideoConverter](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_video_converter/#museglimmervideoconverter)

[`MuseGlimmerVideoConverter` class](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_video_converter/#museglimmervideoconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/muse_glimmer/muse_glimmer_video_converter/#frompreset-method)