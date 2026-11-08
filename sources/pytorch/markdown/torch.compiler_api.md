Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/torch.compiler_api.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/torch.compiler_api.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/torch.compiler_api.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/torch.compiler_api.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/torch.compiler_api.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/torch.compiler_api.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/torch.compiler_api.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/torch.compiler_api.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/torch.compiler_api.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/torch.compiler_api.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/torch.compiler_api.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/torch.compiler_api.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/torch.compiler_api.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/torch.compiler_api.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/torch.compiler_api.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/torch.compiler_api.html)
[v1.13](https://docs.pytorch.org/docs/1.13/torch.compiler_api.html)
[v1.12](https://docs.pytorch.org/docs/1.12/torch.compiler_api.html)
[v1.11](https://docs.pytorch.org/docs/1.11/torch.compiler_api.html)
[v1.10](https://docs.pytorch.org/docs/1.10/torch.compiler_api.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/torch.compiler_api.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/torch.compiler_api.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/torch.compiler_api.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/torch.compiler_api.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/torch.compiler_api.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/torch.compiler_api.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/torch.compiler_api.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/torch.compiler_api.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/torch.compiler_api.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/torch.compiler_api.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/torch.compiler_api.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/torch.compiler_api.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/torch.compiler_api.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/torch.compiler_api.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/torch.compiler_api.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/torch.compiler_api.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/torch.compiler_api.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/torch.compiler_api.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/torch.compiler_api.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/torch.compiler_api.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/torch.compiler_api.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/torch.compiler_api.html)

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

torch.compiler API reference[#](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch-compiler-api-reference "Link to this heading")

================================================================================================================================================

Created On: Jun 02, 2023 | Last Updated On: Sep 23, 2026

For a quick overview of `torch.compiler`, see [torch.compiler](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/torch.compiler.html#torch-compiler-overview)
.

|     |     |
| --- | --- |
| [`compile`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.compile.html#torch.compiler.compile "torch.compiler.compile") | See [`torch.compile()`](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#torch.compile "torch.compile")<br> for details on the arguments for this function. |
| [`reset`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.reset.html#torch.compiler.reset "torch.compiler.reset") | Reset the in-process compiler state. |
| [`nonstrict_trace`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.nonstrict_trace.html#torch.compiler.nonstrict_trace "torch.compiler.nonstrict_trace") | Decorator to mark a function as nonstrict-traceable for dynamo. |
| [`allow_in_graph`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.allow_in_graph.html#torch.compiler.allow_in_graph "torch.compiler.allow_in_graph") | Tells the compiler frontend (Dynamo) to skip symbolic introspection of the function and instead directly write it to the graph when encountered. |
| [`substitute_in_graph`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.substitute_in_graph.html#torch.compiler.substitute_in_graph "torch.compiler.substitute_in_graph") | Register a polyfill handler for a function, usually a C function from the C extension, to be used in place of the original function when inlining the original function in the graph. |
| [`assume_constant_result`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.assume_constant_result.html#torch.compiler.assume_constant_result "torch.compiler.assume_constant_result") | This function is used to mark a function fn as having a constant result. |
| [`list_backends`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.list_backends.html#torch.compiler.list_backends "torch.compiler.list_backends") | Return valid strings that can be passed to torch.compile(..., backend="name"). |
| [`disable`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.disable.html#torch.compiler.disable "torch.compiler.disable") | This function provides a decorator to disable compilation on a function. |
| [`set_default_backend`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.set_default_backend.html#torch.compiler.set_default_backend "torch.compiler.set_default_backend") | Set the default backend for `torch.compile` when no `backend` argument is specified. |
| [`get_default_backend`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.get_default_backend.html#torch.compiler.get_default_backend "torch.compiler.get_default_backend") | Return the current default backend for `torch.compile`. |
| [`set_stance`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.set_stance.html#torch.compiler.set_stance "torch.compiler.set_stance") | Set the current stance of the compiler. |
| [`set_enable_guard_collectives`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.set_enable_guard_collectives.html#torch.compiler.set_enable_guard_collectives "torch.compiler.set_enable_guard_collectives") | Enables use of collectives _during_ guard evaluation to synchronize behavior across ranks. |
| [`cudagraph_mark_step_begin`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.cudagraph_mark_step_begin.html#torch.compiler.cudagraph_mark_step_begin "torch.compiler.cudagraph_mark_step_begin") | Indicates that a new iteration of inference or training is about to begin. |
| [`cudagraph_mark_warmup_incomplete`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.cudagraph_mark_warmup_incomplete.html#torch.compiler.cudagraph_mark_warmup_incomplete "torch.compiler.cudagraph_mark_warmup_incomplete") | Request another warmup for the active CUDA Graph Trees function. |
| [`is_compiling`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.is_compiling.html#torch.compiler.is_compiling "torch.compiler.is_compiling") | Indicates whether a graph is executed/traced as part of torch.compile() or torch.export(). |
| [`is_dynamo_compiling`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.is_dynamo_compiling.html#torch.compiler.is_dynamo_compiling "torch.compiler.is_dynamo_compiling") | Indicates whether a graph is traced via TorchDynamo. |
| [`is_exporting`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.is_exporting.html#torch.compiler.is_exporting "torch.compiler.is_exporting") | Indicates whether we're under exporting. |
| [`keep_portable_guards_unsafe`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.keep_portable_guards_unsafe.html#torch.compiler.keep_portable_guards_unsafe "torch.compiler.keep_portable_guards_unsafe") | A common function to only keep guards that can be used in both Python and non-Python environments. |
| [`skip_guard_on_inbuilt_nn_modules_unsafe`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.skip_guard_on_inbuilt_nn_modules_unsafe.html#torch.compiler.skip_guard_on_inbuilt_nn_modules_unsafe "torch.compiler.skip_guard_on_inbuilt_nn_modules_unsafe") | A common function to skip guards on the inbuilt nn modules like torch.nn.Linear. |
| [`skip_guard_on_all_nn_modules_unsafe`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.skip_guard_on_all_nn_modules_unsafe.html#torch.compiler.skip_guard_on_all_nn_modules_unsafe "torch.compiler.skip_guard_on_all_nn_modules_unsafe") | A common function to skip guards on all nn modules, both user defined as well inbuilt nn modules (like torch.nn.Linear). |
| [`keep_tensor_guards_unsafe`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.keep_tensor_guards_unsafe.html#torch.compiler.keep_tensor_guards_unsafe "torch.compiler.keep_tensor_guards_unsafe") | A common function to keep tensor guards on all tensors. |
| [`skip_guard_on_globals_unsafe`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.skip_guard_on_globals_unsafe.html#torch.compiler.skip_guard_on_globals_unsafe "torch.compiler.skip_guard_on_globals_unsafe") | A common function to skip guards on all globals. |
| [`skip_all_guards_unsafe`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.skip_all_guards_unsafe.html#torch.compiler.skip_all_guards_unsafe "torch.compiler.skip_all_guards_unsafe") | A function for skipping all guards on a compiled function. |
| [`nested_compile_region`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.nested_compile_region.html#torch.compiler.nested_compile_region "torch.compiler.nested_compile_region") | Tells **\`\`torch.compile\`\`** that the marked set of operations forms a nested compile region (which is often repeated in the full model) whose code can be compiled once and safely reused. |
| [`load_cache_artifacts`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.load_cache_artifacts.html#torch.compiler.load_cache_artifacts "torch.compiler.load_cache_artifacts") | Hot loads cache artifacts that were previously serialized via save\_cache\_artifacts |
| [`load_compiled_function`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.load_compiled_function.html#torch.compiler.load_compiled_function "torch.compiler.load_compiled_function") | Load an aot-compiled function from a file. |
| [`save_cache_artifacts`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.save_cache_artifacts.html#torch.compiler.save_cache_artifacts "torch.compiler.save_cache_artifacts") | Serializes all the cache artifacts that were created during the compilation |
| [`wrap_numpy`](https://docs.pytorch.org/docs/2.15/generated/torch.compiler.wrap_numpy.html#torch.compiler.wrap_numpy "torch.compiler.wrap_numpy") | Decorator that turns a function from `np.ndarray`s to `np.ndarray`s into a function from `torch.Tensor`s to `torch.Tensor`s. |

torch.compiler.precompile[#](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#module-torch.compiler.precompile "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

Warning

`torch.compiler.precompile` and everything reached through it is a prototype API. Signatures, error types and the artifact format may change between releases without a deprecation cycle.

`torch.compiler.precompile` captures a whole computation – `fn(model, x)`, with the model(s) passed as arguments – ahead of time from the caller’s own calls, and lowers it to a self-contained Python source artifact plus an acceleration cache that a fresh process reloads. No weights are baked in, so the model is passed again at runtime:

with torch.compiler.precompile.capture(
    lambda model, x: model(x), artifact\_path\="m.py", cache\_path\="m.cache"
) as cap:
    y \= cap(model, x)

f \= torch.compiler.precompile.load("m.py", "m.cache")
y \= f(model, x)

Copy to clipboard

The contract is Note \[precompile programming model\] in `torch/_precompile.py`. It is distinct from `torch._dynamo.config.caching_precompile` (a `torch.compile` caching mode).

torch.compiler.precompile.capture(_fn_, _/_, _\*_, _artifact\_path_, _cache\_path_, _tracer\=MakeFxTracer(decompositions=None)_, _backend\='inductor'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_precompile.py#L2895)
[#](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.capture "Link to this definition")

Capture `fn` across the calls YOUR loop makes, writing the artifact on exit.

Warning

This is a prototype API. Its signature, error types and artifact format may change between releases without a deprecation cycle.

Capture is caller-driven: this returns a capture object rather than running anything. Enter it as a context manager, call it exactly as you would `fn` inside the block (a [`MakeFxTracer`](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.MakeFxTracer "torch.compiler.precompile.MakeFxTracer")
 capture takes exactly one call) – each call runs for real, folds what it exercised into the capture, and returns that run’s result – and the `(python_code, cache)` artifact is written to `artifact_path` / `cache_path` when the block exits:

with torch.compiler.precompile.capture(
    fn, artifact\_path\="m.py", cache\_path\="m.cache"
) as cap:
    y \= cap(model, x)
f \= torch.compiler.precompile.load("m.py", "m.cache")

Copy to clipboard

Because the caller makes the calls, inputs flow through naturally and return values stay available, so the capture drops into an ordinary pipeline loop. To write the artifact before the block ends, call `cap.save()` inside it. A block that raises writes nothing it has not already saved, and a block that made no call raises `PrecompileError` on exit. A capture is single-use: to capture again, call `capture()` again.

`tracer` picks the capture front-end and carries its tracer-specific configuration. [`MakeFxTracer`](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.MakeFxTracer "torch.compiler.precompile.MakeFxTracer")
 is one non-strict ATen trace: the capture takes exactly ONE call, refuses a second, and specializes control flow and shapes to that call, with the contract of Note \[precompile programming model\] in `torch/_precompile.py`. Arguments are matched positionally at capture and at load. `fn` is the whole computation, e.g. `lambda model, x: model(x)`: the `nn.Module` arguments have their params/buffers lifted to graph inputs (no weights are baked in) and the rest are the runtime inputs; the reloaded callable is invoked with the same argument structure, and the runtime model must match the captured model’s parameter/buffer structure.

`backend` selects how the captured graph is realized: `"inductor"` (default) lowers through AOTAutograd + Inductor into one self-contained module, and the cache holds the bundle that primes the inductor kernel caches on load; `"eager"` keeps the captured ATen graph and runs it as-is (no kernels, so the cache carries no artifact). A `fn` that runs a backward captures it: the trace runs with grad enabled, the resulting parameter gradients are scattered onto the runtime model exactly like eager `.backward()`, and the artifact returns `fn`’s own result.

Note

`torch.compiler.precompile` is NOT `torch._dynamo.config.caching_precompile` (a `torch.compile` guard-serialization caching mode); it captures `fn` ahead of time and lowers it to a self-contained Python source artifact.

Return type:

[_Capture_](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.Capture "torch.compiler.precompile.Capture")

torch.compiler.precompile.load(_artifact\_path_, _cache\_path_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_precompile.py#L2980)
[#](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.load "Link to this definition")

Reconstruct a runnable from the two files a precompile capture wrote.

Warning

This is a prototype API. Its signature, error types and artifact format may change between releases without a deprecation cycle.

Name the two files [`capture()`](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.capture "torch.compiler.precompile.capture")
 wrote – the `python_code` artifact and its `cache`. A readable, current-format cache loads only against the `python_code` it was emitted with (it carries a sha256 of exactly those bytes); an unreadable or other-format cache is ignored with a warning.

The driver runs from `python_code` – the single source of truth for the whole calling convention. `load` reads the source’s `BACKEND`, checks the cache’s `backend` tag against it, primes the inductor kernel caches when the cache carries a bundle so a warm reload loads precompiled kernels instead of JIT-compiling, and then exec’s `python_code`. With no usable cache it degrades to JIT’ing from `python_code`. Both files are trusted, EXECUTABLE input: load only artifacts you produced or otherwise trust.

Call the result with the SAME argument structure `fn` took – the model(s) in their original positions plus the runtime inputs. The runtime model must match the captured model’s parameter/buffer structure; precompile re-derives the param/buffer list from it. The result is a [`torch.compiler.precompile.PrecompiledRunnable`](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.PrecompiledRunnable "torch.compiler.precompile.PrecompiledRunnable")
.

Raises `PrecompileError` if either file cannot be read, if `python_code` is not a `torch.compiler.precompile` artifact, or if the cache’s `backend`, `tracer` or `code_hash` does not match `python_code` – the pair came from different captures. A cache whose `format`/`version` does not match (a foreign or different-build envelope) is NOT fatal: the cache is acceleration only, so `load` degrades to JIT’ing from `python_code` rather than crashing.

Return type:

[_PrecompiledRunnable_](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.PrecompiledRunnable "torch.compiler.precompile.PrecompiledRunnable")

_exception_ torch.compiler.PrecompileError[#](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.PrecompileError "Link to this definition")

The error type raised by `torch.compiler.precompile` and its artifacts.

Raised when capture, lowering, `load`, or a runtime call violates the precompile contract – e.g. a tensor baked as a constant (invariant 1), an unsupported / effectful op, a nested example input, which capture does not support on either path (invariant 3), an UNBACKED capture attempted inside another trace (invariant 3), a non-tensor output the inductor backend cannot lower, or a runtime input whose shape or memory format differs from the example (invariants 3 and 6). See Note \[precompile programming model\] in this module for the full contract.

_class_ torch.compiler.precompile.MakeFxTracer(_decompositions\=None_)[#](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.MakeFxTracer "Link to this definition")

The `make_fx` capture front-end, passed as `tracer=` to a precompile capture.

A NON-STRICT single make\_fx trace: it records the ATen ops of ONE execution of `fn`, so a `capture` with this tracer takes exactly one call and refuses a second, and control flow and shapes are specialized to that call (the source of the programming-model contract). Part of the prototype `torch.compiler.precompile` API, so it may change without a deprecation cycle.

The contract in brief (Note \[precompile programming model\] in `torch/_precompile.py` has the full list): every tensor `fn` reads is an argument or a registered parameter/buffer of an `nn.Module` argument, and shapes are static unless a dim is marked with `mark_unbacked` (`torch._dynamo.decorators`, inductor backend only) before the call: a marked dim is captured as an unbacked symint, so one artifact serves any runtime size of it, and a graph that needs to guard on it fails at capture. Dims that must be equal at runtime must share a `shape_id`: marked independently they bake a silent equal-size assumption, and a mismatch at runtime is not caught. Each input’s dtype and device are specialized too (a runtime mismatch is rejected), the inductor backend additionally specializes on memory format, and a nested-tensor example input is refused.

`decompositions` is an optional decomposition table (a dict mapping each `OpOverload` to a decomposition function) forwarded to `make_fx` as its `decomposition_table`; it is specific to this tracer (Dynamo lowers through the backend instead).

_class_ torch.compiler.precompile.Capture[#](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.Capture "Link to this definition")

The caller-driven capture `torch.compiler.precompile.capture` returns.

Part of the prototype `torch.compiler.precompile` API, so it may change without a deprecation cycle. Enter it as a context manager to arm the capture, call it exactly as you would `fn` inside the block – each call runs for real, is folded into the capture, and returns that run’s result – and the artifact is written to the `artifact_path` / `cache_path` files when the block exits. How many calls a capture takes is the tracer’s: [`MakeFxTracer`](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.MakeFxTracer "torch.compiler.precompile.MakeFxTracer")
 takes exactly one. Call [`save()`](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.Capture.save "torch.compiler.precompile.Capture.save")
 inside the block to write what has been captured so far to those same files without ending the capture. A block that raises writes nothing it has not already saved, and a block that made no call raises `PrecompileError` on exit rather than writing an empty artifact. A capture is single-use: once its block exits it cannot be entered again, so call `capture()` again to retry. That includes a failed write at exit: the spent capture does not keep its pair, so fix the path and capture again.

save()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_precompile.py#L425)
[#](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.Capture.save "Link to this definition")

Write everything captured so far to the artifact files without ending the capture.

Raises `PrecompileError` outside the capture’s `with` block.

_class_ torch.compiler.precompile.PrecompiledRunnable[#](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.PrecompiledRunnable "Link to this definition")

What `torch.compiler.precompile.load` returns.

A callable with the captured `fn`’s calling convention that can also be entered as a context manager and unloaded. A standalone artifact installs nothing, so for it `__enter__`/`__exit__`/[`unload()`](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.PrecompiledRunnable.unload "torch.compiler.precompile.PrecompiledRunnable.unload")
 are no-ops. Part of the prototype `torch.compiler.precompile` API, so it may change without a deprecation cycle.

Variables:

**installed** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – Whether calling this handle installs onto the captured code objects; `False` for a standalone artifact.

unload()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_precompile.py#L393)
[#](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.PrecompiledRunnable.unload "Link to this definition")

Remove whatever this loaded artifact installed; a no-op when it installed nothing.

_class_ torch.compiler.precompile.PrecompileSummary(_\*_, _frames_, _resume\_functions_, _guarded\_codes_, _backend\_graphs_, _bypassed\=()_, _truncated\=()_, _uncovered\_frames\=()_, _wont\_generalize\=()_, _dropped\_guards\=()_, _kept\_guards\=()_, _risky\_dropped\_guards\=()_, _policy\_dropped\_guards\=()_, _dropped\_guard\_code\=()_, _capture\_errors\=()_)[#](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.PrecompileSummary "Link to this definition")

Coverage and guard information from an observed precompile capture.

`str(summary)` renders a one-line digest: the counts, the dropped guards tallied by type, the risky slots and frame lists cut to their first five entries (`+N more`), and the first non-empty line of the first capture error. Everything here describes the calls that ran, not every possible input or unexecuted branch, and once `truncated` is non-empty every count and frame list is a lower bound: from a limit hit on, that frame and everything it called ran untraced, so a frame first reached there is in no list here.

The guard fields hold `(guard_type, source)` slots, the source spelled with the local scope stripped (`L['self'].act` -> `self.act`; `G['CFG'].width` unchanged). Each list holds a slot once, however many frames or variants carried it, so `dropped_guard_types` counts distinct slots, not occurrences. The relations between the lists hold within one frame variant, where the producer applies them, and are stated here rather than checked:

*   `kept_guards` and `dropped_guards` are disjoint: the filter gives a slot one verdict, keep or reject.
    
*   `risky_dropped_guards` is drawn from `dropped_guards`.
    
*   `policy_dropped_guards` is disjoint from both: a policy drop is taken out of the serialized copy the filter kept, once the slot held identically across every captured variant, and is not checked either.
    
*   `dropped_guard_code` draws its slots from `dropped_guards` and `policy_dropped_guards`.
    
*   every `wont_generalize` source is the source half of a `kept_guards` slot, the value-equality guard that pins it.
    

The lists aggregate every captured frame and a slot names no frame, so two frames’ `self.act` are one slot: a slot one frame kept and another dropped is in both `kept_guards` and `dropped_guards` (the digest’s `(N kept)` is the kept count beside the drops, not the other half of a total), and a slot one frame’s filter rejected and another frame’s invariance policy dropped is in both drop lists. Nothing is enforced, as for the frame lists below: a report that raised on its own bookkeeping would lose the coverage it exists to describe.

The frame lists differ in what an entry is. `bypassed` and `uncovered_frames` hold one bare `co_name` per frame, read off the package’s entries, so a name can repeat (every `nn.Module` has a `forward`: `['forward', 'forward']` is two frames, not a repeat) and their lengths count frames. `truncated` holds `co_name (filename:firstlineno)`, recorded once per code object that hit the limit, so its entries do identify a frame. A bare name identifies none, so the two bare lists cannot be checked disjoint.

Variables:

*   **frames** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Captured frames: every frame the package holds an entry for, the `bypassed`, `truncated` and `uncovered_frames` ones included, so the digest’s frame clauses cut into this count rather than add to it.
    
*   **resume\_functions** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Of those, the graph-break continuations.
    
*   **guarded\_codes** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Guarded code objects across all frames.
    
*   **backend\_graphs** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Compiled backend graphs.
    
*   **bypassed** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _...__\]_) – The `co_name` of each frame the package holds nothing servable for: no compile of the frame recorded a guarded code and one was bypassed (its guards could not be serialized, or its graph held parameters by static address), or a backend artifact was missing when the package was saved. Not an eager fallback: the frame ran compiled during capture, but the package kept no variant of it a load can serve, so a call that reaches it raises.
    
*   **truncated** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _...__\]_) – `co_name (filename:firstlineno)` of each frame that hit the recompile limit. A lower bound, which is why the digest prints it as `>=`: from a limit hit on, that frame and the frames it calls run without tracing, so a limit hit that would follow it there is never recorded.
    
*   **uncovered\_frames** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _...__\]_) – The `co_name` of each frame the capture ran that ended with no guarded code and was not bypassed, so the artifact cannot serve it: a thin wrapper whose graphs all landed in an inner frame, a frame Dynamo gave up on, or a frame whose compile raised (its message is in `capture_errors`, so one failure shows in both digest clauses). A different cause from `bypassed`, never the same frame; a frame that hit the recompile limit before it recorded a guarded code is in `truncated` too. Not a remainder: which frames count as a gap is the producer’s decision, and a frame the package holds an entry for but never ran is not one, so this is not `frames` minus `bypassed` minus the frames that hold guarded code.
    
*   **wont\_generalize** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _...__\]_) – Guard _sources_ (not frame names) a kept value-equality guard on a bare argument name pins in some variant (`self.eps` is not a bare name) while no other variant of the same frame guards the source without pinning it, so as captured no variant served another value. Observed, not proven: a variant that never guarded the source does not count as serving other values of it.
    
*   **dropped\_guards** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]__,_ _...__\]_) – Slots the serialized copy’s guard filter rejected; a variant that dropped a slot does not check it, so a load through that variant cannot notice whatever it checked. The default filter drops a guard when the serializer refuses its type or a type its check derives: the identity guards (`ID_MATCH`, `FUNCTION_MATCH`, `NN_MODULE` and the like), `WEAKREF_ALIVE` and most `DICT_VERSION` guards, so a load cannot notice that the objects they checked were rebound, mutated or collected. Passing it does not make a guard serializable; a caller-supplied filter decides its own set. A slot is listed under the guard’s own type whatever the reason for the drop, so a `TENSOR_MATCH` rejected for what its check derives is a dropped `TENSOR_MATCH`.
    
*   **kept\_guards** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]__,_ _...__\]_) – Slots the serialized copy’s guard filter kept and the invariance policy left in place.
    
*   **risky\_dropped\_guards** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]__,_ _...__\]_) – The subset of `dropped_guards` observed to tell captured variants apart, or flagged by the risky-drop lint as a configuration-chosen binding.
    
*   **policy\_dropped\_guards** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]__,_ _...__\]_) – Slots the filter kept that the invariance policy then dropped because they held identically across every captured variant (only guard types from a fixed set are eligible). Reported apart from `dropped_guards` because the remedy differs, and reported at all because a capture that discards a precondition should not look like one that had none.
    
*   **dropped\_guard\_code** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]__,_ _...__\]_) – `(guard_type, source, rendered_check)`, one per slot of `dropped_guards` or `policy_dropped_guards` whose guard rendered a check (how a guard is installed does not predict whether it renders one, and a slot whose guard rendered none has no entry). One rendering however many variants dropped the slot: where the check embeds the guarded value (`EQUALS_MATCH` renders `L['n'] == 3`) it is one variant’s, the producer’s pick rather than a merge, so it tells the form of the check and not the value; that the slot varied at all is what `risky_dropped_guards` records. Carried because a slot alone can be ambiguous: a dropped `('HASATTR', "counts['pixel']")` is either the benign companion of a kept `TENSOR_MATCH` on the same source or the only guard on an optional attribute, and only the rendered check tells them apart. Kept beside the slot lists so the slots stay the identity the policy compares on; for programmatic consumers, not the digest.
    
*   **capture\_errors** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _...__\]_) – One message per distinct exception a capture call raised (repeats of the same type and message collapse), the exception type first (`"RuntimeError: boom"`), so the digest’s first line is never empty however the exception was raised.
    

_property_ complete_: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.PrecompileSummary.complete "Link to this definition")

Whether the capture covers everything it exercised.

Coverage only: False if a frame was `bypassed`, hit the recompile limit (`truncated`) or ended with no guarded code (`uncovered_frames`), if a capture call raised (`capture_errors`), or if nothing was compiled. Both `guarded_codes` and `backend_graphs` must be non-zero for the last check, because a frame that compiled nothing can still count as one guarded code, so `guarded_codes` alone cannot tell a real capture from an empty one. The guard fields never enter: `risky_dropped_guards` is a lint finding, not a proof, and `wont_generalize` follows from any value the capture pinned, so both describe how far a complete capture generalizes and the digest reports them on their own.

_property_ dropped\_guard\_types_: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\]_[#](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.PrecompileSummary.dropped_guard_types "Link to this definition")

The distinct dropped slots counted by guard type.

_property_ kept\_guard\_types_: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\]_[#](https://docs.pytorch.org/docs/2.15/torch.compiler_api.html#torch.compiler.precompile.PrecompileSummary.kept_guard_types "Link to this definition")

The distinct kept slots counted by guard type.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/torch.compiler_api.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/torch.compiler_api.md.txt)

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