[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/debugging/assert_shapes#main-content)

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
    

tf.compat.v1.debugging.assert\_shapes Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/check_ops.py#L1685-L1938)

Assert tensor shapes and dimension size relationships between tensors.

tf.compat.v1.debugging.assert_shapes(
        shapes, data=None, summarize=None, message=None, name=None
    )

This Op checks that a collection of tensors shape relationships satisfies given constraints.

#### Example:

    n = 10

    tf.debugging.assert_shapes([\
\
Example of adding a dependency to an operation:\
\
with tf.control_dependencies([tf.assert_shapes(shapes)]):\
      output = tf.matmul(x, y, transpose_a=True)\
\
If `x`, `y`, `param` or `scalar` does not have a shape that satisfies all specified constraints, `message`, as well as the first `summarize` entries of the first encountered violating tensor are printed, and `InvalidArgumentError` is raised.\
\
Size entries in the specified shapes are checked against other entries by their **hash**, except:\
\
*   a size entry is interpreted as an explicit size if it can be parsed as an integer primitive.\
*   a size entry is interpreted as _any_ size if it is None or '.'.\
\
If the first entry of a shape is `...` (type `Ellipsis`) or '\*' that indicates a variable number of outer dimensions of unspecified size, i.e. the constraint applies to the inner-most dimensions only.\
\
Scalar tensors and specified shapes of length zero (excluding the 'inner-most' prefix) are both treated as having a single dimension of size one.\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `shapes` | A list of (`Tensor`, `shape`) tuples, wherein `shape` is the expected shape of `Tensor`. See the example code above. The `shape` must be an iterable. Each element of the iterable can be either a concrete integer value or a string that abstractly represents the dimension. For example,<br><br>*   `('N', 'Q')` specifies a 2D shape wherein the first and second dimensions of shape may or may not be equal.<br>*   `('N', 'N', 'Q')` specifies a 3D shape wherein the first and second dimensions are equal.<br>*   `(1, 'N')` specifies a 2D shape wherein the first dimension is exactly 1 and the second dimension can be any value. Note that the abstract dimension letters take effect across different tuple elements of the list. For example, `tf.debugging.assert_shapes([(x, ('N', 'A')), (y, ('N', 'B'))]` asserts that both `x` and `y` are rank-2 tensors and their first dimensions are equal (`N`). `shape` can also be a [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape)<br>    . |\
| `data` | The tensors to print out if the condition is False. Defaults to error message and first few entries of the violating tensor. |\
| `summarize` | Print this many entries of the tensor. |\
| `message` | A string to prefix to the default message. |\
| `name` | A name for this operation (optional). Defaults to "assert\_shapes". |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| Op raising `InvalidArgumentError` unless all shape constraints are satisfied. If static checks determine all constraints are satisfied, a `no_op` is returned. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If static checks determine any shape constraint is violated. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.