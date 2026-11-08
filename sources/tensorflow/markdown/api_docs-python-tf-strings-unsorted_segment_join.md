[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/strings/unsorted_segment_join#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/strings/unsorted_segment_join)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/strings/unsorted_segment_join?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/unsorted_segment_join#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/unsorted_segment_join#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.strings.unsorted\_segment\_join Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/strings/unsorted_segment_join#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/strings/unsorted_segment_join#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/string_ops.py#L586-L640)

Joins the elements of `inputs` based on `segment_ids`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.strings.unsorted_segment_join`](https://www.tensorflow.org/api_docs/python/tf/strings/unsorted_segment_join)

tf.strings.unsorted_segment_join(
        inputs, segment_ids, num_segments, separator='', name=None
    )

Computes the string join along segments of a tensor.

Given `segment_ids` with rank `N` and `data` with rank `N+M`:

output[i, k1...kM] = strings.join([data[j1...jN, k1...kM])\
\
where the join is over all `[j1...jN]` such that `segment_ids[j1...jN] = i`.\
\
Strings are joined in row-major order.\
\
#### For example:\
\
    inputs = ['this', 'a', 'test', 'is']\
\
    inputs = [['Y', 'q', 'c'], ['Y', '6', '6'], ['p', 'G', 'a']]\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `inputs` | A list of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> objects of type [`tf.string`](https://www.tensorflow.org/api_docs/python/tf#string)<br>. |\
| `segment_ids` | A tensor whose shape is a prefix of `inputs.shape` and whose type must be [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br> or [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>. Negative segment ids are not supported. |\
| `num_segments` | A scalar of type [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br> or [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>. Must be non-negative and larger than any segment id. |\
| `separator` | The separator to use when joining. Defaults to `""`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A [`tf.string`](https://www.tensorflow.org/api_docs/python/tf#string)<br> tensor representing the concatenated values, using the given separator. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.