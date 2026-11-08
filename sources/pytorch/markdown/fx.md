Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/fx.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/fx.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/fx.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/fx.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/fx.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/fx.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/fx.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/fx.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/fx.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/fx.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/fx.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/fx.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/fx.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/fx.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/fx.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/fx.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/fx.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/fx.html)
[v1.13](https://docs.pytorch.org/docs/1.13/fx.html)
[v1.12](https://docs.pytorch.org/docs/1.12/fx.html)
[v1.11](https://docs.pytorch.org/docs/1.11/fx.html)
[v1.10](https://docs.pytorch.org/docs/1.10/fx.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/fx.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/fx.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/fx.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/fx.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/fx.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/fx.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/fx.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/fx.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/fx.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/fx.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/fx.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/fx.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/fx.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/fx.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/fx.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/fx.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/fx.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/fx.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/fx.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/fx.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/fx.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/fx.html)

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

torch.fx[#](https://docs.pytorch.org/docs/2.15/fx.html#torch-fx "Link to this heading")

========================================================================================

Created On: Dec 15, 2020 | Last Updated On: May 08, 2026

Overview[#](https://docs.pytorch.org/docs/2.15/fx.html#module-torch.fx "Link to this heading")

-----------------------------------------------------------------------------------------------

FX is a toolkit for developers to use to transform `nn.Module` instances. FX consists of three main components: a **symbolic tracer,** an **intermediate representation**, and **Python code generation**. A demonstration of these components in action:

import torch

\# Simple module for demonstration
class MyModule(torch.nn.Module):
    def \_\_init\_\_(self) \-> None:
        super().\_\_init\_\_()
        self.param \= torch.nn.Parameter(torch.rand(3, 4))
        self.linear \= torch.nn.Linear(4, 5)

    def forward(self, x):
        return self.linear(x + self.param).clamp(min\=0.0, max\=1.0)

module \= MyModule()

from torch.fx import symbolic\_trace

\# Symbolic tracing frontend - captures the semantics of the module
symbolic\_traced: torch.fx.GraphModule \= symbolic\_trace(module)

\# High-level intermediate representation (IR) - Graph representation
print(symbolic\_traced.graph)
"""
graph():
    %x : \[num\_users=1\] = placeholder\[target=x\]
    %param : \[num\_users=1\] = get\_attr\[target=param\]
    %add : \[num\_users=1\] = call\_function\[target=operator.add\](args = (%x, %param), kwargs = {})
    %linear : \[num\_users=1\] = call\_module\[target=linear\](args = (%add,), kwargs = {})
    %clamp : \[num\_users=1\] = call\_method\[target=clamp\](args = (%linear,), kwargs = {min: 0.0, max: 1.0})
    return clamp
"""

\# Code generation - valid Python code
print(symbolic\_traced.code)
"""
def forward(self, x):
    param = self.param
    add = x + param;  x = param = None
    linear = self.linear(add);  add = None
    clamp = linear.clamp(min = 0.0, max = 1.0);  linear = None
    return clamp
"""

Copy to clipboard

The **symbolic tracer** performs “symbolic execution” of the Python code. It feeds fake values, called Proxies, through the code. Operations on these Proxies are recorded. More information about symbolic tracing can be found in the [`symbolic_trace()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.symbolic_trace "torch.fx.symbolic_trace")
 and [`Tracer`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer "torch.fx.Tracer")
 documentation.

The **intermediate representation** is the container for the operations that were recorded during symbolic tracing. It consists of a list of Nodes that represent function inputs, callsites (to functions, methods, or [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
 instances), and return values. More information about the IR can be found in the documentation for [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
. The IR is the format on which transformations are applied.

**Python code generation** is what makes FX a Python-to-Python (or Module-to-Module) transformation toolkit. For each Graph IR, we can create valid Python code matching the Graph’s semantics. This functionality is wrapped up in [`GraphModule`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.GraphModule")
, which is a [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
 instance that holds a [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
 as well as a `forward` method generated from the Graph.

Taken together, this pipeline of components (symbolic tracing -> intermediate representation -> transforms -> Python code generation) constitutes the Python-to-Python transformation pipeline of FX. In addition, these components can be used separately. For example, symbolic tracing can be used in isolation to capture a form of the code for analysis (and not transformation) purposes. Code generation can be used for programmatically generating models, for example from a config file. There are many uses for FX!

Several example transformations can be found at the [examples](https://github.com/pytorch/examples/tree/master/fx)
 repository.

Writing Transformations[#](https://docs.pytorch.org/docs/2.15/fx.html#writing-transformations "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

What is an FX transform? Essentially, it’s a function that looks like this.

import torch
import torch.fx

def transform(m: nn.Module,
                tracer\_class : type \= torch.fx.Tracer) \-> torch.nn.Module:
    \# Step 1: Acquire a Graph representing the code in \`m\`

    \# NOTE: torch.fx.symbolic\_trace is a wrapper around a call to
    \# fx.Tracer.trace and constructing a GraphModule. We'll
    \# split that out in our transform to allow the caller to
    \# customize tracing behavior.
    graph : torch.fx.Graph \= tracer\_class().trace(m)

    \# Step 2: Modify this Graph or create a new one
    graph \= ...

    \# Step 3: Construct a Module to return
    return torch.fx.GraphModule(m, graph)

Copy to clipboard

Your transform will take in a [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
, acquire a [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
 from it, do some modifications, and return a new [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
. You should think of the [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
 that your FX transform returns as identical to a regular [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
 – you can pass it to another FX transform, or you can run it. Ensuring that the inputs and outputs of your FX transform are a [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
 will allow for composability.

Note

It is also possible to modify an existing [`GraphModule`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.GraphModule")
 instead of creating a new one, like so:

import torch
import torch.fx

def transform(m : nn.Module) \-> nn.Module:
    gm : torch.fx.GraphModule \= torch.fx.symbolic\_trace(m)

    \# Modify gm.graph
    \# <...>

    \# Recompile the forward() method of \`gm\` from its Graph
    gm.recompile()

    return gm

Copy to clipboard

Note that you MUST call [`GraphModule.recompile()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule.recompile "torch.fx.GraphModule.recompile")
 to bring the generated `forward()` method on the `GraphModule` in sync with the modified [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
.

Given that you’ve passed in a [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
 that has been traced into a [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
, there are now two primary approaches you can take to building a new [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
.

### A Quick Primer on Graphs[#](https://docs.pytorch.org/docs/2.15/fx.html#a-quick-primer-on-graphs "Link to this heading")

Full treatment of the semantics of graphs can be found in the [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
 documentation, but we are going to cover the basics here. A [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
 is a data structure that represents a method on a [`GraphModule`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.GraphModule")
. The information that this requires is:

*   What are the inputs to the method?
    
*   What are the operations that run inside the method?
    
*   What is the output (i.e. return) value from the method?
    

All three of these concepts are represented with [`Node`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")
 instances. Let’s see what we mean by that with a short example:

import torch
import torch.fx

class MyModule(torch.nn.Module):
    def \_\_init\_\_(self):
        super().\_\_init\_\_()
        self.param \= torch.nn.Parameter(torch.rand(3, 4))
        self.linear \= torch.nn.Linear(4, 5)

    def forward(self, x):
        return torch.topk(torch.sum(
            self.linear(x + self.linear.weight).relu(), dim\=-1), 3)

m \= MyModule()
gm \= torch.fx.symbolic\_trace(m)

gm.graph.print\_tabular()

Copy to clipboard

Here we define a module `MyModule` for demonstration purposes, instantiate it, symbolically trace it, then call the [`Graph.print_tabular()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.print_tabular "torch.fx.Graph.print_tabular")
 method to print out a table showing the nodes of this [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
:

| opcode | name | target | args | kwargs |
| --- | --- | --- | --- | --- |
| placeholder | x   | x   | ()  | {}  |
| get\_attr | linear\_weight | linear.weight | ()  | {}  |
| call\_function | add\_1 |     | (x, linear\_weight) | {}  |
| call\_module | linear\_1 | linear | (add\_1,) | {}  |
| call\_method | relu\_1 | relu | (linear\_1,) | {}  |
| call\_function | sum\_1 | <built-in method sum …> | (relu\_1,) | {‘dim’: -1} |
| call\_function | topk\_1 | <built-in method topk …> | (sum\_1, 3) | {}  |
| output | output | output | (topk\_1,) | {}  |

We can use this information to answer the questions we posed above.

*   What are the inputs to the method? In FX, method inputs are specified via special `placeholder` nodes. In this case, we have a single `placeholder` node with a `target` of `x`, meaning we have a single (non-self) argument named x.
    
*   What are the operations within the method? The `get_attr`, `call_function`, `call_module`, and `call_method` nodes represent the operations in the method. A full treatment of the semantics of all of these can be found in the [`Node`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")
     documentation.
    
*   What is the return value of the method? The return value in a [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
     is specified by a special `output` node.
    

Given that we now know the basics of how code is represented in FX, we can now explore how we would edit a [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
.

### Graph Manipulation[#](https://docs.pytorch.org/docs/2.15/fx.html#graph-manipulation "Link to this heading")

#### Direct Graph Manipulation[#](https://docs.pytorch.org/docs/2.15/fx.html#direct-graph-manipulation "Link to this heading")

One approach to building this new [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
 is to directly manipulate your old one. To aid in this, we can simply take the [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
 we obtain from symbolic tracing and modify it. For example, let’s say we desire to replace [`torch.add()`](https://docs.pytorch.org/docs/2.15/generated/torch.add.html#torch.add "torch.add")
 calls with [`torch.mul()`](https://docs.pytorch.org/docs/2.15/generated/torch.mul.html#torch.mul "torch.mul")
 calls.

import torch
import torch.fx

\# Sample module
class M(torch.nn.Module):
    def forward(self, x, y):
        return torch.add(x, y)

def transform(m: torch.nn.Module,
                tracer\_class : type \= fx.Tracer) \-> torch.nn.Module:
    graph : fx.Graph \= tracer\_class().trace(m)
    \# FX represents its Graph as an ordered list of
    \# nodes, so we can iterate through them.
    for node in graph.nodes:
        \# Checks if we're calling a function (i.e:
        \# torch.add)
        if node.op \== 'call\_function':
            \# The target attribute is the function
            \# that call\_function calls.
            if node.target \== torch.add:
                node.target \= torch.mul

    graph.lint() \# Does some checks to make sure the
                    \# Graph is well-formed.

    return fx.GraphModule(m, graph)

Copy to clipboard

We can also do more involved [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
 rewrites, such as deleting or appending nodes. To aid in these transformations, FX has utility functions for transforming the graph that can be found in the [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
 documentation. An example of using these APIs to append a `torch.relu()` call can be found below.

\# Specifies the insertion point. Any nodes added to the
\# Graph within this scope will be inserted after \`node\`
with traced.graph.inserting\_after(node):
    \# Insert a new \`call\_function\` node calling \`torch.relu\`
    new\_node \= traced.graph.call\_function(
        torch.relu, args\=(node,))

    \# We want all places that used the value of \`node\` to
    \# now use that value after the \`relu\` call we've added.
    \# We use the \`replace\_all\_uses\_with\` API to do this.
    node.replace\_all\_uses\_with(new\_node)

Copy to clipboard

For simple transformations that only consist of substitutions, you can also make use of the [subgraph rewriter.](https://github.com/pytorch/pytorch/blob/main/torch/fx/subgraph_rewriter.py)

#### Subgraph Rewriting With replace\_pattern()[#](https://docs.pytorch.org/docs/2.15/fx.html#subgraph-rewriting-with-replace-pattern "Link to this heading")

FX also provides another level of automation on top of direct graph manipulation. The [`replace_pattern()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.replace_pattern "torch.fx.replace_pattern")
 API is essentially a “find/replace” tool for editing [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
\\s. It allows you to specify a `pattern` and `replacement` function and it will trace through those functions, find instances of the group of operations in the `pattern` graph, and replace those instances with copies of the `replacement` graph. This can help to greatly automate tedious graph manipulation code, which can get unwieldy as the transformations get more complex.

#### Graph Manipulation Examples[#](https://docs.pytorch.org/docs/2.15/fx.html#graph-manipulation-examples "Link to this heading")

*   [Replace one op](https://github.com/pytorch/examples/blob/master/fx/replace_op.py)
    
*   [Conv/Batch Norm fusion](https://github.com/pytorch/pytorch/blob/40cbf342d3c000712da92cfafeaca651b3e0bd3e/torch/fx/experimental/optimization.py#L50)
    
*   [replace\_pattern: Basic usage](https://github.com/pytorch/examples/blob/master/fx/subgraph_rewriter_basic_use.py)
    
*   [Quantization](https://pytorch.org/docs/main/quantization.html#prototype-fx-graph-mode-quantization)
    
*   [Invert Transformation](https://github.com/pytorch/examples/blob/master/fx/invert.py)
    

### Proxy/Retracing[#](https://docs.pytorch.org/docs/2.15/fx.html#proxy-retracing "Link to this heading")

Another way of manipulating [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
\\s is by reusing the [`Proxy`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "torch.fx.Proxy")
 machinery used in symbolic tracing. For example, let’s imagine that we wanted to write a transformation that decomposed PyTorch functions into smaller operations. It would transform every `F.relu(x)` call into `(x > 0) * x`. One possibility would be to perform the requisite graph rewriting to insert the comparison and multiplication after the `F.relu`, and then clean up the original `F.relu`. However, we can automate this process by using [`Proxy`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "torch.fx.Proxy")
 objects to automatically record operations into the [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
.

To use this method, we write the operations that we want inserted as regular PyTorch code and invoke that code with [`Proxy`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "torch.fx.Proxy")
 objects as arguments. These [`Proxy`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "torch.fx.Proxy")
 objects will capture the operations that are performed on them and append them to the [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
.

\# Note that this decomposition rule can be read as regular Python
def relu\_decomposition(x):
    return (x \> 0) \* x

decomposition\_rules \= {}
decomposition\_rules\[F.relu\] \= relu\_decomposition

def decompose(model: torch.nn.Module,
                tracer\_class : type \= fx.Tracer) \-> torch.nn.Module:
    """
    Decompose \`model\` into smaller constituent operations.
    Currently,this only supports decomposing ReLU into its
    mathematical definition: (x > 0) \* x
    """
    graph : fx.Graph \= tracer\_class().trace(model)
    new\_graph \= fx.Graph()
    env \= {}
    tracer \= torch.fx.proxy.GraphAppendingTracer(new\_graph)
    for node in graph.nodes:
        if node.op \== 'call\_function' and node.target in decomposition\_rules:
            \# By wrapping the arguments with proxies,
            \# we can dispatch to the appropriate
            \# decomposition rule and implicitly add it
            \# to the Graph by symbolically tracing it.
            proxy\_args \= \[\
                fx.Proxy(env\[x.name\], tracer) if isinstance(x, fx.Node) else x for x in node.args\]
            output\_proxy \= decomposition\_rules\[node.target\](\*proxy\_args)

            \# Operations on \`Proxy\` always yield new \`Proxy\`s, and the
            \# return value of our decomposition rule is no exception.
            \# We need to extract the underlying \`Node\` from the \`Proxy\`
            \# to use it in subsequent iterations of this transform.
            new\_node \= output\_proxy.node
            env\[node.name\] \= new\_node
        else:
            \# Default case: we don't have a decomposition rule for this
            \# node, so just copy the node over into the new graph.
            new\_node \= new\_graph.node\_copy(node, lambda x: env\[x.name\])
            env\[node.name\] \= new\_node
    return fx.GraphModule(model, new\_graph)

Copy to clipboard

In addition to avoiding explicit graph manipulation, using [`Proxy`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "torch.fx.Proxy")
\\s also allows you to specify your rewrite rules as native Python code. For transformations that require a large amount of rewrite rules (such as vmap or grad), this can often improve readability and maintainability of the rules. Note that while calling [`Proxy`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "torch.fx.Proxy")
 we also passed a tracer pointing to the underlying variable `graph`. This is done so if in case the operations in graph are n-ary (e.g. add is a binary operator) the call to [`Proxy`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "torch.fx.Proxy")
 does not create multiple instances of a graph tracer which can lead to unexpected runtime errors. We recommend this method of using [`Proxy`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "torch.fx.Proxy")
 especially when the underlying operators can not be safely assumed to be unary.

A worked example of using [`Proxy`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "torch.fx.Proxy")
\\s for [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
 manipulation can be found [here](https://github.com/pytorch/examples/blob/master/fx/proxy_based_graph_creation.py)
.

### The Interpreter Pattern[#](https://docs.pytorch.org/docs/2.15/fx.html#the-interpreter-pattern "Link to this heading")

A useful code organizational pattern in FX is to loop over all the [`Node`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")
\\s in a [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
 and execute them. This can be used for several things including runtime analysis of values flowing through the graph or transformation of the code via retracing with [`Proxy`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "torch.fx.Proxy")
\\s. For example, suppose we want to run a [`GraphModule`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.GraphModule")
 and record the [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 shape and dtype properties on the nodes as we see them at runtime. That might look like:

import torch
import torch.fx
from torch.fx.node import Node

from typing import Dict

class ShapeProp:
    """
    Shape propagation. This class takes a \`GraphModule\`.
    Then, its \`propagate\` method executes the \`GraphModule\`
    node-by-node with the given arguments. As each operation
    executes, the ShapeProp class stores away the shape and
    element type for the output values of each operation on
    the \`shape\` and \`dtype\` attributes of the operation's
    \`Node\`.
    """
    def \_\_init\_\_(self, mod):
        self.mod \= mod
        self.graph \= mod.graph
        self.modules \= dict(self.mod.named\_modules())

    def propagate(self, \*args):
        args\_iter \= iter(args)
        env : Dict\[str, Node\] \= {}

        def load\_arg(a):
            return torch.fx.graph.map\_arg(a, lambda n: env\[n.name\])

        def fetch\_attr(target : str):
            target\_atoms \= target.split('.')
            attr\_itr \= self.mod
            for i, atom in enumerate(target\_atoms):
                if not hasattr(attr\_itr, atom):
                    raise RuntimeError(f"Node referenced nonexistent target {'.'.join(target\_atoms\[:i\])}")
                attr\_itr \= getattr(attr\_itr, atom)
            return attr\_itr

        for node in self.graph.nodes:
            if node.op \== 'placeholder':
                result \= next(args\_iter)
            elif node.op \== 'get\_attr':

                result \= fetch\_attr(node.target)
            elif node.op \== 'call\_function':
                result \= node.target(\*load\_arg(node.args), \*\*load\_arg(node.kwargs))
            elif node.op \== 'call\_method':
                self\_obj, \*args \= load\_arg(node.args)
                kwargs \= load\_arg(node.kwargs)
                result \= getattr(self\_obj, node.target)(\*args, \*\*kwargs)
            elif node.op \== 'call\_module':
                result \= self.modules\[node.target\](\*load\_arg(node.args), \*\*load\_arg(node.kwargs))

            \# This is the only code specific to shape propagation.
            \# you can delete this \`if\` branch and this becomes
            \# a generic GraphModule interpreter.
            if isinstance(result, torch.Tensor):
                node.shape \= result.shape
                node.dtype \= result.dtype

            env\[node.name\] \= result

        return load\_arg(self.graph.result)

Copy to clipboard

As you can see, a full interpreter for FX is not that complicated but it can be very useful. To ease using this pattern, we provide the [`Interpreter`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Interpreter "torch.fx.Interpreter")
 class, which encompasses the above logic in a way that certain aspects of the interpreter’s execution can be overridden via method overrides.

In addition to executing operations, we can also generate a new `Graph` by feeding [`Proxy`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "torch.fx.Proxy")
 values through an interpreter. Similarly, we provide the [`Transformer`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Transformer "torch.fx.Transformer")
 class to encompass this pattern. [`Transformer`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Transformer "torch.fx.Transformer")
 behaves similarly to [`Interpreter`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Interpreter "torch.fx.Interpreter")
, but instead of calling the `run` method to get a concrete output value from the Module, you would call the [`Transformer.transform()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Transformer.transform "torch.fx.Transformer.transform")
 method to return a new [`GraphModule`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.GraphModule")
 which was subject to any transformation rules you installed as overridden methods.

#### Examples of the Interpreter Pattern[#](https://docs.pytorch.org/docs/2.15/fx.html#examples-of-the-interpreter-pattern "Link to this heading")

*   [ShapePropagation](https://github.com/pytorch/pytorch/blob/master/torch/fx/passes/shape_prop.py)
    
*   [Performance Profiler](https://github.com/pytorch/tutorials/pull/1319)
    

Debugging[#](https://docs.pytorch.org/docs/2.15/fx.html#debugging "Link to this heading")

------------------------------------------------------------------------------------------

### Introduction[#](https://docs.pytorch.org/docs/2.15/fx.html#introduction "Link to this heading")

Often in the course of authoring transformations, our code will not be quite right. In this case, we may need to do some debugging. The key is to work backwards: first, check the results of invoking the generated module to prove or disprove correctness. Then, inspect and debug the generated code. Then, debug the process of transformations that led to the generated code.

If you’re not familiar with debuggers, please see the auxiliary section [Available Debuggers](https://docs.pytorch.org/docs/2.15/fx.html#available-debuggers)
.

### Common Pitfalls in Transform Authoring[#](https://docs.pytorch.org/docs/2.15/fx.html#common-pitfalls-in-transform-authoring "Link to this heading")

*   Nondeterministic `set` iteration order. In Python, the `set` datatype is unordered. Using `set` to contain collections of objects like `Node`\\ s, for example, can cause unexpected nondeterminism. An example is iterating over a set of `Node` s to insert them into a `Graph`. Because the `set` data type is unordered, the ordering of the operations in the output program will be nondeterministic and can change across program invocations. The recommended alternative is to use a `dict` data type, which is [insertion ordered](https://mail.python.org/pipermail/python-dev/2017-December/151283.html)
     as of Python 3.7 (and as of cPython 3.6). A `dict` can be used equivalently to a set by storing values to be deduplicated in the keys of the `dict`.
    

### Checking Correctness of Modules[#](https://docs.pytorch.org/docs/2.15/fx.html#checking-correctness-of-modules "Link to this heading")

Because the output of most deep learning modules consists of floating point [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 instances, checking for equivalence between the results of two [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
 is not as straightforward as doing a simple equality check. To motivate this, let’s use an example:

import torch
import torch.fx
import torchvision.models as models

def transform(m : torch.nn.Module) \-> torch.nn.Module:
    gm \= torch.fx.symbolic\_trace(m)

    \# Imagine we're doing some transforms here
    \# <...>

    gm.recompile()

    return gm

resnet18 \= models.resnet18()
transformed\_resnet18 \= transform(resnet18)

input\_image \= torch.randn(5, 3, 224, 224)

assert resnet18(input\_image) \== transformed\_resnet18(input\_image)
"""
RuntimeError: Boolean value of Tensor with more than one value is ambiguous
"""

Copy to clipboard

Here, we’ve tried to check equality of the values of two deep learning models with the `==` equality operator. However, this is not well-  
defined both due to the issue of that operator returning a tensor and not a bool, but also because comparison of floating point values should use a margin of error (or epsilon) to account for the non-commutativity of floating point operations (see [here](https://floating-point-gui.de/errors/comparison/)
 for more details). We can use [`torch.allclose()`](https://docs.pytorch.org/docs/2.15/generated/torch.allclose.html#torch.allclose "torch.allclose")
 instead, which will give us an approximate comparison taking into account a relative and absolute tolerance threshold:

assert torch.allclose(resnet18(input\_image), transformed\_resnet18(input\_image))

Copy to clipboard

This is the first tool in our toolbox to check if transformed modules are behaving as we expect compared to a reference implementation.

### Debugging the Generated Code[#](https://docs.pytorch.org/docs/2.15/fx.html#debugging-the-generated-code "Link to this heading")

Because FX generates the `forward()` function on [`GraphModule`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.GraphModule")
\\s, using traditional debugging techniques like `print` statements or `pdb` is not as straightforward. Luckily, we have several techniques we can use for debugging the generated code.

#### Use `pdb`[#](https://docs.pytorch.org/docs/2.15/fx.html#use-pdb "Link to this heading")

Invoke `pdb` to step into the running program. Although the code that represents the [`Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")
 is not in any source file, we can still step into it manually using `pdb` when the forward pass is invoked.

import torch
import torch.fx
import torchvision.models as models

def my\_pass(inp: torch.nn.Module, tracer\_class : type \= fx.Tracer) \-> torch.nn.Module:
    graph \= tracer\_class().trace(inp)
    \# Transformation logic here
    \# <...>

    \# Return new Module
    return fx.GraphModule(inp, graph)

my\_module \= models.resnet18()
my\_module\_transformed \= my\_pass(my\_module)

input\_value \= torch.randn(5, 3, 224, 224)

\# When this line is executed at runtime, we will be dropped into an
\# interactive \`pdb\` prompt. We can use the \`step\` or \`s\` command to
\# step into the execution of the next line
import pdb; pdb.set\_trace()

my\_module\_transformed(input\_value)

Copy to clipboard

#### Print the Generated Code[#](https://docs.pytorch.org/docs/2.15/fx.html#print-the-generated-code "Link to this heading")

If you’d like to run the same code multiple times, then it can be a bit tedious to step to the right code with `pdb`. In that case, one approach is to simply copy-paste the generated `forward` pass into your code and examine it from there.

\# Assume that \`traced\` is a GraphModule that has undergone some
\# number of transforms

\# Copy this code for later
print(traced)
\# Print the code generated from symbolic tracing. This outputs:
"""
def forward(self, y):
    x = self.x
    add\_1 = x + y;  x = y = None
    return add\_1
"""

\# Subclass the original Module
class SubclassM(M):
    def \_\_init\_\_(self):
        super().\_\_init\_\_()

    \# Paste the generated \`forward\` function (the one we printed and
    \# copied above) here
    def forward(self, y):
        x \= self.x
        add\_1 \= x + y;  x \= y \= None
        return add\_1

\# Create an instance of the original, untraced Module. Then, create an
\# instance of the Module with the copied \`forward\` function. We can
\# now compare the output of both the original and the traced version.
pre\_trace \= M()
post\_trace \= SubclassM()

Copy to clipboard

#### Use the `to_folder` Function From `GraphModule`[#](https://docs.pytorch.org/docs/2.15/fx.html#use-the-to-folder-function-from-graphmodule "Link to this heading")

[`GraphModule.to_folder()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule.to_folder "torch.fx.GraphModule.to_folder")
 is a method in `GraphModule` that allows you to dump out the generated FX code to a folder. Although copying the forward pass into the code often suffices as in [Print the Generated Code](https://docs.pytorch.org/docs/2.15/fx.html#print-the-generated-code)
, it may be easier to examine modules and parameters using `to_folder`.

m \= symbolic\_trace(M())
m.to\_folder("foo", "Bar")
from foo import Bar
y \= Bar()

Copy to clipboard

After running the above example, we can then look at the code within `foo/module.py` and modify it as desired (e.g. adding `print` statements or using `pdb`) to debug the generated code.

### Debugging the Transformation[#](https://docs.pytorch.org/docs/2.15/fx.html#debugging-the-transformation "Link to this heading")

Now that we’ve identified that a transformation is creating incorrect code, it’s time to debug the transformation itself. First, we’ll check the [Limitations of Symbolic Tracing](https://docs.pytorch.org/docs/2.15/fx.html#limitations-of-symbolic-tracing)
 section in the documentation. Once we verify that tracing is working as expected, the goal becomes figuring out what went wrong during our `GraphModule` transformation. There may be a quick answer in [Writing Transformations](https://docs.pytorch.org/docs/2.15/fx.html#writing-transformations)
, but, if not, there are several ways to examine our traced module:

\# Sample Module
class M(torch.nn.Module):
    def forward(self, x, y):
        return x + y

\# Create an instance of \`M\`
m \= M()

\# Symbolically trace an instance of \`M\` (returns a GraphModule). In
\# this example, we'll only be discussing how to inspect a
\# GraphModule, so we aren't showing any sample transforms for the
\# sake of brevity.
traced \= symbolic\_trace(m)

\# Print the code produced by tracing the module.
print(traced)
\# The generated \`forward\` function is:
"""
def forward(self, x, y):
    add = x + y;  x = y = None
    return add
"""

\# Print the internal Graph.
print(traced.graph)
\# This print-out returns:
"""
graph():
    %x : \[num\_users=1\] = placeholder\[target=x\]
    %y : \[num\_users=1\] = placeholder\[target=y\]
    %add : \[num\_users=1\] = call\_function\[target=operator.add\](args = (%x, %y), kwargs = {})
    return add
"""

\# Print a tabular representation of the internal Graph.
traced.graph.print\_tabular()
\# This gives us:
"""
opcode         name    target                   args    kwargs
\-------------  ------  -----------------------  ------  --------
placeholder    x       x                        ()      {}
placeholder    y       y                        ()      {}
call\_function  add     <built-in function add>  (x, y)  {}
output         output  output                   (add,)  {}
"""

Copy to clipboard

Using the utility functions above, we can compare our traced Module before and after we’ve applied our transformations. Sometimes, a simple visual comparison is enough to trace down a bug. If it’s still not clear what’s going wrong, a debugger like `pdb` can be a good next step.

Going off of the example above, consider the following code:

\# Sample user-defined function
def transform\_graph(module: torch.nn.Module, tracer\_class : type \= fx.Tracer) \-> torch.nn.Module:
    \# Get the Graph from our traced Module
    g \= tracer\_class().trace(module)

    """
    Transformations on \`g\` go here
    """

    return fx.GraphModule(module, g)

\# Transform the Graph
transformed \= transform\_graph(traced)

\# Print the new code after our transforms. Check to see if it was
\# what we expected
print(transformed)

Copy to clipboard

Using the above example, let’s say that the call to `print(traced)` showed us that there was an error in our transforms. We want to find what goes wrong using a debugger. We start a `pdb` session. We can see what’s happening during the transform by breaking on `transform_graph(traced)`, then pressing `s` to “step into” the call to `transform_graph(traced)`.

We may also have good luck by editing the `print_tabular` method to print different attributes of the Nodes in the Graph. (For example, we might want to see the Node’s `input_nodes` and `users`.)

### Available Debuggers[#](https://docs.pytorch.org/docs/2.15/fx.html#available-debuggers "Link to this heading")

The most common Python debugger is [pdb](https://docs.python.org/3/library/pdb.html)
. You can start your program in “debug mode” with `pdb` by typing `python -m pdb FILENAME.py` into the command line, where `FILENAME` is the name of the file you want to debug. After that, you can use the `pdb` [debugger commands](https://docs.python.org/3/library/pdb.html#debugger-commands)
 to move through your running program stepwise. It’s common to set a breakpoint (`b LINE-NUMBER`) when you start `pdb`, then call `c` to run the program until that point. This prevents you from having to step through each line of execution (using `s` or `n`) to get to the part of the code you want to examine. Alternatively, you can write `import pdb; pdb.set_trace()` before the line you want to break at. If you add `pdb.set_trace()`, your program will automatically start in debug mode when you run it. (In other words, you can just type `python FILENAME.py` into the command line instead of `python -m pdb FILENAME.py`.) Once you’re running your file in debug mode, you can step through the code and examine your program’s internal state using certain commands. There are many excellent tutorials on `pdb` online, including RealPython’s [“Python Debugging With Pdb”](https://realpython.com/python-debugging-pdb/)
.

IDEs like PyCharm or VSCode usually have a debugger built in. In your IDE, you can choose to either a) use `pdb` by pulling up a terminal window in your IDE (e.g. View → Terminal in VSCode), or b) use the built-in debugger (usually a graphical wrapper around `pdb`).

Limitations of Symbolic Tracing[#](https://docs.pytorch.org/docs/2.15/fx.html#limitations-of-symbolic-tracing "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

FX uses a system of **symbolic tracing** (a.k.a [symbolic execution](https://en.wikipedia.org/wiki/Symbolic_execution)
) to capture the semantics of programs in a transformable/analyzable form. The system is **tracing** in that it executes the program (really a [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
 or function) to record operations. It is **symbolic** in that the data flowing through the program during this execution is not real data, but rather symbols ([`Proxy`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "torch.fx.Proxy")
 in FX parlance).

Although symbolic tracing works for most neural net code, it has some limitations.

### Dynamic Control Flow[#](https://docs.pytorch.org/docs/2.15/fx.html#dynamic-control-flow "Link to this heading")

The main limitation of symbolic tracing is it does not currently support _dynamic control flow_. That is, loops or `if` statements where the condition may depend on the input values of the program.

For example, let’s examine the following program:

def func\_to\_trace(x):
    if x.sum() \> 0:
        return torch.relu(x)
    else:

        return torch.neg(x)

traced \= torch.fx.symbolic\_trace(func\_to\_trace)
"""
    <...>
    File "dyn.py", line 6, in func\_to\_trace
    if x.sum() > 0:
    File "pytorch/torch/fx/proxy.py", line 155, in \_\_bool\_\_
    return self.tracer.to\_bool(self)
    File "pytorch/torch/fx/proxy.py", line 85, in to\_bool
    raise TraceError('symbolically traced variables cannot be used as inputs to control flow')
torch.fx.proxy.TraceError: symbolically traced variables cannot be used as inputs to control flow
"""

Copy to clipboard

The condition to the `if` statement relies on the value of `x.sum()`, which relies on the value of `x`, a function input. Since `x` can change (i.e. if you pass a new input tensor to the traced function), this is _dynamic control flow_. The traceback walks back up through your code to show you where this situation happens.

### Static Control Flow[#](https://docs.pytorch.org/docs/2.15/fx.html#static-control-flow "Link to this heading")

On the other hand, so-called _static control flow_ is supported. Static control flow is loops or `if` statements whose value cannot change across invocations. Typically, in PyTorch programs, this control flow arises for code making decisions about a model’s architecture based on hyper-parameters. As a concrete example:

import torch
import torch.fx

class MyModule(torch.nn.Module):
    def \_\_init\_\_(self, do\_activation : bool \= False):
        super().\_\_init\_\_()
        self.do\_activation \= do\_activation
        self.linear \= torch.nn.Linear(512, 512)

    def forward(self, x):
        x \= self.linear(x)
        \# This if-statement is so-called static control flow.
        \# Its condition does not depend on any input values
        if self.do\_activation:
            x \= torch.relu(x)
        return x

without\_activation \= MyModule(do\_activation\=False)
with\_activation \= MyModule(do\_activation\=True)

traced\_without\_activation \= torch.fx.symbolic\_trace(without\_activation)
print(traced\_without\_activation.code)
"""
def forward(self, x):
    linear\_1 = self.linear(x);  x = None
    return linear\_1
"""

traced\_with\_activation \= torch.fx.symbolic\_trace(with\_activation)
print(traced\_with\_activation.code)
"""
import torch
def forward(self, x):
    linear\_1 = self.linear(x);  x = None
    relu\_1 = torch.relu(linear\_1);  linear\_1 = None
    return relu\_1
"""

Copy to clipboard

The if-statement `if self.do_activation` does not depend on any function inputs, thus it is static. `do_activation` can be considered to be a hyper-parameter, and the traces of different instances of `MyModule` with different values for that parameter have different code. This is a valid pattern that is supported by symbolic tracing.

Many instances of dynamic control flow are semantically static control flow. These instances can be made to support symbolic tracing by removing the data dependencies on input values, for example by moving values to `Module` attributes or by binding concrete values to arguments during symbolic tracing:

def f(x, flag):
    if flag: return x
    else: return x\*2

fx.symbolic\_trace(f) \# Fails!

fx.symbolic\_trace(f, concrete\_args\={'flag': True})

Copy to clipboard

In the case of truly dynamic control flow, the sections of the program that contain this code can be traced as calls to the Method (see [Customizing Tracing with the Tracer class](https://docs.pytorch.org/docs/2.15/fx.html#customizing-tracing)
) or function (see [`wrap()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.wrap "torch.fx.wrap")
) rather than tracing through them.

### Non- `torch` Functions[#](https://docs.pytorch.org/docs/2.15/fx.html#non-torch-functions "Link to this heading")

FX uses `__torch_function__` as the mechanism by which it intercepts calls (see the [technical overview](https://github.com/pytorch/pytorch/blob/main/torch/fx/README.md#technical-details)
 for more information about this). Some functions, such as builtin Python functions or those in the `math` module, are not covered by `__torch_function__`, but we would still like to capture them in symbolic tracing. For example:

import torch
import torch.fx
from math import sqrt

def normalize(x):
    """
    Normalize \`x\` by the size of the batch dimension
    """
    return x / sqrt(len(x))

\# It's valid Python code
normalize(torch.rand(3, 4))

traced \= torch.fx.symbolic\_trace(normalize)
"""
    <...>
    File "sqrt.py", line 9, in normalize
    return x / sqrt(len(x))
    File "pytorch/torch/fx/proxy.py", line 161, in \_\_len\_\_
    raise RuntimeError("'len' is not supported in symbolic tracing by default. If you want "
RuntimeError: 'len' is not supported in symbolic tracing by default. If you want this call to be recorded, please call torch.fx.wrap('len') at module scope
"""

Copy to clipboard

The error tells us that the built-in function `len` is not supported. We can make it so that functions like this are recorded in the trace as direct calls using the [`wrap()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.wrap "torch.fx.wrap")
 API:

torch.fx.wrap('len')
torch.fx.wrap('sqrt')

traced \= torch.fx.symbolic\_trace(normalize)

print(traced.code)
"""
import math
def forward(self, x):
    len\_1 = len(x)
    sqrt\_1 = math.sqrt(len\_1);  len\_1 = None
    truediv = x / sqrt\_1;  x = sqrt\_1 = None
    return truediv
"""

Copy to clipboard

### Customizing Tracing with the `Tracer` class[#](https://docs.pytorch.org/docs/2.15/fx.html#customizing-tracing-with-the-tracer-class "Link to this heading")

The [`Tracer`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer "torch.fx.Tracer")
 class is the class that underlies the implementation of `symbolic_trace`. The behavior of tracing can be customized by subclassing Tracer, like so:

class MyCustomTracer(torch.fx.Tracer):
    \# Inside here you can override various methods
    \# to customize tracing. See the \`Tracer\` API
    \# reference
    pass

\# Let's use this custom tracer to trace through this module
class MyModule(torch.nn.Module):
    def forward(self, x):
        return torch.relu(x) + torch.ones(3, 4)

mod \= MyModule()

traced\_graph \= MyCustomTracer().trace(mod)
\# trace() returns a Graph. Let's wrap it up in a
\# GraphModule to make it runnable
traced \= torch.fx.GraphModule(mod, traced\_graph)

Copy to clipboard

Leaf Modules[#](https://docs.pytorch.org/docs/2.15/fx.html#leaf-modules "Link to this heading")

------------------------------------------------------------------------------------------------

Leaf Modules are the modules that appear as calls in the symbolic trace rather than being traced through. The default set of leaf modules is the set of standard `torch.nn` module instances. For example:

class MySpecialSubmodule(torch.nn.Module):
    def forward(self, x):
        return torch.neg(x)

class MyModule(torch.nn.Module):
    def \_\_init\_\_(self):
        super().\_\_init\_\_()
        self.linear \= torch.nn.Linear(3, 4)
        self.submod \= MySpecialSubmodule()

    def forward(self, x):
        return self.submod(self.linear(x))

traced \= torch.fx.symbolic\_trace(MyModule())
print(traced.code)
\# \`linear\` is preserved as a call, yet \`submod\` is traced though.
\# This is because the default set of "Leaf Modules" includes all
\# standard \`torch.nn\` modules.
"""
import torch
def forward(self, x):
    linear\_1 = self.linear(x);  x = None
    neg\_1 = torch.neg(linear\_1);  linear\_1 = None
    return neg\_1
"""

Copy to clipboard

The set of leaf modules can be customized by overriding [`Tracer.is_leaf_module()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer.is_leaf_module "torch.fx.Tracer.is_leaf_module")
.

### Miscellanea[#](https://docs.pytorch.org/docs/2.15/fx.html#miscellanea "Link to this heading")

*   Tensor constructors (e.g. `torch.zeros`, `torch.ones`, `torch.rand`, `torch.randn`, `torch.sparse_coo_tensor`) are currently not traceable.
    
    *   The deterministic constructors (`zeros`, `ones`) can be used and the value they produce will be embedded in the trace as a constant. This is only problematic if the arguments to these constructors refers to dynamic input sizes. In this case, `ones_like` or `zeros_like` may be a viable substitute.
        
    *   Nondeterministic constructors (`rand`, `randn`) will have a single random value embedded in the trace. This is likely not the intended behavior. One workaround is to wrap `torch.randn` in a `torch.fx.wrap` function and call that instead.
        
    
    @torch.fx.wrap
    def torch\_randn(x, shape):
        return torch.randn(shape)
    
    def f(x):
        return x + torch\_randn(x, 5)
    fx.symbolic\_trace(f)
    
    Copy to clipboard
    
    *   This behavior may be fixed in a future release.
        
*   Type annotations
    
    *   Python 3-style type annotations (e.g. `func(x : torch.Tensor, y : int) -> torch.Tensor`) are supported and will be preserved by symbolic tracing.
        
    *   Python 2-style comment type annotations `# type: (torch.Tensor, int) -> torch.Tensor` are not currently supported.
        
    *   Annotations on local names within a function are not currently supported.
        
*   Gotcha around `training` flag and submodules
    
    *   When using functionals like `torch.nn.functional.dropout`, it will be common for the training argument to be passed in as `self.training`. During FX tracing, this will likely be baked in as a constant value.
        
    
    import torch
    import torch.fx
    
    class DropoutRepro(torch.nn.Module):
        def forward(self, x):
        return torch.nn.functional.dropout(x, training\=self.training)
    
    traced \= torch.fx.symbolic\_trace(DropoutRepro())
    print(traced.code)
    """
    def forward(self, x):
        dropout = torch.nn.functional.dropout(x, p = 0.5, training = True, inplace = False);  x = None
        return dropout
    """
    
    traced.eval()
    
    x \= torch.randn(5, 3)
    torch.testing.assert\_close(traced(x), x)
    """
    AssertionError: Tensor-likes are not close!
    
    Mismatched elements: 15 / 15 (100.0%)
    Greatest absolute difference: 1.6207983493804932 at index (0, 2) (up to 1e-05 allowed)
    Greatest relative difference: 1.0 at index (0, 0) (up to 0.0001 allowed)
    """
    
    Copy to clipboard
    
    *   However, when the standard `nn.Dropout()` submodule is used, the training flag is encapsulated and–because of the preservation of the `nn.Module` object model–can be changed.
        
    
    class DropoutRepro2(torch.nn.Module):
        def \_\_init\_\_(self):
        super().\_\_init\_\_()
        self.drop \= torch.nn.Dropout()
    
        def forward(self, x):
        return self.drop(x)
    
    traced \= torch.fx.symbolic\_trace(DropoutRepro2())
    print(traced.code)
    """
    def forward(self, x):
        drop = self.drop(x);  x = None
        return drop
    """
    
    traced.eval()
    
    x \= torch.randn(5, 3)
    torch.testing.assert\_close(traced(x), x)
    
    Copy to clipboard
    
*   Because of this difference, consider marking modules that interact with the `training` flag dynamically as leaf modules.
    

API Reference[#](https://docs.pytorch.org/docs/2.15/fx.html#api-reference "Link to this heading")

--------------------------------------------------------------------------------------------------

torch.fx.symbolic\_trace(_root_, _concrete\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/_symbolic_trace.py#L1398)
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.symbolic_trace "Link to this definition")

Symbolic tracing API

Given an `nn.Module` or function instance `root`, this function will return a `GraphModule` constructed by recording operations seen while tracing through `root`.

`concrete_args` allows you to partially specialize your function, whether it’s to remove control flow or data structures.

For example:

def f(a, b):
    if b \== True:
        return a
    else:
        return a \* 2

Copy to clipboard

FX can typically not trace through this due to the presence of control flow. However, we can use concrete\_args to specialize on the value of b to trace through this:

f \= fx.symbolic\_trace(f, concrete\_args\={"b": False})
assert f(3, False) \== 6

Copy to clipboard

Note that although you can still pass in different values of b, they will be ignored.

We can also use concrete\_args to eliminate data-structure handling from our function. This will use pytrees to flatten your input. To avoid overspecializing, pass in fx.PH for values that shouldn’t be specialized. For example:

def f(x):
    out \= 0
    for v in x.values():
        out += v
    return out

f \= fx.symbolic\_trace(
    f, concrete\_args\={"x": {"a": fx.PH, "b": fx.PH, "c": fx.PH}}
)
assert f({"a": 1, "b": 2, "c": 4}) \== 7

Copy to clipboard

Parameters:

*   **root** (_Union__\[_[_torch.nn.Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")\
    _,_ _Callable__\]_) – Module or function to be traced and converted into a Graph representation.
    
*   **concrete\_args** (_Optional__\[__Dict__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _any__\]__\]_) – Inputs to be partially specialized
    

Returns:

a Module created from the recorded operations from `root`.

Return type:

[GraphModule](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.GraphModule")

Note

Backwards-compatibility for this API is guaranteed.

torch.fx.wrap(_fn\_or\_name: \_F_) → \_F[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/_symbolic_trace.py#L1320)
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.wrap "Link to this definition")

torch.fx.wrap(_fn\_or\_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_) → [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

This function can be called at module-level scope to register fn\_or\_name as a “leaf function”. A “leaf function” will be preserved as a CallFunction node in the FX trace instead of being traced through:

\# foo/bar/baz.py
def my\_custom\_function(x, y):
    return x \* x + y \* y

torch.fx.wrap("my\_custom\_function")

def fn\_to\_be\_traced(x, y):
    \# When symbolic tracing, the below call to my\_custom\_function will be inserted into
    \# the graph rather than tracing it.
    return my\_custom\_function(x, y)

Copy to clipboard

This function can also equivalently be used as a decorator:

\# foo/bar/baz.py
@torch.fx.wrap
def my\_custom\_function(x, y):
    return x \* x + y \* y

Copy to clipboard

A wrapped function can be thought of a “leaf function”, analogous to the concept of “leaf modules”, that is, they are functions that are left as calls in the FX trace rather than traced through.

Parameters:

**fn\_or\_name** (_Union__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_,_ _Callable__\]_) – The function or name of the global function to insert into the graph when it’s called

Note

Backwards-compatibility for this API is guaranteed.

_class_ torch.fx.GraphModule(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph_module.py#L518)
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "Link to this definition")

GraphModule is an nn.Module generated from an fx.Graph. Graphmodule has a `graph` attribute, as well as `code` and `forward` attributes generated from that `graph`.

Warning

When `graph` is reassigned, `code` and `forward` will be automatically regenerated. However, if you edit the contents of the `graph` without reassigning the `graph` attribute itself, you must call `recompile()` to update the generated code.

Note

Backwards-compatibility for this API is guaranteed.

Return type:

Self

\_\_init\_\_(_root_, _graph_, _class\_name\='GraphModule'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph_module.py#L552)
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule.__init__ "Link to this definition")

Construct a GraphModule.

Parameters:

*   **root** (_Union__\[_[_torch.nn.Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")\
    _,_ _Dict__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Any__\]_) – `root` can either be an nn.Module instance or a Dict mapping strings to any attribute type. In the case that `root` is a Module, any references to Module-based objects (via qualified name) in the Graph’s Nodes’ `target` field will be copied over from the respective place within `root`’s Module hierarchy into the GraphModule’s module hierarchy. In the case that `root` is a dict, the qualified name found in a Node’s `target` will be looked up directly in the dict’s keys. The object mapped to by the Dict will be copied over into the appropriate place within the GraphModule’s module hierarchy.\
    \
*   **graph** ([_Graph_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")\
    ) – `graph` contains the nodes this GraphModule should use for code generation\
    \
*   **class\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – `name` denotes the name of this GraphModule for debugging purposes. If it’s unset, all error messages will report as originating from `GraphModule`. It may be helpful to set this to `root`’s original name or a name that makes sense within the context of your transform.\
    \
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
add\_submodule(_target_, _m_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph_module.py#L775)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule.add_submodule "Link to this definition")\
\
Adds the given submodule to `self`.\
\
This installs empty Modules where none exist yet if they are subpaths of `target`.\
\
Parameters:\
\
*   **target** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The fully-qualified string name of the new submodule (See example in `nn.Module.get_submodule` for how to specify a fully-qualified string.)\
    \
*   **m** ([_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.modules.module.Module")\
    ) – The submodule itself; the actual object we want to install in the current Module\
    \
\
Returns:\
\
Whether or not the submodule could be inserted. For\
\
this method to return True, each object in the chain denoted by `target` must either a) not exist yet, or b) reference an `nn.Module` (not a parameter or other attribute)\
\
Return type:\
\
[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
_property_ code_: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule.code "Link to this definition")\
\
Return the Python code generated from the `Graph` underlying this `GraphModule`.\
\
delete\_all\_unused\_submodules()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph_module.py#L857)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule.delete_all_unused_submodules "Link to this definition")\
\
Deletes all unused submodules from `self`.\
\
A Module is considered “used” if any one of the following is true: 1. It has children that are used 2. Its forward is called directly via a `call_module` node 3. It has a non-Module attribute that is used from a `get_attr` node\
\
This method can be called to clean up an `nn.Module` without manually calling `delete_submodule` on each unused submodule.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
delete\_submodule(_target_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph_module.py#L815)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule.delete_submodule "Link to this definition")\
\
Deletes the given submodule from `self`.\
\
The module will not be deleted if `target` is not a valid target.\
\
Parameters:\
\
**target** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
) – The fully-qualified string name of the new submodule (See example in `nn.Module.get_submodule` for how to specify a fully-qualified string.)\
\
Returns:\
\
Whether or not the target string referenced a\
\
submodule we want to delete. A return value of `False` means that the `target` was not a valid reference to a submodule.\
\
Return type:\
\
[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
_property_ graph_: [Graph](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.graph.Graph")\
_[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule.graph "Link to this definition")\
\
Return the `Graph` underlying this `GraphModule`\
\
print\_readable(_print\_output\=True_, _include\_stride\=False_, _include\_device\=False_, _colored\=False_, _\*_, _fast\_sympy\_print\=False_, _expanded\_def\=False_, _additional\_meta\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph_module.py#L1125)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule.print_readable "Link to this definition")\
\
Return the Python code generated for current GraphModule and its children GraphModules.\
\
Parameters:\
\
**additional\_meta** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
_\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_\]_ _|_ _None_) – Optional list of meta keys to include in the output. For each key in the list, if it exists in node.meta, its value will be shown in the format “key: value”. Example: print\_readable(additional\_meta=\[“seq\_nr”\]).\
\
Return type:\
\
[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
recompile()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph_module.py#L925)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule.recompile "Link to this definition")\
\
Recompile this GraphModule from its `graph` attribute. This should be called after editing the contained `graph`, otherwise the generated code of this `GraphModule` will be out of date.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
Return type:\
\
_PythonCode_\
\
to\_folder(_folder_, _module\_name\='FxModule'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph_module.py#L690)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule.to_folder "Link to this definition")\
\
Dumps out module to `folder` with `module_name` so that it can be\
\
imported with `from <folder> import <module_name>`\
\
Args:\
\
> folder (Union\[str, os.PathLike\]): The folder to write the code out to\
> \
> module\_name (str): Top-level name to use for the `Module` while\
> \
> writing out the code\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
_class_ torch.fx.Graph(_owning\_module\=None_, _tracer\_cls\=None_, _tracer\_extras\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L1398)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "Link to this definition")\
\
`Graph` is the main data structure used in the FX Intermediate Representation. It consists of a series of `Node` s, each representing callsites (or other syntactic constructs). The list of `Node` s, taken together, constitute a valid Python function.\
\
For example, the following code\
\
import torch\
import torch.fx\
\
class MyModule(torch.nn.Module):\
    def \_\_init\_\_(self):\
        super().\_\_init\_\_()\
        self.param \= torch.nn.Parameter(torch.rand(3, 4))\
        self.linear \= torch.nn.Linear(4, 5)\
\
    def forward(self, x):\
        return torch.topk(\
            torch.sum(self.linear(x + self.linear.weight).relu(), dim\=-1), 3\
        )\
\
m \= MyModule()\
gm \= torch.fx.symbolic\_trace(m)\
\
Copy to clipboard\
\
Will produce the following Graph:\
\
print(gm.graph)\
\
Copy to clipboard\
\
graph(x):\
    %linear\_weight : \[num\_users=1\] = self.linear.weight\
    %add\_1 : \[num\_users=1\] = call\_function\[target=operator.add\](args = (%x, %linear\_weight), kwargs = {})\
    %linear\_1 : \[num\_users=1\] = call\_module\[target=linear\](args = (%add\_1,), kwargs = {})\
    %relu\_1 : \[num\_users=1\] = call\_method\[target=relu\](args = (%linear\_1,), kwargs = {})\
    %sum\_1 : \[num\_users=1\] = call\_function\[target=torch.sum\](args = (%relu\_1,), kwargs = {dim: -1})\
    %topk\_1 : \[num\_users=1\] = call\_function\[target=torch.topk\](args = (%sum\_1, 3), kwargs = {})\
    return topk\_1\
\
Copy to clipboard\
\
For the semantics of operations represented in the `Graph`, please see [`Node`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
\_\_init\_\_(_owning\_module\=None_, _tracer\_cls\=None_, _tracer\_extras\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L1447)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.__init__ "Link to this definition")\
\
Construct an empty Graph.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
call\_function(_the\_function_, _args\=None_, _kwargs\=None_, _type\_expr\=None_, _name\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L1960)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.call_function "Link to this definition")\
\
Insert a `call_function` `Node` into the `Graph`. A `call_function` node represents a call to a Python callable, specified by `the_function`.\
\
Parameters:\
\
*   **the\_function** (_Callable__\[__...__,_ _Any__\]_) – The function to be called. Can be any PyTorch operator, Python function, or member of the `builtins` or `operator` namespaces.\
    \
*   **args** (_Optional__\[__Tuple__\[__Argument__,_ _...__\]__\]_) – The positional arguments to be passed to the called function.\
    \
*   **kwargs** (_Optional__\[__Dict__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Argument__\]__\]_) – The keyword arguments to be passed to the called function\
    \
*   **type\_expr** (_Optional__\[__Any__\]_) – an optional type annotation representing the Python type the output of this node will have.\
    \
*   **name** (_Optional__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_) – The name of the node. If not specified, set to None\
    \
\
Returns:\
\
The newly created and inserted `call_function` node.\
\
Return type:\
\
[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
\
Note\
\
The same insertion point and type expression rules apply for this method as [`Graph.create_node()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.create_node "torch.fx.Graph.create_node")\
.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
call\_method(_method\_name_, _args\=None_, _kwargs\=None_, _type\_expr\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L1921)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.call_method "Link to this definition")\
\
Insert a `call_method` `Node` into the `Graph`. A `call_method` node represents a call to a given method on the 0th element of `args`.\
\
Parameters:\
\
*   **method\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The name of the method to apply to the self argument. For example, if args\[0\] is a `Node` representing a `Tensor`, then to call `relu()` on that `Tensor`, pass `relu` to `method_name`.\
    \
*   **args** (_Optional__\[__Tuple__\[__Argument__,_ _...__\]__\]_) – The positional arguments to be passed to the called method. Note that this _should_ include a `self` argument.\
    \
*   **kwargs** (_Optional__\[__Dict__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Argument__\]__\]_) – The keyword arguments to be passed to the called method\
    \
*   **type\_expr** (_Optional__\[__Any__\]_) – an optional type annotation representing the Python type the output of this node will have.\
    \
\
Returns:\
\
The newly created and inserted `call_method` node.\
\
Return type:\
\
[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
\
Note\
\
The same insertion point and type expression rules apply for this method as [`Graph.create_node()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.create_node "torch.fx.Graph.create_node")\
.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
call\_module(_module\_name_, _args\=None_, _kwargs\=None_, _type\_expr\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L1868)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.call_module "Link to this definition")\
\
Insert a `call_module` `Node` into the `Graph`. A `call_module` node represents a call to the forward() function of a `Module` in the `Module` hierarchy.\
\
Parameters:\
\
*   **module\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The qualified name of the `Module` in the `Module` hierarchy to be called. For example, if the traced `Module` has a submodule named `foo`, which has a submodule named `bar`, the qualified name `foo.bar` should be passed as `module_name` to call that module.\
    \
*   **args** (_Optional__\[__Tuple__\[__Argument__,_ _...__\]__\]_) – The positional arguments to be passed to the called method. Note that this should _not_ include a `self` argument.\
    \
*   **kwargs** (_Optional__\[__Dict__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Argument__\]__\]_) – The keyword arguments to be passed to the called method\
    \
*   **type\_expr** (_Optional__\[__Any__\]_) – an optional type annotation representing the Python type the output of this node will have.\
    \
\
Returns:\
\
The newly-created and inserted `call_module` node.\
\
Return type:\
\
[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
\
Note\
\
The same insertion point and type expression rules apply for this method as [`Graph.create_node()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.create_node "torch.fx.Graph.create_node")\
.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
create\_node(_op_, _target_, _args\=None_, _kwargs\=None_, _name\=None_, _type\_expr\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L1586)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.create_node "Link to this definition")\
\
Create a `Node` and add it to the `Graph` at the current insert-point. Note that the current insert-point can be set via [`Graph.inserting_before()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.inserting_before "torch.fx.Graph.inserting_before")\
 and [`Graph.inserting_after()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.inserting_after "torch.fx.Graph.inserting_after")\
.\
\
Parameters:\
\
*   **op** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – the opcode for this Node. One of ‘call\_function’, ‘call\_method’, ‘get\_attr’, ‘call\_module’, ‘placeholder’, or ‘output’. The semantics of these opcodes are described in the `Graph` docstring.\
    \
*   **args** (_Optional__\[__Tuple__\[__Argument__,_ _...__\]__\]_) – is a tuple of arguments to this node.\
    \
*   **kwargs** (_Optional__\[__Dict__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Argument__\]__\]_) – the kwargs of this Node\
    \
*   **name** (_Optional__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_) – an optional string name for the `Node`. This will influence the name of the value assigned to in the Python generated code.\
    \
*   **type\_expr** (_Optional__\[__Any__\]_) – an optional type annotation representing the Python type the output of this node will have.\
    \
\
Returns:\
\
The newly-created and inserted node.\
\
Return type:\
\
[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
create\_size\_node(_tensor\_node_, _dim_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L2019)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.create_size_node "Link to this definition")\
\
Create an FX node for `tensor_node.size(dim)`.\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
Return type:\
\
[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
\
create\_storage\_offset\_node(_tensor\_node_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L2037)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.create_storage_offset_node "Link to this definition")\
\
Create an FX node for `tensor_node.storage_offset()`.\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
Return type:\
\
[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
\
create\_stride\_node(_tensor\_node_, _dim_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L2028)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.create_stride_node "Link to this definition")\
\
Create an FX node for `tensor_node.stride(dim)`.\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
Return type:\
\
[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
\
eliminate\_dead\_code(_is\_impure\_node\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L2691)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.eliminate_dead_code "Link to this definition")\
\
Remove all dead code from the graph, based on each node’s number of users, and whether the nodes have any side effects. The graph must be topologically sorted before calling.\
\
Parameters:\
\
*   **is\_impure\_node** (_Optional__\[__Callable__\[__\[_[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
    _\]__,_ [_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _\]__\]_) – A function that returns\
    \
*   **None** (_whether a node is impure. If this is_) –\
    \
*   **to** (_then the default behavior is_) –\
    \
*   **Node.is\_impure.** (_use_) –\
    \
\
Returns:\
\
Whether the graph was changed as a result of the pass.\
\
Return type:\
\
[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
\
Example:\
\
Before dead code is eliminated, a from a = x + 1 below has no users and thus can be eliminated from the graph without having an effect.\
\
def forward(self, x):\
    a \= x + 1\
    return x + self.attr\_1\
\
Copy to clipboard\
\
After dead code is eliminated, a = x + 1 has been removed, and the rest of forward remains.\
\
def forward(self, x):\
    return x + self.attr\_1\
\
Copy to clipboard\
\
Warning\
\
Dead code elimination has some heuristics to avoid removing side-effectful nodes (see Node.is\_impure) but in general coverage is very bad, so you should assume that this method is not sound to call unless you know that your FX graph consists entirely of functional operations or you supply your own custom function for detecting side-effectful nodes.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
erase\_node(_to\_erase_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L1676)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.erase_node "Link to this definition")\
\
Erases a `Node` from the `Graph`. Throws an exception if there are still users of that node in the `Graph`.\
\
Parameters:\
\
**to\_erase** ([_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
) – The `Node` to erase from the `Graph`.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
find\_nodes(_\*_, _op_, _target\=None_, _sort\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L1499)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.find_nodes "Link to this definition")\
\
Allows for fast query of nodes\
\
Parameters:\
\
*   **op** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – the name of the operation\
    \
*   **target** (_Optional__\[__Target__\]_) – the target of the node. For call\_function, the target is required. For other ops, the target is optional.\
    \
*   **sort** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    ) – whether to return nodes in the order they appear on on the graph.\
    \
\
Returns:\
\
Iterable of nodes with the requested op and target.\
\
Return type:\
\
[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
get\_attr(_qualified\_name_, _type\_expr\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L1800)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.get_attr "Link to this definition")\
\
Insert a `get_attr` node into the Graph. A `get_attr` `Node` represents the fetch of an attribute from the `Module` hierarchy.\
\
Parameters:\
\
*   **qualified\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – the fully-qualified name of the attribute to be retrieved. For example, if the traced Module has a submodule named `foo`, which has a submodule named `bar`, which has an attribute named `baz`, the qualified name `foo.bar.baz` should be passed as `qualified_name`.\
    \
*   **type\_expr** (_Optional__\[__Any__\]_) – an optional type annotation representing the Python type the output of this node will have.\
    \
\
Returns:\
\
The newly-created and inserted `get_attr` node.\
\
Return type:\
\
[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
\
Note\
\
The same insertion point and type expression rules apply for this method as `Graph.create_node`.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
graph\_copy(_g_, _val\_map_, _return\_output\_node\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L1526)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.graph_copy "Link to this definition")\
\
Copy all nodes from a given graph into `self`.\
\
Parameters:\
\
*   **g** ([_Graph_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")\
    ) – The source graph from which to copy Nodes.\
    \
*   **val\_map** (_Dict__\[_[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
    _,_ [_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
    _\]_) – a dictionary that will be populated with a mapping from nodes in `g` to nodes in `self`. Note that `val_map` can be passed in with values in it already to override copying of certain values.\
    \
\
Returns:\
\
The value in `self` that is now equivalent to the output value in `g`, if `g` had an `output` node. `None` otherwise.\
\
Return type:\
\
[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[Argument, …\] | [_Sequence_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[Argument\] | [_Mapping_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, Argument\] | [slice](https://docs.python.org/3/builtins/functions.html#slice "(in Python v3.15)")\
 | [range](https://docs.python.org/3/builtins/stdtypes.html#range "(in Python v3.15)")\
 | [_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [complex](https://docs.python.org/3/builtins/functions.html#complex "(in Python v3.15)")\
 | [_dtype_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
 | [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [_device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
 | [_memory\_format_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")\
 | [_layout_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
 | _OpOverload_ | [_SymInt_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
 | [_SymBool_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymBool "torch.SymBool")\
 | [_SymFloat_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "torch.SymFloat")\
 | None, …\] | [_Sequence_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[Argument, …\] | [_Sequence_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[Argument\] | [_Mapping_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, Argument\] | [slice](https://docs.python.org/3/builtins/functions.html#slice "(in Python v3.15)")\
 | [range](https://docs.python.org/3/builtins/stdtypes.html#range "(in Python v3.15)")\
 | [_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [complex](https://docs.python.org/3/builtins/functions.html#complex "(in Python v3.15)")\
 | [_dtype_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
 | [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [_device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
 | [_memory\_format_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")\
 | [_layout_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
 | _OpOverload_ | [_SymInt_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
 | [_SymBool_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymBool "torch.SymBool")\
 | [_SymFloat_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "torch.SymFloat")\
 | None\] | [_Mapping_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[Argument, …\] | [_Sequence_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[Argument\] | [_Mapping_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, Argument\] | [slice](https://docs.python.org/3/builtins/functions.html#slice "(in Python v3.15)")\
 | [range](https://docs.python.org/3/builtins/stdtypes.html#range "(in Python v3.15)")\
 | [_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [complex](https://docs.python.org/3/builtins/functions.html#complex "(in Python v3.15)")\
 | [_dtype_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
 | [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [_device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
 | [_memory\_format_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")\
 | [_layout_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
 | _OpOverload_ | [_SymInt_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
 | [_SymBool_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymBool "torch.SymBool")\
 | [_SymFloat_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "torch.SymFloat")\
 | None\] | [slice](https://docs.python.org/3/builtins/functions.html#slice "(in Python v3.15)")\
 | [range](https://docs.python.org/3/builtins/stdtypes.html#range "(in Python v3.15)")\
 | [_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [complex](https://docs.python.org/3/builtins/functions.html#complex "(in Python v3.15)")\
 | [_dtype_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
 | [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [_device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
 | [_memory\_format_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")\
 | [_layout_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
 | _OpOverload_ | [_SymInt_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
 | [_SymBool_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymBool "torch.SymBool")\
 | [_SymFloat_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "torch.SymFloat")\
 | None\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
inserting\_after(_n\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L1742)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.inserting_after "Link to this definition")\
\
Set the point at which create\_node and companion methods will insert into the graph.\
\
When used within a ‘with’ statement, this will temporarily set the insert point and then restore it when the with statement exits:\
\
with g.inserting\_after(n):\
    ...  \# inserting after node n\
...  \# insert point restored to what it was previously\
g.inserting\_after(n)  \#  set the insert point permanently\
\
Copy to clipboard\
\
Args:\
\
> n (Optional\[Node\]): The node before which to insert. If None this will insert after\
> \
> the beginning of the entire graph.\
\
Returns:\
\
A resource manager that will restore the insert point on `__exit__`.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
Return type:\
\
_\_InsertPoint_\
\
inserting\_before(_n\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L1717)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.inserting_before "Link to this definition")\
\
Set the point at which create\_node and companion methods will insert into the graph.\
\
When used within a ‘with’ statement, this will temporarily set the insert point and then restore it when the with statement exits:\
\
with g.inserting\_before(n):\
    ...  \# inserting before node n\
...  \# insert point restored to what it was previously\
g.inserting\_before(n)  \#  set the insert point permanently\
\
Copy to clipboard\
\
Args:\
\
> n (Optional\[Node\]): The node before which to insert. If None this will insert before\
> \
> the beginning of the entire graph.\
\
Returns:\
\
A resource manager that will restore the insert point on `__exit__`.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
Return type:\
\
_\_InsertPoint_\
\
lint()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L2611)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.lint "Link to this definition")\
\
Runs various checks on this Graph to make sure it is well-formed. In particular: - Checks Nodes have correct ownership (owned by this graph) - Checks Nodes appear in topological order - If this Graph has an owning GraphModule, checks that targets exist in that GraphModule\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
materialize\_symint(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L2382)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.materialize_symint "Link to this definition")\
\
Single-value convenience wrapper around [`materialize_symints()`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.materialize_symints "torch.fx.Graph.materialize_symints")\
.\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
Return type:\
\
[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\
materialize\_symints(_values_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L2111)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.materialize_symints "Link to this definition")\
\
Materialize a list of `SymInt`/`int` values as FX subgraphs rooted\
\
at existing nodes in this graph whose meta produces the referenced symbols (typically SymInt placeholders or other sym ops).\
\
consider a graph with a tensor placeholder `%x` of shape `(s32, s32)` and we want to record this stride as an FX value to pass to a later op, two ways to do it.\
\
*   `g.create_stride_node(%x, 0)` emits `%t = aten.sym_stride.int(%x, 0)`. The semantics of this op are “ask `%x` for its current stride at dim 0”. If a later pass (e.g. mkldnn channels-last conversion) mutates `%x`’s layout, re-running `FakeTensorProp` will overwrite `%t.meta["val"]` with the NEW stride. This is the right behavior when you want a _live_ query on the producer.\
    \
*   `g.materialize_symints([%x.meta["val"].stride(0)])` walks the sympy expression `s32` and emits an FX subgraph that recomputes it from the existing producer of `s32` (here the placeholder `%x` itself via `aten.sym_size.int(%x, 0)`, or a SymInt placeholder if one exists). The resulting node’s value is “what `s32` is at runtime” – which is determined by the input’s shape and is INDEPENDENT of any layout change to `%x`. This is the right behavior when you want to _freeze_ the trace-time stride into the graph.\
    \
\
Note: like other `Graph` node-creation APIs (`call_function`, `create_size_node`, etc.), nodes are emitted at the graph’s current insertion point. The default insertion point (`Graph._root.prepend`) appends new nodes to the end of the graph, which on a graph that already has an `output` node means they land _after_ `return` (orphaned). Callers typically scope this in `with graph.inserting_before(graph.output_node()):` so the new nodes land in the body.\
\
Performance: each call performs an O(graph\_size) producer-discovery scan and builds a per-call `expr_to_proxy` hash-cons cache. Prefer batching every SymInt you need to lift into a single call (or as few calls as possible) over calling it once per value – this amortises the graph scan and lets symints with shared sub-expressions get hash-consed into a single subgraph.\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
Return type:\
\
[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\]\
\
node\_copy(_node_, _arg\_transform=<function Graph.<lambda>>_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L2387)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.node_copy "Link to this definition")\
\
Copy a node from one graph into another. `arg_transform` needs to transform arguments from the graph of node to the graph of self. Example:\
\
\# Copying all the nodes in \`g\` into \`new\_graph\`\
g: torch.fx.Graph \= ...\
new\_graph \= torch.fx.graph()\
value\_remap \= {}\
for node in g.nodes:\
    value\_remap\[node\] \= new\_graph.node\_copy(node, lambda n: value\_remap\[n\])\
\
Copy to clipboard\
\
Parameters:\
\
*   **node** ([_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
    ) – The node to copy into `self`.\
    \
*   **arg\_transform** (_Callable__\[__\[_[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
    _\]__,_ _Argument__\]_) – A function that transforms `Node` arguments in node’s `args` and `kwargs` into the equivalent argument in `self`. In the simplest case, this should retrieve a value out of a table mapping Nodes in the original graph to `self`.\
    \
\
Return type:\
\
[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
_property_ nodes_: \_node\_list_[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.nodes "Link to this definition")\
\
Get the list of Nodes that constitute this Graph.\
\
Note that this `Node` list representation is a doubly-linked list. Mutations during iteration (e.g. delete a Node, add a Node) are safe.\
\
Returns:\
\
A doubly-linked list of Nodes. Note that `reversed` can be called on this list to switch iteration order.\
\
on\_generate\_code(_make\_transformer_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L2784)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.on_generate_code "Link to this definition")\
\
Register a transformer function when python code is generated\
\
> Args:\
> \
> make\_transformer (Callable\[\[Optional\[TransformCodeFunc\]\], TransformCodeFunc\]):\
> \
> a function that returns a code transformer to be registered. This function is called by on\_generate\_code to obtain the code transformer.\
> \
> This function is also given as its input the currently registered code transformer (or None if nothing is registered), in case it is not desirable to overwrite it. This is useful to chain code transformers together.\
> \
> Returns:\
> \
> a context manager that when used in a with statement, to automatically restore the previously registered code transformer.\
> \
> Example:\
> \
> gm: fx.GraphModule \= ...\
> \
> \# This is a code transformer we want to register. This code\
> \# transformer prepends a pdb import and trace statement at the very\
> \# beginning of the generated torch.fx code to allow for manual\
> \# debugging with the PDB library.\
> def insert\_pdb(body):\
>     return \["import pdb; pdb.set\_trace()\\n", \*body\]\
> \
> \# Registers \`insert\_pdb\`, and overwrites the current registered\
> \# code transformer (given by \`\_\` to the lambda):\
> gm.graph.on\_generate\_code(lambda \_: insert\_pdb)\
> \
> \# Or alternatively, registers a code transformer which first\
> \# runs \`body\` through existing registered transformer, then\
> \# through \`insert\_pdb\`:\
> gm.graph.on\_generate\_code(\
>     lambda current\_trans: (\
>         lambda body: insert\_pdb(\
>             current\_trans(body) if current\_trans else body\
>         )\
>     )\
> )\
> \
> gm.recompile()\
> gm(\*inputs)  \# drops into pdb\
> \
> Copy to clipboard\
> \
> This function can also be used as a context manager, with the benefit to automatically restores the previously registered code transformer:\
> \
> \# ... continue from previous example\
> \
> with gm.graph.on\_generate\_code(lambda \_: insert\_pdb):\
>     \# do more stuff with \`gm\`...\
>     gm.recompile()\
>     gm(\*inputs)  \# drops into pdb\
> \
> \# now previous code transformer is restored (but \`gm\`'s code with pdb\
> \# remains - that means you can run \`gm\` with pdb here too, until you\
> \# run next \`recompile()\`).\
> \
> Copy to clipboard\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
Return type:\
\
[_AbstractContextManager_](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager "(in Python v3.15)")\
\[None\]\
\
output(_result_, _type\_expr\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L2424)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.output "Link to this definition")\
\
Insert an `output` `Node` into the `Graph`. An `output` node represents a `return` statement in Python code. `result` is the value that should be returned.\
\
Parameters:\
\
*   **result** (_Argument_) – The value to be returned.\
    \
*   **type\_expr** (_Optional__\[__Any__\]_) – an optional type annotation representing the Python type the output of this node will have.\
    \
\
Note\
\
The same insertion point and type expression rules apply for this method as `Graph.create_node`.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
output\_node()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L1492)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.output_node "Link to this definition")\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
Return type:\
\
[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
\
placeholder(_name_, _type\_expr=None_, _default\_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L1767)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.placeholder "Link to this definition")\
\
Insert a `placeholder` node into the Graph. A `placeholder` represents a function input.\
\
Parameters:\
\
*   **name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – A name for the input value. This corresponds to the name of the positional argument to the function this `Graph` represents.\
    \
*   **type\_expr** (_Optional__\[__Any__\]_) – an optional type annotation representing the Python type the output of this node will have. This is needed in some cases for proper code generation (e.g. when the function is used subsequently in TorchScript compilation).\
    \
*   **default\_value** (_Any_) – The default value this function argument should take on. NOTE: to allow for None as a default value, inspect.Signature.empty should be passed as this argument to specify that the parameter does \_not\_ have a default value.\
    \
\
Return type:\
\
[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
\
Note\
\
The same insertion point and type expression rules apply for this method as `Graph.create_node`.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
print\_tabular()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L2589)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.print_tabular "Link to this definition")\
\
Prints the intermediate representation of the graph in tabular format. Note that this API requires the `tabulate` module to be installed.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
process\_inputs(_\*args_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L1665)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.process_inputs "Link to this definition")\
\
Processes args so that they can be passed to the FX graph.\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
Return type:\
\
[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\
process\_outputs(_out_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L1672)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.process_outputs "Link to this definition")\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
Return type:\
\
[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\
python\_code(_root\_module_, _\*_, _verbose\=False_, _include\_stride\=False_, _include\_device\=False_, _colored\=False_, _expanded\_def\=False_, _record\_func\=False_, _additional\_meta\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L2462)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.python_code "Link to this definition")\
\
Turn this `Graph` into valid Python code.\
\
Parameters:\
\
**root\_module** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
) – The name of the root module on which to look-up qualified name targets. This is usually ‘self’.\
\
Returns:\
\
src: the Python source code representing the object globals: a dictionary of global names in src -> the objects that they reference.\
\
Return type:\
\
A PythonCode object, consisting of two fields\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
set\_codegen(_codegen_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/graph.py#L2780)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph.set_codegen "Link to this definition")\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
_class_ torch.fx.Node(_graph_, _name_, _op_, _target_, _args_, _kwargs_, _return\_type\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/node.py#L259)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "Link to this definition")\
\
`Node` is the data structure that represents individual operations within a `Graph`. For the most part, Nodes represent callsites to various entities, such as operators, methods, and Modules (some exceptions include nodes that specify function inputs and outputs). Each `Node` has a function specified by its `op` property. The `Node` semantics for each value of `op` are as follows:\
\
*   `placeholder` represents a function input. The `name` attribute specifies the name this value will take on. `target` is similarly the name of the argument. `args` holds either: 1) nothing, or 2) a single argument denoting the default parameter of the function input. `kwargs` is don’t-care. Placeholders correspond to the function parameters (e.g. `x`) in the graph printout.\
    \
*   `get_attr` retrieves a parameter from the module hierarchy. `name` is similarly the name the result of the fetch is assigned to. `target` is the fully-qualified name of the parameter’s position in the module hierarchy. `args` and `kwargs` are don’t-care\
    \
*   `call_function` applies a free function to some values. `name` is similarly the name of the value to assign to. `target` is the function to be applied. `args` and `kwargs` represent the arguments to the function, following the Python calling convention\
    \
*   `call_module` applies a module in the module hierarchy’s `forward()` method to given arguments. `name` is as previous. `target` is the fully-qualified name of the module in the module hierarchy to call. `args` and `kwargs` represent the arguments to invoke the module on, _excluding the self argument_.\
    \
*   `call_method` calls a method on a value. `name` is as similar. `target` is the string name of the method to apply to the `self` argument. `args` and `kwargs` represent the arguments to invoke the module on, _including the self argument_\
    \
*   `output` contains the output of the traced function in its `args[0]` attribute. This corresponds to the “return” statement in the Graph printout.\
    \
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
_property_ all\_input\_nodes_: [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[Node](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
\]_[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node.all_input_nodes "Link to this definition")\
\
Return all Nodes that are inputs to this Node. This is equivalent to iterating over `args` and `kwargs` and only collecting the values that are Nodes.\
\
Returns:\
\
List of `Nodes` that appear in the `args` and `kwargs` of this `Node`, in that order.\
\
append(_x_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/node.py#L442)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node.append "Link to this definition")\
\
Insert `x` after this node in the list of nodes in the graph. Equivalent to `self.next.prepend(x)`\
\
Parameters:\
\
**x** ([_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
) – The node to put after this node. Must be a member of the same graph.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
_property_ args_: [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[Argument, ...\] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[Argument\] | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, Argument\] | [slice](https://docs.python.org/3/builtins/functions.html#slice "(in Python v3.15)")\
 | [range](https://docs.python.org/3/builtins/stdtypes.html#range "(in Python v3.15)")\
 | [Node](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [complex](https://docs.python.org/3/builtins/functions.html#complex "(in Python v3.15)")\
 | [dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
 | [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [device](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
 | [memory\_format](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")\
 | [layout](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
 | OpOverload | [SymInt](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
 | [SymBool](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymBool "torch.SymBool")\
 | [SymFloat](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "torch.SymFloat")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, ...\] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[Argument, ...\] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[Argument\] | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, Argument\] | [slice](https://docs.python.org/3/builtins/functions.html#slice "(in Python v3.15)")\
 | [range](https://docs.python.org/3/builtins/stdtypes.html#range "(in Python v3.15)")\
 | [Node](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [complex](https://docs.python.org/3/builtins/functions.html#complex "(in Python v3.15)")\
 | [dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
 | [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [device](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
 | [memory\_format](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")\
 | [layout](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
 | OpOverload | [SymInt](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
 | [SymBool](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymBool "torch.SymBool")\
 | [SymFloat](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "torch.SymFloat")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
\] | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[Argument, ...\] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[Argument\] | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, Argument\] | [slice](https://docs.python.org/3/builtins/functions.html#slice "(in Python v3.15)")\
 | [range](https://docs.python.org/3/builtins/stdtypes.html#range "(in Python v3.15)")\
 | [Node](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [complex](https://docs.python.org/3/builtins/functions.html#complex "(in Python v3.15)")\
 | [dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
 | [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [device](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
 | [memory\_format](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")\
 | [layout](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
 | OpOverload | [SymInt](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
 | [SymBool](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymBool "torch.SymBool")\
 | [SymFloat](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "torch.SymFloat")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
\] | [slice](https://docs.python.org/3/builtins/functions.html#slice "(in Python v3.15)")\
 | [range](https://docs.python.org/3/builtins/stdtypes.html#range "(in Python v3.15)")\
 | [Node](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [complex](https://docs.python.org/3/builtins/functions.html#complex "(in Python v3.15)")\
 | [dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
 | [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [device](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
 | [memory\_format](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")\
 | [layout](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
 | OpOverload | [SymInt](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
 | [SymBool](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymBool "torch.SymBool")\
 | [SymFloat](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "torch.SymFloat")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, ...\]_[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node.args "Link to this definition")\
\
The tuple of arguments to this `Node`. The interpretation of arguments depends on the node’s opcode. See the [`Node`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
 docstring for more information.\
\
Assignment to this property is allowed. All accounting of uses and users is updated automatically on assignment.\
\
format\_node(_placeholder\_names\=None_, _maybe\_return\_typename\=None_, _\*_, _include\_tensor\_metadata\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/node.py#L617)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node.format_node "Link to this definition")\
\
Return a descriptive string representation of `self`.\
\
This method can be used with no arguments as a debugging utility.\
\
This function is also used internally in the `__str__` method of `Graph`. Together, the strings in `placeholder_names` and `maybe_return_typename` make up the signature of the autogenerated `forward` function in this Graph’s surrounding GraphModule. `placeholder_names` and `maybe_return_typename` should not be used otherwise.\
\
Parameters:\
\
*   **placeholder\_names** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ _None_) – A list that will store formatted strings representing the placeholders in the generated `forward` function. Internal use only.\
    \
*   **maybe\_return\_typename** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ _None_) – A single-element list that will store a formatted string representing the output of the generated `forward` function. Internal use only.\
    \
*   **include\_tensor\_metadata** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    ) – Whether to include tensor metadata\
    \
\
Returns:\
\
If 1) we’re using `format_node` as an internal helper\
\
in the `__str__` method of `Graph`, and 2) `self` is a placeholder Node, return `None`. Otherwise, return a descriptive string representation of the current Node.\
\
Return type:\
\
[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
insert\_arg(_idx_, _arg_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/node.py#L529)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node.insert_arg "Link to this definition")\
\
Insert a positional argument to the argument list with given index.\
\
Parameters:\
\
*   **idx** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – The index of the element in `self.args` to be inserted before.\
    \
*   **arg** (_Argument_) – The new argument value to insert into `args`\
    \
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
is\_impure(_impure\_random\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/node.py#L758)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node.is_impure "Link to this definition")\
\
Returns whether this op is impure, i.e. if its op is a placeholder or output, or if a call\_function or call\_module which is impure.\
\
Parameters:\
\
**impure\_random** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
) – Whether to treat rand op as impure.\
\
Returns:\
\
If the op is impure or not.\
\
Return type:\
\
[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
_property_ kwargs_: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[Argument, ...\] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[Argument\] | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, Argument\] | [slice](https://docs.python.org/3/builtins/functions.html#slice "(in Python v3.15)")\
 | [range](https://docs.python.org/3/builtins/stdtypes.html#range "(in Python v3.15)")\
 | [Node](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [complex](https://docs.python.org/3/builtins/functions.html#complex "(in Python v3.15)")\
 | [dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
 | [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [device](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
 | [memory\_format](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")\
 | [layout](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
 | OpOverload | [SymInt](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
 | [SymBool](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymBool "torch.SymBool")\
 | [SymFloat](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "torch.SymFloat")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, ...\] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[Argument, ...\] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[Argument\] | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, Argument\] | [slice](https://docs.python.org/3/builtins/functions.html#slice "(in Python v3.15)")\
 | [range](https://docs.python.org/3/builtins/stdtypes.html#range "(in Python v3.15)")\
 | [Node](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [complex](https://docs.python.org/3/builtins/functions.html#complex "(in Python v3.15)")\
 | [dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
 | [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [device](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
 | [memory\_format](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")\
 | [layout](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
 | OpOverload | [SymInt](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
 | [SymBool](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymBool "torch.SymBool")\
 | [SymFloat](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "torch.SymFloat")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
\] | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[Argument, ...\] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[Argument\] | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, Argument\] | [slice](https://docs.python.org/3/builtins/functions.html#slice "(in Python v3.15)")\
 | [range](https://docs.python.org/3/builtins/stdtypes.html#range "(in Python v3.15)")\
 | [Node](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [complex](https://docs.python.org/3/builtins/functions.html#complex "(in Python v3.15)")\
 | [dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
 | [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [device](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
 | [memory\_format](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")\
 | [layout](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
 | OpOverload | [SymInt](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
 | [SymBool](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymBool "torch.SymBool")\
 | [SymFloat](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "torch.SymFloat")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
\] | [slice](https://docs.python.org/3/builtins/functions.html#slice "(in Python v3.15)")\
 | [range](https://docs.python.org/3/builtins/stdtypes.html#range "(in Python v3.15)")\
 | [Node](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [complex](https://docs.python.org/3/builtins/functions.html#complex "(in Python v3.15)")\
 | [dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
 | [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [device](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
 | [memory\_format](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")\
 | [layout](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
 | OpOverload | [SymInt](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
 | [SymBool](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymBool "torch.SymBool")\
 | [SymFloat](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "torch.SymFloat")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
\]_[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node.kwargs "Link to this definition")\
\
The dict of keyword arguments to this `Node`. The interpretation of arguments depends on the node’s opcode. See the [`Node`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
 docstring for more information.\
\
Assignment to this property is allowed. All accounting of uses and users is updated automatically on assignment.\
\
_property_ next_: [Node](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
_[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node.next "Link to this definition")\
\
Returns the next `Node` in the linked list of Nodes.\
\
Returns:\
\
The next `Node` in the linked list of Nodes.\
\
normalized\_arguments(_root_, _arg\_types\=None_, _kwarg\_types\=None_, _normalize\_to\_only\_use\_kwargs\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/node.py#L809)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node.normalized_arguments "Link to this definition")\
\
Returns normalized arguments to Python targets. This means that args/kwargs will be matched up to the module/functional’s signature and return exclusively kwargs in positional order if normalize\_to\_only\_use\_kwargs is true. Also populates default values. Does not support positional-only parameters or varargs parameters.\
\
Supports module calls.\
\
May require arg\_types and kwarg\_types in order to disambiguate overloads.\
\
Parameters:\
\
*   **root** ([_torch.nn.Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")\
    ) – Module upon which to resolve module targets.\
    \
*   **arg\_types** (_Optional__\[__Tuple__\[__Any__\]__\]_) – Tuple of arg types for the args\
    \
*   **kwarg\_types** (_Optional__\[__Dict__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Any__\]__\]_) – Dict of arg types for the kwargs\
    \
*   **normalize\_to\_only\_use\_kwargs** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    ) – Whether to normalize to only use kwargs.\
    \
\
Returns:\
\
Returns NamedTuple ArgsKwargsPair, or None if not successful.\
\
Return type:\
\
_ArgsKwargsPair_ | None\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
prepend(_x_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/node.py#L426)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node.prepend "Link to this definition")\
\
Insert x before this node in the list of nodes in the graph. Example:\
\
Before: p \-> self\
        bx \-> x \-> ax\
After:  p \-> x \-> self\
        bx \-> ax\
\
Copy to clipboard\
\
Parameters:\
\
**x** ([_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
) – The node to put before this node. Must be a member of the same graph.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
_property_ prev_: [Node](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
_[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node.prev "Link to this definition")\
\
Returns the previous `Node` in the linked list of Nodes.\
\
Returns:\
\
The previous `Node` in the linked list of Nodes.\
\
replace\_all\_uses\_with(_replace\_with_, _delete\_user\_cb\=None_, _\*_, _propagate\_meta\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/node.py#L711)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node.replace_all_uses_with "Link to this definition")\
\
Replace all uses of `self` in the Graph with the Node `replace_with`.\
\
Parameters:\
\
*   **replace\_with** ([_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
    ) – The node to replace all uses of `self` with.\
    \
*   **delete\_user\_cb** (_Callable_) – Callback that is called to determine whether a given user of the self node should be removed.\
    \
*   **propagate\_meta** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    ) – Whether or not to copy all properties on the .meta field of the original node onto the replacement node. For safety, this is only valid to do if the replacement node doesn’t already have an existing .meta field.\
    \
\
Returns:\
\
The list of Nodes on which this change was made.\
\
Return type:\
\
[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
\]\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
replace\_input\_with(_old\_input_, _new\_input_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/node.py#L867)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node.replace_input_with "Link to this definition")\
\
Loop through input nodes of `self`, and replace all instances of `old_input` with `new_input`.\
\
Parameters:\
\
*   **old\_input** ([_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
    ) – The old input node to be replaced.\
    \
*   **new\_input** ([_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
    ) – The new input node to replace `old_input`.\
    \
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
_property_ stack\_trace_: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
_[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node.stack_trace "Link to this definition")\
\
Return the Python stack trace that was recorded during tracing, if any. When traced with fx.Tracer, this property is usually populated by Tracer.create\_proxy. To record stack traces during tracing for debug purposes, set record\_stack\_traces = True on the Tracer instance. When traced with dynamo, this property will be populated by default by OutputGraph.create\_proxy.\
\
stack\_trace would have the innermost frame at the end of the string.\
\
update\_arg(_idx_, _arg_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/node.py#L514)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node.update_arg "Link to this definition")\
\
Update an existing positional argument to contain the new value `arg`. After calling, `self.args[idx] == arg`.\
\
Parameters:\
\
*   **idx** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – The index into `self.args` of the element to update\
    \
*   **arg** (_Argument_) – The new argument value to write into `args`\
    \
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
update\_kwarg(_key_, _arg_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/node.py#L556)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node.update_kwarg "Link to this definition")\
\
Update an existing keyword argument to contain the new value `arg`. After calling, `self.kwargs[key] == arg`.\
\
Parameters:\
\
*   **key** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The key in `self.kwargs` of the element to update\
    \
*   **arg** (_Argument_) – The new argument value to write into `kwargs`\
    \
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
_class_ torch.fx.Tracer(_autowrap\_modules\=(math,)_, _autowrap\_functions\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/_symbolic_trace.py#L281)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer "Link to this definition")\
\
> `Tracer` is the class that implements the symbolic tracing functionality of `torch.fx.symbolic_trace`. A call to `symbolic_trace(m)` is equivalent to `Tracer().trace(m)`.\
> \
> Tracer can be subclassed to override various behaviors of the tracing process. The different behaviors that can be overridden are described in the docstrings of the methods on this class.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
call\_module(_m_, _forward_, _args_, _kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/_symbolic_trace.py#L558)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer.call_module "Link to this definition")\
\
Method that specifies the behavior of this `Tracer` when it encounters a call to an `nn.Module` instance.\
\
By default, the behavior is to check if the called module is a leaf module via `is_leaf_module`. If it is, emit a `call_module` node referring to `m` in the `Graph`. Otherwise, call the `Module` normally, tracing through the operations in its `forward` function.\
\
This method can be overridden to–for example–create nested traced GraphModules, or any other behavior you would want while tracing across `Module` boundaries.\
\
Parameters:\
\
*   **m** ([_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")\
    ) – The module for which a call is being emitted\
    \
*   **forward** (_Callable_) – The forward() method of the `Module` to be invoked\
    \
*   **args** (_Tuple_) – args of the module callsite\
    \
*   **kwargs** (_Dict_) – kwargs of the module callsite\
    \
\
Returns:\
\
The return value from the Module call. In the case that a `call_module` node was emitted, this is a `Proxy` value. Otherwise, it is whatever value was returned from the `Module` invocation.\
\
Return type:\
\
[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
create\_arg(_a_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/_symbolic_trace.py#L402)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer.create_arg "Link to this definition")\
\
A method to specify the behavior of tracing when preparing values to be used as arguments to nodes in the `Graph`.\
\
By default, the behavior includes:\
\
1.  Iterate through collection types (e.g. tuple, list, dict) and recursively call `create_args` on the elements.\
    \
2.  Given a Proxy object, return a reference to the underlying IR `Node`\
    \
3.  Given a non-Proxy Tensor object, emit IR for various cases:\
    \
    > *   For a Parameter, emit a `get_attr` node referring to that Parameter\
    >     \
    > *   For a non-Parameter Tensor, store the Tensor away in a special attribute referring to that attribute.\
    >     \
    \
\
This method can be overridden to support more types.\
\
Parameters:\
\
**a** (_Any_) – The value to be emitted as an `Argument` in the `Graph`.\
\
Returns:\
\
The value `a` converted into the appropriate `Argument`\
\
Return type:\
\
Argument\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
create\_args\_for\_root(_root\_fn_, _is\_module_, _concrete\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/_symbolic_trace.py#L687)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer.create_args_for_root "Link to this definition")\
\
Create `placeholder` nodes corresponding to the signature of the `root` Module. This method introspects root’s signature and emits those nodes accordingly, also supporting `*args` and `**kwargs`.\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
Return type:\
\
[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
, [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]\]\
\
create\_node(_kind_, _target_, _args_, _kwargs_, _name\=None_, _type\_expr\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/proxy.py#L214)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer.create_node "Link to this definition")\
\
Inserts a graph node given target, args, kwargs, and name.\
\
This method can be overridden to do extra checking, validation, or modification of values used in node creation. For example, one might want to disallow in-place operations from being recorded.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
Return type:\
\
[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
\
create\_proxy(_kind_, _target_, _args_, _kwargs_, _name\=None_, _type\_expr\=None_, _proxy\_factory\_fn\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/proxy.py#L339)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer.create_proxy "Link to this definition")\
\
Create a Node from the given arguments, then return the Node wrapped in a Proxy object.\
\
If kind = ‘placeholder’, then we’re creating a Node that represents the parameter of a function. If we need to encode a default parameter, we use the `args` tuple. `args` is otherwise empty for `placeholder` Nodes.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
Return type:\
\
[_Proxy_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "torch.fx.proxy.Proxy")\
\
get\_fresh\_qualname(_prefix_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/_symbolic_trace.py#L376)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer.get_fresh_qualname "Link to this definition")\
\
Gets a fresh name for a prefix and returns it. This function ensures that it will not clash with an existing attribute on the graph.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
Return type:\
\
[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\
getattr(_attr_, _attr\_val_, _parameter\_proxy\_cache_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/_symbolic_trace.py#L618)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer.getattr "Link to this definition")\
\
Method that specifies the behavior of this `Tracer` when we call getattr on a call to an `nn.Module` instance.\
\
By default, the behavior is to return a proxy value for the attribute. It also stores the proxy value in the `parameter_proxy_cache`, so that future calls will reuse the proxy rather than creating a new one.\
\
This method can be overridden to –for example– not return proxies when querying parameters.\
\
Parameters:\
\
*   **attr** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The name of the attribute being queried\
    \
*   **attr\_val** (_Any_) – The value of the attribute\
    \
*   **parameter\_proxy\_cache** (_Dict__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Any__\]_) – A cache of attr names to proxies\
    \
\
Returns:\
\
The return value from the getattr call.\
\
Return type:\
\
[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
is\_leaf\_module(_m_, _module\_qualified\_name_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/_symbolic_trace.py#L505)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer.is_leaf_module "Link to this definition")\
\
A method to specify whether a given `nn.Module` is a “leaf” module.\
\
Leaf modules are the atomic units that appear in the IR, referenced by `call_module` calls. By default, Modules in the PyTorch standard library namespace (torch.nn) are leaf modules. All other modules are traced through and their constituent ops are recorded, unless specified otherwise via this parameter.\
\
Parameters:\
\
*   **m** ([_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")\
    ) – The module being queried about\
    \
*   **module\_qualified\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The path to root of this module. For example, if you have a module hierarchy where submodule `foo` contains submodule `bar`, which contains submodule `baz`, that module will appear with the qualified name `foo.bar.baz` here.\
    \
\
Return type:\
\
[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
iter(_obj_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/proxy.py#L496)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer.iter "Link to this definition")\
\
Called when a proxy object is being iterated over, such as\
\
when used in control flow. Normally we don’t know what to do because we don’t know the value of the proxy, but a custom tracer can attach more information to the graph node using create\_node and can choose to return an iterator.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
Return type:\
\
[_Iterator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.15)")\
\
keys(_obj_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/proxy.py#L514)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer.keys "Link to this definition")\
\
Called when a proxy object has the keys() method called.\
\
This is what happens when \*\* is called on a proxy. This should return an iterator if \*\* is supposed to work in your custom tracer.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
Return type:\
\
[_Proxy_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "torch.fx.proxy.Proxy")\
\
path\_of\_module(_mod_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/_symbolic_trace.py#L530)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer.path_of_module "Link to this definition")\
\
Helper method to find the qualified name of `mod` in the Module hierarchy of `root`. For example, if `root` has a submodule named `foo`, which has a submodule named `bar`, passing `bar` into this function will return the string “foo.bar”.\
\
Parameters:\
\
**mod** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
) – The `Module` to retrieve the qualified name for.\
\
Return type:\
\
[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
proxy(_node_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/proxy.py#L335)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer.proxy "Link to this definition")\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
Return type:\
\
[_Proxy_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "torch.fx.proxy.Proxy")\
\
to\_bool(_obj_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/proxy.py#L485)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer.to_bool "Link to this definition")\
\
Called when a proxy object is being converted to a boolean, such as\
\
when used in control flow. Normally we don’t know what to do because we don’t know the value of the proxy, but a custom tracer can attach more information to the graph node using create\_node and can choose to return a value.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
Return type:\
\
[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
\
trace(_root_, _concrete\_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/_symbolic_trace.py#L798)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Tracer.trace "Link to this definition")\
\
Trace `root` and return the corresponding FX `Graph` representation. `root` can either be an `nn.Module` instance or a Python callable.\
\
Note that after this call, `self.root` may be different from the `root` passed in here. For example, when a free function is passed to `trace()`, we will create an `nn.Module` instance to use as the root and add embedded constants to.\
\
Parameters:\
\
*   **root** (_Union__\[_[_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")\
    _,_ _Callable__\]_) – Either a `Module` or a function to be traced through. Backwards-compatibility for this parameter is guaranteed.\
    \
*   **concrete\_args** (_Optional__\[__Dict__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _any__\]__\]_) – Concrete arguments that should not be treated as Proxies. This parameter is experimental and its backwards-compatibility is _NOT_ guaranteed.\
    \
\
Returns:\
\
A `Graph` representing the semantics of the passed-in `root`.\
\
Return type:\
\
[_Graph_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.graph.Graph")\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
_class_ torch.fx.Proxy(_node_, _tracer\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/proxy.py#L599)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "Link to this definition")\
\
`Proxy` objects are `Node` wrappers that flow through the program during symbolic tracing and record all the operations (`torch` function calls, method calls, operators) that they touch into the growing FX Graph.\
\
If you’re doing graph transforms, you can wrap your own `Proxy` method around a raw `Node` so that you can use the overloaded operators to add additional things to a `Graph`.\
\
`Proxy` objects cannot be iterated. In other words, the symbolic tracer will throw an error if a `Proxy` is used in a loop or as an `*args`/`**kwargs` function argument.\
\
There are two main ways around this: 1. Factor out the untraceable logic into a top-level function and use `fx.wrap` on it. 2. If the control flow is static (i.e. the loop trip count is based on some hyperparameter), the code can be kept in its original position and refactored into something like:\
\
for i in range(self.some\_hyperparameter):\
    indexed\_item \= proxied\_value\[i\]\
\
Copy to clipboard\
\
For a more detailed description into the Proxy internals, check out the “Proxy” section in torch/fx/README.md\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
_class_ torch.fx.Interpreter(_module_, _garbage\_collect\_values\=True_, _graph\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L51)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Interpreter "Link to this definition")\
\
An Interpreter executes an FX graph Node-by-Node. This pattern can be useful for many things, including writing code transformations as well as analysis passes.\
\
Methods in the Interpreter class can be overridden to customize the behavior of execution. The map of overridable methods in terms of call hierarchy:\
\
run()\
    +-- run\_node\
        +-- placeholder()\
        +-- get\_attr()\
        +-- call\_function()\
        +-- call\_method()\
        +-- call\_module()\
        +-- output()\
\
Copy to clipboard\
\
Example\
\
Suppose we want to swap all instances of `torch.neg` with `torch.sigmoid` and vice versa (including their `Tensor` method equivalents). We could subclass Interpreter like so:\
\
class NegSigmSwapInterpreter(Interpreter):\
    def call\_function(\
        self, target: Target, args: Tuple, kwargs: Dict\
    ) \-> Any:\
        if target is torch.sigmoid:\
            return torch.neg(\*args, \*\*kwargs)\
        return super().call\_function(target, args, kwargs)\
\
    def call\_method(self, target: Target, args: Tuple, kwargs: Dict) \-> Any:\
        if target \== "neg":\
            call\_self, \*args\_tail \= args\
            return call\_self.sigmoid(\*args\_tail, \*\*kwargs)\
        return super().call\_method(target, args, kwargs)\
\
def fn(x):\
    return torch.sigmoid(x).neg()\
\
gm \= torch.fx.symbolic\_trace(fn)\
input \= torch.randn(3, 4)\
result \= NegSigmSwapInterpreter(gm).run(input)\
torch.testing.assert\_close(result, torch.neg(input).sigmoid())\
\
Copy to clipboard\
\
Parameters:\
\
*   **module** ([_torch.nn.Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")\
    ) – The module to be executed\
    \
*   **garbage\_collect\_values** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    ) – Whether to delete values after their last use within the Module’s execution. This ensures optimal memory usage during execution. This can be disabled to, for example, examine all of the intermediate values in the execution by looking at the `Interpreter.env` attribute.\
    \
*   **graph** (_Optional__\[_[_Graph_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")\
    _\]_) – If passed, the interpreter will execute this graph instead of module.graph, using the provided module argument to satisfy any requests for state.\
    \
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
boxed\_run(_args\_list_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L239)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Interpreter.boxed_run "Link to this definition")\
\
Run module via interpretation and return the result. This uses the “boxed” calling convention, where you pass a list of arguments, which will be cleared by the interpreter. This ensures that input tensors are promptly deallocated.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
Return type:\
\
[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\
call\_function(_target_, _args_, _kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L356)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Interpreter.call_function "Link to this definition")\
\
Execute a `call_function` node and return the result.\
\
Parameters:\
\
*   **target** (_Target_) – The call target for this node. See [Node](https://pytorch.org/docs/main/fx.html#torch.fx.Node)\
     for details on semantics\
    \
*   **args** (_Tuple_) – Tuple of positional args for this invocation\
    \
*   **kwargs** (_Dict_) – Dict of keyword arguments for this invocation\
    \
\
Return type:\
\
[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\
Return\
\
Any: The value returned by the function invocation\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
call\_method(_target_, _args_, _kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L379)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Interpreter.call_method "Link to this definition")\
\
Execute a `call_method` node and return the result.\
\
Parameters:\
\
*   **target** (_Target_) – The call target for this node. See [Node](https://pytorch.org/docs/main/fx.html#torch.fx.Node)\
     for details on semantics\
    \
*   **args** (_Tuple_) – Tuple of positional args for this invocation\
    \
*   **kwargs** (_Dict_) – Dict of keyword arguments for this invocation\
    \
\
Return type:\
\
[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\
Return\
\
Any: The value returned by the method invocation\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
call\_module(_target_, _args_, _kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L404)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Interpreter.call_module "Link to this definition")\
\
Execute a `call_module` node and return the result.\
\
Parameters:\
\
*   **target** (_Target_) – The call target for this node. See [Node](https://pytorch.org/docs/main/fx.html#torch.fx.Node)\
     for details on semantics\
    \
*   **args** (_Tuple_) – Tuple of positional args for this invocation\
    \
*   **kwargs** (_Dict_) – Dict of keyword arguments for this invocation\
    \
\
Return type:\
\
[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\
Return\
\
Any: The value returned by the module invocation\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
fetch\_args\_kwargs\_from\_env(_n_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L472)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Interpreter.fetch_args_kwargs_from_env "Link to this definition")\
\
Fetch the concrete values of `args` and `kwargs` of node `n` from the current execution environment.\
\
Parameters:\
\
**n** ([_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
) – The node for which `args` and `kwargs` should be fetched.\
\
Returns:\
\
`args` and `kwargs` with concrete values for `n`.\
\
Return type:\
\
Tuple\[Tuple, Dict\]\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
fetch\_attr(_target_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L451)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Interpreter.fetch_attr "Link to this definition")\
\
Fetch an attribute from the `Module` hierarchy of `self.module`.\
\
Parameters:\
\
**target** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
) – The fully-qualified name of the attribute to fetch\
\
Returns:\
\
The value of the attribute.\
\
Return type:\
\
Any\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
get\_attr(_target_, _args_, _kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L334)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Interpreter.get_attr "Link to this definition")\
\
Execute a `get_attr` node. Will retrieve an attribute value from the `Module` hierarchy of `self.module`.\
\
Parameters:\
\
*   **target** (_Target_) – The call target for this node. See [Node](https://pytorch.org/docs/main/fx.html#torch.fx.Node)\
     for details on semantics\
    \
*   **args** (_Tuple_) – Tuple of positional args for this invocation\
    \
*   **kwargs** (_Dict_) – Dict of keyword arguments for this invocation\
    \
\
Returns:\
\
The value of the attribute that was retrieved\
\
Return type:\
\
Any\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
map\_nodes\_to\_values(_args_, _n_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L494)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Interpreter.map_nodes_to_values "Link to this definition")\
\
Recursively descend through `args` and look up the concrete value for each `Node` in the current execution environment.\
\
Parameters:\
\
*   **args** (_Argument_) – Data structure within which to look up concrete values\
    \
*   **n** ([_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
    ) – Node to which `args` belongs. This is only used for error reporting.\
    \
\
Return type:\
\
[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[Argument, …\] | [_Sequence_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[Argument\] | [_Mapping_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, Argument\] | [slice](https://docs.python.org/3/builtins/functions.html#slice "(in Python v3.15)")\
 | [range](https://docs.python.org/3/builtins/stdtypes.html#range "(in Python v3.15)")\
 | [_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [complex](https://docs.python.org/3/builtins/functions.html#complex "(in Python v3.15)")\
 | [_dtype_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
 | [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [_device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
 | [_memory\_format_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")\
 | [_layout_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
 | _OpOverload_ | [_SymInt_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
 | [_SymBool_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymBool "torch.SymBool")\
 | [_SymFloat_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "torch.SymFloat")\
 | None, …\] | [_Sequence_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[Argument, …\] | [_Sequence_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[Argument\] | [_Mapping_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, Argument\] | [slice](https://docs.python.org/3/builtins/functions.html#slice "(in Python v3.15)")\
 | [range](https://docs.python.org/3/builtins/stdtypes.html#range "(in Python v3.15)")\
 | [_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [complex](https://docs.python.org/3/builtins/functions.html#complex "(in Python v3.15)")\
 | [_dtype_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
 | [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [_device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
 | [_memory\_format_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")\
 | [_layout_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
 | _OpOverload_ | [_SymInt_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
 | [_SymBool_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymBool "torch.SymBool")\
 | [_SymFloat_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "torch.SymFloat")\
 | None\] | [_Mapping_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[Argument, …\] | [_Sequence_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[Argument\] | [_Mapping_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, Argument\] | [slice](https://docs.python.org/3/builtins/functions.html#slice "(in Python v3.15)")\
 | [range](https://docs.python.org/3/builtins/stdtypes.html#range "(in Python v3.15)")\
 | [_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [complex](https://docs.python.org/3/builtins/functions.html#complex "(in Python v3.15)")\
 | [_dtype_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
 | [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [_device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
 | [_memory\_format_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")\
 | [_layout_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
 | _OpOverload_ | [_SymInt_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
 | [_SymBool_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymBool "torch.SymBool")\
 | [_SymFloat_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "torch.SymFloat")\
 | None\] | [slice](https://docs.python.org/3/builtins/functions.html#slice "(in Python v3.15)")\
 | [range](https://docs.python.org/3/builtins/stdtypes.html#range "(in Python v3.15)")\
 | [_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.node.Node")\
 | [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
 | [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
 | [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [complex](https://docs.python.org/3/builtins/functions.html#complex "(in Python v3.15)")\
 | [_dtype_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
 | [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [_device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
 | [_memory\_format_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")\
 | [_layout_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
 | _OpOverload_ | [_SymInt_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
 | [_SymBool_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymBool "torch.SymBool")\
 | [_SymFloat_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymFloat "torch.SymFloat")\
 | None\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
output(_target_, _args_, _kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L430)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Interpreter.output "Link to this definition")\
\
Execute an `output` node. This really just retrieves the value referenced by the `output` node and returns it.\
\
Parameters:\
\
*   **target** (_Target_) – The call target for this node. See [Node](https://pytorch.org/docs/main/fx.html#torch.fx.Node)\
     for details on semantics\
    \
*   **args** (_Tuple_) – Tuple of positional args for this invocation\
    \
*   **kwargs** (_Dict_) – Dict of keyword arguments for this invocation\
    \
\
Returns:\
\
The return value referenced by the output node\
\
Return type:\
\
Any\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
placeholder(_target_, _args_, _kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L297)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Interpreter.placeholder "Link to this definition")\
\
Execute a `placeholder` node. Note that this is stateful: `Interpreter` maintains an internal iterator over arguments passed to `run` and this method returns next() on that iterator.\
\
Parameters:\
\
*   **target** (_Target_) – The call target for this node. See [Node](https://pytorch.org/docs/main/fx.html#torch.fx.Node)\
     for details on semantics\
    \
*   **args** (_Tuple_) – Tuple of positional args for this invocation\
    \
*   **kwargs** (_Dict_) – Dict of keyword arguments for this invocation\
    \
\
Returns:\
\
The argument value that was retrieved.\
\
Return type:\
\
Any\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
run(_\*args_, _initial\_env\=None_, _enable\_io\_processing\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L147)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Interpreter.run "Link to this definition")\
\
Run module via interpretation and return the result.\
\
Parameters:\
\
*   **\*args** ([_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    ) – The arguments to the Module to run, in positional order\
    \
*   **initial\_env** (_Optional__\[__Dict__\[_[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
    _,_ _Any__\]__\]_) – An optional starting environment for execution. This is a dict mapping Node to any value. This can be used, for example, to pre-populate results for certain Nodes so as to do only partial evaluation within the interpreter.\
    \
*   **enable\_io\_processing** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    ) – If true, we process the inputs and outputs with graph’s process\_inputs and process\_outputs function first before using them.\
    \
\
Returns:\
\
The value returned from executing the Module\
\
Return type:\
\
Any\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
run\_node(_n_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L273)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Interpreter.run_node "Link to this definition")\
\
Run a specific node `n` and return the result. Calls into placeholder, get\_attr, call\_function, call\_method, call\_module, or output depending on `node.op`\
\
Parameters:\
\
**n** ([_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
) – The Node to execute\
\
Returns:\
\
The result of executing `n`\
\
Return type:\
\
Any\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
_class_ torch.fx.Transformer(_module_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L517)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Transformer "Link to this definition")\
\
`Transformer` is a special type of interpreter that produces a new `Module`. It exposes a `transform()` method that returns the transformed `Module`. `Transformer` does not require arguments to run, as `Interpreter` does. `Transformer` works entirely symbolically.\
\
Example\
\
Suppose we want to swap all instances of `torch.neg` with `torch.sigmoid` and vice versa (including their `Tensor` method equivalents). We could subclass `Transformer` like so:\
\
class NegSigmSwapXformer(Transformer):\
    def call\_function(\
        self,\
        target: "Target",\
        args: Tuple\[Argument, ...\],\
        kwargs: Dict\[str, Any\],\
    ) \-> Any:\
        if target is torch.sigmoid:\
            return torch.neg(\*args, \*\*kwargs)\
        return super().call\_function(target, args, kwargs)\
\
    def call\_method(\
        self,\
        target: "Target",\
        args: Tuple\[Argument, ...\],\
        kwargs: Dict\[str, Any\],\
    ) \-> Any:\
        if target \== "neg":\
            call\_self, \*args\_tail \= args\
            return call\_self.sigmoid(\*args\_tail, \*\*kwargs)\
        return super().call\_method(target, args, kwargs)\
\
def fn(x):\
    return torch.sigmoid(x).neg()\
\
gm \= torch.fx.symbolic\_trace(fn)\
\
transformed: torch.nn.Module \= NegSigmSwapXformer(gm).transform()\
input \= torch.randn(3, 4)\
torch.testing.assert\_close(transformed(input), torch.neg(input).sigmoid())\
\
Copy to clipboard\
\
Parameters:\
\
**module** ([_GraphModule_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.GraphModule")\
) – The `Module` to be transformed.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
call\_function(_target_, _args_, _kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L640)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Transformer.call_function "Link to this definition")\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
Return type:\
\
[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\
call\_module(_target_, _args_, _kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L630)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Transformer.call_module "Link to this definition")\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
Return type:\
\
[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\
get\_attr(_target_, _args_, _kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L610)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Transformer.get_attr "Link to this definition")\
\
Execute a `get_attr` node. In `Transformer`, this is overridden to insert a new `get_attr` node into the output graph.\
\
Parameters:\
\
*   **target** (_Target_) – The call target for this node. See [Node](https://pytorch.org/docs/main/fx.html#torch.fx.Node)\
     for details on semantics\
    \
*   **args** (_Tuple_) – Tuple of positional args for this invocation\
    \
*   **kwargs** (_Dict_) – Dict of keyword arguments for this invocation\
    \
\
Return type:\
\
[_Proxy_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "torch.fx.proxy.Proxy")\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
placeholder(_target_, _args_, _kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L587)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Transformer.placeholder "Link to this definition")\
\
Execute a `placeholder` node. In `Transformer`, this is overridden to insert a new `placeholder` into the output graph.\
\
Parameters:\
\
*   **target** (_Target_) – The call target for this node. See [Node](https://pytorch.org/docs/main/fx.html#torch.fx.Node)\
     for details on semantics\
    \
*   **args** (_Tuple_) – Tuple of positional args for this invocation\
    \
*   **kwargs** (_Dict_) – Dict of keyword arguments for this invocation\
    \
\
Return type:\
\
[_Proxy_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Proxy "torch.fx.proxy.Proxy")\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
transform()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/interpreter.py#L647)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Transformer.transform "Link to this definition")\
\
Transform `self.module` and return the transformed `GraphModule`.\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
Return type:\
\
[_GraphModule_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.graph_module.GraphModule")\
\
torch.fx.replace\_pattern(_gm_, _pattern_, _replacement_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/subgraph_rewriter.py#L95)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.replace_pattern "Link to this definition")\
\
Matches all possible non-overlapping sets of operators and their data dependencies (`pattern`) in the Graph of a GraphModule (`gm`), then replaces each of these matched subgraphs with another subgraph (`replacement`).\
\
Parameters:\
\
*   **gm** ([_GraphModule_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.graph_module.GraphModule")\
    ) – The GraphModule that wraps the Graph to operate on\
    \
*   **pattern** ([_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")\
    _\[__\[__...__\]__,_ [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _\]_ _|_ [_GraphModule_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.graph_module.GraphModule")\
    ) – The subgraph to match in `gm` for replacement\
    \
*   **replacement** ([_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")\
    _\[__\[__...__\]__,_ [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _\]_ _|_ [_GraphModule_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.graph_module.GraphModule")\
    ) – The subgraph to replace `pattern` with\
    \
\
Returns:\
\
A list of `Match` objects representing the places in the original graph that `pattern` was matched to. The list is empty if there are no matches. `Match` is defined as:\
\
class Match(NamedTuple):\
    \# Node from which the match was found\
    anchor: Node\
    \# Maps nodes in the pattern subgraph to nodes in the larger graph\
    nodes\_map: Dict\[Node, Node\]\
\
Copy to clipboard\
\
Return type:\
\
List\[Match\]\
\
Examples:\
\
import torch\
from torch.fx import symbolic\_trace, subgraph\_rewriter\
\
class M(torch.nn.Module):\
    def \_\_init\_\_(self) \-> None:\
        super().\_\_init\_\_()\
\
    def forward(self, x, w1, w2):\
        m1 \= torch.cat(\[w1, w2\]).sum()\
        m2 \= torch.cat(\[w1, w2\]).sum()\
        return x + torch.max(m1) + torch.max(m2)\
\
def pattern(w1, w2):\
    return torch.cat(\[w1, w2\])\
\
def replacement(w1, w2):\
    return torch.stack(\[w1, w2\])\
\
traced\_module \= symbolic\_trace(M())\
\
subgraph\_rewriter.replace\_pattern(traced\_module, pattern, replacement)\
\
Copy to clipboard\
\
The above code will first match `pattern` in the `forward` method of `traced_module`. Pattern-matching is done based on use-def relationships, not node names. For example, if you had `p = torch.cat([a, b])` in `pattern`, you could match `m = torch.cat([a, b])` in the original `forward` function, despite the variable names being different (`p` vs `m`).\
\
The `return` statement in `pattern` is matched based on its value only; it may or may not match to the `return` statement in the larger graph. In other words, the pattern doesn’t have to extend to the end of the larger graph.\
\
When the pattern is matched, it will be removed from the larger function and replaced by `replacement`. If there are multiple matches for `pattern` in the larger function, each non-overlapping match will be replaced. In the case of a match overlap, the first found match in the set of overlapping matches will be replaced. (“First” here being defined as the first in a topological ordering of the Nodes’ use-def relationships. In most cases, the first Node is the parameter that appears directly after `self`, while the last Node is whatever the function returns.)\
\
One important thing to note is that the parameters of the `pattern` Callable must be used in the Callable itself, and the parameters of the `replacement` Callable must match the pattern. The first rule is why, in the above code block, the `forward` function has parameters `x, w1, w2`, but the `pattern` function only has parameters `w1, w2`. `pattern` doesn’t use `x`, so it shouldn’t specify `x` as a parameter. As an example of the second rule, consider replacing\
\
def pattern(x, y):\
    return torch.neg(x) + torch.relu(y)\
\
Copy to clipboard\
\
with\
\
def replacement(x, y):\
    return torch.relu(x)\
\
Copy to clipboard\
\
In this case, `replacement` needs the same number of parameters as `pattern` (both `x` and `y`), even though the parameter `y` isn’t used in `replacement`.\
\
After calling `subgraph_rewriter.replace_pattern`, the generated Python code looks like this:\
\
def forward(self, x, w1, w2):\
    stack\_1 \= torch.stack(\[w1, w2\])\
    sum\_1 \= stack\_1.sum()\
    stack\_2 \= torch.stack(\[w1, w2\])\
    sum\_2 \= stack\_2.sum()\
    max\_1 \= torch.max(sum\_1)\
    add\_1 \= x + max\_1\
    max\_2 \= torch.max(sum\_2)\
    add\_2 \= add\_1 + max\_2\
    return add\_2\
\
Copy to clipboard\
\
Note\
\
Backwards-compatibility for this API is guaranteed.\
\
torch.fx.traceback.annotate(_annotation\_dict_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/traceback.py#L309)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.traceback.annotate "Link to this definition")\
\
Temporarily adds custom annotations to the current tracing context. The fx\_node produced from this tracing context will have the custom annotations in node.metadata\[“custom”\] field.\
\
This context manager allows you to insert arbitrary metadata into the PT2 tracing system by updating the global current\_meta\[“custom”\] dictionary. The annotations are automatically reverted after the context exits.\
\
Gradient accumulation nodes will not be annotated.\
\
This is intended for advanced users who need to attach additional metadata to the fx nodes (e.g., for debugging, analysis, or external tooling) during export tracing.\
\
Note\
\
This API is **not backward compatible** and may evolve in future releases.\
\
Note\
\
This API is not compatible with fx.symbolic\_trace or jit.trace. It’s intended to be used with PT2 family of tracers, e.g. torch.export and dynamo.\
\
Parameters:\
\
**annotation\_dict** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
) – A dictionary of custom key-value pairs to inject into the FX trace metadata.\
\
Return type:\
\
[_Iterator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.15)")\
\[None\]\
\
Example\
\
After exiting the context, custom annotations are removed.\
\
\>>> with annotate({"source": "custom\_pass", "tag": 42}):\
...     pass  \# Your computation here\
\
Copy to clipboard\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
torch.fx.passes.tools\_common.stable\_topological\_sort(_gm_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/passes/tools_common.py#L346)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.passes.tools_common.stable_topological_sort "Link to this definition")\
\
Replace the graph of the given GraphModule with one that contains the same nodes as the original, but in topologically sorted order while preserving the original node order as much as possible.\
\
This function performs a stable topological sort where nodes appear in an order that: 1. Respects data dependencies (topological ordering) 2. Preserves the original node order when there are no dependency constraints\
\
The algorithm uses Kahn’s algorithm with a priority queue: nodes with all dependencies satisfied are added to a min-heap, ordered by their original position. This ensures we always process the earliest node in the original order among ready nodes.\
\
Parameters:\
\
**gm** ([_GraphModule_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.graph_module.GraphModule")\
) – The graph module to topologically sort. It is modified in-place.\
\
Returns:\
\
The graph module in-place sorted\
\
Return type:\
\
[_GraphModule_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.graph_module.GraphModule")\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
torch.fx.annotate[#](https://docs.pytorch.org/docs/2.15/fx.html#module-torch.fx.annotate "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`annotate`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.annotate.annotate.html#torch.fx.annotate.annotate "torch.fx.annotate.annotate") | Annotates a Proxy object with a given type. |\
\
torch.fx.node[#](https://docs.pytorch.org/docs/2.15/fx.html#module-torch.fx.node "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`has_side_effect`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.node.has_side_effect.html#torch.fx.node.has_side_effect "torch.fx.node.has_side_effect") | Registers a function to not be dead code eliminated by fx.graph.eliminate\_dead\_code |\
| [`map_aggregate`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.node.map_aggregate.html#torch.fx.node.map_aggregate "torch.fx.node.map_aggregate") | Apply fn recursively to each object appearing in arg. |\
| [`map_arg`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.node.map_arg.html#torch.fx.node.map_arg "torch.fx.node.map_arg") | Apply fn recursively to each Node appearing in arg. |\
\
torch.fx.operator\_schemas[#](https://docs.pytorch.org/docs/2.15/fx.html#module-torch.fx.operator_schemas "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`check_for_mutable_operation`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.operator_schemas.check_for_mutable_operation.html#torch.fx.operator_schemas.check_for_mutable_operation "torch.fx.operator_schemas.check_for_mutable_operation") |     |\
| [`create_type_hint`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.operator_schemas.create_type_hint.html#torch.fx.operator_schemas.create_type_hint "torch.fx.operator_schemas.create_type_hint") | Produces a type hint for the given argument. |\
| [`get_signature_for_torch_op`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.operator_schemas.get_signature_for_torch_op.html#torch.fx.operator_schemas.get_signature_for_torch_op "torch.fx.operator_schemas.get_signature_for_torch_op") | Given an operator on the torch namespace, return a list of inspect.Signature objects corresponding to the overloads of that op. |\
| [`normalize_function`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.operator_schemas.normalize_function.html#torch.fx.operator_schemas.normalize_function "torch.fx.operator_schemas.normalize_function") | Returns normalized arguments to PyTorch functions. |\
| [`normalize_module`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.operator_schemas.normalize_module.html#torch.fx.operator_schemas.normalize_module "torch.fx.operator_schemas.normalize_module") | Returns normalized arguments to PyTorch modules. |\
| [`type_matches`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.operator_schemas.type_matches.html#torch.fx.operator_schemas.type_matches "torch.fx.operator_schemas.type_matches") |     |\
\
torch.fx.traceback[#](https://docs.pytorch.org/docs/2.15/fx.html#module-torch.fx.traceback "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`annotate_fn`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.traceback.annotate_fn.html#torch.fx.traceback.annotate_fn "torch.fx.traceback.annotate_fn") | A decorator that wraps a function with the annotate context manager. |\
| [`get_graph_provenance_json`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.traceback.get_graph_provenance_json.html#torch.fx.traceback.get_graph_provenance_json "torch.fx.traceback.get_graph_provenance_json") | Given an fx.Graph, return a json that contains the provenance information of each node. |\
| [`NodeSource`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.traceback.NodeSource.html#torch.fx.traceback.NodeSource "torch.fx.traceback.NodeSource") | NodeSource is a data structure that contains the provenance information of a node. |\
| [`NodeSourceAction`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.traceback.NodeSourceAction.html#torch.fx.traceback.NodeSourceAction "torch.fx.traceback.NodeSourceAction") | Enum representing the action taken to produce a node in provenance tracking. |\
\
torch.fx.subgraph\_rewriter[#](https://docs.pytorch.org/docs/2.15/fx.html#torch-fx-subgraph-rewriter "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`replace_pattern`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.subgraph_rewriter.replace_pattern.html#torch.fx.subgraph_rewriter.replace_pattern "torch.fx.subgraph_rewriter.replace_pattern") | Matches all possible non-overlapping sets of operators and their data dependencies (`pattern`) in the Graph of a GraphModule (`gm`), then replaces each of these matched subgraphs with another subgraph (`replacement`). |\
| [`replace_pattern_with_filters`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.subgraph_rewriter.replace_pattern_with_filters.html#torch.fx.subgraph_rewriter.replace_pattern_with_filters "torch.fx.subgraph_rewriter.replace_pattern_with_filters") | See replace\_pattern for documentation. |\
\
torch.fx.tensor\_type[#](https://docs.pytorch.org/docs/2.15/fx.html#torch-fx-tensor-type "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`is_consistent`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.tensor_type.is_consistent.html#torch.fx.tensor_type.is_consistent "torch.fx.tensor_type.is_consistent") | A binary relation denoted by ~ that determines if t1 is consistent with t2. |\
| [`is_more_precise`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.tensor_type.is_more_precise.html#torch.fx.tensor_type.is_more_precise "torch.fx.tensor_type.is_more_precise") | A binary relation denoted by <= that determines if t1 is more precise than t2. |\
\
torch.fx.passes.backends.cudagraphs[#](https://docs.pytorch.org/docs/2.15/fx.html#torch-fx-passes-backends-cudagraphs "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`partition_cudagraphs`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.backends.cudagraphs.partition_cudagraphs.html#torch.fx.passes.backends.cudagraphs.partition_cudagraphs "torch.fx.passes.backends.cudagraphs.partition_cudagraphs") | Partition an FX graph into sub-GraphModules that can be validly run under CUDA graphs. |\
\
torch.fx.passes.graph\_manipulation[#](https://docs.pytorch.org/docs/2.15/fx.html#torch-fx-passes-graph-manipulation "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------\
\
torch.fx.passes.graph\_manipulation.get\_size\_of\_all\_nodes(_fx\_module_, _args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/passes/graph_manipulation.py#L56)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.passes.graph_manipulation.get_size_of_all_nodes "Link to this definition")\
\
Given a fx graph module, update each node with its total size (weights + bias + output)\
\
and its output\_size(output). For a non-module node, the total size is the output size. return total size\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
torch.fx.passes.graph\_manipulation.get\_size\_of\_node(_fx\_module_, _node_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/passes/graph_manipulation.py#L87)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.passes.graph_manipulation.get_size_of_node "Link to this definition")\
\
Given a node with node.dtype and node.shape, return its total size and its output size.\
\
total\_size = weights + bias + output\_size\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
Return type:\
\
_size\_bytes_\
\
|     |     |\
| --- | --- |\
| [`replace_target_nodes_with`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.graph_manipulation.replace_target_nodes_with.html#torch.fx.passes.graph_manipulation.replace_target_nodes_with "torch.fx.passes.graph_manipulation.replace_target_nodes_with") | Modifies all nodes in fx\_module.graph.nodes which match the specified op code and target, and updates them to match the new op code and target. |\
\
torch.fx.passes.infra.pass\_manager[#](https://docs.pytorch.org/docs/2.15/fx.html#torch-fx-passes-infra-pass-manager "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`pass_result_wrapper`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.infra.pass_manager.pass_result_wrapper.html#torch.fx.passes.infra.pass_manager.pass_result_wrapper "torch.fx.passes.infra.pass_manager.pass_result_wrapper") | Wrapper for passes which currently do not return a PassResult. |\
| [`this_before_that_pass_constraint`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.infra.pass_manager.this_before_that_pass_constraint.html#torch.fx.passes.infra.pass_manager.this_before_that_pass_constraint "torch.fx.passes.infra.pass_manager.this_before_that_pass_constraint") | Defines a partial order ('depends on' function) where `this` must occur before `that`. |\
\
torch.fx.passes.operator\_support[#](https://docs.pytorch.org/docs/2.15/fx.html#torch-fx-passes-operator-support "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`any_chain`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.operator_support.any_chain.html#torch.fx.passes.operator_support.any_chain "torch.fx.passes.operator_support.any_chain") | Combines a sequence of OperatorSupportBase instances to form a single OperatorSupportBase |\
| [`chain`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.operator_support.chain.html#torch.fx.passes.operator_support.chain "torch.fx.passes.operator_support.chain") | Combines a sequence of OperatorSupportBase instances to form a single OperatorSupportBase |\
| [`create_op_support`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.operator_support.create_op_support.html#torch.fx.passes.operator_support.create_op_support "torch.fx.passes.operator_support.create_op_support") | Wraps a IsNodeSupported function into an OperatorSupportBase instance |\
\
torch.fx.passes.param\_fetch[#](https://docs.pytorch.org/docs/2.15/fx.html#module-torch.fx.passes.param_fetch "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------------------------\
\
torch.fx.passes.param\_fetch.default\_matching(_name_, _target\_version_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/passes/param_fetch.py#L18)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.passes.param_fetch.default_matching "Link to this definition")\
\
Default matching method\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
Return type:\
\
[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\
torch.fx.passes.param\_fetch.extract\_attrs\_for\_lowering(_mod_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/passes/param_fetch.py#L58)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.passes.param_fetch.extract_attrs_for_lowering "Link to this definition")\
\
If mod is in module\_fetch\_book, fetch the mod’s attributes that in the module\_fetch\_book\
\
after checking module’s version is compatible with the module\_fetch\_book.\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
Return type:\
\
[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]\
\
torch.fx.passes.param\_fetch.lift\_lowering\_attrs\_to\_nodes(_fx\_module_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/passes/param_fetch.py#L85)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.passes.param_fetch.lift_lowering_attrs_to_nodes "Link to this definition")\
\
Recursively traverse all fx\_module nodes and fetch the module’s attributes if the node is a leaf module.\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
torch.fx.passes.pass\_manager[#](https://docs.pytorch.org/docs/2.15/fx.html#torch-fx-passes-pass-manager "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`inplace_wrapper`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.pass_manager.inplace_wrapper.html#torch.fx.passes.pass_manager.inplace_wrapper "torch.fx.passes.pass_manager.inplace_wrapper") | Convenience wrapper for passes which modify an object inplace. |\
| [`log_hook`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.pass_manager.log_hook.html#torch.fx.passes.pass_manager.log_hook "torch.fx.passes.pass_manager.log_hook") | Logs callable output. |\
| [`loop_pass`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.pass_manager.loop_pass.html#torch.fx.passes.pass_manager.loop_pass "torch.fx.passes.pass_manager.loop_pass") | Convenience wrapper for passes which need to be applied multiple times. |\
| [`these_before_those_pass_constraint`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.pass_manager.these_before_those_pass_constraint.html#torch.fx.passes.pass_manager.these_before_those_pass_constraint "torch.fx.passes.pass_manager.these_before_those_pass_constraint") | Defines a partial order ('depends on' function) where `these` must occur before `those`. |\
| [`this_before_that_pass_constraint`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.pass_manager.this_before_that_pass_constraint.html#torch.fx.passes.pass_manager.this_before_that_pass_constraint "torch.fx.passes.pass_manager.this_before_that_pass_constraint") | Defines a partial order ('depends on' function) where this must occur before that. |\
\
torch.fx.passes.regional\_inductor[#](https://docs.pytorch.org/docs/2.15/fx.html#torch-fx-passes-regional-inductor "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`regional_inductor`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.regional_inductor.regional_inductor.html#torch.fx.passes.regional_inductor.regional_inductor "torch.fx.passes.regional_inductor.regional_inductor") | Scoops out inductor marked regions and compiles them with inductor. |\
\
torch.fx.passes.reinplace[#](https://docs.pytorch.org/docs/2.15/fx.html#torch-fx-passes-reinplace "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`reinplace`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.reinplace.reinplace.html#torch.fx.passes.reinplace.reinplace "torch.fx.passes.reinplace.reinplace") | Given an fx.GraphModule, modifies it to perform "reinplacing", mutating the nodes of the graph. |\
\
torch.fx.passes.split\_utils[#](https://docs.pytorch.org/docs/2.15/fx.html#torch-fx-passes-split-utils "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------\
\
torch.fx.passes.split\_utils.split\_by\_tags(_gm_, _tags_, _return\_fqn\_mapping=False_, _return\_tuple=False_, _GraphModuleCls=<class 'torch.fx.graph\_module.GraphModule'>_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/passes/split_utils.py#L76)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.passes.split_utils.split_by_tags "Link to this definition")\
\
Splits a GraphModule using tags on its graph nodes. We honor the order of tags. For example, we have tags = \[“a”, “b”, “c”\], the function will create the initial submodules in the order of “a”, “b”, “c”.\
\
To set a tag:\
\
gm.graph.nodes\[idx\].tag \= "mytag"\
\
Copy to clipboard\
\
This will result in all nodes with the same tag being extracted and placed in their own submodule. For placeholder, output and get\_attr node, the tag is ignored. placeholder and output nodes are created when needed while get\_attr nodes get copied to submodules where they are used.\
\
Given the following module def:\
\
class SimpleModule(torch.nn.Module):\
    def \_\_init\_\_(self) \-> None:\
        super().\_\_init\_\_()\
        self.linear1 \= torch.nn.Linear(...)\
        self.linear2 \= torch.nn.Linear(...)\
        self.linear3 \= torch.nn.Linear(...)\
\
    def forward(self, in1, in2):\
        r1 \= self.linear1(in1)\
        r2 \= self.linear2(in2)\
        r3 \= torch.cat(\[r1, r2\])\
        return self.linear3(r3)\
\
Copy to clipboard\
\
Marking the node corresponding to in1 with the tag sc.REQUEST\_ONLY.lower() results in the following split:\
\
ro:\
\
def forward(self, in1):\
    self \= self.root\
    linear1 \= self.linear1(in1)\
    return linear1\
\
Copy to clipboard\
\
main:\
\
def forward(self, in2, linear1):\
    self \= self.root\
    linear2 \= self.linear2(in2)\
    cat\_1 \= torch.cat(\[linear1, linear2\])\
    linear3 \= self.linear3(cat\_1)\
    return linear3\
\
Copy to clipboard\
\
main:\
\
def forward(self, in1, in2):\
    self \= self.root\
    ro\_0 \= self.ro\_0(in1)\
    main\_1 \= self.main\_1(in2, ro\_0)\
    return main\_1\
\
Copy to clipboard\
\
Returns:\
\
torch fx graph after split\
\
orig\_to\_split\_fqn\_mapping: a map between the original fqn and the fqn\
\
after split for call\_module and get\_attr.\
\
Return type:\
\
split\_gm\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
|     |     |\
| --- | --- |\
| [`setattr_recursive`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.split_utils.setattr_recursive.html#torch.fx.passes.split_utils.setattr_recursive "torch.fx.passes.split_utils.setattr_recursive") |     |\
\
torch.fx.passes.tools\_common[#](https://docs.pytorch.org/docs/2.15/fx.html#torch-fx-passes-tools-common "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------\
\
|     |     |\
| --- | --- |\
| [`is_node_output_tensor`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.tools_common.is_node_output_tensor.html#torch.fx.passes.tools_common.is_node_output_tensor "torch.fx.passes.tools_common.is_node_output_tensor") | Checks if the node output produces a Tensor or not. |\
\
torch.fx.passes.utils.common[#](https://docs.pytorch.org/docs/2.15/fx.html#torch-fx-passes-utils-common "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------------------\
\
torch.fx.passes.utils.common.lift\_subgraph\_as\_module(_gm_, _subgraph_, _comp\_name\=''_, _class\_name\='GraphModule'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/passes/utils/common.py#L24)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.passes.utils.common.lift_subgraph_as_module "Link to this definition")\
\
Create a GraphModule for subgraph, which copies the necessary attributes from the original parent graph\_module.\
\
Parameters:\
\
*   **gm** ([_GraphModule_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.GraphModule")\
    ) – parent graph module\
    \
*   **subgraph** ([`torch.fx.Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")\
    ) – a valid subgraph that contains copied nodes from the parent graph\
    \
*   **comp\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – name for the new component\
    \
*   **class\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – name for the submodule\
    \
\
Return type:\
\
[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[[_GraphModule_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.graph_module.GraphModule")\
, [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\]\]\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
|     |     |\
| --- | --- |\
| [`compare_graphs`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.utils.common.compare_graphs.html#torch.fx.passes.utils.common.compare_graphs "torch.fx.passes.utils.common.compare_graphs") | Return True if two graphs are identical, i.e they |\
\
torch.fx.passes.utils.fuser\_utils[#](https://docs.pytorch.org/docs/2.15/fx.html#torch-fx-passes-utils-fuser-utils "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------\
\
torch.fx.passes.utils.fuser\_utils.fuse\_as\_graphmodule(_gm_, _nodes_, _module\_name_, _partition\_lookup\_table\=None_, _\*_, _always\_return\_tuple\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/passes/utils/fuser_utils.py#L97)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.passes.utils.fuser_utils.fuse_as_graphmodule "Link to this definition")\
\
Fuse nodes in graph\_module into a GraphModule.\
\
Parameters:\
\
*   **gm** ([_GraphModule_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.GraphModule")\
    ) – target graph\_module\
    \
*   **nodes** (_List__\[_[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
    _\]_) – list of nodes in gm to fuse, where the node must be topologically sorted\
    \
*   **module\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – class name for the fused GraphModule\
    \
*   **partition\_lookup\_table** (_Optional__\[__Dict__\[_[_Node_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Node "torch.fx.Node")\
    _,_ _None__\]__\]_) – optional dict of nodes to speed up lookup\
    \
*   **always\_return\_tuple** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    ) – whether to always return a tuple, even if there is only one output\
    \
\
Returns:\
\
fused graph module, where its node is a copy of nodes in gm\
\
original\_inputs (Tuple\[Node, …\]): input nodes to nodes in original gm\
\
original\_outputs (Tuple\[Node, …\]): consumer nodes of nodes in original gm\
\
Return type:\
\
fused\_gm ([GraphModule](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.GraphModule "torch.fx.GraphModule")\
)\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
|     |     |\
| --- | --- |\
| [`erase_nodes`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.utils.fuser_utils.erase_nodes.html#torch.fx.passes.utils.fuser_utils.erase_nodes "torch.fx.passes.utils.fuser_utils.erase_nodes") |     |\
| [`topo_sort`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.utils.fuser_utils.topo_sort.html#torch.fx.passes.utils.fuser_utils.topo_sort "torch.fx.passes.utils.fuser_utils.topo_sort") |     |\
| [`validate_partition`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.utils.fuser_utils.validate_partition.html#torch.fx.passes.utils.fuser_utils.validate_partition "torch.fx.passes.utils.fuser_utils.validate_partition") |     |\
\
torch.fx.passes.utils.source\_matcher\_utils[#](https://docs.pytorch.org/docs/2.15/fx.html#torch-fx-passes-utils-source-matcher-utils "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
torch.fx.passes.utils.source\_matcher\_utils.get\_source\_partitions(_graph_, _wanted\_sources_, _filter\_fn\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/passes/utils/source_matcher_utils.py#L55)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.passes.utils.source_matcher_utils.get_source_partitions "Link to this definition")\
\
Parameters:\
\
*   **graph** ([_Graph_](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.graph.Graph")\
    ) – The graph we want to partition\
    \
*   **wanted\_sources** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[_[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _\]_) – List of sources of nodes that were decomposed from this source. This can be a function (ex. torch.nn.functional.linear) or a leaf module type (ex. torch.nn.Linear).\
    \
\
Returns:\
\
Dictionary mapping sources that were given to a list of SourcePartitions that correspond to the list of nodes that were decomposed from the given source.\
\
Return type:\
\
[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
, [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[_SourcePartition_\]\]\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
|     |     |\
| --- | --- |\
| [`check_subgraphs_connected`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.utils.source_matcher_utils.check_subgraphs_connected.html#torch.fx.passes.utils.source_matcher_utils.check_subgraphs_connected "torch.fx.passes.utils.source_matcher_utils.check_subgraphs_connected") | Given two subgraphs A and B (in the form of a list of nodes), checks if A has nodes connecting to at least one node in B -- aka there exists a node in B that uses a node in A (not the other way around). |\
\
|     |     |\
| --- | --- |\
| [`get_unique_attr_name_in_module`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.experimental.const_fold.get_unique_attr_name_in_module.html#torch.fx.experimental.const_fold.get_unique_attr_name_in_module "torch.fx.experimental.const_fold.get_unique_attr_name_in_module") | Make sure the name is unique (in a module) and can represents an attr. |\
| [`split_const_subgraphs`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.experimental.const_fold.split_const_subgraphs.html#torch.fx.experimental.const_fold.split_const_subgraphs "torch.fx.experimental.const_fold.split_const_subgraphs") | Looks through module for any nodes that have all constant attribute inputs and separates them out into their own constant subgraph, and returns a FoldedGraphModule which runs that constant subgraph on the first run to set attributes on the module prior to running the non-constant portion of the graph. |\
\
|     |     |\
| --- | --- |\
| [`CodeGen`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.graph.CodeGen.html#torch.fx.graph.CodeGen "torch.fx.graph.CodeGen") |     |\
\
|     |     |\
| --- | --- |\
| [`reduce_graph_module`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.graph_module.reduce_graph_module.html#torch.fx.graph_module.reduce_graph_module "torch.fx.graph_module.reduce_graph_module") |     |\
| [`reduce_package_graph_module`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.graph_module.reduce_package_graph_module.html#torch.fx.graph_module.reduce_package_graph_module "torch.fx.graph_module.reduce_package_graph_module") |     |\
\
torch.fx.passes.annotate\_getitem\_nodes.annotate\_getitem\_nodes(_graph_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/passes/annotate_getitem_nodes.py#L7)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.passes.annotate_getitem_nodes.annotate_getitem_nodes "Link to this definition")\
\
Annotate the type of getitem nodes, inferred from the type of sequence node. If sequence node is not annotated with a type, do nothing. Currently support getitem nodes from tuple, list, and NamedTuple sequence node.\
\
This is helpful since annotations on local names within function are lost during FX transforms. Adding back known type annotation for getitem nodes to improve jit scriptability.\
\
Parameters:\
\
**graph** ([`torch.fx.Graph`](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.Graph "torch.fx.Graph")\
) – The graph to be annotated\
\
|     |     |\
| --- | --- |\
| [`GraphTransformObserver`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.graph_transform_observer.GraphTransformObserver.html#torch.fx.passes.graph_transform_observer.GraphTransformObserver "torch.fx.passes.graph_transform_observer.GraphTransformObserver") |     |\
\
|     |     |\
| --- | --- |\
| [`insert_deferred_runtime_asserts`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.runtime_assert.insert_deferred_runtime_asserts.html#torch.fx.passes.runtime_assert.insert_deferred_runtime_asserts "torch.fx.passes.runtime_assert.insert_deferred_runtime_asserts") | During tracing, we may have discovered that some data-dependent values had runtime assert on them; e.g., torch.empty(x.item()) induces a runtime that x.item() >= 0. |\
\
|     |     |\
| --- | --- |\
| [`TensorMetadata`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.shape_prop.TensorMetadata.html#torch.fx.passes.shape_prop.TensorMetadata "torch.fx.passes.shape_prop.TensorMetadata") | A structure containing pertinent information about a tensor within a PyTorch program. |\
\
torch.fx.passes.split\_utils.move\_non\_tensor\_nodes\_on\_boundary(_subgraphs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/passes/split_utils.py#L346)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.passes.split_utils.move_non_tensor_nodes_on_boundary "Link to this definition")\
\
Move non-tensor nodes on the boundary between subgraphs.\
\
For each subgraph:\
\
1.  Find nodes whose type is not tensor and any of its children is in another subgraph, put them in a queue for next step\
    \
2.  Do a BFS on those nodes in the queue, and run a DFS for each node, let’s say node X and it is in subgraph A:\
    \
    1.  if it is in to\_subgraph, return (continue DFS)\
        \
    2.  if it is in from\_subgraph, collect the nodes to nodes\_to\_move, and continue DFS\
        \
    3.  otherwise, this means it cannot be moved\
        \
    4.  also check if node X’s parent should be put into the queue. (The queue may have duplicated nodes, just process the node once)\
        \
\
Parameters:\
\
**subgraphs** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
_\[__Subgraph__\]_) – List of subgraphs containing nodes to be processed\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
torch.fx.passes.splitter\_base.generate\_inputs\_for\_submodules(_model_, _inputs_, _target\_submodules_, _deepcopy\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fx/passes/splitter_base.py#L440)\
[#](https://docs.pytorch.org/docs/2.15/fx.html#torch.fx.passes.splitter_base.generate_inputs_for_submodules "Link to this definition")\
\
Generate inputs for targeting submodules in the given model. Note that if two submodules refer to the same obj, this function doesn’t work.\
\
Parameters:\
\
*   **model** ([_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.modules.module.Module")\
    ) – root model.\
    \
*   **inputs** ([_Sequence_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
    _\[_[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _\]_) – inputs to the root model.\
    \
*   **target\_submodules** ([_Iterable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.15)")\
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_) – submodules that we want to generate inputs for.\
    \
\
Returns:\
\
A dict that maps from submodule name to its inputs.\
\
Return type:\
\
[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]\
\
Warning\
\
This API is experimental and is _NOT_ backward-compatible.\
\
|     |     |\
| --- | --- |\
| [`NodeEvent`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.splitter_base.NodeEvent.html#torch.fx.passes.splitter_base.NodeEvent "torch.fx.passes.splitter_base.NodeEvent") | An event in graph split that happened on a node. |\
| [`NodeEventTracker`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.splitter_base.NodeEventTracker.html#torch.fx.passes.splitter_base.NodeEventTracker "torch.fx.passes.splitter_base.NodeEventTracker") | Tracks node events during the splitter execution. |\
\
|     |     |\
| --- | --- |\
| [`SubgraphMatcherWithNameNodeMap`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.passes.utils.matcher_with_name_node_map_utils.SubgraphMatcherWithNameNodeMap.html#torch.fx.passes.utils.matcher_with_name_node_map_utils.SubgraphMatcherWithNameNodeMap "torch.fx.passes.utils.matcher_with_name_node_map_utils.SubgraphMatcherWithNameNodeMap") | Extends SubgraphMatcher to support querying the matched subgraph nodes through node name, |\
\
|     |     |\
| --- | --- |\
| [`GraphAppendingTracer`](https://docs.pytorch.org/docs/2.15/generated/torch.fx.proxy.GraphAppendingTracer.html#torch.fx.proxy.GraphAppendingTracer "torch.fx.proxy.GraphAppendingTracer") |     |\
\
On this page\
\
[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/fx.md)\
\
[Show Source](https://docs.pytorch.org/docs/2.15/_sources/fx.md.txt)\
\
PyTorch Libraries\
\
*   [ExecuTorch](https://docs.pytorch.org/executorch)\
    \
*   [Helion](https://docs.pytorch.org/helion)\
    \
*   [torchao](https://docs.pytorch.org/ao)\
    \
*   [kineto](https://github.com/pytorch/kineto)\
    \
*   [torchtitan](https://github.com/pytorch/torchtitan)\
    \
*   [TorchRL](https://docs.pytorch.org/rl)\
    \
*   [torchvision](https://docs.pytorch.org/vision)\
    \
*   [torchaudio](https://docs.pytorch.org/audio)\
    \
*   [tensordict](https://docs.pytorch.org/tensordict)\
    \
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)\
    \
\
Docs\
----\
\
Access comprehensive developer documentation for PyTorch\
\
[View Docs](https://docs.pytorch.org/docs/stable/index.html)\
\
Tutorials\
---------\
\
Get in-depth tutorials for beginners and advanced developers\
\
[View Tutorials](https://docs.pytorch.org/tutorials)\
\
Resources\
---------\
\
Find development resources and get your questions answered\
\
[View Resources](https://pytorch.org/resources)\
\
To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy)\
.\
\
|     |     |\
| --- | --- |\
|     |     |\
\
|     |     |\
| --- | --- |\
|     |     |