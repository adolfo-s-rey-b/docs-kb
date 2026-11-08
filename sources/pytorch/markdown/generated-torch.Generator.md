Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.Generator.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.Generator.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.Generator.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.Generator.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.Generator.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.Generator.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.Generator.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.Generator.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.Generator.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.Generator.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.Generator.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.Generator.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.Generator.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.Generator.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.Generator.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.Generator.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.Generator.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.Generator.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.Generator.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.Generator.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.Generator.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.Generator.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.Generator.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.Generator.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.Generator.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.Generator.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.Generator.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.Generator.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.Generator.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.Generator.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.Generator.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.Generator.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.Generator.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.Generator.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.Generator.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.Generator.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.Generator.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.Generator.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.Generator.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.Generator.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.Generator.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.Generator.html)

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

Generator[#](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#generator "Link to this heading")

=================================================================================================================

_class_ torch.Generator[#](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "Link to this definition")

clone\_state() → [torch.Generator](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator.clone_state "Link to this definition")

Clones the current state of the generator and returns a new generator pointing to this cloned state. This method is beneficial for preserving a particular state of a generator to restore at a later point.

Returns:

A Generator pointing to the newly cloned state.

Return type:

[torch.Generator](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")

Example

\>>> g\_cuda \= torch.Generator(device\='cuda')
\>>> cloned\_state \= g\_cuda.clone\_state()

Copy to clipboard

device[#](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator.device "Link to this definition")

Generator.device -> device

Gets the current device of the generator.

Example:

\>>> g\_cpu \= torch.Generator()
\>>> g\_cpu.device
device(type='cpu')

Copy to clipboard

get\_state() → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator.get_state "Link to this definition")

Returns the Generator state as a `torch.ByteTensor`.

Returns:

A `torch.ByteTensor` which contains all the necessary bits to restore a Generator to a specific point in time.

Return type:

[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Example:

\>>> g\_cpu \= torch.Generator()
\>>> g\_cpu.get\_state()

Copy to clipboard

graphsafe\_get\_state() → [torch.Generator](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator.graphsafe_get_state "Link to this definition")

Retrieves the current state of the generator in a manner that is safe for graph capture. This method is crucial for ensuring that the generator’s state can be captured in the CUDA graph.

Returns:

A Generator point to the current state of the generator

Return type:

[torch.Generator](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")

Example

\>>> g\_cuda \= torch.Generator(device\='cuda')
\>>> current\_state \= g\_cuda.graphsafe\_get\_state()

Copy to clipboard

graphsafe\_set\_state(_state_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator.graphsafe_set_state "Link to this definition")

Sets the state of the generator to the specified state in a manner that is safe for use in graph capture. This method is crucial for ensuring that the generator’s state can be captured in the CUDA graph.

Parameters:

**state** ([_torch.Generator_](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")
) – A Generator point to the new state for the generator, typically obtained from graphsafe\_get\_state.

Example

\>>> g\_cuda \= torch.Generator(device\='cuda')
\>>> g\_cuda\_other \= torch.Generator(device\='cuda')
\>>> current\_state \= g\_cuda\_other.graphsafe\_get\_state()
\>>> g\_cuda.graphsafe\_set\_state(current\_state)

Copy to clipboard

initial\_seed() → [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator.initial_seed "Link to this definition")

Returns the initial seed for generating random numbers.

Example:

\>>> g\_cpu \= torch.Generator()
\>>> g\_cpu.initial\_seed()
2147483647

Copy to clipboard

manual\_seed(_seed_) → [Generator](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator.manual_seed "Link to this definition")

Sets the seed for generating random numbers. Returns a torch.Generator object. Any 32-bit integer is a valid seed.

Parameters:

**seed** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
) – The desired seed. Value must be within the inclusive range \[-0x8000\_0000\_0000\_0000, 0xffff\_ffff\_ffff\_ffff\]. Otherwise, a RuntimeError is raised. Negative inputs are remapped to positive values with the formula 0xffff\_ffff\_ffff\_ffff + seed.

Returns:

An torch.Generator object.

Return type:

[Generator](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")

Example:

\>>> g\_cpu \= torch.Generator()
\>>> g\_cpu.manual\_seed(2147483647)

Copy to clipboard

philox\_state(_increment_) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\][#](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator.philox_state "Link to this definition")

Reserves `increment` values from this generator’s Philox4x32-10 stream and returns the reserved position as `(seed, offset, intragraph_offset)`, three 1-element `int64` tensors. This is the same reservation protocol the built-in CUDA random kernels use (`PhiloxCudaState` in C++), so kernels built on it draw from the same stream as, and compose with, the built-in random operations. Only Philox-based generators (currently CUDA) support this method.

**What the reservation grants.** With `effective_offset = (uint64(offset) + uint64(intragraph_offset)) % 2**64` (both operands reinterpreted back from int64 to uint64 first; see below), the caller owns the Philox counter values `effective_offset / 4` through `effective_offset / 4 + ceil(increment / 4) - 1` (the counter advances once per 4 generated values), at the fixed `seed`, for **every** subsequence. Following the built-in kernels’ convention of one subsequence per thread (`curand_init(seed, subsequence, effective_offset, ...)`, where the counter occupies `counter.x/y` and the subsequence `counter.z/w`), a thread may generate up to `increment` values rounded up to a multiple of 4. The generator’s offset advances by that rounded amount, so `increment` must be at least the number of 32-bit values any single thread of the consuming kernel generates.

**int64 reinterpretation.** Seed and offset are unsigned 64-bit quantities returned bit-exactly in `int64` tensors (PyTorch tensors have no uint64 arithmetic support); values at or above `2**63` appear negative. Kernels should reinterpret the bits back to uint64 (e.g. load as int64 and bitcast); for host-side inspection use `.item() & (2**64 - 1)`. The offset wraps modulo `2**64` on advancement.

**Graph capture.** The two return modes mirror the C++ `PhiloxCudaState` protocol. Outside capture (`HostState`), `seed` and `offset` are CPU tensors holding the current values; `.item()` is cheap and does not synchronize, so callers pass the values as scalar kernel arguments. During capture (`DevState`, under [`torch.accelerator.Graph`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.Graph.html#torch.accelerator.Graph "torch.accelerator.Graph")
 or [`torch.cuda.CUDAGraph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph "torch.cuda.CUDAGraph")
), `seed` and `offset` are CUDA tensors aliasing generator state that each replay refills with the values current at replay time, so kernels must load them from device memory at run time. `intragraph_offset` is always a CPU tensor: 0 outside capture, and this reservation’s position within the graph during capture. Callers branch on capture state (e.g. [`torch.cuda.is_current_stream_capturing()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.is_current_stream_capturing.html#torch.cuda.is_current_stream_capturing "torch.cuda.is_current_stream_capturing")
, or the device of the returned tensors), exactly like the built-in kernels branch on `PhiloxCudaState` via `at::cuda::philox::unpack`.

Warning

Tensors returned during capture alias the capture’s state: their contents are undefined until the first replay and they must not be used after the graph is destroyed.

Parameters:

**increment** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
) – Number of Philox outputs to reserve. Must be non-negative and at most `2**64 - 1`; the offset it advances wraps modulo `2**64` (under graph capture, where the intragraph offset starts at 0, the total reserved within one graph must stay below `2**64`).

Returns:

`(seed, offset, intragraph_offset)`, each a 1-element `int64` tensor. `seed` and `offset` hold the generator’s seed and the reserved stream position as uint64 bits (CPU tensors outside capture, CUDA tensors aliasing generator state during capture); `intragraph_offset` is always a CPU tensor holding this reservation’s position within the capturing graph (0 outside capture).

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

Example

\>>> g\_cuda \= torch.Generator(device\='cuda')
\>>> seed, offset, intragraph \= g\_cuda.philox\_state(4)

Copy to clipboard

seed() → [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator.seed "Link to this definition")

Gets a non-deterministic random number from std::random\_device or the current time and uses it to seed a Generator.

Example:

\>>> g\_cpu \= torch.Generator()
\>>> g\_cpu.seed()
1516516984916

Copy to clipboard

set\_state(_new\_state_) → void[#](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator.set_state "Link to this definition")

Sets the Generator state.

Parameters:

**new\_state** (_torch.ByteTensor_) – The desired state.

Example:

\>>> g\_cpu \= torch.Generator()
\>>> g\_cpu\_other \= torch.Generator()
\>>> g\_cpu.set\_state(g\_cpu\_other.get\_state())

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.Generator.rst.txt)

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