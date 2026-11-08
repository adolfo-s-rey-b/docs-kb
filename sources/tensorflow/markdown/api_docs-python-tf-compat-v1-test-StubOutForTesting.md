[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/test/StubOutForTesting#main-content)

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
    

tf.compat.v1.test.StubOutForTesting Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/googletest.py#L115-L273)

Support class for stubbing methods out for unit testing.

tf.compat.v1.test.StubOutForTesting()

#### Sample Usage:

You want os.path.exists() to always return true during testing.

stubs = StubOutForTesting() stubs.Set(os.path, 'exists', lambda x: 1) ... stubs.CleanUp()

The above changes os.path.exists into a lambda that returns 1. Once the ... part of the code finishes, the CleanUp() looks up the old value of os.path.exists and restores it.

Methods
-------

### `CleanUp`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/googletest.py#L152-L155)

CleanUp()

Undoes all SmartSet() & Set() calls, restoring original definitions.

### `Set`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/googletest.py#L234-L258)

Set(
        parent, child_name, new_child
    )

In parent, replace child\_name's old definition with new\_child.

The parent could be a module when the child is a function at module scope. Or the parent could be a class when a class' method is being replaced. The named child is set to new\_child, while the prior definition is saved away for later, when UnsetAll() is called.

This method supports the case where child\_name is a staticmethod or a classmethod of parent.

|     |     |
| --- | --- |
| Args |     |
| `parent` | The context in which the attribute child\_name is to be changed. |
| `child_name` | The name of the attribute to change. |
| `new_child` | The new value of the attribute. |

### `SmartSet`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/googletest.py#L157-L218)

SmartSet(
        obj, attr_name, new_attr
    )

Replace obj.attr\_name with new\_attr.

This method is smart and works at the module, class, and instance level while preserving proper inheritance. It will not stub out C types however unless that has been explicitly allowed by the type.

This method supports the case where attr\_name is a staticmethod or a classmethod of obj.

|     |
| --- |
| Notes |     |
| *   If obj is an instance, then it is its class that will actually be stubbed. Note that the method Set() does not do that: if obj is an instance, it (and not its class) will be stubbed.<br>*   The stubbing is using the builtin getattr and setattr. So, the **get** and **set** will be called when stubbing ( probably be to manipulate obj.**dict** instead of getattr() and setattr()). |     |

|     |     |
| --- | --- |
| Args |     |
| `obj` | The object whose attributes we want to modify. |
| `attr_name` | The name of the attribute to modify. |
| `new_attr` | The new value for the attribute. |

|     |     |
| --- | --- |
| Raises |     |
| `AttributeError` | If the attribute cannot be found. |

### `SmartUnsetAll`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/googletest.py#L220-L232)

SmartUnsetAll()

Reverses SmartSet() calls, restoring things to original definitions.

This method is automatically called when the StubOutForTesting() object is deleted; there is no need to call it explicitly.

It is okay to call SmartUnsetAll() repeatedly, as later calls have no effect if no SmartSet() calls have been made.

### `UnsetAll`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/googletest.py#L260-L273)

UnsetAll()

Reverses Set() calls, restoring things to their original definitions.

This method is automatically called when the StubOutForTesting() object is deleted; there is no need to call it explicitly.

It is okay to call UnsetAll() repeatedly, as later calls have no effect if no Set() calls have been made.

### `__enter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/googletest.py#L146-L147)

__enter__()

### `__exit__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/platform/googletest.py#L149-L150)

__exit__(
        unused_exc_type, unused_exc_value, unused_tb
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.