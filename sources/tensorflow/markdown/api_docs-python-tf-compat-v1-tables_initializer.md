[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tables_initializer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tables_initializer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tables_initializer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tables_initializer#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tables_initializer#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tables_initializer#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tables_initializer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tables_initializer#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.tables\_initializer Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tables_initializer#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tables_initializer#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tables_initializer#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tables_initializer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tables_initializer#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L67-L108)

Returns an Op that initializes all tables of the default graph.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.initializers.tables_initializer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tables_initializer)

tf.compat.v1.tables_initializer(
        name='init_all_tables'
    )

Migrate to TF2
--------------

[`tf.compat.v1.tables_initializer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tables_initializer)
 is no longer needed with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. In TF2, when creating an initializable table like a [`tf.lookup.StaticHashTable`](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticHashTable)
, the table will automatically be initialized on creation.

#### Before & After Usage Example

Before:

    with tf.compat.v1.Session():

After:

    init = tf.lookup.KeyValueTensorInitializer(['a', 'b'], [1, 2])

Description
-----------

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Universal Sentence Encoder-Lite demo](https://www.tensorflow.org/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder_lite)<br>    <br>*   [Generating Images with BigBiGAN](https://www.tensorflow.org/hub/tutorials/bigbigan_with_tf_hub)<br>    <br>*   [Classify Flowers with Transfer Learning](https://www.tensorflow.org/hub/tutorials/image_feature_vector)<br>    <br>*   [Wiki40B Language Models](https://www.tensorflow.org/hub/tutorials/wiki40b_lm) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | Optional name for the initialization op. |

|     |
| --- |
| Returns<br>------- |     |
| An Op that initializes all tables. Note that if there are not tables the returned Op is a NoOp. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.