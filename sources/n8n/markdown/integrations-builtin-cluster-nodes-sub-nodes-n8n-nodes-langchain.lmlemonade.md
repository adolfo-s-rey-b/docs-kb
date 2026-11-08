For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade.md)
.

Use the Lemonade Model node to generate text completions using language models hosted and managed by a Lemonade server. This node is a simple LangChain-compatible language model root node suitable for text completion tasks within n8n workflows.

On this page, you'll find a list of operations the Lemonade Model node supports, and links to more resources.

**Credentials**

Refer to the [Lemonade credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/lemonade)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade#node-parameters)

-----------------------------------------------------------------------------------------------------------------------------------

Configure the node with the following parameters.

### Model[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade#model)

The model which will generate the completion. Models are loaded and managed through the Lemonade server; select the model you want to use from the list provided by the node.

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade#node-options)

-----------------------------------------------------------------------------------------------------------------------------

Use these options to further refine the node's behavior.

### Sampling Temperature[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade#sampling-temperature)

Controls the randomness of the generated text. Lower values make the output more focused and deterministic, while higher values make it more diverse and random.

Property

Value

Type

number

Required

no

Default

0.7

### Top P[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade#top-p)

Controls which words the model can choose from when generating text. Lower values progressively remove the least likely options, so the model can only pick from a smaller, higher-confidence pool.

Property

Value

Type

number

Required

no

Default

1

### Frequency Penalty[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade#frequency-penalty)

Adjusts the penalty for tokens that have already appeared in the generated text. Positive values discourage repetition, negative values encourage it.

Property

Value

Type

number

Required

no

Default

0

### Presence Penalty[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade#presence-penalty)

Adjusts the penalty for tokens based on their presence in the generated text so far. Positive values penalize tokens that have already appeared, encouraging diversity.

Property

Value

Type

number

Required

no

Default

0

### Max Tokens to Generate[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade#max-tokens-to-generate)

The maximum number of tokens to generate. Set to -1 for no limit. Be cautious when setting this to a large value, as it can lead to very long outputs.

Property

Value

Type

number

Required

no

Default

\-1

### Stop Sequences[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade#stop-sequences)

Comma-separated list of sequences where the model will stop generating text.

Property

Value

Type

string

Required

no

Default

""

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Lemonade Model node documentation integration templates](https://n8n.io/integrations/lemonade-model)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade#related-resources)

---------------------------------------------------------------------------------------------------------------------------------------

Refer to [Lemonade Server's documentation](https://lemonade-server.ai/docs/)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousCohere Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere)
[NextOllama Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama)

Last updated 10 days ago

Was this helpful?