[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/make_initializable_iterator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/make_initializable_iterator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/make_initializable_iterator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/make_initializable_iterator#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/make_initializable_iterator#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/make_initializable_iterator#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/make_initializable_iterator#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/make_initializable_iterator#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.data.make\_initializable\_iterator Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/make_initializable_iterator#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/make_initializable_iterator#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/make_initializable_iterator#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/make_initializable_iterator#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/data/make_initializable_iterator#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L4353-L4398)

Creates an iterator for elements of `dataset`.

tf.compat.v1.data.make_initializable_iterator(
        dataset: tf.compat.v1.data.Dataset,
        shared_name=None
    ) -> tf.compat.v1.data.Iterator

Migrate to TF2
--------------

This is a legacy API for consuming dataset elements and should only be used during transition from TF 1 to TF 2. Note that using this API should be a transient state of your code base as there are in general no guarantees about the interoperability of TF 1 and TF 2 code.

In TF 2 datasets are Python iterables which means you can consume their elements using `for elem in dataset: ...` or by explicitly creating iterator via `iterator = iter(dataset)` and fetching its elements via `values = next(iterator)`.

Description
-----------

dataset = ...
    iterator = tf.compat.v1.data.make_initializable_iterator(dataset)
    # ...
    sess.run(iterator.initializer)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dataset` | A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>. |
| `shared_name` | (Optional.) If non-empty, the returned iterator will be shared under the given name across multiple sessions that share the same devices (e.g. when using a remote server). |

|     |
| --- |
| Returns<br>------- |     |
| A [`tf.data.Iterator`](https://www.tensorflow.org/api_docs/python/tf/data/Iterator)<br> for elements of `dataset`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | If eager execution is enabled. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.