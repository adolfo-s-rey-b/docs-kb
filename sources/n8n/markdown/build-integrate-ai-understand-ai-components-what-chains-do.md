For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-chains-do.md)
.

Chains bring together different components of AI to create a cohesive system. They set up a sequence of calls between the components. These components can include models and memory (though note that in n8n chains can't use memory).

Chains in n8n[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-chains-do#chains-in-n8n)

--------------------------------------------------------------------------------------------------------------

n8n provides three chain nodes:

*   [Basic LLM Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm)
    : use to interact with an LLM, without any additional components.
    
*   [Question and Answer Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa)
    : can connect to a vector store using a retriever, or to an n8n workflow using the Workflow Retriever node. Use this if you want to create a workflow that supports asking questions about specific documents.
    
*   [Summarization Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization)
    : takes an input and returns a summary.
    

There's an important difference between chains in n8n and in other tools such as LangChain: none of the chain nodes support memory. This means they can't remember previous user queries. If you use LangChain to code an AI application, you can give your application memory. In n8n, if you need your workflow to support memory, use an agent. This is essential if you want users to be able to have a natural ongoing conversation with your app.

Related resources[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-chains-do#related-resources)

----------------------------------------------------------------------------------------------------------------------

*   [Understand AI components](https://docs.n8n.io/build/integrate-ai/understand-ai-components)
    
*   [What agents do](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-agents-do)
    
*   [How memory works](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-memory-works)
    
*   [How tools work](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-tools-work)
    
*   [Store and search data with vectors](https://docs.n8n.io/build/integrate-ai/understand-ai-components/store-and-search-data-with-vectors)
    
*   [Retrieve relevant context](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context)
    
*   [Agents vs chains](https://docs.n8n.io/build/integrate-ai/understand-ai-components/agents-vs-chains)
    

[PreviousUnderstand AI components](https://docs.n8n.io/build/integrate-ai/understand-ai-components)
[NextWhat agents do](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-agents-do)

Last updated 10 days ago

Was this helpful?