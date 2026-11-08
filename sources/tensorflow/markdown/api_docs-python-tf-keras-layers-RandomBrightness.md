[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#methods_2)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#from_config)
        
    *   [get\_random\_transformation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#get_random_transformation)
        
    *   [transform\_bounding\_boxes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#transform_bounding_boxes)
        
    *   [transform\_images](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#transform_images)
        
    *   [transform\_labels](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#transform_labels)
        
    *   [transform\_segmentation\_masks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#transform_segmentation_masks)
        
    *   [transform\_single\_bounding\_box](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#transform_single_bounding_box)
        
    *   [transform\_single\_image](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#transform_single_image)
        
    *   [transform\_single\_label](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#transform_single_label)
        
    *   [transform\_single\_segmentation\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#transform_single_segmentation_mask)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.RandomBrightness Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#methods_2)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#from_config)
        
    *   [get\_random\_transformation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#get_random_transformation)
        
    *   [transform\_bounding\_boxes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#transform_bounding_boxes)
        
    *   [transform\_images](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#transform_images)
        
    *   [transform\_labels](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#transform_labels)
        
    *   [transform\_segmentation\_masks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#transform_segmentation_masks)
        
    *   [transform\_single\_bounding\_box](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#transform_single_bounding_box)
        
    *   [transform\_single\_image](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#transform_single_image)
        
    *   [transform\_single\_label](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#transform_single_label)
        
    *   [transform\_single\_segmentation\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomBrightness?version=stable#transform_single_segmentation_mask)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_brightness.py#L8-L158)

A preprocessing layer which randomly adjusts brightness during training.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.RandomBrightness(
        factor, value_range=(0, 255), seed=None, **kwargs
    )

This layer will randomly increase/reduce the brightness for the input RGB images. At inference time, the output will be identical to the input. Call the layer with `training=True` to adjust the brightness of the input.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `factor` | Float or a list/tuple of 2 floats between -1.0 and 1.0. The factor is used to determine the lower bound and upper bound of the brightness adjustment. A float value will be chosen randomly between the limits. When -1.0 is chosen, the output image will be black, and when 1.0 is chosen, the image will be fully white. When only one float is provided, eg, 0.2, then -0.2 will be used for lower bound and 0.2 will be used for upper bound. |
| `value_range` | Optional list/tuple of 2 floats for the lower and upper limit of the values of the input data. To make no change, use `[0.0, 1.0]`, e.g., if the image input has been scaled before this layer. Defaults to `[0.0, 255.0]`. The brightness adjustment will be scaled to this range, and the output values will be clipped to this range. |
| `seed` | optional integer, for fixed RNG behavior. |

Inputs: 3D (HWC) or 4D (NHWC) tensor, with float or int dtype. Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`)\
\
Output: 3D (HWC) or 4D (NHWC) tensor with brightness adjusted based on the `factor`. By default, the layer will output floats. The output value will be clipped to the range `[0, 255]`, the valid range of RGB colors, and rescaled based on the `value_range` if needed.\
\
#### Example:\
\
random_bright = keras.layers.RandomBrightness(factor=0.2)\
    \
    # An image with shape [2, 2, 3]\
    image = [[[1, 2, 3], [4 ,5 ,6]], [[7, 8, 9], [10, 11, 12]]]\
    \
    # Assume we randomly select the factor to be 0.1, then it will apply\
    # 0.1 * 255 to all the channel\
    output = random_bright(image, training=True)\
    \
    # output will be int64 with 25.5 added to each channel and round down.\
\
> > > array(\[\[\[26.5, 27.5, 28.5\] \[29.5, 30.5, 31.5\]\] \[\[32.5, 33.5, 34.5\] \[35.5, 36.5, 37.5\]\]\], shape=(2, 2, 3), dtype=int64)\
\
|     |     |\
| --- | --- |\
| Attributes<br>---------- |     |\
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |\
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |\
\
Methods\
-------\
\
### `convert_weight`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/data_layer.py#L153-L159)\
\
convert_weight(\
        weight\
    )\
\
Convert the weight if it is from the a different backend.\
\
### `from_config`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L322-L362)\
\
@classmethod\
\
Creates an operation from its config.\
\
This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.\
\
if "dtype" in config and isinstance(config["dtype"], dict):\
        policy = dtype_policies.deserialize(config["dtype"])\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `config` | A Python dictionary, typically the output of `get_config`. |\
\
|     |\
| --- |\
| Returns |     |\
| An operation instance. |     |\
\
### `get_random_transformation`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_brightness.py#L90-L120)\
\
get_random_transformation(\
        data, training=True, seed=None\
    )\
\
### `transform_bounding_boxes`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_brightness.py#L135-L141)\
\
transform_bounding_boxes(\
        bounding_boxes, transformation, training=True\
    )\
\
### `transform_images`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_brightness.py#L122-L130)\
\
transform_images(\
        images, transformation, training=True\
    )\
\
### `transform_labels`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_brightness.py#L132-L133)\
\
transform_labels(\
        labels, transformation, training=True\
    )\
\
### `transform_segmentation_masks`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_brightness.py#L143-L146)\
\
transform_segmentation_masks(\
        segmentation_masks, transformation, training=True\
    )\
\
### `transform_single_bounding_box`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L106-L119)\
\
transform_single_bounding_box(\
        bounding_box, transformation, training=True\
    )\
\
### `transform_single_image`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L92-L97)\
\
transform_single_image(\
        image, transformation, training=True\
    )\
\
### `transform_single_label`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L99-L104)\
\
transform_single_label(\
        label, transformation, training=True\
    )\
\
### `transform_single_segmentation_mask`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L121-L130)\
\
transform_single_segmentation_mask(\
        segmentation_mask, transformation, training=True\
    )\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.