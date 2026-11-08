Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/notes/large_scale_deployments.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/notes/large_scale_deployments.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/notes/large_scale_deployments.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/notes/large_scale_deployments.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/notes/large_scale_deployments.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/notes/large_scale_deployments.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/notes/large_scale_deployments.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/notes/large_scale_deployments.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/notes/large_scale_deployments.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/notes/large_scale_deployments.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/notes/large_scale_deployments.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/notes/large_scale_deployments.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/notes/large_scale_deployments.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/notes/large_scale_deployments.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/notes/large_scale_deployments.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/notes/large_scale_deployments.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/notes/large_scale_deployments.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/notes/large_scale_deployments.html)
[v1.13](https://docs.pytorch.org/docs/1.13/notes/large_scale_deployments.html)
[v1.12](https://docs.pytorch.org/docs/1.12/notes/large_scale_deployments.html)
[v1.11](https://docs.pytorch.org/docs/1.11/notes/large_scale_deployments.html)
[v1.10](https://docs.pytorch.org/docs/1.10/notes/large_scale_deployments.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/notes/large_scale_deployments.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/notes/large_scale_deployments.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/notes/large_scale_deployments.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/notes/large_scale_deployments.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/notes/large_scale_deployments.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/notes/large_scale_deployments.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/notes/large_scale_deployments.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/notes/large_scale_deployments.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/notes/large_scale_deployments.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/notes/large_scale_deployments.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/notes/large_scale_deployments.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/notes/large_scale_deployments.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/notes/large_scale_deployments.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/notes/large_scale_deployments.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/notes/large_scale_deployments.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/notes/large_scale_deployments.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/notes/large_scale_deployments.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/notes/large_scale_deployments.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/notes/large_scale_deployments.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/notes/large_scale_deployments.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/notes/large_scale_deployments.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/notes/large_scale_deployments.html)

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

Features for large-scale deployments[#](https://docs.pytorch.org/docs/2.15/notes/large_scale_deployments.html#features-for-large-scale-deployments "Link to this heading")

===========================================================================================================================================================================

Created On: May 06, 2026 | Last Updated On: May 06, 2026

This note talks about several extension points and tricks that might be useful when running PyTorch within a larger system or operating multiple systems using PyTorch in a larger organization.

The note assumes that you either build PyTorch from source in your organization or have an ability to statically link additional code to be loaded when PyTorch is used. Therefore, many of the hooks are exposed as C++ APIs that can be triggered once in a centralized place, e.g. in static initialization code.

[Fleet-wide operator profiling](https://docs.pytorch.org/docs/2.15/notes/large_scale_deployments.html#id1)
[#](https://docs.pytorch.org/docs/2.15/notes/large_scale_deployments.html#fleet-wide-operator-profiling "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

PyTorch comes with [`torch.autograd.profiler`](https://docs.pytorch.org/docs/2.15/autograd.html#module-torch.autograd.profiler "torch.autograd.profiler")
 capable of measuring time taken by individual operators on demand. One can use the same mechanism to do “always ON” measurements for any process running PyTorch. It might be useful for gathering information about PyTorch workloads running in a given process or across the entire set of machines.

New callbacks for any operator invocation can be added with `torch::addGlobalCallback`. Hooks will be called with `torch::RecordFunction` struct that describes invocation context (e.g. `name`). If enabled, `RecordFunction::inputs()` contains arguments of the function represented as `torch::IValue` variant type. Note, that inputs logging is relatively expensive and thus has to be enabled explicitly.

The operator callbacks also have access to `c10::ThreadLocalDebugInfo::get()` interface that returns a pointer to the struct holding the debug information. This debug information can be set earlier by using `at::DebugInfoGuard` object. Debug information is propagated through the forward (including async `fork` tasks) and backward passes and can be useful for passing some extra information about execution environment (e.g. model id) from the higher layers of the application down to the operator callbacks.

Invoking callbacks adds some overhead, so usually it’s useful to just randomly sample operator invocations. This can be enabled on per-callback basis with an optional sampling rate passed into `torch::addGlobalCallback`.

Note, that `addGlobalCallback` is not thread-safe and can be called only when no PyTorch operator is running. Usually, it’s a good idea to call them once during initialization.

Here’s an example:

// Called somewhere in the program beginning
void init() {
    // Sample one in a hundred operator runs randomly
    addGlobalCallback(
      RecordFunctionCallback(
        &onFunctionEnter,
        &onFunctionExit)
      .needsInputs(true)
      .samplingProb(0.01)
    );
    // Note, to enable observers in the model calling thread,
    // call enableRecordFunction() in the thread before running a model
}

void onFunctionEnter(const RecordFunction& fn) {
    std::cerr << "Before function " << fn.name()
              << " with " << fn.inputs().size() << " inputs" << std::endl;
}

void onFunctionExit(const RecordFunction& fn) {
    std::cerr << "After function " << fn.name();
}

Copy to clipboard

[API usage logging](https://docs.pytorch.org/docs/2.15/notes/large_scale_deployments.html#id2)
[#](https://docs.pytorch.org/docs/2.15/notes/large_scale_deployments.html#api-usage-logging "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When running in a broader ecosystem, for example in managed job scheduler, it’s often useful to track which binaries invoke particular PyTorch APIs. There exists simple instrumentation injected at several important API points that triggers a given callback. Because usually PyTorch is invoked in one-off python scripts, the callback fires only once for a given process for each of the APIs.

`c10::SetAPIUsageHandler` can be used to register API usage instrumentation handler. Passed argument is going to be an “api key” identifying used point, for example `python.import` for PyTorch extension import.

SetAPIUsageLogger(\[\](const std::string& event\_name) {
    std::cerr << "API was used: " << event\_name << std::endl;
});

Copy to clipboard

Note for developers: new API trigger points can be added in code with `C10_LOG_API_USAGE_ONCE("my_api")` in C++ or `torch._C._log_api_usage_once("my.api")` in Python.

[Common extension points](https://docs.pytorch.org/docs/2.15/notes/large_scale_deployments.html#id3)
[#](https://docs.pytorch.org/docs/2.15/notes/large_scale_deployments.html#common-extension-points "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

PyTorch APIs are generally loosely coupled and it’s easy to replace a component with specialized version. Common extension points include:

*   Custom operators implemented in C++ - see [tutorial for more details](https://pytorch.org/tutorials/advanced/cpp_extension.html)
    .
    
*   Custom data reading can be often integrated directly by invoking corresponding python library. Existing functionality of [`torch.utils.data`](https://docs.pytorch.org/docs/2.15/data.html#module-torch.utils.data "torch.utils.data")
     can be utilized by extending [`Dataset`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Dataset "torch.utils.data.Dataset")
     or [`IterableDataset`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.IterableDataset "torch.utils.data.IterableDataset")
    .
    

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/notes/large_scale_deployments.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/notes/large_scale_deployments.md.txt)

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