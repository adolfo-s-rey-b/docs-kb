For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/source-control.md)
.

**File-based configuration**

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration#keeping-sensitive-data-in-separate-files)
 for more details.

n8n uses Git-based source control to support environments. Refer to [Source control and environments](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control)
 for more information on how to link a Git repository to an n8n instance and configure your source control.

Variable

Type

Default

Description

`N8N_SOURCECONTROL_DEFAULT_SSH_KEY_TYPE`

String

`ed25519`

Set to `rsa` to make RSA the default SSH key type for [Source control setup](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control)
.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/source-control#related-resources)

------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
    

[PreviousSecurity](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/security)
[NextSSO](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/sso)

Last updated 10 days ago

Was this helpful?