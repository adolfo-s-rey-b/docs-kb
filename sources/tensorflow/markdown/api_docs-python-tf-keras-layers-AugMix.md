[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#methods_2)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#from_config)
        
    *   [get\_random\_transformation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#get_random_transformation)
        
    *   [transform\_bounding\_boxes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#transform_bounding_boxes)
        
    *   [transform\_images](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#transform_images)
        
    *   [transform\_labels](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#transform_labels)
        
    *   [transform\_segmentation\_masks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#transform_segmentation_masks)
        
    *   [transform\_single\_bounding\_box](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#transform_single_bounding_box)
        
    *   [transform\_single\_image](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#transform_single_image)
        
    *   [transform\_single\_label](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#transform_single_label)
        
    *   [transform\_single\_segmentation\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#transform_single_segmentation_mask)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.AugMix Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#methods_2)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#from_config)
        
    *   [get\_random\_transformation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#get_random_transformation)
        
    *   [transform\_bounding\_boxes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#transform_bounding_boxes)
        
    *   [transform\_images](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#transform_images)
        
    *   [transform\_labels](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#transform_labels)
        
    *   [transform\_segmentation\_masks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#transform_segmentation_masks)
        
    *   [transform\_single\_bounding\_box](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#transform_single_bounding_box)
        
    *   [transform\_single\_image](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#transform_single_image)
        
    *   [transform\_single\_label](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#transform_single_label)
        
    *   [transform\_single\_segmentation\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AugMix?version=stable#transform_single_segmentation_mask)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/aug_mix.py#L39-L360)

Performs the AugMix data augmentation technique.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.AugMix(
        value_range=(0, 255),
        num_chains=3,
        chain_depth=3,
        factor=0.3,
        alpha=1.0,
        all_ops=True,
        interpolation='bilinear',
        seed=None,
        data_format=None,
        **kwargs
    )

AugMix aims to produce images with variety while preserving the image
    semantics and local statistics. During the augmentation process,
    the same augmentation is applied across all images in the batch
    in num_chains different ways, with each chain consisting of
    chain_depth augmentations.
    
    Note: This layer is safe to use inside a <a href="../../../tf/data"><code>tf.data</code></a> or `grain` pipeline
    (independently of which backend you're using).
    
    References:
    
        - [AugMix paper](https://arxiv.org/pdf/1912.02781)
        - [Official Code](https://github.com/google-research/augmix)
    
    Args:
        value_range: the range of values the incoming images will have.
            Represented as a two number tuple written (low, high).
            This is typically either `(0, 1)` or `(0, 255)` depending
            on how your preprocessing pipeline is set up.
        num_chains: an integer representing the number of different chains to
            be mixed, defaults to 3.
        chain_depth: an integer representing the maximum number of
            transformations to be applied in each chain. The actual number
            of transformations in each chain will be sampled randomly
            from the range `[0, `chain_depth`]`. Defaults to 3.
        factor: The strength of the augmentation as a normalized value
            between 0 and 1. Default is 0.3.
        alpha: a float value used as the probability coefficients for the
            Beta and Dirichlet distributions, defaults to 1.0.
        all_ops: Use all operations (including random_brightness,
            random_color_degeneration, random_contrast and random_sharpness).
            Default is True.
        interpolation: The interpolation method to use for resizing operations.
            Options include `"nearest"`, `"bilinear"`. Default is `"bilinear"`.
        seed: Integer. Used to create a random seed.
    
    Example:

layer = keras.layers.AugMix(bounding_box_format="xyxy")
    images = np.random.randint(0, 255, (4, 224, 224, 3), dtype="uint8")
    
    bounding_boxes = {
        "boxes": np.array([\
            [[10, 20, 100, 150], [50, 60, 200, 250]],\
            [[15, 25, 110, 160], [55, 65, 210, 260]],\
            [[20, 30, 120, 170], [60, 70, 220, 270]],\
            [[25, 35, 130, 180], [65, 75, 230, 280]],\
        ], dtype="float32"),
        "labels": np.array([[0, 1], [1, 2], [2, 3], [0, 3]], dtype="int32")
    }
    
    labels = keras.ops.one_hot(
        np.array([0, 1, 2, 3]),
        num_classes=4
    )
    
    segmentation_masks = np.random.randint(0, 3, (4, 224, 224, 1), dtype="uint8")
    
    output = layer(
        {
            "images": images,
            "bounding_boxes": bounding_boxes,
            "labels": labels,
            "segmentation_masks": segmentation_masks
        },
        training=True
    )

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/aug_mix.py#L215-L267)

get_random_transformation(
        data, training=True, seed=None
    )

### `transform_bounding_boxes`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/aug_mix.py#L305-L311)

transform_bounding_boxes(
        bounding_boxes, transformation, training=True
    )

### `transform_images`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/aug_mix.py#L269-L300)

transform_images(
        images, transformation, training=True
    )

### `transform_labels`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/aug_mix.py#L302-L303)

transform_labels(
        labels, transformation, training=True
    )

### `transform_segmentation_masks`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/aug_mix.py#L313-L343)

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