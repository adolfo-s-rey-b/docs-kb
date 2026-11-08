For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-hooks.md)
.

**File-based configuration**

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration#keeping-sensitive-data-in-separate-files)
 for more details.

You can define external hooks that n8n executes whenever a specific operation runs. Refer to [External hooks](https://docs.n8n.io/deploy/host-n8n/configure-n8n/external-hooks)
 for the full reference, including available hooks and file formatting.

Variable

Type

Default

Description

`EXTERNAL_HOOK_FILES`

String

\-

Files containing backend external hooks. Provide multiple files separated by the character defined in `EXTERNAL_HOOK_FILES_SEPARATOR`.

`EXTERNAL_HOOK_FILES_SEPARATOR`

String

`:`

Separator character for `EXTERNAL_HOOK_FILES`. Use `;` on Windows to avoid conflicts with drive-letter paths like `C:\`.

`EXTERNAL_FRONTEND_HOOKS_URLS`

String

\-

URLs to files containing frontend external hooks. Provide multiple URLs as a colon-separated list ("`:`").

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-hooks#related-resources)

------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
    

[PreviousExternal data storage](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-data-storage)
[NextExternal secrets](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-secrets)

Last updated 10 days ago

Was this helpful?