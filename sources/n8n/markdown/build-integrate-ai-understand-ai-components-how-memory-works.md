For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-memory-works.md)
.

Memory is a key part of AI chat services. The memory keeps a history of previous messages, allowing for an ongoing conversation with the AI, rather than every interaction starting fresh.

AI memory in n8n[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-memory-works#ai-memory-in-n8n)

----------------------------------------------------------------------------------------------------------------------

To add memory to your AI workflow you can use either:

*   [Simple Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow)
    : stores a customizable length of chat history for the current session. This is the easiest to get started with.
    
*   One of the memory services that n8n provides nodes for. These include:
    
    *   [Motorhead](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead)
        
    *   [Redis Chat Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat)
        
    *   [Postgres Chat Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat)
        
    *   [Xata](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryxata)
        
    *   [Zep](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep)
        
    

If you need to do advanced AI memory management in your workflows, use the [Chat Memory Manager](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager)
 node.

This node is useful when you:

*   Can't add a memory node directly.
    
*   Need to do more complex memory management, beyond what the memory nodes offer. For example, you can add this node to check the memory size of the Agent node's response, and reduce it if needed.
    
*   Want to inject messages to the AI that look like user messages, to give the AI more context.
    

Related resources[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-memory-works#related-resources)

------------------------------------------------------------------------------------------------------------------------

*   [Understand AI components](https://docs.n8n.io/build/integrate-ai/understand-ai-components)
    
*   [What chains do](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-chains-do)
    
*   [What agents do](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-agents-do)
    
*   [How tools work](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-tools-work)
    
*   [Store and search data with vectors](https://docs.n8n.io/build/integrate-ai/understand-ai-components/store-and-search-data-with-vectors)
    
*   [Retrieve relevant context](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context)
    
*   [Agents vs chains](https://docs.n8n.io/build/integrate-ai/understand-ai-components/agents-vs-chains)
    

[PreviousWhat agents do](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-agents-do)
[NextHow tools work](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-tools-work)

Last updated 10 days ago

Was this helpful?