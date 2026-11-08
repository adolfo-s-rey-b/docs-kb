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
 / [D-FINE](https://keras.io/keras_hub/api/models/d_fine/)
 / DFineImageConverter

DFineImageConverter
===================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/d_fine/d_fine_image_converter.py#L6)

### `DFineImageConverter` class

Copied!

`keras_hub.layers.DFineImageConverter(     image_size=None,     scale=None,     offset=None,     crop_to_aspect_ratio=True,     pad_to_aspect_ratio=False,     interpolation="bilinear",     antialias=False,     bounding_box_format="yxyx",     data_format=None,     **kwargs )`

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

`DFineImageConverter.from_preset(preset, **kwargs)`

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
| [dfine\_nano\_coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_nano_coco/1) | 3.79M | D-FINE Nano model, the smallest variant in the family, pretrained on the COCO dataset. Ideal for applications where computational resources are limited. |
| [dfine\_small\_coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_small_coco/1) | 10.33M | D-FINE Small model pretrained on the COCO dataset. Offers a balance between performance and computational efficiency. |
| [dfine\_small\_obj2coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_small_obj2coco/1) | 10.33M | D-FINE Small model first pretrained on Objects365 and then fine-tuned on COCO, combining broad feature learning with benchmark-specific adaptation. |
| [dfine\_small\_obj365](https://www.kaggle.com/models/keras/d-fine/keras/dfine_small_obj365/1) | 10.62M | D-FINE Small model pretrained on the large-scale Objects365 dataset, enhancing its ability to recognize a wider variety of objects. |
| [dfine\_medium\_coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_medium_coco/1) | 19.62M | D-FINE Medium model pretrained on the COCO dataset. A solid baseline with strong performance for general-purpose object detection. |
| [dfine\_medium\_obj2coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_medium_obj2coco/1) | 19.62M | D-FINE Medium model using a two-stage training process: pretraining on Objects365 followed by fine-tuning on COCO. |
| [dfine\_medium\_obj365](https://www.kaggle.com/models/keras/d-fine/keras/dfine_medium_obj365/1) | 19.99M | D-FINE Medium model pretrained on the Objects365 dataset. Benefits from a larger and more diverse pretraining corpus. |
| [dfine\_large\_coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_large_coco/1) | 31.34M | D-FINE Large model pretrained on the COCO dataset. Provides high accuracy and is suitable for more demanding tasks. |
| [dfine\_large\_obj2coco\_e25](https://www.kaggle.com/models/keras/d-fine/keras/dfine_large_obj2coco_e25/1) | 31.34M | D-FINE Large model pretrained on Objects365 and then fine-tuned on COCO for 25 epochs. A high-performance model with specialized tuning. |
| [dfine\_large\_obj365](https://www.kaggle.com/models/keras/d-fine/keras/dfine_large_obj365/1) | 31.86M | D-FINE Large model pretrained on the Objects365 dataset for improved generalization and performance on diverse object categories. |
| [dfine\_xlarge\_coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_xlarge_coco/1) | 62.83M | D-FINE X-Large model, the largest COCO-pretrained variant, designed for state-of-the-art performance where accuracy is the top priority. |
| [dfine\_xlarge\_obj2coco](https://www.kaggle.com/models/keras/d-fine/keras/dfine_xlarge_obj2coco/1) | 62.83M | D-FINE X-Large model, pretrained on Objects365 and fine-tuned on COCO, representing the most powerful model in this series for COCO-style tasks. |
| [dfine\_xlarge\_obj365](https://www.kaggle.com/models/keras/d-fine/keras/dfine_xlarge_obj365/1) | 63.35M | D-FINE X-Large model pretrained on the Objects365 dataset, offering maximum performance by leveraging a vast number of object categories during pretraining. |

* * *

[DFineImageConverter](https://keras.io/keras_hub/api/models/d_fine/d_fine_image_converter/#dfineimageconverter)

[`DFineImageConverter` class](https://keras.io/keras_hub/api/models/d_fine/d_fine_image_converter/#dfineimageconverter-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/d_fine/d_fine_image_converter/#frompreset-method)