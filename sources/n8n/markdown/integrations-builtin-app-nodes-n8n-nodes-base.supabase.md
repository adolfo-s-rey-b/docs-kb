For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase.md)
.

Use the Supabase node to automate work in Supabase, and integrate Supabase with other applications. n8n has built-in support for a wide range of Supabase features, including creating, deleting, and getting rows.

On this page, you'll find a list of operations the Supabase node supports and links to more resources.

**Credentials**

Refer to [Supabase credentials](https://docs.n8n.io/integrations/builtin/credentials/supabase)
 for guidance on setting up authentication.

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase#operations)

----------------------------------------------------------------------------------------------------

*   Row
    
    *   Create a new row
        
    *   Delete a row
        
    *   Get a row
        
    *   Get all rows
        
    *   Update a row
        
    

Using custom schemas[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase#using-custom-schemas)

------------------------------------------------------------------------------------------------------------------------

By default, the Supabase node only fetches the `public` schema. To fetch [custom schemas](https://supabase.com/docs/guides/api/using-custom-schemas)
, enable **Use Custom Schema**.

In the new **Schema** field, provide the custom schema the Supabase node should use.

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase#templates-and-examples)

----------------------------------------------------------------------------------------------------------------------------

[Browse n8n-nodes-base.supabase integration templates](https://n8n.io/integrations/supabase)
 or [search all templates](https://n8n.io/workflows/)

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

Common issues[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase#common-issues)

----------------------------------------------------------------------------------------------------------

For common errors or issues and suggested resolution steps, refer to [Common issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase/common-issues)
.

[PreviousStripe](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.stripe)
[NextCommon issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase/common-issues)

Last updated 10 days ago

Was this helpful?