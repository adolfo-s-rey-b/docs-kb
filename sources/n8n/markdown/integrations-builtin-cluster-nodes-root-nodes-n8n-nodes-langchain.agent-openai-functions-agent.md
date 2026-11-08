For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent.md)
.

**Feature availability**

The OpenAI Functions Agent is deprecated from n8n 1.82.0. New or updated AI Agent nodes use the [Tools Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent)
 instead. Only workflows still using node version 1 of the AI Agent node can select the OpenAI Functions Agent.

Node version 1 of the AI Agent node is removed from n8n 3.0, so the OpenAI Functions Agent stops working for all workflows. See [n8n 3.0 breaking changes](https://docs.n8n.io/changelog/v30-breaking-changes)
 for details.

Use the OpenAI Functions Agent node to use an [OpenAI functions model](https://platform.openai.com/docs/guides/function-calling)
. These are models that detect when a function should be called and respond with the inputs that should be passed to the function.

Refer to [AI Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
 for more information on the AI Agent node itself.

You can use this agent with the [Chat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger)
 node. Attach a memory sub-node so that users can have an ongoing conversation with multiple queries. Memory doesn't persist between sessions.

**OpenAI Chat Model required**

You must use the [OpenAI Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai)
 with this agent.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent#node-parameters)

------------------------------------------------------------------------------------------------------------------------------------------------------

Configure the OpenAI Functions Agent using the following parameters.

### Prompt[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent#prompt)

Select how you want the node to construct the prompt (also known as the user's query or input from the chat).

Choose from:

*   **Take from previous node automatically**: If you select this option, the node expects an input from a previous node called `chatInput`.
    
*   **Define below**: If you select this option, provide either static text or an expression for dynamic content to serve as the prompt in the **Prompt (User Message)** field.
    

### Require Specific Output Format[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent#require-specific-output-format)

This parameter controls whether you want the node to require a specific output format. When turned on, n8n prompts you to connect one of these output parsers to the node:

*   [Auto-fixing Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing)
    
*   [Item List Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist)
    
*   [Structured Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured)
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent#node-options)

------------------------------------------------------------------------------------------------------------------------------------------------

Refine the OpenAI Functions Agent node's behavior using these options:

### System Message[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent#system-message)

If you'd like to send a message to the agent before the conversation starts, enter the message you'd like to send.

Use this option to guide the agent's decision-making.

### Max Iterations[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent#max-iterations)

Enter the number of times the model should run to try and generate a good answer from the user's prompt.

Defaults to `10`.

### Return Intermediate Steps[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent#return-intermediate-steps)

Select whether to include intermediate steps the agent took in the final output (turned on) or not (turned off).

This could be useful for further refining the agent's behavior based on the steps it took.

### Tracing Metadata[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent#tracing-metadata)

Add custom key-value metadata to tracing events for this agent. This is useful for filtering and debugging runs in tracing tools like [LangSmith](https://docs.n8n.io/build/integrate-ai/langchain-in-n8n#use-langsmith-with-a-self-hosted-n8n-instance)
.

Entries with empty keys or values are ignored.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent#templates-and-examples)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Refer to the main AI Agent node's [Templates and examples](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent#templates-and-examples)
 section.

Common issues[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent#common-issues)

--------------------------------------------------------------------------------------------------------------------------------------------------

For common questions or issues and suggested solutions, refer to [Common issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues)
.

[PreviousConversational Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent)
[NextPlan and Execute Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent)

Last updated 10 days ago

Was this helpful?