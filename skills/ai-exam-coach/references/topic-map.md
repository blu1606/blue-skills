# Topic Map

Use this map to select and tag questions. Add project-specific topics when the KB contains them.

## Common Section

- AI design patterns: AI workflow design, human-in-the-loop, fallback, routing, evaluator-optimizer, guardrails.
- RAG pipeline: chunking, embeddings, vector search, hybrid retrieval, reranking, context packing, hallucination reduction.
- Prompt engineering: role/context/output constraints, few-shot, Chain-of-Thought, tool calling, structured outputs, prompt injection defense.
- Agent architecture: ReAct, planner-executor, tool use, memory, multi-agent coordination, state graphs, retry/fallback, loop detection.
- Observability: logs, metrics, traces, correlation ID, latency percentiles, cost tracking, quality metrics, drift detection.
- AI security: prompt injection, data exfiltration, PII handling, authorization, sandboxing, supply-chain risks, eval/guardrail gates.

## Business Track

- Product management: problem framing, user workflow, KPI mapping, non-AI baseline, MVP scope, adoption.
- ROI: cost-benefit, automation value, productivity measurement, risk-adjusted ROI, build-vs-buy.
- AI roadmap: prioritization, data readiness, capability maturity, risk milestones, governance checkpoints.
- Regulation and compliance: EU AI Act risk classes, GDPR-style privacy principles, Vietnam AI/legal context, audit evidence.
- Change management: stakeholder mapping, training, operating model, escalation, accountability.

## Infrastructure Track

- Data lakehouse: bronze/silver/gold, Delta/Iceberg/Hudi concepts, batch vs streaming, data quality, governance.
- GPU FinOps: utilization, right-sizing, quantization, batching, spot/preemptible trade-offs, cost attribution.
- Model serving: TTFT, TPOT, throughput vs goodput, KV cache, PagedAttention, vLLM/SGLang/llama.cpp/TensorRT-LLM concepts.
- CI/CD for AI: eval gates, prompt/version control, model registry, canary/shadow deploy, rollback, reproducibility.
- Security for AI infra: secrets, RBAC, network isolation, artifact scanning, logging without PII, audit trails.

## App Build Track

- Advanced agents: stateful workflows, LangGraph-style graph/state, tool schemas, memory, HITL, error recovery.
- Advanced RAG: query rewriting, multi-hop retrieval, GraphRAG, metadata filtering, contextual compression, evaluation.
- LoRA/QLoRA: PEFT rationale, adapters, rank/alpha/dropout, NF4, quantization trade-offs, when not to fine-tune.
- RAGAS and eval metrics: faithfulness, answer relevancy, context precision, context recall, LLM-as-judge bias.
- Code challenge: Python, NumPy, Pandas, data processing, API glue, parsing, simple evaluation scripts.

## Personal Weakness Tags

Use these tags when KB evidence shows prior misses:
- math-bayes, math-chain-rule, math-log, matrix-vector.
- python-gotchas, list-comprehension, pandas-groupby, numpy-cosine.
- metric-precision-recall-f1, data-leakage, drift-concepts.
- bert-vs-gpt, hallucination-cause, rag-pipeline, agent-failure.
- fairness-metrics, privacy, eu-ai-act, ai-governance.
