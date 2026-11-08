For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/isolate-n8n.md)
.

By default, a self-hosted n8n instance sends data to n8n's servers. It notifies users about available updates, workflow templates, and diagnostics.

To prevent your n8n instance from connecting to n8n's servers, set these environment variables to false:

Copy

    N8N_DIAGNOSTICS_ENABLED=false
    N8N_VERSION_NOTIFICATIONS_ENABLED=false
    N8N_TEMPLATES_ENABLED=false

Unset n8n's diagnostics configuration:

Copy

    EXTERNAL_FRONTEND_HOOKS_URLS=
    N8N_DIAGNOSTICS_CONFIG_FRONTEND=
    N8N_DIAGNOSTICS_CONFIG_BACKEND=

Refer to [Environment variables reference](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment)
 for more information on these variables.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/isolate-n8n#related-resources)

------------------------------------------------------------------------------------------------------------------------------------------------

*   [Configuration examples](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples)
    

[PreviousConfiguration examples](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples)
[NextConfigure the Base URL](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-the-base-url)

Last updated 10 days ago

Was this helpful?