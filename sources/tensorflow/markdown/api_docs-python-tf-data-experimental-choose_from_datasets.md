[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/choose_from_datasets#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/choose_from_datasets)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/choose_from_datasets?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/choose_from_datasets#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/choose_from_datasets#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/choose_from_datasets#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.choose\_from\_datasets Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/choose_from_datasets#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/choose_from_datasets#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/choose_from_datasets#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/interleave_ops.py#L170-L224)

Creates a dataset that deterministically chooses elements from `datasets`. (deprecated)

tf.data.experimental.choose_from_datasets(
        datasets, choice_dataset, stop_on_empty_dataset=False
    )

For example, given the following datasets:

datasets = [tf.data.Dataset.from_tensors("foo").repeat(),\
                tf.data.Dataset.from_tensors("bar").repeat(),\
                tf.data.Dataset.from_tensors("baz").repeat()]
    
    # Define a dataset containing `[0, 1, 2, 0, 1, 2, 0, 1, 2]`.
    choice_dataset = tf.data.Dataset.range(3).repeat(3)
    
    result = tf.data.experimental.choose_from_datasets(datasets, choice_dataset)

The elements of `result` will be:

"foo", "bar", "baz", "foo", "bar", "baz", "foo", "bar", "baz"

|     |     |
| --- | --- |
| Args<br>---- |     |
| `datasets` | A non-empty list of [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> objects with compatible structure. |
| `choice_dataset` | A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> of scalar [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> tensors between `0` and `len(datasets) - 1`. |
| `stop_on_empty_dataset` | If `True`, selection stops if it encounters an empty dataset. If `False`, it skips empty datasets. It is recommended to set it to `True`. Otherwise, the selected elements start off as the user intends, but may change as input datasets become empty. This can be difficult to detect since the dataset starts off looking correct. Default to `False` for backward compatibility. |

|     |
| --- |
| Returns<br>------- |     |
| A dataset that interleaves elements from `datasets` according to the values of `choice_dataset`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `datasets` or `choice_dataset` has the wrong type. |
| `ValueError` | If `datasets` is empty. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.