For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive.md)
.

Use the TheHive node to automate work in TheHive, and integrate TheHive with other applications. n8n has built-in support for a wide range of TheHive features, including creating alerts, counting tasks logs, cases, and observables.

On this page, you'll find a list of operations the TheHive node supports and links to more resources.

**TheHive and TheHive 5**

n8n provides two nodes for TheHive. Use this node (TheHive) if you want to use TheHive's version 3 or 4 API. If you want to use version 5, use [TheHive 5](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive5)
.

**Credentials**

Refer to [TheHive credentials](https://docs.n8n.io/integrations/builtin/credentials/thehive)
 for guidance on setting up authentication.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive#operations)

---------------------------------------------------------------------------------------------------

The available operations depend on your API version. To see the operations list, create your credentials, including selecting your API version. Then return to the node, select the resource you want to use, and n8n displays the available operations for your API version.

*   Alert
    
*   Case
    
*   Log
    
*   Observable
    
*   Task
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------

[Browse TheHive node documentation integration templates](https://n8n.io/integrations/thehive)
 or [search all templates](https://n8n.io/workflows/)

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

Related resources[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive#related-resources)

-----------------------------------------------------------------------------------------------------------------

n8n provides a trigger node for TheHive. Refer to the [TheHive Trigger node documentation](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.thehivetrigger)
 for more information.

Refer to TheHive's documentation for more information about the service:

*   [Version 3](https://docs.thehive-project.org/thehive/legacy/thehive3/api/)
    
*   [Version 4](https://docs.thehive-project.org/cortex/api/api-guide/)
    

[PreviousCommon issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues)
[NextTheHive 5](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive5)

Last updated 10 days ago

Was this helpful?