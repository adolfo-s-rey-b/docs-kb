For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/flow-logic/understand-execution-order.md)
.

Execution order is part of your workflow's [flow logic](https://docs.n8n.io/build/flow-logic)
, and matters most in workflows that [split into multiple branches](https://docs.n8n.io/build/flow-logic/split-with-conditionals)
.

n8n's node execution order depends on the version of n8n you're using:

*   For workflows created before n8n 1.0: n8n executes the first node of each branch, then the second node of each branch, and so on.
    
*   For workflows created from n8n 1.0: executes each branch in turn, completing one branch before starting another. n8n orders the branches based on their position on the canvas, from topmost to bottommost. If two branches are at the same height, the leftmost branch executes first.
    

You can change the execution order in your [workflow settings](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings)
.

Related resources[](https://docs.n8n.io/build/flow-logic/understand-execution-order#related-resources)

-------------------------------------------------------------------------------------------------------

*   [Flow logic](https://docs.n8n.io/build/flow-logic)
    
*   [Split with conditionals](https://docs.n8n.io/build/flow-logic/split-with-conditionals)
    
*   [Merge data](https://docs.n8n.io/build/flow-logic/merge-data)
    
*   [Loop](https://docs.n8n.io/build/flow-logic/loop)
    
*   [Wait](https://docs.n8n.io/build/flow-logic/wait)
    
*   [Break workflows into smaller parts](https://docs.n8n.io/build/flow-logic/break-workflows-into-smaller-parts)
    
*   [Convert to sub-workflows](https://docs.n8n.io/build/flow-logic/convert-to-sub-workflows)
    
*   [Handle errors gracefully](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully)
    

[PreviousHandle errors gracefully](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully)
[NextWork with data](https://docs.n8n.io/build/work-with-data)

Last updated 10 days ago

Was this helpful?