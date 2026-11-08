Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/accelerator/hooks.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/accelerator/hooks.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/accelerator/hooks.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/accelerator/hooks.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/accelerator/hooks.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/accelerator/hooks.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/accelerator/hooks.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/accelerator/hooks.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/accelerator/hooks.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/accelerator/hooks.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/accelerator/hooks.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/accelerator/hooks.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/accelerator/hooks.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/accelerator/hooks.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/accelerator/hooks.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/accelerator/hooks.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/accelerator/hooks.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/accelerator/hooks.html)
[v1.13](https://docs.pytorch.org/docs/1.13/accelerator/hooks.html)
[v1.12](https://docs.pytorch.org/docs/1.12/accelerator/hooks.html)
[v1.11](https://docs.pytorch.org/docs/1.11/accelerator/hooks.html)
[v1.10](https://docs.pytorch.org/docs/1.10/accelerator/hooks.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/accelerator/hooks.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/accelerator/hooks.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/accelerator/hooks.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/accelerator/hooks.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/accelerator/hooks.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/accelerator/hooks.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/accelerator/hooks.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/accelerator/hooks.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/accelerator/hooks.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/accelerator/hooks.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/accelerator/hooks.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/accelerator/hooks.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/accelerator/hooks.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/accelerator/hooks.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/accelerator/hooks.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/accelerator/hooks.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/accelerator/hooks.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/accelerator/hooks.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/accelerator/hooks.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/accelerator/hooks.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/accelerator/hooks.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/accelerator/hooks.html)

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

Accelerator Hooks[#](https://docs.pytorch.org/docs/2.15/accelerator/hooks.html#accelerator-hooks "Link to this heading")

=========================================================================================================================

Created On: Nov 13, 2025 | Last Updated On: Dec 09, 2025

Background[#](https://docs.pytorch.org/docs/2.15/accelerator/hooks.html#background "Link to this heading")

-----------------------------------------------------------------------------------------------------------

Accelerator hooks are the mechanism for integrating custom accelerator devices into PyTorch’s runtime.

Design[#](https://docs.pytorch.org/docs/2.15/accelerator/hooks.html#design "Link to this heading")

---------------------------------------------------------------------------------------------------

The tables below list the hooks accelerator vendors should implement when integrating a new device backend. These hooks are categorized into two priority levels:

*   **High‑priority hooks**: Core APIs that the PyTorch runtime directly depends on. Vendors should implement all high‑priority hooks to ensure core compatibility and basic device functionality.
    
*   **Low‑priority hooks**: Device‑management and utility APIs that PyTorch does not directly depend on. These hooks enhance user experience and multi‑device support and are optional. Vendors can implement them based on specific requirements and use cases.
    

### High‑priority hooks[#](https://docs.pytorch.org/docs/2.15/accelerator/hooks.html#highpriority-hooks "Link to this heading")

| Hook method | Description | Application scenarios |
| --- | --- | --- |
| `init()` | Initializes the accelerator runtime and device contexts | Set up necessary state when PyTorch first accesses the device |
| `hasPrimaryContext(DeviceIndex)` | Checks if a primary context exists for the device | Determine whether device initialization has occurred |
| `getDefaultGenerator(DeviceIndex)` | Returns the default random number generator for a device | Access the device’s primary RNG for reproducible random operations |
| `getNewGenerator(DeviceIndex)` | Creates a new independent random number generator | Create isolated RNG instances for parallel operations |
| `getDeviceFromPtr(void*)` | Determines which device a memory pointer belongs to | Identify the accelerator device associated with a memory allocation |
| `getPinnedMemoryAllocator()` | Returns an allocator for pinned (page-locked) host memory | Allocate host memory that can be efficiently transferred to/from the accelerator |
| `isPinnedPtr(void*)` | Checks if a pointer points to pinned memory | Validate memory types before performing operations |

### Low‑priority hooks[#](https://docs.pytorch.org/docs/2.15/accelerator/hooks.html#lowpriority-hooks "Link to this heading")

| Hook method | Description | Application scenarios |
| --- | --- | --- |
| `isBuilt()` | Returns whether the accelerator backend is built/compiled into the extension | Check whether the accelerator library is available at compile time |
| `isAvailable()` | Returns whether the accelerator hardware is available at runtime | Verify whether accelerator devices can be detected and initialized |
| `deviceCount()` | Returns the number of available accelerator devices | Enumerate all available accelerator devices for device selection |
| `setCurrentDevice(DeviceIndex)` | Sets the active device for the current thread | Switch the current thread’s context to a specific accelerator device |
| `getCurrentDevice()` | Returns the currently active device index | Query which accelerator device is active in the current thread |
| `exchangeDevice(DeviceIndex)` | Atomically exchanges the current device and returns the previous one | Temporarily switch devices and restore the previous device afterward |
| `maybeExchangeDevice(DeviceIndex)` | Conditionally exchanges device only if the index is valid | Safely attempt device switching with validation |

Implementation[#](https://docs.pytorch.org/docs/2.15/accelerator/hooks.html#implementation "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

For illustration, OpenReg (Open Registration) is a PyTorch integration example that fills the gap for out‑of‑tree accelerator backend integration. It demonstrates how vendors can register custom device backends—without modifying PyTorch core—by implementing the hooks interface (see [`at::PrivateUse1HooksInterface`](https://github.com/pytorch/pytorch/tree/main/aten/src/ATen/detail/PrivateUse1HooksInterface.h#L15-L72 "PrivateUse1HooksInterface.h")
).

We use `getDefaultGenerator` as an example:

1  const at::Generator& getDefaultGenerator(DeviceIndex device\_index) const override {
2    return getDefaultOpenRegGenerator(device\_index);
3  }

Copy to clipboard

In this implementation:

1.  **Override the base interface**: The `getDefaultGenerator` method overrides the virtual method from [`at::PrivateUse1HooksInterface`](https://github.com/pytorch/pytorch/tree/main/aten/src/ATen/detail/PrivateUse1HooksInterface.h#L15-L72 "PrivateUse1HooksInterface.h")
    .
    
2.  **Delegate to the device‑specific implementation**: Call `getDefaultOpenRegGenerator(device_index)`, which manages a per‑device generator instance.
    
3.  **Return a device‑specific generator**: The returned `at::Generator` wraps an `OpenRegGeneratorImpl` that implements device‑specific random number generation.
    

This pattern applies to all hooks: override the interface method, validate inputs, delegate to your device‑specific API, and return results in PyTorch’s expected format.

Integration Example[#](https://docs.pytorch.org/docs/2.15/accelerator/hooks.html#integration-example "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

The following sections demonstrate how PyTorch integrates with accelerator hooks when accessing the default random number generator. The example traces the complete flow from user-facing Python code down to the device-specific implementation.

### Layer 1: User Code[#](https://docs.pytorch.org/docs/2.15/accelerator/hooks.html#layer-1-user-code "Link to this heading")

User code sets a deterministic seed by calling `manual_seed`:

import torch
torch.openreg.manual\_seed(42)

Copy to clipboard

### Layer 2: Extension Python API[#](https://docs.pytorch.org/docs/2.15/accelerator/hooks.html#layer-2-extension-python-api "Link to this heading")

The Python API layer manages device selection and calls into the C++ extension (defined in [`torch_openreg/openreg/random.py`](https://github.com/pytorch/pytorch/tree/main/test/cpp_extensions/open_registration_extension/torch_openreg/torch_openreg/openreg/random.py#L48-L53 "random.py")
):

1def manual\_seed(seed: int) \-> None:
2    seed \= int(seed)
3
4    idx \= current\_device()
5    default\_generator \= torch\_openreg.\_C.\_get\_default\_generator(idx)
6    default\_generator.manual\_seed(seed)
7
8

Copy to clipboard

The `manual_seed` function obtains the current device index, calls `torch_openreg._C._get_default_generator(idx)` to get the device‑specific generator, and sets its seed.

### Layer 3: Python/C++ Bridge[#](https://docs.pytorch.org/docs/2.15/accelerator/hooks.html#layer-3-python-c-bridge "Link to this heading")

The C++ extension exposes `_getDefaultGenerator` to Python, which bridges into PyTorch core:

 1static PyObject\* \_getDefaultGenerator(PyObject\* self, PyObject\* arg) {
 2  HANDLE\_TH\_ERRORS
 3  TORCH\_CHECK(
 4      THPUtils\_checkLong(arg),
 5      "\_get\_default\_generator expects an int, but got ",
 6      THPUtils\_typename(arg));
 7  auto idx \= static\_cast<int\>(THPUtils\_unpackLong(arg));
 8
 9  torch::utils::register\_fork\_handler\_for\_device\_init(at::kPrivateUse1);
10  return THPGenerator\_initDefaultGenerator(
11      at::globalContext().defaultGenerator(
12          c10::Device(c10::DeviceType::PrivateUse1, idx)));
13
14  END\_HANDLE\_TH\_ERRORS
15}

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

This function unpacks the device index from Python, creates a `PrivateUse1` device object, and calls `at::globalContext().defaultGenerator()`. PyTorch’s context then dispatches to the registered hooks.

### Layer 4: PyTorch Core Context[#](https://docs.pytorch.org/docs/2.15/accelerator/hooks.html#layer-4-pytorch-core-context "Link to this heading")

PyTorch’s `Context` class dispatches to the appropriate accelerator hooks ([`aten/src/ATen/Context.h`](https://github.com/pytorch/pytorch/tree/main/aten/src/ATen/Context.h#L61-L102 "Context.h")
):

 1  TF32,
 2  BF16,
 3  DEFAULT,
 4  BF16X9
 5};
 6
 7enum class TORCH\_API CuDNNDepthwiseKernel { AUTO, CUDNN, NATIVE };
 8 9TORCH\_API Float32Backend str2backend(const std::string& name);
10TORCH\_API Float32Op str2op(const std::string& name);
11TORCH\_API Float32Precision str2precision(const std::string& name);
12TORCH\_API std::string precision2str(Float32Precision prec);
13TORCH\_API CuDNNDepthwiseKernel str2cudnn\_depthwise(const std::string& name);
14TORCH\_API std::string cudnn\_depthwise2str(CuDNNDepthwiseKernel k);
15
16class TORCH\_API Context {
17 public:
18  Context();
19
20  const Generator& defaultGenerator(Device device) {
21    c10::DeviceType device\_type \= device.type();
22    lazyInitDevice(device\_type);
23
24    if (device\_type \== at::kCPU) {
25      return at::detail::getDefaultCPUGenerator();
26    } else {
27      return getAcceleratorHooksInterface(device\_type)
28          .getDefaultGenerator(device.index());
29    }
30  }
31
32  const AcceleratorHooksInterface& getAcceleratorHooksInterface(
33      std::optional<c10::DeviceType\> opt\_device\_type \= std::nullopt) {
34    if (!opt\_device\_type.has\_value()) {
35      opt\_device\_type \= at::getAccelerator(true);
36    }
37    if (opt\_device\_type \== at::kCUDA) {
38      return at::detail::getCUDAHooks();
39    } else if (opt\_device\_type \== at::kXPU) {
40      return at::detail::getXPUHooks();
41    } else if (opt\_device\_type \== at::kMPS) {
42      return at::detail::getMPSHooks();
43    } else if (opt\_device\_type \== at::kPrivateUse1) {
44      return at::detail::getPrivateUse1Hooks();

Copy to clipboard

This layered architecture keeps PyTorch device‑agnostic while delegating hardware‑specific operations to accelerator implementations. Hooks are registered once at module load time:

1namespace c10::openreg {
2
3static bool register\_hook\_flag \[\[maybe\_unused\]\] \= \[\]() {
4  at::RegisterPrivateUse1HooksInterface(new OpenRegHooksInterface());
5
6  return true;
7}();
8
9} // namespace c10::openreg

Copy to clipboard

### Layer 5: Accelerator Hooks[#](https://docs.pytorch.org/docs/2.15/accelerator/hooks.html#layer-5-accelerator-hooks "Link to this heading")

The hooks interface provides the abstraction PyTorch uses to delegate to device‑specific implementations:

1  const at::Generator& getDefaultGenerator(DeviceIndex device\_index) const override {
2    return getDefaultOpenRegGenerator(device\_index);
3  }

Copy to clipboard

The `getDefaultGenerator` hook method overrides the base interface and delegates to `getDefaultOpenRegGenerator`, which manages the actual generator instances.

### Layer 6: Device-Specific Implementation[#](https://docs.pytorch.org/docs/2.15/accelerator/hooks.html#layer-6-device-specific-implementation "Link to this heading")

The device‑specific implementation manages per‑device generator instances:

 1const at::Generator& getDefaultOpenRegGenerator(c10::DeviceIndex device\_index) {
 2  static bool flag \[\[maybe\_unused\]\] \= \[\]() {
 3    auto deivce\_nums \= device\_count();
 4    default\_generators.resize(deivce\_nums);
 5    for (auto i \= 0; i < deivce\_nums; i++) {
 6      default\_generators\[i\] \= at::make\_generator<OpenRegGeneratorImpl\>(i);
 7      default\_generators\[i\].seed();
 8    }
 9    return true;
10  }();
11
12  c10::DeviceIndex idx \= device\_index;
13  if (idx \== \-1) {
14    idx \= current\_device();
15  } else {
16    TORCH\_CHECK(idx \>= 0 && idx < device\_count());
17  }
18  return default\_generators\[idx\];
19}

Copy to clipboard

This function maintains a static vector of generators (one per device), initializes them on first access, validates the device index, and returns the appropriate generator instance.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/accelerator/hooks.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/accelerator/hooks.md.txt)

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