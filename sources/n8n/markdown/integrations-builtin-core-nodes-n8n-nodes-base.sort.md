For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort.md)
.

Use the Sort node to organize lists of items in a desired ordering, or generate a random selection.

**Array sort behavior**

The Sort operation uses the default JavaScript operation where the elements to be sorted are converted into strings and their values compared. Refer to [Mozilla's guide to Array sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
 to learn more.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort#node-parameters)

-----------------------------------------------------------------------------------------------------------

Configure this node using the **Type** parameter.

Use the dropdown to select how you want to input the sorting from these options.

### Simple[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort#simple)

Performs an ascending or descending sort using the selected fields.

When you select this **Type**:

*   Use the **Add Field To Sort By** button to input the **Field Name**.
    
*   Select whether to use **Ascending** or **Descending** order.
    

#### Simple options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort#simple-options)

When you select **Simple** as the **Type**, you have the option to **Disable Dot Notation**. By default, n8n enables dot notation to reference child fields in the format `parent.child`. Use this option to disable dot notation (turned on) or to continue using dot (turned off).

### Random[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort#random)

Creates a random order in the list.

### Code[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort#code)

Input custom JavaScript code to perform the sort operation. This is a good option if a simple sort won't meet your needs.

Enter your custom JavaScript code in the **Code** input field.

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------

[Browse Sort integration templates](https://n8n.io/integrations/sort)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort#related-resources)

---------------------------------------------------------------------------------------------------------------

Learn more about [data structure and data flow](https://docs.n8n.io/build/work-with-data)
 in n8n workflows.

[PreviousSend Email](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail)
[NextSplit Out](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout)

Last updated 10 days ago

Was this helpful?