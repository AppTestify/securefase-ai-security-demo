# SecureFase AI Security Demo

Intentionally insecure sample app for **SecureFase AI Security** product demos.

Do not deploy this. It is meant to be scanned so the AI Security overview, inventory, and risks tabs light up with real findings.

## What the scanner should find

| Area | Example files |
| --- | --- |
| Ungoverned SDKs / models | `package.json`, `requirements.txt`, `src/api/summarise.ts` |
| Prompt injection | `src/api/summarise.ts`, `src/api/ask.py` |
| Model output → exec / shell | `src/agents/run.py`, `src/agents/run.ts` |
| Excessive agency | `src/agents/ops.py` |
| Sensitive data in prompts | `src/svc/kyc.py` |
| Prompt / response logging | `src/svc/chat.ts` |
| Unsafe model load | `src/ml/load.py` |
| Vector store / shadow keys | `requirements.txt`, `.env.example` |
| Unpinned MCP servers | `.cursor/mcp.json` |
| IaC cloud misconfigs | `infra/terraform/aws/main.tf`, `infra/k8s/` |

## Demo account

Connected to the SecureFase **demo** workspace (`demo` / `demo@securefase.com`).

Run **AI** and **IAC** scans against this repo. Live cloud posture in the demo workspace uses stub AWS/Azure accounts (not this git tree).

## Safe to share

All secrets and identifiers here are **fake fixtures** (`sk-fixture-…`). They exist only so scanners can demonstrate detection.
