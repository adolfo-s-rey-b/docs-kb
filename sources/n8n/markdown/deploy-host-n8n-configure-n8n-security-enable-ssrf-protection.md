For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/enable-ssrf-protection.md)
.

**Feature availability**

SSRF protection is available from n8n 2.12.0.

Server-Side Request Forgery (SSRF) attacks abuse workflow nodes to make requests to internal network resources, cloud metadata endpoints, or localhost services that shouldn't be accessible.

SSRF protection is an additional application-level defense. You should always configure network-level protections (firewalls, security groups, network policies) on your infrastructure as your primary line of defense. n8n's SSRF protection adds defense-in-depth on top of those controls.

Enable SSRF protection[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/enable-ssrf-protection#enable-ssrf-protection)

-----------------------------------------------------------------------------------------------------------------------------------

Copy

    N8N_SSRF_PROTECTION_ENABLED=true

When enabled, n8n validates all outbound HTTP requests from user-controllable nodes (such as the HTTP Request node) against the configured blocked and allowed ranges. This includes redirect targets and DNS resolution to prevent bypass techniques like DNS rebinding.

Default blocked ranges[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/enable-ssrf-protection#default-blocked-ranges)

-----------------------------------------------------------------------------------------------------------------------------------

When SSRF protection is enabled, the following IP ranges are blocked by default:

Range

Description

`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`

RFC 1918 private addresses

`127.0.0.0/8`, `::1/128`

Loopback

`169.254.0.0/16`, `fe80::/10`

Link-local

`fc00::/7`, `fd00::/8`

IPv6 unique local

`0.0.0.0/8`, `192.0.0.0/24`, `192.0.2.0/24`, `198.18.0.0/15`, `198.51.100.0/24`, `203.0.113.0/24`

Reserved/special purpose

You can extend this list with `N8N_SSRF_BLOCKED_IP_RANGES=default,100.0.0.0/8`.

Allow access to internal services[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/enable-ssrf-protection#allow-access-to-internal-services)

---------------------------------------------------------------------------------------------------------------------------------------------------------

If your workflows need to reach legitimate internal services, use allowlists. Allowlists take precedence over blocklists, following this order: hostname allowlist > IP allowlist > IP blocklist.

Allow by hostname pattern (supports wildcards like `*.n8n.internal`):

Copy

    N8N_SSRF_ALLOWED_HOSTNAMES=*.n8n.internal,*.company.local

Allow by IP range:

Copy

    N8N_SSRF_ALLOWED_IP_RANGES=10.0.1.0/24,10.0.2.50/32

Only allowlist hostnames within your control (internal DNS zones). Hostname allowlists bypass IP blocklist checks.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/enable-ssrf-protection#related-resources)

-------------------------------------------------------------------------------------------------------------------------

*   [Security](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security)
    : audit, harden, and restrict a self-hosted instance.
    
*   [SSRF protection environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ssrf-protection)
    : the full list of configuration options.
    
*   [Configuration methods](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration)
    : more information on setting environment variables.
    

[PreviousVerify user emails](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/verify-user-emails)
[NextRotate encryption keys](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/rotate-encryption-keys)

Last updated 10 days ago

Was this helpful?