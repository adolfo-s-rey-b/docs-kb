Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.compile.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.compile.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.compile.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.compile.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.compile.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.compile.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.compile.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.compile.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.compile.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.compile.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.compile.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.compile.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.compile.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.compile.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.compile.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.compile.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.compile.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.compile.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.compile.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.compile.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.compile.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.compile.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.compile.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.compile.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.compile.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.compile.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.compile.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.compile.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.compile.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.compile.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.compile.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.compile.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.compile.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.compile.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.compile.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.compile.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.compile.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.compile.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.compile.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.compile.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.compile.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.compile.html)

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

torch.compile[#](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#torch-compile "Link to this heading")

=======================================================================================================================

torch.compile(_model: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[\_InputT\], \_RetT\]_, _\*_, _fullgraph: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_, _dynamic: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _backend: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[...\], [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\] \= 'inductor'_, _mode: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _options: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")\
\[\[...\], [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]\] | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _disable: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_, _dynamic\_shapes: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")
 \= None_) → [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[\_InputT\], \_RetT\][\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L3100)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#torch.compile "Link to this definition")

torch.compile(_model: [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _\*_, _fullgraph: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_, _dynamic: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _backend: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[...\], [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\] \= 'inductor'_, _mode: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _options: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")\
\[\[...\], [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]\] | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _disable: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_, _dynamic\_shapes: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")
 \= None_) → [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")\
\[\[\_InputT\], \_RetT\]\], [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")\
\[\[\_InputT\], \_RetT\]\]

Optimizes given model/function using TorchDynamo and specified backend. If you are compiling an [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
, you can also use [`torch.nn.Module.compile()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.compile "torch.nn.Module.compile")
 to compile the module inplace without changing its structure.

Concretely, for every frame executed within the compiled region, we will attempt to compile it and cache the compiled result on the code object for future use. A single frame may be compiled multiple times if previous compiled results are not applicable for subsequent calls (this is called a “guard failure”), you can use TORCH\_LOGS=guards to debug these situations. Multiple compiled results can be associated with a frame up to `torch._dynamo.config.recompile_limit`, which defaults to 8; at which point we will fall back to eager. Note that compile caches are per _code object_, not frame; if you dynamically create multiple copies of a function, they will all share the same code cache.

Parameters:

*   **model** (_Callable_ _or_ _None_) – Module/function to optimize
    
*   **fullgraph** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If False (default), torch.compile attempts to discover compilable regions in the function that it will optimize. If True, then we require that the entire function be capturable into a single graph. If this is not possible (that is, if there are graph breaks), then this will raise an error. This also opts into unbacked semantics, notably it will turn on capture\_scalar\_outputs and capture\_dynamic\_output\_shape\_ops on by default.
    
*   **dynamic** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
     _or_ _None_) – Use dynamic shape tracing. When this is True, we will up-front attempt to generate a kernel that is as dynamic as possible to avoid recompilations when sizes change. This may not always work as some operations/optimizations will force specialization; use TORCH\_LOGS=dynamic to debug overspecialization. When this is False, we will NEVER generate dynamic kernels, we will always specialize. By default (None), we automatically detect if dynamism has occurred and compile a more dynamic kernel upon recompile.
    
*   **backend** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _or_ _Callable_) –
    
    backend to be used
    
    *   ”inductor” is the default backend, which is a good balance between performance and overhead
        
    *   Non experimental in-tree backends can be seen with torch.\_dynamo.list\_backends()
        
    *   Experimental or debug in-tree backends can be seen with torch.\_dynamo.list\_backends(None)
        
    *   To register an out-of-tree custom backend: [https://docs.pytorch.org/docs/main/user\_guide/torch\_compiler/torch.compiler\_custom\_backends.html#registering-custom-backends](https://docs.pytorch.org/docs/main/user_guide/torch_compiler/torch.compiler_custom_backends.html#registering-custom-backends)
        
    
*   **mode** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) –
    
    Can be either “default”, “reduce-overhead”, “max-autotune” or “max-autotune-no-cudagraphs”
    
    *   ”default” is the default mode, which is a good balance between performance and overhead
        
    *   ”reduce-overhead” is a mode that reduces the overhead of python with CUDA graphs, useful for small batches. Reduction of overhead can come at the cost of more memory usage, as we will cache the workspace memory required for the invocation so that we do not have to reallocate it on subsequent runs. Reduction of overhead is not guaranteed to work; today, we only reduce overhead for CUDA only graphs which do not mutate inputs. There are other circumstances where CUDA graphs are not applicable; use TORCH\_LOGS=perf\_hints to debug.
        
    *   ”max-autotune” is a mode that leverages Triton or template based matrix multiplications on supported devices and Triton based convolutions on GPU. It enables CUDA graphs by default on GPU.
        
    *   ”max-autotune-no-cudagraphs” is a mode similar to “max-autotune” but without CUDA graphs
        
    *   To see the exact configs that each mode sets you can call torch.\_inductor.list\_mode\_options()
        
    
*   **options** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    ) –
    
    A dictionary of options to pass to the backend. Some notable ones to try out are
    
    *   epilogue\_fusion which fuses pointwise ops into templates. Requires max\_autotune to also be set
        
    *   max\_autotune which will profile to pick the best matmul configuration
        
    *   fallback\_random which is useful when debugging accuracy issues
        
    *   shape\_padding which pads matrix shapes to better align loads on GPUs especially for tensor cores
        
    *   triton.cudagraphs which will reduce the overhead of python with CUDA graphs
        
    *   trace.enabled which is the most useful debugging flag to turn on
        
    *   trace.graph\_diagram which will show you a picture of your graph after fusion
        
    *   guard\_filter\_fn that controls which dynamo guards are saved with compilations. This is an unsafe feature and there is no backward compatibility guarantee provided for dynamo guards as data types. For stable helper functions to use, see the documentation in torch.compiler, for example: - torch.compiler.skip\_guard\_on\_inbuilt\_nn\_modules\_unsafe - torch.compiler.skip\_guard\_on\_all\_nn\_modules\_unsafe - torch.compiler.keep\_tensor\_guards\_unsafe
        
    *   For inductor you can see the full list of configs that it supports by calling torch.\_inductor.list\_options()
        
    
*   **name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _or_ _None_) – Optional identifier for the compiled region. When supported by downstream tooling, this is surfaced on wrapped compiled-region higher-order operators and other debug metadata.
    
*   **disable** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Turn torch.compile() into a no-op for testing
    
*   **recompile\_limit** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ _None_) – Maximum number of recompilations allowed for this `torch.compile()` call before falling back to eager. If None (default), uses the global `torch._dynamo.config.recompile_limit` (default 8). With `fullgraph=True`, exceeding the limit raises `FailOnRecompileLimitHit`.
    
*   **isolate\_recompiles** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If True, this `torch.compile()` call tracks recompilations independently. By default, all `torch.compile()` calls on the same function share a single set of compiled entries, so one call’s recompilations count against every other call’s limit. With `isolate_recompiles=True`, each call gets its own isolated set of entries. Lookups for an isolated compile call will still fall back to entries from non-isolated compile calls (BC-friendly reuse), but new compilations are stored separately. `recompile_limit` is checked per-region; `accumulated_recompile_limit` is a global cap across all regions. Default-strategy behavior is asymmetric: SKIP decisions (from `skip_code`, `@torch._dynamo.skip`, FX-generated code, etc.) are inherited by isolated regions — those remain skipped. RUN\_ONLY persisted by a non-isolated region hitting its recompile limit does NOT bleed into isolated regions — each region manages its own RUN\_ONLY state. Default False.
    

Example:

@torch.compile(options\={"triton.cudagraphs": True}, fullgraph\=True)
def foo(x):
    return torch.sin(x) + torch.cos(x)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.compile.rst.txt)

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