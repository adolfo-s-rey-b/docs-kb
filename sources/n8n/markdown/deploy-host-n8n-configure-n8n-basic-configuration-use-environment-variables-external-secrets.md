For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-secrets.md)
.

**File-based configuration**

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration#keeping-sensitive-data-in-separate-files)
 for more details.

You can use an external secrets store to manage credentials for n8n. Refer to [External secrets](https://docs.n8n.io/administer/manage-credentials/use-external-secret-stores)
 for details.

Variable

Type

Default

Description

`N8N_EXTERNAL_SECRETS_UPDATE_INTERVAL`

Number

`300` (5 minutes)

How often (in seconds) to check for secret updates.

`N8N_EXTERNAL_SECRETS_CONNECT_TIMEOUT`

Number

`20`

Maximum time (in seconds) n8n waits for a secrets vault to connect. If the vault doesn't answer in time, n8n marks it as errored, retries the connection in the background with increasing delays, and startup continues without its secrets. Available from n8n 2.41.0.

`N8N_EXTERNAL_SECRETS_REFRESH_TIMEOUT`

Number

`20`

Maximum time (in seconds) n8n waits for a secrets vault to deliver its secrets, at startup and on each update interval. If the fetch takes longer, n8n stops waiting and the fetch keeps running in the background. When it completes successfully, n8n stores the secrets. At startup, workflows that use secrets from that vault fail until the first fetch completes. On an update interval, the previously fetched secrets stay available. Increase this value for vaults with many secrets. For HashiCorp Vault and Infisical, n8n also cancels each single HTTP request after the larger of the two timeouts. Available from n8n 2.41.0.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-secrets#related-resources)

--------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
    

[PreviousExternal hooks](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-hooks)
[NextInsights](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/insights)

Last updated 10 days ago

Was this helpful?