Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/accelerator/distributed.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/accelerator/distributed.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/accelerator/distributed.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/accelerator/distributed.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/accelerator/distributed.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/accelerator/distributed.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/accelerator/distributed.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/accelerator/distributed.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/accelerator/distributed.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/accelerator/distributed.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/accelerator/distributed.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/accelerator/distributed.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/accelerator/distributed.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/accelerator/distributed.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/accelerator/distributed.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/accelerator/distributed.html)
[v1.13](https://docs.pytorch.org/docs/1.13/accelerator/distributed.html)
[v1.12](https://docs.pytorch.org/docs/1.12/accelerator/distributed.html)
[v1.11](https://docs.pytorch.org/docs/1.11/accelerator/distributed.html)
[v1.10](https://docs.pytorch.org/docs/1.10/accelerator/distributed.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/accelerator/distributed.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/accelerator/distributed.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/accelerator/distributed.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/accelerator/distributed.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/accelerator/distributed.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/accelerator/distributed.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/accelerator/distributed.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/accelerator/distributed.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/accelerator/distributed.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/accelerator/distributed.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/accelerator/distributed.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/accelerator/distributed.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/accelerator/distributed.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/accelerator/distributed.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/accelerator/distributed.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/accelerator/distributed.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/accelerator/distributed.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/accelerator/distributed.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/accelerator/distributed.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/accelerator/distributed.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/accelerator/distributed.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/accelerator/distributed.html)

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

Distributed Training Integration[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#distributed-training-integration "Link to this heading")

=============================================================================================================================================================

Created On: May 18, 2026 | Last Updated On: May 18, 2026

Background[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#background "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

Distributed training allows accelerators to scale workloads across multiple devices and nodes by coordinating collective communication (e.g., allreduce, broadcast, allgather) through a [ProcessGroup](https://github.com/pytorch/pytorch/blob/main/torch/csrc/distributed/c10d/ProcessGroup.hpp)
 backend. PyTorch ships built-in backends such as [NCCL](https://developer.nvidia.com/nccl)
 for CUDA and [Gloo](https://github.com/facebookincubator/gloo)
 for CPU, but the framework exposes a registration mechanism that allows out-of-tree accelerator vendors to plug in their own collective communication library without modifying upstream code.

The integration surface can be broken down into three layers:

1.  **C++ Backend implementation** – A subclass of [`c10d::Backend`](https://github.com/pytorch/pytorch/blob/main/torch/csrc/distributed/c10d/Backend.hpp "Backend.hpp")
     that implements the collective, point-to-point, and synchronization operations.
    
2.  **Python bindings** – Expose the C++ backend class to Python via [pybind11](https://pybind11.readthedocs.io/)
    .
    
3.  **Backend registration** – Register the backend with [`torch.distributed.Backend.register_backend()`](https://github.com/pytorch/pytorch/blob/main/torch/distributed/distributed_c10d.py "distributed_c10d.py")
     so that `init_process_group` can discover and instantiate it.
    

Note

[OpenReg](https://github.com/pytorch/pytorch/tree/main/test/cpp_extensions/open_registration_extension/torch_openreg)
 (`torch_openreg`) is PyTorch’s official reference implementation for out-of-tree accelerator integration. It ships a minimal distributed backend called **OCCL** (OpenReg Collective Communications Library) that demonstrates the full `ProcessGroup` integration. All code examples in this chapter reference the OCCL implementation.

Before You Start[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#before-you-start "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

This guide covers **ProcessGroup backend integration** only – how to register a custom collective communication backend with `torch.distributed`. It does not cover full-stack integration with higher-level APIs such as DDP, FSDP, or other distributed training strategies.

Before following this guide, make sure you have:

*   **An importable `torch_xxx` extension package** that registers your device via `PrivateUse1`. See the earlier chapters in this guide for device registration, operators, and runtime hooks.
    
*   **A collective communication library (CCL)** that provides implementations of basic collectives such as `allreduce` and `broadcast` for your device. The CCL can be vendor-provided (e.g., NCCL for NVIDIA, HCCL for Huawei) or a custom implementation.
    

Design[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#design "Link to this heading")

---------------------------------------------------------------------------------------------------------

This section describes the interfaces and concepts involved in backend registration.

### Registration API[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#registration-api "Link to this heading")

The primary entry point for OOT backend registration is [`Backend.register_backend()`](https://github.com/pytorch/pytorch/blob/main/torch/distributed/distributed_c10d.py "distributed_c10d.py")
:

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `str` | Backend name, e.g. `"occl"`. Must match the value passed to `init_process_group(backend=...)`. |
| `func` | `Callable` | Factory function that creates a backend instance (see signature below). |
| `extended_api` | `bool` | If `True`, the factory receives a `_DistributedBackendOptions` object instead of individual arguments. |
| `devices` | `str \| list[str] \| None` | Device types supported by this backend, e.g. `["openreg"]`. Populates the device-to-backend mapping. |

When `devices` is specified, the backend is automatically associated with those device types. This means `init_process_group()` can resolve the correct backend when the user passes a `device_id` argument without explicitly naming a backend.

### Factory Function Signature[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#factory-function-signature "Link to this heading")

The factory function receives different arguments depending on `extended_api`:

| Mode | Signature |
| --- | --- |
| Standard (default) | `func(store: Store, rank: int, world_size: int, timeout: timedelta) -> Backend` |
| Extended API | `func(dist_backend_opts: _DistributedBackendOptions, backend_options) -> Backend` |

The standard mode is sufficient for most backends. The extended API provides additional context such as `group_id` and `global_ranks_in_group`.

### Backend Operations[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#backend-operations "Link to this heading")

The [`c10d::Backend`](https://github.com/pytorch/pytorch/blob/main/torch/csrc/distributed/c10d/Backend.hpp "Backend.hpp")
 base class defines virtual methods for collective, point-to-point, and synchronization operations. Each operation returns a [`c10::intrusive_ptr<Work>`](https://github.com/pytorch/pytorch/blob/main/torch/csrc/distributed/c10d/Work.hpp "Work.hpp")
 that represents the asynchronous operation. For backends with synchronous operations, the `Work` object can be immediately completed.

#### Minimal Required Operations[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#minimal-required-operations "Link to this heading")

To get a working backend that supports basic distributed training, implement the following operations at minimum:

| Category | Operations |
| --- | --- |
| **Collective** | `broadcast`, `allreduce`, `allgather`, `reduce_scatter` |
| **Synchronization** | `barrier` |

These cover the core communication patterns used by DDP and other common distributed workflows.

#### Extended Operations[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#extended-operations "Link to this heading")

For broader compatibility with advanced distributed strategies (e.g., FSDP, model parallelism, pipeline parallelism), implement the full set of operations:

| Category | Operations |
| --- | --- |
| **Collective** | `allreduce_coalesced`, `reduce`, `_allgather_base`, `allgather_coalesced`, `allgather_into_tensor_coalesced`, `gather`, `scatter`, `_reduce_scatter_base`, `reduce_scatter_tensor_coalesced`, `alltoall_base` |
| **Point-to-Point** | `send`, `recv`, `recvAnysource` |

See [`Backend.hpp`](https://github.com/pytorch/pytorch/blob/main/torch/csrc/distributed/c10d/Backend.hpp "Backend.hpp")
 for the full list of virtual methods and their signatures.

### Optional Capabilities[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#optional-capabilities "Link to this heading")

Backends can advertise optional capabilities by overriding the following methods:

| Method | Default | Description |
| --- | --- | --- |
| `supportsSplitting()` | `false` | Process group splitting support |
| `supportsCoalescing()` | `false` | Coalesced collective operations |

Implementation[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#implementation "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

This section walks through the concrete steps to implement and register a backend, using the OCCL reference implementation as an example. The implementation follows three steps:

1.  Implement the C++ backend
    
2.  Create Python bindings
    
3.  Register the backend in Python
    

### Step 1: Implement the C++ Backend[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#step-1-implement-the-c-backend "Link to this heading")

Create a class that inherits from `c10d::Backend` and implements the required collective operations. The backend must also define:

*   A **`Work` subclass** that tracks asynchronous operation state
    
*   An **`Options` subclass** (inheriting from `Backend::Options`) for backend-specific configuration
    

#### Work Object[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#work-object "Link to this heading")

The `Work` subclass manages the lifecycle of an asynchronous collective operation. For a minimal (synchronous) implementation, the work can be completed immediately in its constructor:

ProcessGroupOCCL::DummyWork declaration (ProcessGroupOCCL.hpp)[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#id1 "Link to this code")

 1  class DummyWork : public Work {
 2   public:
 3    DummyWork();
 4
 5    virtual ~DummyWork();
 6    bool isCompleted() override;
 7    bool isSuccess() const override;
 8    bool wait(std::chrono::milliseconds timeout) override;
 9    void synchronize() override;
10    void abort() override;
11    c10::intrusive\_ptr<c10::ivalue::Future\> getFuture() override;
12
13   protected:
14    friend class ProcessGroupOCCL;
15
16   private:
17    c10::intrusive\_ptr<c10::ivalue::Future\> future\_;
18  };

Copy to clipboard

For production backends, `Work` typically wraps an asynchronous handle from the vendor’s communication library (e.g., a stream event or request handle), and `wait()` blocks until the operation completes on the device.

#### Backend Class[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#backend-class "Link to this heading")

The backend class inherits from `c10d::Backend` and overrides the collective operations. Each method should validate that input tensors reside on the expected device type (e.g., `PrivateUse1`) and then dispatch to the vendor’s communication library. Key implementation details:

*   **`getBackendName()`** must return the same string used during Python registration (e.g., `"occl"`).
    
*   **Input validation** – Each collective should verify tensor device types. The OCCL reference uses `CHECK_TENSOR` and `CHECK_TENSOR_LIST` macros for this.
    
*   **Return value** – All collectives return a `c10::intrusive_ptr<Work>`.
    

See [`ProcessGroupOCCL.hpp`](https://github.com/pytorch/pytorch/blob/main/test/cpp_extensions/open_registration_extension/torch_openreg/csrc/distributed/c10d/ProcessGroupOCCL.hpp "ProcessGroupOCCL.hpp")
 and [`ProcessGroupOCCL.cpp`](https://github.com/pytorch/pytorch/blob/main/test/cpp_extensions/open_registration_extension/torch_openreg/csrc/distributed/c10d/ProcessGroupOCCL.cpp "ProcessGroupOCCL.cpp")
 for the full reference implementation.

### Step 2: Python Bindings[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#step-2-python-bindings "Link to this heading")

Expose the backend class to Python using pybind11. The OCCL reference places bindings in a dedicated [`init.cpp`](https://github.com/pytorch/pytorch/blob/main/test/cpp_extensions/open_registration_extension/torch_openreg/torch_openreg/csrc/distributed/init.cpp "init.cpp")
 file, separate from the main extension module, and calls `initProcessGroupBindings()` from the module’s entry point:

Python bindings for OCCL (init.cpp)[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#id2 "Link to this code")

 1void initProcessGroupBindings(py::module& m) {
 2  py::class\_<c10d::ProcessGroupOCCL, c10d::Backend, c10::intrusive\_ptr<c10d::ProcessGroupOCCL\>>(m, "ProcessGroupOCCL")
 3      .def(
 4          py::init(\[\](const c10::intrusive\_ptr<::c10d::Store\>& /\*store\*/,
 5                      int rank,
 6                      int size,
 7                      std::chrono::milliseconds /\*timeout\*/) {
 8            return c10::make\_intrusive<::c10d::ProcessGroupOCCL\>(rank, size);
 9          }),
10          py::arg("store"),
11          py::arg("rank"),
12          py::arg("size"),
13          py::arg("timeout") \= std::chrono::milliseconds(30 \* 60 \* 1000));
14}

Copy to clipboard

Important considerations:

*   The `py::class_` template must list `c10d::Backend` as a base class and use `c10::intrusive_ptr` as the holder, so that PyTorch recognizes the backend in its internal registry.
    
*   The constructor is exposed directly via `py::init` with a lambda that forwards to the C++ constructor. This avoids the need for a separate factory function.
    
*   Guard the bindings with `#if USE_DISTRIBUTED` to handle builds where distributed is disabled.
    

### Step 3: Register the Backend in Python[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#step-3-register-the-backend-in-python "Link to this heading")

In the extension package’s `__init__.py`, register the backend with `torch.distributed`:

Backend registration (torch\_openreg/\_\_init\_\_.py)[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#id3 "Link to this code")

 1if torch.distributed.is\_available():
 2    try:
 3        from torch\_openreg.\_C import ProcessGroupOCCL
 4
 5        def \_create\_occl\_backend(store, rank, size, timeout):
 6            return ProcessGroupOCCL(store, rank, size, timeout)
 7
 8        torch.distributed.Backend.register\_backend(
 9            "occl", \_create\_occl\_backend, devices\=\["openreg"\]
10        )
11    except Exception as e:
12        raise RuntimeError("Failed to register 'occl' process group backend.") from e

Copy to clipboard

The Python side imports the pybind11-exposed `ProcessGroupOCCL` class and wraps it in a thin factory function that matches the signature expected by `register_backend()`. The call to `Backend.register_backend()` does the following:

1.  Adds `"occl"` to `Backend.backend_list`, making it a recognized backend name.
    
2.  Maps `"openreg"` device type to the `"occl"` backend in `Backend.default_device_backend_map`.
    
3.  Stores the factory function so that `init_process_group()` can call it when `backend="occl"` is specified.
    

Usage[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#usage "Link to this heading")

-------------------------------------------------------------------------------------------------------

After registration, the backend integrates seamlessly with `torch.distributed`:

import torch
import torch.distributed as dist

\# Import triggers autoload, which registers the "occl" backend
import torch\_openreg

\# Initialize process group – OCCL is auto-selected for openreg devices
dist.init\_process\_group(
    backend\="occl",
    init\_method\="env://",
    world\_size\=2,
    rank\=0,
)

\# Use standard distributed APIs
tensor \= torch.randn(4, device\="openreg")
dist.all\_reduce(tensor)

dist.destroy\_process\_group()

Copy to clipboard

Alternatively, the backend name can be omitted if a `device_id` is provided – PyTorch resolves the backend from the device-to-backend mapping:

dist.init\_process\_group(
    device\_id\=torch.device("openreg:0"),
    init\_method\="env://",
    world\_size\=2,
    rank\=0,
)

Copy to clipboard

### Multi-device Backend Strings[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#multi-device-backend-strings "Link to this heading")

PyTorch supports specifying different backends for different device types in a single process group using the `"device:backend"` format:

dist.init\_process\_group(
    backend\="cpu:gloo,openreg:occl",
    init\_method\="env://",
    world\_size\=2,
    rank\=0,
)

Copy to clipboard

Testing[#](https://docs.pytorch.org/docs/2.15/accelerator/distributed.html#testing "Link to this heading")

-----------------------------------------------------------------------------------------------------------

Key testing considerations:

*   Verify that the backend appears in `dist.Backend.backend_list` after import.
    
*   Confirm that `init_process_group` / `destroy_process_group` succeeds.
    
*   Test that collective operations accept tensors on the registered device and return completed `Work` objects.
    
*   Use `MultiProcessTestCase` from `torch.testing._internal.common_distributed` for multi-process test execution.
    

See the [OCCL test suite](https://github.com/pytorch/pytorch/blob/main/test/cpp_extensions/open_registration_extension/torch_openreg/tests/test_distributed.py)
 for a reference example.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/accelerator/distributed.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/accelerator/distributed.md.txt)

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