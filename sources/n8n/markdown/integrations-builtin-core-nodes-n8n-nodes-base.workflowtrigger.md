For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.workflowtrigger.md)
.

The Workflow Trigger node gets triggered when a workflow is updated or activated.

**Feature availability**

The Workflow Trigger node is deprecated from n8n 1.64.0. n8n moved its functionality to the [n8n Trigger node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger)
. Refer to [Deprecated and versioned nodes](https://docs.n8n.io/integrations/builtin/deprecated-nodes)
 for more information.

**Keep in mind**

If you want to use the Workflow Trigger node for a workflow, add the node to the workflow. You don't have to create a separate workflow.

The Workflow Trigger node gets triggered for the workflow that it gets added to. You can use the Workflow Trigger node to trigger a workflow to notify the state of the workflow.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.workflowtrigger#node-parameters)

----------------------------------------------------------------------------------------------------------------------

The node includes a single parameter to identify the **Events** that should trigger it. Choose from these events:

*   **Active Workflow Updated**: If you select this event, the node triggers when this workflow is updated.
    
*   **Workflow Activated**: If you select this event, the node triggers when this workflow is activated.
    

You can select one or both of these events.

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.workflowtrigger#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------------------

[Browse Workflow Trigger node documentation integration templates](https://n8n.io/integrations/workflow-trigger)
 or [search all templates](https://n8n.io/workflows/)

[PreviousCommon issues](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/common-issues)
[NextXML](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.xml)

Last updated 10 days ago

Was this helpful?