For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/disable-the-public-api.md)
.

The [n8n public REST API](https://docs.n8n.io/connect/n8n-api)
 allows you to programmatically perform many of the same tasks as you can in the n8n GUI.

If you don't plan on using this API, n8n recommends disabling it to improve the security of your n8n installation.

To disable the [public REST API](https://docs.n8n.io/connect/n8n-api)
, set the `N8N_PUBLIC_API_DISABLED` environment variable to `true`, for example:

Copy

    export N8N_PUBLIC_API_DISABLED=true

Disable the API playground[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/disable-the-public-api#disable-the-api-playground)

-------------------------------------------------------------------------------------------------------------------------------------------

To disable the [API playground](https://docs.n8n.io/connect/n8n-api/use-an-api-playground)
, set the `N8N_PUBLIC_API_SWAGGERUI_DISABLED` environment variable to `true`, for example:

Copy

    export N8N_PUBLIC_API_SWAGGERUI_DISABLED=true

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/disable-the-public-api#related-resources)

-------------------------------------------------------------------------------------------------------------------------

*   [Security](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security)
    : audit, harden, and restrict a self-hosted instance.
    
*   [Deployment environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment)
    : more information on these environment variables.
    
*   [Configuration](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration)
    : how to set environment variables.
    

[PreviousRun security audits](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/run-security-audits)
[NextControl telemetry](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/control-telemetry)

Last updated 10 days ago

Was this helpful?