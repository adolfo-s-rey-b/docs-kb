For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/understand-workflows/understand-executions/stream-real-time-responses.md)
.

**Feature availability**

Available on all plans.

Streaming responses let you send data back to users as an AI Agent node generates it. This is useful for chatbots, where you want to show the user the answer as it's generated to provide a better user experience.

You can enable streaming using either:

*   The [Chat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger)
    
*   The [Webhook node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook)
    

In both cases, set the node's **Response Mode** to **Streaming**.

Configure nodes for streaming[](https://docs.n8n.io/build/understand-workflows/understand-executions/stream-real-time-responses#configure-nodes-for-streaming)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

To stream data, you need to add nodes to the workflow that support streaming output. Not all nodes support this feature.

1.  Choose a node that supports streaming, such as:
    
    *   [AI agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
        
    *   [Respond to Webhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook)
        
    
2.  You can disable streaming in the options of these nodes. By default, they stream data whenever the executed trigger has its `Response Mode` set to `Streaming response`.
    

Important information[](https://docs.n8n.io/build/understand-workflows/understand-executions/stream-real-time-responses#important-information)

-----------------------------------------------------------------------------------------------------------------------------------------------

Keep in mind the following details when configuring streaming responses:

*   **Trigger**: Your trigger node must support streaming and have streaming configured. Without this, the workflow behaves according to your response mode settings.
    
*   **Node configuration**: Even with streaming enabled on the trigger, you need at least one node configured to stream data. Otherwise, your workflow will send no data.
    

Related resources[](https://docs.n8n.io/build/understand-workflows/understand-executions/stream-real-time-responses#related-resources)

---------------------------------------------------------------------------------------------------------------------------------------

*   [Understand executions](https://docs.n8n.io/build/understand-workflows/understand-executions)
    
*   [Manual, partial, and production executions](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions)
    
*   [View all executions](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions)
    
*   [View executions for a single workflow](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow)
    
*   [Debug and re-run past executions](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
    
*   [Customize executions data](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
    
*   [Dirty nodes](https://docs.n8n.io/build/understand-workflows/understand-executions/understand-dirty-nodes)
    

[PreviousCustomize executions data](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
[NextCreate and run workflows](https://docs.n8n.io/build/understand-workflows/create-and-run-workflows)

Last updated 10 days ago

Was this helpful?