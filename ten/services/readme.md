Design notes and measurement guidance:

- Request flow: Client -> compression middleware -> memory cache -> Redis cache -> DB (lean, select fields, skip/limit) -> response
- Each optimization reduces latency: compression reduces payload size and bandwidth; caches reduce DB hits; lean/select/skip-limit reduce DB CPU and network.
- Measure using: `autocannon` or `wrk` for load; `mongotop`/`mongostat` for DB; Redis `INFO` for hits; APM traces for p95/p99 latency.
- Suggested experiment: baseline 1) no cache, no compression; 2) add compression; 3) add memory cache warm; 4) add Redis; compare throughput and p95 latency.
