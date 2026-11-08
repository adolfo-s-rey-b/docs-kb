For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/flow-logic/split-with-conditionals.md)
.

Splitting uses the [IF](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if)
 or [Switch](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch)
 nodes. It turns a single-branch workflow into a multi-branch workflow. This is a key piece of n8n's [flow logic](https://docs.n8n.io/build/flow-logic)
.

Compare these workflows:

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-572d0272265d8eab310b22f44de81a583e4bc9e5%252Fsingle-multi-branch-workflow.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=0332eaa9448aa80b42af7ab4c152a750&sv=3)

Diagram comparing a linear bug-report workflow with one that branches by urgency and support plan

The first workflow is linear: a user submits a bug and the workflow emails support. The second workflow starts the same way but splits depending on whether the user marked the issue urgent, then splits again by the user's support plan.

This is the power of splitting and conditional nodes in n8n.

Refer to the [IF](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if)
 or [Switch](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch)
 documentation for usage details.

After splitting, you can [merge the branches back together](https://docs.n8n.io/build/flow-logic/merge-data)
. The [execution order](https://docs.n8n.io/build/flow-logic/understand-execution-order)
 of a multi-branch workflow depends on how you arrange the branches on the canvas.

Related resources[](https://docs.n8n.io/build/flow-logic/split-with-conditionals#related-resources)

----------------------------------------------------------------------------------------------------

*   [Flow logic](https://docs.n8n.io/build/flow-logic)
    
*   [Merge data](https://docs.n8n.io/build/flow-logic/merge-data)
    
*   [Loop](https://docs.n8n.io/build/flow-logic/loop)
    
*   [Wait](https://docs.n8n.io/build/flow-logic/wait)
    
*   [Understand execution order](https://docs.n8n.io/build/flow-logic/understand-execution-order)
    
*   [Break workflows into smaller parts](https://docs.n8n.io/build/flow-logic/break-workflows-into-smaller-parts)
    
*   [Convert to sub-workflows](https://docs.n8n.io/build/flow-logic/convert-to-sub-workflows)
    
*   [Handle errors gracefully](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully)
    

[PreviousFlow logic](https://docs.n8n.io/build/flow-logic)
[NextMerge data](https://docs.n8n.io/build/flow-logic/merge-data)

Last updated 10 days ago

Was this helpful?