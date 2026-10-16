#!/usr/bin/env python3
"""Generate PDF CVs and cover letters using weasyprint."""
import os
from weasyprint import HTML, CSS

OUTPUT = "/tmp/job-applications/pdf"
os.makedirs(OUTPUT, exist_ok=True)

CSS_CV = """
@page { size: A4; margin: 18mm 18mm 18mm 18mm; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 9.5pt; color: #222; line-height: 1.4; }
h1 { font-size: 22pt; font-weight: 700; color: #1a4a8a; letter-spacing: 0.5px; }
.subtitle { font-size: 9pt; color: #555; margin-top: 2px; }
.contact { font-size: 8.5pt; color: #444; margin-top: 4px; }
.contact a { color: #1a4a8a; text-decoration: none; }
hr.title-rule { border: none; border-top: 2px solid #1a4a8a; margin: 8px 0 12px; }
h2 { font-size: 10pt; font-weight: 700; color: #1a4a8a; text-transform: uppercase;
     letter-spacing: 1px; border-bottom: 1px solid #1a4a8a; padding-bottom: 2px; margin: 12px 0 6px; }
.entry { display: flex; gap: 10px; margin-bottom: 7px; }
.entry-left { min-width: 80px; max-width: 80px; font-size: 8pt; color: #666; text-align: right; padding-top: 1px; }
.entry-right { flex: 1; }
.entry-title { font-weight: 700; font-size: 9.5pt; }
.entry-org { font-style: italic; color: #444; font-size: 9pt; }
.entry-loc { color: #666; font-size: 8.5pt; }
ul { margin: 4px 0 0 14px; }
li { margin-bottom: 2px; font-size: 9pt; }
.cvitem { display: flex; gap: 8px; margin-bottom: 4px; font-size: 9pt; }
.cvitem-label { font-weight: 700; min-width: 110px; max-width: 110px; color: #1a4a8a; font-size: 8.5pt; }
.cvitem-val { flex: 1; }
a { color: #1a4a8a; text-decoration: none; }
.tagline { font-size: 9pt; color: #333; margin-bottom: 8px; line-height: 1.5; }
"""

CSS_CL = """
@page { size: A4; margin: 25mm 22mm 20mm 22mm; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 10.5pt; color: #222; line-height: 1.55; }
.sender { font-size: 9.5pt; color: #444; margin-bottom: 18px; }
.sender strong { display: block; font-size: 11pt; color: #1a4a8a; margin-bottom: 3px; }
.recipient { margin-bottom: 18px; font-size: 9.5pt; }
.date { margin-bottom: 18px; font-size: 9.5pt; color: #555; }
p { margin-bottom: 10px; }
ul { margin: 8px 0 10px 18px; }
li { margin-bottom: 6px; }
.closing { margin-top: 20px; }
a { color: #1a4a8a; text-decoration: none; }
.sig-links { font-size: 9pt; color: #555; margin-top: 6px; }
"""

# ── CV DATA ──────────────────────────────────────────────────────────────────

COMMON = {
    "name": "Oluwatosin Ayeni",
    "contact": "Glasgow, Scotland, UK &nbsp;·&nbsp; 07727305230 &nbsp;·&nbsp; ayenioluwatosinolawale@gmail.com<br>"
               '<a href="https://github.com/AyeniOluwatosinOlawale">github.com/AyeniOluwatosinOlawale</a> &nbsp;·&nbsp; '
               '<a href="https://www.linkedin.com/in/oluwatosinolawaleayeni/">linkedin.com/in/oluwatosinolawaleayeni</a>',
    "education": [
        ("2022–2023", "MSc Artificial Intelligence and Applications, <strong>Distinction</strong>", "University of Strathclyde", "Glasgow, UK"),
        ("2010–2016", "MTech / BSc Physics", "Federal University of Technology Akure", "Nigeria"),
    ],
    "repos": "43 public repos — <a href='https://github.com/AyeniOluwatosinOlawale'>github.com/AyeniOluwatosinOlawale</a>",
}

EXPERIENCE_FULL = """
<div class="entry">
  <div class="entry-left">Jan 2025–present</div>
  <div class="entry-right">
    <span class="entry-title">Founder &amp; Lead Engineer</span> — <span class="entry-org">Nexora Academic</span>, <span class="entry-loc">Glasgow, UK</span>
    <ul>
      <li>H100 NVL benchmark: vLLM v0.30 vs SGLang v0.5.20 — Qwen3-8B BF16, TP=2. Peak: 5,965 tok/s; RadixAttention: 1,443× TTFT speedup (39 ms vs 55,565 ms) at 131K-token context; 100% SLO compliance up to concurrency 128. Live: <a href="https://inference-web-theta.vercel.app/benchmarks/llm">inference-web-theta.vercel.app</a></li>
      <li>Built <em>inference-optimizer</em>: production AI Inference Gateway — 3.87× faster (parallel execution), 61.4% cost reduction (prompt caching), 14× throughput (concurrency), 64.3% cheaper (model routing). 13 optimisations, 4 providers.</li>
      <li>Built <em>vllm-k8s-stack</em>: Kubernetes LLM serving — KV-cache-aware routing, HPA autoscaling on GPU pools, Prometheus/Grafana observability.</li>
      <li>Built <em>inference-harness</em>: unified benchmark framework spanning closed APIs + vLLM/SGLang/TensorRT-LLM with GPU profiling and live dashboard.</li>
      <li>Designed 13-phase AI Inference Engineering curriculum covering GPU architecture, CUDA optimisation, serving frameworks, and distributed inference.</li>
    </ul>
  </div>
</div>
<div class="entry">
  <div class="entry-left">Jan 2023–present</div>
  <div class="entry-right">
    <span class="entry-title">Founder &amp; AI Consultant</span> — <span class="entry-org">Vertinab / AnaburyAI Technology</span>, <span class="entry-loc">Glasgow, UK</span>
    <ul>
      <li>28× LLM cost reduction deploying Qwen2.5-7B on RTX 4090 via vLLM/SGLang with continuous batching and KV cache optimisation.</li>
      <li>CUDA KV cache kernel profiling with NVIDIA Nsight: identified memory bandwidth bottleneck; 3.8× throughput improvement; 18× latency reduction via continuous batching redesign.</li>
      <li>Fine-tuned Mistral 7B with LoRA/PEFT on radiology corpus: +22% diagnostic accuracy, −35% hallucination rate; deployed as production clinical inference API.</li>
    </ul>
  </div>
</div>
<div class="entry">
  <div class="entry-left">2024–present</div>
  <div class="entry-right">
    <span class="entry-title">Senior Software Engineer (Contract)</span> — <span class="entry-org">EduTechConnect / Stellar Labs</span>, <span class="entry-loc">Remote</span>
    <ul><li>Real-time NLP pipeline (WhatsApp → Zoho CRM → Supabase) with sub-500 ms end-to-end latency under concurrent load.</li></ul>
  </div>
</div>
<div class="entry">
  <div class="entry-left">Mar 2026–present</div>
  <div class="entry-right">
    <span class="entry-title">AI Automation Engineer</span> — <span class="entry-org">EduTech Global</span>, <span class="entry-loc">Remote</span>
    <ul><li>LLM-backed student chatbots with structured output extraction and multi-step reasoning for Ahmadu Bello and Babcock universities.</li></ul>
  </div>
</div>
<div class="entry">
  <div class="entry-left">2018–2022</div>
  <div class="entry-right">
    <span class="entry-title">Data Analyst</span> — <span class="entry-org">Bytelab Technologies Ltd</span>, <span class="entry-loc">Nigeria</span>
  </div>
</div>
"""

ROLES = [
    {
        "slug": "gresearch_nlp-performance-engineer",
        "title": "NLP Performance Engineer",
        "company": "G-Research",
        "tagline": "AI &amp; ML Engineer specialising in LLM inference optimisation and GPU performance engineering. Proven track record benchmarking vLLM and SGLang on H100 NVL — 1,443× TTFT speedup via RadixAttention, 5,965 tok/s peak. Deep expertise in CUDA kernel profiling, KV cache optimisation, continuous batching, and quantisation. MSc AI with Distinction, University of Strathclyde 2023.",
        "competencies": [
            ("Inference Engines", "vLLM, SGLang, TensorRT-LLM, Hugging Face TGI, ONNX Runtime"),
            ("GPU &amp; CUDA", "NVIDIA Nsight Systems/Compute, CUDA kernel profiling, memory bandwidth analysis, warp occupancy, KV cache CUDA ops"),
            ("Optimisation", "Speculative decoding, continuous batching, AWQ/GPTQ quantisation, tensor parallelism, KV cache-aware routing, prefix caching"),
            ("LLM Stack", "PyTorch, Transformers, PEFT/LoRA, flash attention, BFloat16/FP8, Qwen3, Mistral, Phi-4, Gemma 2"),
            ("Infrastructure", "Kubernetes (HPA, GPU node pools), Docker, Prometheus, Grafana, FastAPI, Python, TypeScript"),
        ],
        "projects": [
            ("llm-inference-benchmark (H100)", "vLLM v0.30 vs SGLang v0.5.20 on 2× H100 NVL 94 GB — Qwen3-8B BF16, TP=2. RadixAttention: 1,443× TTFT speedup. Peak: 5,965 tok/s. SLO 100% at concurrency 128. <a href='https://inference-web-theta.vercel.app/benchmarks/llm'>Live results</a>"),
            ("open-model-engine", "GPU-first inference benchmarking: vLLM, SGLang, TensorRT-LLM — CUDA profiling, quantisation, speculative decoding. <a href='https://github.com/AyeniOluwatosinOlawale/open-model-engine'>GitHub</a>"),
            ("inference-optimizer", "Production Inference Gateway: 3.87× faster, 61.4% cost reduction, 14× throughput. <a href='https://github.com/AyeniOluwatosinOlawale/inference-optimizer'>GitHub</a>"),
            ("vllm-k8s-stack", "Kubernetes LLM serving: KV-cache-aware routing, HPA autoscaling, Prometheus/Grafana. <a href='https://github.com/AyeniOluwatosinOlawale/vllm-k8s-stack'>GitHub</a>"),
            ("inference-harness", "Unified benchmark harness across closed + open APIs with GPU profiling. <a href='https://github.com/AyeniOluwatosinOlawale/inference-harness'>GitHub</a>"),
        ],
    },
    {
        "slug": "wayve_inference-optimisation",
        "title": "Staff ML Performance Engineer (Inference Optimisation)",
        "company": "Wayve",
        "tagline": "AI &amp; ML Engineer with deep expertise in LLM inference optimisation, CUDA kernel performance, and GPU serving infrastructure. Benchmarked vLLM and SGLang on H100 NVL — 5,965 tok/s peak throughput, 1,443× TTFT improvement via RadixAttention; profiled CUDA memory bandwidth bottlenecks to deliver 3.8× throughput gains. Experienced building production Kubernetes GPU stacks. Open to London relocation.",
        "competencies": [
            ("Inference Engines", "vLLM, SGLang, TensorRT-LLM, ONNX Runtime, Hugging Face TGI"),
            ("GPU &amp; CUDA", "NVIDIA Nsight Systems/Compute, CUDA kernel profiling, memory bandwidth analysis, kernel fusion, KV cache ops, warp occupancy"),
            ("Optimisation", "Speculative decoding, continuous batching, KV cache optimisation, tensor parallelism TP=2/4, AWQ/GPTQ quantisation, prefix caching, flash attention"),
            ("ML &amp; Models", "PyTorch, PEFT/LoRA fine-tuning, Qwen3, Mistral, Phi-4, Gemma 2, BFloat16/FP8"),
            ("Infrastructure", "Kubernetes (HPA, GPU pools), Docker, Prometheus, Grafana, FastAPI, Python, GitHub Actions"),
        ],
        "projects": [
            ("llm-inference-benchmark (H100)", "2× H100 NVL 94 GB, NVLink 4.0, CUDA 13.4. Qwen3-8B BF16, TP=2. RadixAttention: 1,443× TTFT speedup. Peak: 5,965 tok/s. SLO 100%. <a href='https://inference-web-theta.vercel.app/benchmarks/llm'>Live results</a>"),
            ("vllm-k8s-stack", "Production Kubernetes LLM serving: KV-cache-aware routing, HPA autoscaling, Prometheus/Grafana. <a href='https://github.com/AyeniOluwatosinOlawale/vllm-k8s-stack'>GitHub</a>"),
            ("open-model-engine", "GPU inference benchmarking: CUDA profiling, AWQ/GPTQ, speculative decoding, Pareto curves. <a href='https://github.com/AyeniOluwatosinOlawale/open-model-engine'>GitHub</a>"),
            ("inference-optimizer", "Production Inference Gateway: 3.87× faster, 14× throughput, 61.4% cost reduction. <a href='https://github.com/AyeniOluwatosinOlawale/inference-optimizer'>GitHub</a>"),
            ("inference-harness", "Unified benchmark harness: closed + open engines, GPU profiling, live dashboard. <a href='https://github.com/AyeniOluwatosinOlawale/inference-harness'>GitHub</a>"),
        ],
    },
    {
        "slug": "perplexity_ai-inference-engineer",
        "title": "Member of Technical Staff (AI Inference Engineer)",
        "company": "Perplexity AI",
        "tagline": "AI Inference Engineer with production experience optimising LLM serving latency and throughput at GPU level. Benchmarked vLLM vs SGLang on H100 NVL — 1,443× TTFT speedup via RadixAttention, 5,965 tok/s peak. Built inference gateways delivering 3.87× latency reduction, 14× throughput, 61.4% cost reduction. Strong foundation in CUDA profiling, continuous batching, KV cache optimisation, and speculative decoding.",
        "competencies": [
            ("Inference Engines", "vLLM, SGLang, TensorRT-LLM, ONNX Runtime, Hugging Face Transformers"),
            ("GPU &amp; Performance", "NVIDIA Nsight Systems/Compute, CUDA kernel profiling, memory bandwidth, warp utilisation, kernel fusion"),
            ("Optimisation", "Speculative decoding, continuous batching, prefix/RadixAttention caching, tensor parallelism, AWQ/GPTQ, flash attention, BFloat16/FP8"),
            ("Benchmarking", "End-to-end LLM serving benchmarks (throughput, TTFT, TPOT, SLO compliance), Pareto latency/cost curves, automated regression testing"),
            ("Infrastructure", "Kubernetes, Docker, FastAPI, Prometheus, Grafana, Python, TypeScript, PostgreSQL, Redis"),
        ],
        "projects": [
            ("llm-inference-benchmark (H100)", "vLLM v0.30 vs SGLang v0.5.20, H100 NVL, Qwen3-8B BF16, TP=2. RadixAttention: 1,443× TTFT speedup. Peak: 5,965 tok/s. SLO 100% at concurrency 128. <a href='https://inference-web-theta.vercel.app/benchmarks/llm'>Live results</a>"),
            ("inference-optimizer", "Production Inference Gateway: 13 optimisations, 4 providers, 3.87× faster, 14× throughput, 61.4% cost reduction. <a href='https://github.com/AyeniOluwatosinOlawale/inference-optimizer'>GitHub</a>"),
            ("inference-harness", "Unified benchmark harness: closed + open APIs, GPU profiling, automated dashboard. <a href='https://github.com/AyeniOluwatosinOlawale/inference-harness'>GitHub</a>"),
            ("open-model-engine", "GPU inference benchmarking: CUDA profiling, AWQ/GPTQ, speculative decoding. <a href='https://github.com/AyeniOluwatosinOlawale/open-model-engine'>GitHub</a>"),
            ("vllm-k8s-stack", "Kubernetes LLM serving: KV-cache-aware routing, HPA autoscaling, Prometheus/Grafana. <a href='https://github.com/AyeniOluwatosinOlawale/vllm-k8s-stack'>GitHub</a>"),
        ],
    },
    {
        "slug": "anthropic_staff-inference-engineer",
        "title": "Staff Software Engineer, Inference",
        "company": "Anthropic",
        "tagline": "Staff-calibre AI Inference Engineer with expertise in distributed LLM serving, GPU optimisation, batching pipelines, and Kubernetes GPU infrastructure. Benchmarked H100 NVL — 5,965 tok/s peak, 1,443× TTFT speedup, 100% SLO compliance at concurrency 128. Built production inference gateways (3.87× faster, 14× throughput) and Kubernetes LLM serving stacks. Deep alignment with Anthropic's mission — I use Claude in production and build the same infrastructure layer that serves it.",
        "competencies": [
            ("Distributed Inference", "Tensor parallelism TP=2/4, pipeline parallelism, KV cache-aware routing, multi-node GPU orchestration, batching strategies (continuous, dynamic, chunked prefill)"),
            ("Inference Engines", "vLLM, SGLang, TensorRT-LLM, ONNX Runtime — benchmarking, profiling, production deployment"),
            ("GPU &amp; CUDA", "NVIDIA Nsight Systems/Compute, memory bandwidth profiling, kernel fusion, warp occupancy, BFloat16/FP8"),
            ("ML Infrastructure", "Kubernetes (HPA, GPU node pools), Docker, Prometheus, Grafana, FastAPI, Supabase, GitHub Actions, Python"),
            ("LLM Techniques", "Speculative decoding, prefix/RadixAttention caching, AWQ/GPTQ quantisation, flash attention, PEFT/LoRA, multi-provider routing"),
        ],
        "projects": [
            ("llm-inference-benchmark (H100)", "2× H100 NVL 94 GB, CUDA 13.4. vLLM v0.30 vs SGLang v0.5.20, Qwen3-8B BF16, TP=2. RadixAttention: 1,443× TTFT speedup. Peak: 5,965 tok/s. SLO 100% at concurrency 128. <a href='https://inference-web-theta.vercel.app/benchmarks/llm'>Live results</a>"),
            ("inference-optimizer", "Production Inference Gateway: multi-provider (Claude, GPT, Gemini), 3.87× faster, 14× throughput, 61.4% cost reduction. <a href='https://github.com/AyeniOluwatosinOlawale/inference-optimizer'>GitHub</a>"),
            ("vllm-k8s-stack", "Kubernetes LLM serving: vLLM, KV-cache-aware routing, HPA autoscaling, Prometheus/Grafana. <a href='https://github.com/AyeniOluwatosinOlawale/vllm-k8s-stack'>GitHub</a>"),
            ("inference-harness", "Unified benchmark harness: Anthropic, OpenAI, Gemini + vLLM, SGLang, TensorRT-LLM — GPU profiling, automated reporting. <a href='https://github.com/AyeniOluwatosinOlawale/inference-harness'>GitHub</a>"),
            ("open-model-engine", "GPU-first benchmarking: CUDA profiling, quantisation, speculative decoding. <a href='https://github.com/AyeniOluwatosinOlawale/open-model-engine'>GitHub</a>"),
        ],
    },
    {
        "slug": "doubleword_inference-research",
        "title": "Member of Technical Staff: Inference Research",
        "company": "Doubleword",
        "tagline": "AI Inference Research Engineer with production experience optimising LLM serving across vLLM, SGLang, and TensorRT-LLM on H100 and RTX 4090 hardware. Benchmarked 1,443× TTFT speedup via RadixAttention; profiled CUDA KV cache kernels for 3.8× throughput gain; ran end-to-end speculative decoding and quantisation experiments. Interested in multi-LoRA serving, memory-constrained GPU inference, and the research-to-production pipeline. MSc AI with Distinction, Strathclyde 2023.",
        "competencies": [
            ("Inference Engines", "vLLM, SGLang, TensorRT-LLM, ONNX Runtime, Hugging Face Transformers/TGI"),
            ("GPU &amp; CUDA", "NVIDIA Nsight Systems/Compute, CUDA kernel profiling, memory bandwidth analysis, kernel fusion, warp occupancy, BFloat16/FP8"),
            ("Inference Research", "Speculative decoding, RadixAttention/prefix caching, AWQ/GPTQ quantisation, KV cache compression, multi-LoRA serving, flash attention, continuous batching"),
            ("LLM Fine-tuning", "PyTorch, PEFT/LoRA, Mistral 7B, Qwen3, Phi-4, Gemma 2 — full pipeline: data prep, training, eval, inference"),
            ("Infrastructure", "Kubernetes, Docker, FastAPI, Prometheus, Grafana, Python, GitHub Actions"),
        ],
        "projects": [
            ("llm-inference-benchmark (H100)", "vLLM vs SGLang, H100 NVL, Qwen3-8B BF16 TP=2. RadixAttention: 1,443× TTFT speedup. Peak: 5,965 tok/s. <a href='https://inference-web-theta.vercel.app/benchmarks/llm'>Live results</a>"),
            ("open-model-engine", "Inference benchmarking: vLLM, SGLang, TensorRT-LLM — CUDA profiling, quantisation, speculative decoding. <a href='https://github.com/AyeniOluwatosinOlawale/open-model-engine'>GitHub</a>"),
            ("inference-harness", "Unified benchmark harness: closed + open serving engines, GPU profiling, automated dashboard. <a href='https://github.com/AyeniOluwatosinOlawale/inference-harness'>GitHub</a>"),
            ("lab-vllm-omni", "vLLM-Omni phased inference lab: all 5 output modalities — text, audio, image, video, structured output. <a href='https://github.com/AyeniOluwatosinOlawale/lab-vllm-omni'>GitHub</a>"),
            ("My_finetuned_Phi-4", "Phi-4 LoRA fine-tuning: full pipeline — data prep, training, eval, inference. <a href='https://github.com/AyeniOluwatosinOlawale/My_finetuned_Phi-4'>GitHub</a>"),
        ],
    },
    {
        "slug": "leonardo_ai-platform-engineer",
        "title": "AI Platform Engineer",
        "company": "Leonardo UK",
        "tagline": "AI Platform Engineer with production experience deploying and operating LLM inference services on Kubernetes, building AI gateway infrastructure, and managing GPU workloads at scale. Benchmarked vLLM and SGLang on H100 NVL achieving 5,965 tok/s peak and 100% SLO compliance; built KV-cache-aware routing, HPA autoscaling, and Prometheus/Grafana observability stacks. Experienced designing multi-provider AI gateways with authentication, rate limiting, and model routing. Based in Glasgow — Edinburgh hybrid is ideal.",
        "competencies": [
            ("Inference &amp; Serving", "vLLM, SGLang, TensorRT-LLM, LiteLLM-style AI gateways, model routing, rate limiting, multi-provider API management"),
            ("Containers &amp; Orchestration", "Kubernetes (HPA, GPU node pools, resource quotas), Docker, Helm, container networking, pod security policies"),
            ("GPU &amp; Performance", "NVIDIA Nsight Systems/Compute, GPU utilisation monitoring, CUDA kernel profiling, tensor parallelism, KV cache optimisation, BFloat16/FP8"),
            ("Observability &amp; SRE", "Prometheus, Grafana, distributed tracing, SLO/SLA compliance monitoring, alerting, incident response"),
            ("Platform Engineering", "Python, Bash, FastAPI, PostgreSQL, Redis, GitHub Actions CI/CD, infrastructure as code, secure service design, authentication/access control"),
        ],
        "projects": [
            ("vllm-k8s-stack", "Production Kubernetes LLM serving: vLLM, KV-cache-aware routing, HPA GPU autoscaling, Prometheus/Grafana observability. <a href='https://github.com/AyeniOluwatosinOlawale/vllm-k8s-stack'>GitHub</a>"),
            ("inference-optimizer", "Production AI Gateway: 4 providers, authentication, model routing, rate limiting, caching, monitoring. 3.87× faster, 14× throughput, 61.4% cost reduction. <a href='https://github.com/AyeniOluwatosinOlawale/inference-optimizer'>GitHub</a>"),
            ("llm-inference-benchmark (H100)", "vLLM vs SGLang, H100 NVL — throughput, TTFT, TPOT, SLO compliance at concurrency 1–128. 100% SLO. <a href='https://inference-web-theta.vercel.app/benchmarks/llm'>Live dashboard</a>"),
            ("inference-harness", "Unified benchmark harness: closed + open APIs, GPU profiling, automated reporting. <a href='https://github.com/AyeniOluwatosinOlawale/inference-harness'>GitHub</a>"),
        ],
    },
    {
        "slug": "doubleword_inference-systems",
        "title": "Member of Technical Staff: Inference Systems",
        "company": "Doubleword",
        "tagline": "AI Inference Systems Engineer with production experience building distributed LLM serving infrastructure, GPU-backed Kubernetes stacks, and high-throughput batching pipelines. H100 NVL benchmarks: 5,965 tok/s peak, 100% SLO compliance at concurrency 128. KV-cache-aware routing, HPA autoscaling, Prometheus/Grafana. Profiled CUDA bottlenecks for 3.8× throughput improvement. Strong Python, growing Rust interest; PostgreSQL at production scale.",
        "competencies": [
            ("Inference Systems", "vLLM, SGLang, TensorRT-LLM, distributed batch inference, job scheduling, request routing, KV-cache-aware load balancing"),
            ("Infrastructure", "Kubernetes (HPA, GPU node pools), Docker, Prometheus, Grafana, GitHub Actions, FastAPI"),
            ("GPU &amp; Performance", "NVIDIA Nsight Systems/Compute, CUDA kernel profiling, memory bandwidth, BFloat16/FP8, tensor parallelism"),
            ("Data &amp; Storage", "PostgreSQL, Supabase, Redis — high-load query optimisation, schema design, real-time observability"),
            ("Languages", "Python (primary), TypeScript, SQL; Rust (learning — building inference tooling)"),
        ],
        "projects": [
            ("vllm-k8s-stack", "Production Kubernetes LLM serving: KV-cache-aware routing, HPA autoscaling, Prometheus/Grafana. <a href='https://github.com/AyeniOluwatosinOlawale/vllm-k8s-stack'>GitHub</a>"),
            ("llm-inference-benchmark (H100)", "vLLM vs SGLang, H100 NVL, Qwen3-8B BF16 TP=2. Peak: 5,965 tok/s. SLO 100% at concurrency 128. <a href='https://inference-web-theta.vercel.app/benchmarks/llm'>Live results</a>"),
            ("inference-optimizer", "Production Inference Gateway: 13 optimisations, 3.87× faster, 14× throughput, 61.4% cost reduction. <a href='https://github.com/AyeniOluwatosinOlawale/inference-optimizer'>GitHub</a>"),
            ("inference-harness", "Unified benchmark harness: closed + open serving engines, GPU profiling. <a href='https://github.com/AyeniOluwatosinOlawale/inference-harness'>GitHub</a>"),
        ],
    },
]

COVER_LETTERS = [
    {
        "slug": "gresearch_nlp-performance-engineer",
        "company": "G-Research",
        "recipient": "G-Research, London, UK",
        "body": """
<p>I am writing to apply for the NLP Performance Engineer role at G-Research. With hands-on production experience in vLLM, SGLang, TensorRT-LLM, and CUDA kernel profiling, I am directly aligned with the technical depth this role demands.</p>

<p>Three achievements most relevant to your requirements:</p>
<ul>
  <li><strong>H100 NVL benchmark — vLLM vs SGLang:</strong> I benchmarked vLLM v0.30 against SGLang v0.5.20 on 2× NVIDIA H100 NVL 94 GB (NVLink 4.0, CUDA 13.4) running Qwen3-8B in BF16 with tensor parallelism 2. Peak throughput: 5,965 tok/s; 100% SLO compliance from concurrency 1 to 128; 1,443× TTFT speedup via RadixAttention prefix caching (39 ms vs 55,565 ms at 131K-token context). Live at <a href="https://inference-web-theta.vercel.app/benchmarks/llm">inference-web-theta.vercel.app/benchmarks/llm</a>.</li>
  <li><strong>CUDA-level KV cache optimisation:</strong> Using NVIDIA Nsight Systems and Compute, I identified a memory bandwidth bottleneck in KV cache ops on RTX 4090 hardware and tuned the kernel access pattern, delivering a 3.8× throughput improvement without hardware change. I followed this with an 18× inference latency reduction through continuous batching redesign.</li>
  <li><strong>Production inference gateway at scale:</strong> I built <em>inference-optimizer</em> — implementing parallel execution (3.87× faster), prompt caching (61.4% cost reduction), model routing (64.3% cheaper), and concurrency management (14× throughput) across Claude, GPT-4o, and Gemini.</li>
</ul>

<p>G-Research's reputation for hiring engineers who combine rigorous quantitative thinking with systems depth is exactly the environment I want to work in. The intersection of NLP at scale and GPU performance engineering is where I have focused my independent work for the past two years.</p>

<p>I am happy to walk through the benchmarks in detail, provide compiled materials, or discuss my approach to GPU profiling and serving stack design. I look forward to speaking.</p>
""",
    },
    {
        "slug": "wayve_inference-optimisation",
        "company": "Wayve",
        "recipient": "Wayve, London, UK",
        "body": """
<p>I am applying for the Staff ML Performance Engineer (Inference Optimisation) role at Wayve. I bring production-grade experience in GPU inference optimisation — CUDA profiling, KV cache tuning, serving framework benchmarking on H100 hardware — and I am genuinely excited about the inference challenges involved in deploying large end-to-end neural driving models at scale.</p>

<p>Three specific achievements relevant to what Wayve is building:</p>
<ul>
  <li><strong>H100 inference benchmarks:</strong> I benchmarked vLLM v0.30 against SGLang v0.5.20 on 2× H100 NVL 94 GB GPUs (NVLink 4.0, CUDA 13.4), Qwen3-8B BF16, TP=2. TTFT, TPOT, and throughput measured across concurrency 1–128. Peak: 5,965 tok/s; RadixAttention: 1,443× TTFT speedup (39 ms vs 55,565 ms) at 131K-token context; 100% SLO compliance. Live: <a href="https://inference-web-theta.vercel.app/benchmarks/llm">inference-web-theta.vercel.app</a>.</li>
  <li><strong>CUDA kernel profiling — KV cache bottleneck:</strong> Using NVIDIA Nsight Systems and Compute, I profiled KV cache CUDA operations on RTX 4090 hardware, identified the memory bandwidth bottleneck, and retuned the kernel access pattern to deliver 3.8× throughput improvement. This required reading warp occupancy reports and memory transaction traces directly — not just running benchmarking scripts.</li>
  <li><strong>Production Kubernetes serving stack:</strong> I built <em>vllm-k8s-stack</em> — production LLM serving with vLLM, KV-cache-aware request routing, HPA autoscaling on GPU node pools, and Prometheus/Grafana observability. This is the infrastructure pattern I would bring to Wayve's inference deployment challenges.</li>
</ul>

<p>Wayve's approach of training one end-to-end neural model rather than modular sensor pipelines is what first caught my attention. The inference throughput and latency requirements for real-time autonomous driving decisions sit exactly at the boundary of model architecture and serving infrastructure that I have been building toward. I am open to relocating to London.</p>
""",
    },
    {
        "slug": "perplexity_ai-inference-engineer",
        "company": "Perplexity AI",
        "recipient": "Perplexity AI",
        "body": """
<p>I am applying for the Member of Technical Staff (AI Inference Engineer) role at Perplexity AI. Perplexity's product is only as good as the inference latency behind it — every query is a race between model quality and response time, and I have spent the last two years making that race faster.</p>

<p>Three achievements that speak directly to Perplexity's inference requirements:</p>
<ul>
  <li><strong>H100 NVL — latency at the microsecond level:</strong> I benchmarked vLLM v0.30 vs SGLang v0.5.20 on 2× NVIDIA H100 NVL 94 GB (NVLink 4.0, CUDA 13.4), Qwen3-8B BF16, TP=2. Peak throughput: 5,965 tok/s. Critical finding: RadixAttention prefix caching reduced TTFT from 55,565 ms to 39 ms — a 1,443× speedup — at 131K-token context with 100% SLO compliance at concurrency 128. Full benchmark: <a href="https://inference-web-theta.vercel.app/benchmarks/llm">inference-web-theta.vercel.app/benchmarks/llm</a>.</li>
  <li><strong>Production inference gateway — 13 optimisations:</strong> I built <em>inference-optimizer</em>, a production-grade AI Inference Gateway across Claude, GPT-4o, and Gemini: parallel execution (3.87× faster), prompt caching (61.4% cost reduction), model routing (64.3% cheaper), dynamic concurrency (14× throughput). The same architecture patterns apply directly to high-throughput query serving at Perplexity's scale.</li>
  <li><strong>GPU profiling and CUDA kernel work:</strong> Using NVIDIA Nsight Systems and Compute, I diagnosed a memory bandwidth bottleneck in KV cache CUDA ops and retuned the kernel, delivering 3.8× throughput improvement. Also achieved 18× latency reduction through continuous batching pipeline redesign.</li>
</ul>

<p>Perplexity's engineering challenge is unique: sub-second answers over a live web index using frontier models, at millions of queries per day. That is the class of inference problem I find most interesting — where the gap between a fast system and a slow one is the product itself. I look forward to hearing from you.</p>
""",
    },
    {
        "slug": "anthropic_staff-inference-engineer",
        "company": "Anthropic",
        "recipient": "Anthropic",
        "body": """
<p>I am applying for the Staff Software Engineer, Inference role at Anthropic. I have spent two years building the kind of inference infrastructure this role is designed to scale — GPU serving stacks, batching pipelines, KV cache optimisation, multi-provider routing, and Kubernetes-based deployment — and I have done it while using Claude as my primary LLM provider.</p>

<p>Three achievements most relevant to the scope of this role:</p>
<ul>
  <li><strong>Distributed inference at H100 scale:</strong> I benchmarked vLLM v0.30 vs SGLang v0.5.20 on 2× NVIDIA H100 NVL 94 GB (NVLink 4.0, CUDA 13.4), Qwen3-8B BF16, TP=2. Measured TTFT, TPOT, throughput, and SLO compliance across concurrency 1–128. Peak: 5,965 tok/s. RadixAttention: 1,443× TTFT speedup (39 ms vs 55,565 ms) at 131K-token context. Every result is published live at <a href="https://inference-web-theta.vercel.app/benchmarks/llm">inference-web-theta.vercel.app/benchmarks/llm</a>.</li>
  <li><strong>Production inference gateway — batching, caching, routing:</strong> I built <em>inference-optimizer</em> — parallel execution (3.87× faster), prompt caching (61.4% cost reduction), model routing (64.3% cheaper), dynamic concurrency (14× throughput) across Claude, GPT-4o, and Gemini. These architecture decisions map directly to the batching, routing, and caching challenges in serving Claude at scale.</li>
  <li><strong>Kubernetes GPU serving infrastructure:</strong> I built <em>vllm-k8s-stack</em> — production LLM serving on Kubernetes with KV-cache-aware routing, HPA autoscaling on GPU node pools, and Prometheus/Grafana observability. Also profiled CUDA KV cache kernels with NVIDIA Nsight, identifying and fixing a memory bandwidth bottleneck that delivered 3.8× throughput improvement.</li>
</ul>

<p>Anthropic's mission to build safe and beneficial AI is one I take seriously — I use Claude in production and I have written about inference engineering publicly. The Staff role here is a chance to work on the infrastructure that underpins that mission at scale. I am open to relocating to London and available to interview at your convenience.</p>
""",
    },
    {
        "slug": "leonardo_ai-platform-engineer",
        "company": "Leonardo UK",
        "recipient": "Leonardo UK, Edinburgh",
        "body": """
<p>I am applying for the AI Platform Engineer role at Leonardo UK. The platform layer you are describing — model serving, inference runtimes, AI gateways, and Kubernetes-based GPU infrastructure — is precisely what I have been building independently, and the Edinburgh hybrid arrangement is ideal from my base in Glasgow.</p>

<p>Three achievements that map directly to what this role requires:</p>
<ul>
  <li><strong>Production Kubernetes LLM serving platform:</strong> I built <em>vllm-k8s-stack</em> — production LLM inference on Kubernetes using a vLLM serving engine, KV-cache-aware request routing, HPA autoscaling on GPU node pools, and a Prometheus/Grafana observability stack. This is the same platform layer above managed GPU infrastructure that Leonardo is looking to own and operate — designed for multi-tenant concurrent workloads with resource controls and availability monitoring. <a href="https://github.com/AyeniOluwatosinOlawale/vllm-k8s-stack">github.com/AyeniOluwatosinOlawale/vllm-k8s-stack</a></li>
  <li><strong>Production AI Gateway — authentication, routing, rate limiting:</strong> I built <em>inference-optimizer</em>, a production AI Inference Gateway spanning Claude, GPT-4o, Gemini, and self-hosted vLLM. It handles authentication, model routing (64.3% cost reduction), rate limiting, parallel execution (3.87× faster), and prompt caching (61.4% cost reduction) — with real-time usage monitoring and audit logging. This is the practical equivalent of LiteLLM or Bifrost deployed as an enterprise AI gateway, which Leonardo explicitly lists as a key area of experience. Live at <a href="https://inference-web-theta.vercel.app">inference-web-theta.vercel.app</a>.</li>
  <li><strong>H100 inference platform operations:</strong> I benchmarked and operated vLLM and SGLang on 2× NVIDIA H100 NVL 94 GB hardware — measuring throughput (5,965 tok/s peak), TTFT, TPOT, and SLO compliance across concurrency 1–128. 100% SLO compliance. I also profiled GPU utilisation with NVIDIA Nsight Systems to identify and resolve performance bottlenecks — the same GPU performance and utilisation management this role requires.</li>
</ul>

<p>Leonardo's focus on making AI capabilities easy to consume for engineering teams while maintaining security, performance, and availability controls resonates with how I have approached building internal AI platform infrastructure. Operating in a secure enterprise environment with restricted internet access is a constraint I have designed around directly — API credential management, offline-capable service design, and air-gap-friendly deployment patterns are part of my operational practice.</p>

<p>I am happy to discuss the architecture of any of these systems in detail, walk through the Kubernetes serving configuration, or demonstrate the gateway observability setup. I look forward to hearing from you.</p>
""",
    },
    {
        "slug": "doubleword_inference-research",
        "company": "Doubleword",
        "recipient": "Doubleword, London, UK",
        "body": """
<p>I am writing to apply for the Member of Technical Staff: Inference Research role at Doubleword. Your focus on multi-LoRA serving, GPU architecture, and speculative decoding is exactly the class of problem I have been building toward — and I have the benchmarks to prove it.</p>

<p>Three specific achievements relevant to this role:</p>
<ul>
  <li><strong>H100 NVL inference research — RadixAttention and prefix caching:</strong> I benchmarked vLLM v0.30 vs SGLang v0.5.20 on 2× NVIDIA H100 NVL 94 GB (NVLink 4.0, CUDA 13.4), Qwen3-8B BF16, TP=2. The critical finding was the impact of RadixAttention prefix caching in memory-constrained long-context settings: 1,443× TTFT speedup (39 ms vs 55,565 ms) at 131K-token context, with 100% SLO compliance at concurrency 128 and peak throughput of 5,965 tok/s. Results: <a href="https://inference-web-theta.vercel.app/benchmarks/llm">inference-web-theta.vercel.app</a>.</li>
  <li><strong>CUDA kernel profiling and speculative decoding:</strong> Using NVIDIA Nsight Systems and Compute, I profiled KV cache CUDA ops on RTX 4090 hardware — identified memory bandwidth as the bottleneck and retuned kernel access patterns for 3.8× throughput improvement. I also ran speculative decoding experiments across vLLM and SGLang to characterise speedup vs draft model overhead tradeoffs, documented in <em>open-model-engine</em>.</li>
  <li><strong>Multi-modal LLM inference — vLLM-Omni:</strong> I built <em>lab-vllm-omni</em>, a phased inference lab covering all 5 output modalities (text, audio, image, video, structured output) — characterising throughput, memory pressure, and scheduling behaviour across modalities. Directly relevant to serving diverse inference workloads efficiently.</li>
</ul>

<p>Doubleword's approach — small team, deep technical work, research-to-production focus — is exactly what I want. I am based in Glasgow and happy to relocate to London; Farringdon 2–3 days/week is workable.</p>
""",
    },
    {
        "slug": "doubleword_inference-systems",
        "company": "Doubleword",
        "recipient": "Doubleword, London, UK",
        "body": """
<p>I am writing to apply for the Member of Technical Staff: Inference Systems role at Doubleword. Building a distributed batch inference platform that handles high load with low latency is exactly the kind of systems problem I find most interesting — and I have built the closest equivalent I could as an independent engineer.</p>

<p>Three achievements directly relevant to what this role requires:</p>
<ul>
  <li><strong>Kubernetes LLM serving platform:</strong> I built <em>vllm-k8s-stack</em> — production LLM serving on Kubernetes with a vLLM backend, KV-cache-aware request routing, HPA autoscaling on GPU node pools, and a Prometheus/Grafana observability stack. The system was designed around the constraint that KV cache state cannot be migrated mid-request — so routing decisions must account for prefix reuse. This is the core challenge in a batch inference platform. <a href="https://github.com/AyeniOluwatosinOlawale/vllm-k8s-stack">GitHub</a></li>
  <li><strong>Database optimisation under concurrent load:</strong> I run Supabase (PostgreSQL) as the primary data layer for multi-tenant production applications — designed schemas for concurrent session workloads, tuned query plans for hot paths, and instrumented with real-time observability. Sub-500 ms end-to-end latency under bursty concurrent load is a constraint I have engineered around directly.</li>
  <li><strong>H100 SLO compliance at scale:</strong> Benchmarked vLLM v0.30 vs SGLang v0.5.20 on 2× H100 NVL 94 GB measuring throughput, TTFT, TPOT, and SLO compliance across concurrency 1–128. Peak: 5,965 tok/s; 100% SLO compliance at concurrency 128. Understanding where a serving system breaks its SLO guarantees is as important as peak throughput. <a href="https://inference-web-theta.vercel.app/benchmarks/llm">Live results</a>.</li>
</ul>

<p>I write primarily in Python but am actively building Rust tooling for inference systems — I understand why Rust is the right choice for a low-latency inference platform. I am open to relocating to London; Farringdon 2–3 days/week is workable.</p>
""",
    },
]

# ── HTML BUILDERS ────────────────────────────────────────────────────────────

def build_cv_html(role):
    comps = "".join(
        f'<div class="cvitem"><div class="cvitem-label">{k}</div><div class="cvitem-val">{v}</div></div>'
        for k, v in role["competencies"]
    )
    projects = "".join(
        f'<div class="entry"><div class="entry-left" style="font-size:8pt;font-weight:700">{n}</div>'
        f'<div class="entry-right" style="font-size:8.5pt">{d}</div></div>'
        for n, d in role["projects"]
    )
    edu = "".join(
        f'<div class="entry"><div class="entry-left">{y}</div>'
        f'<div class="entry-right"><span class="entry-title">{deg}</span> — <span class="entry-org">{inst}</span>, <span class="entry-loc">{loc}</span></div></div>'
        for y, deg, inst, loc in COMMON["education"]
    )
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<style>{CSS_CV}</style></head><body>
<h1>{COMMON["name"]}</h1>
<div class="subtitle">{role["title"]} — {role["company"]}</div>
<div class="contact">{COMMON["contact"]}</div>
<hr class="title-rule">

<h2>Profile</h2>
<div class="tagline">{role["tagline"]}</div>

<h2>Core Competencies</h2>
{comps}

<h2>Professional Experience</h2>
{EXPERIENCE_FULL}

<h2>Key Projects</h2>
{projects}

<h2>Education</h2>
{edu}

<h2>Open Source</h2>
<div class="cvitem"><div class="cvitem-label">GitHub</div><div class="cvitem-val">{COMMON["repos"]}</div></div>
</body></html>"""


def build_cl_html(cl):
    from datetime import date
    today = date.today().strftime("%-d %B %Y")
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<style>{CSS_CL}</style></head><body>
<div class="sender">
  <strong>Oluwatosin Ayeni</strong>
  Glasgow, Scotland, UK<br>
  07727305230 &nbsp;·&nbsp; ayenioluwatosinolawale@gmail.com<br>
  <a href="https://github.com/AyeniOluwatosinOlawale">github.com/AyeniOluwatosinOlawale</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/oluwatosinolawaleayeni/">linkedin.com/in/oluwatosinolawaleayeni</a>
</div>
<div class="date">{today}</div>
<div class="recipient"><strong>{cl["recipient"]}</strong></div>
<p>Dear Hiring Team,</p>
{cl["body"]}
<div class="closing">
  <p>Yours sincerely,</p>
  <p><strong>Oluwatosin Ayeni</strong></p>
  <div class="sig-links">
    <a href="https://github.com/AyeniOluwatosinOlawale">github.com/AyeniOluwatosinOlawale</a><br>
    <a href="https://www.linkedin.com/in/oluwatosinolawaleayeni/">linkedin.com/in/oluwatosinolawaleayeni</a>
  </div>
</div>
</body></html>"""


# ── GENERATE ALL ─────────────────────────────────────────────────────────────

print(f"Generating PDFs into {OUTPUT}/\n")

for role in ROLES:
    slug = role["slug"]
    html = build_cv_html(role)
    out = f"{OUTPUT}/cv_{slug}.pdf"
    print(f"  CV:  {out}")
    HTML(string=html).write_pdf(out, stylesheets=[CSS(string="")])

for cl in COVER_LETTERS:
    slug = cl["slug"]
    html = build_cl_html(cl)
    out = f"{OUTPUT}/cover_{slug}.pdf"
    print(f"  CL:  {out}")
    HTML(string=html).write_pdf(out, stylesheets=[CSS(string="")])

print(f"\nDone. Files saved to {OUTPUT}/")
print("\n".join(os.listdir(OUTPUT)))
