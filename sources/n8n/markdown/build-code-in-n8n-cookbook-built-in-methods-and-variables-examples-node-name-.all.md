For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/node-name-.all.md)
.

This gives access to all the items of the current or parent nodes. If you don't supply any parameters, it returns all the items of the current node.

Getting items[](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/node-name-.all#getting-items)

-------------------------------------------------------------------------------------------------------------------------------------

JavaScript

Python

Copy

    // Returns all the items of the given node and current run
    let allItems = $("<node-name>").all();
    
    // Returns all items the node "IF" outputs (index: 0 which is Output "true" of its most recent run)
    let allItems = $("IF").all();
    
    // Returns all items the node "IF" outputs (index: 0 which is Output "true" of the same run as current node)
    let allItems = $("IF").all(0, $runIndex);
    
    // Returns all items the node "IF" outputs (index: 1 which is Output "false" of run 0 which is the first run)
    let allItems = $("IF").all(1, 0);

Copy

    # Returns all the items of the given node and current run
    allItems = _("<node-name>").all();
    
    # Returns all items the node "IF" outputs (index: 0 which is Output "true" of its most recent run)
    allItems = _("IF").all();
    
    # Returns all items the node "IF" outputs (index: 0 which is Output "true" of the same run as current node)
    allItems = _("IF").all(0, _runIndex);
    
    # Returns all items the node "IF" outputs (index: 1 which is Output "false" of run 0 which is the first run)
    allItems = _("IF").all(1, 0);

Accessing item data[](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/node-name-.all#accessing-item-data)

-------------------------------------------------------------------------------------------------------------------------------------------------

Get all items output by a previous node, and log out the data they contain:

JavaScript

Python

Copy

    previousNodeData = $("<node-name>").all();
    for(let i=0; i<previousNodeData.length; i++) {
    	console.log(previousNodeData[i].json);
    }

Copy

    previousNodeData = _("<node-name>").all();
    for item in previousNodeData:
    	# item is of type <class 'pyodide.ffi.JsProxy'>
    	# You need to convert it to a Dict
    	itemDict = item.json.to_py()
    	print(itemDict)

Related resources[](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/node-name-.all#related-resources)

---------------------------------------------------------------------------------------------------------------------------------------------

*   [Built-in methods and variables examples](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples)
    

[PreviousgetWorkflowStaticData](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/getworkflowstaticdata)
[Nextvars](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/vars)

Last updated 10 days ago

Was this helpful?