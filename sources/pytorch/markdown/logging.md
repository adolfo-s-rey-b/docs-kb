Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/logging.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/logging.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/logging.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/logging.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/logging.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/logging.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/logging.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/logging.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/logging.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/logging.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/logging.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/logging.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/logging.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/logging.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/logging.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/logging.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/logging.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/logging.html)
[v1.13](https://docs.pytorch.org/docs/1.13/logging.html)
[v1.12](https://docs.pytorch.org/docs/1.12/logging.html)
[v1.11](https://docs.pytorch.org/docs/1.11/logging.html)
[v1.10](https://docs.pytorch.org/docs/1.10/logging.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/logging.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/logging.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/logging.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/logging.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/logging.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/logging.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/logging.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/logging.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/logging.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/logging.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/logging.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/logging.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/logging.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/logging.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/logging.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/logging.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/logging.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/logging.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/logging.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/logging.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/logging.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/logging.html)

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

torch.\_logging[#](https://docs.pytorch.org/docs/2.15/logging.html#torch-logging "Link to this heading")

=========================================================================================================

Created On: Apr 24, 2023 | Last Updated On: Jul 13, 2026

PyTorch has a configurable logging system, where different components can be given different log level settings. For instance, one component’s log messages can be completely disabled, while another component’s log messages can be set to maximum verbosity.

Warning

This feature is in beta and may have compatibility breaking changes in the future.

Warning

This feature has not been expanded to control the log messages of all components in PyTorch yet.

There are two ways to configure the logging system: through the environment variable `TORCH_LOGS` or the python API torch.\_logging.set\_logs.

|     |     |
| --- | --- |
| [`set_logs`](https://docs.pytorch.org/docs/2.15/generated/torch._logging.set_logs.html#torch._logging.set_logs "torch._logging.set_logs") | Sets the log level for individual components and toggles individual log artifact types. |

The environment variable `TORCH_LOGS` is a comma-separated list of `[+-]<component>` pairs, where `<component>` is a component specified below. The `+` prefix will decrease the log level of the component, displaying more log messages while the `-` prefix will increase the log level of the component and display fewer log messages. The default setting is the behavior when a component is not specified in `TORCH_LOGS`. In addition to components, there are also artifacts. Artifacts are specific pieces of debug information associated with a component that are either displayed or not displayed, so prefixing an artifact with `+` or `-` will be a no-op. Since they are associated with a component, enabling that component will typically also enable that artifact, unless that artifact was specified to be `off_by_default`. This option is specified in \_registrations.py for artifacts that are so spammy they should only be displayed when explicitly enabled. The following components and artifacts are configurable through the `TORCH_LOGS` environment variable (see torch.\_logging.set\_logs for the python API):

Components[#](https://docs.pytorch.org/docs/2.15/logging.html#components "Link to this heading")

-------------------------------------------------------------------------------------------------

Component names set the log level for a group of related loggers. Each component defaults to `logging.WARN` unless configured.

*   `all`: Special component which configures the default log level of all components.
    
*   `aot`: The log level for the AOTAutograd component.
    
*   `async_compile`: The log level for Inductor async compile workers.
    
*   `autograd`: The log level for autograd.
    
*   `c10d`: The log level for c10d communication operations in PyTorch Distributed.
    
*   `cache`: The log level for Inductor cache components.
    
*   `ddp`: The log level for `DistributedDataParallel` components.
    
*   `distributed`: The log level for PyTorch Distributed components.
    
*   `dtensor`: The log level for `DTensor` components.
    
*   `dynamic`: The log level for dynamic shapes.
    
*   `dynamo`: The log level for the TorchDynamo component.
    
*   `export`: The log level for export.
    
*   `fake_tensor`: The log level for FakeTensor.
    
*   `fsdp`: The log level for `FullyShardedDataParallel` components.
    
*   `inductor`: The log level for the TorchInductor component.
    
*   `native_dsl`: The log level for the native DSL component.
    
*   `onnx`: The log level for the ONNX exporter component.
    
*   `pp`: The log level for distributed pipelining.
    
*   `torch`: The log level for the top-level `torch` component.
    
*   `your.custom.module`: The log level for an arbitrary unregistered module. Provide the fully qualified name and the module will be enabled.
    

Artifacts[#](https://docs.pytorch.org/docs/2.15/logging.html#artifacts "Link to this heading")

-----------------------------------------------------------------------------------------------

Artifacts emit specific debug information. Each artifact defaults to `False` unless configured. Artifacts marked “off by default” are not enabled just by setting the log level of their parent component and must be explicitly enabled. Internal test-only artifacts are omitted.

*   `aot_graphs`: Prints the FX forward and backward graph generated by AOTDispatch, after partitioning.
    
*   `aot_graphs_effects`: Prints the FX forward and backward graph generated by AOTDispatch, useful for debugging effects processing.
    
*   `aot_joint_graph`: Prints the FX joint graph from AOTAutograd, prior to partitioning.
    
*   `annotation`: Logs detailed steps of creating annotations on graph nodes. Off by default.
    
*   `autotuning_inputs`: Logs per-kernel input tensor shapes/dtypes/strides during autotuning. Off by default.
    
*   `autotuning`: Logs autotuning choices, such as kernel source, performance, and tuning parameters. Off by default.
    
*   `auto_chunker`: Logs related to the auto chunker. Off by default.
    
*   `benchmarking`: Logs detailed Inductor benchmarking information. Off by default.
    
*   `bytecode`: Prints the original and modified bytecode from Dynamo. Off by default.
    
*   `caching`: Logs detailed Inductor caching information. Off by default.
    
*   `compiled_autograd`: Prints compiled autograd logs, including graphs.
    
*   `compiled_autograd_verbose`: Prints compiled autograd logs with C++ info, such as autograd node to FX node mappings. Off by default.
    
*   `compute_dependencies`: Logs Inductor compute dependency information. Off by default.
    
*   `cudagraphs`: Logs information from wrapping Inductor generated code with CUDA graphs.
    
*   `cudagraph_static_inputs`: Logs static input handling in Dynamo, AOT, and CUDA graphs. Off by default.
    
*   `ddp_graphs`: Prints individual graphs generated when DDPOptimizer splits graphs to trigger communication early.
    
*   `fusion`: Logs detailed Inductor fusion decisions. Off by default.
    
*   `graph`: Prints the Dynamo-traced graph before AOTDispatch in tabular format.
    
*   `graph_breaks`: Prints whenever Dynamo decides that it needs to graph break.
    
*   `graph_code`: Prints the Python code for the Dynamo-traced graph.
    
*   `graph_code_verbose`: Prints verbose FX pass logs, such as `tensorify_python_scalars` and `runtime_assert`.
    
*   `graph_region_expansion`: Logs detailed steps of the duplicate graph region tracker expansion algorithm. Off by default.
    
*   `graph_sizes`: Prints the sizes of all FX nodes in the Dynamo graph.
    
*   `guards`: Prints the guards for every compiled Dynamo frame.
    
*   `hierarchical_compile`: Logs debug info for hierarchical compilation. Off by default.
    
*   `incremental`: Logs incremental autotuning information. Off by default.
    
*   `inductor_metrics`: Logs Inductor metrics, such as `num_bytes`, `nodes_num_elem`, and `node_runtimes`. Off by default.
    
*   `ir_post_fusion`: Prints the IR after Inductor fusion passes. Off by default.
    
*   `ir_pre_fusion`: Prints the IR before Inductor fusion passes. Off by default.
    
*   `kernel_code`: Prints Inductor-generated code on a per-kernel basis. Off by default.
    
*   `loop_ordering`: Logs related to loop ordering. Off by default.
    
*   `loop_tiling`: Logs related to loop tiling. Off by default.
    
*   `node_runtime_estimation`: Logs node runtime estimation for compile-time optimization decisions. Off by default.
    
*   `not_implemented`: Prints log messages whenever a multi-dispatch returns `NotImplemented`.
    
*   `onnx_diagnostics`: Logs ONNX exporter diagnostics. Off by default.
    
*   `output_code`: Prints the code that Inductor generates, either Triton or C++. Off by default.
    
*   `overlap`: Logs detailed Inductor compute/communication overlap decisions. Off by default.
    
*   `overlap_scheduling`: Logs detailed Inductor overlap scheduling pass information. Off by default.
    
*   `perf_hints`: Logs Inductor performance hints. Off by default.
    
*   `post_grad_graphs`: Prints the FX graph generated after Inductor post-grad passes.
    
*   `pre_grad_graphs`: Prints the FX graph before Inductor pre-grad passes.
    
*   `recompiles`: Prints the reason why Dynamo recompiled a graph.
    
*   `recompiles_verbose`: Prints all guard checks that fail during a recompilation. Off by default.
    
*   `schedule`: Logs Inductor scheduler information. Off by default.
    
*   `side_effects`: Prints side effects that Dynamo code-generates, including mutations to variables, attributes, cells, and globals.
    
*   `sym_node`: Logs extra information for various `SymNode` operations. Off by default.
    
*   `trace_bytecode`: Prints the instruction and current stack as Dynamo traces bytecode.
    
*   `trace_call`: Prints per-expression tracing detail when available.
    
*   `trace_shape_events`: Logs traces for every `ShapeEnv` operation recorded for replay. Off by default.
    
*   `trace_source`: Prints the file name, line number, and source code as Dynamo executes bytecode.
    
*   `verbose_guards`: Prints verbose guard information. Off by default.
    

Examples:

`TORCH_LOGS="+dynamo,aot"` will set the log level of TorchDynamo to `logging.DEBUG` and AOT to `logging.INFO`

`TORCH_LOGS="-dynamo,+inductor"` will set the log level of TorchDynamo to `logging.ERROR` and TorchInductor to `logging.DEBUG`

`TORCH_LOGS="aot_graphs"` will enable the `aot_graphs` artifact

`TORCH_LOGS="+dynamo,schedule"` will enable set the log level of TorchDynamo to `logging.DEBUG` and enable the `schedule` artifact

`TORCH_LOGS="+some.random.module,schedule"` will set the log level of some.random.module to `logging.DEBUG` and enable the `schedule` artifact

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/logging.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/logging.md.txt)

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