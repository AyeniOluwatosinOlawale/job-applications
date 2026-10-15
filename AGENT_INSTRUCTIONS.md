# Daily Job Search Agent Instructions

## Candidate
Oluwatosin Olawale Ayeni — ayenioluwatosinolawale@gmail.com — Glasgow UK
Phone: 07727305230 | LinkedIn: linkedin.com/in/oluwatosinolawaleayeni | GitHub: github.com/AyeniOluwatosinOlawale | anaai.tech

## Target Roles
LLM Inference Engineer, ML Engineer (LLM), Generative AI Engineer, AI Engineer, MLOps Engineer

## Skills
Primary: Python, vLLM, SGLang, TensorRT-LLM, CUDA/NVIDIA Nsight, AWQ, speculative decoding, KV cache optimisation, PyTorch, TensorFlow, LLM fine-tuning (Mistral 7B / Phi-4 / Qwen3 via PEFT/LoRA), LangChain, RAG systems, n8n
Secondary: TypeScript, SQL, Scikit-learn, NLP, Computer Vision, Pandas, Power BI

## Work History
- AI Automation Engineer, EduTech Global, Mar 2026-present (remote): student chatbot for ABU and Babcock Univ; n8n AI workflows; LinkedIn auto-poster; Google Sheets automation
- AI Engineer self-employed, AnaburyAI Technology, Jan 2023-present (Glasgow): 28x LLM cost reduction via vLLM/SGLang on RTX 4090; 3.8x throughput KV cache; 18x latency continuous batching; +22% diagnostic accuracy Mistral 7B fine-tuning; built vertinab.com and nexora-academic.com
- Data Analyst, Bytelab Technologies Ltd, Jan 2018-Jul 2022 (Nigeria)
- Junior Data Analyst, Ministry of Education Nigeria, Mar-Oct 2017

## Education
MSc AI and Applications, Distinction, University of Strathclyde 2023
MTech/BSc Physics, Federal University of Technology Akure 2016

## Key Projects
- Qwen2.5-7B inference benchmarks: 28x cost reduction RTX 4090 (github.com/AyeniOluwatosinOlawale/inference-engineering-labs)
- CUDA kernel optimisation: KV cache 3.8x, batching 18x (github.com/AyeniOluwatosinOlawale/phase2-llm-inference-deep-dive)
- Offline AI Health Assistant: Mistral 7B radiology fine-tune +22% accuracy (github.com/AyeniOluwatosinOlawale/Offline-AI-Assisted-Health-Diagnosis)
- Building SLM from scratch: transformer from first principles
- Nexora Academic: AI learning platform with intelligent agents (nexora-academic.com)
- EduTech chatbot live: edutechinternalchatbot.vercel.app
- LangChain Multi-PDF RAG Assistant
- AI Automation n8n workflows
- Open source: build-an-llm contributor

## Constraints
- Location: Glasgow, open to remote, hybrid, London relocation for strong roles
- Deal-breakers: security clearance required, pure management, no AI/ML component
- Always skip: Mistral AI (already applied 2026-10-15)

---

## PART A — CHECK FOR RESPONSES TO EXISTING APPLICATIONS

1. Read tracker.csv (header: date,company,role,status,fit_score,apply_url,cv_file,cover_letter_file,notes,last_updated)
2. For each open row (status not rejected or offer_accepted): use Gmail MCP to search for emails mentioning the company name, last 7 days, not in sent
3. Classify replies: interview invite -> interview_scheduled; rejection -> rejected; assessment/task -> assessment_received; offer -> offer_received
4. Update those tracker rows in memory
5. Any row with status drafted or applied where date is 14+ days before today: append follow_up_due to notes
6. Write updated tracker.csv back to disk

---

## PART B — SEARCH FOR NEW JOBS (posted last 24h)

Use WebSearch with these queries:
- LLM inference engineer UK site:linkedin.com
- generative AI engineer UK remote site:linkedin.com
- ML engineer LLM UK site:greenhouse.io OR site:lever.co OR site:ashbyhq.com
- AI engineer LLM UK remote job 2026
- MLOps engineer LLM UK remote

Also try WebFetch on:
- https://www.linkedin.com/jobs/search/?keywords=LLM+inference+engineer&location=United+Kingdom&f_TPR=r86400
- https://www.linkedin.com/jobs/search/?keywords=generative+AI+engineer&location=United+Kingdom&f_TPR=r86400&f_WT=2

For each job URL found, WebFetch the full posting page to extract title, company, location, requirements, apply URL.

Skip rules: already in tracker (match company+role any status), Mistral AI, security clearance required, no AI/ML component

---

## PART C — EVALUATE EACH NEW JOB

Score 0-100 on four weighted dimensions:
- Technical Skills match (30%): how well requirements match primary/secondary skills
- Experience Match (25%): relevance of work history
- Behavioral/Culture Fit (15%): autonomous/ship-focused/technical depth = strong; heavy process/compliance-first = friction
- Career Alignment (30%): advances toward LLM inference engineering depth at a strong company

Location: PASS if remote/hybrid/UK. FAIL if requires leaving UK or security clearance.
Strong Fit 75+: generate documents. Worth Reviewing 60-74: flag only. Below 60: skip.

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
- Company paragraph: reference something real and specific about this company (product, research, mission) — never generic
- Closing: one sentence on working style fit, I look forward to hearing from you
- Target 1 page

---

## PART E — UPDATE TRACKER AND COMMIT

1. For each 75+ job append row to tracker.csv: date=today, status=drafted, fit_score=number, cv_file and cover_letter_file paths, notes=brief fit reason, last_updated=today
2. Run:
   git config user.email ayenioluwatosinolawale@gmail.com
   git config user.name AyeniOluwatosinOlawale
   git add .
   git diff --cached --quiet || git commit -m "chore: daily job search $(date +%Y-%m-%d)"
   git push origin master 2>/dev/null || git push origin main 2>/dev/null || true

---

## PART F — SEND EMAIL SUMMARY

Use Gmail MCP. Send to: ayenioluwatosinolawale@gmail.com
Subject: Job Search Daily - [DATE]

Email body sections:

APPLICATION UPDATES
For each status change: [Company] - [Role] - [old status] -> [NEW STATUS] - brief detail
For follow-ups due: FOLLOW-UP DUE: [Company] - [Role] - Applied [date] - [N] days no response - [URL]
If no updates: No new responses found for open applications.

NEW STRONG FITS - UPLOAD AND APPLY
For each 75+: [Score]/100 | [Title] at [Company] | [Location]
Why strong fit: [2 sentences]
Apply here: [URL]
Files at github.com/AyeniOluwatosinOlawale/job-applications:
  cv/main_[slug].tex and cover_letters/cover_[slug].tex
ACTION: Download, compile (lualatex for CV, xelatex for cover letter), upload to portal
If none: No new strong fits today.

WORTH A LOOK (60-74)
For each: [Score]/100 | [Title] at [Company] | [one-line reason] | [URL]
If none: None today.

STATS
Jobs scanned: X | Strong fits prepared: X | Worth reviewing: X | Application updates: X | Follow-ups due: X

If no new jobs found: email with just application updates and note no new roles found in last 24h.
If search fails entirely: email reporting the failure clearly plus any application updates from Part A.
