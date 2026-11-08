For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsiam.md)
.

Use the AWS IAM node to automate work in AWS Identity and Access Management (IAM) and integrate AWS IAM with other applications. n8n has built-in support for a wide range of AWS IAM features, which includes creating, updating, getting and deleting users and groups as well as managing group membership.

On this page, you'll find a list of operations the AWS IAM node supports, and links to more resources.

**Credentials**

Refer to the [AWS credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/aws)
 for authentication information for this node.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsiam#operations)

--------------------------------------------------------------------------------------------------

*   **User**:
    
    *   **Add to Group**: Add an existing user to a group.
        
    *   **Create**: Create a new user.
        
    *   **Delete**: Delete a user.
        
    *   **Get**: Retrieve a user.
        
    *   **Get Many**: Retrieve a list of users.
        
    *   **Remove From Group**: Remove a user from a group.
        
    *   **Update**: Update an existing user.
        
    
*   **Group**:
    
    *   **Create**: Create a new group.
        
    *   **Delete**: Create a new group.
        
    *   **Get**: Retrieve a group.
        
    *   **Get Many**: Retrieve a list of groups.
        
    *   **Update**: Update an existing group.
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsiam#templates-and-examples)

--------------------------------------------------------------------------------------------------------------------------

[Browse AWS IAM node documentation integration templates](https://n8n.io/integrations/aws-iam)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsiam#related-resources)

----------------------------------------------------------------------------------------------------------------

Refer to the [AWS IAM documentation](https://docs.aws.amazon.com/IAM/latest/APIReference/welcome.html)
 for more information about the service.

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsiam#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousAWS Elastic Load Balancing](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awselb)
[NextAWS Lambda](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awslambda)

Last updated 10 days ago

Was this helpful?