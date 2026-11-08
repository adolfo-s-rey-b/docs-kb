[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/utils#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/utils)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/utils?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tfm/utils#modules)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/utils#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.utils Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tfm/utils#modules)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/utils#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/tf_utils.py)

Common TF utilities.

Modules
-------

[`activations`](https://www.tensorflow.org/api_docs/python/tfm/utils/activations)
 module: Activations package definition.

Functions
---------

[`assert_rank(...)`](https://www.tensorflow.org/api_docs/python/tfm/utils/assert_rank)
: Raises an exception if the tensor rank is not of the expected rank.

[`clone_initializer(...)`](https://www.tensorflow.org/api_docs/python/tfm/utils/clone_initializer)

[`cross_replica_concat(...)`](https://www.tensorflow.org/api_docs/python/tfm/utils/cross_replica_concat)
: Concatenates the given `value` across (GPU/TPU) cores, along `axis`.

[`deserialize_keras_object(...)`](https://www.tensorflow.org/api_docs/python/tfm/utils/deserialize_keras_object)

[`get_activation(...)`](https://www.tensorflow.org/api_docs/python/tfm/utils/get_activation)
: Maps an identifier to a Python function, e.g., "relu" => [`tf.nn.relu`](https://www.tensorflow.org/api_docs/python/tf/nn/relu)
.

[`get_replica_id(...)`](https://www.tensorflow.org/api_docs/python/tfm/utils/get_replica_id)
: Gets replica id depending on the environment.

[`get_shape_list(...)`](https://www.tensorflow.org/api_docs/python/tfm/utils/get_shape_list)
: Returns a list of the shape of tensor, preferring static dimensions.

[`is_special_none_tensor(...)`](https://www.tensorflow.org/api_docs/python/tfm/utils/is_special_none_tensor)
: Checks if a tensor is a special None Tensor.

[`pack_inputs(...)`](https://www.tensorflow.org/api_docs/python/tfm/utils/pack_inputs)
: Pack a list of `inputs` tensors to a tuple. (deprecated)

[`safe_mean(...)`](https://www.tensorflow.org/api_docs/python/tfm/utils/safe_mean)
: Computes a safe mean of the losses.

[`serialize_activation(...)`](https://www.tensorflow.org/api_docs/python/tfm/utils/serialize_activation)

[`serialize_constraint(...)`](https://www.tensorflow.org/api_docs/python/tfm/utils/serialize_constraint)

[`serialize_initializer(...)`](https://www.tensorflow.org/api_docs/python/tfm/utils/serialize_initializer)

[`serialize_keras_object(...)`](https://www.tensorflow.org/api_docs/python/tfm/utils/serialize_keras_object)

[`serialize_layer(...)`](https://www.tensorflow.org/api_docs/python/tfm/utils/serialize_layer)

[`serialize_regularizer(...)`](https://www.tensorflow.org/api_docs/python/tfm/utils/serialize_regularizer)

[`unpack_inputs(...)`](https://www.tensorflow.org/api_docs/python/tfm/utils/unpack_inputs)
: unpack a tuple of `inputs` tensors to a tuple. (deprecated)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.