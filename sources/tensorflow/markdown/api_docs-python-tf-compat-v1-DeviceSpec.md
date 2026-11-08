[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/DeviceSpec#main-content)

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
    

tf.compat.v1.DeviceSpec Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/device_spec.py#L420-L485)

Represents a (possibly partial) specification for a TensorFlow device.

Inherits From: [`DeviceSpec`](https://www.tensorflow.org/api_docs/python/tf/DeviceSpec)

tf.compat.v1.DeviceSpec(
        job=None, replica=None, task=None, device_type=None, device_index=None
    )

`DeviceSpec`s are used throughout TensorFlow to describe where state is stored and computations occur. Using `DeviceSpec` allows you to parse device spec strings to verify their validity, merge them or compose them programmatically.

#### Example:

# Place the operations on device "GPU:0" in the "ps" job.
    device_spec = DeviceSpec(job="ps", device_type="GPU", device_index=0)
    with tf.device(device_spec.to_string()):
      # Both my_var and squared_var will be placed on /job:ps/device:GPU:0.
      my_var = tf.Variable(..., name="my_variable")
      squared_var = tf.square(my_var)

With eager execution disabled (by default in TensorFlow 1.x and by calling disable\_eager\_execution() in TensorFlow 2.x), the following syntax can be used:

tf.compat.v1.disable_eager_execution()
    
    # Same as previous
    device_spec = DeviceSpec(job="ps", device_type="GPU", device_index=0)
    # No need of .to_string() method.
    with tf.device(device_spec):
      my_var = tf.Variable(..., name="my_variable")
      squared_var = tf.square(my_var)

If a `DeviceSpec` is partially specified, it will be merged with other `DeviceSpec`s according to the scope in which it is defined. `DeviceSpec` components defined in inner scopes take precedence over those defined in outer scopes.

gpu0_spec = DeviceSpec(job="ps", device_type="GPU", device_index=0)
    with tf.device(DeviceSpec(job="train").to_string()):
      with tf.device(gpu0_spec.to_string()):
        # Nodes created here will be assigned to /job:ps/device:GPU:0.
      with tf.device(DeviceSpec(device_type="GPU", device_index=1).to_string()):
        # Nodes created here will be assigned to /job:train/device:GPU:1.

A `DeviceSpec` consists of 5 components -- each of which is optionally specified:

*   Job: The job name.
*   Replica: The replica index.
*   Task: The task index.
*   Device type: The device type string (e.g. "CPU" or "GPU").
*   Device index: The device index.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `job` | string. Optional job name. |
| `replica` | int. Optional replica index. |
| `task` | int. Optional task index. |
| `device_type` | Optional device type string (e.g. "CPU" or "GPU") |
| `device_index` | int. Optional device index. If left unspecified, device represents 'any' device\_index. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `device_index` |     |
| `device_type` |     |
| `job` |     |
| `replica` |     |
| `task` |     |

Methods
-------

### `from_string`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/device_spec.py#L145-L158)

@classmethod

Construct a `DeviceSpec` from a string.

|     |     |
| --- | --- |
| Args |     |
| `spec` | a string of the form /job:/replica:/task:/device:CPU: or /job:/replica:/task:/device:GPU: as cpu and gpu are mutually exclusive. All entries are optional. |

|     |
| --- |
| Returns |     |
| A DeviceSpec. |     |

### `make_merged_spec`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/device_spec.py#L215-L237)

make_merged_spec(
        dev
    )

Returns a new DeviceSpec which incorporates `dev`.

When combining specs, `dev` will take precedence over the current spec. So for instance:

first_spec = tf.DeviceSpec(job=0, device_type="CPU")
    second_spec = tf.DeviceSpec(device_type="GPU")
    combined_spec = first_spec.make_merged_spec(second_spec)

is equivalent to:

combined_spec = tf.DeviceSpec(job=0, device_type="GPU")

|     |     |
| --- | --- |
| Args |     |
| `dev` | a `DeviceSpec` |

|     |
| --- |
| Returns |     |
| A new `DeviceSpec` which combines `self` and `dev` |     |

### `merge_from`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/device_spec.py#L471-L481)

merge_from(
        dev
    )

Merge the properties of "dev" into this `DeviceSpec`.

|     |     |
| --- | --- |
| Args |     |
| `dev` | a `DeviceSpec`. |

### `parse_from_string`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/device_spec.py#L465-L469)

parse_from_string(
        spec
    )

Parse a `DeviceSpec` name into its components.

**2.x behavior change**:

In TensorFlow 1.x, this function mutates its own state and returns itself. In 2.x, DeviceSpecs are immutable, and this function will return a DeviceSpec which contains the spec.

*   Recommended:
    
    # my_spec and my_updated_spec are unrelated.
        my_spec = tf.DeviceSpec.from_string("/CPU:0")
        my_updated_spec = tf.DeviceSpec.from_string("/GPU:0")
        with tf.device(my_updated_spec):
          ...
    
*   Will work in 1.x and 2.x (though deprecated in 2.x):
    
    my_spec = tf.DeviceSpec.from_string("/CPU:0")
        my_updated_spec = my_spec.parse_from_string("/GPU:0")
        with tf.device(my_updated_spec):
          ...
    
*   Will NOT work in 2.x:
    
    my_spec = tf.DeviceSpec.from_string("/CPU:0")
        my_spec.parse_from_string("/GPU:0")  # <== Will not update my_spec
        with tf.device(my_spec):
          ...
    

In general, [`DeviceSpec.from_string`](https://www.tensorflow.org/api_docs/python/tf/DeviceSpec#from_string)
 should completely replace [`DeviceSpec.parse_from_string`](https://www.tensorflow.org/api_docs/python/tf/DeviceSpec#parse_from_string)
, and [`DeviceSpec.replace`](https://www.tensorflow.org/api_docs/python/tf/DeviceSpec#replace)
 should completely replace setting attributes directly.

|     |     |
| --- | --- |
| Args |     |
| `spec` | an optional string of the form /job:/replica:/task:/device:CPU: or /job:/replica:/task:/device:GPU: as cpu and gpu are mutually exclusive. All entries are optional. |

|     |
| --- |
| Returns |     |
| The `DeviceSpec`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | if the spec was not valid. |

### `replace`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/device_spec.py#L239-L264)

replace(
        **kwargs
    )

Convenience method for making a new DeviceSpec by overriding fields.

#### For instance:

my_spec = DeviceSpec=(job="my_job", device="CPU")
    my_updated_spec = my_spec.replace(device="GPU")
    my_other_spec = my_spec.replace(device=None)

|     |     |
| --- | --- |
| Args |     |
| `**kwargs` | This method takes the same args as the DeviceSpec constructor |

|     |
| --- |
| Returns |     |
| A DeviceSpec with the fields specified in kwargs overridden. |     |

### `to_string`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/device_spec.py#L455-L463)

to_string()

Return a string representation of this `DeviceSpec`.

|     |
| --- |
| Returns |     |
| a string of the form /job:/replica:/task:/device::. |     |

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/device_spec.py#L395-L409)

__eq__(
        other
    )

Checks if the `other` DeviceSpec is same as the current instance, eg have

same value for all the internal fields.

|     |     |
| --- | --- |
| Args |     |
| `other` | Another DeviceSpec |

|     |
| --- |
| Returns |     |
| Return `True` if `other` is also a DeviceSpec instance and has same value as the current instance. Return `False` otherwise. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.