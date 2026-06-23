# Harness Engineering 最新论文速读（2026）

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Agent Engineering |
| 材料类型 | 前沿 / 论文速读 |
| 难度 | 前沿 |
| 优先级 | P1 / Frontier |
| 状态 | 可用 |
| 建议用途 | 跟进 Harness Engineering 最新研究方向 |

---

> 返回主文档：[Harness Engineering（驭缰工程）学习资料](harness-engineering.md)
> 更新时间：2026-05-23
> 来源：arXiv 元数据与摘要；仅收录公开外网论文链接。
> 主题：Agent Harness / Harness Engineering / Coding-Agent Harness / 运行时适配 / 安全审计 / 自动演化。

## 先看结论

2026 年 3-5 月，Harness Engineering 已经从“工程经验词”快速变成一个可研究对象，出现了几条清晰主线：

1. **Harness 可表示化**：从隐藏在 controller 里的胶水代码，变成可编辑、可检查、可迁移、可消融的对象。
2. **Harness 可自动演化**：通过轨迹、组件和决策的可观测性，让 agent 自己改进工具、中间件、记忆和流程。
3. **Harness 是对齐与安全边界**：正确答案不等于安全轨迹，执行过程的越权访问、上下文泄漏、资源使用需要被审计。
4. **Harness 可能比模型大小更关键**：一些论文开始把性能差距解释为运行基座、工具接口、反馈回路与验证门控的差异。
5. **领域专用 Harness 爆发**：科研、可视化、算法发现、有限元仿真、搜索等场景都在出现专门 harness。

## 必读论文

### 1. Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses

- **arXiv**：[2604.25850](https://arxiv.org/abs/2604.25850)
- **时间**：2026-04-28（updated: 2026-05-18）
- **作者**：Jiahang Lin, Shichun Liu, Chengjun Pan, Lizhi Lin, Shihan Dou, Zhiheng Xi et al.
- **分类**：自动演化 / Observability
- **一句话价值**：提出 AHE 闭环，用组件可观测、经验可观测、决策可观测让 harness 修改变成可验证契约；强调工具、中间件、长期记忆比系统提示更能迁移。
- **摘要要点**：Harnesses are now central to coding-agent performance, mediating how models interact with tools and execution environments. Yet harness engineering remains a manual craft, because automating it faces a heterogeneous action space across editable components, voluminous trajectories that bury actionable signal, and edits whose effect is hard to attribute. We introduce Agentic Harness Engineering (AHE), a closed loop that addresses these challenges through three matched observability pillars: (1) component observability gives every editable harness component a file-level representation so the action space is explicit and revertible; (2) experience observability distills millions of raw trajectory tokens into a layered, drill-down evidence corpus that an evolving agent can actually consume; and (3) decision observability pairs every edit with a self-declared prediction, later verified against the next round's task-level outcomes. Together, these pillars turn every edit into a falsifiable contract, so harness evolution proceeds autonomously without collapsing into trial-and-error. Empirically, ten AHE iterations lift pass@1 on Terminal-Bench 2 from 69.7% to 77.0%, surpassing the human-designed harness Codex-CLI (71.9%) and the self-evolving baselines ACE and TF-GRPO. The frozen harness transfers without re-evolution: on SWE-bench-verified it tops aggregate success at 12% fewer tokens than the seed, and on Terminal-Bench 2 it yields +5.1 to +10.1pp cross-family gains across three alternate model families, indicating the evolved components encode general engineering experience rather than benchmark-specific tuning. Ablations localize the gain to tools, middleware, and long-term memory rather than the system prompt, suggesting factual harness structure transfers while prose-level strategy does not.

### 2. Natural-Language Agent Harnesses

- **arXiv**：[2603.25723](https://arxiv.org/abs/2603.25723)
- **时间**：2026-03-26（updated: 2026-05-18）
- **作者**：Linyue Pan, Lexiao Zou, Shuo Guo, Jingchen Ni, Hai-Tao Zheng
- **分类**：表示与可复现实验
- **一句话价值**：把 harness 从控制器代码中抽离成可编辑的自然语言对象 NLAH，并由 IHR 解释执行；重点价值是可检查、可迁移、可消融。
- **摘要要点**：Agent performance is strongly shaped by the surrounding harness: the external execution system around a model that organizes a task run. Yet this logic is usually buried in tightly coupled controller code, which makes harnesses hard to inspect, compare, transfer, and ablate. This paper asks whether the reusable design pattern of an agent harness can be represented as an executable natural-language object. We introduce Natural-Language Agent Harnesses (NLAHs), editable documents that describe run-level harness policy, and Intelligent Harness Runtime (IHR), a shared runtime that interprets these documents into agent calls, handoffs, state updates, validation gates, and artifact contracts. Across coding, terminal-use, and computer-use benchmarks, IHR-executed NLAHs achieve comparable task outcomes to code and prompted realizations, while exposing much shorter static harness policies. Module ablations further show that explicit harness modules are analyzable. These results suggest that agent harnesses can be turned from incidental glue around models into scientific representation objects.

### 3. AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents

- **arXiv**：[2605.13357](https://arxiv.org/abs/2605.13357)
- **时间**：2026-05-13（updated: 2026-05-13）
- **作者**：Hailin Zhong, Shengxin Zhu
- **分类**：软件工程运行基座
- **一句话价值**：把软件工程 agent 的可靠性问题归因到运行基座而非单纯模型能力，强调观察、行动、反馈和完成证明。
- **摘要要点**：Foundation models have transformed automated code generation, yet autonomous software-engineering agents remain unreliable in realistic development settings. The dominant explanation locates this gap in model capability. We propose a different locus: software-engineering capability emerges from a model-harness-environment system, in which a runtime substrate -- the harness -- mediates how a foundation-model agent observes a project, acts on it, receives feedback, and establishes that a change is complete. We formalize this substrate as an AI Harness Engineering and identify eleven component responsibilities: task specification, context selection, tool access, project memory, task state, observability, failure attribution, verification, permissions, entropy auditing, and intervention recording. We operationalize the harness through a four-level ladder (H0-H3) that progressively exposes runtime support to the agent, and we propose a trace-based evaluation protocol that converts each agent run into an auditable episode package. Applied to a controlled validation task, the framework yields episode packages whose evidence structure varies systematically with harness level: lower levels produce only a final patch, higher levels produce reproduction logs, failure attributions, deterministic requirement checks, and structured verification reports. The framework reframes the central question of autonomous software engineering from whether a foundation model can produce a patch to whether the model-harness-environment system can produce a verifiably correct, attributed, and maintainable change. We outline a research program for the runtime systems that foundation-model software agents will require.

### 4. Towards Direct Evaluation of Harness Optimizers via Priority Ranking

- **arXiv**：[2605.22505](https://arxiv.org/abs/2605.22505)
- **时间**：2026-05-21（updated: 2026-05-21）
- **作者**：Kai Tzu-iunn Ong, Minseok Kang, Dongwook Choi, Junhee Cho, Seungju Kim, Seungwon Lim et al.
- **分类**：优化器评估
- **一句话价值**：指出只看目标 agent 最终性能是间接评估，提出用优先级排序直接评估 harness optimizer 的改进判断能力。
- **摘要要点**：Harness optimization enables automated agent creation by having an optimizer agent iteratively update the harness of target agents. Despite its success, current studies evaluate optimizers solely by observing target agents' performance gains. This indirect end-improvement evaluation neglects optimizers' actions at intermediate steps, which are often erroneous and hinder agent performance. Therefore, it is unclear whether harness optimization is driven by optimizers' informed update actions or simply trial-and-error. This necessitates direct evaluation of harness optimizers. However, evaluating harness optimizers directly is non-trivial and costly due to the lack of oracle harnesses. To address this, we present a simple, low-cost design to directly evaluate them, namely priority ranking. By asking harness optimizers to rank components (e.g., tools) in a given harness by their potential to improve/hinder agent performance when updated, our design quantifies optimizer ability at the step level without expensive rollouts or manual examination. More importantly, optimizers' ranking performance correlates with their ability to improve agents in actual multi-step harness optimization, establishing priority ranking as a reliable predictor of optimization ability. Priority ranking is enabled by Shor, a collection of 182 human-verified optimization scenarios spanning across domains, designs, and time stages. Codes and data can be found at https://github.com/k59118/Harness_Optimizer_Evaluation.

### 5. Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents

- **arXiv**：[2605.22166](https://arxiv.org/abs/2605.22166)
- **时间**：2026-05-21（updated: 2026-05-21）
- **作者**：Tianshi Xu, Huifeng Wen, Meng Li
- **分类**：运行时适配
- **一句话价值**：强调不改模型参数，而在运行时适配接口、观察、工具、反馈和轨迹控制，使 agent 更确定。
- **摘要要点**：LLM agents are shaped not only by their language models, but also by the runtime harness that mediates observation, tool use, action execution, feedback interpretation, and trajectory control. While existing agent adaptation methods mainly update model parameters, many failures in deterministic, rule-governed domains stem from mismatches at the model--environment interface. We propose Life-Harness, a lifecycle-aware runtime harness that improves frozen LLM agents without changing model weights or evaluation environments. Life-Harness evolves from training trajectories by converting recurring interaction failures into reusable interventions across environment contracts, procedural skills, action realization, and trajectory regulation, and remains fixed during held-out evaluation. On seven deterministic environments from $τ$-bench, $τ^2$-bench, and AgentBench, Life-Harness improves 116 out of 126 model--environment settings across 18 model backbones, with an average relative improvement of 88.5%. Harnesses evolved only from Qwen3-4B-Instruct trajectories transfer to 17 other models, showing that Life-Harness captures reusable environment-side structure rather than model-specific behavior. These results position runtime interface adaptation as a complementary alternative to model-centric agent training. Code is available at GitHub.

### 6. Harnesses for Inference-Time Alignment over Execution Trajectories

- **arXiv**：[2605.21516](https://arxiv.org/abs/2605.21516)
- **时间**：2026-05-15（updated: 2026-05-15）
- **作者**：Boyuan Wang, Bochao Li, Minghan Wang, Yuxin Tao, Fang Kong
- **分类**：推理时对齐
- **一句话价值**：讨论基于执行轨迹的 inference-time alignment，提醒更复杂 harness 不一定更好，需要控制过度约束。
- **摘要要点**：Harness engineering has emerged as an important inference-time technique for large language model (LLM) agents, aiming to improve long-term performance through task decomposition and guided execution. However, more elaborate harnesses are not uniformly better: increasing decomposition or guidance can sometimes improve execution, but can also reduce final task success. We study harness design through the lens of inference-time trajectory alignment. This perspective separates harness into two mechanisms: task decomposition, which structures a task into sub-goals, and guided execution, which reshapes local action distributions during execution. This decomposition allows us to quantify how workflow granularity, retry budgets, and guidance-induced action reweighting shape the performance limits of harness design. It further reveals concrete failure modes, including over-decomposition, over-pruning, and hallucinated execution. We validate these predictions through controlled synthetic experiments and real terminal agent benchmarks. Inspired by the theory, we further show that effective harnesses can be partial: specifying only the initial steps and leaving the remaining execution to agent can achieve higher pass rate than fully structured workflows.

### 7. Auditing Agent Harness Safety

- **arXiv**：[2605.14271](https://arxiv.org/abs/2605.14271)
- **时间**：2026-05-14（updated: 2026-05-16）
- **作者**：Chengzhi Liu, Yichen Guo, Yepeng Liu, Yuzhe Yang, Qianqi Yan, Xuandong Zhao et al.
- **分类**：安全审计
- **一句话价值**：关注 harness 轨迹层面的越权资源访问和上下文泄漏：答案正确不代表执行过程安全。
- **摘要要点**：LLM agents increasingly run inside execution harnesses that dispatch tools, allocate resources, and route messages between specialized components. However, a harness can return a correct, benign answer over a trajectory that accesses unauthorized resources or leaks context to the wrong agent. Output-level evaluation cannot see these failures, yet most safety benchmarks score only final outputs or terminal states, even though many violations occur mid-trajectory rather than at termination. The central question is whether the harness respects user intent, permission boundaries, and information-flow constraints throughout execution. To address this gap, we propose HarnessAudit, a framework that audits full execution trajectories across boundary compliance, execution fidelity, and system stability, with a focus on multi-agent harnesses where these risks are most pronounced. We further introduce HarnessAudit-Bench, a benchmark of 210 tasks across eight real-world domains, instantiated in both single-agent and multi-agent configurations with embedded safety constraints. Evaluating ten harness configurations across frontier models and three multi-agent frameworks, we find that: (i) task completion is misaligned with safe execution, and violations accumulate with trajectory length; (ii) safety risks vary across domains, task types, and agent roles; (iii) most violations concentrate in resource access and inter-agent information transfer; and (iv) multi-agent collaboration expands the safety risk surface, while harness design sets the upper bound of safe deployment.

### 8. Code as Agent Harness

- **arXiv**：[2605.18747](https://arxiv.org/abs/2605.18747)
- **时间**：2026-05-18（updated: 2026-05-18）
- **作者**：Xuying Ning, Katherine Tieu, Dongqi Fu, Tianxin Wei, Zihao Li, Yuanchen Bei et al.
- **分类**：Code-as-Harness
- **一句话价值**：把代码本身视作 agent harness：代码不只是输出，也是状态、工具、控制流和可验证执行环境。
- **摘要要点**：Recent large language models (LLMs) have demonstrated strong capabilities in understanding and generating code, from competitive programming to repository-level software engineering. In emerging agentic systems, code is no longer only a target output. It increasingly serves as an operational substrate for agent reasoning, acting, environment modeling, and execution-based verification. We frame this shift through the lens of agent harnesses and introduce code as agent harness: a unified view that centers code as the basis for agent infrastructure. To systematically study this perspective, we organize the survey around three connected layers. First, we study the harness interface, where code connects agents to reasoning, action, and environment modeling. Second, we examine harness mechanisms: planning, memory, and tool use for long-horizon execution, together with feedback-driven control and optimization that make harness reliable and adaptive. Third, we discuss scaling the harness from single-agent systems to multi-agent settings, where shared code artifacts support multi-agent coordination, review, and verification. Across these layers, we summarize representative methods and practical applications of code as agent harness, spanning coding assistants, GUI/OS automation, embodied agents, scientific discovery, personalization and recommendation, DevOps, and enterprise workflows. We further outline open challenges for harness engineering, including evaluation beyond final task success, verification under incomplete feedback, regression-free harness improvement, consistent shared state across multiple agents, human oversight for safety-critical actions, and extensions to multimodal environments. By centering code as the harness of agentic AI, this survey provides a unified roadmap toward executable, verifiable, and stateful AI agent systems.

### 9. Effective Harness Engineering for Algorithm Discovery with Coding Agents

- **arXiv**：[2605.15221](https://arxiv.org/abs/2605.15221)
- **时间**：2026-05-13（updated: 2026-05-13）
- **作者**：Yoichi Ishibashi, Taro Yano, Masafumi Oyamada
- **分类**：算法发现
- **一句话价值**：面向 AlphaEvolve/FunSearch 类算法发现，说明成功依赖模型之外的候选生成、评估、选择和演化 harness。
- **摘要要点**：AlphaEvolve and FunSearch have demonstrated the potential of combining large language models (LLMs) with evolutionary search for automated algorithm discovery. However, discovery success is shaped not only by model capability but also significantly by the design of the execution infrastructure, i.e., the harness. This paper investigates effective harness design through three questions: under a fixed token budget, is it better to produce many algorithms with brief thought or fewer algorithms with deeper thought? How should the harness handle evaluation hacks, where generated programs exploit the scoring function? And how can agents that require full filesystem access execute safely in parallel? Using Vesper, an algorithm discovery framework that incorporates harness improvements addressing these questions, we evaluate on Circle Packing under the same token budget. Interestingly, generating fewer algorithms while thinking more deeply about each one achieved higher scores. That is, scaling the quality of each individual is more budget-efficient than scaling the number of evolutionary generations. Surprisingly, more capable models produced evaluation hacks at higher rates, making hack detection increasingly necessary as models scale.

### 10. Sibyl-AutoResearch: Autonomous Research Needs Self-Evolving Trial-and-Error Harnesses, Not Paper Generators

- **arXiv**：[2605.22343](https://arxiv.org/abs/2605.22343)
- **时间**：2026-05-21（updated: 2026-05-21）
- **作者**：Chengcheng Wang, Qinhua Xie, Wei He, Jianyuan Guo, Shiqi Wang, Chang Xu
- **分类**：科研 Agent / 自演化
- **一句话价值**：认为自动科研不应只是 paper generator，而需要支持试错、失败归因、研究判断的自演化 harness。
- **摘要要点**：Autonomous research systems increasingly make the scientific workflow executable: agents can propose ideas, run code, inspect results, and draft papers. But executable workflows do not by themselves produce research judgment. We analyze where current systems lose trial experience: weak evidence becomes prose, pilot signals become broad claims, memory remains textual, and recurring process failures do not change later behavior. We introduce Sibyl-AutoResearch, a self-evolving AutoResearch framework built around Scientific Trial-and-Error Harnesses. A harness lets agents run bounded trials, preserve positive and negative outcomes, and route lessons into later planning, validation, claim scope, scheduling, critique, writing, and harness repair. We formalize this through two auditable conversion units: trial-to-behavior conversion, which links trial signals to later research actions, and trial-to-harness-behavior conversion, which links recurring process failures to system updates. We implement the framework in SIBYL, a file-backed autonomous research system that exposes the state, roles, memory, gates, and artifact traces needed to inspect these conversion paths. A retrospective audit identifies eight high-confidence conversion events, with a median latency of one iteration and a maximum latency of three iterations. A recovered-failure registry further shows how five naturally occurring failure classes, including duplicate results, stale numbers, and unsupported statistics, were blocked, downgraded, or routed into later repair. These traces do not establish a comparative performance claim; they show that the proposed conversion units are recoverable from realistic autonomous-research workspaces. The SIBYL framework and system are available at https://github.com/Sibyl-Research-Team/AutoResearch-SibylSystem.

### 11. Toward AI VIS Co-Scientists: A General and End-to-End Agent Harness for Solving Complex Data Visualization Tasks

- **arXiv**：[2605.21825](https://arxiv.org/abs/2605.21825)
- **时间**：2026-05-20（updated: 2026-05-20）
- **作者**：Haichao Miao, Zhimin Li, Kuangshi Ai, Kaiyuan Tang, Chaoli Wang, Peer-Timo Bremer et al.
- **分类**：领域专用 Harness
- **一句话价值**：面向复杂数据可视化任务，构建端到端 agent harness，代表 harness 向垂直科学工作流扩展。
- **摘要要点**：The ability to inspect, interpret, and communicate complex data is crucial for virtually any scientific endeavor, but often requires significant expertise outside the core domain ranging from data management and analysis to visualization design and implementation. We present an end-to-end agentic harness that, based on only the data and a high level description of the tasks, independently designs custom visual analysis applications (VIS apps). This represents an important step towards a general AI co-scientist envisioned by many as an autonomous system that can autonomously execute long horizon tasks based on high-level directions. Our proposed VIS co-scientist is an essential component of this broader AI co-scientist vision: a harness that can autonomously analyze data and design visualization solutions using a collection of agents and specialized skills that coordinate exploratory analysis, plan, configure the environment, implement, validate the interface, and most importantly evaluate the overall task completion. Each stage produces document and instruction artifacts that guide downstream work and enable iterative refinement. We validate this approach on IEEE SciVis Contests spanning multiple science and engineering fields. These contests serve as ideal proving grounds because they encode real-world complexity: ambiguous requirements, diverse data modalities, design trade-offs, and task-driven validation. Given only the data and target tasks, our system autonomously produces functional single-page VIS Apps with verified linked-view behavior, highly customized to domain experts' specified tasks and needs.

### 12. NORA: A Harness-Engineered Autonomous Research Agent for End-to-End Spatial Data Science

- **arXiv**：[2605.02092](https://arxiv.org/abs/2605.02092)
- **时间**：2026-05-03（updated: 2026-05-03）
- **作者**：Bing Zhou, Xiao Huang, Huan Ning, Qiusheng Wu, Diya Li, Ziyi Zhang
- **分类**：空间数据科学
- **一句话价值**：端到端空间数据科学研究 agent，代表 harness-engineered autonomous research 的领域化落地。
- **摘要要点**：The automation of scientific research workflows has emerged as a transformative frontier in artificial intelligence, yet existing autonomous research agents remain largely domain-agnostic, lacking the specialized reasoning, method selection, and data acquisition capabilities required for rigorous spatial data science. This paper introduces NORA (Night Owl Research Agent), a harness-engineered, multi-agent autonomous research system purpose-built for GIScience and spatial data science. NORA orchestrates the complete research lifecycle through a skills-first architecture comprising 21 domain-specialized workflow skills, 9 specialist sub-agents, and custom Model Context Protocol (MCP) servers. Central to the system's design are two novel domain-specialized skills: a spatial analysis skill unit that encodes decision frameworks for exploratory spatial data analysis, spatial regression, and diagnostics; and a spatial data download skill that supports reproducible acquisition from authoritative geospatial data sources. We formalize the concept of harness engineering for scientific research agents, demonstrating how lifecycle hooks, safety gates, generator-evaluator separation, human-in-the-loop, and state persistence ensure reliable and reproducible autonomous research. We evaluate NORA through case studies by 6 domain specialists and 3 LLM reviewers across seven dimensions (novelty, quality, rigor, etc). Results demonstrate that domain-specialized harness engineering substantially improves the efficiency and quality of research output compared to general-purpose agent configurations.

### 13. Is Grep All You Need? How Agent Harnesses Reshape Agentic Search

- **arXiv**：[2605.15184](https://arxiv.org/abs/2605.15184)
- **时间**：2026-05-14（updated: 2026-05-14）
- **作者**：Sahil Sen, Akhil Kasturi, Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah
- **分类**：搜索 Harness
- **一句话价值**：研究 agentic search 中 harness 如何重塑检索行为，挑战复杂 RAG/搜索 agent 是否必要。
- **摘要要点**：Recent advances in Large Language Model (LLM) agents have enabled complex agentic workflows where models autonomously retrieve information, call tools, and reason over large corpora to complete tasks on behalf of users. Despite the growing adoption of retrieval-augmented generation (RAG) in agentic search systems, existing literature lacks a systematic comparison of how retrieval strategy choice interacts with agent architecture and tool-calling paradigm. Important practical dimensions, including how tool outputs are presented to the model and how performance changes when searches must cope with more irrelevant surrounding text, remain under-explored in agent loops. This paper reports an empirical study organized into two experiments. Experiment 1 compares grep and vector retrieval on a 116-question sample from LongMemEval, using a custom agent harness (Chronos) and provider-native CLI harnesses (Claude Code, Codex, and Gemini CLI), for both inline tool results and file-based tool results that the model reads separately. Experiment 2 compares grep-only and vector-only retrieval while progressively mixing in additional unrelated conversation history, so that each query is embedded in more distracting material alongside the passages that matter. Across Chronos and the provider CLIs, grep generally yields higher accuracy than vector retrieval in our comparisons in experiment 1; at the same time, overall scores still depend strongly on which harness and tool-calling style is used, even when the underlying conversation data are the same.

### 14. CAX-Agent: A Lightweight Agent Harness for Reliable APDL Automation

- **arXiv**：[2605.15218](https://arxiv.org/abs/2605.15218)
- **时间**：2026-05-12（updated: 2026-05-12）
- **作者**：Chenying Lin, Yichen Hai, Yi He, Ran Wang, Haiyan Qiang, Liang Yu
- **分类**：工程仿真自动化
- **一句话价值**：APDL/MAPDL 有限元场景的轻量 harness，体现工具封装、执行控制、故障恢复的重要性。
- **摘要要点**：Large language models deployed for MAPDL finite-element simulation face practical reliability challenges: without structured execution control, tool encapsulation, and fault recovery, outputs may be inconsistent and task failures are common. The Agent Harness paradigm addresses this by inserting domain-specific orchestration middleware that manages tool lifecycles, workflow state, and recovery escalation. This paper presents the architecture of CAX-Agent, a lightweight agent harness purpose-built for MAPDL automation, and empirically evaluates one of its core components -- the recovery policy.CAX-Agent organizes execution into three layers -- LLM service, agent harness, and solver backend -- with a recovery ladder that escalates from deterministic rule patching through model-driven regeneration to context enrichment and human intervention. We evaluate three recovery strategies (no_recovery, rule_only, and model_only) on 50 standard structural benchmarks with three repeated runs per strategy (450 case-runs total). Two independent human raters score task completion under blind conditions; inter-rater agreement is strong (quadratic weighted Cohen's kappa = 0.84, 96 percent of score pairs within one point). Model_only achieves the best completion rate (0.9267), task score (3.59/4), total score (9.16/10), and zero-intervention rate (0.84), outperforming rule_only (0.7733, 3.17/4, 7.03/10, 0.00) and no_recovery (0.6933, 2.74/4, 5.60/10, 0.00) with large effect sizes (Cliff's delta = 0.81-0.87). The benchmark uses deliberately simple geometries to isolate recovery-policy effects; we discuss the scope of these findings and directions for broader validation.

### 15. It's Not the Size: Harness Design Determines Operational Stability in Small Language Models

- **arXiv**：[2605.12129](https://arxiv.org/abs/2605.12129)
- **时间**：2026-05-12（updated: 2026-05-12）
- **作者**：Yong-eun Cho
- **分类**：小模型稳定性
- **一句话价值**：实验讨论 2-3B 小模型在不同 harness 条件下的稳定性，强调小模型也能靠结构化流程提升可用性。
- **摘要要点**：This paper experimentally analyzes how the level of harness engineering affects the operational performance of small language models (SLMs, 2-3B parameters). Three harness conditions - model-only (raw prompt), minimal-shell (wrapper tags), and a 4-stage pipeline (plan->execute->verify->recover) - are applied to three models (Gemma4 E2B, Qwen3.5:2B, LLaMA 3.2 3B) across 24 tasks, comparing Task Success Rate (TSR) and Valid TSR (VTSR). The pipeline harness achieves TSR=0.952 and VTSR=1.000 on Gemma4 E2B (T1-T5, 21 tasks). A non-monotonic phenomenon - minimal-shell TSR < model-only TSR - is observed in two models. In LLaMA 3.2 3B model-only, seven format violations yield TSR=0.429, revealing scaffold collapse: the model abandons JSON structure under complex format requirements without harness support. Ablation shows planning and recovery each contribute approximately 24.7% of total gain. VCR (Verification Catch Rate)=0.625 across all pipeline runs.

### 16. Harness Engineering as Categorical Architecture

- **arXiv**：[2605.12239](https://arxiv.org/abs/2605.12239)
- **时间**：2026-05-12（updated: 2026-05-12）
- **作者**：Bogdan Banu
- **分类**：形式化理论
- **一句话价值**：尝试用范畴论描述 prompts、tools、memory、orchestration 的组合与可替换关系，偏理论化。
- **摘要要点**：The agent harness, the system layer comprising prompts, tools, memory, and orchestration logic that surrounds the model, has emerged as the central engineering abstraction for LLMbased agents. Yet harness design remains ad hoc, with no formal theory governing composition, preservation of properties under compilation, or systematic comparison across frameworks. We show that the categorical Architecture triple (G, Know, Phi) from the ArchAgents framework provides exactly this formalization. The four pillars of agent externalization (Memory, Skills, Protocols, Harness Engineering) map onto the triple's components: Memory as coalgebraic state, Skills as operad-composed objects, Protocols as syntactic wiring G, and the full Harness as the Architecture itself. Structural guarantees-integrity gates, quality-based escalation, supported convergence checks-are Know-level certificates whose preservation is structural replay: our compiler checks identity and verifier replay, not output-layer correctness or model behavior. We validate this correspondence with a reference implementation featuring compiler functors targeting Swarms, DeerFlow, Ralph, Scion, and LangGraph: the four configuration compilers preserve three named certificate types by identity or replay, and LangGraph preserves the same certificates through its shared per-stage execution path. The LangGraph compiler creates one node per stage using the same per-stage method as the native runtime, providing LangGraph-native observability without reimplementing harness logic. An end-to-end escalation experiment with real LLM agents confirms that the quality-based escalation control path is model-parametric in this two-model, one-task experiment. The result positions categorical architecture as the formal theory behind harness engineering.

## 推荐阅读顺序

如果想系统进入这个方向，建议按这个顺序读：

1. **概念与表示**：Natural-Language Agent Harnesses → AI Harness Engineering
2. **自动演化**：Agentic Harness Engineering → Direct Evaluation of Harness Optimizers
3. **对齐与安全**：Harnesses for Inference-Time Alignment → Auditing Agent Harness Safety
4. **软件工程落地**：Code as Agent Harness → Algorithm Discovery with Coding Agents
5. **领域扩展**：AI VIS Co-Scientists / NORA / CAX-Agent
6. **理论视角**：Categorical Architecture / Small Language Models Stability

## 和原 Harness Engineering 文档的关系

原来的 [Harness Engineering 学习资料](harness-engineering.md) 更偏工程实践和范式梳理；本文档补充 2026 年最新论文脉络，适合作为后续研究阅读清单。

## 可跟进问题

- Harness 的最小可复现表示是什么：自然语言、代码、配置文件，还是混合对象？
- Harness optimizer 的评价应看最终任务成功率，还是看修改建议的排序质量、可解释性和可回滚性？
- 安全审计应该发生在答案层、工具调用层、轨迹层，还是资源访问层？
- 哪些 harness 组件可跨模型/跨任务迁移：工具、中间件、记忆、验证器、提示词，谁最稳定？
- 领域专用 harness 与通用 agent framework 的边界在哪里？

---

## Freshness

| 字段 | 内容 |
|------|------|
| 最后审阅 | 2026-06 |
| 更新频率 | 每季度；高变化阶段可每月 |
| 过时风险 | 高 |
| 维护重点 | 新论文、新系统、新 benchmark、官方技术报告、失效链接 |
| 稳定性 | 经典材料稳定，前沿系统观察中 |
