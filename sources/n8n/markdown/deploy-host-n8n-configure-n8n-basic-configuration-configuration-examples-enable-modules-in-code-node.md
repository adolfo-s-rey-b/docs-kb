For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/enable-modules-in-code-node.md)
.

For security reasons, the Code node restricts importing modules. It's possible to lift that restriction for built-in and external modules by setting the following environment variables:

*   `NODE_FUNCTION_ALLOW_BUILTIN`: For built-in modules
    
*   `NODE_FUNCTION_ALLOW_EXTERNAL`: For external modules sourced from n8n/node\_modules directory. External module support is disabled when an environment variable isn't set.
    

Copy

    # Allows usage of all builtin modules <a href="#allows-usage-of-all-builtin-modules" id="allows-usage-of-all-builtin-modules"></a>
    export NODE_FUNCTION_ALLOW_BUILTIN=*
    
    # Allows usage of only crypto <a href="#allows-usage-of-only-crypto" id="allows-usage-of-only-crypto"></a>
    export NODE_FUNCTION_ALLOW_BUILTIN=crypto
    
    # Allows usage of only crypto and fs <a href="#allows-usage-of-only-crypto-and-fs" id="allows-usage-of-only-crypto-and-fs"></a>
    export NODE_FUNCTION_ALLOW_BUILTIN=crypto,fs
    
    # Allow usage of external npm modules. <a href="#allow-usage-of-external-npm-modules" id="allow-usage-of-external-npm-modules"></a>
    export NODE_FUNCTION_ALLOW_EXTERNAL=moment,lodash

**If using Task Runners**

If n8n instance is setup with [Task Runners](https://docs.n8n.io/deploy/host-n8n/configure-n8n/set-up-task-runners)
, add the environment variables to the Task Runners instead to the main n8n node.

Refer to [Environment variables reference](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes)
 for more information on these variables.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/enable-modules-in-code-node#related-resources)

----------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Configuration examples](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples)
    

[PreviousSpecify custom nodes location](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/specify-custom-nodes-location)
[NextSet the timezone](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-the-timezone)

Last updated 10 days ago

Was this helpful?