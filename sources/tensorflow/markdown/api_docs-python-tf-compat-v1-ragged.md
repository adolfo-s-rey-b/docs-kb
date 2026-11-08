[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.ragged Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

Public API for tf.\_api.v2.ragged namespace

Classes
-------

[`class RaggedTensorValue`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/RaggedTensorValue)
: Represents the value of a `RaggedTensor`.

Functions
---------

[`boolean_mask(...)`](https://www.tensorflow.org/api_docs/python/tf/ragged/boolean_mask)
: Applies a boolean mask to `data` without flattening the mask dimensions.

[`constant(...)`](https://www.tensorflow.org/api_docs/python/tf/ragged/constant)
: Constructs a constant RaggedTensor from a nested Python list.

[`constant_value(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/constant_value)
: Constructs a RaggedTensorValue from a nested Python list.

[`cross(...)`](https://www.tensorflow.org/api_docs/python/tf/ragged/cross)
: Generates feature cross from a list of tensors.

[`cross_hashed(...)`](https://www.tensorflow.org/api_docs/python/tf/ragged/cross_hashed)
: Generates hashed feature cross from a list of tensors.

[`map_flat_values(...)`](https://www.tensorflow.org/api_docs/python/tf/ragged/map_flat_values)
: Applies `op` to the `flat_values` of one or more RaggedTensors.

[`placeholder(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ragged/placeholder)
: Creates a placeholder for a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 that will always be fed.

[`range(...)`](https://www.tensorflow.org/api_docs/python/tf/ragged/range)
: Returns a `RaggedTensor` containing the specified sequences of numbers.

[`row_splits_to_segment_ids(...)`](https://www.tensorflow.org/api_docs/python/tf/ragged/row_splits_to_segment_ids)
: Generates the segmentation corresponding to a RaggedTensor `row_splits`.

[`segment_ids_to_row_splits(...)`](https://www.tensorflow.org/api_docs/python/tf/ragged/segment_ids_to_row_splits)
: Generates the RaggedTensor `row_splits` corresponding to a segmentation.

[`stack(...)`](https://www.tensorflow.org/api_docs/python/tf/ragged/stack)
: Stacks a list of rank-`R` tensors into one rank-`(R+1)` `RaggedTensor`.

[`stack_dynamic_partitions(...)`](https://www.tensorflow.org/api_docs/python/tf/ragged/stack_dynamic_partitions)
: Stacks dynamic partitions of a Tensor or RaggedTensor.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.