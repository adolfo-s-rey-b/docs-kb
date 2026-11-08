For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode.md)
.

You can run n8n in different modes depending on your needs. The queue mode provides the best scalability.

**Binary data storage**

n8n doesn't support queue mode with binary data storage in filesystem. If your workflows need to persist binary data in queue mode, you can use [S3 external storage](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/use-external-storage)
.

How it works[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#how-it-works)

---------------------------------------------------------------------------------------------------------

When running in queue mode, you have multiple n8n instances set up, with one main instance receiving workflow information (such as triggers) and the worker instances performing the executions.

Each worker is its own Node.js instance, running in `main` mode, but able to handle multiple simultaneous workflow executions due to their high IOPS (input-output operations per second).

By using worker instances and running in queue mode, you can scale n8n up (by adding workers) and down (by removing workers) as needed to handle the workload.

This is the process flow:

1.  The main n8n instance handles timers and webhook calls, generating (but not running) a workflow execution.
    
2.  It passes the execution ID to a message broker, [Redis](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#start-redis)
    , which maintains the queue of pending executions and allows the next available worker to pick them up.
    
3.  A worker in the pool picks up message from Redis.
    
4.  The worker uses the execution ID to get workflow information from the database.
    
5.  After completing the workflow execution, the worker:
    
    *   Writes the results to the database.
        
    *   Posts to Redis, saying that the execution has finished.
        
    
6.  Redis notifies the main instance.
    

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2773773108-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fjm0ZYRpZIPWge2ZSiDYO%252Fuploads%252Fgit-blob-59811a80e5d001a2ec6c66a978626feac27b0637%252Fqueue-mode-flow.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d4a7e235844d9a18b01aebd997cc7f97&sv=3)

Diagram showing the flow of data between the main n8n instance, Redis, the n8n workers, and the n8n database

Configuring workers[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#configuring-workers)

-----------------------------------------------------------------------------------------------------------------------

Workers are n8n instances that do the actual work. They receive information from the main n8n process about the workflows that have to get executed, execute the workflows, and update the status after each execution is complete.

**Per-process event log files**

If your workers share a writable filesystem, give each worker process a unique event log path. Refer to [Per-process event log files](https://docs.n8n.io/administer/observe-and-log/stream-logs-to-external-systems#per-process-event-log-files)
 for details.

### Set encryption key[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#set-encryption-key)

n8n automatically generates an encryption key upon first startup. You can also provide your own custom key using [environment variable](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
 if desired.

The encryption key of the main n8n instance must be shared with all worker and webhooks processor nodes to ensure these worker nodes are able to access credentials stored in the database.

Set the encryption key for each worker node in a [configuration file](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration)
 or by setting the corresponding environment variable:

Copy

    export N8N_ENCRYPTION_KEY=<main_instance_encryption_key>

### Set executions mode[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#set-executions-mode)

**Database considerations** Refer to [Supported PostgreSQL versions](https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database#supported-postgresql-versions)
 for n8n's supported PostgreSQL versions.

Running n8n with execution mode set to `queue` with an SQLite database isn't recommended.

Set the environment variable `EXECUTIONS_MODE` to `queue` on the main instance and any workers using the following command.

Copy

    export EXECUTIONS_MODE=queue

Alternatively, you can set `executions.mode` to `queue` in the [configuration file](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
.

### Start Redis[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#start-redis)

**Running Redis on a separate machine**

You can run Redis on a separate machine, just make sure that it's accessible by the n8n instance.

To run Redis in a Docker container, follow the instructions below:

Run the following command to start a Redis instance:

Copy

    docker run --name some-redis -p 6379:6379  -d redis

By default, Redis runs on `localhost` on port `6379` with no password. Based on your Redis configuration, set the following configurations for the main n8n process. These will allow n8n to interact with Redis.

Using configuration file

Using environment variables

Description

`queue.bull.redis.host:localhost`

`QUEUE_BULL_REDIS_HOST=localhost`

By default, Redis runs on `localhost`.

`queue.bull.redis.port:6379`

`QUEUE_BULL_REDIS_PORT=6379`

The default port is `6379`. If Redis is running on a different port, configure the value.

You can also set the following optional configurations:

Using configuration file

Using environment variables

Description

`queue.bull.redis.username:USERNAME`

`QUEUE_BULL_REDIS_USERNAME`

By default, Redis doesn't require a username. If you're using a specific user, configure it variable.

`queue.bull.redis.password:PASSWORD`

`QUEUE_BULL_REDIS_PASSWORD`

By default, Redis doesn't require a password. If you're using a password, configure it variable.

`queue.bull.redis.db:0`

`QUEUE_BULL_REDIS_DB`

The default value is `0`. If you change this value, update the configuration.

`queue.bull.redis.timeoutThreshold:10000ms`

`QUEUE_BULL_REDIS_TIMEOUT_THRESHOLD`

Tells n8n how long it should wait if Redis is unavailable before exiting. The default value is `10000` (ms).

`queue.bull.gracefulShutdownTimeout:30`

`N8N_GRACEFUL_SHUTDOWN_TIMEOUT`

A graceful shutdown timeout for workers to finish executing jobs before terminating the process. The default value is `30` seconds.

Now you can start your n8n instance and it will connect to your Redis instance.

### Start workers[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#start-workers)

You will need to start worker processes to allow n8n to execute workflows. If you want to host workers on a separate machine, install n8n on the machine and make sure that it's connected to your Redis instance and the n8n database.

Start worker processes by running the following command from the root directory:

Copy

    ./packages/cli/bin/n8n worker

If you're using Docker, use the following command:

Copy

    docker run --name n8n-queue -p 5679:5678 n8nio/n8n worker

You can set up multiple worker processes. Make sure that all the worker processes have access to Redis and the n8n database.

#### Worker server[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#worker-server)

Each worker process runs a server that exposes optional endpoints:

*   `/healthz`: returns whether the worker is up, if you enable the `QUEUE_HEALTH_CHECK_ACTIVE` environment variable
    
*   `/healthz/readiness`: returns whether worker's DB and Redis connections are ready, if you enable the `QUEUE_HEALTH_CHECK_ACTIVE` environment variable
    
*   [credentials overwrite endpoint](https://docs.n8n.io/administer/manage-credentials/credential-overwrites)
    
*   [`/metrics`](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/enable-prometheus-metrics)
    

**Customizing health check endpoints**

You can customize the health check endpoint path using the [`N8N_ENDPOINT_HEALTH`](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints)
 environment variable.

#### View running workers[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#view-running-workers)

**Feature availability**

Viewing running workers is available on:

*   **Self-hosted:** Enterprise
    

On n8n Cloud Enterprise, [contact n8n](https://n8n-community.typeform.com/to/y9X2YuGa)
 to enable it.

You can view running workers and their performance metrics in n8n by selecting **Settings** > **Workers**.

Running n8n with queues[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#running-n8n-with-queues)

-------------------------------------------------------------------------------------------------------------------------------

When running n8n with queues, all the production workflow executions get processed by worker processes. For webhooks, this means the HTTP request is received by the main/webhook process, but the actual workflow execution is passed to a worker, which can add some overhead and latency.

Redis acts as the message broker, and the database persists data, so access to both is required. Running a distributed system with this setup over SQLite isn't supported.

**Migrate data**

If you want to migrate data from one database to another, you can use the Export and Import commands. Refer to the [CLI commands for n8n](https://docs.n8n.io/deploy/host-n8n/configure-n8n/use-the-command-line#export-workflows-and-credentials)
 documentation to learn how to use these commands.

Webhook processors[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#webhook-processors)

---------------------------------------------------------------------------------------------------------------------

**Keep in mind**

Webhook processes rely on Redis and need the `EXECUTIONS_MODE` environment variable set too. Follow the [configure the workers](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#configuring-workers)
 section above to setup webhook processor nodes.

Webhook processors are another layer of scaling in n8n. Configuring the webhook processor is optional, and allows you to scale the incoming webhook requests.

This method allows n8n to process a huge number of parallel requests. All you have to do is add more webhook processes and workers accordingly. The webhook process will listen to requests on the same port (default: `5678`). Run these processes in containers or separate machines, and have a load balancing system to route requests accordingly.

n8n doesn't recommend adding the main process to the load balancer pool. If you add the main process to the pool, it will receive requests and possibly a heavy load. This will result in degraded performance for editing, viewing, and interacting with the n8n UI.

You can start the webhook processor by executing the following command from the root directory:

Copy

    ./packages/cli/bin/n8n webhook

If you're using Docker, use the following command:

Copy

    docker run --name n8n-queue -p 5679:5678 -e "EXECUTIONS_MODE=queue" n8nio/n8n webhook

### Configure webhook URL[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#configure-webhook-url)

To configure your webhook URL, execute the following command on the machine running the main n8n instance:

Copy

    export N8N_WEBHOOK_URL=https://your-webhook-url.com

`N8N_WEBHOOK_URL` is available from n8n 2.30.0; on earlier versions, use `WEBHOOK_URL`.

You can also set this value in the configuration file.

### Configure load balancer[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#configure-load-balancer)

When using multiple webhook processes you will need a load balancer to route requests. If you are using the same domain name for your n8n instance and the webhooks, you can set up your load balancer to route requests as follows:

*   Redirect webhook triggers to the webhook servers pool. Paths to consider:
    
    *   `/webhook/*`: Webhook trigger node endpoints
        
    *   `/webhook-waiting/*`: Human-in-the-loop webhook endpoints used by nodes that perform "send and wait" operations (for example, the Slack node).
        
    
*   All other paths (the n8n internal API, the static files for the editor, etc.) should get routed to the main process
    

**Note:** The default URL for manual workflow executions is `/webhook-test/*`. Make sure that these URLs route to your main process.

You can change this path in the configuration file `endpoints.webhook` or using the `N8N_ENDPOINT_WEBHOOK` environment variable. If you change these, update your load balancer accordingly.

### Disable webhook processing in the main process (optional)[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#disable-webhook-processing-in-the-main-process-optional)

You have webhook processors to execute the workflows. You can disable the webhook processing in the main process. This will make sure to execute all webhook executions in the webhook processors. In the configuration file set `endpoints.disableProductionWebhooksOnMainProcess` to `true` so that n8n doesn't process webhook requests on the main process.

Alternatively, you can use the following command:

Copy

    export N8N_DISABLE_PRODUCTION_MAIN_PROCESS=true

When disabling the webhook process in the main process, run the main process and don't add it to the load balancer's webhook pool.

Large webhook responses[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#large-webhook-responses)

-------------------------------------------------------------------------------------------------------------------------------

In queue mode, a worker runs the execution, but the client that sent the webhook request stays connected to the main or webhook instance. A response from a **Respond to Webhook** node travels from the worker back to that instance inside a queue message, so Redis holds the whole response while the message is in flight.

`N8N_WEBHOOK_RESPONSE_RELAY_SIZE_MAX` sets how large that message can be, in MiB. It defaults to `64`. Redis holds several copies of a response in flight, so budget about 1.5 times this value in Redis memory for each response in flight. Without offloading, a response above the limit fails the node.

The same limit applies to a tool result an MCP Trigger workflow returns from a worker. You can't offload a tool result, so an oversized one reaches the MCP client as a tool error naming the limit.

### Offload a large response body to storage[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#offload-a-large-response-body-to-storage)

**Available from n8n 2.34.0**

Set `N8N_WEBHOOK_RESPONSE_RELAY_OFFLOAD_ENABLED=true` on your workers to store a response body above the limit in [binary data storage](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/binary-data)
 instead of failing the node. The queue message then carries a reference, the main instance streams the body from storage to the client, and n8n deletes the stored body once it delivers the response.

Offloading needs storage that every instance can read. Every mode except `default` stores, so set `N8N_DEFAULT_BINARY_DATA_MODE` to `filesystem`, `database`, `s3`, or `azure`:

Copy

    export N8N_WEBHOOK_RESPONSE_RELAY_SIZE_MAX=64
    export N8N_WEBHOOK_RESPONSE_RELAY_OFFLOAD_ENABLED=true
    export N8N_DEFAULT_BINARY_DATA_MODE=s3

n8n recommends `s3` or `azure` for large responses. Both stream the body, so the main instance holds one chunk at a time. Refer to [External storage](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/use-external-storage)
 for how to configure them. In `database` mode, the main instance loads the whole body into memory before sending it, and the response passes through your primary database. In `filesystem` mode, every instance needs to mount the same disk, which n8n doesn't recommend. The `default` mode keeps binary data in memory, so there's nothing for the main instance to read, and a response above the limit still fails the node.

n8n only offloads the response body. It measures the rest of the response, its headers and status code, against the same limit, so a response whose headers alone exceed the limit fails either way.

### Turn on offloading during an upgrade[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#turn-on-offloading-during-an-upgrade)

Only a main instance running n8n 2.34.0 or later reads an offloaded body. An older one returns the storage reference to the client instead of the response body. Upgrade every main and webhook instance first, then set `N8N_WEBHOOK_RESPONSE_RELAY_OFFLOAD_ENABLED` on your workers. A worker with the variable unset sends every response inline and fails one above the limit.

### Troubleshoot large webhook responses[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#troubleshoot-large-webhook-responses)

Error

Cause

Fix

`The response is too large to be sent back from the worker`, naming `N8N_WEBHOOK_RESPONSE_RELAY_OFFLOAD_ENABLED`

Offloading is off on the worker.

Set the variable on your workers, or raise `N8N_WEBHOOK_RESPONSE_RELAY_SIZE_MAX`.

`The response is too large to be sent back from the worker`, naming `N8N_DEFAULT_BINARY_DATA_MODE`

Binary data storage keeps data in memory, so there's nowhere to offload to.

Set `N8N_DEFAULT_BINARY_DATA_MODE` to `filesystem`, `database`, `s3`, or `azure`.

`The response is too large for the binary-data store to hold`

`database` mode refused the body for its own size limit.

Raise `N8N_BINARY_DATA_DATABASE_MAX_FILE_SIZE`, up to the 1 GB a database column holds, or switch to `filesystem`, `s3`, or `azure`, which apply no limit of their own.

`The stored webhook response body could not be read`

The main instance can't read the storage the worker wrote to.

Point every instance at the same storage. In `filesystem` mode, every instance needs to mount the same disk, which n8n doesn't recommend.

Configure worker concurrency[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#configure-worker-concurrency)

-----------------------------------------------------------------------------------------------------------------------------------------

You can define the number of jobs a worker can run in parallel by using the `concurrency` flag. It defaults to `10`. To change it:

Copy

    n8n worker --concurrency=5

Concurrency and scaling recommendations[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#concurrency-and-scaling-recommendations)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

n8n recommends setting concurrency to 5 or higher for your worker instances. Setting low concurrency values with a large numbers of workers can exhaust your database's connection pool, leading to processing delays and failures.

Multi-main setup[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#multi-main-setup)

-----------------------------------------------------------------------------------------------------------------

**Feature availability**

Multi-main setup is available on:

*   **Self-hosted:** Enterprise
    

It isn't available on n8n Cloud.

In queue mode you can run more than one `main` process for high availability.

In a single-mode setup, the `main` process does two sets of tasks:

*   **regular tasks**, such as running the API, serving the UI, and listening for webhooks, and
    
*   **at-most-once tasks**, such as running non-HTTP triggers (timers, pollers, and persistent connections like RabbitMQ and IMAP), and pruning executions and binary data.
    

In a multi-main setup, there are two kinds of `main` processes:

*   **followers**, which run **regular tasks**, and
    
*   the **leader**, which runs **both regular and at-most-once tasks**.
    

### Leader designation[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#leader-designation)

In a multi-main setup, all main instances handle the leadership process transparently to users. In case the current leader becomes unavailable, for example because it crashed or its event loop became too busy, other followers can take over. If the previous leader becomes responsive again, it becomes a follower.

### Configuring multi-main setup[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#configuring-multi-main-setup)

To deploy n8n in multi-main setup, ensure:

*   All `main` processes are running in queue mode and are connected to Postgres and Redis.
    
*   All `main` and `worker` processes are running the same version of n8n.
    
*   All `main` processes have set the environment variable `N8N_MULTI_MAIN_SETUP_ENABLED` to `true`.
    
*   All `main` processes are running behind a load balancer with session persistence (sticky sessions) enabled.
    

If needed, you can adjust the leader key options:

Using configuration file

Using environment variables

Description

`multiMainSetup.ttl:10`

`N8N_MULTI_MAIN_SETUP_KEY_TTL=10`

Time to live (in seconds) for leader key in multi-main setup.

`multiMainSetup.interval:3`

`N8N_MULTI_MAIN_SETUP_CHECK_INTERVAL=3`

Interval (in seconds) for leader check in multi-main setup.

For a reference multi-main deployment on AWS, including worker autoscaling and Redis high availability, see [Scale and run at high availability on AWS](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform/scale-and-run-at-high-availability)
.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode#related-resources)

-------------------------------------------------------------------------------------------------------------------

*   [Scaling](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling)
    
*   [Measure performance](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/measure-performance)
    
*   [Control concurrency](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/control-concurrency)
    
*   [Manage execution data](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/manage-execution-data)
    
*   [Handle binary data](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/handle-binary-data)
    
*   [Use external storage](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/use-external-storage)
    
*   [Fix memory issues](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/fix-memory-issues)
    

[PreviousMeasure performance](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/measure-performance)
[NextControl concurrency](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/control-concurrency)

Last updated 5 days ago

Was this helpful?