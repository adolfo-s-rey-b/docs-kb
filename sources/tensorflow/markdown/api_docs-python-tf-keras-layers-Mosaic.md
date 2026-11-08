[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FMosaic&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#output-shape)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#references)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#methods)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#from_config)
        
    *   [get\_random\_transformation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#get_random_transformation)
        
    *   [transform\_bounding\_boxes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#transform_bounding_boxes)
        
    *   [transform\_images](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#transform_images)
        
    *   [transform\_labels](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#transform_labels)
        
    *   [transform\_segmentation\_masks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#transform_segmentation_masks)
        
    *   [transform\_single\_bounding\_box](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#transform_single_bounding_box)
        
    *   [transform\_single\_image](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#transform_single_image)
        
    *   [transform\_single\_label](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#transform_single_label)
        
    *   [transform\_single\_segmentation\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#transform_single_segmentation_mask)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Mosaic Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#output-shape)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#references)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#methods)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#from_config)
        
    *   [get\_random\_transformation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#get_random_transformation)
        
    *   [transform\_bounding\_boxes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#transform_bounding_boxes)
        
    *   [transform\_images](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#transform_images)
        
    *   [transform\_labels](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#transform_labels)
        
    *   [transform\_segmentation\_masks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#transform_segmentation_masks)
        
    *   [transform\_single\_bounding\_box](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#transform_single_bounding_box)
        
    *   [transform\_single\_image](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#transform_single_image)
        
    *   [transform\_single\_label](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#transform_single_label)
        
    *   [transform\_single\_segmentation\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#transform_single_segmentation_mask)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Mosaic#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/master/keras/src/layers/preprocessing/image_preprocessing/mosaic.py#L16-L416)

Mosaic implements the Mosaic data augmentation technique.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Mosaic(
        offset=(0.25, 0.75),
        seed=None,
        bounding_box_format=None,
        data_format=None,
        **kwargs
    )

For every image in the batch, Mosaic picks 3 other images at random from the same batch and arranges the 4 images in a 2x2 grid. A crop the size of a single image is then taken from the grid around a randomly sampled mosaic center, so that each output image contains a piece of each of the 4 images.

Labels are mixed in proportion to the area that each of the 4 images covers in the output. Bounding boxes are moved along with their images and clipped to the output image; boxes that end up entirely outside of it get a label of `-1`. Segmentation masks are cropped exactly like the images.

A single (unbatched) image is processed as a batch of one image. All 4 images of its grid are then that same image, so the output is the image shifted with wrap-around. To combine different images, call the layer on batches, for example after [`tf.data.Dataset.batch()`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#batch)
.

|     |
| --- |
| Input shape<br>----------- |     |
| A 3D (unbatched) or 4D (batched) tensor of images, or a dictionary with an `"images"` key and optional `"labels"`, `"bounding_boxes"` and `"segmentation_masks"` keys. Batched images have shape `(batch, height, width, channels)` in `"channels_last"` format, or `(batch, channels, height, width)` in `"channels_first"` format. Labels have shape `(batch, num_classes)`, or `(num_classes,)` for a single image, and segmentation masks have the same layout as the images. |     |

|     |
| --- |
| Output shape<br>------------ |     |
| Same as the input, except that each image's bounding boxes become 4 times as many, since an output image can contain boxes from 4 images. |     |

|     |
| --- |
| References<br>---------- |     |
| *   [YOLOv4 paper](https://arxiv.org/abs/2004.10934)<br>    .<br>*   [YOLOv5 implementation](https://github.com/ultralytics/yolov5)<br>    .<br>*   [YOLOX implementation](https://github.com/Megvii-BaseDetection/YOLOX)<br>    . |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `offset` | A float or a tuple of two floats in the range `[0, 1]`. Controls where the mosaic center can be placed, as a fraction of the image width and height measured from the top-left corner. If a tuple `(lower, upper)` is passed, the x and y coordinates of the center are each sampled uniformly between `lower` and `upper`. If a single float is passed, they are sampled between `0.0` and that value. To always use the same center, pass two identical values, for example `(0.5, 0.5)`. Defaults to `(0.25, 0.75)`. |
| `seed` | Integer. Used to create a random seed. |
| `bounding_box_format` | A string specifying the format of the bounding boxes, for example `"xyxy"`. Required if bounding boxes are passed to the layer. Defaults to `None`. |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |
| `**kwargs` | Base layer keyword arguments, such as `name` and `dtype`. |

#### Example:

(images, labels), _ = keras.datasets.cifar10.load_data()
    images, labels = images[:8], labels[:8]
    labels = keras.ops.cast(keras.ops.one_hot(labels.flatten(), 10), "float32")
    mosaic = keras.layers.Mosaic(seed=42)
    output = mosaic({"images": images, "labels": labels})

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `convert_weight`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/layers/preprocessing/data_layer.py#L153-L159)

convert_weight(
        weight
    )

Convert the weight if it is from the a different backend.

### `from_config`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/ops/operation.py#L329-L369)

@classmethod

Creates an operation from its config.

This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.

if "dtype" in config and isinstance(config["dtype"], dict):
        policy = dtype_policies.deserialize(config["dtype"])

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of `get_config`. |

|     |
| --- |
| Returns |     |
| An operation instance. |     |

### `get_random_transformation`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/layers/preprocessing/image_preprocessing/mosaic.py#L163-L233)

get_random_transformation(
        data, training=True, seed=None
    )

### `transform_bounding_boxes`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/layers/preprocessing/image_preprocessing/mosaic.py#L338-L405)

transform_bounding_boxes(
        bounding_boxes, transformation, training=True
    )

### `transform_images`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L64-L70)

transform_images(
        images, transformation, training=True
    )

### `transform_labels`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/layers/preprocessing/image_preprocessing/mosaic.py#L235-L274)

transform_labels(
        labels, transformation, training=True
    )

### `transform_segmentation_masks`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L83-L90)

transform_segmentation_masks(
        segmentation_masks, transformation, training=True
    )

### `transform_single_bounding_box`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L106-L119)

transform_single_bounding_box(
        bounding_box, transformation, training=True
    )

### `transform_single_image`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L92-L97)

transform_single_image(
        image, transformation, training=True
    )

### `transform_single_label`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L99-L104)

transform_single_label(
        label, transformation, training=True
    )

### `transform_single_segmentation_mask`

[View source](https://github.com/keras-team/keras/tree/master/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L121-L130)

transform_single_segmentation_mask(
        segmentation_mask, transformation, training=True
    )

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| lora\_enabled | `False` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.