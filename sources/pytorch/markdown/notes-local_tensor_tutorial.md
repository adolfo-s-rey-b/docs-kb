Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/notes/local_tensor_tutorial.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/notes/local_tensor_tutorial.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/notes/local_tensor_tutorial.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/notes/local_tensor_tutorial.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/notes/local_tensor_tutorial.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/notes/local_tensor_tutorial.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/notes/local_tensor_tutorial.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/notes/local_tensor_tutorial.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/notes/local_tensor_tutorial.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/notes/local_tensor_tutorial.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/notes/local_tensor_tutorial.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/notes/local_tensor_tutorial.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/notes/local_tensor_tutorial.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/notes/local_tensor_tutorial.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/notes/local_tensor_tutorial.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/notes/local_tensor_tutorial.html)
[v1.13](https://docs.pytorch.org/docs/1.13/notes/local_tensor_tutorial.html)
[v1.12](https://docs.pytorch.org/docs/1.12/notes/local_tensor_tutorial.html)
[v1.11](https://docs.pytorch.org/docs/1.11/notes/local_tensor_tutorial.html)
[v1.10](https://docs.pytorch.org/docs/1.10/notes/local_tensor_tutorial.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/notes/local_tensor_tutorial.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/notes/local_tensor_tutorial.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/notes/local_tensor_tutorial.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/notes/local_tensor_tutorial.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/notes/local_tensor_tutorial.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/notes/local_tensor_tutorial.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/notes/local_tensor_tutorial.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/notes/local_tensor_tutorial.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/notes/local_tensor_tutorial.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/notes/local_tensor_tutorial.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/notes/local_tensor_tutorial.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/notes/local_tensor_tutorial.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/notes/local_tensor_tutorial.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/notes/local_tensor_tutorial.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/notes/local_tensor_tutorial.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/notes/local_tensor_tutorial.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/notes/local_tensor_tutorial.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/notes/local_tensor_tutorial.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/notes/local_tensor_tutorial.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/notes/local_tensor_tutorial.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/notes/local_tensor_tutorial.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/notes/local_tensor_tutorial.html)

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

LocalTensor Tutorial: Single-Process SPMD Debugging[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#localtensor-tutorial-single-process-spmd-debugging "Link to this heading")

======================================================================================================================================================================================================

Created On: Jan 07, 2026 | Last Updated On: May 07, 2026

This tutorial introduces `LocalTensor`, a powerful debugging tool for developing and testing distributed tensor operations without requiring multiple processes or GPUs.

[What is LocalTensor?](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#id1)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#what-is-localtensor "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`LocalTensor` is a `torch.Tensor` subclass that simulates distributed SPMD (Single Program, Multiple Data) computations on a single process. It internally maintains a mapping from rank IDs to their corresponding local tensor shards, allowing you to debug and test distributed code without infrastructure overhead.

### [Key Benefits](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#id2)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#key-benefits "Link to this heading")

1.  **No Multi-Process Setup Required**: Test distributed algorithms on a single CPU/GPU
    
2.  **Faster Debugging Cycles**: Iterate quickly without launching multiple processes
    
3.  **Full Visibility**: Inspect each rank’s tensor state directly
    
4.  **CI-Friendly**: Run distributed tests in single-process CI pipelines
    
5.  **DTensor Integration**: Seamlessly test DTensor code locally
    

Note

`LocalTensor` is intended for **debugging and testing** only, not production use. The overhead of simulating multiple ranks locally is significant.

[Installation and Setup](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#id3)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#installation-and-setup "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`LocalTensor` is part of PyTorch’s distributed package. No additional installation is required beyond PyTorch itself.

[Usage Examples](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#id4)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#usage-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following examples demonstrate core patterns for using `LocalTensor`. Each example’s code is included directly from source files that are also tested to ensure correctness. The tests directly invoke these same functions.

### [Example 1: Basic LocalTensor Creation and Operations](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#id5)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#example-1-basic-localtensor-creation-and-operations "Link to this heading")

**Creating a LocalTensor from per-rank tensors:**

def create\_local\_tensor():
    """Create a LocalTensor from per-rank tensors.

    Returns: (local\_tensor, (expected\_shape, expected\_ranks, expected\_rank\_0, expected\_rank\_1))
    """
    rank\_0\_tensor \= torch.tensor(\[\[1.0, 2.0\], \[3.0, 4.0\]\])
    rank\_1\_tensor \= torch.tensor(\[\[5.0, 6.0\], \[7.0, 8.0\]\])

    local\_tensor \= LocalTensor({0: rank\_0\_tensor, 1: rank\_1\_tensor})

    expected \= (torch.Size(\[2, 2\]), frozenset({0, 1}), rank\_0\_tensor, rank\_1\_tensor)
    return local\_tensor, expected

Copy to clipboard

**Arithmetic operations (applied per-rank):**

def arithmetic\_operations():
    """Demonstrate arithmetic on LocalTensor.

    Returns: ((doubled, added), (expected\_doubled\_0, expected\_doubled\_1, expected\_added\_0))
    """
    input\_0 \= torch.tensor(\[1.0, 2.0, 3.0\])
    input\_1 \= torch.tensor(\[4.0, 5.0, 6.0\])

    lt \= LocalTensor({0: input\_0, 1: input\_1})

    doubled \= lt \* 2
    added \= lt + 10

    expected \= (input\_0 \* 2, input\_1 \* 2, input\_0 + 10)
    return (doubled, added), expected

Copy to clipboard

**Extracting a tensor when all shards are identical:**

def reconcile\_identical\_shards():
    """Extract a single tensor when all shards are identical.

    Returns: (result, expected)
    """
    value \= torch.tensor(\[1.0, 2.0, 3.0\])
    lt \= LocalTensor({0: value.clone(), 1: value.clone(), 2: value.clone()})

    result \= lt.reconcile()
    return result, value

Copy to clipboard

**Using LocalTensorMode for automatic LocalTensor creation:**

def use\_local\_tensor\_mode(world\_size: int \= 4):
    """Use LocalTensorMode to auto-create LocalTensors.

    Returns: ((is\_local, num\_ranks), (expected\_is\_local, expected\_num\_ranks))
    """
    with LocalTensorMode(world\_size):
        x \= torch.ones(2, 3)
        is\_local \= isinstance(x, LocalTensor)
        num\_ranks \= len(x.\_ranks)

    return (is\_local, num\_ranks), (True, world\_size)

Copy to clipboard

**Full source:** [example\_01\_basic\_operations.py](https://github.com/pytorch/pytorch/blob/main/test/distributed/local_tensor_tutorial_examples/example_01_basic_operations.py)

### [Example 2: Simulating Collective Operations](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#id6)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#example-2-simulating-collective-operations "Link to this heading")

Test collective operations like `all_reduce`, `broadcast`, and `all_gather` without multiple processes.

**All-reduce with SUM:**

def all\_reduce\_sum(process\_group):
    """Simulate all\_reduce with SUM across ranks.

    Returns: (result, expected)
    """
    tensors \= {
        0: torch.tensor(\[\[1.0, 2.0\], \[3.0, 4.0\]\]),
        1: torch.tensor(\[\[5.0, 6.0\], \[7.0, 8.0\]\]),
        2: torch.tensor(\[\[9.0, 10.0\], \[11.0, 12.0\]\]),
    }

    expected \= sum(tensors.values())

    with LocalTensorMode(frozenset(tensors.keys())):
        lt \= LocalTensor({k: v.clone() for k, v in tensors.items()})
        dist.all\_reduce(lt, op\=dist.ReduceOp.SUM, group\=process\_group)
        result \= lt.reconcile()

    return result, expected

Copy to clipboard

**Broadcast from a source rank:**

def broadcast\_from\_rank(process\_group, src\_rank: int \= 0):
    """Simulate broadcast from a source rank.

    Returns: (result, expected)
    """
    tensors \= {
        0: torch.tensor(\[10.0, 20.0, 30.0\]),
        1: torch.tensor(\[40.0, 50.0, 60.0\]),
        2: torch.tensor(\[70.0, 80.0, 90.0\]),
    }

    expected \= tensors\[src\_rank\].clone()

    with LocalTensorMode(frozenset(tensors.keys())):
        lt \= LocalTensor({k: v.clone() for k, v in tensors.items()})
        dist.broadcast(lt, src\=src\_rank, group\=process\_group)
        result \= lt.reconcile()

    return result, expected

Copy to clipboard

**All-gather to collect tensors from all ranks:**

def all\_gather\_tensors(process\_group):
    """Simulate all\_gather to collect tensors from all ranks.

    Returns: (results\_list, expected\_list)
    """
    tensors \= {
        0: torch.tensor(\[\[1.0, 2.0\]\]),
        1: torch.tensor(\[\[3.0, 4.0\]\]),
        2: torch.tensor(\[\[5.0, 6.0\]\]),
    }
    num\_ranks \= len(tensors)

    expected \= \[tensors\[i\].clone() for i in range(num\_ranks)\]

    with LocalTensorMode(frozenset(tensors.keys())):
        lt \= LocalTensor(tensors)
        output\_list \= \[torch.zeros\_like(lt) for \_ in range(num\_ranks)\]
        dist.all\_gather(output\_list, lt, group\=process\_group)
        results \= \[out.reconcile() for out in output\_list\]

    return results, expected

Copy to clipboard

**Full source:** [example\_02\_collective\_operations.py](https://github.com/pytorch/pytorch/blob/main/test/distributed/local_tensor_tutorial_examples/example_02_collective_operations.py)

### [Example 3: Working with DTensor](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#id7)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#example-3-working-with-dtensor "Link to this heading")

`LocalTensor` integrates with DTensor for testing distributed tensor parallelism.

**Distribute a tensor and verify reconstruction:**

def distribute\_and\_verify(world\_size: int \= 4):
    """Distribute a tensor and verify reconstruction.

    Returns: ((sharded\_actual, replicated\_actual), (sharded\_expected, replicated\_expected))
    """
    with LocalTensorMode(world\_size):
        mesh \= init\_device\_mesh("cpu", (world\_size,))
        tensor \= torch.arange(16).reshape(4, 4).float()

        dt\_sharded \= distribute\_tensor(tensor, mesh, \[Shard(0)\])
        dt\_replicated \= distribute\_tensor(tensor, mesh, \[Replicate()\])

        sharded\_actual \= dt\_sharded.full\_tensor().reconcile()
        replicated\_actual \= dt\_replicated.to\_local().reconcile()

    return (sharded\_actual, replicated\_actual), (tensor, tensor)

Copy to clipboard

**Distributed matrix multiplication:**

def dtensor\_matmul(world\_size: int \= 4):
    """Perform matrix multiplication with DTensors.

    Returns: (actual, expected)
    """
    with LocalTensorMode(world\_size):
        mesh \= init\_device\_mesh("cpu", (world\_size,))

        a \= torch.randn(8, 4)
        b \= torch.randn(4, 6)

        da \= distribute\_tensor(a, mesh, \[Shard(0)\])
        db \= distribute\_tensor(b, mesh, \[Replicate()\])

        dc \= da @ db

        expected \= a @ b
        actual \= dc.full\_tensor().reconcile()

    return actual, expected

Copy to clipboard

**Simulating a distributed linear layer:**

def dtensor\_linear\_layer(world\_size: int \= 4):
    """Simulate a distributed linear layer forward pass.

    Returns: (actual, expected)
    """
    batch\_size, in\_features, out\_features \= 16, 8, 4

    with LocalTensorMode(world\_size):
        mesh \= init\_device\_mesh("cpu", (world\_size,))

        x \= torch.randn(batch\_size, in\_features)
        w \= torch.randn(in\_features, out\_features)
        b \= torch.randn(out\_features)

        dx \= distribute\_tensor(x, mesh, \[Shard(0)\])
        dw \= distribute\_tensor(w, mesh, \[Replicate()\])
        db \= distribute\_tensor(b, mesh, \[Replicate()\])

        dy \= torch.relu(dx @ dw + db)

        expected \= torch.relu(x @ w + b)
        actual \= dy.full\_tensor().reconcile()

    return actual, expected

Copy to clipboard

**Full source:** [example\_03\_dtensor\_integration.py](https://github.com/pytorch/pytorch/blob/main/test/distributed/local_tensor_tutorial_examples/example_03_dtensor_integration.py)

### [Example 4: Handling Uneven Sharding](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#id8)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#example-4-handling-uneven-sharding "Link to this heading")

Real-world distributed systems often have uneven data distribution across ranks. `LocalTensor` handles this using `LocalIntNode`.

**Creating LocalTensor with different sizes per rank:**

def create\_uneven\_shards():
    """Create LocalTensor with different sizes per rank.

    Returns: ((local\_tensor, is\_symint), expected\_shapes\_dict)
    """
    tensors \= {
        0: torch.tensor(\[\[1.0, 2.0, 3.0, 4.0\]\]),  \# 1 row
        1: torch.tensor(\[\[5.0, 6.0, 7.0, 8.0\], \[9.0, 10.0, 11.0, 12.0\]\]),  \# 2 rows
        2: torch.tensor(\[\[13.0, 14.0, 15.0, 16.0\]\]),  \# 1 row
    }

    lt \= LocalTensor(tensors)
    is\_symint \= isinstance(lt.shape\[0\], torch.SymInt)

    expected\_shapes \= {rank: t.shape for rank, t in tensors.items()}
    return (lt, is\_symint), expected\_shapes

Copy to clipboard

**LocalIntNode arithmetic operations:**

def local\_int\_node\_arithmetic():
    """LocalIntNode for per-rank integer values.

    Returns: ((add\_result, mul\_result), (expected\_add, expected\_mul))
    """
    values\_a \= {0: 10, 1: 20, 2: 30}
    values\_b \= {0: 1, 1: 2, 2: 3}
    local\_a \= LocalIntNode(values\_a)
    local\_b \= LocalIntNode(values\_b)

    result\_add \= local\_a.add(local\_b)
    result\_mul \= local\_a.mul(local\_b)

    expected\_add \= {k: values\_a\[k\] + values\_b\[k\] for k in values\_a}
    expected\_mul \= {k: values\_a\[k\] \* values\_b\[k\] for k in values\_a}

    return (
        (dict(result\_add.\_local\_ints), dict(result\_mul.\_local\_ints)),
        (expected\_add, expected\_mul),
    )

Copy to clipboard

**DTensor with unevenly divisible dimensions:**

def dtensor\_uneven\_sharding(world\_size: int \= 3):
    """DTensor with unevenly divisible tensor dimension.

    Returns: ((rows\_per\_rank, matches), expected\_total\_rows)
    """
    total\_rows \= 10

    with LocalTensorMode(world\_size):
        mesh \= init\_device\_mesh("cpu", (world\_size,))

        tensor \= torch.arange(total\_rows \* 4).reshape(total\_rows, 4).float()
        dt \= distribute\_tensor(tensor, mesh, \[Shard(0)\])

        local \= dt.to\_local()
        rows\_per\_rank \= {
            rank: local.\_local\_tensors\[rank\].shape\[0\] for rank in range(world\_size)
        }

        reconstructed \= dt.full\_tensor().reconcile()
        matches \= torch.equal(reconstructed, tensor)

    return (rows\_per\_rank, matches), total\_rows

Copy to clipboard

**Full source:** [example\_04\_uneven\_sharding.py](https://github.com/pytorch/pytorch/blob/main/test/distributed/local_tensor_tutorial_examples/example_04_uneven_sharding.py)

### [Example 5: Rank-Specific Computations](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#id9)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#example-5-rank-specific-computations "Link to this heading")

Sometimes you need to perform different operations on different ranks.

**Using rank\_map() to create per-rank values:**

def use\_rank\_map(world\_size: int \= 4):
    """Create LocalTensors with per-rank values using rank\_map.

    Returns: (values\_dict, expected\_dict)
    """
    with LocalTensorMode(world\_size):
        lt \= rank\_map(lambda rank: torch.full((2, 3), float(rank)))
        values \= {
            rank: lt.\_local\_tensors\[rank\]\[0, 0\].item() for rank in range(world\_size)
        }

    expected \= {rank: float(rank) for rank in range(world\_size)}
    return values, expected

Copy to clipboard

**Using tensor\_map() to transform shards per-rank:**

def use\_tensor\_map(world\_size: int \= 4):
    """Transform each shard differently using tensor\_map.

    Returns: (values\_dict, expected\_dict)
    """
    with LocalTensorMode(world\_size):
        lt \= rank\_map(lambda rank: torch.ones(2, 2) \* (rank + 1))

        def scale\_by\_rank(rank: int, tensor: torch.Tensor) \-> torch.Tensor:
            return tensor \* (rank + 1)

        scaled \= tensor\_map(lt, scale\_by\_rank)
        values \= {
            rank: scaled.\_local\_tensors\[rank\]\[0, 0\].item() for rank in range(world\_size)
        }

    \# (rank + 1) \* (rank + 1) = (rank + 1)^2
    expected \= {rank: float((rank + 1) \*\* 2) for rank in range(world\_size)}
    return values, expected

Copy to clipboard

**Temporarily exiting LocalTensorMode:**

def disable\_mode\_temporarily(world\_size: int \= 4):
    """Temporarily exit LocalTensorMode for regular tensor ops.

    Returns: ((inside\_type, disabled\_type), (expected\_inside, expected\_disabled))
    """
    with LocalTensorMode(world\_size) as mode:
        lt \= torch.ones(2, 2)
        inside\_type \= type(lt).\_\_name\_\_

        with mode.disable():
            regular \= torch.ones(2, 2)
            disabled\_type \= type(regular).\_\_name\_\_

    return (inside\_type, disabled\_type), ("LocalTensor", "Tensor")

Copy to clipboard

**Full source:** [example\_05\_rank\_specific.py](https://github.com/pytorch/pytorch/blob/main/test/distributed/local_tensor_tutorial_examples/example_05_rank_specific.py)

### [Example 6: Multi-Dimensional Meshes](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#id10)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#example-6-multi-dimensional-meshes "Link to this heading")

Use 2D/3D device meshes for hybrid parallelism (e.g., data parallel + tensor parallel).

**Creating a 2D mesh:**

def create\_2d\_mesh():
    """Create a 2D mesh for hybrid parallelism.

    Returns: ((shape, dim\_names, total\_size), (expected\_shape, expected\_names, expected\_size))
    """
    world\_size \= 8
    dp\_size, tp\_size \= 4, 2

    with LocalTensorMode(world\_size):
        mesh \= init\_device\_mesh("cpu", (dp\_size, tp\_size), mesh\_dim\_names\=("dp", "tp"))
        shape \= mesh.shape
        dim\_names \= mesh.mesh\_dim\_names
        total\_size \= mesh.size()

    expected \= ((dp\_size, tp\_size), ("dp", "tp"), world\_size)
    return (shape, dim\_names, total\_size), expected

Copy to clipboard

**Hybrid parallelism (DP + TP):**

def hybrid\_parallelism():
    """Combine data parallel and tensor parallel.

    Returns: (actual, expected)
    """
    world\_size \= 8
    dp\_size, tp\_size \= 4, 2

    with LocalTensorMode(world\_size):
        mesh \= init\_device\_mesh("cpu", (dp\_size, tp\_size), mesh\_dim\_names\=("dp", "tp"))

        x \= torch.randn(16, 8)
        dx \= distribute\_tensor(x, mesh, \[Shard(0), Replicate()\])

        w \= torch.randn(8, 12)
        dw \= distribute\_tensor(w, mesh, \[Replicate(), Shard(1)\])

        dy \= dx @ dw

        expected \= x @ w
        actual \= dy.full\_tensor().reconcile()

    return actual, expected

Copy to clipboard

**3D mesh for DP + TP + PP:**

def create\_3d\_mesh():
    """Create a 3D mesh for DP + TP + PP.

    Returns: (actual, expected)
    """
    world\_size \= 24
    pp\_size, dp\_size, tp\_size \= 2, 3, 4

    with LocalTensorMode(world\_size):
        mesh \= init\_device\_mesh(
            "cpu",
            (pp\_size, dp\_size, tp\_size),
            mesh\_dim\_names\=("pp", "dp", "tp"),
        )

        tensor \= torch.randn(8, 16, 32)
        dt \= distribute\_tensor(tensor, mesh, \[Replicate(), Shard(0), Shard(2)\])

        actual \= dt.full\_tensor().reconcile()

    return actual, tensor

Copy to clipboard

**Full source:** [example\_06\_multidim\_mesh.py](https://github.com/pytorch/pytorch/blob/main/test/distributed/local_tensor_tutorial_examples/example_06_multidim_mesh.py)

[Testing Tutorial Examples](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#id11)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#testing-tutorial-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

All examples in this tutorial are tested to ensure correctness. The test suite directly invokes the same functions included above:

\# From test\_local\_tensor\_tutorial\_examples.py
from example\_01\_basic\_operations import create\_local\_tensor

def test\_create\_local\_tensor(self):
    lt \= create\_local\_tensor()
    self.assertIsInstance(lt, LocalTensor)
    self.assertEqual(lt.shape, torch.Size(\[2, 2\]))

Copy to clipboard

**Test suite:** [test\_local\_tensor\_tutorial\_examples.py](https://github.com/pytorch/pytorch/blob/main/test/distributed/local_tensor_tutorial_examples/test_local_tensor_tutorial_examples.py)

[API Reference](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#id12)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#api-reference "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Core Classes](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#id13)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#core-classes "Link to this heading")

_class_ torch.distributed.\_local\_tensor.LocalTensor(_local\_tensors_, _requires\_grad\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_local_tensor/__init__.py#L922)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.LocalTensor "Link to this definition")

LocalTensor is a Tensor subclass that simulates a tensor distributed across multiple SPMD (Single Program, Multiple Data) ranks. Each LocalTensor instance internally holds a mapping from global rank ids to their corresponding local Tensor shards.Operations performed on a LocalTensor are applied independently to each local shard, mimicking distributed computation. Collectives and other distributed operations are handled by mapping them to the local shards as appropriate.

Note

This class is primarily intended for debugging and simulating distributed tensor computations on a single process.

Return type:

[LocalTensor](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.LocalTensor "torch.distributed._local_tensor.LocalTensor")

reconcile()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_local_tensor/__init__.py#L1124)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.LocalTensor.reconcile "Link to this definition")

Reconciles the LocalTensor into a single torch.Tensor by ensuring all local shards are identical and returning a detached clone of one of them.

Note

This method is useful for extracting a representative tensor from a LocalTensor when all shards are expected to be the same, such as after a collective operation that synchronizes all ranks.

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

tolist()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_local_tensor/__init__.py#L1103)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.LocalTensor.tolist "Link to this definition")

Try to reconcile, if successful convert to list, otherwise if dtype is integer, convert to list of local integers.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]

_class_ torch.distributed.\_local\_tensor.LocalTensorMode(_ranks_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_local_tensor/__init__.py#L1227)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.LocalTensorMode "Link to this definition")

A TorchDispatchMode that simulates SPMD (Single Program, Multiple Data) execution for LocalTensor objects across a set of ranks.

LocalTensorMode enables PyTorch operations to be transparently applied to each local shard of a LocalTensor, as if they were distributed across multiple ranks. When active, this mode intercepts tensor operations and dispatches them to each rank’s local tensor, collecting and wrapping the results as LocalTensors. It also handles collective operations by mapping them to local implementations.

This mode is primarily intended for debugging and simulating distributed tensor computations on a single process, rather than for high-performance distributed training. It maintains a stack of active modes, patches DeviceMesh coordinate resolution, and provides utilities for temporarily disabling the mode or mapping functions over ranks.

disable()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_local_tensor/__init__.py#L1476)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.LocalTensorMode.disable "Link to this definition")

Disables LocalTensorMode temporarily. Primarily is intended to be used to perform rank specific computations and merge results back before enabling LocalTensorMode back.

Return type:

[_Generator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "(in Python v3.15)")
\[None, None, None\]

rank\_map(_cb_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_local_tensor/__init__.py#L1499)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.LocalTensorMode.rank_map "Link to this definition")

Creates a LocalTensor instance by mapping rank id to its local shard.

Return type:

[_LocalTensor_](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.LocalTensor "torch.distributed._local_tensor.LocalTensor")

tensor\_map(_tensor_, _cb_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_local_tensor/__init__.py#L1508)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.LocalTensorMode.tensor_map "Link to this definition")

Creates a LocalTensor instance by mapping rank id to its local shard.

Return type:

[_LocalTensor_](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.LocalTensor "torch.distributed._local_tensor.LocalTensor")

_class_ torch.distributed.\_local\_tensor.LocalIntNode(_local\_ints_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_local_tensor/__init__.py#L423)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.LocalIntNode "Link to this definition")

Like a LocalTensor, but for an int. We can’t use a 0D tensor to represent this because often only a SymInt is accepted where we wish to use this.

Return type:

ConstantIntNode | [LocalIntNode](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.LocalIntNode "torch.distributed._local_tensor.LocalIntNode")

### [Utility Functions](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#id14)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#utility-functions "Link to this heading")

torch.distributed.\_local\_tensor.local\_tensor\_mode()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_local_tensor/__init__.py#L1794)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.local_tensor_mode "Link to this definition")

Returns the current active LocalTensorMode if one exists.

This function checks the global stack of LocalTensorMode instance. If there is at least one LocalTensorMode active, it returns the most recently entered (top of the stack) LocalTensorMode. If no LocalTensorMode is active, it returns None.

Returns:

The current LocalTensorMode if active, else None.

Return type:

Optional\[[LocalTensorMode](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.LocalTensorMode "torch.distributed._local_tensor.LocalTensorMode")\
\]

torch.distributed.\_local\_tensor.enabled\_local\_tensor\_mode()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_local_tensor/__init__.py#L1811)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.enabled_local_tensor_mode "Link to this definition")

Returns the current active LocalTensorMode only if it’s enabled.

This is a convenience function that combines the common pattern of checking if local\_tensor\_mode() is not None and not disabled.

Returns:

The current LocalTensorMode if active and enabled, else None.

Return type:

Optional\[[LocalTensorMode](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.LocalTensorMode "torch.distributed._local_tensor.LocalTensorMode")\
\]

torch.distributed.\_local\_tensor.maybe\_run\_for\_local\_tensor(_func_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_local_tensor/__init__.py#L1827)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.maybe_run_for_local_tensor "Link to this definition")

Decorator that ensures a function is executed for each local tensor shard when running under LocalTensorMode. If not in LocalTensorMode, the function is executed normally. When in LocalTensorMode, the function is run for each rank, and the results are collected appropriately.

This decorator is useful for functions that exhibit non-SPMD behavior, such as those requiring rank specific actions. For example, a function that computes offset into input tensor based on rank.

Note that the function being decorated must not have any side effects and contain operations for a single rank only. For example, wrapping a function that performs a collective operation will not work.

Parameters:

**func** (_Callable__\[__...__,_ _Any__\]_) – The function to be decorated.

Returns:

The wrapped function that handles LocalTensorMode logic.

Return type:

Callable\[…, Any\]

torch.distributed.\_local\_tensor.maybe\_disable\_local\_tensor\_mode()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_local_tensor/__init__.py#L1898)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#torch.distributed._local_tensor.maybe_disable_local_tensor_mode "Link to this definition")

Context manager that disables LocalTensorMode for the duration of the context.

Return type:

[_AbstractContextManager_](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager "(in Python v3.15)")

[Best Practices](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#id15)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#best-practices "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  **Use for Testing Only**: LocalTensor has significant overhead and should not be used in production code.
    
2.  **Initialize Process Groups**: Even for local testing, you need to initialize a process group (use the “fake” backend).
    
3.  **Avoid requires\_grad on Inner Tensors**: LocalTensor expects inner tensors to not have `requires_grad=True`. Set gradients on the LocalTensor wrapper instead.
    
4.  **Reconcile for Assertions**: Use `reconcile()` to extract a single tensor when all ranks should have identical values (e.g., after an all-reduce).
    
5.  **Debug with Direct Access**: Access individual shards via `tensor._local_tensors[rank]` for debugging.
    

[Common Pitfalls](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#id16)
[#](https://docs.pytorch.org/docs/2.15/notes/local_tensor_tutorial.html#common-pitfalls "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  **Forgetting the Context Manager**: Operations on LocalTensor outside `LocalTensorMode` still work but won’t create new LocalTensors from factories.
    
2.  **Mismatched Ranks**: Ensure all LocalTensors in an operation have compatible ranks.
    
3.  **Inner Tensor Gradients**: Creating LocalTensor from tensors with `requires_grad=True` will raise an error.
    

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/notes/local_tensor_tutorial.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/notes/local_tensor_tutorial.md.txt)

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