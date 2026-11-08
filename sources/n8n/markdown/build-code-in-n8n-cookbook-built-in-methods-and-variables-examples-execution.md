For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/execution.md)
.

`execution.id`[](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/execution#executionid)

-------------------------------------------------------------------------------------------------------------------------------

Contains the unique ID of the current workflow execution.

JavaScript

Python

Copy

    let executionId = $execution.id;

Copy

    executionId = _execution.id

`execution.resumeUrl`[](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/execution#executionresumeurl)

---------------------------------------------------------------------------------------------------------------------------------------------

The webhook URL to call to resume a [waiting](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait)
 workflow.

See the [Wait > On webhook call](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait#on-webhook-call)
 documentation to learn more.

`execution.resumeUrl` is available in workflows containing a Wait node, along with a node that waits for a webhook response.

`execution.customData`[](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/execution#executioncustomdata)

-----------------------------------------------------------------------------------------------------------------------------------------------

This is only available in the Code node.

JavaScript

Python

Copy

    // Set a single piece of custom execution data
    $execution.customData.set("key", "value");
    
    // Set the custom execution data object
    $execution.customData.setAll({"key1": "value1", "key2": "value2"})
    
    // Access the current state of the object during the execution
    var customData = $execution.customData.getAll()
    
    // Access a specific value set during this execution
    var customData = $execution.customData.get("key")

Copy

    # Set a single piece of custom execution data
    _execution.customData.set("key", "value");
    
    # Set the custom execution data object
    _execution.customData.setAll({"key1": "value1", "key2": "value2"})
    
    # Access the current state of the object during the execution
    customData = _execution.customData.getAll()
    
    # Access a specific value set during this execution
    customData = _execution.customData.get("key")

Refer to [Custom executions data](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
 for more information.

* * *

Related resources[](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/execution#related-resources)

----------------------------------------------------------------------------------------------------------------------------------------

*   [Built-in methods and variables examples](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples)
    

[PreviousBuilt-in methods and variables examples](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples)
[NextgetWorkflowStaticData](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/getworkflowstaticdata)

Last updated 10 days ago

Was this helpful?