[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses#main-content)

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
    

Module: tf.compat.v1.losses Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

Public API for tf.\_api.v2.losses namespace

Classes
-------

[`class Reduction`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/Reduction)
: Types of loss reduction.

Functions
---------

[`absolute_difference(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/absolute_difference)
: Adds an Absolute Difference loss to the training procedure.

[`add_loss(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/add_loss)
: Adds a externally defined loss to the collection of losses.

[`compute_weighted_loss(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/compute_weighted_loss)
: Computes the weighted loss.

[`cosine_distance(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/cosine_distance)
: Adds a cosine-distance loss to the training procedure. (deprecated arguments)

[`get_losses(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_losses)
: Gets the list of losses from the loss\_collection.

[`get_regularization_loss(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_regularization_loss)
: Gets the total regularization loss.

[`get_regularization_losses(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_regularization_losses)
: Gets the list of regularization losses.

[`get_total_loss(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_total_loss)
: Returns a tensor whose value represents the total loss.

[`hinge_loss(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/hinge_loss)
: Adds a hinge loss to the training procedure.

[`huber_loss(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/huber_loss)
: Adds a [Huber Loss](https://en.wikipedia.org/wiki/Huber_loss)
 term to the training procedure.

[`log_loss(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/log_loss)
: Adds a Log Loss term to the training procedure.

[`mean_pairwise_squared_error(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_pairwise_squared_error)
: Adds a pairwise-errors-squared loss to the training procedure.

[`mean_squared_error(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/mean_squared_error)
: Adds a Sum-of-Squares loss to the training procedure.

[`sigmoid_cross_entropy(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sigmoid_cross_entropy)
: Creates a cross-entropy loss using tf.nn.sigmoid\_cross\_entropy\_with\_logits.

[`softmax_cross_entropy(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/softmax_cross_entropy)
: Creates a cross-entropy loss using tf.nn.softmax\_cross\_entropy\_with\_logits\_v2.

[`sparse_softmax_cross_entropy(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/sparse_softmax_cross_entropy)
: Cross-entropy loss using [`tf.nn.sparse_softmax_cross_entropy_with_logits`](https://www.tensorflow.org/api_docs/python/tf/nn/sparse_softmax_cross_entropy_with_logits)
.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.