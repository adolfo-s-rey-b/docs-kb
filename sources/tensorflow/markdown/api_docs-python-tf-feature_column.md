[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/feature_column#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/feature_column)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/feature_column?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/feature_column#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.feature\_column Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/feature_column#functions)
    

Public API for tf.\_api.v2.feature\_column namespace

Functions
---------

[`bucketized_column(...)`](https://www.tensorflow.org/api_docs/python/tf/feature_column/bucketized_column)
: Represents discretized dense input bucketed by `boundaries`. (deprecated)

[`categorical_column_with_hash_bucket(...)`](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_hash_bucket)
: Represents sparse feature where ids are set by hashing. (deprecated)

[`categorical_column_with_identity(...)`](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_identity)
: A `CategoricalColumn` that returns identity values. (deprecated)

[`categorical_column_with_vocabulary_file(...)`](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_vocabulary_file)
: A `CategoricalColumn` with a vocabulary file. (deprecated)

[`categorical_column_with_vocabulary_list(...)`](https://www.tensorflow.org/api_docs/python/tf/feature_column/categorical_column_with_vocabulary_list)
: A `CategoricalColumn` with in-memory vocabulary. (deprecated)

[`crossed_column(...)`](https://www.tensorflow.org/api_docs/python/tf/feature_column/crossed_column)
: Returns a column for performing crosses of categorical features. (deprecated)

[`embedding_column(...)`](https://www.tensorflow.org/api_docs/python/tf/feature_column/embedding_column)
: `DenseColumn` that converts from sparse, categorical input. (deprecated)

[`indicator_column(...)`](https://www.tensorflow.org/api_docs/python/tf/feature_column/indicator_column)
: Represents multi-hot representation of given categorical column. (deprecated)

[`make_parse_example_spec(...)`](https://www.tensorflow.org/api_docs/python/tf/feature_column/make_parse_example_spec)
: Creates parsing spec dictionary from input feature\_columns. (deprecated)

[`numeric_column(...)`](https://www.tensorflow.org/api_docs/python/tf/feature_column/numeric_column)
: Represents real valued or numerical features. (deprecated)

[`sequence_categorical_column_with_hash_bucket(...)`](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_hash_bucket)
: A sequence of categorical terms where ids are set by hashing. (deprecated)

[`sequence_categorical_column_with_identity(...)`](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_identity)
: Returns a feature column that represents sequences of integers. (deprecated)

[`sequence_categorical_column_with_vocabulary_file(...)`](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_file)
: A sequence of categorical terms where ids use a vocabulary file. (deprecated)

[`sequence_categorical_column_with_vocabulary_list(...)`](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_categorical_column_with_vocabulary_list)
: A sequence of categorical terms where ids use an in-memory list. (deprecated)

[`sequence_numeric_column(...)`](https://www.tensorflow.org/api_docs/python/tf/feature_column/sequence_numeric_column)
: Returns a feature column that represents sequences of numeric data. (deprecated)

[`shared_embeddings(...)`](https://www.tensorflow.org/api_docs/python/tf/feature_column/shared_embeddings)
: List of dense columns that convert from sparse, categorical input. (deprecated)

[`weighted_categorical_column(...)`](https://www.tensorflow.org/api_docs/python/tf/feature_column/weighted_categorical_column)
: Applies weight values to a `CategoricalColumn`. (deprecated)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.