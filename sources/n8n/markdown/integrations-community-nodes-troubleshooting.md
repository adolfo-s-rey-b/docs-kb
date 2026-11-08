For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/community-nodes/troubleshooting.md)
.

Error: Missing packages[](https://docs.n8n.io/integrations/community-nodes/troubleshooting#error-missing-packages)

-------------------------------------------------------------------------------------------------------------------

n8n installs community nodes directly onto the hard disk. The files must be available at startup for n8n to load them. If the packages aren't available at startup, you get an error warning of missing packages.

If running n8n using Docker: depending on your Docker setup, you may lose the packages when you recreate your container or upgrade your n8n version. You must either:

*   Persist the contents of the `~/.n8n/nodes` directory. This is the best option. If you follow the [Docker installation](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker)
     guide, the setup steps include persisting this directory.
    
*   Set the `N8N_REINSTALL_MISSING_PACKAGES` environment variable to `true`.
    

The second option might increase startup time and may cause health checks to fail.

Prevent loading community nodes on n8n cloud[](https://docs.n8n.io/integrations/community-nodes/troubleshooting#prevent-loading-community-nodes-on-n8n-cloud)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

If your n8n Cloud instance crashes and fails to start, you can prevent installed community nodes from loading on instance startup. In the [n8n Cloud console](https://docs.n8n.io/deploy/use-n8n-cloud/use-the-cloud-console)
, go to **Instance settings**, turn on **Disable all community nodes**, then select **Save and restart**. This setting is only visible when **Verified community nodes** is on. If your instance is offline, you can still [sign in to the Cloud console with a magic link](https://docs.n8n.io/deploy/use-n8n-cloud/use-the-cloud-console#open-the-cloud-console-with-a-magic-link)
.

[PreviousUsing community nodes](https://docs.n8n.io/integrations/community-nodes/using-community-nodes)
[NextBuilding community nodes](https://docs.n8n.io/integrations/community-nodes/building-community-nodes)

Last updated 10 days ago

Was this helpful?