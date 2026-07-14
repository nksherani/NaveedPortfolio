# Products & Projects

Detailed profiles of key products, outlining product specifications, target audience, pricing models, compliance standards, and technical engineering contributions.

---

## 1. Tax Transaction Categorization Engine
**Tagline:** Automated Capital Allowances and Detailed Profit & Loss classification for enterprise auditing
**Category:** FinTech / Tax Compliance & Auditing
**Target Audience:** Global Audit & Advisory Firms (UK market)
**Platforms:** Enterprise Cloud (Azure)
**Tech Stack:** Python, .NET, Azure App Service, React, Azure SQL Database

### Product Overview & Highlights
An enterprise-grade classification engine built from scratch to automate complex corporate tax categorization workflows under UK tax legislation. The system processes auditing transactions to classify them for tax relief optimization with full explainability.
- **Detailed Profit & Loss (DPL) Classifier:** Automatically categorizes high-volume DPL transactions into 76 distinct accounting and tax categories.
- **Tangible Fixed Assets (TFA) Capital Allowances Classifier:** Classifies capital additions into appropriate Capital Allowances pools to calculate eligible tax reliefs.
- **Explainable Decisions:** Provides structured reasoning alongside confidence scores for every transaction categorization to facilitate human auditor review.
- **Anonymization Pipeline & Custom Tool:** Built a custom anonymization pipeline and standalone tool utilizing **Azure NER (Named Entity Recognition)** and **Azure Document Intelligence (DI)** to systematically identify, sanitize, and redact sensitive PII/audit data from raw documents.

### Methodology & AI/ML Implementations
- **Detailed Profit & Loss (DPL) Architecture:**
  - **Traditional ML & Fine-Tuning Experimentation:** Evaluated and experimented with multiple machine learning algorithms including **XGBoost**, **Linear Regression**, and **SVC (Support Vector Classifier)**, alongside the **fine-tuning of BERT models** using different loss functions and hyperparameters.
  - **Data Augmentation & Cleansing:** Utilized LLMs and AI tools to cleanse, denoise, and enrich a small, low-quality training and test dataset.
  - **Performance Benchmarks:** Achieved **80% accuracy** on classification using the refined, AI-cleansed dataset.
  - **NLP Preprocessing & Feature Engineering:** Developed pipelines for text embeddings, feature engineering, data normalization, acronym/short-form expansion, and custom noise reduction.
  - **Pipeline & MLOps:** Integrated model training and selection using Azure AutoML for final evaluations, deploying the champion model as a live production inference endpoint.
- **Tangible Fixed Assets (TFA) Architecture:**
  - Designed an LLM-based architecture to handle low-volume, high-variability TFA transaction descriptions.
  - **Prompt Engineering & Multi-Agent Strategies:**
    1. *Single Prompt Approach:* Contains detailed definitions and examples for all 6 target Capital Allowances categories.
    2. *Binary Classifier Prompts:* 6 distinct binary yes/no evaluation prompts.
    3. *Hybrid Consensus Flow:* Combines both methods—the single-prompt model returns top 3 predictions. If the confidence score exceeds 80%, the prediction is accepted. If below 80%, it triggers 3 individual yes/no LLM calls for the top 3 candidates. This process runs through a 3x majority voting iteration to yield a highly stable and verified confidence score.

### Engineering & Development Contributions (Brainchild Project)
- **End-to-End Ownership:** Conceived and proposed the project as a personal brainchild, taking full ownership of designing the overall architecture from scratch.
- **Tax Domain & Legislation Engineering:** Reviewed UK tax legislation to identify key regulations and created the 76 DPL categories and 6 TFA Capital Allowances pools.
- **Side Product Development:** Engineered a custom data anonymization pipeline and standalone tool leveraging **Azure NER** and **Azure Document Intelligence (DI)** to redact sensitive client details prior to pipeline ingestion.
- **Automated Data & MLOps Pipelines:** Created the complete Azure infrastructure utilizing **Azure ML Workspace** and automated the entire workflow:
  - Ingestion of transaction data into Azure Blob Storage.
  - Raw data preprocessing, normalization, and acronym resolution.
  - Automatic model training, hyperparameter tuning, and algorithm/model selection based on performance metrics.
  - Continuous integration and automated deployment of the final model to a production endpoint on Azure.

---

## 2. Enterprise Document Q&A & Citation Engine (RAG)
**Tagline:** Scalable Retrieval-Augmented Generation with custom document citation logic for audit compliance
**Category:** Enterprise AI / Knowledge Management & Auditing
**Target Audience:** Internal Auditors and Tax Advisory Teams (UK market)
**Platforms:** Enterprise Cloud (Azure)
**Tech Stack:** Python, React, Pinecone, OpenAI API

### Product Overview & Highlights
An enterprise-grade document intelligence and question-answering tool. The system allows auditors to upload large financial documents and ask complex questions, receiving context-aware answers back with precise citations.
- **Scalable Document Ingestion:** Resolved major system timeouts and processing bottlenecks in a legacy RAG application, allowing it to efficiently handle large audit documentation without timing out.
- **Accurate Source Citations:** Developed a custom citation mapping engine that links generated LLM answers back to exact pages, clauses, and reference text within the original document—a critical compliance capability not supported out of the box.
- **Vector Search & Embedding Framework:** Replaced inefficient in-memory search with **Pinecone Vector Database** and **OpenAI embedding models** to power highly accurate semantic search and retrieval.

### Engineering & Development Contributions
- **Legacy Diagnostics:** Conducted a comprehensive code review of the existing RAG tool to identify and isolate performance bottlenecks related to memory usage and API limits.
- **Architectural Redesign & Optimization:** Designed and implemented an alternative, scalable RAG architecture using Pinecone. Researched vector database best practices and engineered a specialized document chunking and overlap strategy to prevent context fragmentation and preserve semantic continuity during search retrieval.
- **Custom Citation Logic:** Designed, prototyped, and engineered the precise page/clause reference attribution algorithms to satisfy auditing requirements.

---

## 3. Agency Platform (Social Media Agency Automation SaaS)
**Tagline:** AI-operated social media management for agencies
**Category:** Business & Marketing SaaS
**Target Audience:** Agencies and operators managing multiple client accounts
**Platforms:** Web (self-hosted, Docker)
**Tech Stack:** Python, React, PostgreSQL
**Pricing:** Local-first, self-hosted licence (bring your own API keys)

### Product Overview & Highlights
A self-hosted, multi-tenant platform that lets an agency manage social presence, content, paid ads, and customer messaging for multiple clients from one interface. AI agents handle the repetitive work while humans keep control of anything brand-sensitive or involving ad spend.
- **Multi-Platform Publishing:** Connect Facebook, Instagram, X (Twitter), and more. Compose, schedule, and publish platform-specific posts, reels, stories, carousels, and threads from one calendar.
- **Unified Inbox:** Every DM, comment, and message request from all connected accounts in a single view, with AI-drafted replies and human approval where it matters.
- **AI Agents with Guardrails:** LangGraph-powered Content, Engagement, Strategy, and Optimization agents, with a brand-safety Guardrails layer and configurable autonomy per client.
- **Campaigns, Approvals & Reporting:** Campaign management with human-in-the-loop approval queues for ad spend, plus per-client analytics and automated reporting.

### Compliance & Privacy
- **Multi-Tenant Isolation:** Each client's data is fully separated.
- **Human-in-the-Loop:** Mandatory approval gates for ad spend and brand-sensitive content.
- **Data Protection:** GDPR controller/processor model for client and end-user data.
- **API Guidelines:** Operates on platform APIs under Meta, X, and other platform terms.

### Engineering & Development Contributions
- Market Research & Competitive Analysis
- Product Roadmap definition
- Converted Roadmap into features & user stories
- Created Architectural Diagram, DB Design, Sequence diagrams
- AI integration: Gemini API, OpenAI API, GLM API
- API integrations: Meta Graph API (fb + IG), X API, Google Youtube API, LinkedIn API, Tiktok API, Google Ad API, Email Marketing APIs
- Business Trends, Social Listening, Content generation Ideas
- Scheduling and automation of content generation & posting
- Complete implementation using AI tools
- Security Audit & compliance
- SaaS features: clients, teams, users, access roles etc.

---

## 4. Together — Relationship Check-In
**Tagline:** A calm, private rhythm for couples
**Category:** Health & Wellness
**Target Audience:** Couples, or solo users exploring before a partner joins
**Platforms:** Android, iOS (Currently in Closed Testing)
**Tech Stack:** React Native, JDK, Firebase, JavaScript, TypeScript
**Pricing:** Free tier · 21-day Pro trial · Pro $8.99/couple/month ($79.99/yr) · AI tier $14.99/couple/month (planned)

### Product Overview & Highlights
A calm, ad-free couples wellness app built around a weekly rhythm: short check-ins, private reflection, appreciation exchanges, connection bids, and structured repair tools after hard moments. Private by design — individual responses are never shared, only aggregated "pulse" data.
- **Weekly Check-In & Shared Pulse:** A 90-second weekly check-in surfaces how both partners feel. Individual answers stay private; only an aggregated connection pulse is shared when both partners complete it.
- **Structured Repair Kit:** Three guided modes — Solo reflection, Async Together, and a real-time Conflict Copilot — to de-escalate and reconnect after difficult moments.
- **Private Journal & Appreciation Bank:** Truly private journaling (never shared) plus weekly gratitude deposits that are revealed only when both partners participate.
- **Relationship Vitals & Life Seasons:** A private, non-gamified trends dashboard, with season-aware prompts that adapt to whether you are newlyweds, new parents, in a rough patch, and more.
- **AI-Driven Chat & Tone Tuner:** Real-time AI-powered chat helper that allows partners to rewrite and tune their messages to a specific selected tone (e.g., romantic, respectful, formal, empathetic) to encourage clear and positive relationship communication.

### Compliance & Privacy
- **Privacy-by-Design Data Model:** Sensitive responses are strictly UID-scoped.
- **Data Rights:** GDPR & CCPA/CPRA data rights (access, export, and deletion).
- **Control:** In-app account and data deletion controls.
- **Security:** Encrypted in transit and at rest via Google Firebase.

### Engineering & Development Contributions
- Market Research & Competitive Analysis
- Product Roadmap definition
- Converted Roadmap into features & user stories
- Feature exploration & innovative ideas
- AI integration: Implemented AI-driven chat and message tone tuning features (formal, respectful, romantic, empathetic, etc.)
- Firebase store, functions & email extensions
- Google Auth 2.0 integration

---

## 5. Alice's Adventures Learner
**Tagline:** Where reading becomes an adventure
**Category:** Children & Education
**Target Audience:** Children ages 5–10, parents, and primary-school teachers
**Platforms:** Android (Launched on Google Play Store), iOS (Planned)
**Tech Stack:** React Native, JDK, Firebase, JavaScript, TypeScript
**Pricing:** Free tier + one-time premium unlock (~$4.99). No ads, no subscriptions.

### Product Overview & Highlights
An immersive, offline-first literacy app for children ages 5–10 built around Lewis Carroll's *Alice's Adventures in Wonderland*. It blends vocabulary, phonics, and creative play so children experience learning as collecting magic words alongside Alice — guided gently by the White Rabbit.
- **Wonderland Vocabulary Flashcards:** Every age-appropriate word becomes a collectible card with whimsical art, text-to-speech audio, phonics breakdown, and a sentence from the book — mastered through gentle spaced repetition.
- **Interactive Read-Aloud Story Mode:** The full Alice story across 12 narrated chapters. Tap any word to hear it and open its flashcard, with "Read to Me" and "I'll Read" modes.
- **Six Playful Mini-Games:** Spell the Rabbit Hole, Tea-Party Letters, Sound Pool of Tears, and more — each reinforcing phonics, listening, and recall without ever feeling like a test.
- **Parent Zone & Creative Play:** A gated dashboard for parents, plus Paint the Rose drawing, colouring pages, and a calming Bedtime audiobook mode for the child.

### Compliance & Privacy
- **COPPA-Compliant:** No personal data from under-13s collected without verifiable parental consent.
- **GDPR-Kids:** No profiling, no third-party child-tracking SDKs.
- **Google Play "Designed for Families":** No ads in the child area.
- **Offline-first:** Progress stays on the device unless a parent opts into cloud sync.

---

## 6. Conversational Database Interface
**Tagline:** Agentic SQL/NoSQL interface translating natural language queries into business insights
**Category:** Enterprise AI / Conversational BI (Business Intelligence)
**Target Audience:** Corporate decision-makers and non-technical business users
**Platforms:** Model Context Protocol (MCP) / Python / LLMs
**Tech Stack:** Python, React

### Product Overview & Highlights
An Agentic AI application designed to democratize data access. The interface enables non-technical business users to query complex corporate databases (SQL/NoSQL) using natural language, returning structured data, visualizations, and business insights.
- **Model Context Protocol (MCP) Workflows:** Engineered custom agentic workflows utilizing Model Context Protocol (MCP) sidecars/servers to bridge LLMs with database connections.
- **Natural Language to Query Translation:** Implemented advanced prompt engineering and schema-context mapping to ensure reliable generation of complex database queries.
- **Explainable Data Retrieval:** Provides users with step-by-step query construction, reasoning, and context for the returned insights.

---

## 7. Healthcare Facility Management Platform
**Tagline:** Modernizing a legacy desktop facility-management system into APIs and mobile apps for scheduling, staffing, and HR
**Category:** Healthcare / Workforce & Facility Operations
**Target Audience:** Healthcare facilities, clinical operations, and HR/payroll teams (US market client)
**Platforms:** Microsoft Azure / Mobile (iOS & Android)
**Tech Stack:** .NET, C#, Azure, Azure SQL, Azure App Service, AKS

### Project Overview & Highlights
Modernization of an existing healthcare facility management desktop application. Core business logic was extracted and rebuilt as service APIs, with new capabilities spanning workforce scheduling, time cards, shift management, HR, payroll, and operational coordination—delivered through mobile apps alongside the web/API platform.
- **Desktop-to-API Modernization:** Converted established facility-management business rules from a legacy desktop application into secure, scalable APIs so clients and new apps could share one source of truth.
- **Scheduling, Shifts & Time Cards:** Extended the platform with scheduling workflows, shift assignment/management, and time-card capture to support day-to-day clinical and support staffing.
- **HR, Payroll & Coordination:** Added HR and payroll-aligned features plus coordination tooling so facility teams could manage staffing, approvals, and operational handoffs in one system.
- **Mobile Workforce Access:** Introduced mobile applications so staff and supervisors could manage shifts, time cards, and coordination on the floor—not only from the desktop.
- **Architecture & Delivery:** Evolved the rewritten services toward a modular, cloud-hosted microservices style on Azure (.NET / C#), deployed via App Service and AKS with Azure SQL, improving reliability and enabling iterative feature delivery.

---

## 8. Custom Document Anonymization Tool & Data Pipeline
**Tagline:** Custom NLP pipeline for PII sanitization and redaction in financial auditing documents
**Category:** Enterprise AI / Data Privacy & Compliance
**Target Audience:** Audit teams and compliance officers handling sensitive client records
**Platforms:** Azure (Language Service / Named Entity Recognition / Document Intelligence)
**Tech Stack:** Python, FastAPI

### Product Overview & Highlights
A custom-built data privacy tool and automated processing pipeline designed to sanitize and redact sensitive Personally Identifiable Information (PII) and corporate-sensitive details from audit documentation before ingestion into AI training workflows or external APIs.
- **Azure NER Integration:** Leveraged **Azure Named Entity Recognition (NER)** to automatically identify and classify entities such as names, organizations, locations, and monetary values.
- **Document Intelligence (DI) Extraction:** Integrated **Azure Document Intelligence** (formerly Form Recognizer) to extract text, tables, and structures from PDFs, scans, and spreadsheets, ensuring spatial coordinates are mapped for visual redaction.
- **Scalable Processing Pipeline:** Created an end-to-end processing pipeline that automatically ingests raw documentation, extracts text, performs entity masking/anonymization, and saves sanitized records to secure cloud storage.

### Engineering & Development Contributions
- **Tool Creation from Scratch:** Designed and implemented the custom anonymization utility as a standalone library and API service.
- **Redaction Logic:** Developed rule-based and machine-learning-based redaction layers to resolve acronyms, custom enterprise identifiers, and context-specific sensitive terms.
- **Integration:** Integrated the anonymization pipeline directly into the upstream data collection and ML training pipelines of the firm's auditing solutions.
