For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock.md)
.

Use the Embeddings AWS Bedrock node to generate embeddings for a given text.

On this page, you'll find the node parameters for the Embeddings AWS Bedrock node, and links to more resources.

**Credentials**

Refer to the [AWS credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/aws)
 for authentication information for this node.

If you route Bedrock through a [VPC interface endpoint (PrivateLink)](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html)
 without private DNS, set the **Bedrock Endpoint** and **Bedrock Runtime Endpoint** custom endpoints in the credential.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock#node-parameters)

---------------------------------------------------------------------------------------------------------------------------------------------

*   **Authentication**: Select the authentication method:
    
    *   **AWS (IAM)**: Use an IAM access key. Select an **AWS** credential.
        
    *   **AWS (Assume Role)**: Temporarily assume an IAM role. Select an **AWS (Assume Role)** credential.
        
    
*   **Model**: Select the model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html)
     that generates the embedding. The dropdown lists on-demand embedding models and embedding inference profiles together. If the dropdown is empty or incomplete, your IAM role may lack the `bedrock:ListFoundationModels` or `bedrock:ListInferenceProfiles` permission. Switch the field to **Expression** mode and enter the model or inference profile ID directly.
    

Learn more about available models in the [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
.

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock#node-options)

---------------------------------------------------------------------------------------------------------------------------------------

*   **Additional Model Request Fields**: Enter model-specific request fields as JSON, for example Titan's `dimensions` and `normalize` or Cohere's `input_type` and `truncate`. Refer to the [AWS model parameters documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html)
     for the fields each model family supports.
    
*   **Max Retries**: Enter the maximum number of times to retry a request.
    
*   **Timeout**: Enter the maximum time in milliseconds to wait for a request to complete. Set it to `0` to disable the timeout.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Embeddings AWS Bedrock node documentation integration templates](https://n8n.io/integrations/embeddings-aws-bedrock)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------------

Refer to the [AWS Bedrock documentation](https://docs.aws.amazon.com/bedrock/)
 for more information about AWS Bedrock.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousGitHub Document Loader](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader)
[NextMicrosoft Foundry Embeddings](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai)

Last updated 10 days ago

Was this helpful?