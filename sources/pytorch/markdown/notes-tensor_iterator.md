Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/notes/tensor_iterator.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/notes/tensor_iterator.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/notes/tensor_iterator.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/notes/tensor_iterator.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/notes/tensor_iterator.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/notes/tensor_iterator.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/notes/tensor_iterator.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/notes/tensor_iterator.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/notes/tensor_iterator.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/notes/tensor_iterator.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/notes/tensor_iterator.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/notes/tensor_iterator.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/notes/tensor_iterator.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/notes/tensor_iterator.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/notes/tensor_iterator.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/notes/tensor_iterator.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/notes/tensor_iterator.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/notes/tensor_iterator.html)
[v1.13](https://docs.pytorch.org/docs/1.13/notes/tensor_iterator.html)
[v1.12](https://docs.pytorch.org/docs/1.12/notes/tensor_iterator.html)
[v1.11](https://docs.pytorch.org/docs/1.11/notes/tensor_iterator.html)
[v1.10](https://docs.pytorch.org/docs/1.10/notes/tensor_iterator.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/notes/tensor_iterator.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/notes/tensor_iterator.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/notes/tensor_iterator.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/notes/tensor_iterator.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/notes/tensor_iterator.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/notes/tensor_iterator.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/notes/tensor_iterator.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/notes/tensor_iterator.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/notes/tensor_iterator.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/notes/tensor_iterator.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/notes/tensor_iterator.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/notes/tensor_iterator.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/notes/tensor_iterator.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/notes/tensor_iterator.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/notes/tensor_iterator.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/notes/tensor_iterator.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/notes/tensor_iterator.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/notes/tensor_iterator.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/notes/tensor_iterator.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/notes/tensor_iterator.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/notes/tensor_iterator.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/notes/tensor_iterator.html)

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

TensorIterator (Python)[#](https://docs.pytorch.org/docs/2.15/notes/tensor_iterator.html#tensoriterator-python "Link to this heading")

=======================================================================================================================================

Created On: May 21, 2026 | Last Updated On: May 21, 2026

`torch._tensor_iterator` is a thin Python surface over ATen’s `at::TensorIterator` build pipeline. It is a developer tool: it lets you inspect the result of a TensorIterator build (shape after coalesce/reorder, strides, dtype/device inference, broadcast result) without leaving Python.

There is no `for_each` here – this surface is build-only. Use it to debug shape/dtype inference, validate custom-op contracts, or pattern-match the post-build geometry from a dispatch decision (see `torch._native/ops/scatter_add/cutedsl_impl.py` for an example).

C++ fluent → Python kwargs[#](https://docs.pytorch.org/docs/2.15/notes/tensor_iterator.html#c-fluent-python-kwargs "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

The C++ builder is a fluent `at::TensorIteratorConfig` whose setters return `*this`:

auto iter \= at::TensorIteratorConfig()
    .add\_output(out)
    .add\_const\_input(a)
    .add\_const\_input(b)
    .promote\_inputs\_to\_common\_dtype(true)
    .cast\_common\_dtype\_to\_outputs(true)
    .enforce\_safe\_casting\_to\_output(true)
    .build();

Copy to clipboard

The Python equivalent passes operands and flags as keyword arguments to `TensorIterator(...)`:

from torch.\_tensor\_iterator import TensorIterator

it \= TensorIterator(
    outputs\=\[out\],
    const\_inputs\=\[a, b\],
    promote\_inputs\_to\_common\_dtype\=True,
    cast\_common\_dtype\_to\_outputs\=True,
    enforce\_safe\_casting\_to\_output\=True,
)

Copy to clipboard

The mapping is mechanical:

| C++ setter | Python kwarg | Default |
| --- | --- | --- |
| `add_output(t)` | `outputs=[t, ...]` (or `[None]`) | `[]` |
| `add_input(t)` | `inputs=[t, ...]` | `[]` |
| `add_const_input(t)` | `const_inputs=[t, ...]` | `[]` |
| `check_all_same_dtype(b)` | `check_all_same_dtype=b` | `True` |
| `check_all_same_device(b)` | `check_all_same_device=b` | `True` |
| `promote_inputs_to_common_dtype(b)` | `promote_inputs_to_common_dtype=b` | `False` |
| `promote_integer_inputs_to_float(b)` | `promote_integer_inputs_to_float=b` | `False` |
| `cast_common_dtype_to_outputs(b)` | `cast_common_dtype_to_outputs=b` | `False` |
| `enforce_safe_casting_to_output(b)` | `enforce_safe_casting_to_output=b` | `False` |
| `enforce_linear_iteration(b)` | `enforce_linear_iteration=b` | `False` |
| `resize_outputs(b)` | `resize_outputs=b` | `True` |
| `set_check_mem_overlap(b)` | `check_mem_overlap=b` | `True` |
| `allow_cpu_scalars(b)` | `allow_cpu_scalars=b` | `False` |
| `is_reduction(b)` | `is_reduction=b` | `False` |
| `declare_static_dtype(d)` | `static_dtype=d` | `None` |
| `declare_static_device(dev)` | `static_device=dev` | `None` |
| `declare_static_shape(s, squash)` | `static_shape=s, squash_dims=squash` | `None` |

`outputs` accepts `None` placeholders for outputs the iterator should allocate itself; `inputs` and `const_inputs` must be defined tensors.

Factory shortcuts[#](https://docs.pytorch.org/docs/2.15/notes/tensor_iterator.html#factory-shortcuts "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

The C++ named constructors at `aten/src/ATen/TensorIterator.cpp` (`binary_op`, `unary_op`, `comparison_op`, `nullary_op`, `reduce_op`, `binary_float_op`, `unary_float_op`) have direct Python equivalents that bake in the canonical flag combinations:

from torch.\_tensor\_iterator import (
    binary\_op,
    binary\_float\_op,
    comparison\_op,
    nullary\_op,
    reduce\_op,
    unary\_op,
    unary\_float\_op,
)

it \= binary\_op(None, a, b)             \# auto-allocate output, promote+cast
it \= comparison\_op(None, a, b)         \# output dtype forced to bool
it \= unary\_float\_op(None, int\_tensor)  \# promotes int input to float

Copy to clipboard

Each factory mirrors its C++ counterpart’s flag set exactly; reach for them when you’d reach for the C++ named constructor.

Canonical-recipe caveats[#](https://docs.pytorch.org/docs/2.15/notes/tensor_iterator.html#canonical-recipe-caveats "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

The Python surface is a _canonical_ projection of the C++ builder, not a faithful replay of arbitrary fluent call sequences. Two consequences:

**Operand ordering is fixed at outputs → inputs → const\_inputs.** The C++ builder distinguishes `add_input(a); add_const_input(b)` from `add_const_input(b); add_input(a)` – `input(0)` refers to different operands. The Python surface cannot express that distinction: every `inputs[i]` precedes every `const_inputs[j]` in the registered operand list.

**Setters are applied as final state, not as a sequence of calls.** Some C++ setters have order-dependent side effects – e.g. `promote_inputs_to_common_dtype(true)` also flips `check_all_same_dtype` to `false`. The Python surface materializes the _final_ boolean state of each knob, so it can’t reproduce a sequence where an intermediate setter observed a since-overwritten value.

Every in-tree caller of `at::TensorIteratorConfig` fits the canonical-recipe shape, so the lossiness is theoretical, not practical.

Inspecting the result[#](https://docs.pytorch.org/docs/2.15/notes/tensor_iterator.html#inspecting-the-result "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

After construction, the iterator is read-only. Useful properties and methods:

it.ndim           \# rank after coalesce/reorder
it.shape          \# zero-copy memoryview of int64 dims
it.numel          \# product of shape
it.ntensors       \# total operands (outputs + inputs)
it.ninputs
it.noutputs
it.is\_contiguous
it.is\_trivial\_1d
it.common\_dtype   \# inferred computation dtype, or None

it.tensor(i)              \# operand at flat index i
it.input(i\=0)             \# input by input-index
it.output(i\=0)            \# output by output-index
it.dtype(i\=0)             \# per-operand dtype
it.device(i\=0)            \# per-operand device
it.strides(i)             \# byte strides, zero-copy memoryview
it.element\_strides(i)     \# element strides (byte\_stride // element\_size)

Copy to clipboard

`shape` and `strides(i)` return `memoryview` objects backed by the iterator’s own buffers. They are valid for the lifetime of the iterator; copy via `tuple(it.shape)` if you need a snapshot.

When to use this[#](https://docs.pytorch.org/docs/2.15/notes/tensor_iterator.html#when-to-use-this "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

*   **Pre-dispatch layout analysis.** Build a TI on the same operands an aten kernel would, then pattern-match `it.ndim` / `it.strides(i)` to decide whether your custom kernel can handle the shape. The `_scatter_add_eligibility` helper in `torch/_native/ops/scatter_add/` is a worked example.
    
*   **Debugging dtype/promotion surprises.** Construct a TI with the flags you think a kernel uses; `it.common_dtype` and `it.dtype(i)` show what the builder actually inferred.
    
*   **Validating custom op contracts.** If your kernel claims to handle a certain shape/dtype combination, build a TI and assert on its post-build geometry.
    

When _not_ to use this[#](https://docs.pytorch.org/docs/2.15/notes/tensor_iterator.html#when-not-to-use-this "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

*   You want to actually run a kernel. There is no `for_each` – use the public `torch.*` op or write a C++ kernel.
    
*   You need exact replay of an arbitrary `TensorIteratorConfig` call sequence (see caveats above).
    

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/notes/tensor_iterator.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/notes/tensor_iterator.md.txt)

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