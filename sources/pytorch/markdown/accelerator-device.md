Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/accelerator/device.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/accelerator/device.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/accelerator/device.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/accelerator/device.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/accelerator/device.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/accelerator/device.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/accelerator/device.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/accelerator/device.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/accelerator/device.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/accelerator/device.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/accelerator/device.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/accelerator/device.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/accelerator/device.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/accelerator/device.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/accelerator/device.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/accelerator/device.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/accelerator/device.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/accelerator/device.html)
[v1.13](https://docs.pytorch.org/docs/1.13/accelerator/device.html)
[v1.12](https://docs.pytorch.org/docs/1.12/accelerator/device.html)
[v1.11](https://docs.pytorch.org/docs/1.11/accelerator/device.html)
[v1.10](https://docs.pytorch.org/docs/1.10/accelerator/device.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/accelerator/device.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/accelerator/device.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/accelerator/device.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/accelerator/device.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/accelerator/device.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/accelerator/device.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/accelerator/device.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/accelerator/device.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/accelerator/device.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/accelerator/device.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/accelerator/device.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/accelerator/device.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/accelerator/device.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/accelerator/device.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/accelerator/device.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/accelerator/device.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/accelerator/device.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/accelerator/device.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/accelerator/device.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/accelerator/device.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/accelerator/device.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/accelerator/device.html)

[Go to pytorch.org](https://pytorch.org/)

 Ctrl+K

|     |     |
| --- | --- |
|     | [×](javascript:void(0) "Clear search box") |

search

Custom Search

|     |     |
| --- | --- |
|     | Sort by<br><br>Relevance<br><br>Date |

*   [X](https://x.com/PyTorch)
    
*   [GitHub](https://github.com/pytorch/pytorch)
    
*   [PyTorch Forum](https://discuss.pytorch.org/)
    
*   [PyPi](https://pypi.org/project/torch/)
    

Rate this Page

★ ★ ★ ★ ★

Device Management[#](https://docs.pytorch.org/docs/2.15/accelerator/device.html#device-management "Link to this heading")

==========================================================================================================================

Created On: Nov 14, 2025 | Last Updated On: Dec 09, 2025

Background[#](https://docs.pytorch.org/docs/2.15/accelerator/device.html#background "Link to this heading")

------------------------------------------------------------------------------------------------------------

Device management covers basics such as querying how many devices are available and switching between them. Accelerator backends wrap their device‑runtime APIs and expose them to PyTorch.

Design[#](https://docs.pytorch.org/docs/2.15/accelerator/device.html#design "Link to this heading")

----------------------------------------------------------------------------------------------------

Accelerator vendors should implement these core functions:

| Function name | Description | Application scenarios |
| --- | --- | --- |
| `device_count()` | Query the total number of available devices in the system | \- Application initialization  <br>\- Multi-device workload distribution  <br>\- Validating device indices before use |
| `current_device()` | Get the currently active device for the calling thread | \- Debugging and logging  <br>\- Determining tensor placement  <br>\- Guard implementations |
| `set_device()` | Change the active device for subsequent operations | \- Switching context between devices  <br>\- Initializing specific device resources  <br>\- Multi-GPU training loops |
| `exchange_device()` | Atomically swap device and return the previous device | \- Implementing device guards  <br>\- Temporarily switching device context  <br>\- RAII-based device management |
| `maybe_exchange_device()` | Conditionally exchange device only if the index is valid (−1 allowed) | \- Safe device switching with optional indices  <br>\- Guard implementations with nullable device values |

These functions are the building blocks for streams, events, and memory management. Validate inputs and handle errors properly.

Implementation[#](https://docs.pytorch.org/docs/2.15/accelerator/device.html#implementation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

This section illustrates device management using `set_device` as an example. The implementation requires:

1.  C++ wrappers around the device runtime
    
2.  Python bindings to expose the C++ functions
    
3.  User-friendly Python APIs
    

For illustration, OpenReg (Open Registration) is a PyTorch integration example that fills the gap for out‑of‑tree accelerator backend integration. Its implementation ([`OpenRegFunctions.h/cpp`](https://github.com/pytorch/pytorch/blob/main/test/cpp_extensions/open_registration_extension/torch_openreg/csrc/runtime/OpenRegFunctions.cpp "OpenReg Device Management")
) demonstrates how to wrap a third‑party runtime cleanly. These functions are reused across the backend—for streams, events, generators, and Python bindings.

### C++ side[#](https://docs.pytorch.org/docs/2.15/accelerator/device.html#c-side "Link to this heading")

Wrap the device‑runtime API and add error handling. The `SetDevice` function shows this pattern:

1orError\_t SetDevice(DeviceIndex device) {
2  int cur\_device \= \-1;
3  OPENREG\_CHECK(orGetDevice(&cur\_device));
4  if (device \== cur\_device) {
5    return orSuccess;
6  }
7  return orSetDevice(device);
8}

Copy to clipboard

1OPENREG\_EXPORT void set\_device(DeviceIndex device) {
2  check\_device\_index(device);
3  OPENREG\_CHECK(SetDevice(device));
4}

Copy to clipboard

### Bindings[#](https://docs.pytorch.org/docs/2.15/accelerator/device.html#bindings "Link to this heading")

Expose the C++ functions to Python using pybind11:

 1PyObject\* \_setDevice(PyObject\* self, PyObject\* arg) {
 2  HANDLE\_TH\_ERRORS
 3  TORCH\_CHECK(THPUtils\_checkLong(arg), "invalid argument to setDevice");
 4  auto device \= THPUtils\_unpackDeviceIndex(arg);
 5  torch::utils::device\_lazy\_init(at::kPrivateUse1);
 6  c10::openreg::set\_device(device);
 7
 8  Py\_RETURN\_NONE;
 9  END\_HANDLE\_TH\_ERRORS
10}

Copy to clipboard

1static PyMethodDef methods\[\] \= {
2    {"\_init", \_initExtension, METH\_NOARGS, nullptr},
3    {"\_isInBadFork", \_isInBadFork, METH\_NOARGS, nullptr},
4    {"\_get\_default\_generator", \_getDefaultGenerator, METH\_O, nullptr},
5    {"\_get\_device", \_getDevice, METH\_NOARGS, nullptr},
6    {"\_set\_device", \_setDevice, METH\_O, nullptr},
7    {"\_exchangeDevice", \_exchangeDevice, METH\_O, nullptr},
8    {"\_get\_device\_count", \_getDeviceCount, METH\_NOARGS, nullptr},
9    {nullptr, nullptr, 0, nullptr}};

Copy to clipboard

### Python side[#](https://docs.pytorch.org/docs/2.15/accelerator/device.html#python-side "Link to this heading")

Wrap the C++ bindings with user-friendly Python functions:

1def set\_device(device) \-> None:
2    if device \>= 0:
3        torch\_openreg.\_C.\_set\_device(device)
4
5

Copy to clipboard

Here’s the complete mapping from C++ to Python:

| C++ binding function | C++ binding API (pybind11) | Python user API | Description |
| --- | --- | --- | --- |
| `_getDeviceCount` | `torch_openreg._C._get_device_count()` | `torch.openreg.device_count()` | Returns the total number of devices |
| `_getDevice` | `torch_openreg._C._get_device()` | `torch.openreg.current_device()` | Returns the current active device index |
| `_setDevice` | `torch_openreg._C._set_device(idx)` | `torch.openreg.set_device(idx)` | Sets the active device |
| `_exchangeDevice` | `torch_openreg._C._exchange_device(idx)` | N/A (internal use only) | Atomically swaps device and returns previous |

Guard[#](https://docs.pytorch.org/docs/2.15/accelerator/device.html#guard "Link to this heading")

--------------------------------------------------------------------------------------------------

Device guards provide automatic device switching with exception safety. They’re similar to C++ lock guards—they switch devices on construction and restore on destruction.

Implement `DeviceGuardImplInterface` to integrate with PyTorch’s guard system:

 1  /\*\*
 2   \* Return the type of device managed by this guard implementation.
 3   \*/
 4  DeviceType type() const override {
 5    return static\_type;
 6  }
 7  /\*\*
 8   \* Set the current device to device d, and return the previous Device.
 9   \*/
10  // LITERALINCLUDE START: OPENREG GUARD DEVICE MANAGEMENT
11  Device exchangeDevice(Device d) const override {
12    TORCH\_CHECK(d.is\_privateuseone(), "Expected a PrivateUse1 device, but got ", d);
13
14    auto old\_device\_index \= ExchangeDevice(d.index());
15    return Device(static\_type, old\_device\_index);
16  }
17  // LITERALINCLUDE END: OPENREG GUARD DEVICE MANAGEMENT
18
19  /\*\*
20   \* Get the current device.
21   \*/
22  Device getDevice() const override {
23    int device\_index \= current\_device();
24    return c10::Device(static\_type, device\_index);
25  }
26
27  /\*\*
28   \* Get the device capability for a given device.
29   \* By default, OpenReg has 2 same devices with the same capability.
30   \*/
31  DeviceCapability getDeviceCapability(Device /\*unused\*/) const override {
32    return DeviceCapability();
33  }
34
35  /\*\*
36   \* Set the current device to c10::Device.
37   \*/
38  void setDevice(Device d) const override {
39    TORCH\_CHECK(d.is\_privateuseone(), "Expected a PrivateUse1 device, but got ", d);
40
41    set\_device(d.index());
42  }
43
44  /\*\*
45   \* Set the current device to device d, without checking for errors
46   \* (so, e.g., this can be called from a destructor).
47   \*/
48  void uncheckedSetDevice(Device d) const noexcept override {
49    set\_device(d.index());
50  }
51
52  /\*\*
53   \* Get the number of devices.
54   \*
55   \* WARNING: This is REQUIRED to not raise an exception.
56   \* If there is some sort of problem, e.g., driver error,
57   \* you should report that there are zero available devices.
58   \*/
59  DeviceIndex deviceCount() const noexcept override {
60    return device\_count();
61  }
62
63  /\*\*
64   \* Wait (by blocking the calling thread) until all the work has
65   \* completed running on the device.
66   \*/
67  void synchronizeDevice(const DeviceIndex device\_index) const override {
68    OPENREG\_CHECK(orDeviceSynchronize());
69  }

Copy to clipboard

This makes the guard available in PyTorch for the `PrivateUse1` device type; users can then use standard PyTorch device guards with the custom backend.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/accelerator/device.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/accelerator/device.md.txt)

PyTorch Libraries

*   [ExecuTorch](https://docs.pytorch.org/executorch)
    
*   [Helion](https://docs.pytorch.org/helion)
    
*   [torchao](https://docs.pytorch.org/ao)
    
*   [kineto](https://github.com/pytorch/kineto)
    
*   [torchtitan](https://github.com/pytorch/torchtitan)
    
*   [TorchRL](https://docs.pytorch.org/rl)
    
*   [torchvision](https://docs.pytorch.org/vision)
    
*   [torchaudio](https://docs.pytorch.org/audio)
    
*   [tensordict](https://docs.pytorch.org/tensordict)
    
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)
    

Docs
----

Access comprehensive developer documentation for PyTorch

[View Docs](https://docs.pytorch.org/docs/stable/index.html)

Tutorials
---------

Get in-depth tutorials for beginners and advanced developers

[View Tutorials](https://docs.pytorch.org/tutorials)

Resources
---------

Find development resources and get your questions answered

[View Resources](https://pytorch.org/resources)

To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy)
.

|     |     |
| --- | --- |
|     |     |

|     |     |
| --- | --- |
|     |     |