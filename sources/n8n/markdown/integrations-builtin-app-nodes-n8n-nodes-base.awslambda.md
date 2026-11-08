For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awslambda.md)
.

Use the AWS Lambda node to automate work in AWS Lambda, and integrate AWS Lambda with other applications. n8n has built-in support for a wide range of AWS Lambda features, including invoking functions.

On this page, you'll find a list of operations the AWS Lambda node supports and links to more resources.

**Credentials**

Refer to [AWS Lambda credentials](https://docs.n8n.io/integrations/builtin/credentials/aws)
 for guidance on setting up authentication.

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awslambda#operations)

-----------------------------------------------------------------------------------------------------

*   Invoke a function
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awslambda#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------

[Browse AWS Lambda node documentation integration templates](https://n8n.io/integrations/aws-lambda)
 or [search all templates](https://n8n.io/workflows/)

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awslambda#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousAWS IAM](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsiam)
[NextAWS Rekognition](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsrekognition)

Last updated 10 days ago

Was this helpful?