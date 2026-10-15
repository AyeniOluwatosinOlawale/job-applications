# Daily Job Search Agent Instructions

## Candidate
Oluwatosin Olawale Ayeni — ayenioluwatosinolawale@gmail.com — Glasgow UK
Phone: 07727305230
LinkedIn: https://www.linkedin.com/in/oluwatosinolawaleayeni/
GitHub: https://github.com/AyeniOluwatosinOlawale
Portfolio: https://portfolio-ten-brown-40.vercel.app/
Consulting: https://anaai.tech | https://vertinab.com

## Target Roles
LLM Inference Engineer, ML Engineer (LLM), Generative AI Engineer, AI Engineer, MLOps Engineer, AI Research Engineer

## Skills
Primary: Python, vLLM, SGLang, TensorRT-LLM, CUDA/NVIDIA Nsight, AWQ, speculative decoding, KV cache optimisation, PyTorch, LLM fine-tuning (Mistral 7B / Phi-4 / Qwen3 / Gemma 2 via PEFT/LoRA), LangChain, RAG systems, n8n, FastAPI, Docker, Kubernetes, Claude API
Secondary: TypeScript, SQL, Scikit-learn, NLP, Computer Vision, Pandas, Power BI, React, Next.js, PostgreSQL, Redis, GitHub Actions, Vertex AI

## GitHub: 43 public repos — github.com/AyeniOluwatosinOlawale
## Portfolio: portfolio-ten-brown-40.vercel.app
## Consulting: vertinab.com | anaai.tech

## Work History
- Founder & Lead Engineer, Nexora Academic, Jan 2025-present (Glasgow): multi-tenant AI inference engineering platform (web + desktop + CLI); benchmarking tools for prompt caching, streaming, structured output, batching; full-stack SaaS (Supabase, Next.js, Stripe, Tauri); designed 13-phase AI Inference Engineering curriculum
- AI Automation Engineer, EduTech Global, Mar 2026-present (remote): student chatbot for ABU and Babcock Univ; n8n AI workflows; LinkedIn auto-poster; Google Sheets automation
- Founder & AI Consultant, Vertinab / AnaburyAI Technology, Jan 2023-present (Glasgow): 28x LLM cost reduction via vLLM/SGLang on RTX 4090; 3.8x throughput KV cache; 18x latency continuous batching; +22% diagnostic accuracy Mistral 7B radiology fine-tune; AI strategy consulting; built AnaRadiologyAI chatbot, anaai.tech, vertinab.com
- Senior Software Engineer (Contract), EduTechConnect / Stellar Labs, 2024-present (remote): n8n automation engine WhatsApp Cloud API → Zoho CRM → Supabase; chatbot data-capture for talent management (Purple Squirrel); real-time lead scoring & alert workflows via Meta Cloud API
- Data Analyst, Bytelab Technologies Ltd, Jan 2018-Jul 2022 (Nigeria)
- Junior Data Analyst, Ministry of Education Nigeria, Mar-Oct 2017

## Education
MSc AI and Applications, Distinction, University of Strathclyde 2023
MTech/BSc Physics, Federal University of Technology Akure 2016

## Key Projects
Inference & Serving:
- open-model-engine: GPU-first inference benchmarking for self-hosted open models — vLLM, SGLang, LayerScale; conventional load sweep + agentic multi-turn workloads (github.com/AyeniOluwatosinOlawale/open-model-engine)
- inference-engineering-labs: Qwen2.5-7B benchmarks, 28x cost reduction RTX 4090; quantization, speculative decoding, serving optimisation (github.com/AyeniOluwatosinOlawale/inference-engineering-labs)
- inference-harness: unified benchmarking harness for closed APIs — Anthropic, OpenAI, Gemini; single interface comparing latency/cost/throughput (github.com/AyeniOluwatosinOlawale/inference-harness)
- inference-optimizer: AI Inference Optimizer — automatically makes LLM API calls faster/cheaper via prompt caching, streaming, structured output, batching (github.com/AyeniOluwatosinOlawale/inference-optimizer)
- vllm-k8s-stack: production LLM serving on Kubernetes — vLLM, KV-cache-aware routing, HPA autoscaling, GPU node management (github.com/AyeniOluwatosinOlawale/vllm-k8s-stack)
- lab-vllm-omni: phased inference lab for vLLM-Omni covering all 5 output modalities — text, audio, image, video, structured output (github.com/AyeniOluwatosinOlawale/lab-vllm-omni)
- CUDA kernel optimisation: KV cache 3.8x throughput, batching 18x latency reduction (github.com/AyeniOluwatosinOlawale/phase2-llm-inference-deep-dive)

Fine-tuning & Models:
- Offline AI Health Assistant: Mistral 7B fine-tuned on radiology data, +22% diagnostic accuracy (github.com/AyeniOluwatosinOlawale/Offline-AI-Assisted-Health-Diagnosis)
- My_finetuned_Phi-4: Phi-4 LoRA fine-tuned on Cosmopedia dataset — full pipeline: data prep, LoRA, eval, inference (github.com/AyeniOluwatosinOlawale/My_finetuned_Phi-4)
- Qwen3-TinyStories-Training: complete Qwen3-based LM training pipeline — tokenizer training, architecture, training loop, generation eval (github.com/AyeniOluwatosinOlawale/Qwen3-TinyStories-Tokenizer-Model-Training)
- embeddinggemma2-local-api: self-hosted EmbeddingGemma 2 API optimised for Apple Silicon — auto-start local embeddings, zero cloud dependency (github.com/AyeniOluwatosinOlawale/embeddinggemma2-local-api)
- Building SLM from scratch: transformer architecture and training loop from first principles

RAG & Agents:
- Conversational Multi-PDF RAG Assistant: LangChain-based conversational query across multiple PDFs (github.com/AyeniOluwatosinOlawale/-Conversational-Multi-PDF-RAG-Assistant-using-LangChain)
- AnaRadiologyAI: domain-specific LLM assistant for radiology Q&A (github.com/AyeniOluwatosinOlawale/AnaRadiologyAI)
- AI Automation n8n workflows (github.com/AyeniOluwatosinOlawale/AI-Powered-Automation-Workflows-with-n8n)

Research:
- Multilingual-Emotion-Analyzer: NLP pipeline for multilingual emotion detection — MSc AI research (github.com/AyeniOluwatosinOlawale/-Multilingual-Emotion-Action-Analyzer)
- PathLoss-ML-mmWave: ML-based path loss prediction for mmWave/Sub-THz 5G/6G networks — MSc AI research (github.com/AyeniOluwatosinOlawale/PathLoss-ML-Predicting-mmWave-Sub-THz-Path-Loss-with-Machine-Learning)
- Open source contributor: build-an-llm (github.com/thekingslee/build-an-llm)

## Constraints
- Location: Glasgow, open to remote, hybrid, London relocation for strong roles
- Deal-breakers: security clearance required, pure management, no AI/ML component
- Always skip: Mistral AI (already applied 2026-10-15)

---

## PART 0 — PROFILE REFRESH (every 3 days)

Run this part FIRST, before anything else.

### 0.1 — Check if refresh is due

Read profile_meta.json. If the file does not exist, create it:
  {"last_profile_refresh": "2000-01-01", "github_repo_count": 0}

Parse last_profile_refresh. If today minus last_profile_refresh is less than 3 days: skip to Part A (no refresh needed).
If 3 or more days have passed: proceed with steps 0.2 through 0.6.

### 0.2 — Fetch GitHub repos

WebFetch: https://api.github.com/users/AyeniOluwatosinOlawale/repos?sort=updated&per_page=100

This returns a JSON array. Extract for each repo:
- name
- description
- language
- updated_at
- html_url
- topics (array)

Also WebFetch: https://github.com/AyeniOluwatosinOlawale
Extract: total public repo count, pinned repos (if visible in the HTML), bio text.

For any repo whose name is NOT already listed anywhere in the "## Key Projects" section of this file:
- WebFetch the repo's README: https://raw.githubusercontent.com/AyeniOluwatosinOlawale/[REPO_NAME]/main/README.md
  (If 404, try: /master/README.md)
- Read the README to understand what the project does, its tech stack, and any quantified results.
- Decide if it is relevant to LLM inference / ML engineering / AI systems / production AI.
  If yes: add it to the appropriate Key Projects category below.
  If not relevant (e.g. a pure web project with no AI component): skip it.

For any NEW skills or technologies found across the new repos that are not already in the ## Skills section: add them.

Update the ## GitHub line to reflect the current repo count.

### 0.3 — Fetch LinkedIn profile

WebFetch: https://www.linkedin.com/in/oluwatosinolawaleayeni/
LinkedIn returns limited content without login. Extract whatever is visible: headline, about summary, any experience or skills listed in the public view.

Also WebSearch: site:linkedin.com/in/oluwatosinolawaleayeni
This sometimes surfaces cached snippets with richer text.

If any new role, certification, skill, or achievement is found that is NOT already in the Work History or Skills sections of this file: add it.

### 0.4 — Fetch portfolio

WebFetch: https://portfolio-ten-brown-40.vercel.app/
Extract any new projects, skills, or experience entries not already in this file and add them.

### 0.5 — Write updates back to this file

Update the relevant sections of AGENT_INSTRUCTIONS.md in place:
- ## Skills — add any new skills found
- ## GitHub: N public repos line — update count
- ## Key Projects — add any new relevant repos with one-line description and GitHub URL
- ## Work History — update if any new role or promotion found

Important: do NOT remove any existing information. Only add or update.

### 0.6 — Commit the updated profile

Update profile_meta.json:
  {"last_profile_refresh": "[TODAY YYYY-MM-DD]", "github_repo_count": [N]}

Run:
  git config user.email ayenioluwatosinolawale@gmail.com
  git config user.name AyeniOluwatosinOlawale
  git add AGENT_INSTRUCTIONS.md profile_meta.json
  git diff --cached --quiet || git commit -m "chore: profile refresh $(date +%Y-%m-%d)"
  git push origin master 2>/dev/null || git push origin main 2>/dev/null || true

---

## PART A — CHECK FOR RESPONSES TO EXISTING APPLICATIONS

1. Read tracker.csv (header: date,company,role,status,fit_score,apply_url,cv_file,cover_letter_file,auto_applied,notes,last_updated)
   If the file lacks the auto_applied column, add it after cover_letter_file (default empty for existing rows).
2. For each open row (status not rejected or offer_accepted): use Gmail MCP to search for emails mentioning the company name, last 7 days, not in sent
3. Classify replies: interview invite -> interview_scheduled; rejection -> rejected; assessment/task -> assessment_received; offer -> offer_received
4. Update those tracker rows in memory
5. Any row with status drafted or applied where date is 14+ days before today: append follow_up_due to notes
6. Write updated tracker.csv back to disk

---

## PART B — SEARCH FOR NEW JOBS (posted last 24h)

Search ALL of the following sources. Collect every job URL found.

### LinkedIn
WebFetch:
- https://www.linkedin.com/jobs/search/?keywords=LLM+inference+engineer&location=United+Kingdom&f_TPR=r86400
- https://www.linkedin.com/jobs/search/?keywords=generative+AI+engineer&location=United+Kingdom&f_TPR=r86400&f_WT=2
- https://www.linkedin.com/jobs/search/?keywords=ML+engineer+LLM&location=United+Kingdom&f_TPR=r86400
- https://www.linkedin.com/jobs/search/?keywords=AI+engineer+LLM&location=United+Kingdom&f_TPR=r86400
- https://www.linkedin.com/jobs/search/?keywords=MLOps+LLM+engineer&location=United+Kingdom&f_TPR=r86400&f_WT=2

### Indeed UK
WebFetch:
- https://uk.indeed.com/jobs?q=LLM+inference+engineer&fromage=1&sort=date
- https://uk.indeed.com/jobs?q=generative+AI+engineer&fromage=1&sort=date
- https://uk.indeed.com/jobs?q=ML+engineer+LLM&l=United+Kingdom&fromage=1&sort=date
- https://uk.indeed.com/jobs?q=AI+engineer+LLM&l=United+Kingdom&fromage=1&sort=date

### Reed UK
WebFetch:
- https://www.reed.co.uk/jobs/llm-engineer-jobs?datecreatedoffset=1
- https://www.reed.co.uk/jobs/ai-engineer-jobs?datecreatedoffset=1&keywords=LLM

### Totaljobs
WebFetch:
- https://www.totaljobs.com/jobs/llm-engineer?postedWithin=1
- https://www.totaljobs.com/jobs/ai-engineer?postedWithin=1&keywords=LLM

### Greenhouse / Lever / Ashby (ATS portals used by AI startups)
WebSearch:
- site:greenhouse.io "LLM" OR "inference" engineer UK 2026
- site:lever.co "LLM" OR "generative AI" engineer UK 2026
- site:ashbyhq.com "ML engineer" OR "AI engineer" LLM UK 2026
- site:workable.com "LLM engineer" UK 2026

### Google Jobs via WebSearch
WebSearch queries:
- "LLM inference engineer" UK job site:linkedin.com OR site:greenhouse.io OR site:lever.co
- "generative AI engineer" UK remote job site:linkedin.com OR site:greenhouse.io
- "ML engineer" LLM UK remote job posted:today
- "AI engineer" LLM inference UK 2026 site:linkedin.com OR site:indeed.com
- "MLOps engineer" LLM UK remote site:linkedin.com OR site:lever.co
- LLM engineer job UK "apply by email" OR "send CV" OR "email your CV"

### HackerNews Who's Hiring (monthly thread — check if current month thread exists)
WebFetch: https://news.ycombinator.com/item?id=43986235
(If that 404s, WebSearch: site:news.ycombinator.com "Ask HN: Who is hiring" 2026 to find the current thread ID)
Extract remote ML/AI/LLM roles. Many HN jobs have direct email addresses — flag these for auto-apply.

### Remote-first boards
WebFetch:
- https://remoteok.com/remote-ml-jobs
- https://weworkremotely.com/categories/remote-machine-learning-jobs

### Company career pages (check directly for new postings)
WebFetch each careers page and look for new LLM/ML/AI engineer openings:
- https://www.anthropic.com/careers
- https://deepmind.google/careers/
- https://huggingface.co/jobs
- https://cohere.com/careers
- https://mistral.ai/careers (skip if role is same as already applied)
- https://stability.ai/careers
- https://wayve.ai/careers
- https://poly.ai/careers
- https://faculty.ai/careers
- https://quantexa.com/careers

For each job URL found across all sources, WebFetch the full posting page to extract: title, company, location, requirements, responsibilities, HOW TO APPLY (very important — check for email address, portal form, or LinkedIn Easy Apply), apply URL or email.

Skip rules: already in tracker (match company+role any status), Mistral AI Applied AI Forward Deployed ML Engineer, security clearance required, no AI/ML, citizenship/PR required.

---

## PART C — EVALUATE EACH NEW JOB

Score 0-100 on four weighted dimensions:
- Technical Skills match (30%): how well requirements match primary/secondary skills
- Experience Match (25%): relevance of work history
- Behavioral/Culture Fit (15%): autonomous/ship-focused/technical depth = strong; heavy process/compliance-first = friction
- Career Alignment (30%): advances toward LLM inference engineering depth at a strong company

Location: PASS if remote/hybrid/UK. FAIL if requires leaving UK or security clearance.
Strong Fit 75+: generate documents. Worth Reviewing 60-74: flag only. Below 60: skip.

For each job also determine the APPLICATION METHOD:
- EMAIL: the posting provides an email address to send applications to -> can auto-apply
- PORTAL: requires submitting via a web form, uploading files to ATS, or LinkedIn Easy Apply -> manual required
- UNKNOWN: no clear method found -> flag as manual

---

## PART D — GENERATE DOCUMENTS FOR STRONG FITS

For each 75+ job, create two files. Slugs are lowercase-hyphenated (e.g. deepmind, ml-engineer).

CV file: cv/main_COMPANY-SLUG_ROLE-SLUG.tex
- Use moderncv documentclass, banking style, blue color, 0.80 scale geometry
- name: Oluwatosin / Ayeni, address: Glasgow UK, phone: 07727305230, email: ayenioluwatosinolawale@gmail.com
- extrainfo with LinkedIn and GitHub links
- Sections: tailored profile statement (3-5 lines), core competencies (5 categories weighted to this role), professional experience (all 4 roles with role-relevant bullets emphasised), key projects (4-5 most relevant to this role), education (MSc Distinction Strathclyde 2023, MTech/BSc FUTA 2016), references available on request
- Target 2 pages

Cover letter file: cover_letters/cover_COMPANY-SLUG_ROLE-SLUG.tex
- Use letter documentclass, 1in margins
- Sender: Oluwatosin Ayeni, Glasgow, ayenioluwatosinolawale@gmail.com, 07727305230
- Addressee: Hiring Team at COMPANY
- Opening paragraph: name the role, state single strongest fit signal
- Bullet list: 3-4 specific achievements from work history mapped to posting requirements
- Company paragraph: reference something real and specific about this company — never generic
- Closing: one sentence on working style fit, I look forward to hearing from you
- Target 1 page

Also write a plain-text email version of the cover letter: cover_letters/cover_COMPANY-SLUG_ROLE-SLUG_email.txt
This is used for auto-apply. Same content as the LaTeX cover letter but formatted as plain text for an email body. Include at the end: "My CV is available at https://github.com/AyeniOluwatosinOlawale/job-applications/blob/master/cv/main_COMPANY-SLUG_ROLE-SLUG.tex (LaTeX source) — I am happy to provide a compiled PDF on request, or please let me know if you need it in another format."

---

## PART E — AUTO-APPLY FOR EMAIL JOBS

For each Strong Fit job where APPLICATION METHOD is EMAIL:

1. Use Gmail MCP to send an application email to the posting's email address
2. Email subject: "Application for [Role Title] — Oluwatosin Ayeni"
3. Email body: use the content of cover_letters/cover_COMPANY-SLUG_ROLE-SLUG_email.txt
4. CC: ayenioluwatosinolawale@gmail.com (so there is a sent copy)
5. Mark auto_applied = true in tracker row
6. Update tracker status to applied (not just drafted)
7. Add to notes: "Auto-applied via email to [email address] on [date]"

Do NOT auto-apply to portal jobs — those require manual file upload.

---

## PART F — COLD OUTREACH (3 per day)

Send 3 personalised cold-outreach emails per day to HR managers, talent leads, or technical hiring contacts at AI/ML companies and research labs. Track every contact in outreach.csv so no one is emailed twice.

### outreach.csv columns
date,company,contact_name,contact_email,contact_role,company_type,email_sent,notes

If the file does not exist, create it with just the header.

### Target companies for cold outreach (rotate through — never repeat a company already in outreach.csv)

AI Research Labs:
- DeepMind (deepmind.google) — London
- Anthropic — UK/remote
- Meta AI (Research) — London
- Microsoft Research Cambridge
- Samsung AI Research — Cambridge
- Qualcomm AI Research — London
- ARM ML Group — Cambridge
- NVIDIA AI Research — remote/London
- AMD ROCm / AI — remote

UK AI Companies:
- Wayve (wayve.ai) — London, AV + LLM
- PolyAI (poly.ai) — London, conversational AI
- Faculty.ai — London
- Quantexa — London, AI analytics
- Stability AI — London/remote
- Cohere — London/remote
- Coreweave — London, GPU cloud
- Groq — remote, inference hardware/software
- Modal Labs (modal.com) — remote
- Replicate (replicate.com) — remote
- Fireworks AI — remote

AI-Heavy Product Companies:
- Harvey AI
- Waymo (London presence)
- Palantir (London)
- Babylon Health / successor
- Healx — Cambridge, AI drug discovery
- BenevolentAI — London
- Exscientia — Oxford, AI drug discovery

### Step-by-step each day

1. Read outreach.csv. Collect all companies already contacted (column: company).

2. Pick 3 companies from the target list above that are NOT already in outreach.csv and NOT already in tracker.csv as applied/drafted.

3. For each of the 3 companies:

   a. WebFetch the company's careers or about page to find any named HR, Talent, or Recruiting contact.
      Also WebSearch: "[company name] head of talent email" OR "[company name] recruiter LinkedIn AI engineering"
      Try patterns: careers@, hr@, talent@, recruiting@[domain]
      If a named contact is found (e.g. "Sarah Jones, Talent Partner"), prefer them over a generic address.

   b. If no email is found after two searches: use careers@ or hr@ at their primary domain as a best-effort address.
      Note in outreach.csv: email_found=inferred.

   c. Write a cold outreach email using this exact template (personalise the [SLOTS]):

      Subject: LLM Inference Engineer — Open to Opportunities at [Company Name]

      Body:
      Hi [Contact Name / Hiring Team],

      I'm Oluwatosin Ayeni — an AI & ML Engineer based in Glasgow, Scotland, specialising in LLM inference engineering and production AI systems.

      A few things that might be relevant to [Company Name]:
      • Benchmarked Qwen2.5-7B on RTX 4090 with vLLM and SGLang — achieved 28x cost reduction and 18x latency improvement via continuous batching and KV cache optimisation.
      • Fine-tuned Mistral 7B on radiology data: +22% diagnostic accuracy, −35% hallucination rate — deployed as a live clinical assistant.
      • Built a production LLM serving stack on Kubernetes (vllm-k8s-stack): KV-cache-aware routing, HPA autoscaling, GPU node management.
      • MSc Artificial Intelligence with Distinction — University of Strathclyde, 2023.

      I'm actively looking for LLM inference, ML engineering, or AI systems roles — open to remote, hybrid, or Glasgow/London-based.

      My profiles:
      • GitHub (43 repos, inference benchmarks, fine-tuning pipelines): https://github.com/AyeniOluwatosinOlawale
      • LinkedIn: https://www.linkedin.com/in/oluwatosinolawaleayeni/
      • CV (LaTeX source): https://github.com/AyeniOluwatosinOlawale/job-applications/blob/master/cv/main_example.tex

      [ONE SENTENCE SPECIFIC TO THIS COMPANY — e.g. for Wayve: "I'm particularly drawn to Wayve's approach of training end-to-end neural driving models — the inference throughput challenges at that scale are exactly the class of problem I want to work on." For DeepMind: "DeepMind's work on Gemini's architecture and the inference optimisation research coming out of the systems team is what pulled me into this field." For Cohere: "Cohere's focus on enterprise-grade open models and the serving infrastructure needed to run them at scale aligns exactly with what I've been building independently."]

      I'd welcome a conversation — even a 15-minute call — if there's a fit.

      Best regards,
      Oluwatosin Ayeni
      07727305230 | ayenioluwatosinolawale@gmail.com

   d. Send the email via Gmail MCP:
      - To: [contact email]
      - CC: ayenioluwatosinolawale@gmail.com
      - Subject and body as above

   e. Append a row to outreach.csv:
      date=today, company=[company], contact_name=[name or "Hiring Team"], contact_email=[email], contact_role=[role or "unknown"], company_type=[Research Lab / UK AI Company / etc.], email_sent=true, notes=[any detail]

4. If all target companies have been contacted (outreach.csv is exhaustive), WebSearch for:
   - "AI inference engineer hiring UK 2026 email"
   - "LLM ML engineer hiring email contact lab 2026"
   Find 3 new companies from these results and add them to the outreach run.

---

## PART G — UPDATE TRACKER AND COMMIT

1. For each 75+ job append row to tracker.csv:
   - date=today, company, role, status=applied (if auto-applied) or drafted (if manual needed)
   - fit_score=number, apply_url, cv_file path, cover_letter_file path
   - auto_applied=true or false
   - notes=brief fit reason + application method
   - last_updated=today

2. Run:
   git config user.email ayenioluwatosinolawale@gmail.com
   git config user.name AyeniOluwatosinOlawale
   git add .
   git diff --cached --quiet || git commit -m "chore: daily job search $(date +%Y-%m-%d)"
   git push origin master 2>/dev/null || git push origin main 2>/dev/null || true

---

## PART H — SEND EMAIL SUMMARY

Use Gmail MCP. Send to: ayenioluwatosinolawale@gmail.com
Subject: Job Search Daily - [DATE]

Email body:

APPLICATION UPDATES
For each status change: [Company] - [Role] - [old] -> [NEW] - brief detail
For follow-ups due: FOLLOW-UP DUE: [Company] - [Role] - Applied [date] - [N] days no response - [URL]
If no updates: No new responses found for open applications.

AUTO-APPLIED (done for you)
For each job where auto_applied=true today:
  [Score]/100 | [Title] at [Company] | [Location]
  Sent to: [email address]
  Why strong fit: [2 sentences]
  Posting: [URL]

NEW STRONG FITS - MANUAL UPLOAD REQUIRED
For each 75+ job today that is PORTAL-based (manual):
  [Score]/100 | [Title] at [Company] | [Location]
  Why strong fit: [2 sentences]
  Apply here: [URL]
  Files at github.com/AyeniOluwatosinOlawale/job-applications:
    cv/main_[slug].tex and cover_letters/cover_[slug].tex
  ACTION: Download, compile (lualatex for CV, xelatex for cover letter), upload to portal

WORTH A LOOK (60-74)
For each 60-74 job: [Score]/100 | [Title] at [Company] | one-line reason | [URL]
If none: None today.

COLD OUTREACH SENT TODAY
For each of the 3 companies contacted:
  [Company] — [Contact Name / Hiring Team] — [contact email]
  Why targeted: [one sentence on why this company is relevant]
  Total outreach to date: X companies contacted

SOURCES SEARCHED TODAY
List every source that was checked (LinkedIn, Indeed, Reed, Totaljobs, HackerNews, RemoteOK, Anthropic, DeepMind, etc.) and how many jobs were found from each.

STATS
Total jobs scanned: X | Auto-applied: X | Manual upload needed: X | Worth reviewing: X | Application updates: X | Follow-ups due: X | Cold outreach sent today: 3

If no new jobs found: email with just application updates, cold outreach, sources checked, and note no new roles in last 24h.
If any source fails to load: note it in the Sources section but continue with the rest.
