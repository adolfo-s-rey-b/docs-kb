Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/symmetric_memory.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/symmetric_memory.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/symmetric_memory.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/symmetric_memory.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/symmetric_memory.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/symmetric_memory.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/symmetric_memory.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/symmetric_memory.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/symmetric_memory.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/symmetric_memory.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/symmetric_memory.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/symmetric_memory.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/symmetric_memory.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/symmetric_memory.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/symmetric_memory.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/symmetric_memory.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/symmetric_memory.html)
[v1.13](https://docs.pytorch.org/docs/1.13/symmetric_memory.html)
[v1.12](https://docs.pytorch.org/docs/1.12/symmetric_memory.html)
[v1.11](https://docs.pytorch.org/docs/1.11/symmetric_memory.html)
[v1.10](https://docs.pytorch.org/docs/1.10/symmetric_memory.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/symmetric_memory.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/symmetric_memory.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/symmetric_memory.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/symmetric_memory.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/symmetric_memory.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/symmetric_memory.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/symmetric_memory.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/symmetric_memory.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/symmetric_memory.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/symmetric_memory.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/symmetric_memory.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/symmetric_memory.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/symmetric_memory.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/symmetric_memory.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/symmetric_memory.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/symmetric_memory.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/symmetric_memory.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/symmetric_memory.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/symmetric_memory.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/symmetric_memory.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/symmetric_memory.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/symmetric_memory.html)

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

PyTorch Symmetric Memory[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#pytorch-symmetric-memory "Link to this heading")

======================================================================================================================================

Created On: Oct 24, 2025 | Last Updated On: Aug 24, 2026

Note

`torch.distributed._symmetric_memory` is currently in alpha state and under development. API changes may be possible.

Why Symmetric Memory?[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#why-symmetric-memory "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

With rapidly evolving parallelization techniques, existing frameworks and libraries often struggle to keep up, and developers increasingly rely on custom implementations directly scheduling communications and computations. In recent years we’ve witnessed a shift from primarily relying on one-dimensional data-parallelism techniques to multi-dimensional parallelism ones. The latter have different latency requirements for different types of communications and thus require fine-grained overlapping of compute and communications.

To minimize compute interference, they also require the use of copy engines and network interface cards (NICs) to drive communication. Network transport protocols such as remote direct memory access (RDMA) enhance the performance by enabling direct, high-speed, and low-latency communication between processors and memory. This increase in variety indicates the need for finer-grained communication primitives than are offered today by high-level collective APIs, ones that would enable developers to implement specific algorithms tailored for their use cases, such as low-latency collectives, fine-grained compute-communications overlap, or custom fusions.

Furthermore, today’s advanced AI systems connect GPUs with high-bandwidth links (such as NVLinks, InfiniBand or RoCE), making GPU global memory directly accessible to peers. Such connections present a great opportunity for programmers to program the system as a single, gigantic GPU with vast accessible memory, instead of programming singular “GPU islands.”

In this document, we will show how you can use PyTorch Symmetric Memory to program modern GPU systems as a “single GPU” and achieve fine-grained remote access.

What PyTorch Symmetric Memory unlocks?[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#what-pytorch-symmetric-memory-unlocks "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

PyTorch Symmetric Memory unlocks three new capabilities:

*   **Customized communication patterns**: Increased flexibility in kernel writing allows developers to write custom kernels that implement their custom computations and communications, directly tailored to the need of the application. It will also be straightforward to add support for new data types along with the special compute that those data types might require, even if it’s not present yet in the standard libraries.
    
*   **In-kernel compute-comm fusion**: Device-initiated communication capability allows developers to write kernels with both computation and communication instructions, allowing for the fusion of computation and data movement in the smallest possible granularity.
    
*   **Low-latency remote access**: Network transport protocols like RDMA enhance the performance of symmetric memory in networked environments by enabling direct, high-speed, and low-latency communication between processors and memory. RDMA eliminates the overhead associated with the traditional network stack and CPU involvement. It also offloads data transfer from the compute to the NICs, freeing up compute resources for computational tasks.
    

Next, we will show you how PyTorch Symmetric Memory (SymmMem) enables new applications with the above capabilities.

A “Hello World” example[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#a-hello-world-example "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

The PyTorch SymmMem programming model involves two key elements:

*   creating symmetric tensors
    
*   creating SymmMem kernels
    

To create symmetric tensors, one can use the `torch.distributed._symmetric_memory` package:

import torch.distributed.\_symmetric\_memory as symm\_mem

t \= symm\_mem.empty(128, device\=torch.device("cuda", rank))
hdl \= symm\_mem.rendezvous(t, group)

Copy to clipboard

The `symm_mem.empty` function creates a tensor that is backed by a symmetric memory allocation. The `rendezvous` function establishes a rendezvous with peers in the group, and returns a handle to the symmetric memory allocation. The handle provides method to access information related to the symmetric memory allocation, such as pointers to symmetric buffer on peer ranks, multicast pointer (if supported), and signal pads.

The `empty` and `rendezvous` functions must be called in the same order on all ranks in the group.

Then, collectives can be called on these tensors. For example, to perform a one-shot all-reduce:

\# Most SymmMem ops are under the torch.ops.symm\_mem namespace
torch.ops.symm\_mem.one\_shot\_all\_reduce(t, "sum", group)

Copy to clipboard

Please note that `torch.ops.symm_mem` is an “op namespace” instead of a python module. Therefore, you can’t import it by `import torch.ops.symm_mem`, neither can you import an op by `from torch.ops.symm_mem import one_shot_all_reduce`. You can call the op directly as in the example above.

Write your own kernel[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#write-your-own-kernel "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

To write your own kernel doing communications with symmetric memory, you’ll need access to the addresses of mapped peer buffers and access to signal pads that are required for synchronization. In the kernel you’ll also need to perform correct synchronizations to make sure that peers are ready for communication, and signal to them that this GPU is ready.

PyTorch Symmetric Memory provides CUDA Graph-compatible synchronization primitives that operate on the signal pad accompanying each symmetric memory allocation. Kernels using symmetric memory can be written both in CUDA and in Triton. Here’s an example allocating symmetric tensor and exchanging handles:

import torch.distributed.\_symmetric\_memory as symm\_mem

dist.init\_process\_group()
rank \= dist.get\_rank()

\# Allocate a tensor
t \= symm\_mem.empty(4096, device\=f"cuda:{rank}")
\# Establish symmetric memory and obtain the handle
hdl \= symm\_mem.rendezvous(t, dist.group.WORLD)

Copy to clipboard

Access to buffer pointers, multimem pointer, and signal pads is provided via:

hdl.buffer\_ptrs
hdl.multicast\_ptr
hdl.signal\_pad\_ptrs

Copy to clipboard

Data pointed to by `buffer_ptrs` can be accessed just like regular local data, and any necessary compute can also be performed in the usual ways. As with local data, you can and should use vectorized accesses to improve efficiency.

Symmetric memory is especially convenient for writing kernels in Triton. While previously Triton removed the barriers to writing efficient CUDA code, now communications can be added easily to Triton kernels. The kernel below demonstrates a low-latency, all-reduce kernel written in Triton.

@triton.jit
def one\_shot\_all\_reduce\_kernel(
    buf\_tuple,
    signal\_pad\_ptrs,
    output\_ptr,
    numel: tl.constexpr,
    rank: tl.constexpr,
    world\_size: tl.constexpr,
    BLOCK\_SIZE: tl.constexpr,
):
    ptx\_utils.symm\_mem\_sync(
        signal\_pad\_ptrs, None, rank, world\_size, hasSubsequenceMemAccess\=True
    )

    pid \= tl.program\_id(axis\=0)
    block\_start \= pid \* BLOCK\_SIZE

    while block\_start < numel:
        offsets \= block\_start + tl.arange(0, BLOCK\_SIZE)
        mask \= offsets < numel
        acc \= tl.zeros((BLOCK\_SIZE,), dtype\=tl.bfloat16)

        for i in tl.static\_range(world\_size):
            buffer\_rank \= buf\_tuple\[i\]
            x \= tl.load(buffer\_rank + offsets, mask\=mask)
            acc += x

        tl.store(output\_ptr + offsets, acc, mask\=mask)
        block\_start += tl.num\_programs(axis\=0) \* BLOCK\_SIZE

    ptx\_utils.symm\_mem\_sync(
        signal\_pad\_ptrs, None, rank, world\_size, hasPreviousMemAccess\=True
    )

Copy to clipboard

Synchronizations at the beginning and the end of the kernel above guarantee that all the processes see consistent data. The bulk of the kernel is recognizable Triton code, and Triton will optimize it behind the scene, making sure memory accesses are performed in an efficient way with vectorization and unrolling. As with all Triton kernels, it is easily modifiable to add extra computations or change the communication algorithm. Visit https://github.com/meta-pytorch/kraken/blob/main/kraken to see additional utilities and examples of using symmetric memory to implement common patterns in Triton.

One-sided get[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#one-sided-get "Link to this heading")

----------------------------------------------------------------------------------------------------------------

Symmetric memory also exposes a small one-sided `get` API for copying data from a peer’s symmetric allocation into a local tensor:

src \= symm\_mem.empty(1024, device\=device)
hdl \= symm\_mem.rendezvous(src, group)

if dist.get\_rank(group) \== 0:
    dst \= torch.empty((512,), device\=device)
    \# Copy the last 512 elements of the peer's allocation into dst.
    symm\_mem.get(dst, hdl, peer\=1, offset\=512)

Copy to clipboard

`hdl` is the symmetric memory handle returned by `rendezvous`; the remote source is the peer’s allocation backing that handle. The number of elements copied is inferred from `dst`, so pass a view (e.g. `dst[:n]`) to fill only part of a tensor; `offset` is given in elements of `dst`’s dtype and defaults to `0`. `dst` may be a regular CUDA tensor or another symmetric tensor; it must be on the same device as `hdl` and backed by contiguous memory. The copy is issued on the current CUDA stream.

Scale out[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#scale-out "Link to this heading")

--------------------------------------------------------------------------------------------------------

Large language models distribute experts onto more than 8 GPUs, hence requiring multi-node access capability. NICs capable of RDMA come to help. In addition, software libraries such as NVSHMEM or rocSHMEM abstract away the programming difference between intra-node access and inter-node access with primitives that are slightly higher level than pointer access, such as put and get.

PyTorch provides NVSHMEM plugins to augment Triton kernels’ cross-node capabilities. As shown in the code snippet below, one can initiate a cross-node put command within the kernel.

import torch.distributed.\_symmetric\_memory.\_nvshmem\_triton as nvshmem
from torch.distributed.\_symmetric\_memory.\_nvshmem\_triton import requires\_nvshmem

@requires\_nvshmem
@triton.jit
def my\_put\_kernel(
    dest,
    src,
    nelems,
    pe,
):
    nvshmem.put(dest, src, nelems, pe)

Copy to clipboard

The `requires_nvshmem` decorator is used to indicate that the kernel requires the NVSHMEM device library as an external dependency. When Triton compiles the kernel, the decorator will search your system paths for the NVSHMEM device library. If it is available, Triton will include the necessary device assembly to use the NVSHMEM functions.

Using Memory Pool[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#using-memory-pool "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

Memory pool allows PyTorch SymmMem to cache memory allocations that have been rendezvoused, saving time when creating new tensors. For convenience, PyTorch SymmMem has added a `get_mem_pool` API to return a symmetric memory pool. Users can use the returned MemPool with the `torch.cuda.use_mem_pool` context manager. In the example below, tensor `x` will be created from symmetric memory:

    import torch.distributed.\_symmetric\_memory as symm\_mem

    mempool \= symm\_mem.get\_mem\_pool(device)

    with torch.cuda.use\_mem\_pool(mempool):
        x \= torch.arange(128, device\=device, dtype\=torch.float32)

    torch.ops.symm\_mem.one\_shot\_all\_reduce(x, "sum", group\_name)

Copy to clipboard

Similarly, you can put a compute operation under the MemPool context, and the result tensor will be created from symmetric memory too.

    dim \= 1024
    w \= torch.ones(dim, dim, device\=device)
    x \= torch.ones(1, dim, device\=device)

    mempool \= symm\_mem.get\_mem\_pool(device)
    with torch.cuda.use\_mem\_pool(mempool):
        \# y will be in symmetric memory
        y \= torch.mm(x, w)

Copy to clipboard

As of torch 2.11, the `CUDA` and `NVSHMEM` backends support MemPool. MemPool support of the `NCCL` backend is in progress.

Note

The pool returned by `get_mem_pool` feeds `torch.ops.symm_mem.*` kernels, though it does not register the allocation with NCCL. To drive `dist.*` collectives onto NCCL’s symmetric memory backed kernels, you can register the mempool for NCCL to auto-select. For more details, see [NCCL Symmetric Kernels](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#nccl-symmetric-kernels)
.

NCCL Symmetric Kernels[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#nccl-symmetric-kernels "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

Note

Requires NCCL 2.27 or later and a single NVLink domain (every rank reachable over direct NVLink).

NCCL 2.27+ added a family of device kernels — “SymK” internally — written specifically for symmetric, window-registered buffers. Because each rank knows every peer’s buffer address up front, these kernels skip the generic proxy/ring machinery and instead use LL (low-latency), multimem/NVLS, and TMA variants. NCCL picks one per call from message size, so the same `dist.all_reduce` gets a latency-optimized kernel for small messages and a bandwidth-optimized one for large ones.

Symmetric kernels are driven through the _standard_ collective API — `dist.all_reduce`, `dist.all_gather_into_tensor`, `dist.reduce_scatter_tensor` — with no change at the call site. What matters is that the buffers were registered with NCCL as symmetric windows. There are two ways to arrange that.

### Option 1: register a memory pool with the process group[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#option-1-register-a-memory-pool-with-the-process-group "Link to this heading")

This route puts NCCL’s allocator behind a `torch.cuda.MemPool`, so _any_ tensor allocated inside the pool’s context is window-registered, including tensors produced by compute ops. It is usually the better fit for an existing model, since allocations do not have to be rewritten as `symm_mem.empty`.

import torch
import torch.distributed as dist

device \= torch.device("cuda", rank)

\# \`device\_id\` eagerly initializes the NCCL communicator. \`register\_mem\_pool\`
\# requires a communicator that already exists, and raises otherwise.
dist.init\_process\_group(backend\="nccl", device\_id\=device)
pg \= dist.group.WORLD

backend \= dist.get\_backend\_impl(pg, device)

\# A MemPool backed by \`ncclMemAlloc\` / \`ncclMemFree\`.
pool \= torch.cuda.MemPool(backend.mem\_allocator)

\# \`symm=True\` registers each segment with \`ncclCommWindowRegister\` using
\# \`NCCL\_WIN\_COLL\_SYMMETRIC\`, which is what makes the symmetric kernels
\# eligible. The default \`symm=False\` performs ordinary user-buffer
\# registration, which does not.
backend.register\_mem\_pool(pool, symm\=True)

with torch.cuda.use\_mem\_pool(pool):
    x \= torch.ones(1024 \* 1024, dtype\=torch.bfloat16, device\=device)

\# Dispatches to a NCCL symmetric kernel.
dist.all\_reduce(x, op\=dist.ReduceOp.SUM)

\# De-register before the pool is torn down.
backend.deregister\_mem\_pool(pool)

Copy to clipboard

`register_mem_pool` registers the segments already in the pool _and_ installs an allocator hook, so later allocations in the pool are registered as well.

### Option 2: allocate through the NCCL symmetric memory backend[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#option-2-allocate-through-the-nccl-symmetric-memory-backend "Link to this heading")

If the tensors are already symmetric-memory tensors — for example because custom kernels need the handle, its peer pointers, or its signal pads — select the `NCCL` backend and rendezvous as usual. `rendezvous` window-registers the allocation, so `dist.*` collectives on it become eligible too.

import torch.distributed as dist
import torch.distributed.\_symmetric\_memory as symm\_mem

symm\_mem.set\_backend("NCCL")

x \= symm\_mem.empty(1024 \* 1024, dtype\=torch.bfloat16, device\=device)
symm\_mem.rendezvous(x, group\=dist.group.WORLD.group\_name)

dist.all\_reduce(x, op\=dist.ReduceOp.SUM)

Copy to clipboard

### When NCCL uses a symmetric kernel[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#when-nccl-uses-a-symmetric-kernel "Link to this heading")

Only these collective / reduction / dtype combinations currently have a symmetric implementation:

| Collective | Reduction ops | Data types |
| --- | --- | --- |
| `all_gather` | n/a | any |
| `all_reduce` | `SUM`, `AVG` | `float32`, `float16`, `bfloat16`, `float8_e4m3fn`, `float8_e5m2` |
| `reduce_scatter` | `SUM`, `AVG` | `float32`, `float16`, `bfloat16`, `float8_e4m3fn`, `float8_e5m2` |

Note in particular that `float64` and the integer dtypes are excluded for the two reducing collectives, as are `MIN` / `MAX` / `PRODUCT`. Collectives outside the table (`broadcast`, `reduce`, `all_to_all`, point-to-point) currently have no symmetric implementation, and fall back to the regular ring/tree path silently.

To confirm, you can use NCCL logs to check kernel names:

NCCL\_DEBUG\=INFO NCCL\_DEBUG\_SUBSYS\=TUNING python train.py

Copy to clipboard

AllReduce \[Symmetric\]: 2097152 Bytes \-> Kernel AllReduce\_RSxLDMC\_AGxSTMC nchannels 16 nthreads 512 nWorks 1

Copy to clipboard

Also, if you are looking at a profiler, device kernel names should resemble `ncclSymkDevKernel_*`. For example, `ncclSymkDevKernel_AllReduce_AGxLLMC_R_sum_bf16`, as opposed to `ncclDevKernel_*` for the generic NCCL path.

### CFT logical-endpoint handles[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#cft-logical-endpoint-handles "Link to this heading")

Note

Requires NCCL 2.31.2+, a Blackwell-class GPU (sm\_100 or newer), and a driver reporting CUDA 13.3 or later (an r610-or-newer driver). NCCL itself must also be built with CUDA 13.3+.

CFT (Compute Fabric Transport) exposes a peer’s window-registered memory as a _logical endpoint_: an opaque `(le_id, le_offset)` pair that a custom device kernel can hand to the `ncclCft` put/get/reduce device API to reach that peer’s copy of a symmetric buffer — without constructing a `ncclDevComm`. When the symmetric-memory backend is `NCCL`, the rendezvous handle exposes the coordinates:

*   `hdl.get_peer_cft_handle(peer)` returns the `(le_id, le_offset)` pair addressing `peer`’s copy of the buffer.
    
*   `hdl.get_multimem_cft_handle()` returns the multicast endpoint (requires NVLS; the first call may be collective, so all ranks must reach it).
    

Handles are only meaningful for the group the tensor was rendezvoused with — each group owns a separate set of logical endpoints over the same allocation.

Two knobs control availability:

*   `host_cft_mode` on the communicator config (`ProcessGroupNCCL.Options().config.host_cft_mode`) decides whether the endpoints are created and what happens when the stack cannot support them: `1` (enable — fail communicator init if unsupported), `2` (disable), `3` (fallback — create them if possible, silently proceed without otherwise). The default is **disable**: host-side CFT is opt-in per communicator, since endpoints are a limited per-device resource. The mode must be identical on every rank and must be set before the communicator is created — the endpoints are made during window registration.
    
*   The `NCCL_CFT_ENABLE` environment variable (default `1`) is NCCL’s global kill switch; `NCCL_CFT_ENABLE=0` makes NCCL report no CFT support regardless of `host_cft_mode`.
    

Under `host_cft_mode=3` (fallback), an unsupported GPU, driver, or NCCL build is not an error at init — the handle queries simply raise `RuntimeError`.

Copy Engine Collectives[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#copy-engine-collectives "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

Note

Copy Engine Collectives require NCCL 2.28 or later, and GPUs with peer-to-peer (P2P) access.

Copy Engine (CE) Collectives are an optimization for NCCL collective operations that offload data movement to the GPU’s copy engines (DMA engines) instead of using CUDA streaming multiprocessors (SMs). This frees up SMs for compute work, enabling better overlap of communication and computation during distributed training.

To use CE collectives, you need to:

1.  Configure the NCCL process group with the zero-CTA policy
    
2.  Set up symmetric memory with the NCCL backend
    
3.  Allocate tensors using symmetric memory
    
4.  Register the tensors with symmetric memory via rendezvous
    

Once set up, standard collective functions like `all_gather_single()` and `all_to_all_single()` will automatically use the copy engines when operating on symmetric memory tensors.

**Example**

import torch
import torch.distributed as dist
import torch.distributed.\_symmetric\_memory as symm\_mem

\# Initialize process group with zero-CTA policy for CE collectives
opts \= dist.ProcessGroupNCCL.Options()
opts.config.cta\_policy \= dist.ProcessGroupNCCL.NCCL\_CTA\_POLICY\_ZERO
device \= torch.device("cuda", rank)
dist.init\_process\_group(backend\="nccl", pg\_options\=opts, device\_id\=device)

\# Set up symmetric memory with NCCL backend
symm\_mem.set\_backend("NCCL")
group\_name \= dist.group.WORLD.group\_name

\# Allocate tensors using symmetric memory
numel \= 1024 \* 1024
inp \= symm\_mem.empty(numel, device\=device)
out \= symm\_mem.empty(numel \* world\_size, device\=device)

\# Register tensors for symmetric memory operations
symm\_mem.rendezvous(inp, group\=group\_name)
symm\_mem.rendezvous(out, group\=group\_name)

\# Perform collective operation using copy engines
\# This now runs on DMA engines instead of SMs
work \= dist.all\_gather\_single(out, inp, async\_op\=True)
work.wait()

Copy to clipboard

**Benefits**

*   **SM offloading**: Communication runs on copy engines, leaving SMs free for computation
    
*   **Better overlap**: Enables more efficient computation/communication overlap
    
*   **Transparent API**: Uses the same collective API, just with symmetric memory tensors
    

**Requirements and Limitations**

*   NCCL version 2.28 or later
    
*   GPUs must have peer-to-peer (P2P) access enabled
    
*   Tensors must be allocated using `torch.distributed._symmetric_memory()` and rendezvoused
    
*   The NCCL process group must be configured with `NCCL_CTA_POLICY_ZERO` or the environment variable `NCCL_CTA_POLICY` be set to 2
    
*   As of NCCL 2.28, CE collectives cannot run with the default stream, so you would need to use the `async_op=True` flag to activate the internal stream of `ProcessGroupNCCL` or create a side stream yourself
    

Higher-Precision Reduction[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#higher-precision-reduction "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

When tensors are allocated with symmetric memory, NCCL’s symmetric kernel implementation enables internal reduction with higher precision. For example, with BF16 inputs, NCCL will automatically accumulate in FP32 internally before producing BF16 outputs (BF16 in → FP32 accumulate → BF16 out). This improves numerical accuracy of reduction operations without changing the collective call.

**Scope**

*   **Applicable operations**: `reduce_scatter` and `all_reduce` only
    
*   **Domain**: Within the NVLink domain as of torch 2.9 (NCCL 2.27); NVLink + network for `reduce_scatter` as of torch 2.11 (NCCL 2.29)
    
*   **Precision**: BF16/FP16 in → FP32 internal accumulation → BF16/FP16 out
    

**Example**

import torch.distributed as dist
import torch.distributed.\_symmetric\_memory as symm\_mem

\# Allocate tensors using NCCL symmetric memory
symm\_mem.set\_backend("NCCL")
inp \= symm\_mem.empty(1024, 1024, device\=device, dtype\=torch.bfloat16)
symm\_mem.rendezvous(inp, group\_name)

\# reduce\_scatter and all\_reduce on symmetric memory tensors
\# automatically benefit from FP32 internal accumulation
dist.all\_reduce(inp)

Copy to clipboard

Note

This higher-precision accumulation is enabled transparently by NCCL when using symmetric memory tensors. No additional configuration is required beyond the symmetric tensor creation and rendezvous described above. This currently applies to `reduce_scatter` and `all_reduce` within the supported domains only; other collectives (e.g., `all_gather`) and inter-node communication are not affected.

Rendezvous at Scale[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#rendezvous-at-scale "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

By default, `rendezvous` exchanges metadata via the TCPStore. Each rank in the symmetric memory group issues one store set and N-1 store gets (where N is the group size, typically 8–72 for NVLink domains). At large world sizes the TCPStore (~200k QPS capacity) becomes a bottleneck: for example, with 72-rank NVLink groups at 10k total ranks, a single rendezvous takes ~3.6s via TCPStore; at 100k ranks this grows to ~36s.

To use the process group’s NCCL allgather instead, set `use_pg_for_symm_mem_rendezvous` in the process group options:

opts \= dist.ProcessGroupNCCL.Options()
opts.use\_pg\_for\_symm\_mem\_rendezvous \= True
pg \= dist.new\_group(ranks, pg\_options\=opts)

t \= symm\_mem.empty(size, device\=device)
hdl \= symm\_mem.rendezvous(t, group\=pg)

Copy to clipboard

If the process group is only used for symmetric memory and won’t be used for regular collectives afterwards (e.g., an expert-parallelism group), you can release the NCCL communicator after rendezvous via `abort()`. The symmetric memory handle remains usable since it only depends on the mapped memory, not the communicator:

opts \= dist.ProcessGroupNCCL.Options()
opts.use\_pg\_for\_symm\_mem\_rendezvous \= True
ep\_pg \= dist.new\_group(ep\_ranks, pg\_options\=opts)

t \= symm\_mem.empty(size, device\=device)
hdl \= symm\_mem.rendezvous(t, group\=ep\_pg)

\# Release the NCCL communicator since ep\_pg won't be used for collectives.
\# The symm\_mem handle is still usable — it only needs the mapped memory.
ep\_pg.abort()

Copy to clipboard

Note

Enabling `use_pg_for_symm_mem_rendezvous` will lazily create the NCCL communicator for the process group if it doesn’t already exist.

API Reference[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#api-reference "Link to this heading")

----------------------------------------------------------------------------------------------------------------

torch.distributed.\_symmetric\_memory.empty(_\*size: \_int_, _dtype: \_dtype | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _device: \_device | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_symmetric_memory/__init__.py#L2191)
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.distributed._symmetric_memory.empty "Link to this definition")

torch.distributed.\_symmetric\_memory.empty(_size: Sequence\[\_int\]_, _\*_, _dtype: \_dtype | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _device: \_device | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Similar to [`torch.empty()`](https://docs.pytorch.org/docs/2.15/generated/torch.empty.html#torch.empty "torch.empty")
. The returned tensor can be used by `torch._distributed._symmetric_memory.rendezvous()` to establish a symmetric memory tensor among participating processes.

Note

This is a host-synchronous allocation. Together with [`rendezvous()`](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.distributed._symmetric_memory.rendezvous "torch.distributed._symmetric_memory.rendezvous")
, it is intended as an initialization-time operation: allocate a symmetric memory tensor once and reuse it, rather than allocating in hot code paths.

Parameters:

**size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_..._) – a sequence of integers defining the shape of the output tensor. Can be a variable number of arguments or a collection like a list or tuple.

Keyword Arguments:

*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – the desired data type of returned tensor. Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_dtype.html#torch.set_default_dtype "torch.set_default_dtype")
    ).
    
*   **device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    , optional) – the desired device of returned tensor. Default: if `None`, uses the current device for the default tensor type (see [`torch.set_default_device()`](https://docs.pytorch.org/docs/2.15/generated/torch.set_default_device.html#torch.set_default_device "torch.set_default_device")
    ). `device` will be the CPU for CPU tensor types, the current CUDA device for CUDA tensor types, and the current XPU device for XPU tensor types.
    

torch.distributed.\_symmetric\_memory.rendezvous(_tensor_, _group_) → \_SymmetricMemory[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_symmetric_memory/__init__.py#L2254)
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.distributed._symmetric_memory.rendezvous "Link to this definition")

Establish a symmetric memory tensor among participating processes. This is a collective operation.

Note

This is a host-blocking initialization operation: the first rendezvous of a tensor performs handle exchange and mapping across processes, and synchronizes the host with the device. It cannot be ordered onto a CUDA stream or captured in a CUDA graph. Rendezvous a buffer once and reuse the returned handle rather than calling this in hot code paths; subsequent calls on the same tensor return the cached handle.

Parameters:

*   **tensor** ([`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the local tensor used to establish the symmetric memory tensor. It must be allocated via `torch._distributed._symmetric_memory.empty()`. The shape, dtype, and device type must be identical across all participating processes.
    
*   **group** (Union\[str, `torch.distributed.ProcessGroup`\]) – The group identifying the participating processes. This can be either a group name or a process group object.
    

Return type:

\_SymmetricMemory

torch.distributed.\_symmetric\_memory.get(_dst_, _hdl_, _peer_, _offset\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_symmetric_memory/__init__.py#L2442)
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.distributed._symmetric_memory.get "Link to this definition")

Copy `dst.numel()` elements starting at `offset` from `peer`’s symmetric allocation into local `dst` using one-sided symmetric memory access.

`hdl` is the symmetric memory handle returned by [`torch.distributed._symmetric_memory.rendezvous()`](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.distributed._symmetric_memory.rendezvous "torch.distributed._symmetric_memory.rendezvous")
; the remote source is `peer`’s allocation backing that handle. The number of elements copied is inferred from `dst`; pass a view (e.g. `dst[:n]`) to fill only part of a tensor. `offset` is expressed in elements of `dst`’s dtype. `dst` can be a regular CUDA tensor or a symmetric-memory tensor; it must be on the same device as `hdl` and backed by contiguous memory. The copy is issued on the current CUDA stream.

Parameters:

*   **dst** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – local destination tensor.
    
*   **hdl** (_SymmetricMemory_) – handle whose peer allocation is the remote source.
    
*   **peer** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – rank to copy from.
    
*   **offset** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – element offset into the peer allocation to start reading from. Defaults to `0`.
    

torch.distributed.\_symmetric\_memory.is\_nvshmem\_available() → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_symmetric_memory/__init__.py#L2282)
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.distributed._symmetric_memory.is_nvshmem_available "Link to this definition")

Check if NVSHMEM (CUDA) or rocSHMEM (ROCm) is available in the current build and usable at runtime. On ROCm, rocSHMEM `VERSION` must be at least 3.3.0 (see `rocshmem/rocshmem.hpp`).

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.distributed.\_symmetric\_memory.set\_backend(_name_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_symmetric_memory/__init__.py#L2300)
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.distributed._symmetric_memory.set_backend "Link to this definition")

Set the backend for symmetric memory allocation. This is a global setting and affects all subsequent calls to `torch._distributed._symmetric_memory.empty()`. Note that the backend cannot be changed once a symmetric memory tensor has been allocated.

Parameters:

**backend** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – the backend for symmetric memory allocation. Currently, only “NVSHMEM”, “CUDA”, “NCCL” are supported.

torch.distributed.\_symmetric\_memory.get\_backend(_device_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_symmetric_memory/__init__.py#L2314)
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.distributed._symmetric_memory.get_backend "Link to this definition")

Get the backend for symmetric memory allocation for a given device. If not found, return None.

Parameters:

**device** (torch.device or str) – the device for which to get the backend.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 | None

torch.distributed.\_symmetric\_memory.get\_mem\_pool(_device_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_symmetric_memory/__init__.py#L2384)
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.distributed._symmetric_memory.get_mem_pool "Link to this definition")

Get the symmetric memory pool for a given device. If not found, create a new pool.

The tensor allocations with this pool must be symmetric across ranks. The allocated tensors can be used with symmetric operations, for example, operations defined under torch.ops.symm\_mem.

Parameters:

**device** (torch.device or str) – the device for which to get the symmetric memory pool.

Returns:

the symmetric memory pool for the given device, e.g. a torch.cuda.MemPool for a CUDA device or a torch.xpu.MemPool for an XPU device.

Return type:

torch.cuda.MemPool | torch.xpu.MemPool

Example:

\>>> pool \= torch.distributed.\_symmetric\_memory.get\_mem\_pool("cuda:0")
\>>> with torch.cuda.use\_mem\_pool(pool):
\>>>     tensor \= torch.randn(1000, device\="cuda:0")
\>>> tensor \= torch.ops.symm\_mem.one\_shot\_all\_reduce(tensor, "sum", group\_name)

Copy to clipboard

torch.distributed.\_symmetric\_memory.is\_symm\_mem\_tensor(_tensor_) → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_symmetric_memory/__init__.py#L2624)
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.distributed._symmetric_memory.is_symm_mem_tensor "Link to this definition")

Returns `True` if `tensor` was allocated via symmetric memory (i.e. via [`torch.distributed._symmetric_memory.empty()`](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.distributed._symmetric_memory.empty "torch.distributed._symmetric_memory.empty")
 or `_SymmetricMemory.empty_strided_p2p()`).

This is a non-collective, O(1) check.

Parameters:

**tensor** ([`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – the tensor to check.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.distributed.\_symmetric\_memory.set\_signal\_pad\_size(_size_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_symmetric_memory/__init__.py#L2336)
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.distributed._symmetric_memory.set_signal_pad_size "Link to this definition")

Set the signal pad size for future symmetric memory allocations.

Signal pads are P2P-accessible memory regions used for synchronization in symmetric memory. This function allows users to configure the signal pad size to be proportional to their workload requirements.

Warning

This must be called before any symmetric memory allocations are made. The size cannot be changed after allocations have been performed.

Parameters:

**size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
) – the signal pad size in bytes. The size should be proportional to the number of blocks launched and the world size.

Example:

\>>> \# Set a larger signal pad size before any allocations
\>>> torch.distributed.\_symmetric\_memory.set\_signal\_pad\_size(1024 \* 1024)  \# 1MB

Copy to clipboard

torch.distributed.\_symmetric\_memory.get\_signal\_pad\_size()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_symmetric_memory/__init__.py#L2361)
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.distributed._symmetric_memory.get_signal_pad_size "Link to this definition")

Get the current signal pad size for symmetric memory allocations.

Returns the user-configured size if set via [`set_signal_pad_size()`](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.distributed._symmetric_memory.set_signal_pad_size "torch.distributed._symmetric_memory.set_signal_pad_size")
, otherwise returns the default size.

Returns:

the signal pad size in bytes.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

Example:

\>>> size \= torch.distributed.\_symmetric\_memory.get\_signal\_pad\_size()
\>>> print(f"Signal pad size: {size} bytes")

Copy to clipboard

Op Reference[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#op-reference "Link to this heading")

--------------------------------------------------------------------------------------------------------------

Note

The following ops are hosted in the `torch.ops.symm_mem` namespace. You can call them directly via `torch.ops.symm_mem.<op_name>`.

torch.distributed.\_symmetric\_memory.reduce\_scatter\_offset(_input_, _out_, _group_, _\*_, _dim_, _offsets_, _dst\_ranks_, _red\_op\='sum'_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_symmetric_memory/__init__.py#L2549)
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.distributed._symmetric_memory.reduce_scatter_offset "Link to this definition")

Simultaneously reduce N blocks of a 2-D `input` tensor from a symmetric memory buffer, routing each block to a specific destination rank. Only `dst_ranks[i]` writes the reduced result for block `i`; the result is written to a contiguous output tensor, with the same shape as block `i`.

The `dim` argument controls which dimension is sharded:

*   `dim=0` (row sharding): block `i` spans `input[offsets[i-1] : offsets[i], :]`. Each `out[j]` has shape `(size_j, input.size(1))`.
    
*   `dim=1` (column sharding): block `i` spans `input[:, offsets[i-1] : offsets[i]]`. Each `out[j]` has shape `(input.size(0), size_j)`.
    

Blocks are described by `offsets`, an inclusive prefix-sum of block sizes along `dim` (first block starts at index 0 by convention). Block offsets can be even or uneven; when uneven, the following condition must be met: for each `j`, the `j`\-th owned block must have the same size across all ranks (so that `out[j]` has a uniform shape); different `j`’s may differ.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – 2-D tensor allocated via symmetric memory (innermost dimension must be contiguous).
    
*   **out** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – Output tensors for this rank’s owned blocks. Must have length equal to the number of blocks owned by this rank (i.e. the count of `i` where `dst_ranks[i] == my_rank`). Each `out[j]` must be contiguous with the same dtype as `input`.
    
*   **group** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The name of the `ProcessGroup` to perform the operation on.
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Dimension along which blocks are defined (0 or 1).
    
*   **offsets** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_ _|_ _None_) – Inclusive prefix-sum of block sizes along `dim`, length N. If not provided, `input.size(dim)` is divided into equal-size blocks based on the size of the `group`.
    
*   **dst\_ranks** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_ _|_ _None_) – Destination rank for each block. If not provided, blocks are distributed round-robin across ranks.
    
*   **red\_op** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Reduction operation; currently only `'sum'` is supported.
    

Example:

\>>> \# Each rank holds a Grouped GEMM gradient buffer in symmetric memory.
\>>> \# The buffer has W experts laid out as equal column blocks; each expert
\>>> \# is reduced to a specific rank (dst\_ranks\[i\] == i % world\_size).
\>>> buf \= symm\_mem.empty(H, W \* C, dtype\=torch.bfloat16, device\="cuda")
\>>> symm\_mem.rendezvous(buf, group\=group\_name)
\>>> offsets \= \[i \* C for i in range(1, W + 1)\]  \# inclusive prefix-sum
\>>> dst\_ranks \= \[i % world\_size for i in range(W)\]
\>>> n\_owned \= sum(r \== rank for r in dst\_ranks)
\>>> out \= \[torch.empty(H, C, dtype\=torch.bfloat16, device\="cuda") for \_ in range(n\_owned)\]
\>>> symm\_mem.reduce\_scatter\_offset(buf, out, group\_name, dim\=1, offsets\=offsets, dst\_ranks\=dst\_ranks)

Copy to clipboard

torch.ops.symm\_mem.multimem\_all\_reduce\_(_input: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _reduce\_op: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_, _group\_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.multimem_all_reduce_ "Link to this definition")

Performs a multimem all-reduce operation on the input tensor. This operation requires hardware support for multimem operations. On NVIDIA GPUs, NVLink SHARP is required.

Warning

All symm\_mem collectives for a given group must be issued from a single CUDA stream. The kernels synchronize ranks using a shared signal pad indexed by block ID with no per-stream isolation; issuing concurrent launches from different streams on the same group will cause a deadlock. To use symm\_mem collectives from multiple streams, serialize them onto one dedicated stream using `stream.wait_stream()` / `current_stream.wait_stream()`.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Input tensor to perform all-reduce on. Must be symmetric.
    
*   **reduce\_op** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Reduction operation to perform. Currently only “sum” is supported.
    
*   **group\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Name of the group to perform all-reduce on.
    

torch.ops.symm\_mem.multimem\_all\_gather\_out(_input: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _group\_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_, _out: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.multimem_all_gather_out "Link to this definition")

Performs a multimem all-gather operation on the input tensor. This operation requires hardware support for multimem operations. On NVIDIA GPUs, NVLink SHARP is required.

Warning

All symm\_mem collectives for a given group must be issued from a single CUDA stream. See [`multimem_all_reduce_()`](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.multimem_all_reduce_ "torch.ops.symm_mem.multimem_all_reduce_")
 for details.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Input tensor to perform all-gather on.
    
*   **group\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Name of the group to perform all-gather on.
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Output tensor to store the result of the all-gather operation. Must be symmetric.
    

torch.ops.symm\_mem.one\_shot\_all\_reduce(_input: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _reduce\_op: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_, _group\_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.one_shot_all_reduce "Link to this definition")

Performs a one-shot all-reduce operation on the input tensor.

Warning

All symm\_mem collectives for a given group must be issued from a single CUDA stream. See [`multimem_all_reduce_()`](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.multimem_all_reduce_ "torch.ops.symm_mem.multimem_all_reduce_")
 for details.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Input tensor to perform all-reduce on. Must be symmetric.
    
*   **reduce\_op** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Reduction operation to perform. Currently only “sum” is supported.
    
*   **group\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Name of the group to perform all-reduce on.
    

torch.ops.symm\_mem.one\_shot\_all\_reduce\_out(_input: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _reduce\_op: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_, _group\_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_, _out: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.one_shot_all_reduce_out "Link to this definition")

Performs a one-shot all-reduce operation based on the input tensor and writes the result to the output tensor.

Warning

All symm\_mem collectives for a given group must be issued from a single CUDA stream. See [`multimem_all_reduce_()`](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.multimem_all_reduce_ "torch.ops.symm_mem.multimem_all_reduce_")
 for details.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Input tensor to perform all-reduce on. Must be symmetric.
    
*   **reduce\_op** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Reduction operation to perform. Currently only “sum” is supported.
    
*   **group\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Name of the group to perform all-reduce on.
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Output tensor to store the result of the all-reduce operation. Can be a regular tensor.
    

torch.ops.symm\_mem.two\_shot\_all\_reduce\_(_input: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _reduce\_op: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_, _group\_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.two_shot_all_reduce_ "Link to this definition")

Performs a two-shot all-reduce operation on the input tensor.

Warning

All symm\_mem collectives for a given group must be issued from a single CUDA stream. See [`multimem_all_reduce_()`](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.multimem_all_reduce_ "torch.ops.symm_mem.multimem_all_reduce_")
 for details.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Input tensor to perform all-reduce on. Must be symmetric.
    
*   **reduce\_op** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Reduction operation to perform. Currently only “sum” is supported.
    
*   **group\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Name of the group to perform all-reduce on.
    

torch.ops.symm\_mem.nvshmem\_broadcast(_input: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _root: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_, _group\_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.nvshmem_broadcast "Link to this definition")

Broadcasts the input tensor from the root rank to all ranks in the group using NVSHMEM, in place. This op is host/stream-initiated and works both intra-node and across nodes. On non-root ranks the contents of input are overwritten with the data from the root; on the root rank they are unchanged. The operation is issued on the current CUDA stream and returns input.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Tensor to broadcast (on the root) or receive into (on other ranks). Must be symmetric.
    
*   **root** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Rank within the group that holds the source data. Must be smaller than the group size.
    
*   **group\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Name of the group to perform the broadcast on.
    

torch.ops.symm\_mem.nvshmem\_put(_tensor: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _peer: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.nvshmem_put "Link to this definition")

Performs a one-sided, host/stream-initiated put over NVSHMEM: copies the local tensor into the same symmetric allocation on peer. Works both intra-node and across nodes (e.g. over RDMA/RoCE). The op only issues the transfer on the current CUDA stream; it does not wait for remote completion, so you must provide your own synchronization (e.g. nvshmem\_put\_with\_signal / nvshmem\_wait\_for\_signal) before consuming the data on the peer.

Parameters:

*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Symmetric, contiguous tensor whose data is sent, and which also names the destination allocation on the peer.
    
*   **peer** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Rank to send the data to. Must be smaller than the world size.
    

torch.ops.symm\_mem.nvshmem\_get(_tensor: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _peer: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.nvshmem_get "Link to this definition")

Performs a one-sided, host/stream-initiated get over NVSHMEM: copies the data from the same symmetric allocation on peer into the local tensor. Works both intra-node and across nodes. The transfer is issued on the current CUDA stream.

Parameters:

*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Symmetric, contiguous tensor that receives the data, and which also names the source allocation on the peer.
    
*   **peer** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Rank to read the data from. Must be smaller than the world size.
    

torch.ops.symm\_mem.nvshmem\_get\_out(_dst: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _hdl: SymmetricMemory_, _offset: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_, _size: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_, _peer: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.nvshmem_get_out "Link to this definition")

Low-level, host/stream-initiated get that copies size elements starting at element offset from the peer’s symmetric allocation (the one backing hdl) into dst. This is the primitive backing the higher-level [`get()`](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.distributed._symmetric_memory.get "torch.distributed._symmetric_memory.get")
 helper; most users should prefer that helper. The copy is issued on the current CUDA stream.

Parameters:

*   **dst** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Local CUDA tensor to receive the data. Must be contiguous, on the same device as hdl, and hold at least size elements.
    
*   **hdl** (_SymmetricMemory_) – Handle returned by rendezvous, identifying the peer’s symmetric allocation to read from.
    
*   **offset** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Starting element (in dst’s dtype) within the peer allocation. Must be non-negative.
    
*   **size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Number of elements to copy. Must be non-negative.
    
*   **peer** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Rank to read the data from. Must be a valid rank in the group.
    

torch.ops.symm\_mem.nvshmem\_put\_with\_signal(_tensor: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _sigpad: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _signal: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_, _peer: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.nvshmem_put_with_signal "Link to this definition")

Performs a one-sided put of tensor to the same symmetric allocation on peer, and atomically sets the peer’s signal location sigpad to signal once the data transfer has completed. This lets the peer detect arrival of the data via nvshmem\_wait\_for\_signal. Issued on the current CUDA stream.

Parameters:

*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Symmetric tensor whose data is sent, and which also names the destination allocation on the peer.
    
*   **sigpad** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Symmetric signal pad on the peer to set once the transfer completes.
    
*   **signal** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Value to set the peer’s sigpad to.
    
*   **peer** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Rank to send the data to.
    

torch.ops.symm\_mem.nvshmem\_wait\_for\_signal(_sigpad: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _signal: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_, _peer: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.nvshmem_wait_for_signal "Link to this definition")

Blocks the current CUDA stream until the local signal location sigpad equals signal. Typically paired with nvshmem\_put\_with\_signal on the sender side to wait for incoming data.

Parameters:

*   **sigpad** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Local signal pad to poll.
    
*   **signal** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Value to wait for.
    
*   **peer** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Reserved for future use.
    

torch.ops.symm\_mem.nvshmem\_all\_to\_all(_input: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _out: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _group\_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.nvshmem_all_to_all "Link to this definition")

Performs an equal-split all-to-all operation using NVSHMEM. Unlike the pointer-based collectives, this op is host/stream-initiated and runs over the NVSHMEM transport, so it works both intra-node and across nodes (e.g. over RDMA/RoCE) without requiring peer buffers to be directly addressable from the GPU.

The input is divided into group\_size equal-sized chunks; chunk i is sent to rank i, and the chunk received from rank i is placed at position i in the output.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Input tensor to perform all-to-all on. Must be symmetric and contiguous. Its number of elements must be divisible by the group size.
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Output tensor to store the result of the all-to-all operation. Must be symmetric and contiguous, and have the same number of elements and dtype as input.
    
*   **group\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Name of the group to perform all-to-all on.
    

torch.ops.symm\_mem.all\_to\_all\_vdev(_input: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _out: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _in\_splits: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _out\_splits\_offsets: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _group\_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.all_to_all_vdev "Link to this definition")

Performs an all-to-all-v operation using NVSHMEM, with split information provided on device.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Input tensor to perform all-to-all on. Must be symmetric.
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Output tensor to store the result of the all-to-all operation. Must be symmetric.
    
*   **in\_splits** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Tensor containing splits of data to send to each peer. Must be symmetric. Must be of size (group\_size,). The splits are in the unit of elements in the 1st dimension.
    
*   **out\_splits\_offsets** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Tensor containing the splits and offsets of data received from each peer. Must be symmetric. Must be of size (2, group\_size). The rows are (in order): output splits and output offsets.
    
*   **group\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Name of the group to perform all-to-all on.
    

torch.ops.symm\_mem.all\_to\_all\_vdev\_2d(_input: Tensor_, _out: Tensor_, _in\_splits: Tensor_, _out\_splits\_offsets: Tensor_, _group\_name: str_\[, _major\_align: int \= None_\]) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.all_to_all_vdev_2d "Link to this definition")

Perform a 2D all-to-all-v operation using NVSHMEM, with split information provided on device. In Mixture of Experts models, this operation can be used to dispatch tokens.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Input tensor to perform all-to-all on. Must be symmetric.
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Output tensor to store the result of the all-to-all operation. Must be symmetric.
    
*   **in\_splits** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Tensor containing the splits of data to send to each expert. Must be symmetric. Must be of size (group\_size \* ne,), where ne is the number of experts per rank. The splits are in the unit of elements in the 1st dimension.
    
*   **out\_splits\_offsets** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Tensor containing the splits and offsets of data received from each peer. Must be symmetric. Must be of size (2, group\_size \* ne). The rows are (in order): output splits and output offsets.
    
*   **group\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Name of the group to perform all-to-all on.
    
*   **major\_align** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Optional alignment for the major dimension of the output chunk for each expert. If not provided, the alignment is assumed to be 1. Any alignment adjustment will be reflected in the output offsets.
    

A 2D AllToAllv shuffle is illustrated below: (world\_size = 2, ne = 2, total number of experts = 4):

Source: |       Rank 0      |       Rank 1      |
        | c0 | c1 | c2 | c3 | d0 | d1 | d2 | d3 |

Dest  : |       Rank 0      |       Rank 1      |
        | c0 | d0 | c1 | d1 | c2 | d2 | c3 | d3 |

Copy to clipboard

where each c\_i / d\_i are slices of the input tensor, targeting expert i, with length indicated by input splits. That is, the 2D AllToAllv shuffle achieves a transpose from rank-major order at input to expert-major order at output.

If major\_align is not 1, the output offsets of c1, c2, c3 will be up-aligned to this value. For example, if c0 has length 5 and d0 has length 7 (making a total of 12), and if the major\_align is set to 16, the output offset of c1 will be 16. Similar for c2 and c3. This value has no effect on the offset of the minor dimension, i.e. d0, d1, d2 and d3. Note: since cutlass does not support empty bins, we set the aligned length to major\_align if it is 0. See [pytorch/pytorch#152668](https://github.com/pytorch/pytorch/issues/152668)
.

torch.ops.symm\_mem.all\_to\_all\_vdev\_2d\_offset(_Tensor input_, _Tensor out_, _Tensor in\_splits\_offsets_, _Tensor out\_splits\_offsets_, _str group\_name_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.all_to_all_vdev_2d_offset "Link to this definition")

Perform a 2D AllToAllv shuffle operation, with input split and offset information provided on device. The input offsets are not required to be exact prefix sum of the input splits, i.e. paddings are allowed between the split chunks. The paddings, however, will not be transferred to peer ranks.

In Mixture of Experts models, this operation can be used to combine tokens processed by experts on parallel ranks. This operation can be viewed as an “reverse” operation to the all\_to\_all\_vdev\_2d operation (which shuffles tokens to experts).

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Input tensor to perform all-to-all on. Must be symmetric.
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Output tensor to store the result of the all-to-all operation. Must be symmetric.
    
*   **in\_splits\_offsets** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Tensor containing the splits and offsets of data to send to each expert. Must be symmetric. Must be of size (2, group\_size \* ne), where ne is the number of experts. The rows are (in order): input splits and input offsets. The splits are in the unit of elements in the 1st dimension.
    
*   **out\_splits\_offsets** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Tensor containing the splits and offsets of data received from each peer. Must be symmetric. Must be of size (2, group\_size \* ne). The rows are (in order): output splits and output offsets.
    
*   **group\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Name of the group to perform all-to-all on.
    

torch.ops.symm\_mem.tile\_reduce(_in\_tile: Tensor_, _out\_tile: Tensor_, _root: int_, _group\_name: str_\[, _reduce\_op: str \= 'sum'_\]) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.tile_reduce "Link to this definition")

Reduces a 2D tile from all ranks to a specified root rank within a process group.

Parameters:

*   **in\_tile** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Input 2D tensor to be reduced. Must be symmetrically allocated.
    
*   **out\_tile** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Output 2D tensor to contain the result of the reduction. Must be symmetric and have the same shape, dtype, and device as in\_tile.
    
*   **root** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The rank of the process in the specified group that will receive the reduced result.
    
*   **group\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The name of the symmetric memory process group to perform the reduction in.
    
*   **reduce\_op** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The reduction operation to perform. Currently, only `"sum"` is supported. Defaults to `"sum"`.
    

This function reduces in\_tile tensors from all members of the group, writing the result to out\_tile at the root rank. All ranks must participate and provide the same group\_name and tensor shapes.

Example:

\>>> 
\>>> \# Reduce the bottom-right quadrant of a tensor
\>>> tile\_size \= full\_size // 2
\>>> full\_inp \= symm\_mem.empty(full\_size, full\_size)
\>>> full\_out \= symm\_mem.empty(full\_size, full\_size)
\>>> s \= slice(tile\_size, 2 \* tile\_size)
\>>> in\_tile \= full\_inp\[s, s\]
\>>> out\_tile \= full\_out\[s, s\]
\>>> torch.ops.symm\_mem.tile\_reduce(in\_tile, out\_tile, root\=0, group\_name)

Copy to clipboard

torch.ops.symm\_mem.multi\_root\_tile\_reduce(_in\_tiles: list\[Tensor\], out\_tile: Tensor, roots: list\[int\], group\_name: str, \[reduce\_op: str \= 'sum'\]_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#torch.ops.symm_mem.multi_root_tile_reduce "Link to this definition")

Perform multiple tile reductions concurrently, with each tile reduced to a separate root.

: param list\[Tensor\] in\_tiles: A list of input tensors. : param Tensor out\_tile: Output tensor to contain the reduced tile. : param list\[int\] roots: A list of root ranks each corresponding to an input tile in in\_tiles, in the same order. A rank cannot be a root more than once. : param str group\_name: Name of the group to use for the collective operation. : param str reduce\_op: Reduction operation to perform. Currently only “sum” is supported.

Example:

\>>> 
\>>> \# Reduce four quadrants of a tensor, each to a different root
\>>> tile\_size \= full\_size // 2
\>>> full\_inp \= symm\_mem.empty(full\_size, full\_size)
\>>> s0 \= slice(0, tile\_size)
\>>> s1 \= slice(tile\_size, 2 \* tile\_size)
\>>> in\_tiles \= \[ full\_inp\[s0, s0\], full\_inp\[s0, s1\], full\_inp\[s1, s0\], full\_inp\[s1, s1\] \]
\>>> out\_tile \= symm\_mem.empty(tile\_size, tile\_size)
\>>> roots \= \[0, 1, 2, 3\]
\>>> torch.ops.symm\_mem.multi\_root\_tile\_reduce(in\_tiles, out\_tile, roots, group\_name)

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/symmetric_memory.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/symmetric_memory.md.txt)

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