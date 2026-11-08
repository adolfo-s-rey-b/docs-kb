For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.limit.md)
.

Use the Limit node to remove items beyond a defined maximum number. You can choose whether n8n takes the items from the beginning or end of the input data.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.limit#node-parameters)

------------------------------------------------------------------------------------------------------------

Configure this node using the following parameters.

### Max Items[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.limit#max-items)

Enter the maximum number of items that n8n should keep. If the input data contains more than this value, n8n removes the items.

### Keep[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.limit#keep)

If the node has to remove items, select where it keeps the input items from:

*   **First Items**: Keeps the **Max Items** number of items from the beginning of the input data.
    
*   **Last Items**: Keeps the **Max Items** number of items from the end of the input data.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.limit#templates-and-examples)

--------------------------------------------------------------------------------------------------------------------------

[Browse Limit integration templates](https://n8n.io/integrations/limit)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.limit#related-resources)

----------------------------------------------------------------------------------------------------------------

Learn more about [data structure and data flow](https://docs.n8n.io/build/work-with-data)
 in n8n workflows.

[PreviousLDAP](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ldap)
[NextLocal File Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger)

Last updated 10 days ago

Was this helpful?