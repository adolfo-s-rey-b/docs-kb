For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger.md)
.

The n8n Trigger node triggers when the workflow containing this node updates or gets published, or when the n8n instance starts or restarts. This node only responds to events in its own workflow; changes to other workflows won't trigger it.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger#node-parameters)

-----------------------------------------------------------------------------------------------------------------

The node includes a single parameter to identify the **Events** that should trigger it. Choose from these events:

*   **Published Workflow Updated**: If you select this event, the node triggers when the workflow containing this node is updated. Changes to other workflows won't trigger this node.
    
*   **Instance started**: If you select this event, the node triggers when the n8n instance starts or restarts.
    
*   **Workflow Published**: If you select this event, the node triggers when the workflow containing this node is published. Publishing other workflows won't trigger this node.
    

You can select one or more of these events.

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------------

[Browse n8n Trigger node documentation integration templates](https://n8n.io/integrations/n8n-trigger)
 or [search all templates](https://n8n.io/workflows/)

[Previousn8n Form](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger)
[NextNo Operation, do nothing](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.noop)

Last updated 10 days ago

Was this helpful?