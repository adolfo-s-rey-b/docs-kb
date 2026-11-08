Loading \[MathJax\]/jax/output/SVG/jax.js

[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tensordot#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tensordot)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tensordot?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftensordot&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [For example](https://www.tensorflow.org/api_docs/python/tf/tensordot#for-example)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tensordot Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================

*   On this page
*   [For example](https://www.tensorflow.org/api_docs/python/tf/tensordot#for-example)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L5247-L5458)

Tensor contraction of a and b along specified axes and outer product.

#### View aliases

**Main aliases**

[`tf.linalg.tensordot`](https://www.tensorflow.org/api_docs/python/tf/tensordot)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.tensordot`](https://www.tensorflow.org/api_docs/python/tf/tensordot)
, [`tf.compat.v1.tensordot`](https://www.tensorflow.org/api_docs/python/tf/tensordot)

tf.tensordot(
        a, b, axes, name=None
    )

Tensordot (also known as tensor contraction) sums the product of elements from `a` and `b` over the indices specified by `axes`.

This operation corresponds to [`numpy.tensordot(a, b, axes)`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/tensordot)
.

Example 1: When `a` and `b` are matrices (order 2), the case `axes=1` is equivalent to matrix multiplication.

Example 2: When `a` and `b` are matrices (order 2), the case `axes = [[1], [0]]` is equivalent to matrix multiplication.

Example 3: When `a` and `b` are matrices (order 2), the case `axes=0` gives the outer product, a tensor of order 4.

Example 4: Suppose that aijk and blmn represent two tensors of order 3. Then, `contract(a, b, [[0], [2]])` is the order 4 tensor cjklm whose entry corresponding to the indices (j,k,l,m) is given by:

cjklm\=∑iaijkblmi.

In general, `order(c) = order(a) + order(b) - 2*len(axes[0])`.

|     |
| --- |
| For example<br>----------- |     |
| import numpy as np<br>    import tensorflow as tf<br>    <br>    a = np.arange(60).reshape(3,4,5)<br>    b = np.arange(24).reshape(4,3,2)<br>    c = tf.tensordot(a,b, axes=([1,0],[0,1]))<br>    c<br>    <br>    <tf.Tensor: shape=(5, 2), dtype=int64, numpy=<br>    array([[4400, 4730],<br>        [4532, 4874],<br>        [4664, 5018],<br>        [4796, 5162],<br>        [4928, 5306]])><br>    </td><br>    </tr><br>    <br>    </table><br>    <br>    <br>    # Another example<br>    d = tf.random.uniform((3,4,5))<br>    e = tf.random.uniform((5,3,2))<br>    f = tf.tensordot(d,e, axes=([2,0],[0,1]))<br>    f<br>    <br>    <tf.Tensor: shape=(4, 2), dtype=float32, numpy=<br>    array([[4.8271146, 4.493    ],<br>         [5.8537536, 5.492961 ],<br>         [5.2579894, 5.2020206],<br>         [3.5817177, 4.2104754]], dtype=float32)><br>         <br>        ```<br>    <br>      Args:<br>        a: `Tensor` of type `float32` or `float64`.<br>        b: `Tensor` with the same type as `a`.<br>        axes: Either a scalar `N`, or a list or an `int32` `Tensor` of shape [2, k].<br>          If axes is a scalar, sum over the last N axes of a and the first N axes of<br>          b in order. If axes is a list or `Tensor` the first and second row contain<br>          the set of unique integers specifying axes along which the contraction is<br>          computed, for `a` and `b`, respectively. The number of axes for `a` and<br>          `b` must be equal. If `axes=0`, computes the outer product between `a` and<br>          `b`.<br>        name: A name for the operation (optional).<br>    <br>      <!-- Tabular view --><br>       <table class="responsive fixed orange"><br>      <colgroup><col width="214px"><col></colgroup><br>      <tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr><br>      <tr class="alt"><br>      <td colspan="2"><br>      A `Tensor` with the same type as `a`.<br>      </td><br>      </tr><br>    <br>      </table><br>    <br>    <br>    <br>      <!-- Tabular view --><br>       <table class="responsive fixed orange"><br>      <colgroup><col width="214px"><col></colgroup><br>      <tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr><br>    <br>      <tr><br>      <td><br>      `ValueError`<a id="ValueError"></a><br>      </td><br>      <td><br>      If the shapes of `a`, `b`, and `axes` are incompatible.<br>      </td><br>      </tr><tr><br>      <td><br>      `IndexError`<a id="IndexError"></a><br>      </td><br>      <td><br>      If the values in axes exceed the rank of the corresponding<br>      tensor.<br>      </td><br>      </tr><br>      </table><br><br>Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)<br>, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)<br>. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)<br>. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)<br>.<br><br>Last updated 2026-10-31 UTC. |     |