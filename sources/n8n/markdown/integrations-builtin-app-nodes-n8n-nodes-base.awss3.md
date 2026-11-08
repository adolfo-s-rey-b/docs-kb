For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awss3.md)
.

Use the AWS S3 node to automate work in AWS S3, and integrate AWS S3 with other applications. n8n has built-in support for a wide range of AWS S3 features, including creating and deleting buckets, copying and downloading files, as well as getting folders.

On this page, you'll find a list of operations the AWS S3 node supports and links to more resources.

**Credentials**

Refer to [AWS credentials](https://docs.n8n.io/integrations/builtin/credentials/aws)
 for guidance on setting up authentication.

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awss3#operations)

-------------------------------------------------------------------------------------------------

*   Bucket
    
    *   Create a bucket
        
    *   Delete a bucket
        
    *   Get all buckets
        
    *   Search within a bucket
        
    
*   File
    
    *   Copy a file
        
    *   Delete a file
        
    *   Download a file
        
    *   Get all files
        
    *   Upload a file
        
    
*   Folder
    
    *   Create a folder
        
    *   Delete a folder
        
    *   Get all folders
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awss3#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------

[Browse AWS S3 node documentation integration templates](https://n8n.io/integrations/aws-s3)
 or [search all templates](https://n8n.io/workflows/)

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awss3#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousAWS Rekognition](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsrekognition)
[NextAWS SES](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsses)

Last updated 10 days ago

Was this helpful?