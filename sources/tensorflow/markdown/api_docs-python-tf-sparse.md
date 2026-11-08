[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/sparse#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/sparse#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.sparse Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/sparse#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/sparse#functions)
    

Public API for tf.\_api.v2.sparse namespace

Classes
-------

[`class SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
: Represents a sparse tensor.

Functions
---------

[`add(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/add)
: Adds two tensors, at least one of each is a `SparseTensor`.

[`bincount(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/bincount)
: Count the number of times an integer value appears in a tensor.

[`concat(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/concat)
: Concatenates a list of `SparseTensor` along the specified dimension. (deprecated arguments)

[`cross(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/cross)
: Generates sparse cross from a list of sparse and dense tensors.

[`cross_hashed(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/cross_hashed)
: Generates hashed sparse cross from a list of sparse and dense tensors.

[`expand_dims(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/expand_dims)
: Returns a tensor with an length 1 axis inserted at index `axis`.

[`eye(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/eye)
: Creates a two-dimensional sparse tensor with ones along the diagonal.

[`fill_empty_rows(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/fill_empty_rows)
: Fills empty rows in the input 2-D `SparseTensor` with a default value.

[`from_dense(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/from_dense)
: Converts a dense tensor into a sparse tensor.

[`map_values(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/map_values)
: Applies `op` to the `.values` tensor of one or more `SparseTensor`s.

[`mask(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/mask)
: Masks elements of `IndexedSlices`.

[`maximum(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/maximum)
: Returns the element-wise max of two SparseTensors.

[`minimum(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/minimum)
: Returns the element-wise min of two SparseTensors.

[`reduce_max(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/reduce_max)
: Computes [`tf.sparse.maximum`](https://www.tensorflow.org/api_docs/python/tf/sparse/maximum)
 of elements across dimensions of a SparseTensor.

[`reduce_sum(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/reduce_sum)
: Computes [`tf.sparse.add`](https://www.tensorflow.org/api_docs/python/tf/sparse/add)
 of elements across dimensions of a SparseTensor.

[`reorder(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/reorder)
: Reorders a `SparseTensor` into the canonical, row-major ordering.

[`reset_shape(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/reset_shape)
: Resets the shape of a `SparseTensor` with indices and values unchanged.

[`reshape(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/reshape)
: Reshapes a `SparseTensor` to represent values in a new dense shape.

[`retain(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/retain)
: Retains specified non-empty values within a `SparseTensor`.

[`sampled_addmm(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/sampled_addmm)
: Performs the sampled matrix multiplication of two dense matrices.

[`segment_mean(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/segment_mean)
: Computes the mean along sparse segments of a tensor.

[`segment_sqrt_n(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/segment_sqrt_n)
: Computes the sum along sparse segments of a tensor divided by the sqrt(N).

[`segment_sum(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/segment_sum)
: Computes the sum along sparse segments of a tensor.

[`slice(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/slice)
: Slice a `SparseTensor` based on the `start` and `size`.

[`softmax(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/softmax)
: Applies softmax to a batched N-D `SparseTensor`.

[`sparse_dense_matmul(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/sparse_dense_matmul)
: Multiply SparseTensor (or dense Matrix) (of rank 2) "A" by dense matrix

[`split(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/split)
: Split a `SparseTensor` into `num_split` tensors along `axis`.

[`to_dense(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/to_dense)
: Converts a `SparseTensor` into a dense tensor.

[`to_indicator(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/to_indicator)
: Converts a `SparseTensor` of ids into a dense bool indicator tensor.

[`transpose(...)`](https://www.tensorflow.org/api_docs/python/tf/sparse/transpose)
: Transposes a `SparseTensor`.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.