Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/notes/randomness.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/notes/randomness.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/notes/randomness.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/notes/randomness.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/notes/randomness.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/notes/randomness.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/notes/randomness.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/notes/randomness.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/notes/randomness.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/notes/randomness.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/notes/randomness.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/notes/randomness.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/notes/randomness.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/notes/randomness.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/notes/randomness.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/notes/randomness.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/notes/randomness.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/notes/randomness.html)
[v1.13](https://docs.pytorch.org/docs/1.13/notes/randomness.html)
[v1.12](https://docs.pytorch.org/docs/1.12/notes/randomness.html)
[v1.11](https://docs.pytorch.org/docs/1.11/notes/randomness.html)
[v1.10](https://docs.pytorch.org/docs/1.10/notes/randomness.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/notes/randomness.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/notes/randomness.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/notes/randomness.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/notes/randomness.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/notes/randomness.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/notes/randomness.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/notes/randomness.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/notes/randomness.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/notes/randomness.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/notes/randomness.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/notes/randomness.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/notes/randomness.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/notes/randomness.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/notes/randomness.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/notes/randomness.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/notes/randomness.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/notes/randomness.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/notes/randomness.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/notes/randomness.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/notes/randomness.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/notes/randomness.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/notes/randomness.html)

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

Reproducibility[#](https://docs.pytorch.org/docs/2.15/notes/randomness.html#reproducibility "Link to this heading")

====================================================================================================================

Created On: May 14, 2026 | Last Updated On: May 14, 2026

Completely reproducible results are not guaranteed across PyTorch releases, individual commits, or different platforms. Furthermore, results may not be reproducible between CPU and GPU executions, even when using identical seeds.

However, there are some steps you can take to limit the number of sources of nondeterministic behavior for a specific platform, device, and PyTorch release. First, you can control sources of randomness that can cause multiple executions of your application to behave differently. Second, you can configure PyTorch to avoid using nondeterministic algorithms for some operations, so that multiple calls to those operations, given the same inputs, will produce the same result.

Warning

Deterministic operations are often slower than nondeterministic operations, so single-run performance may decrease for your model. However, determinism may save time in development by facilitating experimentation, debugging, and regression testing.

Controlling sources of randomness[#](https://docs.pytorch.org/docs/2.15/notes/randomness.html#controlling-sources-of-randomness "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

### PyTorch random number generator[#](https://docs.pytorch.org/docs/2.15/notes/randomness.html#pytorch-random-number-generator "Link to this heading")

You can use [`torch.manual_seed()`](https://docs.pytorch.org/docs/2.15/generated/torch.manual_seed.html#torch.manual_seed "torch.manual_seed")
 to seed the RNG for all devices (both CPU and CUDA):

import torch
torch.manual\_seed(0)

Copy to clipboard

Some PyTorch operations may use random numbers internally. [`torch.svd_lowrank()`](https://docs.pytorch.org/docs/2.15/generated/torch.svd_lowrank.html#torch.svd_lowrank "torch.svd_lowrank")
 does this, for instance. Consequently, calling it multiple times back-to-back with the same input arguments may give different results. However, as long as [`torch.manual_seed()`](https://docs.pytorch.org/docs/2.15/generated/torch.manual_seed.html#torch.manual_seed "torch.manual_seed")
 is set to a constant at the beginning of an application and all other sources of nondeterminism have been eliminated, the same series of random numbers will be generated each time the application is run in the same environment.

It is also possible to obtain identical results from an operation that uses random numbers by setting [`torch.manual_seed()`](https://docs.pytorch.org/docs/2.15/generated/torch.manual_seed.html#torch.manual_seed "torch.manual_seed")
 to the same value between subsequent calls.

### Python[#](https://docs.pytorch.org/docs/2.15/notes/randomness.html#python "Link to this heading")

For custom operators, you might need to set python seed as well:

import random
random.seed(0)

Copy to clipboard

### Random number generators in other libraries[#](https://docs.pytorch.org/docs/2.15/notes/randomness.html#random-number-generators-in-other-libraries "Link to this heading")

If you or any of the libraries you are using rely on NumPy, you can seed the global NumPy RNG with:

import numpy as np
np.random.seed(0)

Copy to clipboard

However, some applications and libraries may use NumPy Random Generator objects, not the global RNG ([https://numpy.org/doc/stable/reference/random/generator.html](https://numpy.org/doc/stable/reference/random/generator.html)
), and those will need to be seeded consistently as well.

If you are using any other libraries that use random number generators, refer to the documentation for those libraries to see how to set consistent seeds for them.

### CUDA convolution benchmarking[#](https://docs.pytorch.org/docs/2.15/notes/randomness.html#cuda-convolution-benchmarking "Link to this heading")

The cuDNN library, used by CUDA convolution operations, can be a source of nondeterminism across multiple executions of an application. When a cuDNN convolution is called with a new set of size parameters, an optional feature can run multiple convolution algorithms, benchmarking them to find the fastest one. Then, the fastest algorithm will be used consistently during the rest of the process for the corresponding set of size parameters. Due to benchmarking noise and different hardware, the benchmark may select different algorithms on subsequent runs, even on the same machine.

Disabling the benchmarking feature with `torch.backends.cudnn.benchmark = False` causes cuDNN to deterministically select an algorithm, possibly at the cost of reduced performance.

However, if you do not need reproducibility across multiple executions of your application, then performance might improve if the benchmarking feature is enabled with `torch.backends.cudnn.benchmark = True`.

Note that this setting is different from the `torch.backends.cudnn.deterministic` setting discussed below.

Avoiding nondeterministic algorithms[#](https://docs.pytorch.org/docs/2.15/notes/randomness.html#avoiding-nondeterministic-algorithms "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

[`torch.use_deterministic_algorithms()`](https://docs.pytorch.org/docs/2.15/generated/torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms "torch.use_deterministic_algorithms")
 lets you configure PyTorch to use deterministic algorithms instead of nondeterministic ones where available, and to throw an error if an operation is known to be nondeterministic (and without a deterministic alternative).

Please check the documentation for [`torch.use_deterministic_algorithms()`](https://docs.pytorch.org/docs/2.15/generated/torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms "torch.use_deterministic_algorithms")
 for a full list of affected operations. If an operation does not act correctly according to the documentation, or if you need a deterministic implementation of an operation that does not have one, please submit an issue: [https://github.com/pytorch/pytorch/issues?q=label:”module: determinism”](https://github.com/pytorch/pytorch/issues?q=label:%22module:%20determinism%22)

For example, running the nondeterministic CUDA implementation of [`torch.Tensor.index_add_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.index_add_.html#torch.Tensor.index_add_ "torch.Tensor.index_add_")
 will throw an error:

\>>> import torch
\>>> torch.use\_deterministic\_algorithms(True)
\>>> torch.randn(2, 2).cuda().index\_add\_(0, torch.tensor(\[0, 1\]), torch.randn(2, 2))
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
RuntimeError: index\_add\_cuda\_ does not have a deterministic implementation, but you set
'torch.use\_deterministic\_algorithms(True)'. ...

Copy to clipboard

When [`torch.bmm()`](https://docs.pytorch.org/docs/2.15/generated/torch.bmm.html#torch.bmm "torch.bmm")
 is called with sparse-dense CUDA tensors it typically uses a nondeterministic algorithm, but when the deterministic flag is turned on, its alternate deterministic implementation will be used:

\>>> import torch
\>>> torch.use\_deterministic\_algorithms(True)
\>>> torch.bmm(torch.randn(2, 2, 2).to\_sparse().cuda(), torch.randn(2, 2, 2).cuda())
tensor(\[\[\[ 1.1900, -2.3409\],\
         \[ 0.4796,  0.8003\]\],\
        \[\[ 0.1509,  1.8027\],\
         \[ 0.0333, -1.1444\]\]\], device='cuda:0')

Copy to clipboard

### CUDA convolution determinism[#](https://docs.pytorch.org/docs/2.15/notes/randomness.html#cuda-convolution-determinism "Link to this heading")

While disabling CUDA convolution benchmarking (discussed above) ensures that CUDA selects the same algorithm each time an application is run, that algorithm itself may be nondeterministic, unless either `torch.use_deterministic_algorithms(True)` or `torch.backends.cudnn.deterministic = True` is set. The latter setting controls only this behavior, unlike [`torch.use_deterministic_algorithms()`](https://docs.pytorch.org/docs/2.15/generated/torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms "torch.use_deterministic_algorithms")
 which will make other PyTorch operations behave deterministically, too.

### CUDA Scaled Dot Product Attention[#](https://docs.pytorch.org/docs/2.15/notes/randomness.html#cuda-scaled-dot-product-attention "Link to this heading")

[`torch.nn.functional.scaled_dot_product_attention()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.scaled_dot_product_attention.html#torch.nn.functional.scaled_dot_product_attention "torch.nn.functional.scaled_dot_product_attention")
 (SDPA) dispatches to multiple backends at runtime. Each backend has different determinism characteristics, summarized in the table below:

   
| Backend | Forward | Backward | Notes |
| --- | --- | --- | --- |
| `SDPBackend.MATH` | Deterministic | Deterministic | Uses standard PyTorch operators (`matmul`, `softmax`). Deterministic when [`torch.use_deterministic_algorithms()`](https://docs.pytorch.org/docs/2.15/generated/torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms "torch.use_deterministic_algorithms")<br> is enabled. |
| `SDPBackend.FLASH_ATTENTION` | Deterministic | Non-deterministic | The backward pass uses non-deterministic atomic operations by default. Setting `torch.use_deterministic_algorithms(True, warn_only=False)` enables a deterministic backward implementation. |
| `SDPBackend.EFFICIENT_ATTENTION` | Deterministic | Non-deterministic | The backward pass may split work across keys (`num_splits_key > 1`) for performance, which is non-deterministic. Setting `torch.use_deterministic_algorithms(True, warn_only=False)` forces `num_splits_key = 1`, making the backward pass deterministic. |
| `SDPBackend.CUDNN_ATTENTION` | Deterministic | Non-deterministic | cuDNN provides an opt-in deterministic backward for `float16` starting in [cuDNN 9.18](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/release-notes.html#cudnn-9-18-0)<br> (via [set\_deterministic\_algorithm](https://docs.nvidia.com/deeplearning/cudnn/frontend/latest/operations/Attention.html#sdpa-fp16-bf16-backward)<br>), but this has not yet been integrated into PyTorch. This backend is **disabled** when `torch.use_deterministic_algorithms(True, warn_only=False)` is set, regardless of whether inputs require gradients or the call is inside a `torch.no_grad()` context. |

When `torch.use_deterministic_algorithms(True, warn_only=True)` is set, the fused backends (Flash, Efficient, and cuDNN) emit a one-time warning but still use their default non-deterministic code paths. To actually enforce determinism, pass `warn_only=False`.

**Low-precision dtypes and numerical reproducibility**

Bitwise matching numerics across different SDPA backends are **not guaranteed**, even for the same inputs and dtype. Each backend performs floating-point accumulation in a different order, and because floating-point addition is not associative, the results will differ between backends.

The Math backend by default accumulates in `float32` even when given `float16` or `bfloat16` inputs. The function [`torch.backends.cuda.allow_fp16_bf16_reduction_math_sdp()`](https://docs.pytorch.org/docs/2.15/backends.html#torch.backends.cuda.allow_fp16_bf16_reduction_math_sdp "torch.backends.cuda.allow_fp16_bf16_reduction_math_sdp")
 can enable reduced-precision accumulation for higher performance at the cost of different numerical results.

**Selecting a specific backend**

Use the [`torch.nn.attention.sdpa_kernel()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.attention.sdpa_kernel.html#torch.nn.attention.sdpa_kernel "torch.nn.attention.sdpa_kernel")
 context manager to restrict which backends SDPA may use. For example, to guarantee deterministic behavior regardless of hardware:

import torch
from torch.nn.attention import sdpa\_kernel, SDPBackend

torch.use\_deterministic\_algorithms(True)

\# Option 1: Use only the Math backend (always deterministic)
with sdpa\_kernel(SDPBackend.MATH):
    out \= torch.nn.functional.scaled\_dot\_product\_attention(q, k, v)

\# Option 2: Allow Flash and Efficient (deterministic with the flag above)
with sdpa\_kernel(\[SDPBackend.FLASH\_ATTENTION, SDPBackend.EFFICIENT\_ATTENTION\]):
    out \= torch.nn.functional.scaled\_dot\_product\_attention(q, k, v)

Copy to clipboard

### CUDA RNN and LSTM[#](https://docs.pytorch.org/docs/2.15/notes/randomness.html#cuda-rnn-and-lstm "Link to this heading")

In some versions of CUDA, RNNs and LSTM networks may have non-deterministic behavior. See [`torch.nn.RNN()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.RNN.html#torch.nn.RNN "torch.nn.RNN")
 and [`torch.nn.LSTM()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.LSTM.html#torch.nn.LSTM "torch.nn.LSTM")
 for details and workarounds.

### Filling uninitialized memory[#](https://docs.pytorch.org/docs/2.15/notes/randomness.html#filling-uninitialized-memory "Link to this heading")

Operations like [`torch.empty()`](https://docs.pytorch.org/docs/2.15/generated/torch.empty.html#torch.empty "torch.empty")
 and [`torch.Tensor.resize_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.resize_.html#torch.Tensor.resize_ "torch.Tensor.resize_")
 can return tensors with uninitialized memory that contain undefined values. Using such a tensor as an input to another operation is invalid if determinism is required, because the output will be nondeterministic. But there is nothing to actually prevent such invalid code from being run. So for safety, [`torch.utils.deterministic.fill_uninitialized_memory`](https://docs.pytorch.org/docs/2.15/deterministic.html#torch.utils.deterministic.fill_uninitialized_memory "torch.utils.deterministic.fill_uninitialized_memory")
 is set to `True` by default, which will fill the uninitialized memory with a known value if `torch.use_deterministic_algorithms(True)` is set. This will prevent the possibility of this kind of nondeterministic behavior.

However, filling uninitialized memory is detrimental to performance. So if your program is valid and does not use uninitialized memory as the input to an operation, then this setting can be turned off for better performance.

DataLoader[#](https://docs.pytorch.org/docs/2.15/notes/randomness.html#dataloader "Link to this heading")

----------------------------------------------------------------------------------------------------------

DataLoader will reseed workers following the [Randomness in multi-process data loading](https://docs.pytorch.org/docs/2.15/data.html#data-loading-randomness)
 algorithm. Use `worker_init_fn()` and `generator` to preserve reproducibility:

def seed\_worker(worker\_id):
    worker\_seed \= torch.initial\_seed() % 2\*\*32
    numpy.random.seed(worker\_seed)
    random.seed(worker\_seed)

g \= torch.Generator()
g.manual\_seed(0)

DataLoader(
    train\_dataset,
    batch\_size\=batch\_size,
    num\_workers\=num\_workers,
    worker\_init\_fn\=seed\_worker,
    generator\=g,
)

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/notes/randomness.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/notes/randomness.md.txt)

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