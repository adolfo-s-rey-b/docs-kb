Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/exportdb/index.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/exportdb/index.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/exportdb/index.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/exportdb/index.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/exportdb/index.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/exportdb/index.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/exportdb/index.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/exportdb/index.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/exportdb/index.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/exportdb/index.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/exportdb/index.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/exportdb/index.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/exportdb/index.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/exportdb/index.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/exportdb/index.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/exportdb/index.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/exportdb/index.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/exportdb/index.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/exportdb/index.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/exportdb/index.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/exportdb/index.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/exportdb/index.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/exportdb/index.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/exportdb/index.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/exportdb/index.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/exportdb/index.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/exportdb/index.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/exportdb/index.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/exportdb/index.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/exportdb/index.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/exportdb/index.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/exportdb/index.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/exportdb/index.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/exportdb/index.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/exportdb/index.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/exportdb/index.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/exportdb/index.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/exportdb/index.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/exportdb/index.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/exportdb/index.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/exportdb/index.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/exportdb/index.html)

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

ExportDB[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#exportdb "Link to this heading")

==============================================================================================================

ExportDB is a centralized dataset of supported and unsupported export cases. It is targeted towards users who want to understand specifically what types of code are supported, the subtleties of export, and how to modify their existing code to be compatible with export. Note that this is not an exhaustive set of everything that is supported by exportdb, but it covers the most common and confusing use cases that users will run into.

If you have a feature that you think needs a stronger guarantee from us to support in export please create an issue in the pytorch/pytorch repo with a module:export tag.

Tags

*   [torch.escape-hatch](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.escape-hatch.html)
    
*   [torch.cond](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.cond.html)
    
*   [torch.dynamic-shape](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-shape.html)
    
*   [python.closure](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.closure.html)
    
*   [torch.dynamic-value](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-value.html)
    
*   [python.data-structure](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.data-structure.html)
    
*   [python.assert](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.assert.html)
    
*   [python.control-flow](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.control-flow.html)
    
*   [torch.map](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.map.html)
    
*   [python.builtin](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.builtin.html)
    
*   [python.object-model](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.object-model.html)
    
*   [python.context-manager](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.context-manager.html)
    
*   [torch.operator](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.operator.html)
    
*   [torch.mutation](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.mutation.html)
    

Supported[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#supported "Link to this heading")

----------------------------------------------------------------------------------------------------------------

### assume\_constant\_result[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#assume-constant-result "Link to this heading")

Note

Tags: [torch.escape-hatch](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.escape-hatch.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch
import torch.\_dynamo as torchdynamo

class AssumeConstantResult(torch.nn.Module):
    """
    Applying \`assume\_constant\_result\` decorator to burn make non-traceable code as constant.
    """

    @torchdynamo.assume\_constant\_result
    def get\_item(self, y):
        return y.int().item()

    def forward(self, x, y):
        return x\[: self.get\_item(y)\]

example\_args \= (torch.randn(3, 2), torch.tensor(4))
tags \= {"torch.escape-hatch"}
model \= AssumeConstantResult()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]", y: "i64\[\]"):
                slice\_1: "f32\[3, 2\]" \= torch.ops.aten.slice.Tensor(x, 0, 0, 4);  x \= None
            return (slice\_1,)

Graph signature:
    \# inputs
    x: USER\_INPUT
    y: USER\_INPUT

    \# outputs
    slice\_1: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### autograd\_function[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#autograd-function "Link to this heading")

Note

Tags:

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class MyAutogradFunction(torch.autograd.Function):
    @staticmethod
    \# pyrefly: ignore \[bad-override\]
    def forward(ctx, x):
        return x.clone()

    @staticmethod
    \# pyrefly: ignore \[bad-override\]
    def backward(ctx, grad\_output):
        return grad\_output + 1

class AutogradFunction(torch.nn.Module):
    """
    TorchDynamo does not keep track of backward() on autograd functions. We recommend to
    use \`allow\_in\_graph\` to mitigate this problem.
    """

    def forward(self, x):
        return MyAutogradFunction.apply(x)

example\_args \= (torch.randn(3, 2),)
model \= AutogradFunction()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]"):
                clone: "f32\[3, 2\]" \= torch.ops.aten.clone.default(x);  x \= None
            return (clone,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    clone: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### class\_method[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#class-method "Link to this heading")

Note

Tags:

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class ClassMethod(torch.nn.Module):
    """
    Class methods are inlined during tracing.
    """

    @classmethod
    def method(cls, x):
        return x + 1

    def \_\_init\_\_(self) \-> None:
        super().\_\_init\_\_()
        self.linear \= torch.nn.Linear(4, 2)

    def forward(self, x):
        x \= self.linear(x)
        return self.method(x) \* self.\_\_class\_\_.method(x) \* type(self).method(x)

example\_args \= (torch.randn(3, 4),)
model \= ClassMethod()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, p\_linear\_weight: "f32\[2, 4\]", p\_linear\_bias: "f32\[2\]", x: "f32\[3, 4\]"):
                linear: "f32\[3, 2\]" \= torch.ops.aten.linear.default(x, p\_linear\_weight, p\_linear\_bias);  x \= p\_linear\_weight \= p\_linear\_bias \= None

                add: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(linear, 1)
            add\_1: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(linear, 1)

                mul: "f32\[3, 2\]" \= torch.ops.aten.mul.Tensor(add, add\_1);  add \= add\_1 \= None

                add\_2: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(linear, 1);  linear \= None

                mul\_1: "f32\[3, 2\]" \= torch.ops.aten.mul.Tensor(mul, add\_2);  mul \= add\_2 \= None
            return (mul\_1,)

Graph signature:
    \# inputs
    p\_linear\_weight: PARAMETER target\='linear.weight'
    p\_linear\_bias: PARAMETER target\='linear.bias'
    x: USER\_INPUT

    \# outputs
    mul\_1: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### cond\_branch\_class\_method[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#cond-branch-class-method "Link to this heading")

Note

Tags: [torch.cond](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.cond.html)
, [torch.dynamic-shape](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-shape.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

from functorch.experimental.control\_flow import cond

class MySubModule(torch.nn.Module):
    def foo(self, x):
        return x.cos()

    def forward(self, x):
        return self.foo(x)

class CondBranchClassMethod(torch.nn.Module):
    """
    The branch functions (\`true\_fn\` and \`false\_fn\`) passed to cond() must follow these rules:
      - both branches must take the same args, which must also match the branch args passed to cond.
      - both branches must return a single tensor
      - returned tensor must have the same tensor metadata, e.g. shape and dtype
      - branch function can be free function, nested function, lambda, class methods
      - branch function can not have closure variables
      - no inplace mutations on inputs or global variables

    This example demonstrates using class method in cond().

    NOTE: If the \`pred\` is tested on a dim with batch size < 2, it will be specialized.
    """

    def \_\_init\_\_(self) \-> None:
        super().\_\_init\_\_()
        self.subm \= MySubModule()

    def bar(self, x):
        return x.sin()

    def forward(self, x):
        return cond(x.shape\[0\] <= 2, self.subm.forward, self.bar, \[x\])

example\_args \= (torch.randn(3),)
tags \= {
    "torch.cond",
    "torch.dynamic-shape",
}
model \= CondBranchClassMethod()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3\]"):
                sin: "f32\[3\]" \= torch.ops.aten.sin.default(x);  x \= None
            return (sin,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    sin: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### cond\_branch\_nested\_function[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#cond-branch-nested-function "Link to this heading")

Note

Tags: [torch.cond](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.cond.html)
, [torch.dynamic-shape](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-shape.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

from functorch.experimental.control\_flow import cond

class CondBranchNestedFunction(torch.nn.Module):
    """
    The branch functions (\`true\_fn\` and \`false\_fn\`) passed to cond() must follow these rules:
      - both branches must take the same args, which must also match the branch args passed to cond.
      - both branches must return a single tensor
      - returned tensor must have the same tensor metadata, e.g. shape and dtype
      - branch function can be free function, nested function, lambda, class methods
      - branch function can not have closure variables
      - no inplace mutations on inputs or global variables

    This example demonstrates using nested function in cond().

    NOTE: If the \`pred\` is tested on a dim with batch size < 2, it will be specialized.
    """

    def forward(self, x):
        def true\_fn(x):
            def inner\_true\_fn(y):
                return x + y

            return inner\_true\_fn(x)

        def false\_fn(x):
            def inner\_false\_fn(y):
                return x \- y

            return inner\_false\_fn(x)

        return cond(x.shape\[0\] < 10, true\_fn, false\_fn, \[x\])

example\_args \= (torch.randn(3),)
tags \= {
    "torch.cond",
    "torch.dynamic-shape",
}
model \= CondBranchNestedFunction()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3\]"):
                add: "f32\[3\]" \= torch.ops.aten.add.Tensor(x, x);  x \= None
            return (add,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    add: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### cond\_branch\_nonlocal\_variables[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#cond-branch-nonlocal-variables "Link to this heading")

Note

Tags: [torch.cond](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.cond.html)
, [torch.dynamic-shape](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-shape.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

from functorch.experimental.control\_flow import cond

class CondBranchNonlocalVariables(torch.nn.Module):
    """
    The branch functions (\`true\_fn\` and \`false\_fn\`) passed to cond() must follow these rules:
    - both branches must take the same args, which must also match the branch args passed to cond.
    - both branches must return a single tensor
    - returned tensor must have the same tensor metadata, e.g. shape and dtype
    - branch function can be free function, nested function, lambda, class methods
    - branch function can not have closure variables
    - no inplace mutations on inputs or global variables

    This example demonstrates how to rewrite code to avoid capturing closure variables in branch functions.

    The code below will not work because capturing closure variables is not supported.
    \`\`\`
    my\_tensor\_var = x + 100
    my\_primitive\_var = 3.14

    def true\_fn(y):
        nonlocal my\_tensor\_var, my\_primitive\_var
        return y + my\_tensor\_var + my\_primitive\_var

    def false\_fn(y):
        nonlocal my\_tensor\_var, my\_primitive\_var
        return y - my\_tensor\_var - my\_primitive\_var

    return cond(x.shape\[0\] > 5, true\_fn, false\_fn, \[x\])
    \`\`\`

    NOTE: If the \`pred\` is tested on a dim with batch size < 2, it will be specialized.
    """

    def forward(self, x):
        my\_tensor\_var \= x + 100
        my\_primitive\_var \= 3.14

        def true\_fn(x, y, z):
            return x + y + z

        def false\_fn(x, y, z):
            return x \- y \- z

        return cond(
            x.shape\[0\] \> 5,
            true\_fn,
            false\_fn,
            \[x, my\_tensor\_var, torch.tensor(my\_primitive\_var)\],
        )

example\_args \= (torch.randn(6),)
tags \= {
    "torch.cond",
    "torch.dynamic-shape",
}
model \= CondBranchNonlocalVariables()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, c\_lifted\_tensor\_0: "f32\[\]", x: "f32\[6\]"):
                add: "f32\[6\]" \= torch.ops.aten.add.Tensor(x, 100)

                lift\_fresh\_copy: "f32\[\]" \= torch.ops.aten.lift\_fresh\_copy.default(c\_lifted\_tensor\_0);  c\_lifted\_tensor\_0 \= None
            detach\_: "f32\[\]" \= torch.ops.aten.detach\_.default(lift\_fresh\_copy);  lift\_fresh\_copy \= None

                add\_1: "f32\[6\]" \= torch.ops.aten.add.Tensor(x, add);  x \= add \= None
            add\_2: "f32\[6\]" \= torch.ops.aten.add.Tensor(add\_1, detach\_);  add\_1 \= detach\_ \= None
            return (add\_2,)

Graph signature:
    \# inputs
    c\_lifted\_tensor\_0: CONSTANT\_TENSOR target\='lifted\_tensor\_0'
    x: USER\_INPUT

    \# outputs
    add\_2: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### cond\_closed\_over\_variable[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#cond-closed-over-variable "Link to this heading")

Note

Tags: [python.closure](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.closure.html)
, [torch.cond](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.cond.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

from functorch.experimental.control\_flow import cond

class CondClosedOverVariable(torch.nn.Module):
    """
    torch.cond() supports branches closed over arbitrary variables.
    """

    def forward(self, pred, x):
        def true\_fn(val):
            return x \* 2

        def false\_fn(val):
            return x \- 2

        return cond(pred, true\_fn, false\_fn, \[x + 1\])

example\_args \= (torch.tensor(True), torch.randn(3, 2))
tags \= {"torch.cond", "python.closure"}
model \= CondClosedOverVariable()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, pred: "b8\[\]", x: "f32\[3, 2\]"):
                add: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(x, 1);  add \= None
            true\_graph\_0 \= self.true\_graph\_0
            false\_graph\_0 \= self.false\_graph\_0
            cond \= torch.ops.higher\_order.cond(pred, true\_graph\_0, false\_graph\_0, (x,));  pred \= true\_graph\_0 \= false\_graph\_0 \= x \= None
            getitem: "f32\[3, 2\]" \= cond\[0\];  cond \= None
            return (getitem,)

        class true\_graph\_0(torch.nn.Module):
            def forward(self, x: "f32\[3, 2\]"):
                        mul: "f32\[3, 2\]" \= torch.ops.aten.mul.Tensor(x, 2);  x \= None
                return (mul,)

        class false\_graph\_0(torch.nn.Module):
            def forward(self, x: "f32\[3, 2\]"):
                        sub: "f32\[3, 2\]" \= torch.ops.aten.sub.Tensor(x, 2);  x \= None
                return (sub,)

Graph signature:
    \# inputs
    pred: USER\_INPUT
    x: USER\_INPUT

    \# outputs
    getitem: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### cond\_operands[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#cond-operands "Link to this heading")

Note

Tags: [torch.cond](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.cond.html)
, [torch.dynamic-shape](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-shape.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

from torch.export import Dim

x \= torch.randn(3, 2)
y \= torch.randn(2)
dim0\_x \= Dim("dim0\_x")

class CondOperands(torch.nn.Module):
    """
    The operands passed to cond() must be:
    - a list of tensors
    - match arguments of \`true\_fn\` and \`false\_fn\`

    NOTE: If the \`pred\` is tested on a dim with batch size < 2, it will be specialized.
    """

    def forward(self, x, y):
        def true\_fn(x, y):
            return x + y

        def false\_fn(x, y):
            return x \- y

        return torch.cond(x.shape\[0\] \> 2, true\_fn, false\_fn, \[x, y\])

example\_args \= (x, y)
tags \= {
    "torch.cond",
    "torch.dynamic-shape",
}
extra\_inputs \= (torch.randn(2, 2), torch.randn(2))
dynamic\_shapes \= {"x": {0: dim0\_x}, "y": None}
model \= CondOperands()

torch.export.export(model, example\_args, dynamic\_shapes\=dynamic\_shapes)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[s6, 2\]", y: "f32\[2\]"):
            \# No stacktrace found for following nodes
            sym\_size\_int\_1: "Sym(s6)" \= torch.ops.aten.sym\_size.int(x, 0)

                gt: "Sym(s6 > 2)" \= sym\_size\_int\_1 \> 2;  sym\_size\_int\_1 \= None
            true\_graph\_0 \= self.true\_graph\_0
            false\_graph\_0 \= self.false\_graph\_0
            cond \= torch.ops.higher\_order.cond(gt, true\_graph\_0, false\_graph\_0, (x, y));  gt \= true\_graph\_0 \= false\_graph\_0 \= x \= y \= None
            getitem: "f32\[s6, 2\]" \= cond\[0\];  cond \= None
            return (getitem,)

        class true\_graph\_0(torch.nn.Module):
            def forward(self, x: "f32\[s6, 2\]", y: "f32\[2\]"):
                        add: "f32\[s6, 2\]" \= torch.ops.aten.add.Tensor(x, y);  x \= y \= None
                return (add,)

        class false\_graph\_0(torch.nn.Module):
            def forward(self, x: "f32\[s6, 2\]", y: "f32\[2\]"):
                        sub: "f32\[s6, 2\]" \= torch.ops.aten.sub.Tensor(x, y);  x \= y \= None
                return (sub,)

Graph signature:
    \# inputs
    x: USER\_INPUT
    y: USER\_INPUT

    \# outputs
    getitem: USER\_OUTPUT

Range constraints: {s6: VR\[0, int\_oo\]}

Copy to clipboard

### cond\_predicate[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#cond-predicate "Link to this heading")

Note

Tags: [torch.cond](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.cond.html)
, [torch.dynamic-shape](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-shape.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

from functorch.experimental.control\_flow import cond

class CondPredicate(torch.nn.Module):
    """
    The conditional statement (aka predicate) passed to cond() must be one of the following:
      - torch.Tensor with a single element
      - boolean expression

    NOTE: If the \`pred\` is tested on a dim with batch size < 2, it will be specialized.
    """

    def forward(self, x):
        pred \= x.dim() \> 2 and x.shape\[2\] \> 10

        return cond(pred, lambda x: x.cos(), lambda y: y.sin(), \[x\])

example\_args \= (torch.randn(6, 4, 3),)
tags \= {
    "torch.cond",
    "torch.dynamic-shape",
}
model \= CondPredicate()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[6, 4, 3\]"):
                sin: "f32\[6, 4, 3\]" \= torch.ops.aten.sin.default(x);  x \= None
            return (sin,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    sin: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### constrain\_as\_size\_example[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#constrain-as-size-example "Link to this heading")

Note

Tags: [torch.dynamic-value](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-value.html)
, [torch.escape-hatch](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.escape-hatch.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class ConstrainAsSizeExample(torch.nn.Module):
    """
    If the value is not known at tracing time, you can provide hint so that we
    can trace further. Please look at torch.\_check APIs.
    """

    def forward(self, x):
        a \= x.item()
        torch.\_check(a \>= 0)
        torch.\_check(a <= 5)
        return torch.zeros((a, 5))

example\_args \= (torch.tensor(4),)
tags \= {
    "torch.dynamic-value",
    "torch.escape-hatch",
}
model \= ConstrainAsSizeExample()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "i64\[\]"):
                item: "Sym(u0)" \= torch.ops.aten.item.default(x);  x \= None
            ge\_1: "Sym(u0 >= 0)" \= item \>= 0
            \_assert\_scalar\_default \= torch.ops.aten.\_assert\_scalar.default(ge\_1, "Runtime assertion failed for expression u0 >= 0 on node 'ge\_1'");  ge\_1 \= \_assert\_scalar\_default \= None
            le\_1: "Sym(u0 <= 5)" \= item <= 5
            \_assert\_scalar\_default\_1 \= torch.ops.aten.\_assert\_scalar.default(le\_1, "Runtime assertion failed for expression u0 <= 5 on node 'le\_1'");  le\_1 \= \_assert\_scalar\_default\_1 \= None

                zeros: "f32\[u0, 5\]" \= torch.ops.aten.zeros.default(\[item, 5\], device \= device(type\='cpu'), pin\_memory \= False);  item \= None
            return (zeros,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    zeros: USER\_OUTPUT

Range constraints: {u0: VR\[0, 5\], u1: VR\[0, 5\]}

Copy to clipboard

### constrain\_as\_value\_example[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#constrain-as-value-example "Link to this heading")

Note

Tags: [torch.dynamic-value](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-value.html)
, [torch.escape-hatch](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.escape-hatch.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class ConstrainAsValueExample(torch.nn.Module):
    """
    If the value is not known at tracing time, you can provide hint so that we
    can trace further. Please look at torch.\_check API.
    """

    def forward(self, x, y):
        a \= x.item()
        torch.\_check(a \>= 0)
        torch.\_check(a <= 5)

        if a < 6:
            return y.sin()
        return y.cos()

example\_args \= (torch.tensor(4), torch.randn(5, 5))
tags \= {
    "torch.dynamic-value",
    "torch.escape-hatch",
}
model \= ConstrainAsValueExample()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "i64\[\]", y: "f32\[5, 5\]"):
                item: "Sym(u0)" \= torch.ops.aten.item.default(x);  x \= None
            ge\_1: "Sym(u0 >= 0)" \= item \>= 0
            \_assert\_scalar\_default \= torch.ops.aten.\_assert\_scalar.default(ge\_1, "Runtime assertion failed for expression u0 >= 0 on node 'ge\_1'");  ge\_1 \= \_assert\_scalar\_default \= None
            le\_1: "Sym(u0 <= 5)" \= item <= 5;  item \= None
            \_assert\_scalar\_default\_1 \= torch.ops.aten.\_assert\_scalar.default(le\_1, "Runtime assertion failed for expression u0 <= 5 on node 'le\_1'");  le\_1 \= \_assert\_scalar\_default\_1 \= None

                sin: "f32\[5, 5\]" \= torch.ops.aten.sin.default(y);  y \= None
            return (sin,)

Graph signature:
    \# inputs
    x: USER\_INPUT
    y: USER\_INPUT

    \# outputs
    sin: USER\_OUTPUT

Range constraints: {u0: VR\[0, 5\], u1: VR\[0, 5\]}

Copy to clipboard

### decorator[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#decorator "Link to this heading")

Note

Tags:

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import functools

import torch

def test\_decorator(func):
    @functools.wraps(func)
    def wrapper(\*args, \*\*kwargs):
        return func(\*args, \*\*kwargs) + 1

    return wrapper

class Decorator(torch.nn.Module):
    """
    Decorators calls are inlined into the exported function during tracing.
    """

    @test\_decorator
    def forward(self, x, y):
        return x + y

example\_args \= (torch.randn(3, 2), torch.randn(3, 2))
model \= Decorator()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]", y: "f32\[3, 2\]"):
                add: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(x, y);  x \= y \= None

                add\_1: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(add, 1);  add \= None
            return (add\_1,)

Graph signature:
    \# inputs
    x: USER\_INPUT
    y: USER\_INPUT

    \# outputs
    add\_1: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### dictionary[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#dictionary "Link to this heading")

Note

Tags: [python.data-structure](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.data-structure.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class Dictionary(torch.nn.Module):
    """
    Dictionary structures are inlined and flattened along tracing.
    """

    def forward(self, x, y):
        elements \= {}
        elements\["x2"\] \= x \* x
        y \= y \* elements\["x2"\]
        return {"y": y}

example\_args \= (torch.randn(3, 2), torch.tensor(4))
tags \= {"python.data-structure"}
model \= Dictionary()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]", y: "i64\[\]"):
                mul: "f32\[3, 2\]" \= torch.ops.aten.mul.Tensor(x, x);  x \= None

                mul\_1: "f32\[3, 2\]" \= torch.ops.aten.mul.Tensor(y, mul);  y \= mul \= None
            return (mul\_1,)

Graph signature:
    \# inputs
    x: USER\_INPUT
    y: USER\_INPUT

    \# outputs
    mul\_1: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### dynamic\_shape\_assert[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#dynamic-shape-assert "Link to this heading")

Note

Tags: [python.assert](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.assert.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class DynamicShapeAssert(torch.nn.Module):
    """
    A basic usage of python assertion.
    """

    def forward(self, x):
        \# assertion with error message
        assert x.shape\[0\] \> 2, f"{x.shape\[0\]} is greater than 2"  \# noqa: S101
        \# assertion without error message
        assert x.shape\[0\] \> 1  \# noqa: S101
        return x

example\_args \= (torch.randn(3, 2),)
tags \= {"python.assert"}
model \= DynamicShapeAssert()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]"):
            return (x,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    x: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### dynamic\_shape\_constructor[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#dynamic-shape-constructor "Link to this heading")

Note

Tags: [torch.dynamic-shape](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-shape.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class DynamicShapeConstructor(torch.nn.Module):
    """
    Tensor constructors should be captured with dynamic shape inputs rather
    than being baked in with static shape.
    """

    def forward(self, x):
        return torch.zeros(x.shape\[0\] \* 2)

example\_args \= (torch.randn(3, 2),)
tags \= {"torch.dynamic-shape"}
model \= DynamicShapeConstructor()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]"):
                zeros: "f32\[6\]" \= torch.ops.aten.zeros.default(\[6\], device \= device(type\='cpu'), pin\_memory \= False)
            return (zeros,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    zeros: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### dynamic\_shape\_if\_guard[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#dynamic-shape-if-guard "Link to this heading")

Note

Tags: [python.control-flow](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.control-flow.html)
, [torch.dynamic-shape](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-shape.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class DynamicShapeIfGuard(torch.nn.Module):
    """
    \`if\` statement with backed dynamic shape predicate will be specialized into
    one particular branch and generate a guard. However, export will fail if the
    dimension is marked as dynamic shape from higher level API.
    """

    def forward(self, x):
        if x.shape\[0\] \== 3:
            return x.cos()

        return x.sin()

example\_args \= (torch.randn(3, 2, 2),)
tags \= {"torch.dynamic-shape", "python.control-flow"}
model \= DynamicShapeIfGuard()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2, 2\]"):
                cos: "f32\[3, 2, 2\]" \= torch.ops.aten.cos.default(x);  x \= None
            return (cos,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    cos: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### dynamic\_shape\_map[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#dynamic-shape-map "Link to this heading")

Note

Tags: [torch.dynamic-shape](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-shape.html)
, [torch.map](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.map.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

from functorch.experimental.control\_flow import map

class DynamicShapeMap(torch.nn.Module):
    """
    functorch map() maps a function over the first tensor dimension.
    """

    def forward(self, xs, y):
        def body(x, y):
            return x + y

        return map(body, xs, y)

example\_args \= (torch.randn(3, 2), torch.randn(2))
tags \= {"torch.dynamic-shape", "torch.map"}
model \= DynamicShapeMap()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, xs: "f32\[3, 2\]", y: "f32\[2\]"):
                body\_graph\_0 \= self.body\_graph\_0
            map\_impl \= torch.ops.higher\_order.map\_impl(body\_graph\_0, \[xs\], \[y\]);  body\_graph\_0 \= xs \= y \= None
            getitem: "f32\[3, 2\]" \= map\_impl\[0\];  map\_impl \= None
            return (getitem,)

        class body\_graph\_0(torch.nn.Module):
            def forward(self, xs: "f32\[2\]", y: "f32\[2\]"):
                        add: "f32\[2\]" \= torch.ops.aten.add.Tensor(xs, y);  xs \= y \= None
                return (add,)

Graph signature:
    \# inputs
    xs: USER\_INPUT
    y: USER\_INPUT

    \# outputs
    getitem: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### dynamic\_shape\_slicing[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#dynamic-shape-slicing "Link to this heading")

Note

Tags: [torch.dynamic-shape](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-shape.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class DynamicShapeSlicing(torch.nn.Module):
    """
    Slices with dynamic shape arguments should be captured into the graph
    rather than being baked in.
    """

    def forward(self, x):
        return x\[: x.shape\[0\] \- 2, x.shape\[1\] \- 1 :: 2\]

example\_args \= (torch.randn(3, 2),)
tags \= {"torch.dynamic-shape"}
model \= DynamicShapeSlicing()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]"):
                slice\_1: "f32\[1, 2\]" \= torch.ops.aten.slice.Tensor(x, 0, 0, 1);  x \= None
            slice\_2: "f32\[1, 1\]" \= torch.ops.aten.slice.Tensor(slice\_1, 1, 1, 9223372036854775807, 2);  slice\_1 \= None
            return (slice\_2,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    slice\_2: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### dynamic\_shape\_view[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#dynamic-shape-view "Link to this heading")

Note

Tags: [torch.dynamic-shape](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-shape.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class DynamicShapeView(torch.nn.Module):
    """
    Dynamic shapes should be propagated to view arguments instead of being
    baked into the exported graph.
    """

    def forward(self, x):
        new\_x\_shape \= x.size()\[:\-1\] + (2, 5)
        x \= x.view(\*new\_x\_shape)
        return x.permute(0, 2, 1)

example\_args \= (torch.randn(10, 10),)
tags \= {"torch.dynamic-shape"}
model \= DynamicShapeView()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[10, 10\]"):
                view: "f32\[10, 2, 5\]" \= torch.ops.aten.view.default(x, \[10, 2, 5\]);  x \= None

                permute: "f32\[10, 5, 2\]" \= torch.ops.aten.permute.default(view, \[0, 2, 1\]);  view \= None
            return (permute,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    permute: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### fn\_with\_kwargs[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#fn-with-kwargs "Link to this heading")

Note

Tags: [python.data-structure](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.data-structure.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class FnWithKwargs(torch.nn.Module):
    """
    Keyword arguments are not supported at the moment.
    """

    def forward(self, pos0, tuple0, \*myargs, mykw0, \*\*mykwargs):
        out \= pos0
        for arg in tuple0:
            out \= out \* arg
        for arg in myargs:
            out \= out \* arg
        out \= out \* mykw0
        out \= out \* mykwargs\["input0"\] \* mykwargs\["input1"\]
        return out

example\_args \= (
    torch.randn(4),
    (torch.randn(4), torch.randn(4)),
    \*\[torch.randn(4), torch.randn(4)\]
)
example\_kwargs \= {
    "mykw0": torch.randn(4),
    "input0": torch.randn(4),
    "input1": torch.randn(4),
}
tags \= {"python.data-structure"}
model \= FnWithKwargs()

torch.export.export(model, example\_args, example\_kwargs)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, pos0: "f32\[4\]", tuple0\_0: "f32\[4\]", tuple0\_1: "f32\[4\]", myargs\_0: "f32\[4\]", myargs\_1: "f32\[4\]", mykw0: "f32\[4\]", input0: "f32\[4\]", input1: "f32\[4\]"):
                mul: "f32\[4\]" \= torch.ops.aten.mul.Tensor(pos0, tuple0\_0);  pos0 \= tuple0\_0 \= None
            mul\_1: "f32\[4\]" \= torch.ops.aten.mul.Tensor(mul, tuple0\_1);  mul \= tuple0\_1 \= None

                mul\_2: "f32\[4\]" \= torch.ops.aten.mul.Tensor(mul\_1, myargs\_0);  mul\_1 \= myargs\_0 \= None
            mul\_3: "f32\[4\]" \= torch.ops.aten.mul.Tensor(mul\_2, myargs\_1);  mul\_2 \= myargs\_1 \= None

                mul\_4: "f32\[4\]" \= torch.ops.aten.mul.Tensor(mul\_3, mykw0);  mul\_3 \= mykw0 \= None

                mul\_5: "f32\[4\]" \= torch.ops.aten.mul.Tensor(mul\_4, input0);  mul\_4 \= input0 \= None
            mul\_6: "f32\[4\]" \= torch.ops.aten.mul.Tensor(mul\_5, input1);  mul\_5 \= input1 \= None
            return (mul\_6,)

Graph signature:
    \# inputs
    pos0: USER\_INPUT
    tuple0\_0: USER\_INPUT
    tuple0\_1: USER\_INPUT
    myargs\_0: USER\_INPUT
    myargs\_1: USER\_INPUT
    mykw0: USER\_INPUT
    input0: USER\_INPUT
    input1: USER\_INPUT

    \# outputs
    mul\_6: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### list\_contains[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#list-contains "Link to this heading")

Note

Tags: [python.assert](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.assert.html)
, [python.data-structure](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.data-structure.html)
, [torch.dynamic-shape](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-shape.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class ListContains(torch.nn.Module):
    """
    List containment relation can be checked on a dynamic shape or constants.
    """

    def forward(self, x):
        assert x.size(\-1) in \[6, 2\]  \# noqa: S101
        assert x.size(0) not in \[4, 5, 6\]  \# noqa: S101
        assert "monkey" not in \["cow", "pig"\]  \# noqa: S101
        return x + x

example\_args \= (torch.randn(3, 2),)
tags \= {"torch.dynamic-shape", "python.data-structure", "python.assert"}
model \= ListContains()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]"):
                add: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(x, x);  x \= None
            return (add,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    add: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### list\_unpack[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#list-unpack "Link to this heading")

Note

Tags: [python.control-flow](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.control-flow.html)
, [python.data-structure](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.data-structure.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs

import torch

class ListUnpack(torch.nn.Module):
    """
    Lists are treated as static construct, therefore unpacking should be
    erased after tracing.
    """

    def forward(self, args: list\[torch.Tensor\]):
        """
        Lists are treated as static construct, therefore unpacking should be
        erased after tracing.
        """
        x, \*y \= args
        return x + y\[0\]

example\_args \= (\[torch.randn(3, 2), torch.tensor(4), torch.tensor(5)\],)
tags \= {"python.control-flow", "python.data-structure"}
model \= ListUnpack()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, args\_0: "f32\[3, 2\]", args\_1: "i64\[\]", args\_2: "i64\[\]"):
                add: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(args\_0, args\_1);  args\_0 \= args\_1 \= None
            return (add,)

Graph signature:
    \# inputs
    args\_0: USER\_INPUT
    args\_1: USER\_INPUT
    args\_2: USER\_INPUT

    \# outputs
    add: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### model\_attr\_mutation[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#model-attr-mutation "Link to this heading")

Note

Tags: [python.object-model](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.object-model.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class ModelAttrMutation(torch.nn.Module):
    """
    Attribute mutation raises a warning. Covered in the test\_export.py test\_detect\_leak\_strict test.
    """

    def \_\_init\_\_(self) \-> None:
        super().\_\_init\_\_()
        self.attr\_list \= \[torch.randn(3, 2), torch.randn(3, 2)\]

    def recreate\_list(self):
        return \[torch.zeros(3, 2), torch.zeros(3, 2)\]

    def forward(self, x):
        self.attr\_list \= self.recreate\_list()
        return x.sum() + self.attr\_list\[0\].sum()

example\_args \= (torch.randn(3, 2),)
tags \= {"python.object-model"}
model \= ModelAttrMutation()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]"):
                zeros: "f32\[3, 2\]" \= torch.ops.aten.zeros.default(\[3, 2\], device \= device(type\='cpu'), pin\_memory \= False)
            zeros\_1: "f32\[3, 2\]" \= torch.ops.aten.zeros.default(\[3, 2\], device \= device(type\='cpu'), pin\_memory \= False);  zeros\_1 \= None

                sum\_1: "f32\[\]" \= torch.ops.aten.sum.default(x);  x \= None
            sum\_2: "f32\[\]" \= torch.ops.aten.sum.default(zeros);  zeros \= None
            add: "f32\[\]" \= torch.ops.aten.add.Tensor(sum\_1, sum\_2);  sum\_1 \= sum\_2 \= None
            return (add,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    add: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### nested\_function[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#nested-function "Link to this heading")

Note

Tags: [python.closure](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.closure.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class NestedFunction(torch.nn.Module):
    """
    Nested functions are traced through. Side effects on global captures
    are not supported though.
    """

    def forward(self, a, b):
        x \= a + b
        z \= a \- b

        def closure(y):
            nonlocal x
            x += 1
            return x \* y + z

        return closure(x)

example\_args \= (torch.randn(3, 2), torch.randn(2))
tags \= {"python.closure"}
model \= NestedFunction()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, a: "f32\[3, 2\]", b: "f32\[2\]"):
                add: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(a, b)

                sub: "f32\[3, 2\]" \= torch.ops.aten.sub.Tensor(a, b);  a \= b \= None

                add\_: "f32\[3, 2\]" \= torch.ops.aten.add\_.Tensor(add, 1);  add \= None

                mul: "f32\[3, 2\]" \= torch.ops.aten.mul.Tensor(add\_, add\_);  add\_ \= None
            add\_1: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(mul, sub);  mul \= sub \= None
            return (add\_1,)

Graph signature:
    \# inputs
    a: USER\_INPUT
    b: USER\_INPUT

    \# outputs
    add\_1: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### null\_context\_manager[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#null-context-manager "Link to this heading")

Note

Tags: [python.context-manager](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.context-manager.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import contextlib

import torch

class NullContextManager(torch.nn.Module):
    """
    Null context manager in Python will be traced out.
    """

    def forward(self, x):
        """
        Null context manager in Python will be traced out.
        """
        ctx \= contextlib.nullcontext()
        with ctx:
            return x.sin() + x.cos()

example\_args \= (torch.randn(3, 2),)
tags \= {"python.context-manager"}
model \= NullContextManager()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]"):
                sin: "f32\[3, 2\]" \= torch.ops.aten.sin.default(x)
            cos: "f32\[3, 2\]" \= torch.ops.aten.cos.default(x);  x \= None
            add: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(sin, cos);  sin \= cos \= None
            return (add,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    add: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### optional\_input[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#optional-input "Link to this heading")

Note

Tags: [python.object-model](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.object-model.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch
from torch.\_export.db.case import SupportLevel

class OptionalInput(torch.nn.Module):
    """
    Tracing through optional input is not supported yet
    """

    def forward(self, x, y\=torch.randn(2, 3)):
        if y is not None:
            return x + y
        return x

example\_args \= (torch.randn(2, 3),)
tags \= {"python.object-model"}
support\_level \= SupportLevel.SUPPORTED
model \= OptionalInput()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, c\_dict\_type\_l\_\_self\_\_\_\_\_\_dict\_\_\_\_\_forward\_\_\_\_\_defaults\_\_\_0: "f32\[2, 3\]", x: "f32\[2, 3\]"):
                add: "f32\[2, 3\]" \= torch.ops.aten.add.Tensor(x, c\_dict\_type\_l\_\_self\_\_\_\_\_\_dict\_\_\_\_\_forward\_\_\_\_\_defaults\_\_\_0);  x \= c\_dict\_type\_l\_\_self\_\_\_\_\_\_dict\_\_\_\_\_forward\_\_\_\_\_defaults\_\_\_0 \= None
            return (add,)

Graph signature:
    \# inputs
    c\_dict\_type\_l\_\_self\_\_\_\_\_\_dict\_\_\_\_\_forward\_\_\_\_\_defaults\_\_\_0: CONSTANT\_TENSOR target\='dict\_type\_L\_\_self\_\_\_\_\_\_dict\_\_\_\_\_forward\_\_\_\_\_defaults\_\_\_0'
    x: USER\_INPUT

    \# outputs
    add: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### pytree\_flatten[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#pytree-flatten "Link to this heading")

Note

Tags:

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

from torch.utils import \_pytree as pytree

class PytreeFlatten(torch.nn.Module):
    """
    Pytree from PyTorch can be captured by TorchDynamo.
    """

    def forward(self, x):
        y, \_spec \= pytree.tree\_flatten(x)
        return y\[0\] + 1

example\_args \= ({1: torch.randn(3, 2), 2: torch.randn(3, 2)},),
model \= PytreeFlatten()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x\_0\_1: "f32\[3, 2\]", x\_0\_2: "f32\[3, 2\]"):
                add: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(x\_0\_1, 1);  x\_0\_1 \= None
            return (add,)

Graph signature:
    \# inputs
    x\_0\_1: USER\_INPUT
    x\_0\_2: USER\_INPUT

    \# outputs
    add: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### scalar\_output[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#scalar-output "Link to this heading")

Note

Tags: [torch.dynamic-shape](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-shape.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

from torch.export import Dim

x \= torch.randn(3, 2)
dim1\_x \= Dim("dim1\_x")

class ScalarOutput(torch.nn.Module):
    """
    Returning scalar values from the graph is supported, in addition to Tensor
    outputs. Symbolic shapes are captured and rank is specialized.
    """
    def \_\_init\_\_(self) \-> None:
        super().\_\_init\_\_()

    def forward(self, x):
        return x.shape\[1\] + 1

example\_args \= (x,)
tags \= {"torch.dynamic-shape"}
dynamic\_shapes \= {"x": {1: dim1\_x}}
model \= ScalarOutput()

torch.export.export(model, example\_args, dynamic\_shapes\=dynamic\_shapes)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, s11\]"):
            \# No stacktrace found for following nodes
            sym\_size\_int\_1: "Sym(s11)" \= torch.ops.aten.sym\_size.int(x, 1);  x \= None

                add: "Sym(s11 + 1)" \= sym\_size\_int\_1 + 1;  sym\_size\_int\_1 \= None
            return (add,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    add: USER\_OUTPUT

Range constraints: {s11: VR\[0, int\_oo\]}

Copy to clipboard

### specialized\_attribute[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#specialized-attribute "Link to this heading")

Note

Tags:

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
from enum import Enum

import torch

class Animal(Enum):
    COW \= "moo"

class SpecializedAttribute(torch.nn.Module):
    """
    Model attributes are specialized.
    """

    def \_\_init\_\_(self) \-> None:
        super().\_\_init\_\_()
        self.a \= "moo"
        self.b \= 4

    def forward(self, x):
        if self.a \== Animal.COW.value:
            return x \* x + self.b
        else:
            raise ValueError("bad")

example\_args \= (torch.randn(3, 2),)
model \= SpecializedAttribute()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]"):
                mul: "f32\[3, 2\]" \= torch.ops.aten.mul.Tensor(x, x);  x \= None
            add: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(mul, 4);  mul \= None
            return (add,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    add: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### static\_for\_loop[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#static-for-loop "Link to this heading")

Note

Tags: [python.control-flow](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.control-flow.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class StaticForLoop(torch.nn.Module):
    """
    A for loop with constant number of iterations should be unrolled in the exported graph.
    """

    def forward(self, x):
        \# constant
        ret \= \[i + x for i in range(10)\]
        return ret

example\_args \= (torch.randn(3, 2),)
tags \= {"python.control-flow"}
model \= StaticForLoop()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]"):
                add: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(x, 0)
            add\_1: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(x, 1)
            add\_2: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(x, 2)
            add\_3: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(x, 3)
            add\_4: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(x, 4)
            add\_5: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(x, 5)
            add\_6: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(x, 6)
            add\_7: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(x, 7)
            add\_8: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(x, 8)
            add\_9: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(x, 9);  x \= None
            return (add, add\_1, add\_2, add\_3, add\_4, add\_5, add\_6, add\_7, add\_8, add\_9)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    add: USER\_OUTPUT
    add\_1: USER\_OUTPUT
    add\_2: USER\_OUTPUT
    add\_3: USER\_OUTPUT
    add\_4: USER\_OUTPUT
    add\_5: USER\_OUTPUT
    add\_6: USER\_OUTPUT
    add\_7: USER\_OUTPUT
    add\_8: USER\_OUTPUT
    add\_9: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### static\_if[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#static-if "Link to this heading")

Note

Tags: [python.control-flow](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.control-flow.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class StaticIf(torch.nn.Module):
    """
    \`if\` statement with static predicate value should be traced through with the
    taken branch.
    """

    def forward(self, x):
        if len(x.shape) \== 3:
            return x + torch.ones(1, 1, 1)

        return x

example\_args \= (torch.randn(3, 2, 2),)
tags \= {"python.control-flow"}
model \= StaticIf()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2, 2\]"):
                ones: "f32\[1, 1, 1\]" \= torch.ops.aten.ones.default(\[1, 1, 1\], device \= device(type\='cpu'), pin\_memory \= False)
            add: "f32\[3, 2, 2\]" \= torch.ops.aten.add.Tensor(x, ones);  x \= ones \= None
            return (add,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    add: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### tensor\_setattr[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#tensor-setattr "Link to this heading")

Note

Tags: [python.builtin](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.builtin.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class TensorSetattr(torch.nn.Module):
    """
    setattr() call onto tensors is not supported.
    """
    def forward(self, x, attr):
        setattr(x, attr, torch.randn(3, 2))
        return x + 4

example\_args \= (torch.randn(3, 2), "attr")
tags \= {"python.builtin"}
model \= TensorSetattr()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]", attr):
                randn: "f32\[3, 2\]" \= torch.ops.aten.randn.default(\[3, 2\], device \= device(type\='cpu'), pin\_memory \= False);  randn \= None

                add: "f32\[3, 2\]" \= torch.ops.aten.add.Tensor(x, 4);  x \= None
            return (add,)

Graph signature:
    \# inputs
    x: USER\_INPUT
    attr: USER\_INPUT

    \# outputs
    add: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### type\_reflection\_method[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#type-reflection-method "Link to this heading")

Note

Tags: [python.builtin](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.builtin.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class A:
    @classmethod
    def func(cls, x):
        return 1 + x

class TypeReflectionMethod(torch.nn.Module):
    """
    type() calls on custom objects followed by attribute accesses are not allowed
    due to its overly dynamic nature.
    """

    def forward(self, x):
        a \= A()
        return type(a).func(x)

example\_args \= (torch.randn(3, 4),)
tags \= {"python.builtin"}
model \= TypeReflectionMethod()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 4\]"):
                add: "f32\[3, 4\]" \= torch.ops.aten.add.Tensor(x, 1);  x \= None
            return (add,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    add: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### unsupported\_operator[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#unsupported-operator "Link to this heading")

Note

Tags: [torch.operator](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.operator.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch
from torch.\_export.db.case import SupportLevel

class TorchSymMin(torch.nn.Module):
    """
    torch.sym\_min operator is supported in export.
    """

    def forward(self, x):
        return x.sum() + torch.sym\_min(x.size(0), 100)

example\_args \= (torch.randn(3, 2),)
tags \= {"torch.operator"}
support\_level \= SupportLevel.SUPPORTED
model \= TorchSymMin()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]"):
                sum\_1: "f32\[\]" \= torch.ops.aten.sum.default(x);  x \= None
            add: "f32\[\]" \= torch.ops.aten.add.Tensor(sum\_1, 3);  sum\_1 \= None
            return (add,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    add: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

### user\_input\_mutation[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#user-input-mutation "Link to this heading")

Note

Tags: [torch.mutation](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.mutation.html)

Support Level: SUPPORTED

Original source code:

\# mypy: allow-untyped-defs
import torch

class UserInputMutation(torch.nn.Module):
    """
    Directly mutate user input in forward
    """

    def forward(self, x):
        x.mul\_(2)
        return x.cos()

example\_args \= (torch.randn(3, 2),)
tags \= {"torch.mutation"}
model \= UserInputMutation()

torch.export.export(model, example\_args)

Copy to clipboard

Result:

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32\[3, 2\]"):
                mul\_: "f32\[3, 2\]" \= torch.ops.aten.mul\_.Tensor(x, 2);  x \= None

                cos: "f32\[3, 2\]" \= torch.ops.aten.cos.default(mul\_);  mul\_ \= None
            return (cos,)

Graph signature:
    \# inputs
    x: USER\_INPUT

    \# outputs
    cos: USER\_OUTPUT

Range constraints: {}

Copy to clipboard

Not Supported Yet[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#not-supported-yet "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

### dynamic\_shape\_round[#](https://docs.pytorch.org/docs/2.15/generated/exportdb/index.html#dynamic-shape-round "Link to this heading")

Note

Tags: [torch.dynamic-shape](https://docs.pytorch.org/docs/2.15/generated/exportdb/torch.dynamic-shape.html)
, [python.builtin](https://docs.pytorch.org/docs/2.15/generated/exportdb/python.builtin.html)

Support Level: NOT\_SUPPORTED\_YET

Original source code:

\# mypy: allow-untyped-defs
import torch

from torch.\_export.db.case import SupportLevel
from torch.export import Dim

class DynamicShapeRound(torch.nn.Module):
    """
    Calling round on dynamic shapes is not supported.
    """

    def forward(self, x):
        return x\[: round(x.shape\[0\] / 2)\]

x \= torch.randn(3, 2)
dim0\_x \= Dim("dim0\_x")
example\_args \= (x,)
tags \= {"torch.dynamic-shape", "python.builtin"}
support\_level \= SupportLevel.NOT\_SUPPORTED\_YET
dynamic\_shapes \= {"x": {0: dim0\_x}}
model \= DynamicShapeRound()

torch.export.export(model, example\_args, dynamic\_shapes\=dynamic\_shapes)

Copy to clipboard

Result:

RuntimeError: Constraints violated (dim0\_x)! For more information, run with TORCH\_LOGS="+dynamic".

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/exportdb/index.rst.txt)

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