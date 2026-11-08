For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout.md)
.

Use the Split Out node to separate a single data item containing a list into multiple items. For example, a list of customers, and you want to split them so that you have an item for each customer.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout#node-parameters)

---------------------------------------------------------------------------------------------------------------

Configure this node using the following parameters.

### Field to Split Out[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout#field-to-split-out)

Enter the field containing the list you want to separate out into individual items.

If you're working with binary data inputs, use `$binary` in an expression to set the field to split out.

### Include[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout#include)

Select whether and how you want n8n to keep any other fields from the input data with each new individual item.

You can select:

*   **No Other Fields**: No other fields will be included.
    
*   **All Other Fields**: All other fields will be included.
    
*   **Selected Other Fields**: Only the selected fields will be included.
    
    *   **Fields to Include**: Enter a comma separated list of the fields you want to include.
        
    

Node options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout#node-options)

---------------------------------------------------------------------------------------------------------

### Disable Dot Notation[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout#disable-dot-notation)

By default, n8n enables dot notation to reference child fields in the format `parent.child`. Use this option to disable dot notation (turned on) or to continue using dot (turned off).

### Destination Field Name[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout#destination-field-name)

Enter the field in the output where the split field contents should go.

### Include Binary[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout#include-binary)

Choose whether to include binary data from the input in the new output (turned on) or not (turned off).

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------

[Browse Split Out integration templates](https://n8n.io/integrations/split-out)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout#related-resources)

-------------------------------------------------------------------------------------------------------------------

Learn more about [data structure and data flow](https://docs.n8n.io/build/work-with-data)
 in n8n workflows.

[PreviousSort](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort)
[NextSSE Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssetrigger)

Last updated 10 days ago

Was this helpful?