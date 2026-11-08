Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/higher_order_ops/index.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/higher_order_ops/index.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/higher_order_ops/index.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/higher_order_ops/index.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/higher_order_ops/index.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/higher_order_ops/index.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/higher_order_ops/index.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/higher_order_ops/index.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/higher_order_ops/index.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/higher_order_ops/index.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/higher_order_ops/index.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/higher_order_ops/index.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/higher_order_ops/index.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/higher_order_ops/index.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/higher_order_ops/index.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/higher_order_ops/index.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/higher_order_ops/index.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/higher_order_ops/index.html)
[v1.13](https://docs.pytorch.org/docs/1.13/higher_order_ops/index.html)
[v1.12](https://docs.pytorch.org/docs/1.12/higher_order_ops/index.html)
[v1.11](https://docs.pytorch.org/docs/1.11/higher_order_ops/index.html)
[v1.10](https://docs.pytorch.org/docs/1.10/higher_order_ops/index.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/higher_order_ops/index.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/higher_order_ops/index.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/higher_order_ops/index.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/higher_order_ops/index.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/higher_order_ops/index.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/higher_order_ops/index.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/higher_order_ops/index.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/higher_order_ops/index.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/higher_order_ops/index.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/higher_order_ops/index.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/higher_order_ops/index.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/higher_order_ops/index.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/higher_order_ops/index.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/higher_order_ops/index.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/higher_order_ops/index.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/higher_order_ops/index.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/higher_order_ops/index.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/higher_order_ops/index.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/higher_order_ops/index.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/higher_order_ops/index.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/higher_order_ops/index.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/higher_order_ops/index.html)

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

Control Flow Operators[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/index.html#control-flow-operators "Link to this heading")

========================================================================================================================================

Created On: Feb 14, 2026 | Last Updated On: Jun 24, 2026

Control flow operators are structured operators in PyTorch that enable expressing complex control flow patterns in a way that is compatible with `torch.compile` and `torch.export`. Unlike regular Python control flow, these operators preserve their semantics through torch.compile and torch.export, enabling data-dependent control flow in traced programs.

Warning

Control flow operators are prototype features in PyTorch. They may have limited support for certain input/output types and some may not fully support training. Read more about feature classification at: https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype

Why Use Control Flow Operators?[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/index.html#why-use-control-flow-operators "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

PyTorch lets you write models using native Python, including control flow like `if` statements, `for` loops, and `while` loops. This is great for flexibility, but it creates challenges for compilation.

Consider this simple example:

if mod.static\_config \== 0:
    return f(x)
return g(x)

Copy to clipboard

The two branches might have completely different operations. If we tried to compile both branches every time we hit an `if` statement, the number of code paths would explode exponentially and quickly become intractable.

To deal with this, `torch.compile` uses **specialization and guards**. When tracing your model, the compiler picks one code path based on the current value of the predicate (specialization), then adds a guard to check that assumption at runtime. If the guard fails, it recompiles.

The same applies to loops: the compiler unrolls them and guards on the number of iterations. This produces a straight-line computational graph that’s easy to optimize.

This approach works well for static control flow, but breaks down in several cases:

*   **Data-dependent control flow**: When the predicate depends on the _value_ of a tensor, the compiler can’t pick a branch at compile time because the value isn’t known yet. Similarly, it can’t unroll a `while` loop if the iteration count depends on tensor values. The compiler handles this by graph breaking and falling back to Python, which also makes it impossible to run the model without a Python runtime (e.g., on edge devices).
    
*   **Dynamic shape-dependent control flow**: When the number of loop iterations or the branch predicate depends on a dynamic tensor size, specialization means the compiled code only works for that specific size. The compiler has to recompile whenever the size changes.
    
*   **Large computational graphs**: Even with a static iteration count, unrolling a large loop creates a graph that grows linearly with the number of iterations, even though each iteration does the same thing. This leads to long compile times and high memory usage.
    

Control flow operators solve these problems by representing control flow as explicit operators that the compiler understands. Instead of specializing away the control flow, these operators preserve it in the compiled graph.

Available Operators[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/index.html#available-operators "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

*   [Control Flow - Cond](https://docs.pytorch.org/docs/2.15/higher_order_ops/cond.html)
    
*   [Control Flow - Switch](https://docs.pytorch.org/docs/2.15/higher_order_ops/switch.html)
    
*   [Control Flow - While Loop](https://docs.pytorch.org/docs/2.15/higher_order_ops/while_loop.html)
    
*   [Control Flow - Scan](https://docs.pytorch.org/docs/2.15/higher_order_ops/scan.html)
    
*   [Control Flow - Associative Scan](https://docs.pytorch.org/docs/2.15/higher_order_ops/associative_scan.html)
    
*   [Control Flow - Map](https://docs.pytorch.org/docs/2.15/higher_order_ops/map.html)
    

### Quick Comparison[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/index.html#quick-comparison "Link to this heading")

| Operator | Use Case | Example |
| --- | --- | --- |
| [cond](https://docs.pytorch.org/docs/2.15/higher_order_ops/cond.html) | If `pred` is True, returns `true_fn(*operands)`, otherwise returns `false_fn(*operands)`. | `cond(pred, true_fn, false_fn, operands)` |
| [switch](https://docs.pytorch.org/docs/2.15/higher_order_ops/switch.html) | N-way branching: returns `branches[index](*operands)` with `index` clamped into `[0, len(branches)-1]`. | `switch(index, branches, operands)` |
| [while\_loop](https://docs.pytorch.org/docs/2.15/higher_order_ops/while_loop.html) | While `cond_fn(*operands)` is True, executes `body_fn(*operands)`, which returns the operands for the next iteration. | `while_loop(cond_fn, body_fn, operands)` |
| [scan](https://docs.pytorch.org/docs/2.15/higher_order_ops/scan.html) | Applies cumulative operations to `xs` with carried state | `scan(combine_fn, init, xs)` |
| [associative\_scan](https://docs.pytorch.org/docs/2.15/higher_order_ops/associative_scan.html) | Similar to `scan`, but requiring an associative `combine_fn` to allow for more optimizations. | `associative_scan(add, xs, dim=0)` |
| [map](https://docs.pytorch.org/docs/2.15/higher_order_ops/map.html) | Computes `fn` on each slice of `xs` and returns the stacked output. | `map(fn, xs)` |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/higher_order_ops/index.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/higher_order_ops/index.md.txt)

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