None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Tree utilities](https://keras.io/api/tree/tree_utilities/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Tree API](https://keras.io/api/tree/)
 / Tree utilities

Tree utilities
==============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L27)

### `MAP_TO_NONE` class

Copied!

`keras.tree.MAP_TO_NONE()`

Special value for use with `traverse()`.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L308)

### `assert_same_paths` function

Copied!

`keras.tree.assert_same_paths(a, b)`

Asserts that two structures have identical paths in their tree structure.

This function verifies that two nested structures have the same paths. Unlike `assert_same_structure`, this function only checks the paths and ignores the collection types. For Sequences, to path is the index: 0, 1, 2, etc. For Mappings, the path is the key, for instance "a", "b", "c". Note that namedtuples also use indices and not field names for the path.

**Examples**

Copied!

`>>> keras.tree.assert_same_paths([0, 1], (2, 3)) >>> Point1 = collections.namedtuple('Point1', ['x', 'y']) >>> Point2 = collections.namedtuple('Point2', ['x', 'y']) >>> keras.tree.assert_same_paths(Point1(0, 1), Point2(2, 3))`

**Arguments**

*   **a**: an arbitrarily nested structure.
*   **b**: an arbitrarily nested structure.

**Raises**

*   **ValueError**: If the paths in structure `a` don't match the paths in structure `b`. The error message will include the specific paths that differ.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L252)

### `assert_same_structure` function

Copied!

`keras.tree.assert_same_structure(a, b, check_types=None)`

Asserts that two structures are nested in the same way.

This function verifies that the nested structures match. The leafs can be of any type. At each level, the structures must be of the same type and have the same number of elements. Instances of `dict`, `OrderedDict` and `defaultdict` are all considered the same as long as they have the same set of keys. However, `list`, `tuple`, `namedtuple` and `deque` are not the same structures. Two namedtuples with identical fields and even identical names are not the same structures.

**Examples**

Copied!

`>>> keras.tree.assert_same_structure([(0, 1)], [(2, 3)])`

Copied!

`>>> Foo = collections.namedtuple('Foo', ['a', 'b']) >>> AlsoFoo = collections.namedtuple('Foo', ['a', 'b']) >>> keras.tree.assert_same_structure(Foo(0, 1), Foo(2, 3)) >>> keras.tree.assert_same_structure(Foo(0, 1), AlsoFoo(2, 3)) Traceback (most recent call last):     ... ValueError: The two structures don't have the same nested structure. ...`

**Arguments**

*   **a**: an arbitrarily nested structure.
*   **b**: an arbitrarily nested structure.
*   **check\_types**: Deprecated. The behavior of this flag was inconsistent, it no longer has any effect. For a looser check, use `assert_same_paths` instead, which considers `list`, `tuple`, `namedtuple` and `deque` as matching structures.

**Raises**

*   **ValueError**: If the two structures `a` and `b` don't match.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L108)

### `flatten` function

Copied!

`keras.tree.flatten(structure)`

Flattens a possibly nested structure into a list.

In the case of dict instances, the sequence consists of the values, sorted by key to ensure deterministic behavior. However, instances of `collections.OrderedDict` are handled differently: their sequence order is used instead of the sorted keys. The same convention is followed in `pack_sequence_as`. This correctly unflattens dicts and `OrderedDict` after they have been flattened, or vice-versa.

Dictionaries with non-sortable keys are not supported.

**Examples**

Copied!

`>>> keras.tree.flatten([[1, 2, 3], [4, [5], [[6]]]]) [1, 2, 3, 4, 5, 6] >>> keras.tree.flatten(None) [None] >>> keras.tree.flatten(1) [1] >>> keras.tree.flatten({100: 'world!', 6: 'Hello'}) ['Hello', 'world!']`

**Arguments**

*   **structure**: An arbitrarily nested structure.

**Returns**

A list, the flattened version of the input `structure`.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L149)

### `flatten_with_path` function

Copied!

`keras.tree.flatten_with_path(structure)`

Flattens a possibly nested structure into a list.

This is a variant of flattens() which produces a list of pairs: `(path, item)`. A path is a tuple of indices and/or keys which uniquely identifies the position of the corresponding item.

Dictionaries with non-sortable keys are not supported.

**Examples**

Copied!

`>>> keras.flatten_with_path([{"foo": 42}]) [((0, 'foo'), 42)]`

**Arguments**

*   **structure**: An arbitrarily nested structure.

**Returns**

A list of `(path, item)` pairs corresponding to the flattened version of the input `structure`.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L34)

### `is_nested` function

Copied!

`keras.tree.is_nested(structure)`

Checks if a given structure is nested.

**Examples**

Copied!

`>>> keras.tree.is_nested(42) False >>> keras.tree.is_nested({"foo": 42}) True`

**Arguments**

*   **structure**: A structure to check.

**Returns**

`True` if a given structure is nested, i.e. is a sequence, a mapping, or a namedtuple, and `False` otherwise.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L399)

### `lists_to_tuples` function

Copied!

`keras.tree.lists_to_tuples(structure)`

Returns the structure with list instances changed to tuples.

**Arguments**

*   **structure**: Arbitrarily nested structure.

**Returns**

The same structure but with tuples instead of lists.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L412)

### `map_shape_structure` function

Copied!

`keras.tree.map_shape_structure(func, structure)`

Variant of keras.tree.map\_structure that operates on shape tuples.

Tuples containing ints and Nones are considered shapes and passed to `func`.

**Arguments**

*   **structure**: Arbitrarily nested structure.

**Returns**

The same structure with `func` applied.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L175)

### `map_structure` function

Copied!

`keras.tree.map_structure(func, *structures, none_is_leaf=True)`

Maps `func` through given structures.

**Examples**

Copied!

`>>> structure = [[1], [2], [3]] >>> keras.tree.map_structure(lambda v: v**2, structure) [[1], [4], [9]] >>> keras.tree.map_structure(lambda x, y: x * y, structure, structure) [[1], [4], [9]]`

Copied!

`>>> Foo = collections.namedtuple('Foo', ['a', 'b']) >>> structure = Foo(a=1, b=2) >>> keras.tree.map_structure(lambda v: v * 2, structure) Foo(a=2, b=4)`

**Arguments**

*   **func**: A callable that accepts as many arguments as there are structures.
*   **\*structures**: Arbitrarily nested structures of the same layout.
*   **none\_is\_leaf**: If True, `func` will be called on `None` leaves. If False, `None` values are not passed to `func` and are returned in the output directly.

**Returns**

A new structure with the same layout as the given ones.

**Raises**

*   **TypeError**: If `structures` is empty or `func` is not callable.
*   **ValueError**: If there is more than one items in `structures` and some of the nested structures don't match according to the rules of `assert_same_structure`.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L215)

### `map_structure_up_to` function

Copied!

`keras.tree.map_structure_up_to(shallow_structure, func, *structures)`

Maps `func` through given structures up to `shallow_structure`.

This is a variant of `map_structure` which only maps the given structures up to `shallow_structure`. All further nested components are retained as-is.

**Examples**

Copied!

`>>> shallow_structure = [None, None] >>> structure = [[1, 1], [2, 2]] >>> keras.tree.map_structure_up_to(shallow_structure, len, structure) [2, 2]`

Copied!

`>>> shallow_structure = [None, [None, None]] >>> keras.tree.map_structure_up_to(shallow_structure, str, structure) ['[1, 1]', ['2', '2']]`

**Arguments**

*   **shallow\_structure**: A structure with layout common to all `structures`.
*   **func**: A callable that accepts as many arguments as there are structures.
*   **\*structures**: Arbitrarily nested structures of the same layout.

**Returns**

A new structure with the same layout as `shallow_structure`.

**Raises**

*   **TypeError**: If `structures` is empty or `func` is not callable.
*   **ValueError**: If one of the items in `structures` doesn't match the nested structure of `shallow_structure` according to the rules of `assert_same_structure`. Items in `structures` are allowed to be nested deeper than `shallow_structure`, but they cannot be shallower.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L337)

### `pack_sequence_as` function

Copied!

`keras.tree.pack_sequence_as(structure, flat_sequence)`

Returns a given flattened sequence packed into a given structure.

If `structure` is an atom, `flat_sequence` must be a single-item list; in this case the return value is `flat_sequence[0]`.

If `structure` is or contains a dict instance, the keys will be sorted to pack the flat sequence in deterministic order. However, instances of `collections.OrderedDict` are handled differently: their sequence order is used instead of the sorted keys. The same convention is followed in `flatten`. This correctly repacks dicts and `OrderedDicts` after they have been flattened, or vice-versa.

Dictionaries with non-sortable keys are not supported.

**Examples**

Copied!

`>>> structure = {"key3": "", "key1": "", "key2": ""} >>> flat_sequence = ["value1", "value2", "value3"] >>> keras.tree.pack_sequence_as(structure, flat_sequence) {"key3": "value3", "key1": "value1", "key2": "value2"}`

Copied!

`>>> structure = (("a", "b"), ("c", "d", "e"), "f") >>> flat_sequence = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0] >>> keras.tree.pack_sequence_as(structure, flat_sequence) ((1.0, 2.0), (3.0, 4.0, 5.0), 6.0)`

Copied!

`>>> structure = {"key3": {"c": ("alpha", "beta"), "a": ("gamma")}, ... "key1": {"e": "val1", "d": "val2"}} >>> flat_sequence = ["val2", "val1", 3.0, 1.0, 2.0] >>> keras.tree.pack_sequence_as(structure, flat_sequence) {'key3': {'c': (1.0, 2.0), 'a': 3.0}, 'key1': {'e': 'val1', 'd': 'val2'}}`

Copied!

`>>> structure = ["a"] >>> flat_sequence = [np.array([[1, 2], [3, 4]])] >>> keras.tree.pack_sequence_as(structure, flat_sequence) [array([[1, 2],    [3, 4]])]`

Copied!

`>>> structure = ["a"] >>> flat_sequence = [keras.ops.ones([2, 2])] >>> keras.tree.pack_sequence_as(structure, flat_sequence) [array([[1., 1.],    [1., 1.]]]`

**Arguments**

*   **structure**: Arbitrarily nested structure.
*   **flat\_sequence**: Flat sequence to pack.

**Returns**

`flat_sequence` converted to have the same recursive structure as `structure`.

**Raises**

*   **TypeError**: If `flat_sequence` is not iterable.
*   **ValueError**: If `flat_sequence` cannot be repacked as `structure`; for instance, if `flat_sequence` has too few or too many elements.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/tree/tree_api.py#L55)

### `traverse` function

Copied!

`keras.tree.traverse(func, structure, top_down=True)`

Traverses the given nested structure, applying the given function.

The traversal is depth-first. If `top_down` is True (default), parents are returned before their children (giving the option to avoid traversing into a sub-tree).

**Examples**

Copied!

`>>> v = [] >>> keras.tree.traverse(v.append, [(1, 2), [3], {"a": 4}], top_down=True) [(1, 2), [3], {'a': 4}] >>> v [[(1, 2), [3], {'a': 4}], (1, 2), 1, 2, [3], 3, {'a': 4}, 4]`

Copied!

`>>> v = [] >>> keras.tree.traverse(v.append, [(1, 2), [3], {"a": 4}], top_down=False) [(1, 2), [3], {'a': 4}] >>> v [1, 2, (1, 2), 3, [3], 4, {'a': 4}, [(1, 2), [3], {'a': 4}]]`

**Arguments**

*   **func**: The function to be applied to each sub-nest of the structure.
*   \_\_ When traversing top-down\_\_: If `func(subtree) is None` the traversal continues into the sub-tree. If `func(subtree) is not None` the traversal does not continue into the sub-tree. The sub-tree will be replaced by `func(subtree)` in the returned structure (to replace the sub-tree with `None`, use the special value `MAP_TO_NONE`).
*   \_\_ When traversing bottom-up\_\_: If `func(subtree) is None` the traversed sub-tree is returned unaltered. If `func(subtree) is not None` the sub-tree will be replaced by `func(subtree)` in the returned structure (to replace the sub-tree with None, use the special value `MAP_TO_NONE`).
*   \_\_ structure\_\_: The structure to traverse.
*   **top\_down**: If True, parent structures will be visited before their children.

**Returns**

The structured output from the traversal.

**Raises**

*   **TypeError**: If `func` is not callable.

* * *

[Tree utilities](https://keras.io/api/tree/tree_utilities/#tree-utilities)

[`MAP_TO_NONE` class](https://keras.io/api/tree/tree_utilities/#maptonone-class)

[`assert_same_paths` function](https://keras.io/api/tree/tree_utilities/#assertsamepaths-function)

[`assert_same_structure` function](https://keras.io/api/tree/tree_utilities/#assertsamestructure-function)

[`flatten` function](https://keras.io/api/tree/tree_utilities/#flatten-function)

[`flatten_with_path` function](https://keras.io/api/tree/tree_utilities/#flattenwithpath-function)

[`is_nested` function](https://keras.io/api/tree/tree_utilities/#isnested-function)

[`lists_to_tuples` function](https://keras.io/api/tree/tree_utilities/#liststotuples-function)

[`map_shape_structure` function](https://keras.io/api/tree/tree_utilities/#mapshapestructure-function)

[`map_structure` function](https://keras.io/api/tree/tree_utilities/#mapstructure-function)

[`map_structure_up_to` function](https://keras.io/api/tree/tree_utilities/#mapstructureupto-function)

[`pack_sequence_as` function](https://keras.io/api/tree/tree_utilities/#packsequenceas-function)

[`traverse` function](https://keras.io/api/tree/tree_utilities/#traverse-function)