For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awselb.md)
.

Use the AWS Elastic Load Balancing node to automate work in AWS ELB, and integrate AWS ELB with other applications. n8n has built-in support for a wide range of AWS ELB features, including adding, getting, removing, deleting certificates and load balancers.

On this page, you'll find a list of operations the AWS ELB node supports and links to more resources.

**Credentials**

Refer to [AWS ELB credentials](https://docs.n8n.io/integrations/builtin/credentials/aws)
 for guidance on setting up authentication.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awselb#operations)

--------------------------------------------------------------------------------------------------

*   Listener Certificate
    
    *   Add
        
    *   Get Many
        
    *   Remove
        
    
*   Load Balancer
    
    *   Create
        
    *   Delete
        
    *   Get
        
    *   Get Many
        
    

This node supports creating and managing application and network load balancers. It doesn't currently support gateway load balancers.

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awselb#templates-and-examples)

--------------------------------------------------------------------------------------------------------------------------

[Browse AWS Elastic Load Balancing node documentation integration templates](https://n8n.io/integrations/aws-elb)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awselb#related-resources)

----------------------------------------------------------------------------------------------------------------

Refer to [AWS ELB's documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
 for more information on this service.

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awselb#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousAWS DynamoDB](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsdynamodb)
[NextAWS IAM](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsiam)

Last updated 10 days ago

Was this helpful?