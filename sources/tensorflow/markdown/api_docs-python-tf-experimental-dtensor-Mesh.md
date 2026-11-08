[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fexperimental%2Fdtensor%2FMesh&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#methods)
    *   [as\_proto](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#as_proto)
        
    *   [contains\_dim](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#contains_dim)
        
    *   [coords](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#coords)
        
    *   [device\_location](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#device_location)
        
    *   [device\_type](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#device_type)
        
    *   [dim\_size](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#dim_size)
        
    *   [from\_device](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#from_device)
        
    *   [from\_proto](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#from_proto)
        
    *   [from\_string](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#from_string)
        
    *   [global\_device\_ids](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#global_device_ids)
        
    *   [global\_devices](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#global_devices)
        
    *   [host\_mesh](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#host_mesh)
        
    *   [is\_remote](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#is_remote)
        
    *   [is\_single\_device](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#is_single_device)
        
    *   [local\_device\_ids](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#local_device_ids)
        
    *   [local\_device\_locations](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#local_device_locations)
        
    *   [local\_devices](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#local_devices)
        
    *   [min\_global\_device\_id](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#min_global_device_id)
        
    *   [num\_local\_devices](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#num_local_devices)
        
    *   [shape](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#shape)
        
    *   [to\_string](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#to_string)
        
    *   [unravel\_index](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#unravel_index)
        
    *   [use\_xla\_spmd](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#use_xla_spmd)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#__eq__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#__getitem__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dtensor.Mesh Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#methods)
    *   [as\_proto](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#as_proto)
        
    *   [contains\_dim](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#contains_dim)
        
    *   [coords](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#coords)
        
    *   [device\_location](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#device_location)
        
    *   [device\_type](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#device_type)
        
    *   [dim\_size](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#dim_size)
        
    *   [from\_device](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#from_device)
        
    *   [from\_proto](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#from_proto)
        
    *   [from\_string](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#from_string)
        
    *   [global\_device\_ids](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#global_device_ids)
        
    *   [global\_devices](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#global_devices)
        
    *   [host\_mesh](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#host_mesh)
        
    *   [is\_remote](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#is_remote)
        
    *   [is\_single\_device](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#is_single_device)
        
    *   [local\_device\_ids](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#local_device_ids)
        
    *   [local\_device\_locations](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#local_device_locations)
        
    *   [local\_devices](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#local_devices)
        
    *   [min\_global\_device\_id](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#min_global_device_id)
        
    *   [num\_local\_devices](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#num_local_devices)
        
    *   [shape](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#shape)
        
    *   [to\_string](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#to_string)
        
    *   [unravel\_index](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#unravel_index)
        
    *   [use\_xla\_spmd](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#use_xla_spmd)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#__eq__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh#__getitem__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L53-L344)

Represents a Mesh configuration over a certain list of Mesh Dimensions.

tf.experimental.dtensor.Mesh(
        dim_names: List[str],
        global_device_ids: np.ndarray,
        local_device_ids: List[int],
        local_devices: List[Union[tf_device.DeviceSpec, str]],
        mesh_name: str = '',
        global_devices: Optional[List[Union[tf_device.DeviceSpec, str]]] = None,
        use_xla_spmd: bool = USE_XLA_SPMD
    )

A mesh consists of named dimensions with sizes, which describe how a set of devices are arranged. Defining tensor layouts in terms of mesh dimensions allows us to efficiently determine the communication required when computing an operation with tensors of different layouts.

A mesh provides information not only about the placement of the tensors but also the topology of the underlying devices. For example, we can group 8 TPUs as a 1-D array for data parallelism or a `2x4` grid for (2-way) data parallelism and (4-way) model parallelism.

Refer to [DTensor Concepts](https://www.tensorflow.org/guide/dtensor_overview)
 for in depth discussion and examples.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dim_names` | A list of strings indicating dimension names. |
| `global_device_ids` | An ndarray of global device IDs is used to compose DeviceSpecs describing the mesh. The shape of this array determines the size of each mesh dimension. Values in this array should increment sequentially from 0. This argument is the same for every DTensor client. |
| `local_device_ids` | A list of local device IDs equal to a subset of values in global\_device\_ids. They indicate the position of local devices in the global mesh. Different DTensor clients must contain distinct local\_device\_ids contents. All local\_device\_ids from all DTensor clients must cover every element in global\_device\_ids. |
| `local_devices` | The list of devices hosted locally. The elements correspond 1:1 to those of local\_device\_ids. |
| `mesh_name` | The name of the mesh. Currently, this is rarely used, and is mostly used to indicate whether it is a CPU, GPU, or TPU-based mesh. |
| `global_devices` | `optional`<br><br>The list of global devices. Set when multiple device meshes are in use. |
| `use_xla_spmd` | `optional`<br><br>Boolean when True, will use XLA SPMD instead of DTensor SPMD. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `dim_names` |     |
| `name` |     |
| `single_device` |     |
| `size` |     |
| `strides` | Returns the strides tensor array for this mesh.<br><br>If the mesh shape is `[a, b, c, d]`, then the strides array can be computed as `[b*c*d, c*d, d, 1]`. This array can be useful in computing local device offsets given a device ID. Using the same example, the device coordinates of the mesh can be computed as:<br><br>[(device_id / (b*c*d)) % a,<br>     (device_id / (c*d))   % b,<br>     (device_id / (d))     % c,<br>     (device_id)           % d]<br><br>This is the same as `(device_id // mesh.strides) % mesh.shape`. |

Methods
-------

### `as_proto`

as_proto()

as\_proto(self: tensorflow.python.\_pywrap\_dtensor\_device.Mesh) -> tensorflow::dtensor::MeshProto

Returns the MeshProto protobuf message.

### `contains_dim`

contains_dim()

contains\_dim(self: tensorflow.python.\_pywrap\_dtensor\_device.Mesh, dim\_name: str) -> bool

Returns True if a Mesh contains the given dimension name.

### `coords`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L252-L256)

coords(
        device_idx: int
    ) -> tf.Tensor

Converts the device index into a tensor of mesh coordinates.

### `device_location`

device_location()

device\_location(self: tensorflow.python.\_pywrap\_dtensor\_device.Mesh, arg0: int) -> list\[int\]

### `device_type`

device_type()

device\_type(self: tensorflow.python.\_pywrap\_dtensor\_device.Mesh) -> str

Returns the device\_type of a Mesh.

### `dim_size`

dim_size()

dim\_size(self: tensorflow.python.\_pywrap\_dtensor\_device.Mesh, dim\_name: str) -> int

Returns the size of mesh dimension.

### `from_device`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L267-L270)

@classmethod

Constructs a single device mesh from a device string.

### `from_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L258-L261)

@classmethod

Construct a mesh instance from input `proto`.

### `from_string`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L263-L265)

@classmethod

### `global_device_ids`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L232-L236)

global_device_ids() -> np.ndarray

Returns a global device list as an array.

### `global_devices`

global_devices()

global\_devices(self: tensorflow.python.\_pywrap\_dtensor\_device.Mesh) -> list\[str\]

Returns a list of global device specs represented as strings.

### `host_mesh`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L281-L285)

host_mesh() -> 'Mesh'

Returns a host mesh.

### `is_remote`

is_remote()

is\_remote(self: tensorflow.python.\_pywrap\_dtensor\_device.Mesh) -> bool

Returns True if a Mesh contains only remote devices.

### `is_single_device`

is_single_device()

is\_single\_device(self: tensorflow.python.\_pywrap\_dtensor\_device.Mesh) -> bool

Returns True if the mesh represents a non-distributed device.

### `local_device_ids`

local_device_ids()

local\_device\_ids(self: tensorflow.python.\_pywrap\_dtensor\_device.Mesh) -> Span\[int\]

Returns a list of local device IDs.

### `local_device_locations`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L288-L295)

local_device_locations() -> List[Dict[str, int]]

Returns a list of local device locations.

A device location is a dictionary from dimension names to indices on those dimensions.

### `local_devices`

local_devices()

local\_devices(self: tensorflow.python.\_pywrap\_dtensor\_device.Mesh) -> Span\[str\]

Returns a list of local device specs represented as strings.

### `min_global_device_id`

min_global_device_id()

min\_global\_device\_id(self: tensorflow.python.\_pywrap\_dtensor\_device.Mesh) -> int

Returns the minimum global device ID.

### `num_local_devices`

num_local_devices()

num\_local\_devices(self: tensorflow.python.\_pywrap\_dtensor\_device.Mesh) -> int

Returns the number of local devices.

### `shape`

shape()

shape(self: tensorflow.python.\_pywrap\_dtensor\_device.Mesh) -> list\[int\]

Returns the shape of the mesh.

### `to_string`

to_string()

to\_string(self: tensorflow.python.\_pywrap\_dtensor\_device.Mesh) -> str

Returns string representation of Mesh.

### `unravel_index`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L322-L344)

unravel_index()

Returns a dictionary from device ID to {dim\_name: dim\_index}.

For example, for a 3x2 mesh, return this:

  { 0: {'x': 0, 'y', 0},
        1: {'x': 0, 'y', 1},
        2: {'x': 1, 'y', 0},
        3: {'x': 1, 'y', 1},
        4: {'x': 2, 'y', 0},
        5: {'x': 2, 'y', 1} }

### `use_xla_spmd`

use_xla_spmd()

use\_xla\_spmd(self: tensorflow.python.\_pywrap\_dtensor\_device.Mesh) -> bool

Returns True if Mesh will use XLA for SPMD instead of DTensor SPMD.

### `__contains__`

__contains__()

**contains**(self: tensorflow.python.\_pywrap\_dtensor\_device.Mesh, dim\_name: str) -> bool

### `__eq__`

__eq__()

**eq**(self: tensorflow.python.\_pywrap\_dtensor\_device.Mesh, arg0: tensorflow.python.\_pywrap\_dtensor\_device.Mesh) -> bool

### `__getitem__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/layout.py#L238-L239)

__getitem__(
        dim_name: str
    ) -> MeshDimension

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.