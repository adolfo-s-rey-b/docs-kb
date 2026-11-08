For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-the-base-url.md)
.

**Requires manual UI build**

This use case involves configuring the `VUE_APP_URL_BASE_API` environmental variable which requires a manual build of the `n8n-editor-ui` package. You can't use it with the default n8n Docker image where the default setting for this variable is `/`, meaning that it uses the root-domain.

You can configure the Base URL that the front end uses to connect to the back end's REST API. This is relevant when you want to host n8n's front end and back end separately.

Copy

    export VUE_APP_URL_BASE_API=https://n8n.example.com/

Refer to [Environment variables reference](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment)
 for more information on this variable.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-the-base-url#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Configuration examples](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples)
    

[PreviousIsolate n8n](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/isolate-n8n)
[NextConfigure custom SSL certificate authorities](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-custom-ssl-certificate-authorities)

Last updated 10 days ago

Was this helpful?