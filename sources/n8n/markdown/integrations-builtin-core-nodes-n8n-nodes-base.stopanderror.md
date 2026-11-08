For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror.md)
.

Use the Stop And Error node to display custom error messages, cause executions to fail under certain conditions, and send custom error information to error workflows.

Operations[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror#operations)

---------------------------------------------------------------------------------------------------------

*   Error Message
    
*   Error Object
    

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror#node-parameters)

-------------------------------------------------------------------------------------------------------------------

Both operations include one node parameter, the **Error Type**. Use this parameter to select the type of error to throw. Choose between the two operations: **Error Message** and **Error Object**.

The other parameters depend on which operation you select.

### Error Message parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror#error-message-parameters)

The Error Message Error Type adds one parameter, the **Error Message** field. Enter the message you'd like to throw.

### Error Object parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror#error-object-parameters)

The Error Object Error Type adds one parameter, the **Error Object**. Enter a JSON object that contains the error properties you'd like to throw.

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------

[Browse Stop And Error integration templates](https://n8n.io/integrations/stop-and-error)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror#related-resources)

-----------------------------------------------------------------------------------------------------------------------

You can use the Stop And Error node with the [Error trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger)
 node.

Read more about [Error workflows](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully)
 in n8n workflows.

[PreviousSSH](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh)
[NextSummarize](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.summarize)

Last updated 10 days ago

Was this helpful?