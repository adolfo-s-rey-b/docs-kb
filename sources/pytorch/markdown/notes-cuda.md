Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/notes/cuda.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/notes/cuda.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/notes/cuda.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/notes/cuda.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/notes/cuda.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/notes/cuda.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/notes/cuda.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/notes/cuda.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/notes/cuda.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/notes/cuda.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/notes/cuda.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/notes/cuda.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/notes/cuda.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/notes/cuda.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/notes/cuda.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/notes/cuda.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/notes/cuda.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/notes/cuda.html)
[v1.13](https://docs.pytorch.org/docs/1.13/notes/cuda.html)
[v1.12](https://docs.pytorch.org/docs/1.12/notes/cuda.html)
[v1.11](https://docs.pytorch.org/docs/1.11/notes/cuda.html)
[v1.10](https://docs.pytorch.org/docs/1.10/notes/cuda.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/notes/cuda.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/notes/cuda.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/notes/cuda.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/notes/cuda.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/notes/cuda.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/notes/cuda.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/notes/cuda.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/notes/cuda.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/notes/cuda.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/notes/cuda.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/notes/cuda.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/notes/cuda.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/notes/cuda.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/notes/cuda.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/notes/cuda.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/notes/cuda.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/notes/cuda.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/notes/cuda.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/notes/cuda.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/notes/cuda.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/notes/cuda.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/notes/cuda.html)

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

CUDA semantics[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#cuda-semantics "Link to this heading")

============================================================================================================

Created On: Jan 16, 2017 | Last Updated On: Sep 05, 2026

[`torch.cuda`](https://docs.pytorch.org/docs/2.15/cuda.html#module-torch.cuda "torch.cuda")
 is used to set up and run CUDA operations. It keeps track of the currently selected GPU, and all CUDA tensors you allocate will by default be created on that device. The selected device can be changed with a [`torch.cuda.device`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.device.html#torch.cuda.device "torch.cuda.device")
 context manager.

However, once a tensor is allocated, you can do operations on it irrespective of the selected device, and the results will be always placed on the same device as the tensor.

Cross-GPU operations are not allowed by default, with the exception of [`copy_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.copy_.html#torch.Tensor.copy_ "torch.Tensor.copy_")
 and other methods with copy-like functionality such as [`to()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.to.html#torch.Tensor.to "torch.Tensor.to")
 and [`cuda()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.cuda.html#torch.Tensor.cuda "torch.Tensor.cuda")
. Unless you enable peer-to-peer memory access, any attempts to launch ops on tensors spread across different devices will raise an error.

Below you can find a small example showcasing this:

cuda \= torch.device('cuda')     \# Default CUDA device
cuda0 \= torch.device('cuda:0')
cuda2 \= torch.device('cuda:2')  \# GPU 2 (these are 0-indexed)

x \= torch.tensor(\[1., 2.\], device\=cuda0)
\# x.device is device(type='cuda', index=0)
y \= torch.tensor(\[1., 2.\]).cuda()
\# y.device is device(type='cuda', index=0)

with torch.cuda.device(1):
    \# allocates a tensor on GPU 1
    a \= torch.tensor(\[1., 2.\], device\=cuda)

    \# transfers a tensor from CPU to GPU 1
    b \= torch.tensor(\[1., 2.\]).cuda()
    \# a.device and b.device are device(type='cuda', index=1)

    \# You can also use \`\`Tensor.to\`\` to transfer a tensor:
    b2 \= torch.tensor(\[1., 2.\]).to(device\=cuda)
    \# b.device and b2.device are device(type='cuda', index=1)

    c \= a + b
    \# c.device is device(type='cuda', index=1)

    z \= x + y
    \# z.device is device(type='cuda', index=0)

    \# even within a context, you can specify the device
    \# (or give a GPU index to the .cuda call)
    d \= torch.randn(2, device\=cuda2)
    e \= torch.randn(2).to(cuda2)
    f \= torch.randn(2).cuda(cuda2)
    \# d.device, e.device, and f.device are all device(type='cuda', index=2)

Copy to clipboard

TensorFloat-32 (TF32) on Ampere (and later) devices[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#tensorfloat-32-tf32-on-ampere-and-later-devices "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

After PyTorch 2.9, we provide a new sets of APIs to control the TF32 behavior in a more fine-grained way, and suggest to use the new APIs for better control. We can set float32 precision per backend and per operators. We can also override the global setting for a specific operator.

torch.backends.fp32\_precision \= "ieee"
torch.backends.cuda.matmul.fp32\_precision \= "ieee"
torch.backends.cudnn.fp32\_precision \= "ieee"
torch.backends.cudnn.conv.fp32\_precision \= "tf32"
torch.backends.cudnn.rnn.fp32\_precision \= "tf32"

Copy to clipboard

The `fp32_precision` setting can be set to `ieee` or `tf32` for CUDA matmuls and cuDNN. `ieee` uses FP32 for internal computation, while `tf32` allows TF32 for internal computation.

With a CUDA 12.9 or newer build, CUDA matmuls also accept `bfx9`, which allows cuBLAS to use its BF16x9 algorithm:

torch.backends.cuda.matmul.fp32\_precision \= "bfx9"

Copy to clipboard

This mode keeps the inputs and output in FP32 while allowing cuBLAS to decompose each input into three BF16 values and evaluate the resulting nine BF16 products with FP32 accumulation. The decomposition retains all FP32 input bits, but the resulting arithmetic is not IEEE-754 compliant and its relative accuracy is workload-dependent. The BF16x9 algorithm is available on GPUs with compute capability 10.0 or 10.3. On other NVIDIA GPU architectures, cuBLAS accepts the mode but uses native FP32 because no BF16x9 implementation is available. `bfx9` requires a PyTorch build with CUDA 12.9 or newer and is valid only for `torch.backends.cuda.matmul.fp32_precision`; using it for a generic, cuDNN, or MKLDNN precision setting raises an error. Setting `bfx9` on an older CUDA build or ROCm raises an error.

As with `tf32`, operations implemented using CUDA GEMM can inherit the matmul precision setting, including slow or naive convolution fallbacks. Under `torch.compile`, FP32 matmuls using `bfx9` remain ATen/cuBLAS calls because Triton’s `bf16x3` and `bf16x6` modes do not implement the full nine-product algorithm. Fused Triton kernels that cannot preserve `bfx9`, such as FP32 FlexAttention, warn once and use IEEE precision instead.

We can override a generic setting for a specific operator if the fp32\_precision is set to `ieee`.

torch.backends.cudnn.fp32\_precision \= "tf32"
torch.backends.cudnn.conv.fp32\_precision \= "ieee"
torch.backends.cudnn.rnn.fp32\_precision \= "ieee"

Copy to clipboard

We can also override a generic setting for a specific backend if the fp32\_precision is set to `ieee`.

torch.backends.fp32\_precision \= "tf32"
torch.backends.cudnn.fp32\_precision \= "ieee"
torch.backends.cudnn.conv.fp32\_precision \= "ieee"
torch.backends.cudnn.rnn.fp32\_precision \= "ieee"

Copy to clipboard

For above 2 cases, both `torch.backends.cudnn.conv.fp32_precision` and `torch.backends.cudnn.rnn.fp32_precision` is overridden to `ieee`.

We suggest to use the new settings for better control. And we do not support to use mix of old and new settings.

Warning

Old settings with `allow_tf32` as follows is going to be deprecated. We suggest to use the above new settings for better control. And we do not support to use mix of old and new settings.

Starting in PyTorch 1.7, there is a new flag called `allow_tf32`. This flag defaults to True in PyTorch 1.7 to PyTorch 1.11, and False in PyTorch 1.12 and later. This flag controls whether PyTorch is allowed to use the TensorFloat32 (TF32) tensor cores, available on NVIDIA GPUs since Ampere, internally to compute matmul (matrix multiplies and batched matrix multiplies) and convolutions.

TF32 tensor cores are designed to achieve better performance on matmul and convolutions on `torch.float32` tensors by rounding input data to have 10 bits of mantissa, and accumulating results with FP32 precision, maintaining FP32 dynamic range.

matmuls and convolutions are controlled separately, and their corresponding flags can be accessed at:

\# The flag below controls whether to allow TF32 on matmul. This flag defaults to False
\# in PyTorch 1.12 and later.
torch.backends.cuda.matmul.allow\_tf32 \= True

\# The flag below controls whether to allow TF32 on cuDNN. This flag defaults to True.
torch.backends.cudnn.allow\_tf32 \= True

Copy to clipboard

The precision of matmuls can also be set more broadly (limited not just to CUDA) via [`set_float32_matmul_precision()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_float32_matmul_precision.html#torch.set_float32_matmul_precision "torch.set_float32_matmul_precision")
. Note that besides matmuls and convolutions themselves, functions and nn modules that internally uses matmuls or convolutions are also affected. These include `nn.Linear`, `nn.Conv*`, cdist, tensordot, affine grid and grid sample, adaptive log softmax, GRU and LSTM.

To get an idea of the precision and speed, see the example code and benchmark data (on A100) below:

a\_full \= torch.randn(10240, 10240, dtype\=torch.double, device\='cuda')
b\_full \= torch.randn(10240, 10240, dtype\=torch.double, device\='cuda')
ab\_full \= a\_full @ b\_full
mean \= ab\_full.abs().mean()  \# 80.7277

a \= a\_full.float()
b \= b\_full.float()

\# Do matmul at TF32 mode.
torch.backends.cuda.matmul.allow\_tf32 \= True
ab\_tf32 \= a @ b  \# takes 0.016s on GA100
error \= (ab\_tf32 \- ab\_full).abs().max()  \# 0.1747
relative\_error \= error / mean  \# 0.0022

\# Do matmul with TF32 disabled.
torch.backends.cuda.matmul.allow\_tf32 \= False
ab\_fp32 \= a @ b  \# takes 0.11s on GA100
error \= (ab\_fp32 \- ab\_full).abs().max()  \# 0.0031
relative\_error \= error / mean  \# 0.000039

Copy to clipboard

From the above example, we can see that with TF32 enabled, the speed is ~7x faster on A100, and that relative error compared to double precision is approximately 2 orders of magnitude larger. Note that the exact ratio of TF32 to single precision speed depends on the hardware generation, as properties such as the ratio of memory bandwidth to compute as well as the ratio of TF32 to FP32 matmul throughput may vary from generation to generation or model to model. If full FP32 precision is needed, users can disable TF32 by:

torch.backends.cuda.matmul.allow\_tf32 \= False
torch.backends.cudnn.allow\_tf32 \= False

Copy to clipboard

To toggle the TF32 flags off in C++, you can do

at::globalContext().setAllowTF32CuBLAS(false);
at::globalContext().setAllowTF32CuDNN(false);

Copy to clipboard

For more information about TF32, see:

*   [TensorFloat-32](https://blogs.nvidia.com/blog/2020/05/14/tensorfloat-32-precision-format/)
    
*   [CUDA 11](https://devblogs.nvidia.com/cuda-11-features-revealed/)
    
*   [Ampere architecture](https://devblogs.nvidia.com/nvidia-ampere-architecture-in-depth/)
    

Reduced Precision Reduction in FP16 GEMMs[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#reduced-precision-reduction-in-fp16-gemms "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

(Distinct from full FP16 accumulation that is intended for hardware that has higher throughput with FP16 accumulation than FP32 accumulation, see [Full FP16 accumulation](https://docs.pytorch.org/docs/2.15/notes/cuda.html#fp16accumulation)
)

fp16 GEMMs are potentially done with some intermediate reduced precision reductions (e.g., in fp16 rather than fp32). These selective reductions in precision can allow for higher performance on certain workloads (particularly those with a large `k` dimension) and GPU architectures at the cost of numerical precision and potential for overflow.

Some example benchmark data on V100:

\[\--------------------------- bench\_gemm\_transformer \--------------------------\]
      \[  m ,  k  ,  n  \]    |  allow\_fp16\_reduc\=True  |  allow\_fp16\_reduc\=False
1 threads: \--------------------------------------------------------------------
      \[4096, 4048, 4096\]    |           1634.6        |           1639.8
      \[4096, 4056, 4096\]    |           1670.8        |           1661.9
      \[4096, 4080, 4096\]    |           1664.2        |           1658.3
      \[4096, 4096, 4096\]    |           1639.4        |           1651.0
      \[4096, 4104, 4096\]    |           1677.4        |           1674.9
      \[4096, 4128, 4096\]    |           1655.7        |           1646.0
      \[4096, 4144, 4096\]    |           1796.8        |           2519.6
      \[4096, 5096, 4096\]    |           2094.6        |           3190.0
      \[4096, 5104, 4096\]    |           2144.0        |           2663.5
      \[4096, 5112, 4096\]    |           2149.1        |           2766.9
      \[4096, 5120, 4096\]    |           2142.8        |           2631.0
      \[4096, 9728, 4096\]    |           3875.1        |           5779.8
      \[4096, 16384, 4096\]   |           6182.9        |           9656.5
(times in microseconds).

Copy to clipboard

If full precision reductions are needed, users can disable reduced precision reductions in fp16 GEMMs with:

torch.backends.cuda.matmul.allow\_fp16\_reduced\_precision\_reduction \= False

Copy to clipboard

Assigning a boolean is equivalent to assigning `(allow_reduced_precision, True)` and sets `allow_splitk` to `True`. To disable both reduced precision reductions and split-k reductions, assign `(allow_reduced_precision, allow_splitk)` explicitly:

torch.backends.cuda.matmul.allow\_fp16\_reduced\_precision\_reduction \= (False, False)

Copy to clipboard

The current split-k setting can be queried with `torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction_split_k`. The combination `(True, False)` is not supported because reduced precision reductions require split-k.

To toggle the reduced precision reduction flags in C++, one can do

at::globalContext().setAllowFP16ReductionCuBLAS(false, false);

Copy to clipboard

The second argument is `allow_splitk` and defaults to `true` when omitted.

Reduced Precision Reduction in BF16 GEMMs[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#reduced-precision-reduction-in-bf16-gemms "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

A similar flag (as above) exists for BFloat16 GEMMs. Note that this switch is set to `True` by default for BF16, if you observe numerical instability in your workload, you may wish to set it to `False`.

If reduced precision reductions are not desired, users can disable reduced precision reductions in bf16 GEMMs with:

torch.backends.cuda.matmul.allow\_bf16\_reduced\_precision\_reduction \= False

Copy to clipboard

Assigning a boolean is equivalent to assigning `(allow_reduced_precision, True)` and sets `allow_splitk` to `True`. To disable both reduced precision reductions and split-k reductions, assign `(allow_reduced_precision, allow_splitk)` explicitly:

torch.backends.cuda.matmul.allow\_bf16\_reduced\_precision\_reduction \= (False, False)

Copy to clipboard

The current split-K setting can be queried with `torch.backends.cuda.matmul.allow_bf16_reduced_precision_reduction_split_k`. The combination `(True, False)` is not supported because reduced precision reductions require split-K.

To toggle the reduced precision reduction flags in C++, one can do

at::globalContext().setAllowBF16ReductionCuBLAS(false, false);

Copy to clipboard

The second argument is `allow_splitk` and defaults to `true` when omitted.

Full FP16 Accumulation in FP16 GEMMs[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#full-fp16-accumulation-in-fp16-gemms "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

Certain GPUs have increased performance when doing _all_ FP16 GEMM accumulation in FP16, at the cost of numerical precision and greater likelihood of overflow. Note that this setting only has an effect on GPUs of compute capability 7.0 (Volta) or newer.

This behavior can be enabled via:

torch.backends.cuda.matmul.allow\_fp16\_accumulation \= True

Copy to clipboard

To toggle the reduced precision reduction flags in C++, one can do

at::globalContext().setAllowFP16AccumulationCuBLAS(true);

Copy to clipboard

Asynchronous execution[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#asynchronous-execution "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

By default, GPU operations are asynchronous. When you call a function that uses the GPU, the operations are _enqueued_ to the particular device, but not necessarily executed until later. This allows us to execute more computations in parallel, including operations on CPU or other GPUs.

In general, the effect of asynchronous computation is invisible to the caller, because (1) each device executes operations in the order they are queued, and (2) PyTorch automatically performs necessary synchronization when copying data between CPU and GPU or between two GPUs. Hence, computation will proceed as if every operation was executed synchronously.

You can force synchronous computation by setting environment variable `CUDA_LAUNCH_BLOCKING=1`. This can be handy when an error occurs on the GPU. (With asynchronous execution, such an error isn’t reported until after the operation is actually executed, so the stack trace does not show where it was requested.)

A consequence of the asynchronous computation is that time measurements without synchronizations are not accurate. To get precise measurements, one should either call [`torch.cuda.synchronize()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.synchronize.html#torch.cuda.synchronize "torch.cuda.synchronize")
 before measuring, or use [`torch.cuda.Event`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.Event.html#torch.cuda.Event "torch.cuda.Event")
 to record times as following:

start\_event \= torch.cuda.Event(enable\_timing\=True)
end\_event \= torch.cuda.Event(enable\_timing\=True)
start\_event.record()

\# Run some things here

end\_event.record()
torch.cuda.synchronize()  \# Wait for the events to be recorded!
elapsed\_time\_ms \= start\_event.elapsed\_time(end\_event)

Copy to clipboard

As an exception, several functions such as [`to()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.to.html#torch.Tensor.to "torch.Tensor.to")
 and [`copy_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.copy_.html#torch.Tensor.copy_ "torch.Tensor.copy_")
 admit an explicit `non_blocking` argument, which lets the caller bypass synchronization when it is unnecessary. Another exception is CUDA streams, explained below.

### CUDA streams[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#cuda-streams "Link to this heading")

A [CUDA stream](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#streams)
 is a linear sequence of execution that belongs to a specific device. You normally do not need to create one explicitly: by default, each device uses its own “default” stream.

Operations inside each stream are serialized in the order they are created, but operations from different streams can execute concurrently in any relative order, unless explicit synchronization functions (such as [`synchronize()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.synchronize.html#torch.cuda.synchronize "torch.cuda.synchronize")
 or [`wait_stream()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.Stream_class.html#torch.cuda.Stream.wait_stream "torch.cuda.Stream.wait_stream")
) are used. For example, the following code is incorrect:

cuda \= torch.device('cuda')
s \= torch.cuda.Stream()  \# Create a new stream.
A \= torch.empty((100, 100), device\=cuda).normal\_(0.0, 1.0)
with torch.cuda.stream(s):
    \# sum() may start execution before normal\_() finishes!
    B \= torch.sum(A)

Copy to clipboard

When the “current stream” is the default stream, PyTorch automatically performs necessary synchronization when data is moved around, as explained above. However, when using non-default streams, it is the user’s responsibility to ensure proper synchronization. The fixed version of this example is:

cuda \= torch.device('cuda')
s \= torch.cuda.Stream()  \# Create a new stream.
A \= torch.empty((100, 100), device\=cuda).normal\_(0.0, 1.0)
s.wait\_stream(torch.cuda.default\_stream(cuda))  \# NEW!
with torch.cuda.stream(s):
    B \= torch.sum(A)
A.record\_stream(s)  \# NEW!

Copy to clipboard

There are two new additions. The [`torch.cuda.Stream.wait_stream()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.Stream_class.html#torch.cuda.Stream.wait_stream "torch.cuda.Stream.wait_stream")
 call ensures that the `normal_()` execution has finished before we start running `sum(A)` on a side stream. The [`torch.Tensor.record_stream()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.record_stream.html#torch.Tensor.record_stream "torch.Tensor.record_stream")
 (see for more details) ensures that we do not deallocate A before `sum(A)` has completed. You can also manually wait on the stream at some later point in time with `torch.cuda.default_stream(cuda).wait_stream(s)` (note that it is pointless to wait immediately, since that will prevent the stream execution from running in parallel with other work on the default stream.) See the documentation for [`torch.Tensor.record_stream()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.record_stream.html#torch.Tensor.record_stream "torch.Tensor.record_stream")
 on more details on when to use one or another.

Note that this synchronization is necessary even when there is no read dependency, e.g., as seen in this example:

cuda \= torch.device('cuda')
s \= torch.cuda.Stream()  \# Create a new stream.
A \= torch.empty((100, 100), device\=cuda)
s.wait\_stream(torch.cuda.default\_stream(cuda))  \# STILL REQUIRED!
with torch.cuda.stream(s):
    A.normal\_(0.0, 1.0)
    A.record\_stream(s)

Copy to clipboard

Despite the computation on `s` not reading the contents of `A` and no other uses of `A`, it is still necessary to synchronize, because `A` may correspond to memory reallocated by the CUDA caching allocator, with pending operations from the old (deallocated) memory.

### Stream semantics of backward passes[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#stream-semantics-of-backward-passes "Link to this heading")

Each backward CUDA op runs on the same stream that was used for its corresponding forward op. If your forward pass runs independent ops in parallel on different streams, this helps the backward pass exploit that same parallelism.

The stream semantics of a backward call with respect to surrounding ops are the same as for any other call. The backward pass inserts internal syncs to ensure this even when backward ops run on multiple streams as described in the previous paragraph. More concretely, when calling [`autograd.backward`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.backward.html#torch.autograd.backward "torch.autograd.backward")
, [`autograd.grad`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.grad.html#torch.autograd.grad "torch.autograd.grad")
, or [`tensor.backward`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.backward.html#torch.Tensor.backward "torch.Tensor.backward")
, and optionally supplying CUDA tensor(s) as the initial gradient(s) (e.g., [`autograd.backward(..., grad_tensors=initial_grads)`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.backward.html#torch.autograd.backward "torch.autograd.backward")
, [`autograd.grad(..., grad_outputs=initial_grads)`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.grad.html#torch.autograd.grad "torch.autograd.grad")
, or [`tensor.backward(..., gradient=initial_grad)`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.backward.html#torch.Tensor.backward "torch.Tensor.backward")
), the acts of

1.  optionally populating initial gradient(s),
    
2.  invoking the backward pass, and
    
3.  using the gradients
    

have the same stream-semantics relationship as any group of ops:

s \= torch.cuda.Stream()

\# Safe, grads are used in the same stream context as backward()
with torch.cuda.stream(s):
    loss.backward()
    use grads

\# Unsafe
with torch.cuda.stream(s):
    loss.backward()
use grads

\# Safe, with synchronization
with torch.cuda.stream(s):
    loss.backward()
torch.cuda.current\_stream().wait\_stream(s)
use grads

\# Safe, populating initial grad and invoking backward are in the same stream context
with torch.cuda.stream(s):
    loss.backward(gradient\=torch.ones\_like(loss))

\# Unsafe, populating initial\_grad and invoking backward are in different stream contexts,
\# without synchronization
initial\_grad \= torch.ones\_like(loss)
with torch.cuda.stream(s):
    loss.backward(gradient\=initial\_grad)

\# Safe, with synchronization
initial\_grad \= torch.ones\_like(loss)
s.wait\_stream(torch.cuda.current\_stream())
with torch.cuda.stream(s):
    initial\_grad.record\_stream(s)
    loss.backward(gradient\=initial\_grad)

Copy to clipboard

#### BC note: Using grads on the default stream[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#bc-note-using-grads-on-the-default-stream "Link to this heading")

In prior versions of PyTorch (1.9 and earlier), the autograd engine always synced the default stream with all backward ops, so the following pattern:

with torch.cuda.stream(s):
    loss.backward()
use grads

Copy to clipboard

was safe as long as `use grads` happened on the default stream. In present PyTorch, that pattern is no longer safe. If `backward()` and `use grads` are in different stream contexts, you must sync the streams:

with torch.cuda.stream(s):
    loss.backward()
torch.cuda.current\_stream().wait\_stream(s)
use grads

Copy to clipboard

even if `use grads` is on the default stream.

Memory management[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#memory-management "Link to this heading")

------------------------------------------------------------------------------------------------------------------

PyTorch uses a caching memory allocator to speed up memory allocations. This allows fast memory deallocation without device synchronizations. However, the unused memory managed by the allocator will still show as if used in `nvidia-smi`. You can use `memory_allocated()` and `max_memory_allocated()` to monitor memory occupied by tensors, and use `memory_reserved()` and `max_memory_reserved()` to monitor the total amount of memory managed by the caching allocator. Calling `empty_cache()` releases all **unused** cached memory from PyTorch so that those can be used by other GPU applications. However, the occupied GPU memory by tensors will not be freed so it can not increase the amount of GPU memory available for PyTorch.

To better understand how CUDA memory is being used over time, [Understanding CUDA Memory Usage](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#torch-cuda-memory)
 describes tools for capturing and visualizing traces of memory use.

For more advanced users, we offer more comprehensive memory benchmarking via `memory_stats()`. We also offer the capability to capture a complete snapshot of the memory allocator state via `memory_snapshot()`, which can help you understand the underlying allocation patterns produced by your code.

### Optimizing memory usage with `PYTORCH_ALLOC_CONF`[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#optimizing-memory-usage-with-pytorch-alloc-conf "Link to this heading")

Use of a caching allocator can interfere with memory checking tools such as `cuda-memcheck`. To debug memory errors using `cuda-memcheck`, set `PYTORCH_NO_CUDA_MEMORY_CACHING=1` in your environment to disable caching.

The behavior of the caching allocator can be controlled via the environment variable `PYTORCH_ALLOC_CONF`. `PYTORCH_CUDA_ALLOC_CONF` is its alias and is provided only for backward compatibility. The format is `PYTORCH_ALLOC_CONF=<option>:<value>,<option2>:<value2>...` Available options:

*   `backend` allows selecting the underlying allocator implementation. Currently, valid options are `native`, which uses PyTorch’s native implementation, and `cudaMallocAsync`, which uses [CUDA’s built-in asynchronous allocator](https://developer.nvidia.com/blog/using-cuda-stream-ordered-memory-allocator-part-1/)
    . `cudaMallocAsync` requires CUDA 11.4 or newer. The default is `native`. `backend` applies to all devices used by the process, and can’t be specified on a per-device basis.
    
*   `large_segment_size_mb` the native allocator uses small and large blocks to manage allocated memory. This setting is used to configure the size of the large block. The default value is 20 MB.
    
*   `max_split_size_mb` prevents the native allocator from splitting blocks larger than this size (in MB). This can reduce fragmentation and may allow some borderline workloads to complete without running out of memory. Performance cost can range from ‘zero’ to ‘substantial’ depending on allocation patterns. Default value is unlimited, i.e. all blocks can be split. The `memory_stats()` and `memory_summary()` methods are useful for tuning. This option should be used as a last resort for a workload that is aborting due to ‘out of memory’ and showing a large amount of inactive split blocks. `max_split_size_mb` is only meaningful with `backend:native`. With `backend:cudaMallocAsync`, `max_split_size_mb` is ignored.
    
*   `roundup_power2_divisions` helps with rounding the requested allocation size to nearest power-2 division and making better use of the blocks. In the native CUDACachingAllocator, the sizes are rounded up in multiple of blocks size of 512, so this works fine for smaller sizes. However, this can be inefficient for large near-by allocations as each will go to different size of blocks and reuse of those blocks are minimized. This might create lots of unused blocks and will waste GPU memory capacity. This option enables the rounding of allocation size to nearest power-2 division. For example, if we need to round-up size of 1200 and if number of divisions is 4, the size 1200 lies between 1024 and 2048 and if we do 4 divisions between them, the values are 1024, 1280, 1536, and 1792. So, allocation size of 1200 will be rounded to 1280 as the nearest ceiling of power-2 division. Specify a single value to apply for all allocation sizes or specify an array of key value pairs to set power-2 division individually for each power of two interval. For example to set 1 division for all allocations under 256MB, 2 division for allocations between 256MB and 512MB, 4 divisions for allocations between 512MB and 1GB and 8 divisions for any larger allocations, set the knob value to: \[256:1,512:2,1024:4,>:8\]. `roundup_power2_divisions` is only meaningful with `backend:native`. With `backend:cudaMallocAsync`, `roundup_power2_divisions` is ignored.
    
*   `max_non_split_rounding_mb` will allow non-split blocks for better reuse, eg, a 1024MB cached block can be reused for a 512MB allocation request. In the default case, we only allow up to 20MB of rounding of non-split blocks, so a 512MB block can only be served with between 512-532 MB size block. If we set the value of this option to 1024, it will allow 512-1536 MB size blocks to be used for a 512MB block which increases reuse of larger blocks. This will also help in reducing the stalls in avoiding expensive cudaMalloc calls.
    
*   `garbage_collection_threshold` helps actively reclaiming unused GPU memory to avoid triggering expensive sync-and-reclaim-all operation (release\_cached\_blocks), which can be unfavorable to latency-critical GPU applications (e.g., servers). Upon setting this threshold (e.g., 0.8), the allocator will start reclaiming GPU memory blocks if the GPU memory capacity usage exceeds the threshold (i.e., 80% of the total memory allocated to the GPU application). The algorithm prefers to free old & unused blocks first to avoid freeing blocks that are actively being reused. The threshold value should be between greater than 0.0 and less than 1.0. The default value is set at 1.0.
    
    `garbage_collection_threshold` is only meaningful with `backend:native`. With `backend:cudaMallocAsync`, `garbage_collection_threshold` is ignored.
    
*   `expandable_segments` (experimental, default: `False`) If set to `True`, this setting instructs the allocator to create CUDA allocations that can later be expanded to better handle cases where a job changing allocation sizes frequently, such as having a changing batch size. Normally for large (>2MB) allocations, the allocator calls cudaMalloc to get allocations that are the same size as what the user requests. In the future, parts of these allocations can be reused for other requests if they are free. This works well when the program makes many requests of exactly the same size or of sizes that even multiples of that size. Many deep learning models follow this behavior. However, one common exception is when the batch size changes slightly from one iteration to the next, e.g. in batched inference. When the program runs initially with batch size `N`, it will make allocations appropriate for that size. If in the future, it runs at size `N - 1`, the existing allocations will still be big enough. However, if it runs at size `N + 1`, then it will have to make new allocations that are slightly larger. Not all the tensors are the same size. Some might be `(N + 1)*A` and others `(N + 1)*A*B` where `A` and `B` are some non-batch dimensions in the model. Because the allocator reuses existing allocations when they are big enough, some number of `(N + 1)*A` allocations will actually fit in the already existing `N*B*A` segments, though not perfectly. As the model runs it will partially fill up all of these segments leaving unusable free slices of memory at the end of these segments. The allocator at some point will need to `cudaMalloc` a new `(N + 1)*A*B` segment. If there is not enough memory, there is now no way to recover the slices of memory that are free at the end of existing segments. With models 50+ layers deep, this pattern might repeat 50+ times creating many slivers.
    
    `expandable_segments` allows the allocator to create a segment initially and then expand its size later when more memory is needed. Instead of making one segment per allocation, it tries to make one segment (per stream) that grows as necessary. Now when the `N + 1` case runs, the allocations will tile nicely into the one large segment until it fills up. Then more memory is requested and appended to the end of the segment. This process does not create as many slivers of unusable memory, so it is more likely to succeed at finding this memory.
    
*   `pinned_use_cuda_host_register` option is a boolean flag that determines whether to use the CUDA API’s cudaHostRegister function for allocating pinned memory instead of the default cudaHostAlloc. When set to True, the memory is allocated using regular malloc and then pages are mapped to the memory before calling cudaHostRegister. This pre-mapping of pages helps reduce the lock time during the execution of cudaHostRegister.
    
*   `pinned_num_register_threads` option is only valid when pinned\_use\_cuda\_host\_register is set to True. By default, one thread is used to map the pages. This option allows using more threads to parallelize the page mapping operations to reduce the overall allocation time of pinned memory. A good value for this option is 8 based on benchmarking results.
    
*   `pinned_use_background_threads` option is a boolean flag to enable background thread for processing events. This avoids any slow path associated with querying/processing of events in the fast allocation path. This feature is disabled by default.
    
*   `pinned_reserve_segment_size_mb` option is a size in MB to reserve for pinned memory segment. This allocates a large segment of pinned memory upfront and then uses to allocate small size requests. This helps reduce the number of expensive device library calls.
    
*   `pinned_max_round_threshold_mb` option sets the maximum allocation size (in MB) that will be rounded up to the nearest power-of-2. Allocations larger than this threshold will use their exact requested size, which can reduce memory waste for large pinned memory allocations. For example, with a threshold of 128 MB, a 129 MB allocation will use 129 MB instead of being rounded to 256 MB. By default, this option is disabled. Allocations that exceed `pinned_max_cached_size_mb` are never rounded up, regardless of this setting, since rounding is only useful for cached blocks.
    
*   `pinned_max_cached_size_mb` option sets the maximum block size (in MB) that will be cached in the free list for reuse. Blocks larger than this threshold will not be rounded up to power-of-2 and will be freed immediately when no longer in use, rather than being cached. This can help reduce peak memory usage for workloads with large pinned memory allocations that are used infrequently. By default, this option is disabled (all blocks are cached).
    
*   `graph_capture_record_stream_reuse` (experimental, default: `False`) If set to `True`, the CUDA caching allocator will attempt to reclaim device memory during CUDA Graph capture by using the graph topology (instead of CUDA events) to determine when a freed block is safe to reuse. This can reduce peak memory during long captures that free and reallocate buffers across multiple streams, especially when the capture DAG frequently reaches joined frontiers.
    
*   `per_process_memory_fraction` option limits the amount of memory that can be allocated on all the CUDA devices to a specified fraction of the available memory. This is a value between 0 and 1. Attempting to allocate more memory will raise an out of memory error.
    
*   `throw_on_cudamalloc_oom` (default: `False`) When set to `True`, the allocator will preemptively reject allocations that would exceed the `per_process_memory_fraction` limit by throwing an `OutOfMemoryError` instead of attempting the allocation through the driver, which could trigger a fatal GPU runtime abort (e.g., `HSA_STATUS_ERROR_OUT_OF_RESOURCES` on ROCm). The rejected allocation skips the retry chain and throws immediately, allowing the caller to catch the exception and handle it gracefully.
    
    Example configuration:
    

PYTORCH\_CUDA\_ALLOC\_CONF\=per\_process\_memory\_fraction:0.95,throw\_on\_cudamalloc\_oom:True

Copy to clipboard

This is particularly useful for inference serving, where a fatal GPU OOM would crash the server process. With this option, the serving framework can catch the `OutOfMemoryError` and reject the individual request while continuing to serve subsequent requests.

Note

Some stats reported by the
{ref}\`CUDA memory management API<cuda-memory-management-api>\`
are specific to \`backend:native\`, and are not meaningful with
\`backend:cudaMallocAsync\`.
See each function's docstring for details.

Copy to clipboard

Using custom memory allocators for CUDA[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#using-custom-memory-allocators-for-cuda "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

It is possible to define allocators as simple functions in C/C++ and compile them as a shared library, the code below shows a basic allocator that just traces all the memory operations.

#include <sys/types.h>
#include <cuda\_runtime\_api.h>
#include <iostream>
// Compile with g++ alloc.cc -o alloc.so -I/usr/local/cuda/include -shared -fPIC
extern "C" {
void\* my\_malloc(ssize\_t size, int device, cudaStream\_t stream) {
   void \*ptr;
   cudaMalloc(&ptr, size);
   std::cout<<"alloc "<<ptr<<size<<std::endl;
   return ptr;
}

void my\_free(void\* ptr, ssize\_t size, int device, cudaStream\_t stream) {
   std::cout<<"free "<<ptr<< " "<<stream<<std::endl;
   cudaFree(ptr);
}
}

Copy to clipboard

This can be used in python through the [`torch.cuda.memory.CUDAPluggableAllocator`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.CUDAPluggableAllocator.html#torch.cuda.memory.CUDAPluggableAllocator "torch.cuda.memory.CUDAPluggableAllocator")
. The user is responsible for supplying the path to the `.so` file and the name of the alloc/free functions that match the signatures specified above.

import torch

\# Load the allocator
new\_alloc \= torch.cuda.memory.CUDAPluggableAllocator(
    'alloc.so', 'my\_malloc', 'my\_free')
\# Swap the current allocator
torch.cuda.memory.change\_current\_allocator(new\_alloc)
\# This will allocate memory in the device using the new allocator
b \= torch.zeros(10, device\='cuda')

Copy to clipboard

import torch

\# Do an initial memory allocator
b \= torch.zeros(10, device\='cuda')
\# Load the allocator
new\_alloc \= torch.cuda.memory.CUDAPluggableAllocator(
    'alloc.so', 'my\_malloc', 'my\_free')
\# This will error since the current allocator was already instantiated
torch.cuda.memory.change\_current\_allocator(new\_alloc)

Copy to clipboard

Mixing different CUDA system allocators in the same program[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#mixing-different-cuda-system-allocators-in-the-same-program "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Depending on your use case, `change_current_allocator()` may not be what you want to use, since it swaps the CUDA allocator for the entire program (similar to `PYTORCH_ALLOC_CONF=backend:cudaMallocAsync`). For instance, if the swapped allocator doesn’t have caching mechanism, you will lose all the benefits of PyTorch’s CUDACachingAllocator. Instead, you can selectively mark a region of PyTorch code to use a custom allocator using `torch.cuda.MemPool`. This will let you use multiple CUDA system allocators in the same PyTorch program, along with most of the benefits of the CUDACachingAllocator (e.g. caching). Using `torch.cuda.MemPool`, you can utilize custom allocators that enable several features, such as:

*   Allocating output buffers for an all-reduce using `ncclMemAlloc` allocator can enable NVLink Switch Reductions (NVLS). This can reduce contention between overlapping compute and communication kernels on GPU resources (SMs, and Copy Engines), especially on tensor-parallel workloads.
    
*   For Grace CPU based systems, allocating host outputs buffers for an all-gather using `cuMemCreate` and specifying `CU_MEM_LOCATION_TYPE_HOST_NUMA` can enable Extended GPU Memory (EGM) based memory transfers from source GPUs to the destination CPU. This accelerates the all-gather since the transfer happens over NVLinks, which otherwise would have happened over bandwidth-limited, Network Interface Card (NIC) links. Such an accelerated all-gather can in turn speed up model checkpointing.
    
*   If you are crafting a model and don’t want to think about the optimal memory placements of a memory intensive module at first (e.g. an embedding table), or perhaps you have a module which is not performance sensitive and doesn’t fit in the GPU, then you could just allocate that module with `cudaMallocManaged` with preferred CPU location and get your model working first.
    

Note

While \`cudaMallocManaged\` offers convenient automatic memory management using CUDA Unified Virtual Memory (UVM),
it is not recommended for DL workloads. For DL workloads that fit in GPU memory, explicit placement consistently
outperforms UVM, since there are no page faults and access patterns remain predictable. When GPU memory gets
saturated, UVM has to perform costly double transfers, evicting pages to CPU before bringing in new ones.

Copy to clipboard

The code below shows `ncclMemAlloc` wrapped in a [`torch.cuda.memory.CUDAPluggableAllocator`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.memory.CUDAPluggableAllocator.html#torch.cuda.memory.CUDAPluggableAllocator "torch.cuda.memory.CUDAPluggableAllocator")
.

import os

import torch
import torch.distributed as dist
from torch.cuda.memory import CUDAPluggableAllocator
from torch.distributed.distributed\_c10d import \_get\_default\_group
from torch.utils import cpp\_extension

\# create allocator
nccl\_allocator\_source \= """
#include <nccl.h>
#include <iostream>
extern "C" {

void\* nccl\_alloc\_plug(size\_t size, int device, void\* stream) {
  std::cout << "Using ncclMemAlloc" << std::endl;
  void\* ptr;
  ncclResult\_t err = ncclMemAlloc(&ptr, size);
  return ptr;

}

void nccl\_free\_plug(void\* ptr, size\_t size, int device, void\* stream) {
  std::cout << "Using ncclMemFree" << std::endl;
  ncclResult\_t err = ncclMemFree(ptr);
}

}
"""
nccl\_allocator\_libname \= "nccl\_allocator"
nccl\_allocator \= torch.utils.cpp\_extension.load\_inline(
    name\=nccl\_allocator\_libname,
    cpp\_sources\=nccl\_allocator\_source,
    with\_cuda\=True,
    extra\_ldflags\=\["-lnccl"\],
    verbose\=True,
    is\_python\_module\=False,
    build\_directory\="./",
)

allocator \= CUDAPluggableAllocator(
    f"./{nccl\_allocator\_libname}.so", "nccl\_alloc\_plug", "nccl\_free\_plug"
).allocator()

\# setup distributed
rank \= int(os.getenv("RANK"))
local\_rank \= int(os.getenv("LOCAL\_RANK"))
world\_size \= int(os.getenv("WORLD\_SIZE"))
torch.cuda.set\_device(local\_rank)
dist.init\_process\_group(backend\="nccl")
device \= torch.device(f"cuda:{local\_rank}")
default\_pg \= \_get\_default\_group()
backend \= default\_pg.\_get\_backend(device)

\# Note: for convenience, ProcessGroupNCCL backend provides
\# the ncclMemAlloc allocator as backend.mem\_allocator
allocator \= backend.mem\_allocator

Copy to clipboard

You can now define a new memory pool by passing this allocator to `torch.cuda.MemPool`:

pool \= torch.cuda.MemPool(allocator)

Copy to clipboard

The pool can then be used with the [`torch.cuda.use_mem_pool`](https://docs.pytorch.org/docs/2.15/cuda.html#torch.cuda.use_mem_pool "torch.cuda.use_mem_pool")
 context manager to allocate tensors into that pool:

with torch.cuda.use\_mem\_pool(pool):
    \# tensor gets allocated with ncclMemAlloc passed in the pool
    tensor \= torch.arange(1024 \* 1024 \* 2, device\=device)
    print(f"tensor ptr on rank {rank} is {hex(tensor.data\_ptr())}")

\# register user buffers using ncclCommRegister (called under the hood)
backend.register\_mem\_pool(pool)

\# Collective uses Zero Copy NVLS
dist.all\_reduce(tensor\[0:4\])
torch.cuda.synchronize()
print(tensor\[0:4\])

Copy to clipboard

Note the usage of `register_mem_pool` in the above example. This is an extra step for NVLS reductions, where the user buffers need to be registered with NCCL. A user can de-register the buffers with a similar `deregister_mem_pool` call.

To reclaim memory, users will first need to ensure nothing is using the pool. When none of the tensors are holding a reference to the pool, `empty_cache()` will be called internally on deletion of the pool, hence returning all the memory to the system.

del tensor, del pool

Copy to clipboard

Users can optionally specify a `use_on_oom` bool (which is False by default) during MemPool creation. If true, then the CUDACachingAllocator will be able to use memory in this pool as a last resort instead of OOMing.

pool \= torch.cuda.MemPool(allocator, use\_on\_oom\=True)
with torch.cuda.use\_mem\_pool(pool):
    a \= torch.randn(40 \* 1024 \* 1024, dtype\=torch.uint8, device\="cuda")
del a

\# at the memory limit, this will succeed by using pool's memory in order to avoid the oom
b \= torch.randn(40 \* 1024 \* 1024, dtype\=torch.uint8, device\="cuda")

Copy to clipboard

The following `torch.cuda.MemPool.use_count()` and `torch.cuda.MemPool.snapshot()` APIs can be used for debugging purposes:

pool \= torch.cuda.MemPool(allocator)

\# pool's use count should be 1 at this point as MemPool object
\# holds a reference
assert pool.use\_count() \== 1

nelem\_1mb \= 1024 \* 1024 // 4

with torch.cuda.use\_mem\_pool(pool):
    out\_0 \= torch.randn(nelem\_1mb, device\="cuda")

    \# pool's use count should be 2 at this point as use\_mem\_pool
    \# holds a reference
    assert pool.use\_count() \== 2

\# pool's use count should be back to 1 at this point as use\_mem\_pool
\# released its reference
assert pool.use\_count() \== 1

with torch.cuda.use\_mem\_pool(pool):
    \# pool should have 1 segment since we made a small allocation (1 MB)
    \# above and so the CUDACachingAllocator packed it into a 2 MB buffer
    assert len(pool.snapshot()) \== 1

    out\_1 \= torch.randn(nelem\_1mb, device\="cuda")

    \# pool should still have 1 segment since we made another small allocation
    \# (1 MB) that got packed into the existing 2 MB buffer
    assert len(pool.snapshot()) \== 1

    out\_2 \= torch.randn(nelem\_1mb, device\="cuda")

    \# pool now should have 2 segments since the CUDACachingAllocator had
    \# to make a new 2 MB buffer to accommodate out\_2
    assert len(pool.snapshot()) \== 2

Copy to clipboard

Note

*   `torch.cuda.MemPool` holds a reference to the pool. When you use the [`torch.cuda.use_mem_pool`](https://docs.pytorch.org/docs/2.15/cuda.html#torch.cuda.use_mem_pool "torch.cuda.use_mem_pool")
     context manager, it will also acquire another reference to the pool. On exit of the context manager, it will release its reference. After that, ideally it should only be tensors holding references to the pool. Once the tensors release their references, the use count of the pool will be 1, reflecting that only the `torch.cuda.MemPool` object is holding a reference. Only at that point, can the memory held by the pool be returned to the system when the pool’s destructor is called using `del`.
    
*   [NCCL has specific requirements](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/bufferreg.html#memory-allocator)
     for a buffer to be compatible with NVLS reductions. These requirements can be broken in a dynamic workload, for instance, the buffer being sent to NCCL by the CUDACachingAllocator might be split and hence, not correctly aligned. In those cases, NCCL can use a fallback algorithm instead of NVLS.
    
*   Allocators like `ncclMemAlloc` can use more memory than requested, due to alignment requirements (`CU_MULTICAST_GRANULARITY_RECOMMENDED`, `CU_MULTICAST_GRANULARITY_MINIMUM`), and can cause your workload to run out of memory.
    

Tuning NVLink Performance with Custom Memory Allocator on H100/H200 GPUs[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#tuning-nvlink-performance-with-custom-memory-allocator-on-h100-h200-gpus "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In rare cases, performance of NVLink on H100/H200 GPUs can be influenced by the physical memory layout of data, creating an opportunity for developers to tune their applications for optimal throughput.

An example of how physical memory layout of data affects performance is when communication kernels issue unbalanced NVLink read/write operations. In the following figure, we can see that each warp accesses memory addresses with a consistent strided pattern in each single wave. We can have a more balanced load by tuning the stride size in the workload or we can implement a custom CUDA allocator.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_      \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
| Warp 0 Reading | No\-reading |  | Warp 1 Reading | No\-reading |  ...  Warp N Reading | No\-reading |
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_      \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
<----------------------------->
        Stride size

Copy to clipboard

Such an allocator can maintain contiguous virtual memory addresses for the kernel while strategically arranging the mapping to physical memory addresses (e.g., through shuffling). This technique allows developers to explore different physical access patterns to find the most efficient one, unlocking higher performance without modifying the kernel’s logic. A practical implementation of such an allocator can be achieved using PyTorch’s custom allocator support as mentioned before, where the malloc and free functions are:

// assuming a system with 8 GPUs
struct CustomAllocInfo {
  void\*\* devPtr;  // This will be the usable virtual memory address
  CUdeviceptr dptr;
  size\_t totalSize;  // Total size of the allocated memory
  size\_t padded\_size;
  int device\_id;
  std::vector<CUmemGenericAllocationHandle\> handles;  // Handles to physical memory allocations
};

// loop over pages
cudaError\_t customCudaMalloc(CustomAllocInfo\* info) {
    if (!info) return cudaErrorInvalidValue;

    CUdeviceptr dptr;

    // Handles to redundant physical memory allocations which help truncate stride pattern in physical memory
    std::vector<CUmemGenericAllocationHandle\> handles\_redundant;

    size\_t granularity \= 0;
    CUmemAllocationProp prop \= {};

    int currentDev \= info\->device\_id;
    size\_t totalSize \= info\->totalSize;

    prop.type \= CU\_MEM\_ALLOCATION\_TYPE\_PINNED;
    prop.location.type \= CU\_MEM\_LOCATION\_TYPE\_DEVICE;
    prop.location.id \= currentDev;
    cuMemGetAllocationGranularity(&granularity, &prop, CU\_MEM\_ALLOC\_GRANULARITY\_MINIMUM);
    size\_t padded\_size \= ROUND\_UP(totalSize, granularity);

    info\->padded\_size \= padded\_size;

    // loop over pages
    size\_t iter\_granularity \= granularity \* 64; // 64 \* granularity with shift\_size = 2 works
    uint32\_t iteration\_count \= (totalSize + iter\_granularity \- 1) / iter\_granularity;

    cuMemAddressReserve(&dptr, padded\_size, 0ULL, 0ULL, 0ULL);

    const int shift\_size \= 2;
    for (size\_t i \= 0; i < iteration\_count; i+=shift\_size) {

        CUmemGenericAllocationHandle allocHandle\[shift\_size\];
        for (int shift \= 0; (shift < shift\_size)&&(i+shift < iteration\_count); shift++){
            CHECK\_CUDA(cuMemCreate(&allocHandle\[shift\], iter\_granularity, &prop, 0));
            info\->handles.push\_back(allocHandle\[shift\]);
        }

        for (int shift \= 0; (shift < shift\_size)&&(i+shift < iteration\_count); shift++){

            // mapping makes the shift (shift -> (shift+1)%shift\_size  )
            CHECK\_CUDA(cuMemMap(dptr + (i+shift) \* iter\_granularity, iter\_granularity, 0, allocHandle\[(shift+1)%shift\_size\], 0));

            setupMultiGPUAccess(dptr + (i+shift) \* iter\_granularity, iter\_granularity, {0, 1, 2, 3, 4, 5, 6, 7}); // Enable access for all 8 GPUs
        }

        // std::cout << "Here we allocate one redundant page (2MB)..." << std::endl;
        // this is an extra optimization on top of the swizzling. It helps "break"
        // the physical access pattern even more. It can be left out if workload is already
        // performing at SOL with just swizzling.
        CUmemGenericAllocationHandle allocHandle\_redundant;
        CHECK\_CUDA(cuMemCreate(&allocHandle\_redundant, granularity, &prop, 0));
        handles\_redundant.push\_back(allocHandle\_redundant);
    }

    \*info\->devPtr \= (void\*)dptr;
    info\->dptr \= dptr;

    // Release each redundant allocation
    for (auto handle : handles\_redundant) {
        // std::cout << "Here we release one redundant page (2MB)..." << std::endl;
        CHECK\_CUDA(cuMemRelease(handle));
    }

    return cudaSuccess;
}

void customCudaFree(CustomAllocInfo\* info) {
    if (!info) return;

    // CHECK\_CUDA(cudaSetDevice(info->device\_id));

    CHECK\_CUDA(cuMemUnmap(info\->dptr, info\->padded\_size));

    // Unmap and release each allocation
    for (auto handle : info\->handles) {
        CHECK\_CUDA(cuMemRelease(handle));
    }

    // Unreserve the virtual address space
    // CHECK\_CUDA(cuMemAddressFree((CUdeviceptr)\*info->devPtr, info->padded\_size));
    CHECK\_CUDA(cuMemAddressFree(info\->dptr, info\->padded\_size));
}

Copy to clipboard

cuBLAS workspaces[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#cublas-workspaces "Link to this heading")

------------------------------------------------------------------------------------------------------------------

By default, ATen allocates a cuBLAS workspace for each operation from the CUDA caching allocator and releases it when the operation returns. Set `TORCH_CUBLAS_WORKSPACE_CACHE=1` to instead retain one workspace for each cuBLAS handle and CUDA stream until `torch._C._cuda_clearCublasWorkspaces()` is called. Persistent workspaces must not be used when capturing multiple CUDA graphs on the same stream. Handles returned by `torch.cuda.current_blas_handle()` use cuBLAS’s default workspace when ATen workspace caching is disabled.

The workspace size per allocation can be specified via `CUBLAS_WORKSPACE_CONFIG` with the format `:[SIZE]:[COUNT]`. For example, `CUBLAS_WORKSPACE_CONFIG=:4096:2:16:8` specifies a total size of `2 * 4096 + 8 * 16 KiB`. To force cuBLAS to avoid using workspaces, set `CUBLAS_WORKSPACE_CONFIG=:0:0`.

cuFFT plan cache[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#cufft-plan-cache "Link to this heading")

----------------------------------------------------------------------------------------------------------------

For each CUDA device, an LRU cache of cuFFT plans is used to speed up repeatedly running FFT methods (e.g., [`torch.fft.fft()`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.fft.html#torch.fft.fft "torch.fft.fft")
) on CUDA tensors of same geometry with same configuration. Because some cuFFT plans may allocate GPU memory, these caches have a maximum capacity.

You may control and query the properties of the cache of current device with the following APIs:

*   `torch.backends.cuda.cufft_plan_cache.max_size` gives the capacity of the cache (default is 4096 on CUDA 10 and newer, and 1023 on older CUDA versions). Setting this value directly modifies the capacity.
    
*   `torch.backends.cuda.cufft_plan_cache.size` gives the number of plans currently residing in the cache.
    
*   `torch.backends.cuda.cufft_plan_cache.clear()` clears the cache.
    

To control and query plan caches of a non-default device, you can index the `torch.backends.cuda.cufft_plan_cache` object with either a [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
 object or a device index, and access one of the above attributes. E.g., to set the capacity of the cache for device `1`, one can write `torch.backends.cuda.cufft_plan_cache[1].max_size = 10`.

Just-in-Time Compilation[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#just-in-time-compilation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

PyTorch just-in-time compiles some operations, like torch.special.zeta, when performed on CUDA tensors. This compilation can be time consuming (up to a few seconds depending on your hardware and software) and may occur multiple times for a single operator since many PyTorch operators actually select from a variety of kernels, each of which must be compiled once, depending on their input. This compilation occurs once per process, or just once if a kernel cache is used.

By default, PyTorch creates a kernel cache in $XDG\_CACHE\_HOME/torch/kernels if XDG\_CACHE\_HOME is defined and $HOME/.cache/torch/kernels if it’s not (except on Windows, where the kernel cache is not yet supported). The caching behavior can be directly controlled with two environment variables. If USE\_PYTORCH\_KERNEL\_CACHE is set to 0 then no cache will be used, and if PYTORCH\_KERNEL\_CACHE\_PATH is set then that path will be used as a kernel cache instead of the default location.

Best practices[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#best-practices "Link to this heading")

------------------------------------------------------------------------------------------------------------

### Device-agnostic code[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#device-agnostic-code "Link to this heading")

Due to the structure of PyTorch, you may need to explicitly write device-agnostic (CPU or GPU) code; an example may be creating a new tensor as the initial hidden state of a recurrent neural network.

The first step is to determine whether the GPU should be used or not. A common pattern is to use Python’s `argparse` module to read in user arguments, and have a flag that can be used to disable CUDA, in combination with [`is_available()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.is_available.html#torch.cuda.is_available "torch.cuda.is_available")
. In the following, `args.device` results in a [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
 object that can be used to move tensors to CPU or CUDA.

import argparse
import torch

parser \= argparse.ArgumentParser(description\='PyTorch Example')
parser.add\_argument('--disable-cuda', action\='store\_true',
                    help\='Disable CUDA')
args \= parser.parse\_args()
args.device \= None
if not args.disable\_cuda and torch.cuda.is\_available():
    args.device \= torch.device('cuda')
else:
    args.device \= torch.device('cpu')

Copy to clipboard

Note

When assessing the availability of CUDA in a given environment ({meth}\`~torch.cuda.is\_available\`), PyTorch's default
behavior is to call the CUDA Runtime API method \[cudaGetDeviceCount\](https://docs.nvidia.com/cuda/cuda-runtime-api/group\_\_CUDART\_\_DEVICE.html#group\_\_CUDART\_\_DEVICE\_1g18808e54893cfcaafefeab31a73cc55f). Because this call in turn initializes the
CUDA Driver API (via \[cuInit\](https://docs.nvidia.com/cuda/cuda-driver-api/group\_\_CUDA\_\_INITIALIZE.html#group\_\_CUDA\_\_INITIALIZE\_1g0a2f1517e1bd8502c7194c3a8c134bc3)) if it is not already initialized, subsequent forks of a process that has run
{meth}\`~torch.cuda.is\_available\` will fail with a CUDA initialization error.

One can set \`PYTORCH\_NVML\_BASED\_CUDA\_CHECK=1\` in your environment before importing PyTorch modules that execute
{meth}\`~torch.cuda.is\_available\` (or before executing it directly) in order to direct
{meth}\`~torch.cuda.is\_available\` to attempt an NVML-based assessment (\[nvmlDeviceGetCount\_v2\](https://docs.nvidia.com/deploy/nvml-api/group\_\_nvmlDeviceQueries.html#group\_\_nvmlDeviceQueries\_1ga93623b195bff04bbe3490ca33c8a42d)). If the
NVML-based assessment is successful (i.e. NVML discovery/initialization does not fail),
{meth}\`~torch.cuda.is\_available\` calls will not poison subsequent forks.

If NVML discovery/initialization fails, {meth}\`~torch.cuda.is\_available\` will fallback to the standard CUDA Runtime
API assessment and the aforementioned fork constraint will apply.

Note that the above NVML-based CUDA availability assessment provides a weaker guarantee than the default CUDA
Runtime API approach (which requires CUDA initialization to succeed). In some circumstances, the NVML-based check
may succeed while later CUDA initialization fails.

Copy to clipboard

Now that we have `args.device`, we can use it to create a Tensor on the desired device.

x \= torch.empty((8, 42), device\=args.device)
net \= Network().to(device\=args.device)

Copy to clipboard

This can be used in a number of cases to produce device agnostic code. Below is an example when using a dataloader:

cuda0 \= torch.device('cuda:0')  \# CUDA GPU 0
for i, x in enumerate(train\_loader):
    x \= x.to(cuda0)

Copy to clipboard

When working with multiple GPUs on a system, you can use the `CUDA_VISIBLE_DEVICES` environment flag to manage which GPUs are available to PyTorch. As mentioned above, to manually control which GPU a tensor is created on, the best practice is to use a [`torch.cuda.device`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.device.html#torch.cuda.device "torch.cuda.device")
 context manager.

print("Outside device is 0")  \# On device 0 (default in most scenarios)
with torch.cuda.device(1):
    print("Inside device is 1")  \# On device 1
print("Outside device is still 0")  \# On device 0

Copy to clipboard

If you have a tensor and would like to create a new tensor of the same type on the same device, then you can use a `torch.Tensor.new_*` method (see [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
). Whilst the previously mentioned `torch.*` factory functions ([Creation Ops](https://docs.pytorch.org/docs/2.15/torch.html#tensor-creation-ops)
) depend on the current GPU context and the attributes arguments you pass in, `torch.Tensor.new_*` methods preserve the device and other attributes of the tensor.

This is the recommended practice when creating modules in which new tensors need to be created internally during the forward pass.

cuda \= torch.device('cuda')
x\_cpu \= torch.empty(2)
x\_gpu \= torch.empty(2, device\=cuda)
x\_cpu\_long \= torch.empty(2, dtype\=torch.int64)

y\_cpu \= x\_cpu.new\_full(\[3, 2\], fill\_value\=0.3)
print(y\_cpu)

    tensor(\[\[ 0.3000,  0.3000\],\
            \[ 0.3000,  0.3000\],\
            \[ 0.3000,  0.3000\]\])

y\_gpu \= x\_gpu.new\_full(\[3, 2\], fill\_value\=-5)
print(y\_gpu)

    tensor(\[\[\-5.0000, \-5.0000\],\
            \[\-5.0000, \-5.0000\],\
            \[\-5.0000, \-5.0000\]\], device\='cuda:0')

y\_cpu\_long \= x\_cpu\_long.new\_tensor(\[\[1, 2, 3\]\])
print(y\_cpu\_long)

    tensor(\[\[ 1,  2,  3\]\])

Copy to clipboard

If you want to create a tensor of the same type and size of another tensor, and fill it with either ones or zeros, [`ones_like()`](https://docs.pytorch.org/docs/2.15/generated/torch.ones_like.html#torch.ones_like "torch.ones_like")
 or [`zeros_like()`](https://docs.pytorch.org/docs/2.15/generated/torch.zeros_like.html#torch.zeros_like "torch.zeros_like")
 are provided as convenient helper functions (which also preserve [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
 and [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 of a Tensor).

x\_cpu \= torch.empty(2, 3)
x\_gpu \= torch.empty(2, 3)

y\_cpu \= torch.ones\_like(x\_cpu)
y\_gpu \= torch.zeros\_like(x\_gpu)

Copy to clipboard

### Use pinned memory buffers[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#use-pinned-memory-buffers "Link to this heading")

Warning

This is an advanced tip. If you overuse pinned memory, it can cause serious
problems when running low on RAM, and you should be aware that pinning is
often an expensive operation.

Copy to clipboard

Host to GPU copies are much faster when they originate from pinned (page-locked) memory. CPU tensors and storages expose a [`pin_memory()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.pin_memory.html#torch.Tensor.pin_memory "torch.Tensor.pin_memory")
 method, that returns a copy of the object, with data put in a pinned region.

Also, once you pin a tensor or storage, you can use asynchronous GPU copies. Just pass an additional `non_blocking=True` argument to a [`to()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.to.html#torch.Tensor.to "torch.Tensor.to")
 or a [`cuda()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.cuda.html#torch.Tensor.cuda "torch.Tensor.cuda")
 call. This can be used to overlap data transfers with computation.

You can make the [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
 return batches placed in pinned memory by passing `pin_memory=True` to its constructor.

### Use nn.parallel.DistributedDataParallel instead of multiprocessing or nn.DataParallel[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#use-nn-parallel-distributeddataparallel-instead-of-multiprocessing-or-nn-dataparallel "Link to this heading")

Most use cases involving batched inputs and multiple GPUs should default to using [`DistributedDataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
 to utilize more than one GPU.

There are significant caveats to using CUDA models with [`multiprocessing`](https://docs.pytorch.org/docs/2.15/multiprocessing.html#module-torch.multiprocessing "torch.multiprocessing")
; unless care is taken to meet the data handling requirements exactly, it is likely that your program will have incorrect or undefined behavior.

It is recommended to use [`DistributedDataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
, instead of [`DataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.DataParallel.html#torch.nn.DataParallel "torch.nn.DataParallel")
 to do multi-GPU training, even if there is only a single node.

The difference between [`DistributedDataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
 and [`DataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.DataParallel.html#torch.nn.DataParallel "torch.nn.DataParallel")
 is: [`DistributedDataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
 uses multiprocessing where a process is created for each GPU, while [`DataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.DataParallel.html#torch.nn.DataParallel "torch.nn.DataParallel")
 uses multithreading. By using multiprocessing, each GPU has its dedicated process, this avoids the performance overhead caused by GIL of Python interpreter.

If you use [`DistributedDataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
, you could use `torch.distributed.launch` utility to launch your program, see [Launch utility](https://docs.pytorch.org/docs/2.15/distributed.html#distributed-launch)
.

CUDA Graphs[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#cuda-graphs "Link to this heading")

------------------------------------------------------------------------------------------------------

A CUDA graph is a record of the work (mostly kernels and their arguments) that a CUDA stream and its dependent streams perform. For general principles and details on the underlying CUDA API, see [Getting Started with CUDA Graphs](https://developer.nvidia.com/blog/cuda-graphs/)
 and the [Graphs section](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#cuda-graphs)
 of the CUDA C Programming Guide.

PyTorch supports the construction of CUDA graphs using [stream capture](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#creating-a-graph-using-stream-capture)
, which puts a CUDA stream in _capture mode_. CUDA work issued to a capturing stream doesn’t actually run on the GPU. Instead, the work is recorded in a graph.

After capture, the graph can be _launched_ to run the GPU work as many times as needed. Each replay runs the same kernels with the same arguments. For pointer arguments this means the same memory addresses are used. By filling input memory with new data (e.g., from a new batch) before each replay, you can rerun the same work on new data.

### Why CUDA Graphs?[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#why-cuda-graphs "Link to this heading")

Replaying a graph sacrifices the dynamic flexibility of typical eager execution in exchange for **greatly reduced CPU overhead**. A graph’s arguments and kernels are fixed, so a graph replay skips all layers of argument setup and kernel dispatch, including Python, C++, and CUDA driver overheads. Under the hood, a replay submits the entire graph’s work to the GPU with a single call to [cudaGraphLaunch](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__GRAPH.html#group__CUDART__GRAPH_1g1accfe1da0c605a577c22d9751a09597)
. Kernels in a replay also execute slightly faster on the GPU, but eliding CPU overhead is the main benefit.

You should try CUDA graphs if all or part of your network is graph-safe (usually this means static shapes and static control flow, but see the other [constraints](https://docs.pytorch.org/docs/2.15/notes/cuda.html#capture-constraints)
) and you suspect its runtime is at least somewhat CPU-limited.

### PyTorch API[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#pytorch-api "Link to this heading")

Warning

This API is in beta and may change in future releases.

Copy to clipboard

PyTorch exposes graphs via a raw [`torch.cuda.CUDAGraph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph "torch.cuda.CUDAGraph")
 class and two convenience wrappers, [`torch.cuda.graph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph.html#torch.cuda.graph "torch.cuda.graph")
 and [`torch.cuda.make_graphed_callables`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables "torch.cuda.make_graphed_callables")
.

[`torch.cuda.graph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph.html#torch.cuda.graph "torch.cuda.graph")
 is a simple, versatile context manager that captures CUDA work in its context. Before capture, warm up the workload to be captured by running a few eager iterations. Warmup must occur on a side stream. Because the graph reads from and writes to the same memory addresses in every replay, you must maintain long-lived references to tensors that hold input and output data during capture. To run the graph on new input data, copy new data to the capture’s input tensor(s), replay the graph, then read the new output from the capture’s output tensor(s). Example:

g \= torch.cuda.CUDAGraph()

\# Placeholder input used for capture
static\_input \= torch.empty((5,), device\="cuda")

\# Warmup before capture
s \= torch.cuda.Stream()
s.wait\_stream(torch.cuda.current\_stream())
with torch.cuda.stream(s):
    for \_ in range(3):
        static\_output \= static\_input \* 2
torch.cuda.current\_stream().wait\_stream(s)

\# Captures the graph
\# To allow capture, automatically sets a side stream as the current stream in the context
with torch.cuda.graph(g):
    static\_output \= static\_input \* 2

\# Fills the graph's input memory with new data to compute on
static\_input.copy\_(torch.full((5,), 3, device\="cuda"))
g.replay()
\# static\_output holds the results
print(static\_output)  \# full of 3 \* 2 = 6

\# Fills the graph's input memory with more data to compute on
static\_input.copy\_(torch.full((5,), 4, device\="cuda"))
g.replay()
print(static\_output)  \# full of 4 \* 2 = 8

Copy to clipboard

See [Whole-network capture](https://docs.pytorch.org/docs/2.15/notes/cuda.html#whole-network-capture)
, [Usage with torch.cuda.amp](https://docs.pytorch.org/docs/2.15/notes/cuda.html#graphs-with-amp)
, and [Usage with multiple streams](https://docs.pytorch.org/docs/2.15/notes/cuda.html#multistream-capture)
 for realistic and advanced patterns.

[`make_graphed_callables`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables "torch.cuda.make_graphed_callables")
 is more sophisticated. [`make_graphed_callables`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables "torch.cuda.make_graphed_callables")
 accepts Python functions and [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
\\s. For each passed function or Module, it creates separate graphs of the forward-pass and backward-pass work. See [Partial-network capture](https://docs.pytorch.org/docs/2.15/notes/cuda.html#partial-network-capture)
.

#### Constraints[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#constraints "Link to this heading")

A set of ops is _capturable_ if it doesn’t violate any of the following constraints.

Constraints apply to all work in a [`torch.cuda.graph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph.html#torch.cuda.graph "torch.cuda.graph")
 context and all work in the forward and backward passes of any callable you pass to [`torch.cuda.make_graphed_callables()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables "torch.cuda.make_graphed_callables")
.

Violating any of these will likely cause a runtime error:

*   Capture must occur on a non-default stream. (This is only a concern if you use the raw [`CUDAGraph.capture_begin`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph.capture_begin "torch.cuda.CUDAGraph.capture_begin")
     and [`CUDAGraph.capture_end`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph.capture_end "torch.cuda.CUDAGraph.capture_end")
     calls. [`graph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph.html#torch.cuda.graph "torch.cuda.graph")
     and [`make_graphed_callables()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables "torch.cuda.make_graphed_callables")
     set a side stream for you.)
    
*   Ops that synchronize the CPU with the GPU (e.g., `.item()` calls) are prohibited.
    
*   CUDA RNG operations are permitted, and when using multiple [`torch.Generator`](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")
     instances within a graph, Avoid using `Generator.get_state` and `Generator.set_state` during capture; instead, utilize [`Generator.graphsafe_set_state`](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator.graphsafe_set_state "torch.Generator.graphsafe_set_state")
     and [`Generator.graphsafe_get_state`](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator.graphsafe_get_state "torch.Generator.graphsafe_get_state")
     for managing generator states safely within the graph context. This ensures proper RNG operation and generator management within CUDA graphs.
    
*   Dynamic control flow (based on CPU or GPU data) is prohibited, unless it is based on GPU data and implemented via higher order operator torch.cond(). See [Data Dependent Control Flow](https://docs.pytorch.org/docs/2.15/notes/cuda.html#graph-data-dependent-control-flow)
    .
    

Violating any of these will likely cause silent numerical errors or undefined behavior:

*   Within a process, only one capture may be underway at a time.
    
*   No non-captured CUDA work may run in this process (on any thread) while capture is underway.
    
*   CPU work is not captured. If the captured ops include CPU work, that work will be elided during replay.
    
*   Every replay reads from and writes to the same (virtual) memory addresses.
    
*   Dynamic shapes are prohibited. The graph assumes every tensor in the captured op sequence has the same size and layout in every replay.
    
*   Using multiple streams in a capture is allowed, but there are [restrictions](https://docs.pytorch.org/docs/2.15/notes/cuda.html#multistream-capture)
    .
    

#### Non-constraints[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#non-constraints "Link to this heading")

*   Once captured, the graph may be replayed on any stream.
    

### Whole-network capture[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#whole-network-capture "Link to this heading")

If your entire network is capturable, you can capture and replay an entire iteration:

N, D\_in, H, D\_out \= 640, 4096, 2048, 1024
model \= torch.nn.Sequential(torch.nn.Linear(D\_in, H),
                            torch.nn.Dropout(p\=0.2),
                            torch.nn.Linear(H, D\_out),
                            torch.nn.Dropout(p\=0.1)).cuda()
loss\_fn \= torch.nn.MSELoss()
optimizer \= torch.optim.SGD(model.parameters(), lr\=0.1)

\# Placeholders used for capture
static\_input \= torch.randn(N, D\_in, device\='cuda')
static\_target \= torch.randn(N, D\_out, device\='cuda')

\# warmup
\# Uses static\_input and static\_target here for convenience,
\# but in a real setting, because the warmup includes optimizer.step()
\# you must use a few batches of real data.
s \= torch.cuda.Stream()
s.wait\_stream(torch.cuda.current\_stream())
with torch.cuda.stream(s):
    for i in range(3):
        optimizer.zero\_grad(set\_to\_none\=True)
        y\_pred \= model(static\_input)
        loss \= loss\_fn(y\_pred, static\_target)
        loss.backward()
        optimizer.step()
torch.cuda.current\_stream().wait\_stream(s)

\# capture
g \= torch.cuda.CUDAGraph()
\# Sets grads to None before capture, so backward() will create
\# .grad attributes with allocations from the graph's private pool
optimizer.zero\_grad(set\_to\_none\=True)
with torch.cuda.graph(g):
    static\_y\_pred \= model(static\_input)
    static\_loss \= loss\_fn(static\_y\_pred, static\_target)
    static\_loss.backward()
    optimizer.step()

real\_inputs \= \[torch.rand\_like(static\_input) for \_ in range(10)\]
real\_targets \= \[torch.rand\_like(static\_target) for \_ in range(10)\]

for data, target in zip(real\_inputs, real\_targets):
    \# Fills the graph's input memory with new data to compute on
    static\_input.copy\_(data)
    static\_target.copy\_(target)
    \# replay() includes forward, backward, and step.
    \# You don't even need to call optimizer.zero\_grad() between iterations
    \# because the captured backward refills static .grad tensors in place.
    g.replay()
    \# Params have been updated. static\_y\_pred, static\_loss, and .grad
    \# attributes hold values from computing on this iteration's data.

Copy to clipboard

### Partial-network capture[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#partial-network-capture "Link to this heading")

If some of your network is unsafe to capture (e.g., due to dynamic control flow, dynamic shapes, CPU syncs, or essential CPU-side logic), you can run the unsafe part(s) eagerly and use [`torch.cuda.make_graphed_callables()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables "torch.cuda.make_graphed_callables")
 to graph only the capture-safe part(s).

By default, callables returned by [`make_graphed_callables()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables "torch.cuda.make_graphed_callables")
 are autograd-aware, and can be used in the training loop as direct replacements for the functions or [`nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
\\ s you passed.

[`make_graphed_callables()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables "torch.cuda.make_graphed_callables")
 internally creates [`CUDAGraph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph "torch.cuda.CUDAGraph")
 objects, runs warmup iterations, and maintains static inputs and outputs as needed. Therefore (unlike with [`torch.cuda.graph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph.html#torch.cuda.graph "torch.cuda.graph")
) you don’t need to handle those manually.

In the following example, data-dependent dynamic control flow means the network isn’t capturable end-to-end, but [`make_graphed_callables()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables "torch.cuda.make_graphed_callables")
 lets us capture and run graph-safe sections as graphs regardless:

N, D\_in, H, D\_out \= 640, 4096, 2048, 1024

module1 \= torch.nn.Linear(D\_in, H).cuda()
module2 \= torch.nn.Linear(H, D\_out).cuda()
module3 \= torch.nn.Linear(H, D\_out).cuda()

loss\_fn \= torch.nn.MSELoss()
optimizer \= torch.optim.SGD(chain(module1.parameters(),
                                  module2.parameters(),
                                  module3.parameters()),
                            lr\=0.1)

\# Sample inputs used for capture
\# requires\_grad state of sample inputs must match
\# requires\_grad state of real inputs each callable will see.
x \= torch.randn(N, D\_in, device\='cuda')
h \= torch.randn(N, H, device\='cuda', requires\_grad\=True)

module1 \= torch.cuda.make\_graphed\_callables(module1, (x,))
module2 \= torch.cuda.make\_graphed\_callables(module2, (h,))
module3 \= torch.cuda.make\_graphed\_callables(module3, (h,))

real\_inputs \= \[torch.rand\_like(x) for \_ in range(10)\]
real\_targets \= \[torch.randn(N, D\_out, device\="cuda") for \_ in range(10)\]

for data, target in zip(real\_inputs, real\_targets):
    optimizer.zero\_grad(set\_to\_none\=True)

    tmp \= module1(data)  \# forward ops run as a graph

    if tmp.sum().item() \> 0:
        tmp \= module2(tmp)  \# forward ops run as a graph
    else:
        tmp \= module3(tmp)  \# forward ops run as a graph

    loss \= loss\_fn(tmp, target)
    \# module2's or module3's (whichever was chosen) backward ops,
    \# as well as module1's backward ops, run as graphs
    loss.backward()
    optimizer.step()

Copy to clipboard

### Usage with torch.cuda.amp[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#usage-with-torch-cuda-amp "Link to this heading")

For typical optimizers, `GradScaler.step` syncs the CPU with the GPU, which is prohibited during capture. To avoid errors, either use [partial-network capture](https://docs.pytorch.org/docs/2.15/notes/cuda.html#partial-network-capture)
, or (if forward, loss, and backward are capture-safe) capture forward, loss, and backward but not the optimizer step:

\# warmup
\# In a real setting, use a few batches of real data.
s \= torch.cuda.Stream()
s.wait\_stream(torch.cuda.current\_stream())
with torch.cuda.stream(s):
    for i in range(3):
        optimizer.zero\_grad(set\_to\_none\=True)
        with torch.cuda.amp.autocast():
            y\_pred \= model(static\_input)
            loss \= loss\_fn(y\_pred, static\_target)
        scaler.scale(loss).backward()
        scaler.step(optimizer)
        scaler.update()
torch.cuda.current\_stream().wait\_stream(s)

\# capture
g \= torch.cuda.CUDAGraph()
optimizer.zero\_grad(set\_to\_none\=True)
with torch.cuda.graph(g):
    with torch.cuda.amp.autocast():
        static\_y\_pred \= model(static\_input)
        static\_loss \= loss\_fn(static\_y\_pred, static\_target)
    scaler.scale(static\_loss).backward()
    \# don't capture scaler.step(optimizer) or scaler.update()

real\_inputs \= \[torch.rand\_like(static\_input) for \_ in range(10)\]
real\_targets \= \[torch.rand\_like(static\_target) for \_ in range(10)\]

for data, target in zip(real\_inputs, real\_targets):
    static\_input.copy\_(data)
    static\_target.copy\_(target)
    g.replay()
    \# Runs scaler.step and scaler.update eagerly
    scaler.step(optimizer)
    scaler.update()

Copy to clipboard

### Usage with multiple streams[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#usage-with-multiple-streams "Link to this heading")

Capture mode automatically propagates to any streams that sync with a capturing stream. Within capture, you may expose parallelism by issuing calls to different streams, but the overall stream dependency DAG must branch out from the initial capturing stream after capture begins and rejoin the initial stream before capture ends:

with torch.cuda.graph(g):
    \# at context manager entrance, torch.cuda.current\_stream()
    \# is the initial capturing stream

    \# INCORRECT (does not branch out from or rejoin initial stream)
    with torch.cuda.stream(s):
        cuda\_work()

    \# CORRECT:
    \# branches out from initial stream
    s.wait\_stream(torch.cuda.current\_stream())
    with torch.cuda.stream(s):
        cuda\_work()
    \# rejoins initial stream before capture ends
    torch.cuda.current\_stream().wait\_stream(s)

Copy to clipboard

Note

To avoid confusion for power users looking at replays in nsight systems or nvprof:
Unlike eager execution, the graph interprets a nontrivial stream DAG in capture
as a hint, not a command. During replay, the graph may reorganize independent ops
onto different streams or enqueue them in a different order (while respecting your
original DAG's overall dependencies).

Copy to clipboard

### Usage with DistributedDataParallel[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#usage-with-distributeddataparallel "Link to this heading")

#### NCCL < 2.9.6[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#nccl-2-9-6 "Link to this heading")

NCCL versions earlier than 2.9.6 don’t allow collectives to be captured. You must use [partial-network capture](https://docs.pytorch.org/docs/2.15/notes/cuda.html#partial-network-capture)
, which defers allreduces to happen outside graphed sections of backward.

Call [`make_graphed_callables()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables "torch.cuda.make_graphed_callables")
 on graphable network sections _before_ wrapping the network with DDP.

#### NCCL >= 2.9.6[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#id5 "Link to this heading")

NCCL versions 2.9.6 or later allow collectives in the graph. Approaches that capture an [entire backward pass](https://docs.pytorch.org/docs/2.15/notes/cuda.html#whole-network-capture)
 are a viable option, but need three setup steps.

1.  Disable DDP’s internal async error handling:
    

os.environ\["NCCL\_ASYNC\_ERROR\_HANDLING"\] \= "0"
torch.distributed.init\_process\_group(...)

Copy to clipboard

2.  Before full-backward capture, DDP must be constructed in a side-stream context:
    

with torch.cuda.stream(s):
    model \= DistributedDataParallel(model)

Copy to clipboard

3.  Your warmup must run at least 11 DDP-enabled eager iterations before capture.
    

### Graph memory management[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#graph-memory-management "Link to this heading")

A captured graph acts on the same virtual addresses every time it replays. If PyTorch frees the memory, a later replay can hit an illegal memory access. If PyTorch reassigns the memory to new tensors, the replay can corrupt the values seen by those tensors. Therefore, the virtual addresses used by the graph must be reserved for the graph across replays. The PyTorch caching allocator achieves this by detecting when capture is underway and satisfying the capture’s allocations from a graph-private memory pool. The private pool stays alive until its [`CUDAGraph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph "torch.cuda.CUDAGraph")
 object and all tensors created during capture go out of scope.

Private pools are maintained automatically. By default, the allocator creates a separate private pool for each capture. If you capture multiple graphs, this conservative approach ensures graph replays never corrupt each other’s values, but sometimes needlessly wastes memory.

#### Sharing memory across captures[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#sharing-memory-across-captures "Link to this heading")

To economize the memory stashed in private pools, [`torch.cuda.graph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph.html#torch.cuda.graph "torch.cuda.graph")
 and [`torch.cuda.make_graphed_callables()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables "torch.cuda.make_graphed_callables")
 optionally allow different captures to share the same private pool. It’s safe for a set of graphs to share a private pool if you know they’ll always be replayed in the same order they were captured, and never be replayed concurrently.

[`torch.cuda.graph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph.html#torch.cuda.graph "torch.cuda.graph")
’s `pool` argument is a hint to use a particular private pool, and can be used to share memory across graphs as shown:

g1 \= torch.cuda.CUDAGraph()
g2 \= torch.cuda.CUDAGraph()

\# (create static inputs for g1 and g2, run warmups of their workloads...)

\# Captures g1
with torch.cuda.graph(g1):
    static\_out\_1 \= g1\_workload(static\_in\_1)

\# Captures g2, hinting that g2 may share a memory pool with g1
with torch.cuda.graph(g2, pool\=g1.pool()):
    static\_out\_2 \= g2\_workload(static\_in\_2)

static\_in\_1.copy\_(real\_data\_1)
static\_in\_2.copy\_(real\_data\_2)
g1.replay()
g2.replay()

Copy to clipboard

The `pool` argument also accepts `MemPool`. If [`use_mem_pool()`](https://docs.pytorch.org/docs/2.15/cuda.html#torch.cuda.use_mem_pool "torch.cuda.use_mem_pool")
 is used during capture, the graph retains that pool until the graph is reset or destroyed. [`torch.cuda.CUDAGraph.pool()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph.pool "torch.cuda.CUDAGraph.pool")
 returns the primary capture pool, while `CUDAGraph.pools()` returns all pools retained by the graph.

g\_default\_pool \= torch.cuda.MemPool()
g\_side\_pool \= torch.cuda.MemPool()
g \= torch.cuda.CUDAGraph()

with torch.cuda.graph(g, pool\=g\_default\_pool):
    y \= foo(x)
    with torch.cuda.use\_mem\_pool(g\_side\_pool):
        tmp \= baz(y)
    z \= bar(tmp)

primary\_pool \= g.pool()
retained\_pools \= g.pools()

Copy to clipboard

It’s also safe to share a memory pool across separate graphs that do not depend on each other’s outputs, provided they never run concurrently. Be aware that replaying one graph can clobber another graph’s outputs when they share a pool, unless [`clone()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.clone.html#torch.Tensor.clone "torch.Tensor.clone")
 is called on the outputs beforehand. This pattern is frequently used in inference servers that accept variable batch sizes at runtime. vLLM is a notable example; see [here](https://github.com/vllm-project/vllm/blob/938a81692ea318e59ead4750e7e7425bfd6a4896/vllm/platforms/interface.py#L508-L515)
 and [here](https://github.com/vllm-project/vllm/blob/938a81692ea318e59ead4750e7e7425bfd6a4896/vllm/compilation/cuda_graph.py#L86-L89)
.

With [`torch.cuda.make_graphed_callables()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables "torch.cuda.make_graphed_callables")
, if you want to graph several callables and you know they’ll always run in the same order (and never concurrently) pass them as a tuple in the same order they’ll run in the live workload, and [`make_graphed_callables()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables "torch.cuda.make_graphed_callables")
 will capture their graphs using a shared private pool.

If, in the live workload, your callables will run in an order that occasionally changes, or if they’ll run concurrently, passing them as a tuple to a single invocation of [`make_graphed_callables()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables "torch.cuda.make_graphed_callables")
 is not allowed. Instead, you must call [`make_graphed_callables()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.make_graphed_callables.html#torch.cuda.make_graphed_callables "torch.cuda.make_graphed_callables")
 separately for each one.

### Data Dependent Control Flow[#](https://docs.pytorch.org/docs/2.15/notes/cuda.html#data-dependent-control-flow "Link to this heading")

Data-dependent control flow can with cuda graphs if the control flow is implemented using torch.cond(). If your function uses this function, compiling it with the “cudagraphs” backend will enable control flow in the resulting cuda graph via [conditional nodes](https://developer.nvidia.com/blog/dynamic-control-flow-in-cuda-graphs-with-conditional-nodes/)
.

Doing cuda graph capture of eager mode code using torch.cond() will also work.

Support for inductor backend to torch.compile is not available yet, but there is no fundamental blocker.

An example of using the cudagraphs backend to torch.compile on code using torch.cond is demonstrated below:

import torch

def true\_fn(x):
    return x.sin()

def false\_fn(x):
    return x.cos()

x \= torch.randn(4, device\="cuda", requires\_grad\=False)
pred \= torch.tensor(False, device\="cuda", requires\_grad\=False)
def foo(pred, x):
    with torch.inference\_mode():
        return torch.cond(pred, true\_fn, false\_fn, \[x\])

\# First call will run eager for warmup, second call will do graph
\# capture followed by graph replay, third call and beyond will do
\# just graph replay.
compiled\_foo \= torch.compile(foo, backend\="cudagraphs")
for i in range(3):
    y \= compiled\_foo(pred, x)

\# will output x.sin()
y \= compiled\_foo(~pred, x)

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/notes/cuda.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/notes/cuda.md.txt)

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