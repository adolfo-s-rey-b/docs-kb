[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable&hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FEqualization%3Fversion%3Dstable&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#args_1)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#input-shape_1)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#output-shape_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#methods_2)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#from_config)
        
    *   [get\_random\_transformation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#get_random_transformation)
        
    *   [transform\_bounding\_boxes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#transform_bounding_boxes)
        
    *   [transform\_images](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#transform_images)
        
    *   [transform\_labels](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#transform_labels)
        
    *   [transform\_segmentation\_masks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#transform_segmentation_masks)
        
    *   [transform\_single\_bounding\_box](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#transform_single_bounding_box)
        
    *   [transform\_single\_image](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#transform_single_image)
        
    *   [transform\_single\_label](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#transform_single_label)
        
    *   [transform\_single\_segmentation\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#transform_single_segmentation_mask)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Equalization Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#args_1)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#input-shape_1)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#output-shape_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#methods_2)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#from_config)
        
    *   [get\_random\_transformation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#get_random_transformation)
        
    *   [transform\_bounding\_boxes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#transform_bounding_boxes)
        
    *   [transform\_images](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#transform_images)
        
    *   [transform\_labels](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#transform_labels)
        
    *   [transform\_segmentation\_masks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#transform_segmentation_masks)
        
    *   [transform\_single\_bounding\_box](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#transform_single_bounding_box)
        
    *   [transform\_single\_image](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#transform_single_image)
        
    *   [transform\_single\_label](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#transform_single_label)
        
    *   [transform\_single\_segmentation\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Equalization?version=stable#transform_single_segmentation_mask)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/equalization.py#L8-L224)

Preprocessing layer for histogram equalization on image channels.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Equalization(
        value_range=(0, 255), bins=256, data_format=None, **kwargs
    )

Histogram equalization is a technique to adjust image intensities to enhance contrast by effectively spreading out the most frequent intensity values. This layer applies equalization on a channel-wise basis, which can improve the visibility of details in images.

This layer works with both grayscale and color images, performing equalization independently on each color channel. At inference time, the equalization is consistently applied.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value_range` | Optional list/tuple of 2 floats specifying the lower and upper limits of the input data values. Defaults to `[0, 255]`. If the input image has been scaled, use the appropriate range (e.g., `[0.0, 1.0]`). The equalization will be scaled to this range, and output values will be clipped accordingly. |
| `bins` | Integer specifying the number of histogram bins to use for equalization. Defaults to 256, which is suitable for 8-bit images. Larger values can provide more granular intensity redistribution. |

|     |     |
| --- | --- |
| Input shape<br>----------- |     |
| `3D` | `unbatched) or 4D (batched) tensor with shape`<br><br>`(..., height, width, channels)`, in `"channels_last"` format, or `(..., channels, height, width)`, in `"channels_first"` format. |

|     |     |
| --- | --- |
| Output shape<br>------------ |     |
| `3D` | `unbatched) or 4D (batched) tensor with shape`<br><br>`(..., target_height, target_width, channels)`, or `(..., channels, target_height, target_width)`, in `"channels_first"` format. |

#### Example:

# Create an equalization layer for standard 8-bit images
    equalizer = keras.layers.Equalization()
    
    # An image with uneven intensity distribution
    image = [...] # your input image
    
    # Apply histogram equalization
    equalized_image = equalizer(image)
    
    # For images with custom value range
    custom_equalizer = keras.layers.Equalization(
        value_range=[0.0, 1.0],  # for normalized images
        bins=128  # fewer bins for more subtle equalization
    )
    custom_equalized = custom_equalizer(normalized_image)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `convert_weight`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/data_layer.py#L153-L159)

convert_weight(
        weight
    )

Convert the weight if it is from the a different backend.

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L322-L362)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L58-L59)

get_random_transformation(
        data, training=True, seed=None
    )

### `transform_bounding_boxes`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/equalization.py#L205-L211)

transform_bounding_boxes(
        bounding_boxes, transformation, training=True
    )

### `transform_images`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/equalization.py#L173-L197)

transform_images(
        images, transformation, training=True
    )

### `transform_labels`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/equalization.py#L213-L214)

transform_labels(
        labels, transformation, training=True
    )

### `transform_segmentation_masks`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/equalization.py#L216-L219)

transform_segmentation_masks(
        segmentation_masks, transformation, training=True
    )

### `transform_single_bounding_box`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L106-L119)

transform_single_bounding_box(
        bounding_box, transformation, training=True
    )

### `transform_single_image`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L92-L97)

transform_single_image(
        image, transformation, training=True
    )

### `transform_single_label`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L99-L104)

transform_single_label(
        label, transformation, training=True
    )

### `transform_single_segmentation_mask`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L121-L130)

transform_single_segmentation_mask(
        segmentation_mask, transformation, training=True
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.