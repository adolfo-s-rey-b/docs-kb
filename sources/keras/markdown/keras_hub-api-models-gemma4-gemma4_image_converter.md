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
 / [Gemma4](https://keras.io/keras_hub/api/models/gemma4/)
 / Gemma4ImageConverter

Gemma4ImageConverter
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma4/gemma4_image_converter.py#L104)

### `Gemma4ImageConverter` class

Copied!

`keras_hub.layers.Gemma4ImageConverter(     patch_size=16, max_soft_tokens=280, pooling_kernel_size=3, **kwargs )`

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

`Gemma4ImageConverter.from_preset(preset, **kwargs)`

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
| [embedding\_gemma2](https://www.kaggle.com/models/keras/embedding-gemma2/keras/embedding_gemma2/1) | 744.37M | EmbeddingGemma 2: 744M-parameter, 24-layer multimodal embedding model built on Gemma 4. Embeds text, images, video and audio into a 768-dimensional space. |
| [gemma4\_instruct\_2b\_assistant](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_2b_assistant/1) | 77.73M | Gemma 4 E2B MTP Assistant model: 4-layer speculative-decoding assistant for the 2B-it model. Uses Multi-Token Prediction to propose candidate tokens and achieve inference speedups. This model must NOT be used standalone. It is designed exclusively as a draft model to be passed to the target model's generate() method via the assistant\_model argument. |
| [gemma4\_instruct\_4b\_assistant](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_4b_assistant/1) | 77.73M | Gemma 4 E4B MTP Assistant model: 4-layer speculative-decoding assistant for the 4B-it model. Uses Multi-Token Prediction to propose candidate tokens and achieve inference speedups. This model must NOT be used standalone. It is designed exclusively as a draft model to be passed to the target model's generate() method via the assistant\_model argument. |
| [gemma4\_instruct\_26b\_a4b\_assistant](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_26b_a4b_assistant/1) | 412.76M | Gemma 4 26B A4B MTP Assistant model: 4-layer speculative-decoding assistant for the 26B MoE model. Uses Multi-Token Prediction and a standard logit head to propose candidates. This model must NOT be used standalone. It is designed exclusively as a draft model to be passed to the target model's generate() method via the assistant\_model argument. |
| [gemma4\_instruct\_31b\_assistant](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_31b_assistant/1) | 454.71M | Gemma 4 31B MTP Assistant model: 4-layer speculative-decoding assistant for the 31B dense model. Uses Multi-Token Prediction and a standard logit head to propose candidates. This model must NOT be used standalone. It is designed exclusively as a draft model to be passed to the target model's generate() method via the assistant\_model argument. |
| [gemma4\_2b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_2b/2) | 5.10B | Gemma 4 E2B base model: 2.3B effective parameters (5.1B total with Per-Layer Embeddings), 35-layer, audio+vision+text pretrained Gemma4 model. The 'E' denotes effective parameters — PLE gives each decoder layer its own token embedding table, maximizing parameter efficiency for on-device deployment. |
| [gemma4\_instruct\_2b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_2b/2) | 5.10B | Gemma 4 E2B instruction-tuned model: 2.3B effective parameters (5.1B total with Per-Layer Embeddings), 35-layer, audio+vision+text instruction-tuned Gemma4 model. The 'E' denotes effective parameters — PLE gives each decoder layer its own token embedding table, maximizing parameter efficiency for on-device deployment. |
| [gemma4\_4b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_4b/2) | 7.90B | Gemma 4 E4B base model: 4.5B effective parameters (7.9B total with Per-Layer Embeddings), 42-layer, audio+vision+text pretrained Gemma4 model. The 'E' denotes effective parameters — PLE gives each decoder layer its own token embedding table, maximizing parameter efficiency for on-device deployment. |
| [gemma4\_instruct\_4b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_4b/2) | 7.90B | Gemma 4 E4B instruction-tuned model: 4.5B effective parameters (7.9B total with Per-Layer Embeddings), 42-layer, audio+vision+text instruction-tuned Gemma4 model. The 'E' denotes effective parameters — PLE gives each decoder layer its own token embedding table, maximizing parameter efficiency for on-device deployment. |
| [gemma4\_26b\_a4b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_26b_a4b/2) | 26.00B | Gemma 4 26B A4B base model: Mixture-of-Experts (MoE) model with 26B total parameters and only 4B active parameters per forward pass, 30-layer, vision+text pretrained Gemma4 model. The 'A' denotes active parameters — by activating only a 4B subset during inference, this MoE model runs nearly as fast as a dense 4B model. |
| [gemma4\_instruct\_26b\_a4b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_26b_a4b/2) | 26.00B | Gemma 4 26B A4B instruction-tuned model: Mixture-of-Experts (MoE) model with 26B total parameters and only 4B active parameters per forward pass, 30-layer, vision+text instruction-tuned Gemma4 model. The 'A' denotes active parameters — by activating only a 4B subset during inference, this MoE model runs nearly as fast as a dense 4B model. |
| [gemma4\_31b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_31b/2) | 31.00B | Gemma 4 31B base model: 31B parameter, 60-layer, dense vision+text pretrained Gemma4 model. The dense model in the Gemma 4 family, offering maximum quality for deployments where inference speed is less of a constraint. |
| [gemma4\_instruct\_31b](https://www.kaggle.com/models/keras/gemma4/keras/gemma4_instruct_31b/2) | 31.00B | Gemma 4 31B instruction-tuned model: 31B parameter, 60-layer, dense vision+text instruction-tuned Gemma4 model. The dense model in the Gemma 4 family, offering maximum quality for deployments where inference speed is less of a constraint. |

* * *

[Gemma4ImageConverter](https://keras.io/keras_hub/api/models/gemma4/gemma4_image_converter/#gemma4imageconverter)

[`Gemma4ImageConverter` class](https://keras.io/keras_hub/api/models/gemma4/gemma4_image_converter/#gemma4imageconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gemma4/gemma4_image_converter/#frompreset-method)