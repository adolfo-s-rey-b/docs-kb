[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdata%2Fexperimental%2FRandomDataset%3Fversion%3Dstable&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#methods_2)
    *   [apply](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#apply)
        
    *   [as\_numpy\_iterator](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#as_numpy_iterator)
        
    *   [batch](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#batch)
        
    *   [bucket\_by\_sequence\_length](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#bucket_by_sequence_length)
        
    *   [cache](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#cache)
        
    *   [cardinality](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#cardinality)
        
    *   [choose\_from\_datasets](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#choose_from_datasets)
        
    *   [concatenate](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#concatenate)
        
    *   [counter](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#counter)
        
    *   [enumerate](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#enumerate)
        
    *   [filter](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#filter)
        
    *   [fingerprint](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#fingerprint)
        
    *   [flat\_map](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#flat_map)
        
    *   [from\_generator](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#from_generator)
        
    *   [from\_tensor\_slices](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#from_tensor_slices)
        
    *   [from\_tensors](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#from_tensors)
        
    *   [get\_single\_element](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#get_single_element)
        
    *   [group\_by\_window](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#group_by_window)
        
    *   [ignore\_errors](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#ignore_errors)
        
    *   [interleave](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#interleave)
        
    *   [list\_files](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#list_files)
        
    *   [load](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#load)
        
    *   [map](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#map)
        
    *   [options](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#options)
        
    *   [padded\_batch](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#padded_batch)
        
    *   [prefetch](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#prefetch)
        
    *   [ragged\_batch](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#ragged_batch)
        
    *   [random](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#random)
        
    *   [range](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#range)
        
    *   [rebatch](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#rebatch)
        
    *   [reduce](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#reduce)
        
    *   [rejection\_resample](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#rejection_resample)
        
    *   [repeat](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#repeat)
        
    *   [sample\_from\_datasets](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#sample_from_datasets)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#save)
        
    *   [scan](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#scan)
        
    *   [shard](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#shard)
        
    *   [shuffle](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#shuffle)
        
    *   [skip](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#skip)
        
    *   [snapshot](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#snapshot)
        
    *   [sparse\_batch](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#sparse_batch)
        
    *   [take](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#take)
        
    *   [take\_while](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#take_while)
        
    *   [unbatch](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#unbatch)
        
    *   [unique](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#unique)
        
    *   [window](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#window)
        
    *   [with\_options](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#with_options)
        
    *   [zip](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#zip)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#__bool__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#__len__)
        
    *   [\_\_nonzero\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#__nonzero__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.RandomDataset Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#methods_2)
    *   [apply](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#apply)
        
    *   [as\_numpy\_iterator](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#as_numpy_iterator)
        
    *   [batch](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#batch)
        
    *   [bucket\_by\_sequence\_length](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#bucket_by_sequence_length)
        
    *   [cache](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#cache)
        
    *   [cardinality](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#cardinality)
        
    *   [choose\_from\_datasets](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#choose_from_datasets)
        
    *   [concatenate](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#concatenate)
        
    *   [counter](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#counter)
        
    *   [enumerate](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#enumerate)
        
    *   [filter](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#filter)
        
    *   [fingerprint](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#fingerprint)
        
    *   [flat\_map](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#flat_map)
        
    *   [from\_generator](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#from_generator)
        
    *   [from\_tensor\_slices](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#from_tensor_slices)
        
    *   [from\_tensors](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#from_tensors)
        
    *   [get\_single\_element](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#get_single_element)
        
    *   [group\_by\_window](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#group_by_window)
        
    *   [ignore\_errors](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#ignore_errors)
        
    *   [interleave](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#interleave)
        
    *   [list\_files](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#list_files)
        
    *   [load](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#load)
        
    *   [map](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#map)
        
    *   [options](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#options)
        
    *   [padded\_batch](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#padded_batch)
        
    *   [prefetch](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#prefetch)
        
    *   [ragged\_batch](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#ragged_batch)
        
    *   [random](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#random)
        
    *   [range](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#range)
        
    *   [rebatch](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#rebatch)
        
    *   [reduce](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#reduce)
        
    *   [rejection\_resample](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#rejection_resample)
        
    *   [repeat](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#repeat)
        
    *   [sample\_from\_datasets](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#sample_from_datasets)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#save)
        
    *   [scan](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#scan)
        
    *   [shard](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#shard)
        
    *   [shuffle](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#shuffle)
        
    *   [skip](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#skip)
        
    *   [snapshot](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#snapshot)
        
    *   [sparse\_batch](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#sparse_batch)
        
    *   [take](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#take)
        
    *   [take\_while](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#take_while)
        
    *   [unbatch](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#unbatch)
        
    *   [unique](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#unique)
        
    *   [window](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#window)
        
    *   [with\_options](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#with_options)
        
    *   [zip](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#zip)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#__bool__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#__len__)
        
    *   [\_\_nonzero\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/RandomDataset?version=stable#__nonzero__)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/random_ops.py#L27-L30)

A `Dataset` of pseudorandom values. (deprecated)

Inherits From: [`Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)

tf.data.experimental.RandomDataset(
        seed=None, rerandomize_each_iteration=None, name=None
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `element_spec` | The type specification of an element of this dataset.<br><br>    dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])<br><br>For more information, read [this guide](https://www.tensorflow.org/guide/data#dataset_structure)<br>. |

Methods
-------

### `apply`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L2566-L2593)

apply(
        transformation_func
    ) -> 'DatasetV2'

Applies a transformation function to this dataset.

`apply` enables chaining of custom `Dataset` transformations, which are represented as functions that take one `Dataset` argument and return a transformed `Dataset`.

    dataset = tf.data.Dataset.range(100)

|     |     |
| --- | --- |
| Args |     |
| `transformation_func` | A function that takes one `Dataset` argument and returns a `Dataset`. |

|     |
| --- |
| Returns |     |
| A new `Dataset` with the transformation applied as described above. |     |

### `as_numpy_iterator`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L571-L628)

as_numpy_iterator()

Returns an iterator which converts all elements of the dataset to numpy.

Use `as_numpy_iterator` to inspect the content of your dataset. To see element shapes and types, print dataset elements directly instead of using `as_numpy_iterator`.

    dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])

This method requires that you are running in eager mode and the dataset's element\_spec contains only `TensorSpec` components.

    dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])

    dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])

`as_numpy_iterator()` will preserve the nested structure of dataset elements.

    dataset = tf.data.Dataset.from_tensor_slices({'a': ([1, 2], [3, 4]),

|     |
| --- |
| Returns |     |
| An iterable over the elements of the dataset, with their tensors converted to numpy arrays. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | if an element contains a non-`Tensor` value. |
| `RuntimeError` | if eager execution is not enabled. |

### `batch`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1854-L1917)

batch(
        batch_size,
        drop_remainder=False,
        num_parallel_calls=None,
        deterministic=None,
        name=None
    ) -> 'DatasetV2'

Combines consecutive elements of this dataset into batches.

    dataset = tf.data.Dataset.range(8)

    dataset = tf.data.Dataset.range(8)

The components of the resulting element will have an additional outer dimension, which will be `batch_size` (or `N % batch_size` for the last element if `batch_size` does not divide the number of input elements `N` evenly and `drop_remainder` is `False`). If your program depends on the batches having the same outer dimension, you should set the `drop_remainder` argument to `True` to prevent the smaller batch from being produced.

|     |     |
| --- | --- |
| Args |     |
| `batch_size` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of consecutive elements of this dataset to combine in a single batch. |
| `drop_remainder` | (Optional.) A [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing whether the last batch should be dropped in the case it has fewer than `batch_size` elements; the default behavior is not to drop the smaller batch. |
| `num_parallel_calls` | (Optional.) A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of batches to compute asynchronously in parallel. If not specified, batches will be computed sequentially. If the value [`tf.data.AUTOTUNE`](https://www.tensorflow.org/api_docs/python/tf/data#AUTOTUNE)<br> is used, then the number of parallel calls is set dynamically based on available resources. |
| `deterministic` | (Optional.) When `num_parallel_calls` is specified, if this boolean is specified (`True` or `False`), it controls the order in which the transformation produces elements. If set to `False`, the transformation is allowed to yield elements out of order to trade determinism for performance. If not specified, the [`tf.data.Options.deterministic`](https://www.tensorflow.org/api_docs/python/tf/data/Options#deterministic)<br> option (`True` by default) controls the behavior. |
| `name` | (Optional.) A name for the tf.data operation. |

|     |
| --- |
| Returns |     |
| A new `Dataset` with the transformation applied as described above. |     |

### `bucket_by_sequence_length`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L3105-L3252)

bucket_by_sequence_length(
        element_length_func,
        bucket_boundaries,
        bucket_batch_sizes,
        padded_shapes=None,
        padding_values=None,
        pad_to_bucket_boundary=False,
        no_padding=False,
        drop_remainder=False,
        name=None
    ) -> 'DatasetV2'

A transformation that buckets elements in a `Dataset` by length.

Elements of the `Dataset` are grouped together by length and then are padded and batched.

This is useful for sequence tasks in which the elements have variable length. Grouping together elements that have similar lengths reduces the total fraction of padding in a batch which increases training step efficiency.

Below is an example to bucketize the input data to the 3 buckets "\[0, 3), \[3, 5), \[5, inf)" based on sequence length, with batch size 2.\
\
    elements = [\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `element_length_func` | function from element in `Dataset` to [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>, determines the length of the element, which will determine the bucket it goes into. |\
| `bucket_boundaries` | `list<int>`, upper length boundaries of the buckets. |\
| `bucket_batch_sizes` | `list<int>`, batch size per bucket. Length should be `len(bucket_boundaries) + 1`. |\
| `padded_shapes` | Nested structure of [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> to pass to [`tf.data.Dataset.padded_batch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#padded_batch)<br>. If not provided, will use `dataset.output_shapes`, which will result in variable length dimensions being padded out to the maximum length in each batch. |\
| `padding_values` | Values to pad with, passed to [`tf.data.Dataset.padded_batch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#padded_batch)<br>. Defaults to padding with 0. |\
| `pad_to_bucket_boundary` | bool, if `False`, will pad dimensions with unknown size to maximum length in batch. If `True`, will pad dimensions with unknown size to bucket boundary minus 1 (i.e., the maximum length in each bucket), and caller must ensure that the source `Dataset` does not contain any elements with length longer than `max(bucket_boundaries)`. |\
| `no_padding` | `bool`, indicates whether to pad the batch features (features need to be either of type [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br> or of same shape). |\
| `drop_remainder` | (Optional.) A [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing whether the last batch should be dropped in the case it has fewer than `batch_size` elements; the default behavior is not to drop the smaller batch. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `ValueError` | if `len(bucket_batch_sizes) != len(bucket_boundaries) + 1`. |\
\
### `cache`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1513-L1569)\
\
cache(\
        filename='', name=None\
    ) -> 'DatasetV2'\
\
Caches the elements in this dataset.\
\
The first time the dataset is iterated over, its elements will be cached either in the specified file or in memory. Subsequent iterations will use the cached data.\
\
    dataset = tf.data.Dataset.range(5)\
\
When caching to a file, the cached data will persist across runs. Even the first iteration through the data will read from the cache file. Changing the input pipeline before the call to `.cache()` will have no effect until the cache file is removed or the filename is changed.\
\
dataset = tf.data.Dataset.range(5)\
    dataset = dataset.cache("/path/to/file")\
    list(dataset.as_numpy_iterator())\
    # [0, 1, 2, 3, 4]\
    dataset = tf.data.Dataset.range(10)\
    dataset = dataset.cache("/path/to/file")  # Same file!\
    list(dataset.as_numpy_iterator())\
    # [0, 1, 2, 3, 4]\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `filename` | A [`tf.string`](https://www.tensorflow.org/api_docs/python/tf#string)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the name of a directory on the filesystem to use for caching elements in this Dataset. If a filename is not provided, the dataset will be cached in memory. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `cardinality`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L3014-L3040)\
\
cardinality()\
\
Returns the cardinality of the dataset, if known.\
\
`cardinality` may return [`tf.data.INFINITE_CARDINALITY`](https://www.tensorflow.org/api_docs/python/tf/data#INFINITE_CARDINALITY)\
 if the dataset contains an infinite number of elements or [`tf.data.UNKNOWN_CARDINALITY`](https://www.tensorflow.org/api_docs/python/tf/data#UNKNOWN_CARDINALITY)\
 if the analysis fails to determine the number of elements in the dataset (e.g. when the dataset source is a file).\
\
    dataset = tf.data.Dataset.range(42)\
\
|     |\
| --- |\
| Returns |     |\
| A scalar [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> `Tensor` representing the cardinality of the dataset. If the cardinality is infinite or unknown, `cardinality` returns the named constants [`tf.data.INFINITE_CARDINALITY`](https://www.tensorflow.org/api_docs/python/tf/data#INFINITE_CARDINALITY)<br> and [`tf.data.UNKNOWN_CARDINALITY`](https://www.tensorflow.org/api_docs/python/tf/data#UNKNOWN_CARDINALITY)<br> respectively. |     |\
\
### `choose_from_datasets`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L3657-L3707)\
\
@staticmethod\
\
Creates a dataset that deterministically chooses elements from `datasets`.\
\
For example, given the following datasets:\
\
datasets = [tf.data.Dataset.from_tensors("foo").repeat(),\
                tf.data.Dataset.from_tensors("bar").repeat(),\
                tf.data.Dataset.from_tensors("baz").repeat()]\
    \
    # Define a dataset containing `[0, 1, 2, 0, 1, 2, 0, 1, 2]`.\
    choice_dataset = tf.data.Dataset.range(3).repeat(3)\
    \
    result = tf.data.Dataset.choose_from_datasets(datasets, choice_dataset)\
\
The elements of `result` will be:\
\
"foo", "bar", "baz", "foo", "bar", "baz", "foo", "bar", "baz"\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `datasets` | A non-empty list of [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> objects with compatible structure. |\
| `choice_dataset` | A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> of scalar [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> tensors between `0` and `len(datasets) - 1`. |\
| `stop_on_empty_dataset` | If `True`, selection stops if it encounters an empty dataset. If `False`, it skips empty datasets. It is recommended to set it to `True`. Otherwise, the selected elements start off as the user intends, but may change as input datasets become empty. This can be difficult to detect since the dataset starts off looking correct. Defaults to `True`. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `TypeError` | If `datasets` or `choice_dataset` has the wrong type. |\
| `ValueError` | If `datasets` is empty. |\
\
### `concatenate`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1091-L1124)\
\
concatenate(\
        dataset, name=None\
    ) -> 'DatasetV2'\
\
Creates a `Dataset` by concatenating the given dataset with this dataset.\
\
    a = tf.data.Dataset.range(1, 4)  # ==> [ 1, 2, 3 ]\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `dataset` | `Dataset` to be concatenated. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `counter`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1126-L1166)\
\
@staticmethod\
\
Creates a `Dataset` that counts from `start` in steps of size `step`.\
\
Unlike [`tf.data.Dataset.range`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#range)\
, which stops at some ending number, [`tf.data.Dataset.counter`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#counter)\
 produces elements indefinitely.\
\
    dataset = tf.data.experimental.Counter().take(5)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `start` | (Optional.) The starting value for the counter. Defaults to 0. |\
| `step` | (Optional.) The step size for the counter. Defaults to 1. |\
| `dtype` | (Optional.) The data type for counter elements. Defaults to [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A `Dataset` of scalar `dtype` elements. |     |\
\
### `enumerate`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1380-L1417)\
\
enumerate(\
        start=0, name=None\
    ) -> 'DatasetV2'\
\
Enumerates the elements of this dataset.\
\
It is similar to python's `enumerate`.\
\
    dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])\
\
    # The (nested) structure of the input dataset determines the\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `start` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the start value for enumeration. |\
| `name` | Optional. A name for the tf.data operations used by `enumerate`. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `filter`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L2538-L2564)\
\
filter(\
        predicate, name=None\
    ) -> 'DatasetV2'\
\
Filters this dataset according to `predicate`.\
\
    dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `predicate` | A function mapping a dataset element to a boolean. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `fingerprint`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1168-L1184)\
\
fingerprint()\
\
Computes the fingerprint of this `Dataset`.\
\
If two datasets have the same fingerprint, it is guaranteed that they would produce identical elements as long as the content of the upstream input files does not change and they produce data deterministically.\
\
However, two datasets producing identical values does not always mean they would have the same fingerprint due to different graph constructs.\
\
In other words, if two datasets have different fingerprints, they could still produce identical values.\
\
|     |\
| --- |\
| Returns |     |\
| A scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type [`tf.uint64`](https://www.tensorflow.org/api_docs/python/tf#uint64)<br>. |     |\
\
### `flat_map`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L2352-L2390)\
\
flat_map(\
        map_func, name=None\
    ) -> 'DatasetV2'\
\
Maps `map_func` across this dataset and flattens the result.\
\
#### The type signature is:\
\
def flat_map(\
      self: Dataset[T],\
      map_func: Callable[[T], Dataset[S]]\
    ) -> Dataset[S]\
\
Use `flat_map` if you want to make sure that the order of your dataset stays the same. For example, to flatten a dataset of batches into a dataset of their elements:\
\
    dataset = tf.data.Dataset.from_tensor_slices(\
\
[`tf.data.Dataset.interleave()`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave)\
 is a generalization of `flat_map`, since `flat_map` produces the same output as [`tf.data.Dataset.interleave(cycle_length=1)`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `map_func` | A function mapping a dataset element to a dataset. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `from_generator`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L874-L972)\
\
@staticmethod\
\
Creates a `Dataset` whose elements are generated by `generator`. (deprecated arguments)\
\
The `generator` argument must be a callable object that returns an object that supports the `iter()` protocol (e.g. a generator function).\
\
The elements generated by `generator` must be compatible with either the given `output_signature` argument or with the given `output_types` and (optionally) `output_shapes` arguments, whichever was specified.\
\
The recommended way to call `from_generator` is to use the `output_signature` argument. In this case the output will be assumed to consist of objects with the classes, shapes and types defined by [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)\
 objects from `output_signature` argument:\
\
    def gen():\
\
There is also a deprecated way to call `from_generator` by either with `output_types` argument alone or together with `output_shapes` argument. In this case the output of the function will be assumed to consist of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
 objects with the types defined by `output_types` and with the shapes which are either unknown or defined by `output_shapes`.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `generator` | A callable object that returns an object that supports the `iter()` protocol. If `args` is not specified, `generator` must take no arguments; otherwise it must take as many arguments as there are values in `args`. |\
| `output_types` | (Optional.) A (nested) structure of [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> objects corresponding to each component of an element yielded by `generator`. |\
| `output_shapes` | (Optional.) A (nested) structure of [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> objects corresponding to each component of an element yielded by `generator`. |\
| `args` | (Optional.) A tuple of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> objects that will be evaluated and passed to `generator` as NumPy-array arguments. |\
| `output_signature` | (Optional.) A (nested) structure of [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)<br> objects corresponding to each component of an element yielded by `generator`. |\
| `name` | (Optional.) A name for the tf.data operations used by `from_generator`. |\
\
|     |     |\
| --- | --- |\
| Returns |     |\
| `Dataset` | A `Dataset`. |\
\
### `from_tensor_slices`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L744-L828)\
\
@staticmethod\
\
Creates a `Dataset` whose elements are slices of the given tensors.\
\
The given tensors are sliced along their first dimension. This operation preserves the structure of the input tensors, removing the first dimension of each tensor and using it as the dataset dimension. All input tensors must have the same size in their first dimensions.\
\
    # Slicing a 1D tensor produces scalar tensor elements.\
\
    # Slicing a 2D tensor produces 1D tensor elements.\
\
    # Slicing a tuple of 1D tensors produces tuple elements containing\
\
    # Dictionary structure is also preserved.\
\
    # Two tensors can be combined into one Dataset object.\
\
Note that if `tensors` contains a NumPy array, and eager execution is not enabled, the values will be embedded in the graph as one or more [`tf.constant`](https://www.tensorflow.org/api_docs/python/tf/constant)\
 operations. For large datasets (> 1 GB), this can waste memory and run into byte limits of graph serialization. If `tensors` contains one or more large NumPy arrays, consider the alternative described in [this guide](https://tensorflow.org/guide/data#consuming_numpy_arrays)\
.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `tensors` | A dataset element, whose components have the same first dimension. Supported values are documented [here](https://www.tensorflow.org/guide/data#dataset_structure)<br>. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |     |\
| --- | --- |\
| Returns |     |\
| `Dataset` | A `Dataset`. |\
\
### `from_tensors`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L700-L742)\
\
@staticmethod\
\
Creates a `Dataset` with a single element, comprising the given tensors.\
\
`from_tensors` produces a dataset containing only a single element. To slice the input tensor into multiple elements, use `from_tensor_slices` instead.\
\
    dataset = tf.data.Dataset.from_tensors([1, 2, 3])\
\
    # You can use `from_tensors` to produce a dataset which repeats\
\
Note that if `tensors` contains a NumPy array, and eager execution is not enabled, the values will be embedded in the graph as one or more [`tf.constant`](https://www.tensorflow.org/api_docs/python/tf/constant)\
 operations. For large datasets (> 1 GB), this can waste memory and run into byte limits of graph serialization. If `tensors` contains one or more large NumPy arrays, consider the alternative described in [this guide](https://tensorflow.org/guide/data#consuming_numpy_arrays)\
.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `tensors` | A dataset "element". Supported values are documented [here](https://www.tensorflow.org/guide/data#dataset_structure)<br>. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |     |\
| --- | --- |\
| Returns |     |\
| `Dataset` | A `Dataset`. |\
\
### `get_single_element`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L2866-L2953)\
\
get_single_element(\
        name=None\
    )\
\
Returns the single element of the `dataset`.\
\
The function enables you to use a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)\
 in a stateless "tensor-in tensor-out" expression, without creating an iterator. This facilitates the ease of data transformation on tensors using the optimized [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)\
 abstraction on top of them.\
\
For example, lets consider a `preprocessing_fn` which would take as an input the raw features and returns the processed feature along with it's label.\
\
def preprocessing_fn(raw_feature):\
      # ... the raw_feature is preprocessed as per the use-case\
      return feature\
    \
    raw_features = ...  # input batch of BATCH_SIZE elements.\
    dataset = (tf.data.Dataset.from_tensor_slices(raw_features)\
              .map(preprocessing_fn, num_parallel_calls=BATCH_SIZE)\
              .batch(BATCH_SIZE))\
    \
    processed_features = dataset.get_single_element()\
\
In the above example, the `raw_features` tensor of length=BATCH\_SIZE was converted to a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)\
. Next, each of the `raw_feature` was mapped using the `preprocessing_fn` and the processed features were grouped into a single batch. The final `dataset` contains only one element which is a batch of all the processed features.\
\
Now, instead of creating an iterator for the `dataset` and retrieving the batch of features, the `tf.data.get_single_element()` function is used to skip the iterator creation process and directly output the batch of features.\
\
This can be particularly useful when your tensor transformations are expressed as [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)\
 operations, and you want to use those transformations while serving your model.\
\
#### Keras\
\
model = ... # A pre-built or custom model\
    \
    class PreprocessingModel(tf.keras.Model):\
      def __init__(self, model):\
        super().__init__(self)\
        self.model = model\
    \
      @tf.function(input_signature=[...])\
      def serving_fn(self, data):\
        ds = tf.data.Dataset.from_tensor_slices(data)\
        ds = ds.map(preprocessing_fn, num_parallel_calls=BATCH_SIZE)\
        ds = ds.batch(batch_size=BATCH_SIZE)\
        return tf.argmax(self.model(ds.get_single_element()), axis=-1)\
    \
    preprocessing_model = PreprocessingModel(model)\
    your_exported_model_dir = ... # save the model to this path.\
    tf.saved_model.save(preprocessing_model, your_exported_model_dir,\
                  signatures={'serving_default': preprocessing_model.serving_fn}\
                  )\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A nested structure of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> objects, corresponding to the single element of `dataset`. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `InvalidArgumentError` | (at runtime) if `dataset` does not contain exactly one element. |\
\
### `group_by_window`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L3042-L3103)\
\
group_by_window(\
        key_func, reduce_func, window_size=None, window_size_func=None, name=None\
    ) -> 'DatasetV2'\
\
Groups windows of elements by key and reduces them.\
\
This transformation maps each consecutive element in a dataset to a key using `key_func` and groups the elements by key. It then applies `reduce_func` to at most `window_size_func(key)` elements matching the same key. All except the final window for each key will contain `window_size_func(key)` elements; the final window may be smaller.\
\
You may provide either a constant `window_size` or a window size determined by the key through `window_size_func`.\
\
    dataset = tf.data.Dataset.range(10)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `key_func` | A function mapping a nested structure of tensors (having shapes and types defined by `self.output_shapes` and `self.output_types`) to a scalar [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> tensor. |\
| `reduce_func` | A function mapping a key and a dataset of up to `window_size` consecutive elements matching that key to another dataset. |\
| `window_size` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of consecutive elements matching the same key to combine in a single batch, which will be passed to `reduce_func`. Mutually exclusive with `window_size_func`. |\
| `window_size_func` | A function mapping a key to a [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of consecutive elements matching the same key to combine in a single batch, which will be passed to `reduce_func`. Mutually exclusive with `window_size`. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `ValueError` | if neither or both of {`window_size`, `window_size_func`} are passed. |\
\
### `ignore_errors`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L2392-L2418)\
\
ignore_errors(\
        log_warning=False, name=None\
    ) -> 'DatasetV2'\
\
Drops elements that cause errors.\
\
    dataset = tf.data.Dataset.from_tensor_slices([1., 2., 0., 4.])\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `log_warning` | (Optional.) A bool indicating whether or not ignored errors should be logged to stderr. Defaults to `False`. |\
| `name` | (Optional.) A string indicating a name for the [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)<br> operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `interleave`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L2420-L2536)\
\
interleave(\
        map_func,\
        cycle_length=None,\
        block_length=None,\
        num_parallel_calls=None,\
        deterministic=None,\
        name=None\
    ) -> 'DatasetV2'\
\
Maps `map_func` across this dataset, and interleaves the results.\
\
#### The type signature is:\
\
def interleave(\
      self: Dataset[T],\
      map_func: Callable[[T], Dataset[S]]\
    ) -> Dataset[S]\
\
For example, you can use [`Dataset.interleave()`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave)\
 to process many input files concurrently:\
\
    # Preprocess 4 files concurrently, and interleave blocks of 16 records\
\
The `cycle_length` and `block_length` arguments control the order in which elements are produced. `cycle_length` controls the number of input elements that are processed concurrently. If you set `cycle_length` to 1, this transformation will handle one input element at a time, and will produce identical results to [`tf.data.Dataset.flat_map`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#flat_map)\
. In general, this transformation will apply `map_func` to `cycle_length` input elements, open iterators on the returned `Dataset` objects, and cycle through them producing `block_length` consecutive elements from each iterator, and consuming the next input element each time it reaches the end of an iterator.\
\
#### For example:\
\
    dataset = Dataset.range(1, 6)  # ==> [ 1, 2, 3, 4, 5 ]\
\
Performance can often be improved by setting `num_parallel_calls` so that `interleave` will use multiple threads to fetch elements. If determinism isn't required, it can also improve performance to set `deterministic=False`.\
\
    filenames = ["/var/data/file1.txt", "/var/data/file2.txt",\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `map_func` | A function that takes a dataset element and returns a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>. |\
| `cycle_length` | (Optional.) The number of input elements that will be processed concurrently. If not set, the tf.data runtime decides what it should be based on available CPU. If `num_parallel_calls` is set to [`tf.data.AUTOTUNE`](https://www.tensorflow.org/api_docs/python/tf/data#AUTOTUNE)<br>, the `cycle_length` argument identifies the maximum degree of parallelism. |\
| `block_length` | (Optional.) The number of consecutive elements to produce from each input element before cycling to another input element. If not set, defaults to 1. |\
| `num_parallel_calls` | (Optional.) If specified, the implementation creates a threadpool, which is used to fetch inputs from cycle elements asynchronously and in parallel. The default behavior is to fetch inputs from cycle elements synchronously with no parallelism. If the value [`tf.data.AUTOTUNE`](https://www.tensorflow.org/api_docs/python/tf/data#AUTOTUNE)<br> is used, then the number of parallel calls is set dynamically based on available CPU. |\
| `deterministic` | (Optional.) When `num_parallel_calls` is specified, if this boolean is specified (`True` or `False`), it controls the order in which the transformation produces elements. If set to `False`, the transformation is allowed to yield elements out of order to trade determinism for performance. If not specified, the [`tf.data.Options.deterministic`](https://www.tensorflow.org/api_docs/python/tf/data/Options#deterministic)<br> option (`True` by default) controls the behavior. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `list_files`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1271-L1350)\
\
@staticmethod\
\
A dataset of all files matching one or more glob patterns.\
\
The `file_pattern` argument should be a small number of glob patterns. If your filenames have already been globbed, use [`Dataset.from_tensor_slices(filenames)`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#from_tensor_slices)\
 instead, as re-globbing every filename with `list_files` may result in poor performance with remote storage systems.\
\
|     |\
| --- |\
| Example |     |\
| If we had the following files on our filesystem:<br><br>*   /path/to/dir/a.txt<br>*   /path/to/dir/b.py<br>*   /path/to/dir/c.py<br><br>If we pass "/path/to/dir/\*.py" as the directory, the dataset would produce:<br><br>*   /path/to/dir/b.py<br>*   /path/to/dir/c.py |     |\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `file_pattern` | A string, a list of strings, or a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of string type (scalar or vector), representing the filename glob (i.e. shell wildcard) pattern(s) that will be matched. |\
| `shuffle` | (Optional.) If `True`, the file names will be shuffled randomly. Defaults to `True`. |\
| `seed` | (Optional.) A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the random seed that will be used to create the distribution. See [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)<br> for behavior. |\
| `name` | Optional. A name for the tf.data operations used by `list_files`. |\
\
|     |     |\
| --- | --- |\
| Returns |     |\
| `Dataset` | A `Dataset` of strings corresponding to file names. |\
\
### `load`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1777-L1852)\
\
@staticmethod\
\
Loads a previously saved dataset.\
\
#### Example usage:\
\
    import tempfile\
\
If the default option of sharding the saved dataset was used, the element order of the saved dataset will be preserved when loading it.\
\
The `reader_func` argument can be used to specify a custom order in which elements should be loaded from the individual shards. The `reader_func` is expected to take a single argument -- a dataset of datasets, each containing elements of one of the shards -- and return a dataset of elements. For example, the order of shards can be shuffled when loading them as follows:\
\
def custom_reader_func(datasets):\
      datasets = datasets.shuffle(NUM_SHARDS)\
      return datasets.interleave(lambda x: x, num_parallel_calls=AUTOTUNE)\
    \
    dataset = tf.data.Dataset.load(\
        path="/path/to/data", ..., reader_func=custom_reader_func)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `path` | Required. A path pointing to a previously saved dataset. |\
| `element_spec` | Optional. A nested structure of [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)<br> objects matching the structure of an element of the saved dataset and specifying the type of individual element components. If not provided, the nested structure of [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)<br> saved with the saved dataset is used. Note that this argument is required in graph mode. |\
| `compression` | Optional. The algorithm to use to decompress the data when reading it. Supported options are `GZIP` and `NONE`. Defaults to `NONE`. |\
| `reader_func` | Optional. A function to control how to read data from shards. If present, the function will be traced and executed as graph computation. |\
| `wait` | If `True`, for snapshots written with `distributed_save`, it reads the snapshot while it is being written. For snapshots written with regular `save`, it waits for the snapshot until it's finished. The default is `False` for backward compatibility. Users of `distributed_save` are recommended to set it to `True`. |\
\
|     |\
| --- |\
| Returns |     |\
| A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> instance. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `FileNotFoundError` | If `element_spec` is not specified and the saved nested structure of [`tf.TypeSpec`](https://www.tensorflow.org/api_docs/python/tf/TypeSpec)<br> can not be located with the saved dataset. |\
| `ValueError` | If `element_spec` is not specified and the method is executed in graph mode. |\
\
### `map`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L2163-L2350)\
\
map(\
        map_func,\
        num_parallel_calls=None,\
        deterministic=None,\
        synchronous=None,\
        use_unbounded_threadpool=False,\
        name=None\
    )\
\
Maps `map_func` across the elements of this dataset.\
\
This transformation applies `map_func` to each element of this dataset, and returns a new dataset containing the transformed elements, in the same order as they appeared in the input. `map_func` can be used to change both the values and the structure of a dataset's elements. Supported structure constructs are documented [here](https://www.tensorflow.org/guide/data#dataset_structure)\
.\
\
For example, `map` can be used for adding 1 to each element, or projecting a subset of element components.\
\
    dataset = Dataset.range(1, 6)  # ==> [ 1, 2, 3, 4, 5 ]\
\
The input signature of `map_func` is determined by the structure of each element in this dataset.\
\
    dataset = Dataset.range(5)\
\
    # Each element is a tuple containing two `tf.Tensor` objects.\
\
    # Each element is a dictionary mapping strings to `tf.Tensor` objects.\
\
The value or values returned by `map_func` determine the structure of each element in the returned dataset.\
\
    dataset = tf.data.Dataset.range(3)\
\
`map_func` can accept as arguments and return any type of dataset element.\
\
Note that irrespective of the context in which `map_func` is defined (eager vs. graph), tf.data traces the function and executes it as a graph. To use Python code inside of the function you have a few options:\
\
1) Rely on AutoGraph to convert Python code into an equivalent graph computation. The downside of this approach is that AutoGraph can convert some but not all Python code.\
\
2) Use [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)\
, which allows you to write arbitrary Python code but will generally result in worse performance than 1). For example:\
\
    d = tf.data.Dataset.from_tensor_slices(['hello', 'world'])\
\
3) Use [`tf.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)\
, which also allows you to write arbitrary Python code. Note that [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)\
 accepts [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
 whereas [`tf.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)\
 accepts numpy arrays and returns only numpy arrays. For example:\
\
    d = tf.data.Dataset.from_tensor_slices(['hello', 'world'])\
\
Note that the use of [`tf.numpy_function`](https://www.tensorflow.org/api_docs/python/tf/numpy_function)\
 and [`tf.py_function`](https://www.tensorflow.org/api_docs/python/tf/py_function)\
 in general precludes the possibility of executing user-defined transformations in parallel (because of Python GIL).\
\
Performance can often be improved by setting `num_parallel_calls` so that `map` will use multiple threads to process elements. If deterministic order isn't required, it can also improve performance to set `deterministic=False`.\
\
    dataset = Dataset.range(1, 6)  # ==> [ 1, 2, 3, 4, 5 ]\
\
The order of elements yielded by this transformation is deterministic if `deterministic=True`. If `map_func` contains stateful operations and `num_parallel_calls > 1`, the order in which that state is accessed is undefined, so the values of output elements may not be deterministic regardless of the `deterministic` flag value.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `map_func` | A function mapping a dataset element to another dataset element. |\
| `num_parallel_calls` | (Optional.) A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number elements to process asynchronously in parallel. If the value [`tf.data.AUTOTUNE`](https://www.tensorflow.org/api_docs/python/tf/data#AUTOTUNE)<br> is used, then the number of parallel calls is set dynamically based on available CPU. If not specified, the `tf.data.Options.experimental_optimization.map_parallelization` option (`True` by default) controls whether the map will run as with [`tf.data.AUTOTUNE`](https://www.tensorflow.org/api_docs/python/tf/data#AUTOTUNE)<br> or run sequentially. |\
| `deterministic` | (Optional.) When `num_parallel_calls` is specified, if this boolean is specified (`True` or `False`), it controls the order in which the transformation produces elements. If set to `False`, the transformation is allowed to yield elements out of order to trade determinism for performance. If not specified, the [`tf.data.Options.deterministic`](https://www.tensorflow.org/api_docs/python/tf/data/Options#deterministic)<br> option (`True` by default) controls the behavior. |\
| `synchronous` | (Optional.) Whether to force the map transformation to run synchronously. This only matters when `options.experimental_optimization.map_parallelization=True`. That option would normally change the map to run with `num_parallel_calls=tf.data.AUTOTUNE`, but if `synchronous=True` is specified, the map will not be parallelized at all. This is useful for saving memory, since even setting `num_parallel_calls=1` will cause one batch to be buffered, while with `synchronous=True` the map transformation doesn't buffer anything. |\
| `use_unbounded_threadpool` | (Optional.) By default, map functions run in a limited threadpool based on the number of cores on the machine. This efficient for CPU-heavy processing, but if the map function performs IO it is better to use an unbounded threadpool by setting it to `True`. It is `False` by default. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `options`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L453-L471)\
\
options()\
\
Returns the options for this dataset and its inputs.\
\
|     |\
| --- |\
| Returns |     |\
| A [`tf.data.Options`](https://www.tensorflow.org/api_docs/python/tf/data/Options)<br> object representing the dataset options. |     |\
\
### `padded_batch`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1919-L2047)\
\
padded_batch(\
        batch_size,\
        padded_shapes=None,\
        padding_values=None,\
        drop_remainder=False,\
        name=None\
    ) -> 'DatasetV2'\
\
Combines consecutive elements of this dataset into padded batches.\
\
This transformation combines multiple consecutive elements of the input dataset into a single element.\
\
Like [`tf.data.Dataset.batch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#batch)\
, the components of the resulting element will have an additional outer dimension, which will be `batch_size` (or `N % batch_size` for the last element if `batch_size` does not divide the number of input elements `N` evenly and `drop_remainder` is `False`). If your program depends on the batches having the same outer dimension, you should set the `drop_remainder` argument to `True` to prevent the smaller batch from being produced.\
\
Unlike [`tf.data.Dataset.batch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#batch)\
, the input elements to be batched may have different shapes, and this transformation will pad each component to the respective shape in `padded_shapes`. The `padded_shapes` argument determines the resulting shape for each dimension of each component in an output element:\
\
*   If the dimension is a constant, the component will be padded out to that length in that dimension.\
*   If the dimension is unknown, the component will be padded out to the maximum length of all elements in that dimension.\
\
    A = (tf.data.Dataset\
\
See also [`tf.data.experimental.dense_to_sparse_batch`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/dense_to_sparse_batch)\
, which combines elements that may have different shapes into a [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)\
.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `batch_size` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of consecutive elements of this dataset to combine in a single batch. |\
| `padded_shapes` | (Optional.) A (nested) structure of [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> or [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> vector tensor-like objects representing the shape to which the respective component of each input element should be padded prior to batching. Any unknown dimensions will be padded to the maximum size of that dimension in each batch. If unset, all dimensions of all components are padded to the maximum size in the batch. `padded_shapes` must be set if any component has an unknown rank. |\
| `padding_values` | (Optional.) A (nested) structure of scalar-shaped [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the padding values to use for the respective components. None represents that the (nested) structure should be padded with default values. Defaults are `0` for numeric types and the empty string for string types. The `padding_values` should have the same (nested) structure as the input dataset. If `padding_values` is a single element and the input dataset has multiple components, then the same `padding_values` will be used to pad every component of the dataset. If `padding_values` is a scalar, then its value will be broadcasted to match the shape of each component. |\
| `drop_remainder` | (Optional.) A [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing whether the last batch should be dropped in the case it has fewer than `batch_size` elements; the default behavior is not to drop the smaller batch. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `ValueError` | If a component has an unknown rank, and the `padded_shapes` argument is not set. |\
| `TypeError` | If a component is of an unsupported type. The list of supported types is documented in [https://www.tensorflow.org/guide/data#dataset\_structure](https://www.tensorflow.org/guide/data#dataset_structure) |\
\
### `prefetch`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1240-L1269)\
\
prefetch(\
        buffer_size, name=None\
    ) -> 'DatasetV2'\
\
Creates a `Dataset` that prefetches elements from this dataset.\
\
Most dataset input pipelines should end with a call to `prefetch`. This allows later elements to be prepared while the current element is being processed. This often improves latency and throughput, at the cost of using additional memory to store prefetched elements.\
\
    dataset = tf.data.Dataset.range(3)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `buffer_size` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the maximum number of elements that will be buffered when prefetching. If the value [`tf.data.AUTOTUNE`](https://www.tensorflow.org/api_docs/python/tf/data#AUTOTUNE)<br> is used, then the buffer size is dynamically tuned. |\
| `name` | Optional. A name for the tf.data transformation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `ragged_batch`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L2049-L2112)\
\
ragged_batch(\
        batch_size,\
        drop_remainder=False,\
        row_splits_dtype=tf.dtypes.int64,\
        name=None\
    ) -> 'DatasetV2'\
\
Combines consecutive elements of this dataset into [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)\
s.\
\
Like [`tf.data.Dataset.batch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#batch)\
, the components of the resulting element will have an additional outer dimension, which will be `batch_size` (or `N % batch_size` for the last element if `batch_size` does not divide the number of input elements `N` evenly and `drop_remainder` is `False`). If your program depends on the batches having the same outer dimension, you should set the `drop_remainder` argument to `True` to prevent the smaller batch from being produced.\
\
Unlike [`tf.data.Dataset.batch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#batch)\
, the input elements to be batched may have different shapes:\
\
*   If an input element is a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
     whose static [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)\
     is fully defined, then it is batched as normal.\
*   If an input element is a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)\
     whose static [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)\
     contains one or more axes with unknown size (i.e., `shape[i]=None`), then the output will contain a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)\
     that is ragged up to any of such dimensions.\
*   If an input element is a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)\
     or any other type, then it is batched as normal.\
\
#### Example:\
\
    dataset = tf.data.Dataset.range(6)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `batch_size` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of consecutive elements of this dataset to combine in a single batch. |\
| `drop_remainder` | (Optional.) A [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing whether the last batch should be dropped in the case it has fewer than `batch_size` elements; the default behavior is not to drop the smaller batch. |\
| `row_splits_dtype` | The dtype that should be used for the `row_splits` of any new ragged tensors. Existing [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br> elements do not have their row\_splits dtype changed. |\
| `name` | (Optional.) A string indicating a name for the [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)<br> operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `random`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L3254-L3305)\
\
@staticmethod\
\
Creates a `Dataset` of pseudorandom values.\
\
The dataset generates a sequence of uniformly distributed integer values.\
\
`rerandomize_each_iteration` controls whether the sequence of random number generated should be re-randomized for each epoch. The default value is False where the dataset generates the same sequence of random numbers for each epoch.\
\
    ds1 = tf.data.Dataset.random(seed=4).take(10)\
\
    ds3 = tf.data.Dataset.random(seed=4).take(10)\
\
    ds4 = tf.data.Dataset.random(\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `seed` | (Optional) If specified, the dataset produces a deterministic sequence of values. |\
| `rerandomize_each_iteration` | (Optional) If set to False, the dataset generates the same sequence of random numbers for each epoch. If set to True, it generates a different deterministic sequence of random numbers for each epoch. It is defaulted to False if left unspecified. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |     |\
| --- | --- |\
| Returns |     |\
| `Dataset` | A `Dataset`. |\
\
### `range`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L974-L1023)\
\
@staticmethod\
\
Creates a `Dataset` of a step-separated range of values.\
\
    ds = Dataset.range(5)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `*args` | follows the same semantics as python's range. len(args) == 1 -> start = 0, stop = args\[0\], step = 1. len(args) == 2 -> start = args\[0\], stop = args\[1\], step = 1. len(args) == 3 -> start = args\[0\], stop = args\[1\], step = args\[2\]. |\
| `**kwargs` | *   output\_type: Its expected dtype. (Optional, default: [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>    ).<br>*   name: (Optional.) A name for the tf.data operation. |\
\
|     |     |\
| --- | --- |\
| Returns |     |\
| `Dataset` | A `RangeDataset`. |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `ValueError` | if len(args) == 0. |\
\
### `rebatch`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1186-L1238)\
\
rebatch(\
        batch_size, drop_remainder=False, name=None\
    ) -> 'DatasetV2'\
\
Creates a `Dataset` that rebatches the elements from this dataset.\
\
`rebatch(N)` is functionally equivalent to `unbatch().batch(N)`, but is more efficient, performing one copy instead of two.\
\
    ds = tf.data.Dataset.range(6)\
\
    ds = tf.data.Dataset.range(7)\
\
    ds = tf.data.Dataset.range(7)\
\
If the `batch_size` argument is a list, `rebatch` cycles through the list to determine the size of each batch.\
\
    ds = tf.data.Dataset.range(8)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `batch_size` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar or vector, representing the size of batches to produce. If this argument is a vector, these values are cycled through in round robin fashion. |\
| `drop_remainder` | (Optional.) A [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing whether the last batch should be dropped in the case it has fewer than `batch_size[cycle_index]` elements; the default behavior is not to drop the smaller batch. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A `Dataset` of scalar `dtype` elements. |     |\
\
### `reduce`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L2748-L2864)\
\
reduce(\
        initial_state, reduce_func, name=None\
    )\
\
Reduces the input dataset to a single element.\
\
The transformation calls `reduce_func` successively on every element of the input dataset until the dataset is exhausted, aggregating information in its internal state. The `initial_state` argument is used for the initial state and the final state is returned as the result.\
\
    tf.data.Dataset.range(5).reduce(np.int64(0), lambda x, _: x +\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `initial_state` | An element representing the initial state of the transformation. |\
| `reduce_func` | A function that maps `(old_state, input_element)` to `new_state`. It must take two arguments and return a new element The structure of `new_state` must match the structure of `initial_state`. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A dataset element corresponding to the final state of the transformation. |     |\
\
### `rejection_resample`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L3484-L3577)\
\
rejection_resample(\
        class_func, target_dist, initial_dist=None, seed=None, name=None\
    ) -> 'DatasetV2'\
\
Resamples elements to reach a target distribution.\
\
    initial_dist = [0.6, 0.4]\
\
Following from `initial_dist`, `zero` is ~0.6 and `one` is ~0.4.\
\
    target_dist = [0.5, 0.5]\
\
Following from `target_dist`, `zero` is ~0.5 and `one` is ~0.5.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `class_func` | A function mapping an element of the input dataset to a scalar [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br> tensor. Values should be in `[0, num_classes)`. |\
| `target_dist` | A floating point type tensor, shaped `[num_classes]`. |\
| `initial_dist` | (Optional.) A floating point type tensor, shaped `[num_classes]`. If not provided, the true class distribution is estimated live in a streaming fashion. |\
| `seed` | (Optional.) Python integer seed for the resampler. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `repeat`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1352-L1378)\
\
repeat(\
        count=None, name=None\
    ) -> 'DatasetV2'\
\
Repeats this dataset so each original value is seen `count` times.\
\
    dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `count` | (Optional.) A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of times the dataset should be repeated. The default behavior (if `count` is `None` or `-1`) is for the dataset be repeated indefinitely. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `sample_from_datasets`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L3579-L3655)\
\
@staticmethod\
\
Samples elements at random from the datasets in `datasets`.\
\
Creates a dataset by interleaving elements of `datasets` with `weight[i]` probability of picking an element from dataset `i`. Sampling is done without replacement. For example, suppose we have 2 datasets:\
\
dataset1 = tf.data.Dataset.range(0, 3)\
    dataset2 = tf.data.Dataset.range(100, 103)\
\
Suppose that we sample from these 2 datasets with the following weights:\
\
sample_dataset = tf.data.Dataset.sample_from_datasets(\
        [dataset1, dataset2], weights=[0.5, 0.5])\
\
One possible outcome of elements in sample\_dataset is:\
\
print(list(sample_dataset.as_numpy_iterator()))\
    # [100, 0, 1, 101, 2, 102]\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `datasets` | A non-empty list of [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> objects with compatible structure. |\
| `weights` | (Optional.) A list or Tensor of `len(datasets)` floating-point values where `weights[i]` represents the probability to sample from `datasets[i]`, or a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> object where each element is such a list. Defaults to a uniform distribution across `datasets`. |\
| `seed` | (Optional.) A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the random seed that will be used to create the distribution. See [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)<br> for behavior. |\
| `stop_on_empty_dataset` | If `True`, sampling stops if it encounters an empty dataset. If `False`, it continues sampling and skips any empty datasets. It is recommended to set it to `True`. Otherwise, the distribution of samples starts off as the user intends, but may change as input datasets become empty. This can be difficult to detect since the dataset starts off looking correct. Default to `False` for backward compatibility. |\
| `rerandomize_each_iteration` | An optional `bool`. The boolean argument controls whether the sequence of random numbers used to determine which dataset to sample from will be rerandomized each epoch. That is, it determinies whether datasets will be sampled in the same order across different epochs (the default behavior) or not. |\
\
|     |\
| --- |\
| Returns |     |\
| A dataset that interleaves elements from `datasets` at random, according to `weights` if provided, otherwise with uniform probability. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `TypeError` | If the `datasets` or `weights` arguments have the wrong type. |\
| `ValueError` | *   If `datasets` is empty, or<br>*   If `weights` is specified and does not match the length of `datasets`. |\
\
### `save`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1693-L1775)\
\
save(\
        path, compression=None, shard_func=None, checkpoint_args=None\
    )\
\
Saves the content of the given dataset.\
\
Example usage:\
\
  `import tempfile`\
  `path = os.path.join(tempfile.gettempdir(), "saved_data")`\
  `# Save a dataset`\
  `dataset = tf.data.Dataset.range(2)`\
  `dataset.save(path)`\
  `new_dataset = tf.data.Dataset.load(path)`\
  `for elem in new_dataset:`\
  `  print(elem)`\
  `  tf.Tensor(0, shape=(), dtype=int64)`\
  `  tf.Tensor(1, shape=(), dtype=int64)`\
    \
  \
\
The saved dataset is saved in multiple file "shards". By default, the dataset output is divided to shards in a round-robin fashion but custom sharding can be specified via the `shard_func` function. For example, you can save the dataset to using a single shard as follows:\
\
  dataset = make_dataset()\
      def custom_shard_func(element):\
        return np.int64(0)\
      dataset.save(\
          path="/path/to/data", ..., shard_func=custom_shard_func)\
\
To enable checkpointing, pass in `checkpoint_args` to the `save` method as follows:\
\
  dataset = tf.data.Dataset.range(100)\
      save_dir = "..."\
      checkpoint_prefix = "..."\
      step_counter = tf.Variable(0, trainable=False)\
      checkpoint_args = {\
        "checkpoint_interval": 50,\
        "step_counter": step_counter,\
        "directory": checkpoint_prefix,\
        "max_to_keep": 20,\
      }\
      dataset.save(dataset, save_dir, checkpoint_args=checkpoint_args)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `path` | Required. A directory to use for saving the dataset. |\
| `compression` | Optional. The algorithm to use to compress data when writing it. Supported options are `GZIP` and `NONE`. Defaults to `NONE`. |\
| `shard_func` | Optional. A function to control the mapping of dataset elements to file shards. The function is expected to map elements of the input dataset to int64 shard IDs. If present, the function will be traced and executed as graph computation. |\
| `checkpoint_args` | Optional args for checkpointing which will be passed into the [`tf.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)<br>. If `checkpoint_args` are not specified, then checkpointing will not be performed. The `save()` implementation creates a [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)<br> object internally, so users should not set the `checkpoint` argument in `checkpoint_args`. |\
\
|     |\
| --- |\
| Returns |     |\
| An operation which when executed performs the save. When writing checkpoints, returns None. The return value is useful in unit tests. |     |\
\
|     |\
| --- |\
| Raises |     |\
| ValueError if `checkpoint` is passed into `checkpoint_args`. |     |\
\
### `scan`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L3398-L3431)\
\
scan(\
        initial_state, scan_func, name=None\
    ) -> 'DatasetV2'\
\
A transformation that scans a function across an input dataset.\
\
This transformation is a stateful relative of [`tf.data.Dataset.map`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map)\
. In addition to mapping `scan_func` across the elements of the input dataset, `scan()` accumulates one or more state tensors, whose initial values are `initial_state`.\
\
    dataset = tf.data.Dataset.range(10)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `initial_state` | A nested structure of tensors, representing the initial state of the accumulator. |\
| `scan_func` | A function that maps `(old_state, input_element)` to `(new_state, output_element)`. It must take two arguments and return a pair of nested structures of tensors. The `new_state` must match the structure of `initial_state`. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `shard`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1621-L1691)\
\
shard(\
        num_shards, index, name=None\
    ) -> 'DatasetV2'\
\
Creates a `Dataset` that includes only 1/`num_shards` of this dataset.\
\
`shard` is deterministic. The Dataset produced by `A.shard(n, i)` will contain all elements of A whose index mod n = i.\
\
    A = tf.data.Dataset.range(10)\
\
This dataset operator is very useful when running distributed training, as it allows each worker to read a unique subset.\
\
When reading a single input file, you can shard elements as follows:\
\
d = tf.data.TFRecordDataset(input_file)\
    d = d.shard(num_workers, worker_index)\
    d = d.repeat(num_epochs)\
    d = d.shuffle(shuffle_buffer_size)\
    d = d.map(parser_fn, num_parallel_calls=num_map_threads)\
\
#### Important caveats:\
\
*   Be sure to shard before you use any randomizing operator (such as shuffle).\
*   Generally it is best if the shard operator is used early in the dataset pipeline. For example, when reading from a set of TFRecord files, shard before converting the dataset to input samples. This avoids reading every file on every worker. The following is an example of an efficient sharding strategy within a complete pipeline:\
\
d = Dataset.list_files(pattern, shuffle=False)\
    d = d.shard(num_workers, worker_index)\
    d = d.repeat(num_epochs)\
    d = d.shuffle(shuffle_buffer_size)\
    d = d.interleave(tf.data.TFRecordDataset,\
                     cycle_length=num_readers, block_length=1)\
    d = d.map(parser_fn, num_parallel_calls=num_map_threads)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `num_shards` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of shards operating in parallel. |\
| `index` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the worker index. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `InvalidArgumentError` | if `num_shards` or `index` are illegal values. |\
\
### `shuffle`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1419-L1511)\
\
shuffle(\
        buffer_size, seed=None, reshuffle_each_iteration=True, name=None\
    ) -> 'DatasetV2'\
\
Randomly shuffles the elements of this dataset.\
\
This dataset fills a buffer with `buffer_size` elements, then randomly samples elements from this buffer, replacing the selected elements with new elements. For perfect shuffling, a buffer size greater than or equal to the full size of the dataset is required.\
\
For instance, if your dataset contains 10,000 elements but `buffer_size` is set to 1,000, then `shuffle` will initially select a random element from only the first 1,000 elements in the buffer. Once an element is selected, its space in the buffer is replaced by the next (i.e. 1,001-st) element, maintaining the 1,000 element buffer.\
\
`reshuffle_each_iteration` controls whether the shuffle order should be different for each epoch. However you should avoid using `shuffle(reshuffle_each_iteration=True)`, then `take` and `skip` to split a dataset into training and test sets, which would lead to data leakage (as the entire dataset would be re-shuffled then re-split after each epoch). Please use the [`tf.keras.utils.split_dataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/split_dataset)\
 method instead. In TF 1.X, the idiomatic way to create epochs was through the `repeat` transformation:\
\
dataset = tf.data.Dataset.range(3)\
    dataset = dataset.shuffle(3, reshuffle_each_iteration=True)\
    dataset = dataset.repeat(2)\
    # [1, 0, 2, 1, 2, 0]\
    \
    dataset = tf.data.Dataset.range(3)\
    dataset = dataset.shuffle(3, reshuffle_each_iteration=False)\
    dataset = dataset.repeat(2)\
    # [1, 0, 2, 1, 0, 2]\
\
In TF 2.0, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)\
 objects are Python iterables which makes it possible to also create epochs through Python iteration:\
\
dataset = tf.data.Dataset.range(3)\
    dataset = dataset.shuffle(3, reshuffle_each_iteration=True)\
    list(dataset.as_numpy_iterator())\
    # [1, 0, 2]\
    list(dataset.as_numpy_iterator())\
    # [1, 2, 0]\
\
dataset = tf.data.Dataset.range(3)\
    dataset = dataset.shuffle(3, reshuffle_each_iteration=False)\
    list(dataset.as_numpy_iterator())\
    # [1, 0, 2]\
    list(dataset.as_numpy_iterator())\
    # [1, 0, 2]\
\
#### Fully shuffling all the data\
\
To shuffle an entire dataset, set `buffer_size=dataset.cardinality()`. This is equivalent to setting the `buffer_size` equal to the number of elements in the dataset, resulting in uniform shuffle.\
\
dataset = tf.data.Dataset.range(20)\
    dataset = dataset.shuffle(dataset.cardinality())\
    # [18, 4, 9, 2, 17, 8, 5, 10, 0, 6, 16, 3, 19, 7, 14, 11, 15, 13, 12, 1]\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `buffer_size` | An int or [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of elements from this dataset from which the new dataset will sample. To uniformly shuffle the entire dataset, use `buffer_size=dataset.cardinality()`. |\
| `seed` | (Optional.) An int or [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the random seed that will be used to create the distribution. See [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)<br> for behavior. |\
| `reshuffle_each_iteration` | (Optional.) A boolean, which if true indicates that the dataset should be pseudorandomly reshuffled each time it is iterated over. (Defaults to `True`.) |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `skip`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1596-L1619)\
\
skip(\
        count, name=None\
    ) -> 'DatasetV2'\
\
Creates a `Dataset` that skips `count` elements from this dataset.\
\
    dataset = tf.data.Dataset.range(10)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `count` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of elements of this dataset that should be skipped to form the new dataset. If `count` is greater than the size of this dataset, the new dataset will contain no elements. If `count` is -1, skips the entire dataset. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `snapshot`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L3307-L3396)\
\
snapshot(\
        path,\
        compression='AUTO',\
        reader_func=None,\
        shard_func=None,\
        name=None\
    ) -> 'DatasetV2'\
\
API to persist the output of the input dataset.\
\
The snapshot API allows users to transparently persist the output of their preprocessing pipeline to disk, and materialize the pre-processed data on a different training run.\
\
This API enables repeated preprocessing steps to be consolidated, and allows re-use of already processed data, trading off disk storage and network bandwidth for freeing up more valuable CPU resources and accelerator compute time.\
\
[https://github.com/tensorflow/community/blob/master/rfcs/20200107-tf-data-snapshot.md](https://github.com/tensorflow/community/blob/master/rfcs/20200107-tf-data-snapshot.md)\
 has detailed design documentation of this feature.\
\
Users can specify various options to control the behavior of snapshot, including how snapshots are read from and written to by passing in user-defined functions to the `reader_func` and `shard_func` parameters.\
\
`shard_func` is a user specified function that maps input elements to snapshot shards.\
\
Users may want to specify this function to control how snapshot files should be written to disk. Below is an example of how a potential `shard_func` could be written.\
\
dataset = ...\
    dataset = dataset.enumerate()\
    dataset = dataset.snapshot("/path/to/snapshot/dir",\
        shard_func=lambda x, y: x % NUM_SHARDS, ...)\
    dataset = dataset.map(lambda x, y: y)\
\
`reader_func` is a user specified function that accepts a single argument: (1) a Dataset of Datasets, each representing a "split" of elements of the original dataset. The cardinality of the input dataset matches the number of the shards specified in the `shard_func` (see above). The function should return a Dataset of elements of the original dataset.\
\
Users may want specify this function to control how snapshot files should be read from disk, including the amount of shuffling and parallelism.\
\
Here is an example of a standard reader function a user can define. This function enables both dataset shuffling and parallel reading of datasets:\
\
def user_reader_func(datasets):\
      # shuffle the datasets splits\
      datasets = datasets.shuffle(NUM_CORES)\
      # read datasets in parallel and interleave their elements\
      return datasets.interleave(lambda x: x, num_parallel_calls=AUTOTUNE)\
    \
    dataset = dataset.snapshot("/path/to/snapshot/dir",\
        reader_func=user_reader_func)\
\
By default, snapshot parallelizes reads by the number of cores available on the system, but will not attempt to shuffle the data.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `path` | Required. A directory to use for storing / loading the snapshot to / from. |\
| `compression` | Optional. The type of compression to apply to the snapshot written to disk. Supported options are `GZIP`, `SNAPPY`, `AUTO` or None. Defaults to `AUTO`, which attempts to pick an appropriate compression algorithm for the dataset. |\
| `reader_func` | Optional. A function to control how to read data from snapshot shards. |\
| `shard_func` | Optional. A function to control how to shard data when writing a snapshot. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `sparse_batch`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L2114-L2161)\
\
sparse_batch(\
        batch_size, row_shape, name=None\
    ) -> 'DatasetV2'\
\
Combines consecutive elements into [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)\
s.\
\
Like [`Dataset.padded_batch()`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#padded_batch)\
, this transformation combines multiple consecutive elements of the dataset, which might have different shapes, into a single element. The resulting element has three components (`indices`, `values`, and `dense_shape`), which comprise a [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)\
 that represents the same data. The `row_shape` represents the dense shape of each row in the resulting [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)\
, to which the effective batch size is prepended. For example:\
\
# NOTE: The following examples use `{ ... }` to represent the\
    # contents of a dataset.\
    a = { ['a', 'b', 'c'], ['a', 'b'], ['a', 'b', 'c', 'd'] }\
    \
    a.apply(tf.data.experimental.dense_to_sparse_batch(\
        batch_size=2, row_shape=[6])) ==\
    {\
        ([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1]],  # indices\
         ['a', 'b', 'c', 'a', 'b'],                 # values\
         [2, 6]),                                   # dense_shape\
        ([[0, 0], [0, 1], [0, 2], [0, 3]],\
         ['a', 'b', 'c', 'd'],\
         [1, 6])\
    }\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `batch_size` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of consecutive elements of this dataset to combine in a single batch. |\
| `row_shape` | A [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br> or [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> vector tensor-like object representing the equivalent dense shape of a row in the resulting [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br>. Each element of this dataset must have the same rank as `row_shape`, and must have size less than or equal to `row_shape` in each dimension. |\
| `name` | (Optional.) A string indicating a name for the [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)<br> operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `take`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1571-L1594)\
\
take(\
        count, name=None\
    ) -> 'DatasetV2'\
\
Creates a `Dataset` with at most `count` elements from this dataset.\
\
    dataset = tf.data.Dataset.range(10)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `count` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of elements of this dataset that should be taken to form the new dataset. If `count` is -1, or if `count` is greater than the size of this dataset, the new dataset will contain all elements of this dataset. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `take_while`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L3433-L3455)\
\
take_while(\
        predicate, name=None\
    ) -> 'DatasetV2'\
\
A transformation that stops dataset iteration based on a `predicate`.\
\
    dataset = tf.data.Dataset.range(10)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `predicate` | A function that maps a nested structure of tensors (having shapes and types defined by `self.output_shapes` and `self.output_types`) to a scalar [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)<br> tensor. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `unbatch`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L2955-L2984)\
\
unbatch(\
        name=None\
    ) -> 'DatasetV2'\
\
Splits elements of a dataset into multiple elements.\
\
For example, if elements of the dataset are shaped `[B, a0, a1, ...]`, where `B` may vary for each input element, then for each element in the dataset, the unbatched dataset will contain `B` consecutive elements of shape `[a0, a1, ...]`.\
\
    elements = [ [1, 2, 3], [1, 2], [1, 2, 3, 4] ]\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `unique`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L3457-L3482)\
\
unique(\
        name=None\
    ) -> 'DatasetV2'\
\
A transformation that discards duplicate elements of a `Dataset`.\
\
Use this transformation to produce a dataset that contains one instance of each unique element in the input. For example:\
\
    dataset = tf.data.Dataset.from_tensor_slices([1, 37, 2, 37, 2, 1])\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `window`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L2595-L2746)\
\
window(\
        size, shift=None, stride=1, drop_remainder=False, name=None\
    ) -> 'DatasetV2'\
\
Returns a dataset of "windows".\
\
Each "window" is a dataset that contains a subset of elements of the input dataset. These are finite datasets of size `size` (or possibly fewer if there are not enough input elements to fill the window and `drop_remainder` evaluates to `False`).\
\
#### For example:\
\
    dataset = tf.data.Dataset.range(7).window(3)\
\
Since windows are datasets, they can be iterated over:\
\
    for window in dataset:\
\
#### Shift\
\
The `shift` argument determines the number of input elements to shift between the start of each window. If windows and elements are both numbered starting at 0, the first element in window `k` will be element `k * shift` of the input dataset. In particular, the first element of the first window will always be the first element of the input dataset.\
\
    dataset = tf.data.Dataset.range(7).window(3, shift=1,\
\
#### Stride\
\
The `stride` argument determines the stride between input elements within a window.\
\
    dataset = tf.data.Dataset.range(7).window(3, shift=1, stride=2,\
\
#### Nested elements\
\
When the `window` transformation is applied to a dataset whose elements are nested structures, it produces a dataset where the elements have the same nested structure but each leaf is replaced by a window. In other words, the nesting is applied outside of the windows as opposed inside of them.\
\
#### The type signature is:\
\
def window(\
        self: Dataset[Nest[T]], ...\
    ) -> Dataset[Nest[Dataset[T]]]\
\
Applying `window` to a `Dataset` of tuples gives a tuple of windows:\
\
    dataset = tf.data.Dataset.from_tensor_slices(([1, 2, 3, 4, 5],\
\
    def to_numpy(ds):\
\
Applying `window` to a `Dataset` of dictionaries gives a dictionary of `Datasets`:\
\
    dataset = tf.data.Dataset.from_tensor_slices({'a': [1, 2, 3],\
\
#### Flatten a dataset of windows\
\
The [`Dataset.flat_map`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#flat_map)\
 and [`Dataset.interleave`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave)\
 methods can be used to flatten a dataset of windows into a single dataset.\
\
The argument to `flat_map` is a function that takes an element from the dataset and returns a `Dataset`. `flat_map` chains together the resulting datasets sequentially.\
\
For example, to turn each window into a dense tensor:\
\
    dataset = tf.data.Dataset.range(7).window(3, shift=1,\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `size` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of elements of the input dataset to combine into a window. Must be positive. |\
| `shift` | (Optional.) A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of input elements by which the window moves in each iteration. Defaults to `size`. Must be positive. |\
| `stride` | (Optional.) A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the stride of the input elements in the sliding window. Must be positive. The default value of 1 means "retain every input element". |\
| `drop_remainder` | (Optional.) A [`tf.bool`](https://www.tensorflow.org/api_docs/python/tf#bool)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing whether the last windows should be dropped if their size is smaller than `size`. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `with_options`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L2986-L3012)\
\
with_options(\
        options, name=None\
    ) -> 'DatasetV2'\
\
Returns a new [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)\
 with the given options set.\
\
The options are "global" in the sense they apply to the entire dataset. If options are set multiple times, they are merged as long as different options do not use different non-default values.\
\
    ds = tf.data.Dataset.range(5)\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `options` | A [`tf.data.Options`](https://www.tensorflow.org/api_docs/python/tf/data/Options)<br> that identifies the options the use. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `ValueError` | when an option is set more than once to a non-default value |\
\
### `zip`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L1025-L1089)\
\
@staticmethod\
\
Creates a `Dataset` by zipping together the given datasets.\
\
This method has similar semantics to the built-in `zip()` function in Python, with the main difference being that the `datasets` argument can be a (nested) structure of `Dataset` objects. The supported nesting mechanisms are documented [here](https://www.tensorflow.org/guide/data#dataset_structure)\
.\
\
    # The datasets or nested structure of datasets `*args` argument\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `*args` | Datasets or nested structures of datasets to zip together. This can't be set if `datasets` is set. |\
| `datasets` | A (nested) structure of datasets. This can't be set if `*args` is set. Note that this exists only for backwards compatibility and it is preferred to use \*args. |\
| `name` | (Optional.) A name for the tf.data operation. |\
\
|     |\
| --- |\
| Returns |     |\
| A new `Dataset` with the transformation applied as described above. |     |\
\
### `__bool__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L506-L507)\
\
__bool__()\
\
### `__iter__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L488-L504)\
\
__iter__() -> iterator_ops.OwnedIterator\
\
Creates an iterator for elements of this dataset.\
\
The returned iterator implements the Python Iterator protocol.\
\
|     |\
| --- |\
| Returns |     |\
| An [`tf.data.Iterator`](https://www.tensorflow.org/api_docs/python/tf/data/Iterator)<br> for the elements of this dataset. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `RuntimeError` | If not inside of tf.function and not executing eagerly. |\
\
### `__len__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L511-L534)\
\
__len__()\
\
Returns the length of the dataset if it is known and finite.\
\
This method requires that you are running in eager mode, and that the length of the dataset is known and non-infinite. When the length may be unknown or infinite, or if you are running in graph mode, use [`tf.data.Dataset.cardinality`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#cardinality)\
 instead.\
\
|     |\
| --- |\
| Returns |     |\
| An integer representing the length of the dataset. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `RuntimeError` | If the dataset length is unknown or infinite, or if eager execution is not enabled. |\
\
### `__nonzero__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/dataset_ops.py#L506-L507)\
\
__nonzero__()\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-11-04 UTC.