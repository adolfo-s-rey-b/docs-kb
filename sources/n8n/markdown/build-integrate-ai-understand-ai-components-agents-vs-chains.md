For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/integrate-ai/understand-ai-components/agents-vs-chains.md)
.

In this workflow you can choose whether your chat query goes to an agent or chain. It shows some of the ways that agents are more powerful than chains.

spinner

Key features[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/agents-vs-chains#key-features)

--------------------------------------------------------------------------------------------------------------

This workflow uses:

*   [Chat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger)
    : start your workflow and respond to user chat interactions. The node provides a customizable chat interface.
    
*   [Switch node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch)
    : directs your query to either the agent or chain, depending on which you specify in your query. If you say "agent" it sends it to the agent. If you say "chain" it sends it to the chain.
    
*   [Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
    : the Agent node interacts with other components of the workflow and makes decisions about what tools to use.
    
*   [Basic LLM Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm)
    : the Basic LLM Chain node supports chatting with a connected LLM, but doesn't support memory or tools.
    

Using the example[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/agents-vs-chains#using-the-example)

------------------------------------------------------------------------------------------------------------------------

To load the template into your n8n instance:

1.  Download the workflow JSON file.
    
2.  Open a new workflow in your n8n instance.
    
3.  Copy in the JSON, or select **Workflow menu** ![Workflow menu icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2738857267-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FGixZThfitWP21x2gQFpD%252Fuploads%252Fgit-blob-513566d28f893c602d89d96c0a06037329725e61%252Fthree-dots-horizontal.png%3Falt%3Dmedia&width=54&dpr=3&quality=100&sign=0d48cb7a502e001d3f9694f0a8b239bf&sv=3) > **Import from file...**.
    

The example workflows use Sticky Notes to guide you:

*   Yellow: notes and information.
    
*   Green: instructions to run the workflow.
    
*   Orange: you need to change something to make the workflow work.
    
*   Blue: draws attention to a key feature of the example.
    

Related resources[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/agents-vs-chains#related-resources)

------------------------------------------------------------------------------------------------------------------------

*   [Understand AI components](https://docs.n8n.io/build/integrate-ai/understand-ai-components)
    
*   [What chains do](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-chains-do)
    
*   [What agents do](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-agents-do)
    
*   [How memory works](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-memory-works)
    
*   [How tools work](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-tools-work)
    
*   [Store and search data with vectors](https://docs.n8n.io/build/integrate-ai/understand-ai-components/store-and-search-data-with-vectors)
    
*   [Retrieve relevant context](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context)
    

[PreviousRetrieve relevant context](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context)
[NextLangChain in n8n](https://docs.n8n.io/build/integrate-ai/langchain-in-n8n)

Last updated 10 days ago

Was this helpful?