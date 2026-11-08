For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/set-up-ssl.md)
.

There are two methods to support TLS/SSL in n8n.

Use a reverse proxy (recommended)[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/set-up-ssl#use-a-reverse-proxy-recommended)

-------------------------------------------------------------------------------------------------------------------------------------------

Use a reverse proxy like [Traefik](https://doc.traefik.io/traefik/)
 or a Network Load Balancer (NLB) in front of the n8n instance. This should also take care of certificate renewals.

Refer to [Security | Data encryption](https://n8n.io/legal/#security)
 for more information.

Pass certificates into n8n directly[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/set-up-ssl#pass-certificates-into-n8n-directly)

-------------------------------------------------------------------------------------------------------------------------------------------------

You can also choose to pass certificates into n8n directly. To do so, set the `N8N_SSL_CERT` and `N8N_SSL_KEY` environment variables to point to your generated certificate and key file.

You'll need to make sure the certificate stays renewed and up to date.

Refer to [Deployment environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment)
 for more information on these variables and [Configuration](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration)
 for more information on setting environment variables.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/set-up-ssl#related-resources)

-------------------------------------------------------------------------------------------------------------

*   [Security](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security)
    

[PreviousManage security policies](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/manage-security-policies)
[NextConfigure SSO](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/configure-sso)

Last updated 10 days ago

Was this helpful?