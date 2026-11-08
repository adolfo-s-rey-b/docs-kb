Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/torch_cuda_memory.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/torch_cuda_memory.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/torch_cuda_memory.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/torch_cuda_memory.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/torch_cuda_memory.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/torch_cuda_memory.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/torch_cuda_memory.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/torch_cuda_memory.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/torch_cuda_memory.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/torch_cuda_memory.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/torch_cuda_memory.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/torch_cuda_memory.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/torch_cuda_memory.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/torch_cuda_memory.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/torch_cuda_memory.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/torch_cuda_memory.html)
[v1.13](https://docs.pytorch.org/docs/1.13/torch_cuda_memory.html)
[v1.12](https://docs.pytorch.org/docs/1.12/torch_cuda_memory.html)
[v1.11](https://docs.pytorch.org/docs/1.11/torch_cuda_memory.html)
[v1.10](https://docs.pytorch.org/docs/1.10/torch_cuda_memory.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/torch_cuda_memory.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/torch_cuda_memory.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/torch_cuda_memory.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/torch_cuda_memory.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/torch_cuda_memory.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/torch_cuda_memory.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/torch_cuda_memory.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/torch_cuda_memory.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/torch_cuda_memory.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/torch_cuda_memory.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/torch_cuda_memory.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/torch_cuda_memory.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/torch_cuda_memory.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/torch_cuda_memory.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/torch_cuda_memory.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/torch_cuda_memory.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/torch_cuda_memory.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/torch_cuda_memory.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/torch_cuda_memory.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/torch_cuda_memory.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/torch_cuda_memory.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/torch_cuda_memory.html)

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

Understanding CUDA Memory Usage[#](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#understanding-cuda-memory-usage "Link to this heading")

=====================================================================================================================================================

Created On: Aug 23, 2023 | Last Updated On: Jul 07, 2026

To debug CUDA memory use, PyTorch provides a way to generate memory snapshots that record the state of allocated CUDA memory at any point in time, and optionally record the history of allocation events that led up to that snapshot.

The generated snapshots can then be drag and dropped onto the interactiver viewer hosted at [pytorch.org/memory\_viz](https://pytorch.org/memory_viz)
 which can be used to explore the snapshot.

Note

By default, the memory profiler only has visibility into CUDA device memory allocated and managed through the PyTorch allocator (e.g., `torch.empty(..., device='cuda')`, :func:`torch.cuda.memory.CUDAPluggableAllocator`). CPU pinned memory (host memory) can optionally be included by passing `record_pinned_host_memory=True` to :func:`~torch.cuda.memory._record_memory_history`; see [Including Pinned (Host) Memory](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#pinned-host-memory)
 below.

Any memory allocated directly from CUDA APIs in C++ (e.g., `cudaMalloc`, `cuMemCreate`) or via third-party Python bindings such as `cuda-python <https://github.com/NVIDIA/cuda-python>`\_ will not be visible in the PyTorch memory profiler. NCCL (used for distributed communication on CUDA devices) is a common example of a library that allocates GPU memory outside of PyTorch’s allocator. See [Identifying Non-PyTorch allocations](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#non-pytorch-alloc)
 for more info.

Generating a Snapshot[#](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#generating-a-snapshot "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

The common pattern for recording a snapshot is to enable memory history, run the code to be observed, and then save a file with a pickled snapshot:

\# enable memory history, which will
\# add tracebacks and event history to snapshots
torch.cuda.memory.\_record\_memory\_history()

run\_your\_code()
torch.cuda.memory.\_dump\_snapshot("my\_snapshot.pickle")

Copy to clipboard

Using the visualizer[#](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#using-the-visualizer "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

Open [https://pytorch.org/memory\_viz](https://pytorch.org/memory_viz)
 and drag/drop the pickled snapshot file into the visualizer. The visualizer is a javascript application that runs locally on your computer. It does not upload any snapshot data.

Including Pinned (Host) Memory[#](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#including-pinned-host-memory "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

By default, memory snapshots only include CUDA device memory. To also capture CPU pinned memory allocations (e.g., tensors created with `pin_memory=True`), pass `record_pinned_host_memory=True`:

torch.cuda.memory.\_record\_memory\_history(record\_pinned\_host\_memory\=True)

run\_your\_code()
snapshot \= torch.cuda.memory.\_snapshot()
\# Host allocator data is in snapshot\["host\_segments"\] and snapshot\["host\_traces"\]
torch.cuda.memory.\_dump\_snapshot("my\_snapshot.pickle")

Copy to clipboard

To record only host pinned memory and skip the CUDA device allocator entirely, pair `record_pinned_host_memory=True` with `record_cuda=False`:

torch.cuda.memory.\_record\_memory\_history(record\_pinned\_host\_memory\=True, record\_cuda\=False)

Copy to clipboard

Note

The [pytorch.org/memory\_viz](https://pytorch.org/memory_viz)
 visualizer does not yet support displaying host memory data. You can inspect `host_segments` and `host_traces` programmatically from the snapshot dict.

Active Memory Timeline[#](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#active-memory-timeline "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

The Active Memory Timeline shows all the live tensors over time in the snapshot on a particular GPU. Pan/Zoom over the plot to look at smaller allocations. Mouse over allocated blocks to see a stack trace for when that block was allocated, and details like its address. The detail slider can be adjusted to render fewer allocations and improve performance when there is a lot of data.

![_images/active_memory_timeline.png](https://docs.pytorch.org/docs/2.15/_images/active_memory_timeline.png)

Allocator State History[#](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#allocator-state-history "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

The Allocator State History shows individual allocator events in a timeline on the left. Select an event in the timeline to see a visual summary of the allocator state at that event. This summary shows each individual segment returned from cudaMalloc and how it is split up into blocks of individual allocations or free space. Mouse over segments and blocks to see the stack trace when the memory was allocated. Mouse over events to see the stack trace when the event occurred, such as when a tensor was freed. Out of memory errors are reported as OOM events. Looking at the state of memory during an OOM may provide insight into why an allocation failed even though reserved memory still exists.

![_images/allocator_state_history.png](https://docs.pytorch.org/docs/2.15/_images/allocator_state_history.png)

The stack trace information also reports the address at which an allocation occurred. The address b7f064c000000\_0 refers to the (b)lock at address 7f064c000000 which is the “\_0”th time this address was allocated. This unique string can be looked up in the Active Memory Timeline and searched in the Active State History to examine the memory state when a tensor was allocated or freed.

Identifying Non-PyTorch allocations[#](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#non-pytorch-alloc "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

If you suspect CUDA memory is being allocated outside of PyTorch, you can collect the raw CUDA allocation info using the pynvml package, and compare that to the allocation reported by pytorch.

To collect raw memory usage outside pytorch, use `device_memory_used()`

import torch
device\_idx \= ...
print(torch.cuda.device\_memory\_used(device\_idx))

Copy to clipboard

Snapshot API Reference[#](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#snapshot-api-reference "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

torch.cuda.memory.\_record\_memory\_history(_enabled\='all'_, _context\='all'_, _stacks\='all'_, _max\_entries\=9223372036854775807_, _device\=None_, _clear\_history\=False_, _compile\_context\=False_, _global\_record\_annotations\=False_, _skip\_actions\=None_, _record\_pinned\_host\_memory\=False_, _record\_cuda\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/memory.py#L898)
[#](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#torch.cuda.memory._record_memory_history "Link to this definition")

Enable recording of stack traces associated with memory allocations, so you can tell what allocated any piece of memory in [`torch.cuda.memory._snapshot()`](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#torch.cuda.memory._snapshot "torch.cuda.memory._snapshot")
.

In addition to keeping stack traces with each current allocation and free, this will also enable recording of a history of all alloc/free events.

Use [`torch.cuda.memory._snapshot()`](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#torch.cuda.memory._snapshot "torch.cuda.memory._snapshot")
 to retrieve this information, and the tools in \_memory\_viz.py to visualize snapshots.

### Buffer behavior[#](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#buffer-behavior "Link to this heading")

This will store up to max\_entries instances of TraceEntry when enabled. Python trace collection defaults to sys.maxsize, meaning long-running or indefinitely running jobs should set a reasonable limit to avoid excessive memory use. Expect each entry to be several KB.

Longer running workflows or those with smaller max\_entries values will only store the last accumulated max\_entries entries, meaning new entries overwrite older entries.

C++ implementation for reference to ring buffer implementation:

if (record\_history) {
  if (alloc\_trace\->size() < alloc\_trace\_max\_entries\_) {
    alloc\_trace\->emplace\_back(te);
  } else {
    (\*alloc\_trace)\[alloc\_trace\_next++\] \= te;
    if (alloc\_trace\_next \== alloc\_trace\_max\_entries\_) {
      alloc\_trace\_next \= 0;
    }
  }
}

Copy to clipboard

### Latency impact[#](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#latency-impact "Link to this heading")

The Python trace collection is fast (2us per trace), so you may consider enabling this on production jobs if you anticipate ever having to debug memory issues.

C++ trace collection is also fast (~50ns/frame), which for many typical programs works out to ~2us per trace, but can vary depending on stack depth.

param enabled:

None, disable recording memory history. “state”, keep information for currently allocated memory. “all”, additionally keep a history of all alloc/free calls. Defaults to “all”.

type enabled:

Literal\[None, “state”, “all”\], optional

param context:

None, Do not record any tracebacks. “state”, Record tracebacks for currently allocated memory. “alloc”, additionally keep tracebacks for alloc calls. “all”, additionally keep tracebacks for free calls. Defaults to “all”.

type context:

Literal\[None, “state”, “alloc”, “all”\], optional

param stacks:

“python”, include Python, TorchScript, and inductor frames in tracebacks “all”, additionally include C++ frames Defaults to “all”.

type stacks:

Literal\[“python”, “all”\], optional

param max\_entries:

Keep a maximum of max\_entries alloc/free events in the recorded history recorded.

type max\_entries:

int, optional

param clear\_history:

Clear history when enabling, defaults to False.

type clear\_history:

bool, optional

param skip\_actions:

List of action types to skip when recording memory history. This can be used to reduce memory overhead by excluding certain types of events from being recorded. Valid action types are:

*   “alloc”: Memory allocation events
    
*   “free\_requested”: Free requests (memory marked for freeing)
    
*   “free\_completed”: Completed free operations (memory actually freed)
    
*   “segment\_alloc”: Segment allocation from cudaMalloc
    
*   “segment\_free”: Segment freed back to CUDA via cudaFree
    
*   “oom”: Out-of-memory exceptions
    
*   “snapshot”: Memory snapshot generation events
    

For example, to skip recording free\_requested events: skip\_actions=\[“free\_requested”\]

Defaults to None (record all actions).

type skip\_actions:

list\[str\], optional

param record\_pinned\_host\_memory:

If True, also record memory history for the CPU pinned memory (host) allocator. Host allocator traces will appear in the `host_segments` and `host_traces` keys of the snapshot returned by [`_snapshot()`](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#torch.cuda.memory._snapshot "torch.cuda.memory._snapshot")
. Defaults to False.

type record\_pinned\_host\_memory:

bool, optional

param record\_cuda:

If True, record memory history for the CUDA device allocator. Set to False (together with `record_pinned_host_memory=True`) to record only host pinned memory. Defaults to True.

type record\_cuda:

bool, optional

torch.cuda.memory.\_snapshot(_device\=None_, _augment\_with\_fx\_traces\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/memory.py#L1045)
[#](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#torch.cuda.memory._snapshot "Link to this definition")

Save a snapshot of CUDA memory state at the time it was called.

The state is represented as a dictionary with the following structure.

class Snapshot(TypedDict):
    segments: List\[Segment\]
    device\_traces: List\[List\[TraceEntry\]\]

class Segment(TypedDict):
    \# Segments are memory returned from a cudaMalloc call.
    \# The size of reserved memory is the sum of all Segments.
    \# Segments are cached and reused for future allocations.
    \# If the reuse is smaller than the segment, the segment
    \# is split into more than one Block.
    \# empty\_cache() frees Segments that are entirely inactive.
    address: int
    total\_size: int  \#  cudaMalloc'd size of segment
    stream: int
    segment\_type: Literal\["small", "large"\]  \# 'large' (>1MB)
    segment\_pool\_id: Tuple\[\
        int, int\
    \]  \# id of the memory pool owning this segment
    allocated\_size: int  \# size of memory in use
    active\_size: int  \# size of memory in use or in active\_awaiting\_free state
    blocks: List\[Block\]

class Block(TypedDict):
    \# A piece of memory returned from the allocator, or
    \# current cached but inactive.
    size: int
    requested\_size: int  \# size requested during malloc, may be smaller than
    \# size due to rounding
    address: int
    state: Literal\[\
        "active\_allocated",  \# used by a tensor\
        "active\_awaiting\_free",  \# waiting for another stream to finish using\
        \# this, then it will become free\
        "inactive",\
    \]  \# free for reuse
    frames: List\[Frame\]  \# stack trace from where the allocation occurred

class Frame(TypedDict):
    filename: str
    line: int
    name: str
    \# Optional FX debug fields (present when augment\_with\_fx\_traces=True
    \# and the frame corresponds to FX-generated code)
    fx\_node\_op: str  \# FX node operation type (e.g., 'call\_function', 'output')
    fx\_node\_name: str  \# FX node name (e.g., 'linear', 'relu\_1')
    fx\_original\_trace: str  \# Original model source code stack trace

class TraceEntry(TypedDict):
    \# When \`torch.cuda.memory.\_record\_memory\_history()\` is enabled,
    \# the snapshot will contain TraceEntry objects that record each
    \# action the allocator took.
    action: Literal\[\
        "alloc"  \# memory allocated\
        "free\_requested",  \# the allocated received a call to free memory\
        "free\_completed",  \# the memory that was requested to be freed is now\
        \# able to be used in future allocation calls\
        "segment\_alloc",  \# the caching allocator ask cudaMalloc for more memory\
        \# and added it as a segment in its cache\
        "segment\_free",  \# the caching allocator called cudaFree to return memory\
        \# to cuda possibly trying free up memory to\
        \# allocate more segments or because empty\_caches was called\
        "oom",  \# the allocator threw an OOM exception. 'size' is\
        \# the requested number of bytes that did not succeed\
        "snapshot",  \# the allocator generated a memory snapshot\
        \# useful to correlate a previously taken\
        \# snapshot with this trace\
        "annotate",  \# metadata was attached to a live allocation\
        \# via \_annotate\_tensor. 'addr' is the allocation's base\
        \# address and 'user\_metadata' holds the annotation\
    \]
    addr: int  \# not present for OOM
    frames: List\[Frame\]
    size: int
    stream: int
    user\_metadata: str  \# the calling thread's metadata at the time of
    \# the event, as set via \_set\_memory\_metadata (dicts appear as
    \# their JSON serialization)
    internal\_metadata: str  \# only present when allocator internals
    \# tagged the event (e.g. "mallocWithAddress" on the synthetic
    \# prefix-block malloc/free pair)
    device\_free: int  \# only present for OOM, the amount of
    \# memory cuda still reports to be free
    pool\_id: Tuple\[int, int\]  \# id of the memory pool for this entry

Copy to clipboard

Parameters:

*   **device** (_Device_) – Device to capture snapshot for. If None, captures for current device.
    
*   **augment\_with\_fx\_traces** – If True, augment stack trace frames with FX debug information that maps generated FX code back to original model source code. This adds fx\_node\_op, fx\_node\_name, fx\_original\_trace, and fx\_node\_info fields to Frame objects. Default: False.
    

Returns:

The Snapshot dictionary object

torch.cuda.memory.\_dump\_snapshot(_filename\='dump\_snapshot.pickle'_, _augment\_with\_fx\_traces\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/memory.py#L1156)
[#](https://docs.pytorch.org/docs/2.15/torch_cuda_memory.html#torch.cuda.memory._dump_snapshot "Link to this definition")

Save a pickled version of the torch.memory.\_snapshot() dictionary to a file.

This file can be opened by the interactive snapshot viewer at pytorch.org/memory\_viz

Snapshot file sizes scale with max\_entries and stack trace depth per entry, with several KB per entry. These can easily be in the GB range for longer running workflows with large max\_entries.

Parameters:

*   **filename** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – Name of the file to create. Defaults to “dump\_snapshot.pickle”.
    
*   **augment\_with\_fx\_traces** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If True, augment the snapshot with FX debug information before dumping. This maps generated FX code stack traces back to original model source code. Defaults to False.
    

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/torch_cuda_memory.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/torch_cuda_memory.md.txt)

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