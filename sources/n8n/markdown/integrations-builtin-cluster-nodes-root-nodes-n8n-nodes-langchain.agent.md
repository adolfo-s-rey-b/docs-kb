For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent.md)
.

The AI Agent node lets you build an AI agent in n8n. Connect a chat model and one or more tools, and the agent decides which tools to call to complete a task.

An AI agent is an autonomous system that receives data, makes rational decisions, and acts within its environment to achieve specific goals. The AI agent's environment is everything the agent can access that isn't the agent itself. This agent uses external tools and APIs to perform actions and retrieve information. It can understand the capabilities of different tools and determine which tool to use depending on the task.

**Connect a tool**

You must connect at least one tool [sub-node](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes)
 to an AI Agent node.

**Feature availability**

The AI Agent node's agent type setting is deprecated from n8n 1.82.0. All AI Agent nodes now work as a `Tools Agent`, which was the recommended and most frequently used setting. Workflows or templates using an older AI Agent node set to `Tools Agent` continue to work as expected.

The version of the node (v1) that has the agent type setting **will be removed from n8n 3.0**. If you're using v1 of the AI Agent node, update to the latest version. For use cases like an SQL Agent, use a Postgres/MySQL tool sub-node with a recent Agent node instead.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------

[Browse n8n-nodes-langchain.agent integration templates](https://n8n.io/integrations/agent)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's documentation on agents](https://docs.langchain.com/oss/javascript/langchain/agents)
 for more information about the service.

New to AI Agents? Read the [n8n blog introduction to AI agents](https://blog.n8n.io/ai-agents/)
.

To connect a registry MCP server as a tool with one click, see [MCP servers](https://docs.n8n.io/build/integrate-ai/mcp-servers)
.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Common issues[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent#common-issues)

---------------------------------------------------------------------------------------------------------------------------

For common errors or issues and suggested resolution steps, refer to [Common Issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues)
.

[PreviousRoot nodes](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes)
[NextConversational Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent)

Last updated 10 days ago

Was this helpful?