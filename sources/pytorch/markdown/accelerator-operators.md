Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/accelerator/operators.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/accelerator/operators.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/accelerator/operators.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/accelerator/operators.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/accelerator/operators.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/accelerator/operators.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/accelerator/operators.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/accelerator/operators.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/accelerator/operators.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/accelerator/operators.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/accelerator/operators.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/accelerator/operators.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/accelerator/operators.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/accelerator/operators.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/accelerator/operators.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/accelerator/operators.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/accelerator/operators.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/accelerator/operators.html)
[v1.13](https://docs.pytorch.org/docs/1.13/accelerator/operators.html)
[v1.12](https://docs.pytorch.org/docs/1.12/accelerator/operators.html)
[v1.11](https://docs.pytorch.org/docs/1.11/accelerator/operators.html)
[v1.10](https://docs.pytorch.org/docs/1.10/accelerator/operators.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/accelerator/operators.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/accelerator/operators.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/accelerator/operators.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/accelerator/operators.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/accelerator/operators.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/accelerator/operators.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/accelerator/operators.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/accelerator/operators.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/accelerator/operators.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/accelerator/operators.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/accelerator/operators.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/accelerator/operators.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/accelerator/operators.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/accelerator/operators.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/accelerator/operators.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/accelerator/operators.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/accelerator/operators.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/accelerator/operators.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/accelerator/operators.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/accelerator/operators.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/accelerator/operators.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/accelerator/operators.html)

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

Operator Registration[#](https://docs.pytorch.org/docs/2.15/accelerator/operators.html#operator-registration "Link to this heading")

=====================================================================================================================================

Created On: Aug 27, 2025 | Last Updated On: Oct 24, 2025

For new accelerators, one of the most important and fundamental aspects of integration is supporting high-performance operators. To facilitate operator adaptation for users and accelerator developers, PyTorch provides multiple methods for developing and registering operators in both `Python` and `C++`. The following sections detail some of PyTorch’s fundamental capabilities for operator registration.

Note

`Dispatch Key` is used to uniquely identify accelerator within PyTorch, such as `CPU`, `CUDA`, `MPS`, and `PrivateUse1`. In theory, all subsequent new accelerators will share `PrivateUse1`, leveraging its built-in comprehensive scaffolding capabilities to complete the integration of new accelerators. Please refer to [Let’s talk about the PyTorch dispatcher](https://blog.ezyang.com/2020/09/lets-talk-about-the-pytorch-dispatcher/)
 if you are interested with dispatcher.

Operator Set[#](https://docs.pytorch.org/docs/2.15/accelerator/operators.html#operator-set "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

PyTorch currently has over 3500 built-in operators (including related operator variants). This represents a significant workload from any perspective, and supporting this massive number of operators in a short period of time is no easy task. Therefore, as the first step in developing new backend operators, our goal should be to focus on the essential operators. For other operators, we can first use the community’s fallback mechanism to support the feature as the first priority. After that, we can gradually complete other operators to improve the performance of the new backend.

The required operator set is listed below, primarily consisting of low-level operators required by factory functions and fallback operators:

| Operator Name | Dispatch Key | Description |
| --- | --- | --- |
| empty.memory\_format | PrivateUse1 | Create an uninitialized Tensor with the specified shape and memory layout (the stride is automatically calculated) |
| empty\_strided | PrivateUse1 | Create an uninitialized Tensor of the specified shape and stride (more degrees of freedom) |
| as\_strided | PrivateUse1 | Create a shared view of the input Tensor with new shape, stride, and offset (without allocating new memory) |
| view | PrivateUse1 | Create a shared view of the input Tensor with new shape, but the original Tensor must be memory-contiguous |
| \_reshape\_alias | PrivateUse1 | Creates a shared view without safety checks(Internal version of reshape) |
| resize\_ | PrivateUse1 | Modify the shape of the Tensor in place and reallocate memory if capacity is insufficient |
| \_copy\_from | PrivateUse1 | The underlying core function of Tensor.copy\_ is responsible for the actual cross-device data copying |
| \_copy\_from\_and\_resize | PrivateUse1 | Combine `resize_` and `_copy_from` to resize first and then copy |
| \_local\_scalar\_dense | PrivateUse1 | The underlying implementation of `.item()`, extracting values from Tensor to CPU scalars |
| set\_.source\_Tensor | PrivateUse1 | Set the current Tensor using the specified Tensor |
| set\_.source\_Storage | PrivateUse1 | Set the current Tensor using the specified Storage |
| set\_.source\_Storage\_storage\_offset | PrivateUse1 | Set the current Tensor using the specified Storage with the storage offset |
| fallback | PrivateUse1 | Fallback to CPU |

Basics[#](https://docs.pytorch.org/docs/2.15/accelerator/operators.html#basics "Link to this heading")

-------------------------------------------------------------------------------------------------------

Now that we have defined the initial scope of operator support, we can begin developing operator adaptations. This section will explain these implementations in `Python` and `C++` based on actual scenarios.

### Step 1[#](https://docs.pytorch.org/docs/2.15/accelerator/operators.html#step-1 "Link to this heading")

[The operators mentioned above](https://docs.pytorch.org/docs/2.15/accelerator/operators.html#operator-set)
 share a common characteristic: They are built-in PyTorch operators with defined `namespaces` and `Schemas`, and these operators’ built-in accelerators (`CPU`, `CUDA`, etc.) have been implemented. What we have to do next is to implement these operators for the new accelerators.

 C++

 1at::Tensor empty\_memory\_format(
 2    c10::IntArrayRef size,
 3    std::optional<c10::ScalarType\> dtype\_opt,
 4    std::optional<c10::Layout\> layout\_opt,
 5    std::optional<c10::Device\> device\_opt,
 6    std::optional<bool\> pin\_memory\_opt,
 7    std::optional<c10::MemoryFormat\> memory\_format\_opt) {
 8  const auto device \= c10::device\_or\_default(device\_opt);
 9  const auto dtype \= c10::dtype\_or\_default(dtype\_opt);
10  TORCH\_CHECK(device.is\_privateuseone());
11  TORCH\_CHECK(
12      c10::layout\_or\_default(layout\_opt) \== c10::Layout::Strided,
13      "Non strided layout not supported");
14  TORCH\_CHECK(
15      !c10::pinned\_memory\_or\_default(pin\_memory\_opt),
16      "Pin memory can only be on CPU");
17  const c10::DeviceGuard device\_guard(device);
18  constexpr c10::DispatchKeySet pu1\_dks(c10::DispatchKey::PrivateUse1);
19  auto allocator \= at::GetAllocator(at::kPrivateUse1);
20  return at::detail::empty\_generic(
21      size, allocator, pu1\_dks, dtype, memory\_format\_opt);
22}

Copy to clipboard

 1at::Tensor wrapper\_empty\_memory\_format(
 2    c10::IntArrayRef size,
 3    std::optional<c10::ScalarType\> dtype\_opt,
 4    std::optional<c10::Layout\> layout\_opt,
 5    std::optional<c10::Device\> device\_opt,
 6    std::optional<bool\> pin\_memory\_opt,
 7    std::optional<c10::MemoryFormat\> memory\_format\_opt) {
 8  return at::native::openreg::empty\_memory\_format(
 9      size,
10      dtype\_opt,
11      layout\_opt,
12      device\_opt,
13      pin\_memory\_opt,
14      memory\_format\_opt);
15}

Copy to clipboard

Taking the `empty.memory_format` operator as an example, we first need to query the operator’s `schema` information in `native_functions.yaml`, which contains detailed signature information. Then, we can implement the operator based on the capabilities of the new accelerator.

\- func: empty.memory\_format(SymInt\[\] size, \*, ScalarType? dtype=None, Layout? layout=None, Device? device=None, bool? pin\_memory=None, MemoryFormat? memory\_format=None) -> Tensor
dispatch:
    CPU: empty\_cpu
    CUDA: empty\_cuda
    ...

Copy to clipboard

 C++

 1TORCH\_LIBRARY\_IMPL(aten, PrivateUse1, m) { 2  m.impl("empty.memory\_format", wrapper\_empty\_memory\_format); 3  m.impl("empty\_strided", wrapper\_empty\_strided);
 4  m.impl("as\_strided", wrapper\_as\_strided);
 5  m.impl("resize\_", wrapper\_resize\_);
 6  m.impl("\_reshape\_alias", wrapper\_\_reshape\_alias);
 7  m.impl("\_copy\_from", wrapper\_\_copy\_from);
 8  m.impl("\_copy\_from\_and\_resize", wrapper\_\_copy\_from\_and\_resize);
 9  m.impl("\_local\_scalar\_dense", wrapper\_\_local\_scalar\_densor);
10  m.impl(
11      "\_has\_compatible\_shallow\_copy\_type",
12      wrapper\_has\_compatible\_shallow\_copy\_type);
13  m.impl("set\_.source\_Tensor", wrapper\_set\_source\_Tensor\_);
14  m.impl("set\_.source\_Storage", wrapper\_set\_source\_Storage\_);
15  m.impl(
16      "set\_.source\_Storage\_storage\_offset",
17      wrapper\_set\_source\_Storage\_storage\_offsetset\_);
18  m.impl("view", wrapper\_view);
19}

Copy to clipboard

After completing the `wrapper_empty_memory_format`, we can register `aten::empty.memory_format` for `PrivateUse1` through `TORCH_LIBRARY_IMPL`.

### Step 2[#](https://docs.pytorch.org/docs/2.15/accelerator/operators.html#step-2 "Link to this heading")

By following [Step 1](https://docs.pytorch.org/docs/2.15/accelerator/operators.html#step-one)
, we can complete the development and registration of all operators except `fallback`. Next, to support operators related to operations (such as mathematical operations and convolution operations), we need to implement the registration of fallback semantics. This is a built-in capability provided by the PyTorch framework that can fallback some operations that are not supported by new accelerators to the CPU for execution. For new backends in development, this is an extremely effective way to ensure functionality at the expense of performance.

 C++

 1void cpu\_fallback(const c10::OperatorHandle& op, torch::jit::Stack\* stack) {
 2  static const std::unordered\_set<c10::OperatorName\> cpu\_fallback\_blocklist \= {
 3      c10::OperatorName("aten::abs", ""),
 4      c10::OperatorName("aten::abs", "out"),
 5  };
 6
 7  const auto& op\_name \= op.schema().operator\_name();
 8  if (cpu\_fallback\_blocklist.count(op\_name)) {
 9    TORCH\_CHECK(
10        false,
11        "Operator '",
12        op\_name,
13        "' is not implemented for device openreg.");
14  } else {
15    at::native::cpu\_fallback(op, stack);
16  }
17}

Copy to clipboard

1void wrapper\_cpu\_fallback(
2    const c10::OperatorHandle& op,
3    torch::jit::Stack\* stack) {
4  at::native::openreg::cpu\_fallback(op, stack);
5}

Copy to clipboard

1TORCH\_LIBRARY\_IMPL(\_, PrivateUse1, m) {
2  m.fallback(
3      torch::CppFunction::makeFromBoxedFunction<&wrapper\_cpu\_fallback\>());
4}

Copy to clipboard

`wrapper_cpu_fallback` wraps the `at::native::cpu_fallback` method provided by PyTorch and is registered with `PrivateUse1` in PyTorch via `TORCH_LIBRARY_IMPL`. Subsequent operations not supported by the new backend will automatically fall back to the CPU for execution, and the results will be passed back to the new backend after execution.

Advanced[#](https://docs.pytorch.org/docs/2.15/accelerator/operators.html#advanced "Link to this heading")

-----------------------------------------------------------------------------------------------------------

### Selective Fallback[#](https://docs.pytorch.org/docs/2.15/accelerator/operators.html#selective-fallback "Link to this heading")

Enabling the fallback mechanism only for certain operators, while following PyTorch’s default behavior for other operators (an error will be reported if the accelerator does not have a corresponding operator implementation), this is a very reasonable scenario as well.

 C++

1void wrapper\_cpu\_fallback(
2    const c10::OperatorHandle& op,
3    torch::jit::Stack\* stack) {
4  at::native::openreg::cpu\_fallback(op, stack);
5}

Copy to clipboard

1TORCH\_LIBRARY\_IMPL(aten, PrivateUse1, m) {
2  m.impl(
3      "sub.Tensor",
4      torch::CppFunction::makeFromBoxedFunction<&wrapper\_cpu\_fallback\>());
5}

Copy to clipboard

Per-operator fallbacks are very similar to global fallbacks, the only difference being the registration method: calling `m.impl` registers an implementation for a specific operator, while `m.fallback` registers a default implementation for all operators.

 C++

 1void cpu\_fallback(const c10::OperatorHandle& op, torch::jit::Stack\* stack) {
 2  static const std::unordered\_set<c10::OperatorName\> cpu\_fallback\_blocklist \= { 3      c10::OperatorName("aten::abs", ""), 4      c10::OperatorName("aten::abs", "out"), 5  }; 6
 7  const auto& op\_name \= op.schema().operator\_name();
 8  if (cpu\_fallback\_blocklist.count(op\_name)) {
 9    TORCH\_CHECK(
10        false,
11        "Operator '",
12        op\_name,
13        "' is not implemented for device openreg.");
14  } else {
15    at::native::cpu\_fallback(op, stack);
16  }
17}

Copy to clipboard

Of course, global fallbacks can also be combined with a blacklist of fallbacks, which is a common approach, especially when only a few operators do not support fallbacks.

### PyTorch STUB[#](https://docs.pytorch.org/docs/2.15/accelerator/operators.html#pytorch-stub "Link to this heading")

PyTorch also provides another approach for built-in operators: `STUB`. This method is essentially based on the [Step 1](https://docs.pytorch.org/docs/2.15/accelerator/operators.html#step-one)
 approach, but adds secondary scheduling capabilities (for example, scheduling based on CPU characteristics).

Note

The `STUB` method currently supports only a limited set of operators. For new accelerator devices, the advantage of the `STUB` method is that it significantly reduces the cost of development at the cost of a small performance overhead. PyTorch currently does not clearly list the set of operators that can be registered through `STUB`. Due to the large number of related operators, only the query method for the supported operator list is provided here.

pushd ${TORCH\_ROOT}

find aten \-type f \-a \-name "\*.h" | xargs \-I {} grep \-wl "^DECLARE\_DISPATCH" {}

popd

Copy to clipboard

`DECLARE_DISPATCH` is a macro used to explicitly declare `STUB`. It is currently distributed in the `aten` directory. Based on this macro, you can find all operators that can be integrated using the `STUB` method.

...
aten/src/ATen/native/Activation.h
aten/src/ATen/native/FusedSGD.h
aten/src/ATen/native/nested/NestedTensorBinaryOps.h
aten/src/ATen/native/TensorCompare.h
aten/src/ATen/native/Sorting.h
...

Copy to clipboard

using unary\_fn \= void(\*)(TensorIteratorBase&);

DECLARE\_DISPATCH(unary\_fn, abs\_stub)

Copy to clipboard

The above listing contains the file that declares the `STUB` operator, where you can clearly see the STUB name and the associated function signature. Next, we will take `abs_stub` as an example to briefly introduce the path to support operators through `STUB`.

 C++

 1void abs\_kernel(at::TensorIteratorBase& iter) {
 2  TORCH\_CHECK(iter.ntensors() \== 2, "Abs kernel expects 2 tensors");
 3  TORCH\_CHECK(
 4      iter.common\_dtype() \== at::ScalarType::Float,
 5      "Abs kernel only supports float type");
 6
 7  auto& output\_tensor \= iter.tensor(0);
 8  auto& input\_tensor \= iter.tensor(1);
 9
10  TORCH\_CHECK(
11      input\_tensor.sizes() \== output\_tensor.sizes(),
12      "Input and output tensor sizes must match.");
13
14  auto abs\_loop \= \[\](float\* out\_ptr, const float\* in\_ptr, int64\_t n) {
15    for (int64\_t i \= 0; i < n; ++i) {
16      out\_ptr\[i\] \= std::abs(in\_ptr\[i\]);
17    }
18  };
19
20  MemoryGuard guard(input\_tensor, output\_tensor);
21
22  if (iter.is\_contiguous()) {
23    abs\_loop(
24        static\_cast<float\*>(iter.data\_ptr(0)),
25        static\_cast<float\*>(iter.data\_ptr(1)),
26        iter.numel());
27  } else {
28    TORCH\_CHECK(
29        input\_tensor.is\_contiguous(), "Input tensor must be contiguous.")
30
31    auto output \= at::empty(
32        input\_tensor.sizes(),
33        input\_tensor.options().memory\_format(
34            input\_tensor.suggest\_memory\_format()));
35
36    MemoryGuard guard(output);
37
38    abs\_loop(
39        static\_cast<float\*>(output.data\_ptr()),
40        static\_cast<float\*>(iter.data\_ptr(1)),
41        iter.numel());
42
43    output\_tensor.copy\_(output);
44  }
45}

Copy to clipboard

1REGISTER\_PRIVATEUSE1\_DISPATCH(abs\_stub, &wrapper\_abs\_stub);
2REGISTER\_PRIVATEUSE1\_DISPATCH(
3    quantize\_tensor\_per\_tensor\_affine\_stub,
4    &wrapper\_quantize\_tensor\_per\_tensor\_affine\_stub);
5REGISTER\_PRIVATEUSE1\_DISPATCH(
6    \_fused\_sdp\_choice\_stub,
7    &wrapper\_\_fused\_sdp\_choice);

Copy to clipboard

From the signature, we can see that the input of `abs_stub` is `TensorIteratorBase`, a powerful helper class provided by PyTorch that contains all input and output operators, as well as some other auxiliary methods. Based on it, we can develop the `abs_kernel` operator and then call `REGISTER_PRIVATEUSE1_DISPATCH` to specify `abs_stub` to complete the registration.

### Custom Operators[#](https://docs.pytorch.org/docs/2.15/accelerator/operators.html#custom-operators "Link to this heading")

In addition to PyTorch’s built-in operators, custom accelerator operators are also very common to improve performance in specific scenarios. These can be categorized into three main approaches:

*   Forward-only
    
*   Forward and backward: Separate registration
    
*   Forward and backward: Implemented using `torch.autograd.Function`
    

Note

There are more details in PyTorch tutorials, so refer to [PyTorch Custom Operators](https://docs.pytorch.org/tutorials/advanced/custom_ops_landing_page.html)
 if you are interested.

#### Forward Only[#](https://docs.pytorch.org/docs/2.15/accelerator/operators.html#forward-only "Link to this heading")

Here, we’ll briefly introduce the implementation process of custom operators, focusing on the forward-only approach. The implementation can be summarized into the following three points:

1.  **Define Schema:**
    
     C++
    
    1TORCH\_LIBRARY(openreg, m) {
    2  m.def("custom\_abs(Tensor input)-> Tensor");
    3}
    
    Copy to clipboard
    
    *   Namespace Name: `openreg`
        
    *   Function Name: `custom_abs`
        
    *   Input Parameters:
        
        *   Type: `Tensor`
            
        *   Name: `input`
            
    *   Output Type: `Tensor`
        
2.  **Register Operator**
    
     C++
    
    1TORCH\_LIBRARY\_IMPL(openreg, PrivateUse1, m) {
    2  m.impl("custom\_abs", &wrapper\_custom\_abs);
    3}
    
    Copy to clipboard
    
    Use `TORCH_LIBRARY_IMPL` to register the `wrapper_custom_abs` implementation for the `custom_abs` operator in `PrivateUse1`. Because `Autograd` is always enabled in PyTorch, PyTorch defaults to finding and executing the corresponding backward implementation even if only forward computation is required(will fallthrough in backward implementation). Fortunately, PyTorch have implemented a general `Autograd Fallback` for PrivateUse1 as well, if only forward computation is involved, it is equivalent to a fallthrough operation, selecting the next DispatchKey for computation; if backward computation is involved, an error is thrown.
    
3.  **Register Metadata(optional, but required by the graph mode, etc.):**
    
     PYTHON
    
    1lib \= torch.library.Library("openreg", "IMPL", "Meta")  \# noqa: SCOPED\_LIBRARY
    2
    3
    4@torch.library.impl(lib, "custom\_abs")
    5def custom\_abs(self):
    6    return torch.empty\_like(self)
    7
    8
    
    Copy to clipboard
    
    PyTorch supports registering `Meta` in both C++ and Python. Since Python registration is simpler, Python is used as an example here. Similar to the `TORCH_LIBRARY_IMPL` function in C++, Python provides the more user-friendly `torch.library.impl` decorator.
    

Tools[#](https://docs.pytorch.org/docs/2.15/accelerator/operators.html#tools "Link to this heading")

-----------------------------------------------------------------------------------------------------

Operator registration in PyTorch is complex, with diverse registration methods and numerous scenarios. Therefore, the PyTorch community has provided a number of tools to help developers quickly understand the underlying principles and assist in troubleshooting. Here we briefly introduce several commonly used tools:

### Commands[#](https://docs.pytorch.org/docs/2.15/accelerator/operators.html#commands "Link to this heading")

PyTorch provides a set of commands prefixed with `torch._C._dispatch_` around its Dispatch feature. You can query all related interfaces using the following command:

python \-c 'import torch; print("\\n".join(\[x for x in dir(torch.\_C) if x.startswith("\_dispatch\_")\]))'

...
\_dispatch\_dump
\_dispatch\_dump\_table
\_dispatch\_has\_kernel
\_dispatch\_has\_kernel\_for\_any\_dispatch\_key
\_dispatch\_has\_kernel\_for\_dispatch\_key
\_dispatch\_isTensorSubclassLike
\_dispatch\_is\_alias\_key
\_dispatch\_is\_included\_in\_alias
\_dispatch\_is\_main\_interpreter
\_dispatch\_kernel\_for\_dispatch\_key\_is\_fallthrough
\_dispatch\_key\_for\_device
\_dispatch\_key\_name
\_dispatch\_key\_parse
\_dispatch\_key\_set
...

Copy to clipboard

Here are explanations for several commonly used commands:

*   `torch._C._dispatch_key_set`:
    
    Displays the DispatchKey of the current Tensor, with priority increasing from left to right.
    
    \>>> import torch
    \>>> a \= torch.randn(3,3,device\="cuda")
    \>>> torch.\_C.\_dispatch\_key\_set(a)
    'DispatchKeySet(CUDA, ADInplaceOrView, AutogradCUDA, AutocastCUDA)'
    
    Copy to clipboard
    
*   `torch._C._dispatch_dump_table`:
    
    Queries the support status of a given operator across different Dispatch Keys, making it easy to locate the corresponding implementation code.
    
    \>>> import torch
    \>>> print(torch.\_C.\_dispatch\_dump\_table("aten::add.Tensor"))
    \>>> ...
        CPU: registered at ./build/aten/src/ATen/RegisterCPU\_0.cpp:1309 \[kernel\]
        CUDA: registered at ./build/aten/src/ATen/RegisterCUDA\_0.cpp:2420 \[kernel\]
        HIP: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional\_0.cpp:1373 \[default backend kernel\]
        MPS: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional\_0.cpp:1373 \[default backend kernel\]
        IPU: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional\_0.cpp:1373 \[default backend kernel\]
        XPU: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional\_0.cpp:1373 \[default backend kernel\]
        HPU: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional\_0.cpp:1373 \[default backend kernel\]
        VE: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional\_0.cpp:1373 \[default backend kernel\]
        MTIA: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional\_0.cpp:1373 \[default backend kernel\]
        MAIA: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional\_0.cpp:1373 \[default backend kernel\]
        PrivateUse1: registered at ./build/aten/src/ATen/RegisterCompositeExplicitAutogradNonFunctional\_0.cpp:1373 \[default backend kernel\]
        ...
    
    Copy to clipboard
    
    You can easily query the corresponding implementation of the `aten::add.Tensor` operator on other platforms, so that you can track the entire operator calling process from the source code level.
    

### Environment Variables[#](https://docs.pytorch.org/docs/2.15/accelerator/operators.html#environment-variables "Link to this heading")

PyTorch also provides some dispatcher-related environment variables that can help with learning and quickly locating issues.

*   TORCH\_SHOW\_DISPATCH\_TRACE
    
    Displays detailed internal dispatch key scheduling during PyTorch execution.
    
    export TORCH\_SHOW\_DISPATCH\_TRACE\=1
    
    Copy to clipboard
    
    \>>> import torch
    \>>> a \= torch.randn(3,3)
     \[call\] op\=\[aten::randn\], key\=\[BackendSelect\]
       \[redispatch\] op\=\[aten::randn\], key\=\[CPU\]
         \[call\] op\=\[aten::empty.memory\_format\], key\=\[BackendSelect\]
           \[redispatch\] op\=\[aten::empty.memory\_format\], key\=\[CPU\]
         \[call\] op\=\[aten::normal\_\], key\=\[CPU\]
    
    Copy to clipboard
    
    You can clearly see all the underlying operators called by Python-level operators within PyTorch: including the operator name, calling hierarchy, and corresponding `Dispatch Key`.
    

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/accelerator/operators.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/accelerator/operators.md.txt)

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