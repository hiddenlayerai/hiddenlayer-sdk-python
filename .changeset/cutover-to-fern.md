---
"hiddenlayer-sdk-python-ledger": major
---

Generate the SDK with Fern. The package name, the `HiddenLayer` and `AsyncHiddenLayer` clients, their environment variables, the model and community scanners and the red team sessions stay; Python 3.10 is now the minimum, `bearer_token` becomes `token`, response types are named after the API's schemas, errors derive from `ApiError`, per-request options move into `request_options`, `scans.jobs.list` and `sensors.query` return pagers, and every public API in the specification is now covered. [docs/BREAKING_CHANGES_v4.0.0.md](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/blob/main/docs/BREAKING_CHANGES_v4.0.0.md) lists every change.
