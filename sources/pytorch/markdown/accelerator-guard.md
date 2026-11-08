Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/accelerator/guard.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/accelerator/guard.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/accelerator/guard.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/accelerator/guard.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/accelerator/guard.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/accelerator/guard.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/accelerator/guard.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/accelerator/guard.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/accelerator/guard.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/accelerator/guard.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/accelerator/guard.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/accelerator/guard.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/accelerator/guard.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/accelerator/guard.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/accelerator/guard.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/accelerator/guard.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/accelerator/guard.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/accelerator/guard.html)
[v1.13](https://docs.pytorch.org/docs/1.13/accelerator/guard.html)
[v1.12](https://docs.pytorch.org/docs/1.12/accelerator/guard.html)
[v1.11](https://docs.pytorch.org/docs/1.11/accelerator/guard.html)
[v1.10](https://docs.pytorch.org/docs/1.10/accelerator/guard.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/accelerator/guard.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/accelerator/guard.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/accelerator/guard.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/accelerator/guard.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/accelerator/guard.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/accelerator/guard.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/accelerator/guard.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/accelerator/guard.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/accelerator/guard.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/accelerator/guard.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/accelerator/guard.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/accelerator/guard.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/accelerator/guard.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/accelerator/guard.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/accelerator/guard.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/accelerator/guard.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/accelerator/guard.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/accelerator/guard.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/accelerator/guard.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/accelerator/guard.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/accelerator/guard.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/accelerator/guard.html)

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

Guard[#](https://docs.pytorch.org/docs/2.15/accelerator/guard.html#guard "Link to this heading")

=================================================================================================

Created On: Dec 08, 2025 | Last Updated On: Dec 09, 2025

Background[#](https://docs.pytorch.org/docs/2.15/accelerator/guard.html#background "Link to this heading")

-----------------------------------------------------------------------------------------------------------

The Device Guard abstraction in PyTorch provides RAII-based device and stream management, allowing code to temporarily switch device contexts and automatically restore the original device upon exiting a scope. This is essential for operations that need to ensure they execute on a specific device regardless of the current global device state.

For custom accelerators, a `CustomDeviceGuardImpl` that implements `c10::impl::DeviceGuardImplInterface` enables seamless integration with PyTorch’s device management infrastructure. For example, the OpenReg (Open Registration) integration example in PyTorch provides an `OpenRegGuardImpl` for the `PrivateUse1` dispatch key, with the following capabilities:

*   **Device Management**: Save, switch, and restore the current device index
    
*   **Stream Management**: Create, query, and switch between computation streams
    
*   **Event Management**: Record events on streams and synchronize execution
    

By registering `OpenRegGuardImpl` with PyTorch, user code can use device context managers like `torch.accelerator.device_index()`, and operations automatically handle device switching via the guard’s RAII semantics.

Design[#](https://docs.pytorch.org/docs/2.15/accelerator/guard.html#design "Link to this heading")

---------------------------------------------------------------------------------------------------

The guard interface class [`c10::impl::DeviceGuardImplInterface`](https://github.com/pytorch/pytorch/blob/main/c10/core/impl/DeviceGuardImplInterface.h "DeviceGuardImplInterface")
 provides three main categories of functionality:

### Device Management[#](https://docs.pytorch.org/docs/2.15/accelerator/guard.html#device-management "Link to this heading")

Device management enables switching between different accelerator devices and querying device information. This forms the foundation for device context management in PyTorch.

| Functionality | Description | Application Scenario |
| --- | --- | --- |
| **Device Query and Switch** | `exchangeDevice`, `setDevice`, `getDevice`, `uncheckedSetDevice` | Change the current device for operations; save/restore device context in RAII guards |
| **Device Count** | `deviceCount` (noexcept) | Query number of available devices; must return 0 on errors rather than throwing |
| **Device Synchronization** | `synchronizeDevice` | Wait for all operations on a device to complete |

### Stream Management[#](https://docs.pytorch.org/docs/2.15/accelerator/guard.html#stream-management "Link to this heading")

Streams enable asynchronous execution of operations on accelerator devices. Multiple streams allow concurrent execution of independent operations on the same device.

| Functionality | Description | Application Scenario |
| --- | --- | --- |
| **Stream Creation/Access** | `getStream`, `getDefaultStream`, `getNewStream`, `getStreamFromGlobalPool`, `exchangeStream` | Create and manage compute streams for asynchronous execution |
| **Stream Synchronization** | `queryStream`, `synchronizeStream` | Check stream completion status, wait for stream operations to finish |

### Event Management[#](https://docs.pytorch.org/docs/2.15/accelerator/guard.html#event-management "Link to this heading")

Events provide synchronization primitives for coordinating execution across streams and measuring execution time. They mark specific points in stream execution that can be awaited or timed.

| Functionality | Description | Application Scenario |
| --- | --- | --- |
| **Event Recording** | `record` | Mark a point in stream execution for later synchronization or timing |
| **Event Blocking** | `block` | Make one stream wait for an event from another stream (inter-stream dependencies) |
| **Event Synchronization** | `queryEvent`, `synchronizeEvent` | Check event completion, wait for event to complete |
| **Event Lifecycle** | `destroyEvent` | Free event resources when no longer needed |
| **Event Timing** | `elapsedTime` | Measure time between two events for performance profiling |

Implementation[#](https://docs.pytorch.org/docs/2.15/accelerator/guard.html#implementation "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

*   [Device Guard Implementation](https://docs.pytorch.org/docs/2.15/accelerator/device.html#device-guard)
    
*   Stream Guard Implementation (Upcoming)
    
*   Event Guard Implementation (Upcoming)
    

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/accelerator/guard.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/accelerator/guard.md.txt)

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