For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent.md)
.

**Feature availability**

The Conversational Agent is deprecated from n8n 1.82.0. New or updated AI Agent nodes use the [Tools Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent)
 instead. Only workflows still using node version 1 of the AI Agent node can select the Conversational Agent.

Node version 1 of the AI Agent node is removed from n8n 3.0, so the Conversational Agent stops working for all workflows. See [n8n 3.0 breaking changes](https://docs.n8n.io/changelog/v30-breaking-changes)
 for details.

The Conversational Agent has human-like conversations. It can maintain context, understand user intent, and provide relevant answers. This agent is typically used for building chatbots, virtual assistants, and customer support systems.

The Conversational Agent describes tools in the system prompt and parses JSON responses for tool calls. If your preferred AI model doesn't support tool calling or you're handling simpler interactions, this agent is a good general option. It's more flexible but may be less accurate than the [Tools Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent)
.

Refer to [AI Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
 for more information on the AI Agent node itself.

You can use this agent with the [Chat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger)
 node. Attach a memory sub-node so that users can have an ongoing conversation with multiple queries. Memory doesn't persist between sessions.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent#node-parameters)

----------------------------------------------------------------------------------------------------------------------------------------------------

Configure the Conversational Agent using the following parameters.

### Prompt[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent#prompt)

Select how you want the node to construct the prompt (also known as the user's query or input from the chat).

Choose from:

*   **Take from previous node automatically**: If you select this option, the node expects an input from a previous node called `chatInput`.
    
*   **Define below**: If you select this option, provide either static text or an expression for dynamic content to serve as the prompt in the **Prompt (User Message)** field.
    

### Require Specific Output Format[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent#require-specific-output-format)

This parameter controls whether you want the node to require a specific output format. When turned on, n8n prompts you to connect one of these output parsers to the node:

*   [Auto-fixing Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing)
    
*   [Item List Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist)
    
*   [Structured Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured)
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent#node-options)

----------------------------------------------------------------------------------------------------------------------------------------------

Refine the Conversational Agent node's behavior using these options:

### Human Message[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent#human-message)

Tell the agent about the tools it can use and add context to the user's input.

You must include these expressions and variable:

*   `{tools}`: A LangChain expression that provides a string of the tools you've connected to the Agent. Provide some context or explanation about who should use the tools and how they should use them.
    
*   `{format_instructions}`: A LangChain expression that provides the schema or format from the output parser node you've connected. Since the instructions themselves are context, you don't need to provide context for this expression.
    
*   `{{input}}`: A LangChain variable containing the user's prompt. This variable populates with the value of the **Prompt** parameter. Provide some context that this is the user's input.
    

Here's an example of how you might use these strings:

Example:

Copy

    TOOLS
    ------
    Assistant can ask the user to use tools to look up information that may be helpful in answering the user's original question. The tools the human can use are:
    
    {tools}
    
    {format_instructions}
    
    USER'S INPUT
    --------------------
    Here is the user's input (remember to respond with a markdown code snippet of a JSON blob with a single action, and NOTHING else):
    
    {{input}}

### System Message[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent#system-message)

If you'd like to send a message to the agent before the conversation starts, enter the message you'd like to send.

Use this option to guide the agent's decision-making.

### Max Iterations[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent#max-iterations)

Enter the number of times the model should run to try and generate a good answer from the user's prompt.

Defaults to `10`.

### Return Intermediate Steps[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent#return-intermediate-steps)

Select whether to include intermediate steps the agent took in the final output (turned on) or not (turned off).

This could be useful for further refining the agent's behavior based on the steps it took.

### Tracing Metadata[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent#tracing-metadata)

Add custom key-value metadata to tracing events for this agent. This is useful for filtering and debugging runs in tracing tools like [LangSmith](https://docs.n8n.io/build/integrate-ai/langchain-in-n8n#use-langsmith-with-a-self-hosted-n8n-instance)
.

Entries with empty keys or values are ignored.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Refer to the main AI Agent node's [Templates and examples](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent#templates-and-examples)
 section.

Common issues[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent#common-issues)

------------------------------------------------------------------------------------------------------------------------------------------------

For common questions or issues and suggested solutions, refer to [Common issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues)
.

[PreviousAI Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
[NextOpenAI Functions Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent)

Last updated 10 days ago

Was this helpful?