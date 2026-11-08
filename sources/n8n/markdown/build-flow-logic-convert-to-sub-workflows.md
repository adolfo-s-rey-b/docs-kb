For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/flow-logic/convert-to-sub-workflows.md)
.

**Feature availability**

Sub-workflow conversion is available from n8n 1.97.0.

Use sub-workflow conversion to refactor your workflows into reusable parts, as part of your workflow's [flow logic](https://docs.n8n.io/build/flow-logic)
. Expressions referencing other nodes are automatically updated and added as parameters in the [Execute Workflow Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger)
 node.

See [sub-workflows](https://docs.n8n.io/build/flow-logic/break-workflows-into-smaller-parts)
 for a general introduction to the concept.

Selecting nodes for a sub-workflow[](https://docs.n8n.io/build/flow-logic/convert-to-sub-workflows#selecting-nodes-for-a-sub-workflow)

---------------------------------------------------------------------------------------------------------------------------------------

To convert part of a workflow to a sub-workflow, you must select the nodes in the original workflow that you want to convert.

Do this by selecting a group of valid nodes. The selection must be continuous and must connect to the rest of the workflow from at most one start node and one end node. The selection must fulfill these conditions:

*   Must not include trigger nodes.
    
*   Only a single node in the selection can have incoming connections from nodes _outside_ of the selection.
    
    *   That node can have multiple incoming connections, but only a single input _branch_ (which means it can't be a [Merge node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.merge)
         for example).
        
    *   That node can't have incoming connections from other nodes in the selection.
        
    
*   Only a single node in the selection can have outgoing connections to nodes _outside_ of the selection.
    
    *   That node can have multiple outgoing connections, but only a single output branch (it can't be an [If node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if)
         for example).
        
    *   That node can't have outgoing connections to other nodes in the selection.
        
    
*   The selection must include all nodes between the input and output nodes.
    

How to convert part of a workflow to a sub-workflow[](https://docs.n8n.io/build/flow-logic/convert-to-sub-workflows#how-to-convert-part-of-a-workflow-to-a-sub-workflow)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Select the desired nodes on the canvas. Right-click the canvas background and select **Convert to sub-workflow**.

Things to keep in mind[](https://docs.n8n.io/build/flow-logic/convert-to-sub-workflows#things-to-keep-in-mind)

---------------------------------------------------------------------------------------------------------------

Most sub-workflow conversions work without issues, but there are some caveats and limitations to keep in mind:

*   **You must set type constraints for input and output manually**: By default, sub-workflow input and output allow all types. You can set expected types in sub-workflow's [Execute Sub-workflow Trigger node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger)
     and [Edit Fields (set) node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set)
     (labeled as **Return** and only included if the sub-workflow has outputs).
    
*   **Limited support for AI nodes**: When dealing with sub-nodes like AI tools, you must select them all and may need to duplicate any nodes shared with other AI Agents before conversion.
    
*   **Uses v1 execution ordering:** New workflows use [`v1` execution ordering](https://docs.n8n.io/build/flow-logic/understand-execution-order)
     regardless of the parent workflow's settings - you can change this back in the settings.
    
*   **Accessor functions like** `**first()**`**,** `**last()**`**, and** `**all()**` **require extra care**: Expressions using these functions don't always translate cleanly to a sub-workflow context. n8n may transform them to try to preserve their functionality, but you should check that they work as intended in their new context.
    
    **Sub-node parameter suffixes**
    
    n8n adds suffixes like `_firstItem`, `_lastItem`, and `_allItems` to variable names accessed by these functions. This helps preserve information about the original expression, since item ordering may be different in the sub-workflow context.
    
*   **The** `**itemMatching**` **function requires a fixed index**: You can't use expressions for the index value when using the [`itemMatching` function](https://docs.n8n.io/build/work-with-data/reference-data/reference-previous-nodes)
    . You must pass it a fixed number.
    

Related resources[](https://docs.n8n.io/build/flow-logic/convert-to-sub-workflows#related-resources)

-----------------------------------------------------------------------------------------------------

*   [Flow logic](https://docs.n8n.io/build/flow-logic)
    
*   [Split with conditionals](https://docs.n8n.io/build/flow-logic/split-with-conditionals)
    
*   [Merge data](https://docs.n8n.io/build/flow-logic/merge-data)
    
*   [Loop](https://docs.n8n.io/build/flow-logic/loop)
    
*   [Wait](https://docs.n8n.io/build/flow-logic/wait)
    
*   [Understand execution order](https://docs.n8n.io/build/flow-logic/understand-execution-order)
    
*   [Break workflows into smaller parts](https://docs.n8n.io/build/flow-logic/break-workflows-into-smaller-parts)
    
*   [Handle errors gracefully](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully)
    

[PreviousBreak workflows into smaller parts](https://docs.n8n.io/build/flow-logic/break-workflows-into-smaller-parts)
[NextHandle errors gracefully](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully)

Last updated 10 days ago

Was this helpful?