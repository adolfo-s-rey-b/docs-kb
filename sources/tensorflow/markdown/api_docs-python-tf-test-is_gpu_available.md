[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/test/is_gpu_available#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/test/is_gpu_available)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/test/is_gpu_available?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftest%2Fis_gpu_available&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/test/is_gpu_available#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/test/is_gpu_available#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.test.is\_gpu\_available Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/test/is_gpu_available#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/test/is_gpu_available#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/test_util.py#L2072-L2130)

Returns whether TensorFlow can access a GPU. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.test.is_gpu_available`](https://www.tensorflow.org/api_docs/python/tf/test/is_gpu_available)

tf.test.is_gpu_available(
        cuda_only: bool = False,
        min_cuda_compute_capability: Optional[tuple[int, int]] = None
    ) -> bool

For example,

>>> gpu_available = tf.test.is_gpu_available()
    >>> is_cuda_gpu_available = tf.test.is_gpu_available(cuda_only=True)
    >>> is_cuda_gpu_min_3 = tf.test.is_gpu_available(True, (3,0))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `cuda_only` | limit the search to CUDA GPUs. |
| `min_cuda_compute_capability` | a (major,minor) pair that indicates the minimum CUDA compute capability required, or None if no requirement. |

Note that the keyword arg name "cuda\_only" is misleading (since routine will return true when a GPU device is available irrespective of whether TF was built with CUDA support or ROCm support. However no changes here because

++ Changing the name "cuda\_only" to something more generic would break backward compatibility

++ Adding an equivalent "rocm\_only" would require the implementation check the build type. This in turn would require doing the same for CUDA and thus potentially break backward compatibility

++ Adding a new "cuda\_or\_rocm\_only" would not break backward compatibility, but would require most (if not all) callers to update the call to use "cuda\_or\_rocm\_only" instead of "cuda\_only"

|     |
| --- |
| Returns<br>------- |     |
| True if a GPU device of the requested kind is available. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.