[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/bucket_by_sequence_length#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/bucket_by_sequence_length)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/bucket_by_sequence_length?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/bucket_by_sequence_length#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/bucket_by_sequence_length#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/bucket_by_sequence_length#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.bucket\_by\_sequence\_length Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/bucket_by_sequence_length#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/bucket_by_sequence_length#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/bucket_by_sequence_length#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/grouping.py#L110-L257)

A transformation that buckets elements in a `Dataset` by length. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.bucket_by_sequence_length`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/bucket_by_sequence_length)

tf.data.experimental.bucket_by_sequence_length(
        element_length_func,
        bucket_boundaries,
        bucket_batch_sizes,
        padded_shapes=None,
        padding_values=None,
        pad_to_bucket_boundary=False,
        no_padding=False,
        drop_remainder=False
    )

Elements of the `Dataset` are grouped together by length and then are padded and batched.

This is useful for sequence tasks in which the elements have variable length. Grouping together elements that have similar lengths reduces the total fraction of padding in a batch which increases training step efficiency.

Below is an example to bucketize the input data to the 3 buckets "\[0, 3), \[3, 5), \[5, inf)" based on sequence length, with batch size 2.\
\
    elements = [\
\
    dataset = tf.data.Dataset.from_generator(\
\
    dataset = dataset.apply(\
\
    for elem in dataset.as_numpy_iterator():\
\
There is also a possibility to pad the dataset till the bucket boundary. You can also provide which value to be used while padding the data. Below example uses `-1` as padding and it also shows the input data being bucketizied to two buckets "\[0,3\], \[4,6\]".\
\
    elements = [\
\
    dataset = tf.data.Dataset.from_generator(\
\
    dataset = dataset.apply(\
\
    for elem in dataset.as_numpy_iterator():\
\
When using `pad_to_bucket_boundary` option, it can be seen that it is not always possible to maintain the bucket batch size. You can drop the batches that do not maintain the bucket batch size by using the option `drop_remainder`. Using the same input data as in the above example you get the following result.\
\
    elements = [\
\
    dataset = tf.data.Dataset.from_generator(\
\
    dataset = dataset.apply(\
\
    for elem in dataset.as_numpy_iterator():\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `element_length_func` | function from element in `Dataset` to [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>, determines the length of the element, which will determine the bucket it goes into. |\
| `bucket_boundaries` | `list<int>`, upper length boundaries of the buckets. |\
| `bucket_batch_sizes` | `list<int>`, batch size per bucket. Length should be `len(bucket_boundaries) + 1`. |\
| `padded_shapes` | Nested structure of [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> to pass to [`tf.data.Dataset.padded_batch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#padded_batch)<br>. If not provided, will use `dataset.output_shapes`, which will result in variable length dimensions being padded out to the maximum length in each batch. |\
| `padding_values` | Values to pad with, passed to [`tf.data.Dataset.padded_batch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#padded_batch)<br>. Defaults to padding with 0. |\
| `pad_to_bucket_boundary` | bool, if `False`, will pad dimensions with unknown size to maximum length in batch. If `True`, will pad dimensions with unknown size to bucket boundary minus 1 (i.e., the maximum length in each bucket), and caller must ensure that the source `Dataset` does not contain any elements with length longer than `max(bucket_boundaries)`. |\
| `no_padding` | `bool`, indicates whether to pad the batch features (features need to be either of type [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br> or of same shape). |\
| `drop_remainder` | (Optional.) A [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing whether the last batch should be dropped in the case it has fewer than `batch_size` elements; the default behavior is not to drop the smaller batch. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#apply)<br>. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | if `len(bucket_batch_sizes) != len(bucket_boundaries) + 1`. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.