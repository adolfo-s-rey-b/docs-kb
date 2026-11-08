For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executiondata.md)
.

Use this node to save metadata for workflow executions. You can then search by this data in the **Executions** list.

You can retrieve custom execution data during workflow execution using the Code node. Refer to [Custom executions data](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
 for more information.

**Feature availability**

Custom executions data is available on:

*   **n8n Cloud:** Pro, Enterprise
    
*   **Self-hosted:** Registered Community, Enterprise
    

Operations[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executiondata#operations)

----------------------------------------------------------------------------------------------------------

*   Save Execution Data for Search
    

Data to Save[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executiondata#data-to-save)

--------------------------------------------------------------------------------------------------------------

Add a **Saved Field** for each key/value pair of metadata you'd like to save.

Limitations[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executiondata#limitations)

------------------------------------------------------------------------------------------------------------

The Execution Data node has the following restrictions when storing execution metadata:

*   `key`: limited to 50 characters
    
*   `value`: limited to 512 characters
    

If either the `key` or `value` exceed the above limitations, n8n truncates to their maximum length and outputs a log entry.

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executiondata#templates-and-examples)

----------------------------------------------------------------------------------------------------------------------------------

[Browse Execution Data integration templates](https://n8n.io/integrations/execution-data)
 or [search all templates](https://n8n.io/workflows/)

[PreviousExecute Sub-workflow Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger)
[NextExtract From File](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile)

Last updated 10 days ago

Was this helpful?