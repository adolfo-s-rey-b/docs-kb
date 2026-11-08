For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscognito.md)
.

Use the AWS Cognito node to automate work in AWS Cognito and integrate AWS Cognito with other applications. n8n has built-in support for a wide range of AWS Cognito features, which includes creating, retrieving, updating, and deleting groups, users, and user pools.

On this page, you'll find a list of operations the AWS Cognito node supports, and links to more resources.

**Credentials**

Refer to the [AWS credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/aws)
 for authentication information for this node.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscognito#operations)

------------------------------------------------------------------------------------------------------

*   Group:
    
    *   Create: Create a new group.
        
    *   Delete: Delete an existing group.
        
    *   Get: Retrieve details about an existing group.
        
    *   Get Many: Retrieve a list of groups.
        
    *   Update: Update an existing group.
        
    
*   User:
    
    *   Add to Group: Add an existing user to a group.
        
    *   Create: Create a new user.
        
    *   Delete: Delete a user.
        
    *   Get: Retrieve information about an existing user.
        
    *   Get Many: Retrieve a list of users.
        
    *   Remove From Group: Remove a user from a group.
        
    *   Update: Update an existing user.
        
    
*   User Pool:
    
    *   Get: Retrieve information about an existing user pool.
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscognito#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------------

[Browse AWS Cognito node documentation integration templates](https://n8n.io/integrations/aws-cognito)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscognito#related-resources)

--------------------------------------------------------------------------------------------------------------------

Refer to [AWS Cognito's documentation](https://docs.aws.amazon.com/cognito/)
 for more information about the service.

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscognito#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousAWS Certificate Manager](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscertificatemanager)
[NextAWS Comprehend](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscomprehend)

Last updated 10 days ago

Was this helpful?