For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data.md)
.

You can set custom data on your workflow using the Code node or the [Execution Data node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executiondata)
. n8n records this with each execution. You can then use this data when filtering the executions list, or fetch it in your workflows using the Code node.

**Feature availability**

Custom executions data is available on:

*   **n8n Cloud:** Pro, Enterprise
    
*   **Self-hosted:** Registered Community, Enterprise
    

Set and access custom data using the Code node[](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data#set-and-access-custom-data-using-the-code-node)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This section describes how to set and access data using the Code node. Refer to [Execution Data node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executiondata)
 for information on using the Execution Data node to set data. You can't retrieve custom data using the Execution Data node.

### Set custom executions data[](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data#set-custom-executions-data)

Set a single piece of extra data:

JavaScript

Python

Copy

    $execution.customData.set("key", "value");

Copy

    _execution.customData.set("key", "value");

Set all extra data. This overwrites the whole custom data object for this execution:

JavaScript

Python

Copy

    $execution.customData.setAll({"key1": "value1", "key2": "value2"})

Copy

    _execution.customData.setAll({"key1": "value1", "key2": "value2"})

There are limitations:

*   They must be strings
    
*   `key` has a maximum length of 50 characters
    
*   `value` has a maximum length of 255 characters
    
*   n8n supports a maximum of 10 items of custom data
    

### Access the custom data object during execution[](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data#access-the-custom-data-object-during-execution)

You can retrieve the custom data object, or a specific value in it, during an execution:

JavaScript

Python

Copy

    // Access the current state of the object during the execution
    const customData = $execution.customData.getAll();
    
    // Access a specific value set during this execution
    const customData = $execution.customData.get("key");

Copy

    # Access the current state of the object during the execution
    customData = _execution.customData.getAll();
    
    # Access a specific value set during this execution
    customData = _execution.customData.get("key");

Related resources[](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data#related-resources)

--------------------------------------------------------------------------------------------------------------------------------------

*   [Understand executions](https://docs.n8n.io/build/understand-workflows/understand-executions)
    
*   [Manual, partial, and production executions](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions)
    
*   [View all executions](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions)
    
*   [View executions for a single workflow](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow)
    
*   [Debug and re-run past executions](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
    
*   [Stream real-time responses](https://docs.n8n.io/build/understand-workflows/understand-executions/stream-real-time-responses)
    
*   [Dirty nodes](https://docs.n8n.io/build/understand-workflows/understand-executions/understand-dirty-nodes)
    

[PreviousView all executions](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions)
[NextStream real-time responses](https://docs.n8n.io/build/understand-workflows/understand-executions/stream-real-time-responses)

Last updated 10 days ago

Was this helpful?