For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if.md)
.

Use the If node to split a workflow conditionally based on comparison operations.

Add conditions[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if#add-conditions)

-------------------------------------------------------------------------------------------------------

Create comparison **Conditions** for your If node.

*   Use the data type dropdown to select the data type and comparison operation type for your condition. For example, to filter for dates after a particular date, select **Date & Time > is after**.
    
*   The fields and values to enter into the condition change based on the data type and comparison you select. Refer to [Available data type comparisons](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if#available-data-type-comparisons)
     for a full list of all comparisons by data type.
    

Select **Add condition** to create more conditions.

### Combining conditions[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if#combining-conditions)

You can choose to keep data:

*   When it meets all conditions: Create two or more conditions and select **AND** in the dropdown between them.
    
*   When it meets any of the conditions: Create two or more conditions and select **OR** in the dropdown between them.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------

[Browse If integration templates](https://n8n.io/integrations/if)
 or [search all templates](https://n8n.io/workflows/)

Branch execution with If and Merge nodes[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if#branch-execution-with-if-and-merge-nodes)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

**0.236.0 and below**

n8n removed this execution behavior in n8n 1.0. This section applies to workflows using the **v0 (legacy)** workflow execution order. By default, this is all workflows built before n8n 1.0. You can change the execution order in your [workflow settings](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings)
.

If you add a Merge node to a workflow containing an If node, it can result in both output data streams of the If node executing.

One data stream triggers the Merge node, which then goes and executes the other data stream.

For example, in the screenshot below there's a workflow containing an Edit Fields node, If node, and Merge node. The standard If node behavior is to execute one data stream (in the screenshot, this is the **true** output). However, due to the Merge node, both data streams execute, despite the If node not sending any data down the **false** data stream.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2738857267-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FGixZThfitWP21x2gQFpD%252Fuploads%252Fgit-blob-fa1e5ef610cdcb3524176705af7aed6a50a50cda%252Fif-merge-node.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a85c50d72955e627e82f672948c0e8bd&sv=3)

A workflow with an Edit Fields node, an If node, and a Merge node connected in sequence

Related resources[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if#related-resources)

-------------------------------------------------------------------------------------------------------------

Refer to [Splitting with conditionals](https://docs.n8n.io/build/flow-logic/split-with-conditionals)
 for more information on using conditionals to create complex logic in n8n.

If you need more than two conditional outputs, use the [Switch node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch)
.

### Available data type comparisons[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if#available-data-type-comparisons)

#### String[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if#string)

String data type supports these comparisons:

*   exists
    
*   does not exist
    
*   is empty
    
*   is not empty
    
*   is equal to
    
*   is not equal to
    
*   contains
    
*   does not contain
    
*   starts with
    
*   does not start with
    
*   ends with
    
*   does not end with
    
*   matches regex
    
*   does not match regex
    

#### Number[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if#number)

Number data type supports these comparisons:

*   exists
    
*   does not exist
    
*   is empty
    
*   is not empty
    
*   is equal to
    
*   is not equal to
    
*   is greater than
    
*   is less than
    
*   is greater than or equal to
    
*   is less than or equal to
    

#### Date & Time[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if#date-and-time)

Date & Time data type supports these comparisons:

*   exists
    
*   does not exist
    
*   is empty
    
*   is not empty
    
*   is equal to
    
*   is not equal to
    
*   is after
    
*   is before
    
*   is after or equal to
    
*   is before or equal to
    

#### Boolean[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if#boolean)

Boolean data type supports these comparisons:

*   exists
    
*   does not exist
    
*   is empty
    
*   is not empty
    
*   is true
    
*   is false
    
*   is equal to
    
*   is not equal to
    

#### Array[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if#array)

Array data type supports these comparisons:

*   exists
    
*   does not exist
    
*   is empty
    
*   is not empty
    
*   contains
    
*   does not contain
    
*   length equal to
    
*   length not equal to
    
*   length greater than
    
*   length less than
    
*   length greater than or equal to
    
*   length less than or equal to
    

#### Object[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if#object)

Object data type supports these comparisons:

*   exists
    
*   does not exist
    
*   is empty
    
*   is not empty
    

[PreviousCommon Issues](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/common-issues)
[NextJWT](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt)

Last updated 10 days ago

Was this helpful?