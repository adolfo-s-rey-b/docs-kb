For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsdynamodb.md)
.

Use the AWS DynamoDB node to automate work in AWS DynamoDB, and integrate AWS DynamoDB with other applications. n8n has built-in support for a wide range of AWS DynamoDB features, including creating, reading, updating, deleting items, and records on a database.

On this page, you'll find a list of operations the AWS DynamoDB node supports and links to more resources.

**Credentials**

Refer to [AWS credentials](https://docs.n8n.io/integrations/builtin/credentials/aws)
 for guidance on setting up authentication.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsdynamodb#operations)

-------------------------------------------------------------------------------------------------------

*   Item
    
    *   Create a new record, or update the current one if it already exists (upsert/put)
        
    *   Delete an item
        
    *   Get an item
        
    *   Get all items
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsdynamodb#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------------

[Browse AWS DynamoDB node documentation integration templates](https://n8n.io/integrations/aws-dynamodb)
 or [search all templates](https://n8n.io/workflows/)

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsdynamodb#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousAWS Comprehend](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscomprehend)
[NextAWS Elastic Load Balancing](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awselb)

Last updated 10 days ago

Was this helpful?