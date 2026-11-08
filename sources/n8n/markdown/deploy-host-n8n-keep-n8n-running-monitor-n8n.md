For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/monitor-n8n.md)
.

There are three API endpoints you can call to check the status of your instance: `/healthz`, `healthz/readiness`, and `/metrics`.

healthz and healthz/readiness[](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/monitor-n8n#healthz-and-healthzreadiness)

-------------------------------------------------------------------------------------------------------------------------------

The `/healthz` endpoint returns a standard HTTP status code. 200 indicates the instance is reachable. It doesn't indicate DB status. It's available for both self-hosted and Cloud users.

Access the endpoint:

Copy

    <your-instance-url>/healthz

The `/healthz/readiness` endpoint is similar to the `/healthz` endpoint, but it returns a HTTP status code of 200 if the DB is connected and migrated and therefore the instance is ready to accept traffic.

Access the endpoint:

Copy

    <your-instance-url>/healthz/readiness

**Customizing health check endpoints**

You can customize the health check endpoint path using the [`N8N_ENDPOINT_HEALTH`](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints)
 environment variable.

metrics[](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/monitor-n8n#metrics)

------------------------------------------------------------------------------------

The `/metrics` endpoint provides more detailed information about the current status of the instance.

Access the endpoint:

Copy

    <your-instance-url>/metrics

**Feature availability**

The `/metrics` endpoint is available on:

*   **Self-hosted:** All editions
    

It isn't available on n8n Cloud.

How do I enable metrics and health checks?[](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/monitor-n8n#enable-metrics-and-health-checks-for-self-hosted-n8n)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `/metrics` endpoint is disabled by default. The health endpoint is always enabled on the main n8n server. For worker servers in [queue mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode)
, the health endpoint is disabled by default.

To enable them, configure your n8n instance:

Copy

    # metrics <a href="#metrics" id="metrics"></a>
    N8N_METRICS=true
    # healthz <a href="#healthz" id="healthz"></a>
    QUEUE_HEALTH_CHECK_ACTIVE=true

Refer to [Configuration methods](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration)
 for more information on how to configure your instance using environment variables.

Related resources[](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/monitor-n8n#related-resources)

--------------------------------------------------------------------------------------------------------

*   [Keep n8n running](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running)
    
*   [Set up logging](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/set-up-logging)
    
*   [Visualize metrics with Grafana](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/visualize-metrics-with-grafana)
    
*   [Back up and restore](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/backup-and-restore)
    
*   [Update n8n](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/update-n8n)
    
*   [Trace executions with OpenTelemetry](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/trace-executions-with-opentelemetry)
    

[PreviousSet up logging](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/set-up-logging)
[NextVisualize metrics with Grafana](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/visualize-metrics-with-grafana)

Last updated 10 days ago

Was this helpful?