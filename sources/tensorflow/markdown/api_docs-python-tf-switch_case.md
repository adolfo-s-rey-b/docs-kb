[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/switch_case#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/switch_case)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/switch_case?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/switch_case#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/switch_case#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/switch_case#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.switch\_case Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/switch_case#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/switch_case#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/switch_case#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/control_flow_switch_case.py#L181-L253)

Create a switch/case operation, i.e.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.switch_case`](https://www.tensorflow.org/api_docs/python/tf/switch_case)

tf.switch_case(
        branch_index, branch_fns, default=None, name='switch_case'
    )

an integer-indexed conditional.

See also [`tf.case`](https://www.tensorflow.org/api_docs/python/tf/case)
.

This op can be substantially more efficient than [`tf.case`](https://www.tensorflow.org/api_docs/python/tf/case)
 when exactly one branch will be selected. [`tf.switch_case`](https://www.tensorflow.org/api_docs/python/tf/switch_case)
 is more like a C++ switch/case statement than [`tf.case`](https://www.tensorflow.org/api_docs/python/tf/case)
, which is more like an if/elif/elif/else chain.

The `branch_fns` parameter is either a dict from `int` to callables, or list of (`int`, callable) pairs, or simply a list of callables (in which case the index is implicitly the key). The `branch_index` `Tensor` is used to select an element in `branch_fns` with matching `int` key, falling back to `default` if none match, or `max(keys)` if no `default` is provided. The keys must form a contiguous set from `0` to `len(branch_fns) - 1`.

[`tf.switch_case`](https://www.tensorflow.org/api_docs/python/tf/switch_case)
 supports nested structures as implemented in [`tf.nest`](https://www.tensorflow.org/api_docs/python/tf/nest)
. All callables must return the same (possibly nested) value structure of lists, tuples, and/or named tuples.

**Example:**

#### Pseudocode:

switch (branch_index) {  // c-style switch
      case 0: return 17;
      case 1: return 31;
      default: return -1;
    }

or

branches = {0: lambda: 17, 1: lambda: 31}
    branches.get(branch_index, lambda: -1)()

#### Expressions:

def f1(): return tf.constant(17)
    def f2(): return tf.constant(31)
    def f3(): return tf.constant(-1)
    r = tf.switch_case(branch_index, branch_fns={0: f1, 1: f2}, default=f3)
    # Equivalent: tf.switch_case(branch_index, branch_fns={0: f1, 1: f2, 2: f3})

|     |     |
| --- | --- |
| Args<br>---- |     |
| `branch_index` | An int Tensor specifying which of `branch_fns` should be executed. |
| `branch_fns` | A `dict` mapping `int`s to callables, or a `list` of (`int`, callable) pairs, or simply a list of callables (in which case the index serves as the key). Each callable must return a matching structure of tensors. |
| `default` | Optional callable that returns a structure of tensors. |
| `name` | A name for this operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| The tensors returned by the callable identified by `branch_index`, or those returned by `default` if no key matches and `default` was provided, or those returned by the max-keyed `branch_fn` if no `default` is provided. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `branch_fns` is not a list/dictionary. |
| `TypeError` | If `branch_fns` is a list but does not contain 2-tuples or callables. |
| `TypeError` | If `fns[i]` is not callable for any i, or `default` is not callable. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.