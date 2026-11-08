For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock.md)
.

The AWS Bedrock Chat Model node allows you use LLM models utilising AWS Bedrock platform.

On this page, you'll find the node parameters for the AWS Bedrock Chat Model node, and links to more resources.

**Credentials**

Refer to the [AWS credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/aws)
 for authentication information for this node.

If you route Bedrock through a [VPC interface endpoint (PrivateLink)](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html)
 without private DNS, set the **Bedrock Endpoint** and **Bedrock Runtime Endpoint** custom endpoints in the credential.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock#node-parameters)

-----------------------------------------------------------------------------------------------------------------------------------------

*   **Authentication**: Select the authentication method:
    
    *   **AWS (IAM)**: Use an IAM access key. Select an **AWS** credential.
        
    *   **AWS (Assume Role)**: Temporarily assume an IAM role. Select an **AWS (Assume Role)** credential.
        
    
*   **Model**: Select the model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html)
     that generates the completion. The dropdown lists on-demand foundation models and cross-region inference profiles together. The newest models (for example Claude Sonnet 4.x) are only available as inference profiles. If part of the list is missing, your IAM role may lack the `bedrock:ListFoundationModels` or `bedrock:ListInferenceProfiles` permission. You can also switch the field to **Expression** mode and enter a model ID, inference profile ID, or ARN directly.
    

On node version 1.1, the dropdown shows one list at a time: use the **Model Source** parameter to switch between on-demand foundation models and inference profiles. Node version 1 only supports on-demand foundation models.

Learn more about available models in the [Amazon Bedrock model documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html)
.

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock#node-options)

-----------------------------------------------------------------------------------------------------------------------------------

*   **Maximum Number of Tokens**: Enter the maximum number of tokens used, which sets the completion length.
    
*   **Sampling Temperature**: Use this option to control the randomness of the sampling process. A higher temperature creates more diverse sampling, but increases the risk of hallucinations.
    
*   **Top P**: Set the probability threshold for token selection. A lower value limits the pool to more probable tokens; a higher value allows more diverse options.
    
*   **Max Retries**: Enter the maximum number of times to retry a request.
    
*   **Timeout**: Enter the maximum time in milliseconds to wait for a request to complete. Increase this for long generations. Set it to `0` to disable the timeout.
    
*   **Additional Model Request Fields**: Enter model-family-specific inference parameters as JSON, for example Claude's `top_k` or Nova's `inferenceConfig`. Refer to the [AWS model parameters documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html)
     for the parameters each model family supports.
    
*   **Latency Optimization**: Choose whether requests use **Standard** or **Optimized** latency. Optimized mode can reduce response time for supported models and regions. Refer to the [AWS latency-optimized inference documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html)
     for availability.
    
*   **Guardrail**: Apply an [Amazon Bedrock guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
     to requests. Refer to [Using AWS Guardrails](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock#using-aws-guardrails)
     for details.
    

### Using AWS Guardrails[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock#using-aws-guardrails)

Guardrails let your organization enforce content and safety policies on model invocations. The guardrail must exist in the same AWS region as the model. The **Guardrail** option has these fields:

*   **Guardrail Identifier**: The ID or full ARN of the guardrail to apply.
    
*   **Guardrail Version**: The guardrail version to use: a numeric version string (for example `1`) or `DRAFT` for the working draft. Defaults to `DRAFT`.
    
*   **Trace**: Whether AWS includes diagnostic trace information about the guardrail's evaluation in the response: **Disabled** (default), **Enabled**, or **Enabled (Full)**. Note: enabling trace makes AWS include guardrail assessment details (which can echo matched input content, e.g. PII findings) in responses; n8n doesn't currently surface these in the AI log.
    

When a guardrail intervenes, the node returns the guardrail's configured blocked message in place of the model output, as a normal response rather than an error. n8n doesn't expose the underlying stop reason: to detect an intervention downstream, match on your guardrail's blocked message text. An invalid guardrail identifier or version fails the node with the AWS validation error. Guardrails apply to both streaming and non-streaming requests.

**IAM permissions**

The credential needs the `bedrock:ApplyGuardrail` permission on the guardrail resource in addition to the invoke permissions. Without it, requests fail with an `AccessDeniedException` once a guardrail is set. If your organization requires guardrails on every invocation, enforce the `bedrock:GuardrailIdentifier` condition key on invoke permissions in IAM rather than relying on this optional node field.

Proxy limitations[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock#proxy-limitations)

---------------------------------------------------------------------------------------------------------------------------------------------

This node doesn't support the [`NO_PROXY` environment variable](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment)
.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse AWS Bedrock Chat Model node documentation integration templates](https://n8n.io/integrations/aws-bedrock-chat-model)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock#related-resources)

---------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's AWS Bedrock Chat Model documentation](https://docs.langchain.com/oss/javascript/integrations/chat/bedrock_converse)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousAnthropic Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic)
[NextMicrosoft Foundry Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatazureopenai)

Last updated 10 days ago

Was this helpful?