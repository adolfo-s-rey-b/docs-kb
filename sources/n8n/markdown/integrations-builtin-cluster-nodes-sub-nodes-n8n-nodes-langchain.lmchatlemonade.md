For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade.md)
.

Use the Lemonade Chat Model node to run chat-capable language models managed by a Lemonade server from within n8n. This node functions as a LangChain-compatible chat model root node and is suitable for chat-style workloads. It lets you select a model hosted on your Lemonade server, and control generation behavior using common sampling and decoding options.

On this page, you'll find a list of the node parameters, and available options to refine generation.

**Credentials**

Refer to the [Lemonade credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/lemonade)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade#node-parameters)

---------------------------------------------------------------------------------------------------------------------------------------

### Model[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade#model)

The model which will generate the completion. Models are loaded and managed through the Lemonade server. This parameter is required. Select the model name made available by your Lemonade server (for example, a model alias like "gpt-4", or any custom model name exposed by Lemonade).

Models are provided by the Lemonade server; if you don't see the model you expect, verify your Lemonade server configuration and credentials.

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade#node-options)

---------------------------------------------------------------------------------------------------------------------------------

Use these options to further refine the node's behavior.

### Sampling Temperature[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade#sampling-temperature)

Controls the randomness of the generated text. Lower values make the output more focused and deterministic, while higher values make it more diverse and random.

Property

Value

Type

number

Required

no

Default

0.7

### Top P[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade#top-p)

Controls which words the model can choose from when generating text. Lower values progressively remove the least likely options, so the model can only pick from a smaller, higher-confidence pool.

Property

Value

Type

number

Required

no

Default

1

### Frequency Penalty[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade#frequency-penalty)

Adjusts the penalty for tokens that have already appeared in the generated text. Positive values discourage repetition, negative values encourage it.

Property

Value

Type

number

Required

no

Default

0

### Presence Penalty[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade#presence-penalty)

Adjusts the penalty for tokens based on their presence in the generated text so far. Positive values penalize tokens that have already appeared, encouraging diversity.

Property

Value

Type

number

Required

no

Default

0

### Max Tokens to Generate[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade#max-tokens-to-generate)

The maximum number of tokens to generate. Set to -1 for no limit. Be cautious when setting this to a large value, as it can lead to long outputs.

Property

Value

Type

number

Required

no

Default

\-1

### Stop Sequences[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade#stop-sequences)

Comma-separated list of sequences where the model will stop generating text. Use this to define explicit termination strings for responses.

Property

Value

Type

string

Required

no

Default

""

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Lemonade Chat Model node documentation integration templates](https://n8n.io/integrations/lemonade-chat-model)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------

Refer to [Lemonade Server's documentation](https://lemonade-server.ai/docs/)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousGroq Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgroq)
[NextMiniMax Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax)

Last updated 10 days ago

Was this helpful?