Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/accelerator/profiler.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/accelerator/profiler.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/accelerator/profiler.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/accelerator/profiler.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/accelerator/profiler.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/accelerator/profiler.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/accelerator/profiler.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/accelerator/profiler.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/accelerator/profiler.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/accelerator/profiler.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/accelerator/profiler.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/accelerator/profiler.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/accelerator/profiler.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/accelerator/profiler.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/accelerator/profiler.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/accelerator/profiler.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/accelerator/profiler.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/accelerator/profiler.html)
[v1.13](https://docs.pytorch.org/docs/1.13/accelerator/profiler.html)
[v1.12](https://docs.pytorch.org/docs/1.12/accelerator/profiler.html)
[v1.11](https://docs.pytorch.org/docs/1.11/accelerator/profiler.html)
[v1.10](https://docs.pytorch.org/docs/1.10/accelerator/profiler.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/accelerator/profiler.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/accelerator/profiler.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/accelerator/profiler.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/accelerator/profiler.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/accelerator/profiler.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/accelerator/profiler.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/accelerator/profiler.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/accelerator/profiler.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/accelerator/profiler.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/accelerator/profiler.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/accelerator/profiler.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/accelerator/profiler.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/accelerator/profiler.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/accelerator/profiler.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/accelerator/profiler.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/accelerator/profiler.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/accelerator/profiler.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/accelerator/profiler.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/accelerator/profiler.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/accelerator/profiler.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/accelerator/profiler.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/accelerator/profiler.html)

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

Profiler Integration[#](https://docs.pytorch.org/docs/2.15/accelerator/profiler.html#profiler-integration "Link to this heading")

==================================================================================================================================

Created On: Dec 26, 2025 | Last Updated On: Jul 07, 2026

Background[#](https://docs.pytorch.org/docs/2.15/accelerator/profiler.html#background "Link to this heading")

--------------------------------------------------------------------------------------------------------------

PyTorch ships a device-agnostic profiler that instruments CPU-side operator dispatch, coordinates with accelerator collectors, captures Python stacks, and exports aggregated statistics or Chrome/Perfetto traces. For core architecture, see [`torch/csrc/profiler/README.md`](https://github.com/pytorch/pytorch/blob/main/torch/csrc/profiler/README.md "PyTorch Profiler README")
.

There are two primary integration paths for accelerators:

1.  Legacy autograd profiler:
    
    *   Can attach backend-specific hooks via `ProfilerStubs` to record device events and compute elapsed times.
        
    *   Works without Kineto; suitable for PrivateUse1 backends that want a minimal, self-contained path.
        
2.  Kineto `IActivityProfiler` plugin:
    
    *   Registers a full activity profiler with Kineto via `REGISTER_PRIVATEUSE1_PROFILER`.
        
    *   Wires Kineto sessions and correlation-ID plumbing; vendors extend this to emit kernel events, flow links, and Chrome/Perfetto trace compatibility.
        
    *   Requires Kineto at backend build time (`kineto_LIBRARY` from `find_package(Torch)`, guarded by `USE_KINETO`).
        

| Path | Python API | Profiler State | What it provides |
| --- | --- | --- | --- |
| Legacy (1) | `torch.autograd.profiler.profile(use_device="openreg")` (default `use_kineto=False`) | `KINETO_PRIVATEUSE1_FALLBACK` | Operator-level timing via `ProfilerStubs` device events |
| Kineto plugin (2) | `profile(activities=[ProfilerActivity.CPU, ProfilerActivity.PrivateUse1])` | `KINETO_PRIVATEUSE1` | Kineto session + correlation-ID plumbing; vendors add kernel events and flow links |

Both paths can coexist when the backend extension is built with Kineto available (`kineto_LIBRARY` from `find_package(Torch)`). The legacy stubs path always works; the Kineto plugin path requires `USE_KINETO` at backend build time. PyTorch core already exposes `REGISTER_PRIVATEUSE1_PROFILER`; vendors implement and register their `IActivityProfiler` in the backend extension.

Design[#](https://docs.pytorch.org/docs/2.15/accelerator/profiler.html#design "Link to this heading")

------------------------------------------------------------------------------------------------------

### Architecture overview[#](https://docs.pytorch.org/docs/2.15/accelerator/profiler.html#architecture-overview "Link to this heading")

| Layer | Responsibility | Source |
| --- | --- | --- |
| Python control plane | Owns profiler lifecycle (`prepare → start → stop → step`) and exposes user APIs such as `torch.autograd.profiler.profile`. | `torch/autograd/profiler.py` |
| Profiler stubs | Implements `torch::profiler::impl::ProfilerStubs` so the profiler can record device events, synchronize, iterate devices, and compute elapsed time. | `torch/csrc/profiler/stubs/` |
| Device runtime | Provides streams, events, and device guards used by the stubs; implementation is backend-specific. | Backend extension (vendor code) |

This layering keeps PyTorch device-agnostic: Python brokers the session, `ProfilerStubs` translate profiler requests into backend runtime calls, and the runtime interacts with the accelerator.

### Key contracts[#](https://docs.pytorch.org/docs/2.15/accelerator/profiler.html#key-contracts "Link to this heading")

*   **Record hooks**: `record()` must capture (optional) device index, allocate a backend event, optionally stash a CPU timestamp, and enqueue the event on the active stream.
    
*   **Elapsed time**: `elapsed()` is responsible for synchronizing individual events and returning durations in microseconds.
    
*   **Synchronization hooks**: `synchronize()` and `onEachDevice()` guarantee phase transitions (e.g., warmup → active) are aligned across devices.
    
*   **Annotations**: `mark`, `rangePush`, and `rangePop` can be implemented to enrich traces; otherwise they may be left as no-ops.
    

Implementation (Legacy way)[#](https://docs.pytorch.org/docs/2.15/accelerator/profiler.html#implementation-legacy-way "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

Here we use OpenReg (Open Registration) to illustrate the minimal set of hooks a `PrivateUse1` accelerator needs to expose so the profiler can attribute ATen ops, `record_function` ranges, and user code to device activity. OpenReg keeps upstream code untouched by translating profiler requests into its runtime calls, mirroring what a production accelerator would implement inside an out-of-tree extension.

OpenReg supports both paths: the legacy autograd profiler (`use_kineto=False`, the default) for operator-level timing via stubs, and the modern `torch.profiler.profile` API (`use_kineto=True`) for the Kineto plugin path described below.

### Profiler stubs (C++)[#](https://docs.pytorch.org/docs/2.15/accelerator/profiler.html#profiler-stubs-c "Link to this heading")

[`torch::profiler::impl::OpenRegMethods`](https://github.com/pytorch/pytorch/blob/main/test/cpp_extensions/open_registration_extension/torch_openreg/csrc/profiler/stubs/openreg.cpp "OpenReg profiler stubs")
 inherits from `ProfilerStubs` and wires the hooks described above:

| Method | Purpose |
| --- | --- |
| `record` | Grabs the current `OpenRegStream`, creates an `orEvent`, captures an optional CPU timestamp via `c10::getTime()`, and records the event on the stream. |
| `elapsed` | Synchronizes both events, calls `orEventElapsedTime`, and converts milliseconds to microseconds for the profiler. |
| `onEachDevice` | Uses `c10::DeviceGuard(DeviceType::PrivateUse1)` to iterate over `torch.openreg.device_count()` so schedulers can run per-device setup or teardown. |
| `synchronize` | Calls `orDeviceSynchronize()` to align device work with CPU scheduling phases. |
| `enabled` and annotation shims | Report availability and provide placeholder implementations for mark/push/pop. |

The constructor registers the methods once via `registerPrivateUse1Methods(&methods);`, making them discoverable whenever the profiler is enabled with `use_device="openreg"`.

### Python control plane[#](https://docs.pytorch.org/docs/2.15/accelerator/profiler.html#python-control-plane "Link to this heading")

On the Python side, no new entrypoint is required—developers use the standard autograd profiler:

from torch.autograd.profiler import profile as autograd\_profile
from torch.profiler import record\_function

with autograd\_profile(use\_device\="openreg", record\_shapes\=True) as prof:
    with record\_function("matmul"):
        x \= torch.randn(512, 512, device\="openreg")
        y \= torch.randn(512, 512, device\="openreg")
        z \= x @ y

print(prof.key\_averages().table(sort\_by\="cpu\_time\_total", row\_limit\=10))
prof.export\_chrome\_trace("openreg\_trace.json")

Copy to clipboard

### Data capture flow[#](https://docs.pytorch.org/docs/2.15/accelerator/profiler.html#data-capture-flow "Link to this heading")

1.  User code enters `autograd_profile(use_device="openreg")`.
    
2.  The profiler transitions to `ProfilerState.KINETO_PRIVATEUSE1_FALLBACK`.
    
3.  The profiler asks the active backend to `record()` an event.
    
4.  The OpenReg stubs allocate `orEvent` objects, attach them to the current stream, and stash CPU timestamps.
    
5.  When events end, the profiler calls `elapsed()` to compute durations.
    

Implementation (Kineto Plugin)[#](https://docs.pytorch.org/docs/2.15/accelerator/profiler.html#implementation-kineto-plugin "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

Note

This section covers the Kineto `IActivityProfiler` plugin path for kernel-level tracing. It requires `USE_KINETO` at build time. All Kineto-dependent code must be guarded with `#ifdef USE_KINETO`.

The plugin path has two layers: a **device library** component (the CUPTI analog) and the **PyTorch integration** layer. OpenReg keeps these clearly separated.

### Device library: correlation tracking[#](https://docs.pytorch.org/docs/2.15/accelerator/profiler.html#device-library-correlation-tracking "Link to this heading")

The device library provides `openreg::profiler::OpenRegTracer` (`third_party/openreg/csrc/tracer.h/.cpp`) — a singleton with a thread-local correlation-ID stack and an atomic enable/disable flag that the profiler session uses to control the recording window.

Kineto pushes/pops correlation IDs through the session. The session calls C-style activity APIs in `openreg.h` (mirroring CUPTI):

*   `orActivityEnableTracing()` / `orActivityDisableTracing()` — control the recording window
    
*   `orActivityPushExternalCorrelationId()` / `orActivityPopExternalCorrelationId()` — maintain the correlation stack
    

A real vendor’s equivalent would be their device tracing SDK (e.g., CUPTI for CUDA).

### PyTorch integration: IActivityProfiler and IActivityProfilerSession[#](https://docs.pytorch.org/docs/2.15/accelerator/profiler.html#pytorch-integration-iactivityprofiler-and-iactivityprofilersession "Link to this heading")

Implement the two Kineto interfaces from `third_party/kineto/libkineto/include/IActivityProfiler.h`. In OpenReg, these live in `torch_openreg/csrc/profiler/` — the backend extension integration layer.

*   **`IActivityProfiler`** — stateless factory. Two `configure()` overloads both create and return a session:
    
    *   `configure(activity_types, config)` — synchronous overload; required by the interface. The OpenReg stub implements this as the core session-creation path.
        
    *   `configure(ts_ms, duration_ms, activity_types, config)` — Kineto’s child-profiler path calls this overload for all traces (including on-demand), passing `profileStartTime()` epoch ms and `profileDuration()` ms. The OpenReg stub ignores scheduling and delegates to the first overload; vendors use `ts_ms`/`duration_ms` to defer device-SDK activation.
        
*   **`IActivityProfilerSession`** — per-trace session. `start()`/`stop()` manage the profiling window and toggle activity tracing via `orActivityEnableTracing()`/`orActivityDisableTracing()`; `getTraceBuffer()` returns the buffer to Kineto.
    
    *   **Reference stub**: `processTrace()` only sets the trace span (`traceBuffer_.span = TraceSpan(startTs_, endTs_, "openreg")`); it emits no kernel records.
        
    *   **Vendor extension**: replace `processTrace()` to flush records from your device tracing SDK, emit `GenericTraceActivity` entries with timestamps (µs), correlation IDs, and flow links (`flow.id = correlationId`, `flow.type = kLinkAsyncCpuGpu`, `flow.start = 0`).
        

### Registration and build[#](https://docs.pytorch.org/docs/2.15/accelerator/profiler.html#registration-and-build "Link to this heading")

Register with one line: `REGISTER_PRIVATEUSE1_PROFILER(OpenRegActivityProfiler)`. The macro (defined in `torch/csrc/profiler/standalone/privateuse1_profiler.h`) creates a static registration object that forwards a factory to Kineto at profiler init time.

Kineto is on by default in PyTorch; no special build flags are needed unless explicitly disabled it with `USE_KINETO=0`. In backend extension, `find_package(Torch)` sets `kineto_LIBRARY`; link against `kineto` and `torch_cpu_library`, and guard Kineto code with `#ifdef USE_KINETO`. Without Kineto, the plugin compiles as a no-op and only the legacy stubs path is available.

### Usage[#](https://docs.pytorch.org/docs/2.15/accelerator/profiler.html#usage "Link to this heading")

import torch
from torch.profiler import profile, ProfilerActivity

with profile(activities\=\[ProfilerActivity.CPU, ProfilerActivity.PrivateUse1\]) as prof:
    x \= torch.randn(512, 512, device\="openreg")
    y \= torch.randn(512, 512, device\="openreg")
    z \= x @ y

prof.export\_chrome\_trace("kernel\_trace.json")

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/accelerator/profiler.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/accelerator/profiler.md.txt)

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