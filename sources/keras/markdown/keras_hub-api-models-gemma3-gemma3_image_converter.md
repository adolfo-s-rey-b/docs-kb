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
 / [Gemma3](https://keras.io/keras_hub/api/models/gemma3/)
 / Gemma3ImageConverter

Gemma3ImageConverter
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma3/gemma3_image_converter.py#L6)

### `Gemma3ImageConverter` class

Copied!

`keras_hub.layers.Gemma3ImageConverter(**kwargs)`

Preprocess raw images into model ready inputs.

This class converts from raw images to model ready inputs. This conversion proceeds in the following steps:

1.  Resize the image using to `image_size`. If `image_size` is `None`, this step will be skipped.
2.  Rescale the image by multiplying by `scale`, which can be either global or per channel. If `scale` is `None`, this step will be skipped.
3.  Offset the image by adding `offset`, which can be either global or per channel. If `offset` is `None`, this step will be skipped.

The layer will take as input a raw image tensor in the channels last or channels first format, and output a preprocessed image input for modeling. This tensor can be batched (rank 4), or unbatched (rank 3).

This layer can be used with the `from_preset()` constructor to load a layer that will rescale and resize an image for a specific pretrained model. Using the layer this way allows writing preprocessing code that does not need updating when switching between model checkpoints.

**Arguments**

*   **image\_size**: `(int, int)` tuple or `None`. The output size of the image, not including the channels axis. If `None`, the input will not be resized.
*   **scale**: float, tuple of floats, or `None`. The scale to apply to the inputs. If `scale` is a single float, the entire input will be multiplied by `scale`. If `scale` is a tuple, it's assumed to contain per-channel scale value multiplied against each channel of the input images. If `scale` is `None`, no scaling is applied.
*   **offset**: float, tuple of floats, or `None`. The offset to apply to the inputs. If `offset` is a single float, the entire input will be summed with `offset`. If `offset` is a tuple, it's assumed to contain per-channel offset value summed against each channel of the input images. If `offset` is `None`, no scaling is applied.
*   **crop\_to\_aspect\_ratio**: If `True`, resize the images without aspect ratio distortion. When the original aspect ratio differs from the target aspect ratio, the output image will be cropped so as to return the largest possible window in the image (of size `(height, width)`) that matches the target aspect ratio. By default (`crop_to_aspect_ratio=False`), aspect ratio may not be preserved.
*   **interpolation**: String, the interpolation method. Supports `"bilinear"`, `"nearest"`, `"bicubic"`, `"lanczos3"`, `"lanczos5"`. Defaults to `"bilinear"`.
*   **antialias**: Whether to use an antialiasing filter when downsampling an image. Defaults to `False`.
*   **bounding\_box\_format**: A string specifying the format of the bounding boxes, one of `"xyxy"`, `"rel_xyxy"`, `"xywh"`, `"center_xywh"`, `"yxyx"`, `"rel_yxyx"`. Specifies the format of the bounding boxes which will be resized to `image_size` along with the image. To pass bounding boxed to this layer, pass a dict with keys `"images"` and `"bounding_boxes"` when calling the layer.
*   **data\_format**: String, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`.

**Examples**

Copied!

`# Resize raw images and scale them to [0, 1]. converter = keras_hub.layers.ImageConverter(     image_size=(128, 128),     scale=1. / 255, ) converter(np.random.randint(0, 256, size=(2, 512, 512, 3)))  # Resize images to the specific size needed for a PaliGemma preset. converter = keras_hub.layers.ImageConverter.from_preset(     "pali_gemma_3b_224" ) converter(np.random.randint(0, 256, size=(2, 512, 512, 3)))`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/image_converter.py#L287)

### `from_preset` method

Copied!

`Gemma3ImageConverter.from_preset(preset, **kwargs)`

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
| [gemma3\_270m](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_270m/3) | 268.10M | 270-million parameter(170m embedding,100m transformer params) model, 18-layer, text-only designed for hyper-efficient AI, particularly for task-specific fine-tuning. |
| [gemma3\_instruct\_270m](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_270m/4) | 268.10M | 270-million parameter(170m embedding,100m transformer params) model, 18-layer, text-only,instruction-tuned model designed for hyper-efficient AI, particularly for task-specific fine-tuning. |
| [function\_gemma\_instruct\_270m](https://www.kaggle.com/models/keras/function-gemma/keras/function_gemma_instruct_270m/1) | 268.10M | A 270M Million parameter text-only model based on Gemma 3. This model is trained specifically for function calling improvements. |
| [harrier\_embedding\_oss\_270m](https://www.kaggle.com/models/keras/harrier/keras/harrier_embedding_oss_270m/1) | 268.10M | Microsoft harrier-oss-v1 270M multilingual text embedding model based on the Gemma3-270M architecture, fine-tuned for dense retrieval and semantic similarity across 94+ languages. Achieves 66.5 on Multilingual MTEB v2. |
| [embedding\_gemma3\_300m](https://www.kaggle.com/models/keras/embeddinggemma/keras/embedding_gemma3_300m/2) | 307.58M | Embedding-focused Gemma 3 model (300M parameters, 24 layers). |
| [gemma3\_1b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_1b/3) | 999.89M | 1 billion parameter, 26-layer, text-only pretrained Gemma3 model. |
| [gemma3\_instruct\_1b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_1b/3) | 999.89M | 1 billion parameter, 26-layer, text-only instruction-tuned Gemma3 model. |
| [gemma3\_4b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_4b_text/2) | 3.88B | 4 billion parameter, 34-layer, text-only pretrained Gemma3 model. |
| [gemma3\_instruct\_4b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_4b_text/3) | 3.88B | 4 billion parameter, 34-layer, text-only instruction-tuned Gemma3 model. |
| [gemma3\_4b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_4b/1) | 4.30B | 4 billion parameter, 34-layer, vision+text pretrained Gemma3 model. |
| [gemma3\_instruct\_4b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_4b/1) | 4.30B | 4 billion parameter, 34-layer, vision+text instruction-tuned Gemma3 model. |
| [translategemma\_4b\_it](https://www.kaggle.com/models/keras/translategemma/keras/translategemma_4b_it/1) | 4.30B | 4 billion parameter, 34-layer, multimodal instruction-tuned translation model based on Gemma 3. Supports text and image input for translation across 55 languages. |
| [medgemma\_4b](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_4b/1) | 4.30B | A 4 billion parameter model based on Gemma 3. This model is pre-trained for performance on medical text and image comprehension and is optimized for medical applications that involve a text generation component. |
| [medgemma\_instruct\_4b](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_instruct_4b/1) | 4.30B | A 4 billion parameter model based on Gemma 3. This model is instruction-tuned for performance on medical text and image comprehension and is optimized for medical applications that involve a text generation component. |
| [medgemma\_1.5\_instruct\_4b](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_1.5_instruct_4b/1) | 4.30B | A 4 billion parameter,Instruct-tuned MedGemma 1.5 4B is an updated version of the Instruction-tuned MedGemma 4B model. |
| [gemma3\_12b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_12b_text/3) | 11.77B | 12 billion parameter, 48-layer, text-only pretrained Gemma3 model. |
| [gemma3\_instruct\_12b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_12b_text/3) | 11.77B | 12 billion parameter, 48-layer, text-only instruction-tuned Gemma3 model. |
| [gemma3\_12b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_12b/2) | 12.19B | 12 billion parameter, 48-layer, vision+text pretrained Gemma3 model. |
| [gemma3\_instruct\_12b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_12b/2) | 12.19B | 12 billion parameter, 48-layer, vision+text instruction-tuned Gemma3 model. |
| [translategemma\_12b\_it](https://www.kaggle.com/models/keras/translategemma/keras/translategemma_12b_it/1) | 12.19B | 12 billion parameter, 48-layer, multimodal instruction-tuned translation model based on Gemma 3. Supports text and image input for translation across 55 languages. |
| [gemma3\_27b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_27b_text/4) | 27.01B | 27 billion parameter, 62-layer, text-only pretrained Gemma3 model. |
| [gemma3\_instruct\_27b\_text](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_27b_text/3) | 27.01B | 27 billion parameter, 62-layer, text-only instruction-tuned Gemma3 model. |
| [medgemma\_instruct\_27b\_text](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_instruct_27b_text/1) | 27.01B | A 27 billion parameter text-only model based on Gemma 3. This model is instruction-tuned (No images) for performance on medical text comprehension and is optimized for medical applications that involve a text generation component. |
| [gemma3\_27b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_27b/2) | 27.43B | 27 billion parameter, 62-layer, vision+text pretrained Gemma3 model. |
| [gemma3\_instruct\_27b](https://www.kaggle.com/models/keras/gemma3/keras/gemma3_instruct_27b/2) | 27.43B | 27 billion parameter, 62-layer, vision+text instruction-tuned Gemma3 model. |
| [translategemma\_27b\_it](https://www.kaggle.com/models/keras/translategemma/keras/translategemma_27b_it/1) | 27.43B | 27 billion parameter, 62-layer, multimodal instruction-tuned translation model based on Gemma 3. Supports text and image input for translation across 55 languages. |
| [medgemma\_instruct\_27b](https://www.kaggle.com/models/keras/medgemma/keras/medgemma_instruct_27b/1) | 27.43B | A 27 billion parameter model based on Gemma 3. This model is instruction-tuned for performance on medical text and image comprehension and is optimized for medical applications that involve a text generation component. |

* * *

[Gemma3ImageConverter](https://keras.io/keras_hub/api/models/gemma3/gemma3_image_converter/#gemma3imageconverter)

[`Gemma3ImageConverter` class](https://keras.io/keras_hub/api/models/gemma3/gemma3_image_converter/#gemma3imageconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gemma3/gemma3_image_converter/#frompreset-method)