For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.segment.md)
.

Use the Segment node to automate work in Segment, and integrate Segment with other applications. n8n has built-in support for a wide range of Segment features, including adding users to groups, creating identities, and tracking activities.

On this page, you'll find a list of operations the Segment node supports and links to more resources.

**Credentials**

Refer to [Segment credentials](https://docs.n8n.io/integrations/builtin/credentials/segment)
 for guidance on setting up authentication.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.segment#operations)

---------------------------------------------------------------------------------------------------

*   Group
    
    *   Add a user to a group
        
    
*   Identify
    
    *   Create an identity
        
    
*   Track
    
    *   Record the actions your users perform. Every action triggers an event, which can also have associated properties.
        
    *   Record page views on your website, along with optional extra information about the page being viewed.
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.segment#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------

[Browse Segment node documentation integration templates](https://n8n.io/integrations/segment)
 or [search all templates](https://n8n.io/workflows/)

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.segment#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousSecurityScorecard](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.securityscorecard)
[NextSendGrid](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.sendgrid)

Last updated 10 days ago

Was this helpful?