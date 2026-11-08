For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/control-telemetry.md)
.

n8n collects anonymous telemetry data from self-hosted n8n installations. You can opt out of data telemetry collection.

Collected data[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/control-telemetry#collected-data)

--------------------------------------------------------------------------------------------------------------

Refer to [Privacy | Data collection in self-hosted n8n](https://docs.n8n.io/privacy-and-security#data-collection-in-self-hosted-n8n)
 for details on the data n8n collects.

How collection works[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/control-telemetry#how-collection-works)

--------------------------------------------------------------------------------------------------------------------------

n8n sends most data when events occur. Workflow execution counts and an instance pulse are sent periodically (every 6 hours).

Opting out of data collection[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/control-telemetry#opting-out-of-data-collection)

--------------------------------------------------------------------------------------------------------------------------------------------

n8n enables telemetry collection by default. To disable it, configure the following environment variables.

### Opt out of telemetry events[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/control-telemetry#opt-out-of-telemetry-events)

To opt out of diagnostic telemetry, set the `N8N_DIAGNOSTICS_ENABLED` environment variable to false:

Copy

    export N8N_DIAGNOSTICS_ENABLED=false

### Opt out of checking for new versions of n8n[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/control-telemetry#opt-out-of-checking-for-new-versions-of-n8n)

To opt out of version notifications, set the `N8N_VERSION_NOTIFICATIONS_ENABLED` environment variable to false:

Copy

    export N8N_VERSION_NOTIFICATIONS_ENABLED=false

Disable all connection to n8n servers[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/control-telemetry#disable-all-connection-to-n8n-servers)

------------------------------------------------------------------------------------------------------------------------------------------------------------

To prevent all communication with n8n's servers, refer to [Isolate n8n](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/isolate-n8n)
.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/control-telemetry#related-resources)

--------------------------------------------------------------------------------------------------------------------

*   [Security](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security)
    : audit, harden, and restrict a self-hosted instance.
    
*   [Deployment environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment)
    : More information on these environment variables.
    
*   [Configuration](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration)
    : How to set environment variables.
    

[PreviousDisable the public API](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/disable-the-public-api)
[NextBlock specific nodes](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/block-specific-nodes)

Last updated 10 days ago

Was this helpful?