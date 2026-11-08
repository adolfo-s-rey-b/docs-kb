For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/reference-data/reference-previous-nodes.md)
.

When working with data in n8n, you'll often need to reference information from the current node or from previous nodes in your workflow.

Common ways of referencing[](https://docs.n8n.io/build/work-with-data/reference-data/reference-previous-nodes#common-ways-of-referencing)

------------------------------------------------------------------------------------------------------------------------------------------

The most frequently used methods for accessing data are:

*   `**$json**`: Access JSON data from the current input item
    
*   `**$('<node-name>').item.json**`: Access JSON data from a [linked item](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)
     in a previous node
    
*   `**$('<node-name>').item.binary**`: Access binary data (files, images) from a [linked item](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)
     in a previous node
    

Other referencing methods[](https://docs.n8n.io/build/work-with-data/reference-data/reference-previous-nodes#other-referencing-methods)

----------------------------------------------------------------------------------------------------------------------------------------

These methods work in both expressions and the Code node:

Method

Description

`$binary`

Access binary data from the current input item

`$input.item`

The input item currently being processed

`$('<node-name>').first()`

Get the first item from a specified node

`$('<node-name>').last()`

Get the last item from a specified node

`$('<node-name>').all()`

Get all items from a specified node

Current node input[](https://docs.n8n.io/build/work-with-data/reference-data/reference-previous-nodes#current-node-input)

--------------------------------------------------------------------------------------------------------------------------

Methods for working with the input of the current node. Some methods and variables aren't available in the Code node.

**Python support**

You can use Python in the Code node. It isn't available in expressions.

JavaScript

Python

Method

Description

Available in Code node?

`$binary`

Shorthand for `$input.item.binary`. Incoming binary data from a node

❌

`$input.item`

The input item of the current node that's being processed. Refer to [Item linking](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)
 for more information on paired items and item linking.

✅

`$input.all()`

All input items in current node.

✅

`$input.first()`

First input item in current node.

✅

`$input.last()`

Last input item in current node.

✅

`$input.params`

Object containing the query settings of the previous node. This includes data such as the operation it ran, result limits, and so on.

✅

`$json`

Shorthand for `$input.item.json`. Incoming JSON data from a node. Refer to [Data structure](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure)
 for information on item structure.

✅ (when running once for each item)

`$input.context.noItemsLeft`

Boolean. Only available when working with the Loop Over Items node. Provides information about what's happening in the node. Use this to determine whether the node is still processing items.

✅

Method

Description

`_input.item`

The input item of the current node that's being processed. Refer to [Item linking](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)
 for more information on paired items and item linking.

`_input.all()`

All input items in current node.

`_input.first()`

First input item in current node.

`_input.last()`

Last input item in current node.

`_input.params`

Object containing the query settings of the previous node. This includes data such as the operation it ran, result limits, and so on.

`_json`

Shorthand for `_input.item.json`. Incoming JSON data from a node. Refer to [Data structure](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure)
 for information on item structure. Available when you set **Mode** to **Run Once for Each Item**.

`_input.context.noItemsLeft`

Boolean. Only available when working with the Loop Over Items node. Provides information about what's happening in the node. Use this to determine whether the node is still processing items.

Output of other nodes[](https://docs.n8n.io/build/work-with-data/reference-data/reference-previous-nodes#output-of-other-nodes)

--------------------------------------------------------------------------------------------------------------------------------

Methods for working with the output of other nodes. Some methods and variables aren't available in the Code node.

Method

Description

Available in Code node?

`$("<node-name>").all(branchIndex?, runIndex?)`

Returns all items from a given node. If `branchIndex` isn't given it will default to the output that connects `node-name` with the node where you use the expression or code.

✅

`$("<node-name>").first(branchIndex?, runIndex?)`

The first item output by the given node. If `branchIndex` isn't given it will default to the output that connects `node-name` with the node where you use the expression or code.

✅

`$("<node-name>").last(branchIndex?, runIndex?)`

The last item output by the given node. If `branchIndex` isn't given it will default to the output that connects `node-name` with the node where you use the expression or code.

✅

`$("<node-name>").item`

The linked item. This is the item in the specified node used to produce the current item. Refer to [Item linking](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)
 for more information on item linking.

✅

`$("<node-name>").item.binary`

Binary data from the linked item, keyed by binary property name (`data` by default). Refer to [`BinaryFile`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile)
 for the available properties.

✅

`$("<node-name>").params`

Object containing the query settings of the given node. This includes data such as the operation it ran, result limits, and so on.

✅

`$("<node-name>").context`

Boolean. Only available when working with the Loop Over Items node. Provides information about what's happening in the node. Use this to determine whether the node is still processing items.

✅

`$("<node-name>").itemMatching(currentNodeInputIndex)`

Use instead of `$("<node-name>").item` in the Code node if you need to trace back from an input item.

✅

Reference binary data from a previous node[](https://docs.n8n.io/build/work-with-data/reference-data/reference-previous-nodes#reference-binary-data-from-a-previous-node)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`$('<node-name>').item` returns the whole [linked item](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)
, so you can read its binary data the same way you read its JSON data: use `.item.json` for the item's JSON object and `.item.binary` for its binary data (files, images, and other attachments).

An item can hold several binary properties, each under its own name, so `.item.binary` returns an object of those properties rather than a single value. Most nodes output binary data under the property name `data`, but the name depends on the upstream node. Each binary property is a `BinaryFile` with fields such as `fileName`, `mimeType`, and `fileExtension`.

For example, to get the file name of the binary property `data` produced by an **HTTP Request** node:

Copy

    {{ $('HTTP Request').item.binary.data.fileName }}

For more about binary data and the nodes that produce it, refer to [Binary data](https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-files-and-images)
.

Related resources[](https://docs.n8n.io/build/work-with-data/reference-data/reference-previous-nodes#related-resources)

------------------------------------------------------------------------------------------------------------------------

*   [Reference data](https://docs.n8n.io/build/work-with-data/reference-data)
    
*   [Use the UI mapper](https://docs.n8n.io/build/work-with-data/reference-data/use-the-ui-mapper)
    
*   [Link data items](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)
    

[PreviousUse the UI mapper](https://docs.n8n.io/build/work-with-data/reference-data/use-the-ui-mapper)
[NextLink data items](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)

Last updated 10 days ago

Was this helpful?