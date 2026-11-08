For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/specify-user-folder-path.md)
.

n8n saves user-specific data like the encryption key, SQLite database file, and the ID of the tunnel (if used) in the subfolder `.n8n` of the user who started n8n. It's possible to overwrite the user-folder using an environment variable.

Copy

    export N8N_USER_FOLDER=/home/jim/n8n

Refer to [Environment variables reference](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment)
 for more information on this variable.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/specify-user-folder-path#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Configuration examples](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples)
    

[PreviousSet the timezone](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-the-timezone)
[NextConfigure webhook URLs with reverse proxy](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-webhook-urls-with-reverse-proxy)

Last updated 10 days ago

Was this helpful?