For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-agents-do.md)
.

One way to think of an agent is as a [chain](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-chains-do)
 that knows how to make decisions. Where a chain follows a predetermined sequence of calls to different AI components, an agent uses a language model to determine which actions to take.

Agents are the part of AI that act as decision-makers. They can interact with other agents and tools. When you send a query to an agent, it tries to choose the best tools to use to answer. Agents adapt to your specific queries, as well as the prompts that configure their behavior.

Agents in n8n[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-agents-do#agents-in-n8n)

--------------------------------------------------------------------------------------------------------------

n8n provides one Agent node, which can act as different types of agent depending on the settings you choose. Refer to the [Agent node documentation](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
 for details on the available agent types.

When you execute a workflow containing an agent, the agent runs multiple times. For example, it may do an initial setup, followed by a run to call a tool, then another run to evaluate the tool response and respond to the user.

Related resources[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-agents-do#related-resources)

----------------------------------------------------------------------------------------------------------------------

*   [Understand AI components](https://docs.n8n.io/build/integrate-ai/understand-ai-components)
    
*   [What chains do](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-chains-do)
    
*   [How memory works](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-memory-works)
    
*   [How tools work](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-tools-work)
    
*   [Store and search data with vectors](https://docs.n8n.io/build/integrate-ai/understand-ai-components/store-and-search-data-with-vectors)
    
*   [Retrieve relevant context](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context)
    
*   [Agents vs chains](https://docs.n8n.io/build/integrate-ai/understand-ai-components/agents-vs-chains)
    

[PreviousWhat chains do](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-chains-do)
[NextHow memory works](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-memory-works)

Last updated 10 days ago

Was this helpful?