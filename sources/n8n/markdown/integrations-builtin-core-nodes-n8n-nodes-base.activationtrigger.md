For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.activationtrigger.md)
.

The Activation Trigger node gets triggered when an event gets fired by n8n or a workflow.

**Feature availability**

The Activation Trigger node is deprecated from n8n 0.117.0. It was replaced with two new nodes: the [n8n Trigger node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger)
 and the [Workflow Trigger node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.workflowtrigger)
. For more details, check out the entry in the [breaking changes](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md#01170)
 page, and see [Deprecated and versioned nodes](https://docs.n8n.io/integrations/builtin/deprecated-nodes)
.

**Keep in mind**

If you want to use the Activation Trigger node for a workflow, add the node to the workflow. You don't have to create a separate workflow.

The Activation Trigger node gets triggered for the workflow that it gets added to. You can use the Activation Trigger node to trigger a workflow to notify the state of the workflow.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.activationtrigger#node-parameters)

------------------------------------------------------------------------------------------------------------------------

*   Events
    
    *   **Activation**: Run when the workflow gets published
        
    *   **Start**: Run when n8n starts or restarts
        
    *   **Update**: Run when the workflow gets saved while it's active
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.activationtrigger#templates-and-examples)

--------------------------------------------------------------------------------------------------------------------------------------

[Browse Activation Trigger node documentation integration templates](https://n8n.io/integrations/activation-trigger)
 or [search all templates](https://n8n.io/workflows/)

[PreviousCore nodes](https://docs.n8n.io/integrations/builtin/core-nodes)
[NextAggregate](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.aggregate)

Last updated 10 days ago

Was this helpful?