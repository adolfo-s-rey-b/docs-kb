[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#used-in-the-notebooks_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#methods_2)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#from_config)
        
    *   [get\_random\_transformation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#get_random_transformation)
        
    *   [get\_shifted\_bbox](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#get_shifted_bbox)
        
    *   [get\_transformed\_x\_y](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#get_transformed_x_y)
        
    *   [transform\_bounding\_boxes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#transform_bounding_boxes)
        
    *   [transform\_images](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#transform_images)
        
    *   [transform\_labels](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#transform_labels)
        
    *   [transform\_segmentation\_masks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#transform_segmentation_masks)
        
    *   [transform\_single\_bounding\_box](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#transform_single_bounding_box)
        
    *   [transform\_single\_image](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#transform_single_image)
        
    *   [transform\_single\_label](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#transform_single_label)
        
    *   [transform\_single\_segmentation\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#transform_single_segmentation_mask)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.RandomTranslation Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#used-in-the-notebooks_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#methods_2)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#from_config)
        
    *   [get\_random\_transformation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#get_random_transformation)
        
    *   [get\_shifted\_bbox](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#get_shifted_bbox)
        
    *   [get\_transformed\_x\_y](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#get_transformed_x_y)
        
    *   [transform\_bounding\_boxes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#transform_bounding_boxes)
        
    *   [transform\_images](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#transform_images)
        
    *   [transform\_labels](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#transform_labels)
        
    *   [transform\_segmentation\_masks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#transform_segmentation_masks)
        
    *   [transform\_single\_bounding\_box](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#transform_single_bounding_box)
        
    *   [transform\_single\_image](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#transform_single_image)
        
    *   [transform\_single\_label](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#transform_single_label)
        
    *   [transform\_single\_segmentation\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomTranslation?version=stable#transform_single_segmentation_mask)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_translation.py#L18-L381)

A preprocessing layer which randomly translates images during training.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.RandomTranslation(
        height_factor,
        width_factor,
        fill_mode='reflect',
        interpolation='bilinear',
        seed=None,
        fill_value=0.0,
        data_format=None,
        **kwargs
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Retraining an Image Classifier](https://www.tensorflow.org/hub/tutorials/tf2_image_retraining) |

This layer will apply random translations to each image during training,
    filling empty space according to `fill_mode`.
    
    Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and\
    of integer or floating point dtype. By default, the layer will output\
    floats.\
    \
    Note: This layer is safe to use inside a <a href="../../../tf/data"><code>tf.data</code></a> or `grain` pipeline\
    (independently of which backend you're using).\
    \
    Input shape:\
        3D (unbatched) or 4D (batched) tensor with shape:\
        `(..., height, width, channels)`, in `"channels_last"` format,\
        or `(..., channels, height, width)`, in `"channels_first"` format.\
    \
    Output shape:\
        3D (unbatched) or 4D (batched) tensor with shape:\
        `(..., target_height, target_width, channels)`,\
        or `(..., channels, target_height, target_width)`,\
        in `"channels_first"` format.\
    \
    Args:\
        height_factor: a float represented as fraction of value, or a tuple of\
            size 2 representing lower and upper bound for shifting vertically. A\
            negative value means shifting image up, while a positive value means\
            shifting image down. When represented as a single positive float,\
            this value is used for both the upper and lower bound. For instance,\
            `height_factor=(-0.2, 0.3)` results in an output shifted by a random\
            amount in the range `[-20%, +30%]`. `height_factor=0.2` results in\
            an output height shifted by a random amount in the range\
            `[-20%, +20%]`.\
        width_factor: a float represented as fraction of value, or a tuple of\
            size 2 representing lower and upper bound for shifting horizontally.\
            A negative value means shifting image left, while a positive value\
            means shifting image right. When represented as a single positive\
            float, this value is used for both the upper and lower bound. For\
            instance, `width_factor=(-0.2, 0.3)` results in an output shifted\
            left by 20%, and shifted right by 30%. `width_factor=0.2` results\
            in an output height shifted left or right by 20%.\
        fill_mode: Points outside the boundaries of the input are filled\
            according to the given mode. Available methods are `"constant"`,\
            `"nearest"`, `"wrap"` and `"reflect"`. Defaults to `"constant"`.\
    \
            - `"reflect"`: `(d c b a | a b c d | d c b a)`\
                The input is extended by reflecting about the edge of the last\
                pixel.\
            - `"constant"`: `(k k k k | a b c d | k k k k)`\
                The input is extended by filling all values beyond\
                the edge with the same constant value k specified by\
                `fill_value`.\
            - `"wrap"`: `(a b c d | a b c d | a b c d)`\
                The input is extended by wrapping around to the opposite edge.\
            - `"nearest"`: `(a a a a | a b c d | d d d d)`\
                The input is extended by the nearest pixel.\
            Note that when using torch backend, `"reflect"` is redirected to\
            `"mirror"` `(c d c b | a b c d | c b a b)` because torch does not\
            support `"reflect"`.\
            Note that torch backend does not support `"wrap"`.\
        interpolation: Interpolation mode. Supported values: `"nearest"`,\
            `"bilinear"`.\
        seed: Integer. Used to create a random seed.\
        fill_value: a float represents the value to be filled outside the\
            boundaries when `fill_mode="constant"`.\
        data_format: string, either `"channels_last"` or `"channels_first"`.\
            The ordering of the dimensions in the inputs. `"channels_last"`\
            corresponds to inputs with shape `(batch, height, width, channels)`\
            while `"channels_first"` corresponds to inputs with shape\
            `(batch, channels, height, width)`. It defaults to the\
            `image_data_format` value found in your Keras config file at\
            `~/.keras/keras.json`. If you never set it, then it will be\
            `"channels_last"`.\
        **kwargs: Base layer keyword arguments, such as `name` and `dtype`.\
    \
    Example:\
\
layer = keras.layers.RandomTranslation(bounding_box_format="xyxy")\
    images = np.random.randint(0, 255, (4, 224, 224, 3), dtype="uint8")\
    \
    bounding_boxes = {\
        "boxes": np.array([\
            [[10, 20, 100, 150], [50, 60, 200, 250]],\
            [[15, 25, 110, 160], [55, 65, 210, 260]],\
            [[20, 30, 120, 170], [60, 70, 220, 270]],\
            [[25, 35, 130, 180], [65, 75, 230, 280]],\
        ], dtype="float32"),\
        "labels": np.array([[0, 1], [1, 2], [2, 3], [0, 3]], dtype="int32")\
    }\
    \
    labels = keras.ops.one_hot(\
        np.array([0, 1, 2, 3]),\
        num_classes=4\
    )\
    \
    segmentation_masks = np.random.randint(0, 3, (4, 224, 224, 1), dtype="uint8")\
    \
    output = layer(\
        {\
            "images": images,\
            "bounding_boxes": bounding_boxes,\
            "labels": labels,\
            "segmentation_masks": segmentation_masks\
        },\
        training=True\
    )\
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
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_translation.py#L275-L321)\
\
get_random_transformation(\
        data, training=True, seed=None\
    )\
\
### `get_shifted_bbox`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_translation.py#L190-L214)\
\
get_shifted_bbox(\
        bounding_boxes, w_shift_factor, h_shift_factor\
    )\
\
### `get_transformed_x_y`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_translation.py#L180-L188)\
\
get_transformed_x_y(\
        x, y, transform\
    )\
\
### `transform_bounding_boxes`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_translation.py#L216-L273)\
\
transform_bounding_boxes(\
        bounding_boxes, transformation, training=True\
    )\
\
### `transform_images`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L64-L70)\
\
transform_images(\
        images, transformation, training=True\
    )\
\
### `transform_labels`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_translation.py#L177-L178)\
\
transform_labels(\
        labels, transformation, training=True\
    )\
\
### `transform_segmentation_masks`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L83-L90)\
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