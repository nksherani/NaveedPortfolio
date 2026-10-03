# Naveed Ahmed
**Senior AI Engineer | Backend & Production AI Systems**

📍 Karachi, Pakistan &nbsp;|&nbsp; 📞 +92 332 3919193 &nbsp;|&nbsp; ✉️ nksherani@outlook.com
🔗 [linkedin.com/in/naveed-ahmed-96b45552](https://linkedin.com/in/naveed-ahmed-96b45552) &nbsp;|&nbsp; 🌐 [naveed-portfolio-rho.vercel.app](https://naveed-portfolio-rho.vercel.app/)

---

## Professional Summary

Senior AI Engineer and Backend Architect with 9+ years of hands-on software delivery and 1.5+ years of deep, production-focused AI and ML engineering. Primary backend engineering background is in **C# / .NET** — building distributed, event-driven, and cloud-native SaaS systems at scale — with Python applied specifically across all AI/ML, data pipeline, and scripting work. Proven track record of owning AI products end-to-end: from data ingestion and embedding strategies through to managed inference endpoints, real-time monitoring, and CI/CD automation. Hands-on experience across both **AWS** (Lambda, SQS, SNS, S3, API Gateway, CloudWatch, EventBridge) and **Azure** (Azure OpenAI, Azure ML Workspace, AKS, Azure AI Foundry), with strong grounding in Kubernetes, event-driven architectures, and MLOps.

---

## Core Technical Skills

### AI & LLM Engineering
- **Agentic AI Frameworks:** OpenAI Agents SDK, Zapier, n8n (multi-agent systems with cooperative Content, Engagement, Strategy & Optimization agents); brand-safety guardrail layers; human-in-the-loop approval workflows; LangGraph & AutoGen (quick MVPs and experimentation)
- **RAG Systems:** End-to-end RAG pipeline design — chunking strategies, context-preserving overlap, OpenAI embedding models, Pinecone vector DB, custom re-ranking and precise citation/clause mapping
- **LLMs & Orchestration:** GPT-4, Gemini, GLM; Azure OpenAI; structured prompt engineering, tool calling, binary cascade and majority-voting workflows
- **Production AI Monitoring:** MLOps pipeline automation, confidence scoring, hallucination mitigation via consensus workflows, model performance evaluation
- **OCR & Document Pipelines:** Azure Document Intelligence / Form Recognizer; custom PII redaction and NLP preprocessing pipelines

### Backend Engineering
- **C# / .NET (Primary):** .NET 6/8 Web API, Domain-Driven Design (DDD) domain services, Hangfire background jobs, shared middlewares, REST API design — primary production language across 7+ years
- **Python (AI/ML & Pipelines):** FastAPI service wrappers, data pipeline scripting, ML experimentation, and AI integration work; used across all AI/ML and data engineering projects
- **Node.js:** API services and integrations across multiple client projects
- **Data Stores:** PostgreSQL, Azure SQL, Cosmos DB, Redis, MongoDB, Pinecone
- **AI Development Tools:** GitHub Copilot, Cursor, Claude, Antigravity

### Cloud & AWS
- **AWS (Hands-on):** Lambda, SQS, SNS, S3, API Gateway, CloudWatch, EventBridge, AWS CLI
- **Azure (Deep):** Azure OpenAI, Azure AI Foundry (≈ Bedrock), Azure ML Workspace (≈ SageMaker), Azure Blob Storage, Azure Service Bus, Azure API Management, Azure Kubernetes Service (AKS), Azure Document Intelligence, Azure NER
- **Kubernetes & Containers:** AKS — 7+ years; Docker; microservices orchestration at scale
- **CI/CD & IaC:** Azure DevOps, Azure CLI, AWS CLI, Firebase CLI, GitHub CLI; Bicep (Azure IaC)
- **Event-Driven Architecture:** Apache Kafka, AWS SQS/SNS, AWS EventBridge, Azure Service Bus — high-throughput, real-time message integration

### MLOps & Data Science
- **ML Lifecycle:** Azure ML Workspace — automated training triggers, hyperparameter tuning, AutoML champion selection, managed production endpoint deployment
- **Algorithms:** XGBoost, SVC, Linear Regression, BERT fine-tuning (custom loss functions & hyperparameters), NLP feature engineering
- **Data Engineering:** Text embeddings, normalization, synthetic data generation, LLM-assisted dataset cleansing and denoising

---

## Work Experience

### Principal Software Engineer (AI Focus)
**10Pearls Pakistan** &nbsp;|&nbsp; Karachi, PK (International Clients) &nbsp;|&nbsp; *January 2025 – Present*

- Lead AI engineer for enterprise AI products across international clients, owning architecture and end-to-end delivery.
- Architected and delivered production RAG platforms using **Azure AI Search**, Pinecone, and OpenAI embeddings with custom citation-mapping engines for precise page/clause attribution for audit teams.
- Built and deployed **multi-agent AI systems** (Content, Engagement, Strategy, Optimization agents) using OpenAI Agents SDK with brand-safety guardrail layers and configurable human-in-the-loop approval workflows.
- Leveraged **Azure OpenAI** and **Azure AI Foundry** for managed LLM access, model deployment, and AI service orchestration across client projects.
- Owned the full **MLOps lifecycle** in Azure ML Workspace: automated ingestion from blob storage → preprocessing → model training with AutoML → production inference endpoint deployment.
- Engineered agentic **MCP (Model Context Protocol)** workflows connecting LLMs to live SQL/NoSQL databases for natural-language business intelligence queries.
- Designed and delivered a custom **OCR/NLP anonymization pipeline** using Azure Document Intelligence and Azure NER — integrated directly into upstream ML training workflows.
- Produced architecture diagrams, RFP responses, and technical roadmaps for C-level and technical stakeholder audiences.

---

### Technical Lead
**Turing.com (Contract)** &nbsp;|&nbsp; Remote, US &nbsp;|&nbsp; *July 2022 – January 2025*

- Owned end-to-end solution design and delivery for a US healthcare facility-management SaaS platform — greenfield architecture, DB design, and engineering team leadership.
- Built cloud-native backend on Azure with **AKS (Kubernetes)**, App Service, Azure SQL, and Azure AD SSO.
- Introduced Hangfire for reliable async background processing across scheduling, payroll, and HR workflows.
- Implemented DDD domain services with bounded contexts, structured logging middlewares, and global exception handling for production-grade reliability.

---

### Senior Software Engineer
**VentureDive (Contractor)** &nbsp;|&nbsp; Remote &nbsp;|&nbsp; *September 2020 – April 2022*

- Delivered production backend services across multiple clients (Daraz, Motiv, PayActiv) spanning ecommerce, payment gateways, and financial software.
- Built event-driven data pipelines and integrations using **Apache Kafka**, **Azure Service Bus**, and **AWS EventBridge** — high-throughput, real-time processing.
- Stack: .NET, Node.js, PostgreSQL; performance optimisation and technical auditing across client platforms.

---

### Senior Software Engineer
**Stingray Technologies (Pvt) Ltd** &nbsp;|&nbsp; Karachi, PK &nbsp;|&nbsp; *October 2017 – August 2020*

- Owned core platform development for real-time, distributed defence equipment systems with strict performance constraints on high-throughput message delivery.
- Built and maintained simulators for system validation; delivered in C#, SQL, and MongoDB.

---

### Software Engineer
**Techlogix** &nbsp;|&nbsp; Karachi, PK &nbsp;|&nbsp; *December 2016 – October 2017*

- Developed highly scalable enterprise solutions for local and international clients using .NET Web API and SQL Server.

---

## Key AI & Production Projects

### 1. Enterprise Document Q&A & Citation Engine (RAG)
*Python · FastAPI · Pinecone · OpenAI Embeddings*

- Production RAG system for UK audit teams: ingests large financial documents, performs semantic retrieval via **Pinecone vector DB**, and returns LLM answers with precise page/clause citations — a hard compliance requirement.
- Engineered specialized document chunking and overlap strategies to prevent context fragmentation during retrieval.
- Diagnosed and resolved timeout and memory bottlenecks in the legacy system, enabling it to handle enterprise-scale document volumes reliably in production.

---

### 2. Tax Transaction Categorization Engine (MLOps · Production AI)
*Python · Azure ML Workspace · AutoML · Azure Blob Storage · FastAPI*

- End-to-end production AI system classifying financial transactions into 76 DPL categories and 6 Capital Allowances pools for UK audit compliance — **80% accuracy** achieved on AI-cleansed dataset.
- Fully automated MLOps pipeline: Blob ingestion → preprocessing → AutoML training & hyperparameter tuning → managed production inference endpoint deployment.
- Evaluated XGBoost, SVC, Linear Regression, and fine-tuned BERT; implemented a hybrid majority-voting LLM pipeline for high-variability transaction types.

---

### 3. Agency Platform — Multi-Agent AI SaaS
*Python · OpenAI Agents SDK · Zapier · n8n · PostgreSQL · Docker · Gemini/OpenAI/GLM APIs*

- Self-hosted multi-tenant SaaS with **AI agents** (Content, Engagement, Strategy, Optimization) built on OpenAI Agents SDK, Zapier, and n8n automating social media management for multiple agency clients.
- Implemented brand-safety guardrail layers and configurable human-in-the-loop approval gates for ad spend and sensitive content.
- Integrated Meta Graph API, X API, YouTube API, LinkedIn API, TikTok API, Google Ads API, and email marketing APIs.

---

### 4. Conversational Database Interface (Agentic AI · MCP)
*Python · MCP · LLMs · React*

- Agentic AI system enabling non-technical users to query complex SQL/NoSQL databases in natural language, returning structured insights with step-by-step query reasoning.
- Engineered custom **MCP (Model Context Protocol)** server workflows bridging LLMs with live database connections and schema-context mapping.

---

### 5. Custom Document Anonymization Pipeline (OCR · NLP)
*Python · FastAPI · Azure Document Intelligence · Azure NER*

- Custom PII redaction pipeline using Azure Document Intelligence and Azure Named Entity Recognition to sanitize financial audit documents before AI ingestion.
- Developed rule-based and ML-based redaction layers; integrated directly into upstream ML training pipelines.

---

## Education

**Bachelor of Engineering — Computer Engineering**
NED University of Engineering and Technology &nbsp;|&nbsp; 2013 – 2016 &nbsp;|&nbsp; **CGPA: 3.86 / 4.00**

