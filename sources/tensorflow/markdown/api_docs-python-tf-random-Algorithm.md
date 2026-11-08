[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/Algorithm#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/Algorithm)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/Algorithm?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Frandom%2FAlgorithm&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/random/Algorithm#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.Algorithm Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/random/Algorithm#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/random_ops_util.py#L30-L55)

A random-number-generation (RNG) algorithm.

#### View aliases

**Main aliases**

[`tf.random.experimental.Algorithm`](https://www.tensorflow.org/api_docs/python/tf/random/Algorithm)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.Algorithm`](https://www.tensorflow.org/api_docs/python/tf/random/Algorithm)
, [`tf.compat.v1.random.experimental.Algorithm`](https://www.tensorflow.org/api_docs/python/tf/random/Algorithm)

Many random-number generators (e.g. the `alg` argument of [`tf.random.Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator)
 and [`tf.random.stateless_uniform`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform)
) in TF allow you to choose the algorithm used to generate the (pseudo-)random numbers. You can set the algorithm to be one of the options below.

*   `PHILOX`: The Philox algorithm introduced in the paper ["Parallel Random Numbers: As Easy as 1, 2, 3"](https://www.thesalmons.org/john/random123/papers/random123sc11.pdf)
    .
*   `THREEFRY`: The ThreeFry algorithm introduced in the paper ["Parallel Random Numbers: As Easy as 1, 2, 3"](https://www.thesalmons.org/john/random123/papers/random123sc11.pdf)
    .
*   `AUTO_SELECT`: Allow TF to automatically select the algorithm depending on the accelerator device. Note that with this option, running the same TF program on different devices may result in different random numbers. Also note that TF may select an algorithm that is different from `PHILOX` and `THREEFRY`.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| AUTO\_SELECT | `<Algorithm.AUTO_SELECT: 3>` |
| PHILOX | `<Algorithm.PHILOX: 1>` |
| THREEFRY | `<Algorithm.THREEFRY: 2>` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.