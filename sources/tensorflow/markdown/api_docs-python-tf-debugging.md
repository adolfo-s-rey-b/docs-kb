[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/debugging#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/debugging)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/debugging?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/debugging#modules)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/debugging#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.debugging Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/debugging#modules)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/debugging#functions)
    

Public API for tf.\_api.v2.debugging namespace

Modules
-------

[`experimental`](https://www.tensorflow.org/api_docs/python/tf/debugging/experimental)
 module: Public API for tf.\_api.v2.debugging.experimental namespace

Functions
---------

[`Assert(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert)
: Asserts that the given condition is true.

[`assert_all_finite(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_all_finite)
: Assert that the tensor does not contain any NaN's or Inf's.

[`assert_equal(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_equal)
: Assert the condition `x == y` holds element-wise.

[`assert_greater(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_greater)
: Assert the condition `x > y` holds element-wise.

[`assert_greater_equal(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_greater_equal)
: Assert the condition `x >= y` holds element-wise.

[`assert_integer(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_integer)
: Assert that `x` is of integer dtype.

[`assert_less(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_less)
: Assert the condition `x < y` holds element-wise.

[`assert_less_equal(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_less_equal)
: Assert the condition `x <= y` holds element-wise.

[`assert_near(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_near)
: Assert the condition `x` and `y` are close element-wise.

[`assert_negative(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_negative)
: Assert the condition `x < 0` holds element-wise.

[`assert_non_negative(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_non_negative)
: Assert the condition `x >= 0` holds element-wise.

[`assert_non_positive(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_non_positive)
: Assert the condition `x <= 0` holds element-wise.

[`assert_none_equal(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_none_equal)
: Assert the condition `x != y` holds element-wise.

[`assert_positive(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_positive)
: Assert the condition `x > 0` holds element-wise.

[`assert_proper_iterable(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_proper_iterable)
: Static assert that values is a "proper" iterable.

[`assert_rank(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_rank)
: Assert that `x` has rank equal to `rank`.

[`assert_rank_at_least(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_rank_at_least)
: Assert that `x` has rank of at least `rank`.

[`assert_rank_in(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_rank_in)
: Assert that `x` has a rank in `ranks`.

[`assert_same_float_dtype(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_same_float_dtype)
: Validate and return float type based on `tensors` and `dtype`.

[`assert_scalar(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_scalar)
: Asserts that the given `tensor` is a scalar.

[`assert_shapes(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_shapes)
: Assert tensor shapes and dimension size relationships between tensors.

[`assert_type(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_type)
: Asserts that the given `Tensor` is of the specified type.

[`check_numerics(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/check_numerics)
: Checks a tensor for NaN and Inf values.

[`disable_check_numerics(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/disable_check_numerics)
: Disable the eager/graph unified numerics checking mechanism.

[`disable_traceback_filtering(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/disable_traceback_filtering)
: Disable filtering out TensorFlow-internal frames in exception stack traces.

[`enable_check_numerics(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/enable_check_numerics)
: Enable tensor numerics checking in an eager/graph unified fashion.

[`enable_traceback_filtering(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/enable_traceback_filtering)
: Enable filtering out TensorFlow-internal frames in exception stack traces.

[`get_log_device_placement(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/get_log_device_placement)
: Get if device placements are logged.

[`is_numeric_tensor(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/is_numeric_tensor)
: Returns `True` if the elements of `tensor` are numbers.

[`is_traceback_filtering_enabled(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/is_traceback_filtering_enabled)
: Check whether traceback filtering is currently enabled.

[`set_log_device_placement(...)`](https://www.tensorflow.org/api_docs/python/tf/debugging/set_log_device_placement)
: Turns logging for device placement decisions on or off.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.