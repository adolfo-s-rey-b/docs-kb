[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.initializers Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers#functions)
    

Public API for tf.\_api.v2.initializers namespace

Classes
-------

[`class constant`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/constant_initializer)
: Initializer that generates tensors with constant values.

[`class glorot_normal`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/glorot_normal_initializer)
: The Glorot normal initializer, also called Xavier normal initializer.

[`class glorot_uniform`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/glorot_uniform_initializer)
: The Glorot uniform initializer, also called Xavier uniform initializer.

[`class identity`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/identity)
: Initializer that generates the identity matrix.

[`class ones`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ones_initializer)
: Initializer that generates tensors initialized to 1.

[`class orthogonal`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/orthogonal_initializer)
: Initializer that generates an orthogonal matrix.

[`class random_normal`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_normal_initializer)
: Initializer that generates tensors with a normal distribution.

[`class random_uniform`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_uniform_initializer)
: Initializer that generates tensors with a uniform distribution.

[`class truncated_normal`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/truncated_normal_initializer)
: Initializer that generates a truncated normal distribution.

[`class uniform_unit_scaling`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/uniform_unit_scaling_initializer)
: Initializer that generates tensors without scaling variance.

[`class variance_scaling`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/variance_scaling_initializer)
: Initializer capable of adapting its scale to the shape of weights tensors.

[`class zeros`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/zeros_initializer)
: Initializer that generates tensors initialized to 0.

Functions
---------

[`global_variables(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables_initializer)
: Returns an Op that initializes global variables.

[`he_normal(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/he_normal)
: He normal initializer.

[`he_uniform(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/he_uniform)
: He uniform variance scaling initializer.

[`lecun_normal(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/lecun_normal)
: LeCun normal initializer.

[`lecun_uniform(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/initializers/lecun_uniform)
: LeCun uniform initializer.

[`local_variables(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/local_variables_initializer)
: Returns an Op that initializes all local variables.

[`tables_initializer(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tables_initializer)
: Returns an Op that initializes all tables of the default graph.

[`variables(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/variables_initializer)
: Returns an Op that initializes a list of variables.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.