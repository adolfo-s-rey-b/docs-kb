For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent.md)
.

**Feature availability**

The ReAct Agent is deprecated from n8n 1.82.0. New or updated AI Agent nodes use the [Tools Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent)
 instead. Only workflows still using node version 1 of the AI Agent node can select the ReAct Agent.

Node version 1 of the AI Agent node is removed from n8n 3.0, so the ReAct Agent stops working for all workflows. See [n8n 3.0 breaking changes](https://docs.n8n.io/changelog/v30-breaking-changes)
 for details.

The ReAct Agent node implements [ReAct](https://react-lm.github.io/)
 logic. ReAct (reasoning and acting) brings together the reasoning powers of chain-of-thought prompting and action plan generation.

The ReAct Agent reasons about a given task, determines the necessary actions, and then executes them. It follows the cycle of reasoning and acting until it completes the task. The ReAct agent can break down complex tasks into smaller sub-tasks, prioritise them, and execute them one after the other.

Refer to [AI Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
 for more information on the AI Agent node itself.

**No memory**

The ReAct agent doesn't support memory sub-nodes. This means it can't recall previous prompts or simulate an ongoing conversation.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent#node-parameters)

-------------------------------------------------------------------------------------------------------------------------------------------

Configure the ReAct Agent using the following parameters.

### Prompt[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent#prompt)

Select how you want the node to construct the prompt (also known as the user's query or input from the chat).

Choose from:

*   **Take from previous node automatically**: If you select this option, the node expects an input from a previous node called `chatInput`.
    
*   **Define below**: If you select this option, provide either static text or an expression for dynamic content to serve as the prompt in the **Prompt (User Message)** field.
    

### Require Specific Output Format[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent#require-specific-output-format)

This parameter controls whether you want the node to require a specific output format. When turned on, n8n prompts you to connect one of these output parsers to the node:

*   [Auto-fixing Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing)
    
*   [Item List Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist)
    
*   [Structured Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured)
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent#node-options)

-------------------------------------------------------------------------------------------------------------------------------------

Use the options to create a message to send to the agent at the start of the conversation. The message type depends on the model you're using:

*   **Chat models**: These models have the concept of three components interacting (AI, system, and human). They can receive system messages and human messages (prompts).
    
*   **Instruct models**: These models don't have the concept of separate AI, system, and human components. They receive one body of text, the instruct message.
    

### Human Message Template[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent#human-message-template)

Use this option to extend the user prompt. This is a way for the agent to pass information from one iteration to the next.

Available LangChain expressions:

*   `{input}`: Contains the user prompt.
    
*   `{agent_scratchpad}`: Information to remember for the next iteration.
    

### Prefix Message[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent#prefix-message)

Enter text to prefix the tools list at the start of the conversation. You don't need to add the list of tools. LangChain automatically adds the tools list.

### Suffix Message for Chat Model[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent#suffix-message-for-chat-model)

Add text to append after the tools list at the start of the conversation when the agent uses a chat model. You don't need to add the list of tools. LangChain automatically adds the tools list.

### Suffix Message for Regular Model[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent#suffix-message-for-regular-model)

Add text to append after the tools list at the start of the conversation when the agent uses a regular/instruct model. You don't need to add the list of tools. LangChain automatically adds the tools list.

### Return Intermediate Steps[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent#return-intermediate-steps)

Select whether to include intermediate steps the agent took in the final output (turned on) or not (turned off).

This could be useful for further refining the agent's behavior based on the steps it took.

### Tracing Metadata[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent#tracing-metadata)

Add custom key-value metadata to tracing events for this agent. This is useful for filtering and debugging runs in tracing tools like [LangSmith](https://docs.n8n.io/build/integrate-ai/langchain-in-n8n#use-langsmith-with-a-self-hosted-n8n-instance)
.

Entries with empty keys or values are ignored.

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------------

Refer to LangChain's [ReAct Agents](https://docs.langchain.com/oss/javascript/langchain/agents)
 documentation for more information.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------------------

Refer to the main AI Agent node's [Templates and examples](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent#templates-and-examples)
 section.

Common issues[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent#common-issues)

---------------------------------------------------------------------------------------------------------------------------------------

For common questions or issues and suggested solutions, refer to [Common issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues)
.

[PreviousPlan and Execute Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent)
[NextSQL Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/sql-agent)

Last updated 10 days ago

Was this helpful?