For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/fix-common-issues.md)
.

Combining multiple triggers[](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/fix-common-issues#combining-multiple-triggers)

--------------------------------------------------------------------------------------------------------------------------------------------------

If you have another trigger in the workflow already, you have two potential starting points: that trigger and the [evaluation trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.evaluationtrigger)
. To make sure your workflow works as expected no matter which trigger executes, you will need to merge these branches together.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-bf42d36caace51c61a703fe9c79ca19e9fe472e8%252Fmerging-trigger-branches.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=77cfdbde5d5fca265cc96488346a837e&sv=3)

Logic to merge two trigger branches together so that they have the same data format and can be referenced from a single node.

To do so:

1.  **Get the data format of the other trigger**:
    
    *   Execute the other trigger.
        
    *   Open it and navigate to the JSON view of its output pane.
        
    *   Click the **copy** button on the right.
        
    
2.  **Re-shape the evaluation trigger data to match**:
    
    *   Insert an [Edit Fields (Set) node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set)
         after the evaluation trigger and connect them together.
        
    *   Change its mode to **JSON**.
        
    *   Paste your data into the 'JSON' field, removing the `[` and `]` on the first and last lines.
        
    *   Switch the field type to **Expression**.
        
    *   Map in the data from the trigger by dragging it from the input pane.
        
    *   For strings, make sure to replace the entire value (including the quotes) and add `.toJsonString()` to the end of the expression.
        
    
3.  **Merge the branches using a 'No-op' node**: Insert a [No-op node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.noop)
     and wire both the other trigger and the Set node up to it. The 'No-op' node just outputs whatever input it receives.
    
4.  **Reference the 'No-op' node outputs in the rest of the workflow**: Since both paths will flow through this node with the same format, you can be sure that your input data will always be there.
    

Avoiding evaluation breaking the chat[](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/fix-common-issues#avoiding-evaluation-breaking-the-chat)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

n8n's internal chat reads the output data of the last executed node in the workflow. After adding an evaluation node with the ['set outputs' operation](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.evaluation#set-outputs)
, this data may not be in the expected format, or even contain the chat response.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-f3a44f174756eb6c6c9ce027b0d9867ecb4fa891%252Fadd-second-output-branch.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=954b12ff39473283a3077ff4e868a1df&sv=3)

Agent node with a second output branch wired to a No-op node, positioned to execute last

The solution is to add an extra branch coming out of your agent. [Lower branches execute later](https://docs.n8n.io/build/flow-logic/understand-execution-order)
 in n8n, which means any node you attach to this branch will execute last. You can use a no-op node here since it only needs to pass the agent output through.

Accessing tool data when calculating metrics[](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/fix-common-issues#accessing-tool-data-when-calculating-metrics)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes you need to know what happened in executed sub-nodes of an agent, for example to check whether it executed a tool. You can't reference these nodes directly with expressions, but you can enable the **Return intermediate steps** option in the agent. This will add an extra output field called `intermediateSteps` which you can use in later nodes:

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-2f8a0dbbcbbe7a3d5c626889ab8c536584c4e1f8%252Fenable-return-intermediate-steps.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f123a1ee976893d289a0ae3fc70c4080&sv=3)

Enable return intermediate steps

Multiple evaluations in the same workflow[](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/fix-common-issues#multiple-evaluations-in-the-same-workflow)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can only have one evaluation set up per workflow. In other words, you can only have one evaluation trigger per workflow.

Even so, you can still test different parts of your workflow with different evaluations by putting those parts in [sub-workflows](https://docs.n8n.io/build/flow-logic/break-workflows-into-smaller-parts)
 and evaluating each sub-workflow.

Dealing with inconsistent results[](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/fix-common-issues#dealing-with-inconsistent-results)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

Metrics can often have noise: they may be different across evaluation runs of the exact same workflow. This is because the workflow itself may return different results, or any LLM-based metrics might have natural variation in them.

You can compensate for this by duplicating the rows of your dataset, so that each row appears more than once in the dataset. Since this means that each input will effectively be running multiple times, it will smooth out any variations.

Related resources[](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/fix-common-issues#related-resources)

------------------------------------------------------------------------------------------------------------------------------

*   [Test and improve AI workflows](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows)
    
*   [Understand why to test](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/understand-why-to-test)
    
*   [Run quick evaluations](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/run-quick-evaluations)
    
*   [Use metrics to measure quality](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality)
    

[PreviousUse metrics to measure quality](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality)
[NextAI examples](https://docs.n8n.io/build/integrate-ai/ai-examples)

Last updated 10 days ago

Was this helpful?