For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.stripe.md)
.

Use the Stripe node to automate work in Stripe, and integrate Stripe with other applications. n8n has built-in support for a wide range of Stripe features, including getting balance, creating charge and meter events, and deleting customers.

On this page, you'll find a list of operations the Stripe node supports and links to more resources.

**Credentials**

Refer to [Stripe credentials](https://docs.n8n.io/integrations/builtin/credentials/stripe)
 for guidance on setting up authentication.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.stripe#operations)

--------------------------------------------------------------------------------------------------

*   Balance
    
    *   Get a balance
        
    
*   Charge
    
    *   Create a charge
        
    *   Get a charge
        
    *   Get all charges
        
    *   Update a charge
        
    
*   Coupon
    
    *   Create a coupon
        
    *   Get all coupons
        
    
*   Customer
    
    *   Create a customer
        
    *   Delete a customer
        
    *   Get a customer
        
    *   Get all customers
        
    *   Update a customer
        
    
*   Customer Card
    
    *   Add a customer card
        
    *   Get a customer card
        
    *   Remove a customer card
        
    
*   Meter Event
    
    *   Create a meter event
        
    
*   Source
    
    *   Create a source
        
    *   Delete a source
        
    *   Get a source
        
    
*   Token
    
    *   Create a token
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.stripe#templates-and-examples)

--------------------------------------------------------------------------------------------------------------------------

[Browse Stripe node documentation integration templates](https://n8n.io/integrations/stripe)
 or [search all templates](https://n8n.io/workflows/)

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.stripe#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousStrava](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.strava)
[NextSupabase](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase)

Last updated 10 days ago

Was this helpful?