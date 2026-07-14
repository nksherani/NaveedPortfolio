import os
from weasyprint import HTML

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
    @page {
        size: A4;
        margin: 12mm 15mm;
        background-color: #ffffff;
    }
    * {
        box-sizing: border-box;
    }
    body {
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        margin: 0;
        padding: 0;
        color: #2b2b2b;
        font-size: 9.5pt;
        line-height: 1.4;
    }
    .header {
        text-align: center;
        margin-bottom: 10px;
        padding-bottom: 10px;
        border-bottom: 1.5px solid #2c3e50;
    }
    .header h1 {
        margin: 0 0 4px 0;
        font-size: 20pt;
        color: #1a252f;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .header h2 {
        margin: 0 0 6px 0;
        font-size: 12pt;
        color: #34495e;
        font-weight: 500;
    }
    .contact-info {
        font-size: 8.5pt;
        color: #555555;
    }
    .contact-info span {
        margin: 0 4px;
    }
    h3.section-title {
        font-size: 11pt;
        color: #1a252f;
        text-transform: uppercase;
        border-bottom: 1px solid #bdc3c7;
        padding-bottom: 2px;
        margin-top: 10px;
        margin-bottom: 6px;
        page-break-after: avoid;
    }
    .summary {
        text-align: justify;
        margin-bottom: 10px;
    }
    .skills-list {
        margin: 0;
        padding-left: 18px;
        margin-bottom: 10px;
    }
    .skills-list li {
        margin-bottom: 2px;
    }
    .job, .project {
        margin-bottom: 8px;
        page-break-inside: avoid;
    }
    .job-header {
        width: 100%;
        display: table;
        margin-bottom: 2px;
    }
    .job-title-company {
        display: table-cell;
        font-weight: 600;
        font-size: 10pt;
        color: #2c3e50;
    }
    .job-date-location {
        display: table-cell;
        text-align: right;
        font-style: italic;
        font-size: 8.5pt;
        color: #7f8c8d;
    }
    .job ul, .project ul {
        margin-top: 2px;
        margin-bottom: 0;
        padding-left: 18px;
    }
    .job ul li, .project ul li {
        margin-bottom: 2px;
        text-align: justify;
    }
    .project-title {
        font-weight: 600;
        color: #2c3e50;
        font-size: 10pt;
    }
    .project-intro {
        font-style: italic;
        margin-bottom: 4px;
        color: #444;
        text-align: justify;
    }
</style>
</head>
<body>

<div class="header">
    <h1>Naveed Ahmed</h1>
    <h2>Principal Software Engineer | AI Solution Architect</h2>
    <div class="contact-info">
        <span>+92 332 3919193</span> |
        <span>nksherani@outlook.com</span> |
        <span>linkedin.com/in/naveed-ahmed-96b45552</span> |
        <span>Karachi, Sindh, Pakistan</span>
    </div>
</div>

<h3 class="section-title">Professional Summary</h3>
<div class="summary">
    Principal Software Engineer and AI Solution Architect with 9+ years of experience in software architecture, including 7 years of deep expertise in Microsoft Azure cloud services and 1.5 years of specialized, hands-on experience in AI and MLOps. Proven ability to translate complex business problems into practical AI solutions, leading end-to-end delivery from data preparation and feature engineering to model training, deployment, and production monitoring. Deeply experienced in Generative AI, Agentic AI, RAG, and LLMs (including Local LLMs). Highly proficient in creating RFP responses, technical roadmaps, and engaging with technical and executive stakeholders to drive AI adoption across diverse domains.
</div>

<h3 class="section-title">Skills</h3>
<ul class="skills-list">
    <li><strong>AI & Machine Learning (1.5+ years):</strong> Generative AI, Agentic AI, Local LLMs, RAG, Prompt Engineering, Embeddings, Vector Search, Feature Engineering, Model Evaluation, Tool Calling, Guardrails, Anomaly/Fraud Detection.</li>
    <li><strong>Cloud & Enterprise Architecture (7+ years):</strong> Microsoft Azure, Azure AI Foundry, Azure AI Search, Azure OpenAI, Document Intelligence, Cosmos DB, Microservices, Data Pipelines, API Management, End-to-End System Design.</li>
    <li><strong>MLOps & LLMOps (1.5+ years):</strong> Azure Machine Learning, AutoML, Deployment Automation, Production Monitoring, Model Context Protocol (MCP).</li>
    <li><strong>Programming & Development:</strong> Python, C#, .NET 6/8, Node.js, JavaScript, TypeScript, React.js, Next.js.</li>
    <li><strong>AI Development Tools:</strong> Cursor AI, GitHub Copilot, Claude, Antigravity, Google Flow.</li>
    <li><strong>Databases & Vector DBs:</strong> Pinecone, Qdrant, Azure AI Search, SQL Server, PostgreSQL, MongoDB, Redis, Snowflake.</li>
    <li><strong>APIs, Integration & CLI:</strong> Meta Graph API, X API, Google YouTube API, LinkedIn API, TikTok API, GitHub CLI, Firebase CLI, Azure CLI, AWS CLI.</li>
</ul>

<h3 class="section-title">Independent AI & Automation Products (Personal Projects)</h3>
<div class="project-intro">
    Architected and built three distinct applications from scratch. Conducted comprehensive market research, gap analysis, and competition analysis using AI tools to define product features and create full project roadmaps. Extensively utilized Claude, Cursor, Antigravity, and Google Flow to accelerate development and generate Agentic AI workflows. Streamlined CI/CD and infrastructure using GitHub CLI, Firebase CLI, Azure CLI, and AWS CLI.
</div>
<div class="project">
    <div class="project-title">Agency Platform (AI-Operated Social Media Management)</div>
    <ul>
        <li>Engineered a self-hosted, multi-tenant platform enabling agencies to manage social presence, content, and messaging across multiple clients.</li>
        <li>Integrated AI agents powered by LangGraph for Content, Engagement, Strategy, and Optimization tasks, complete with a brand-safety guardrails layer.</li>
        <li>Automated workflows by integrating major platforms via their native APIs, including the Meta Graph API, X API, Google YouTube API, LinkedIn API, and TikTok API.</li>
        <li>Implemented multi-platform publishing and a unified inbox with AI-drafted replies and human-in-the-loop approvals for ad spend.</li>
    </ul>
</div>
<div class="project">
    <div class="project-title">Together — Relationship Check-In (Health & Wellness App)</div>
    <ul>
        <li>Developed a calm, ad-free couples wellness app centered around weekly check-ins, private reflection, and appreciation exchanges.</li>
        <li>Built a structured repair kit with Guided Solo reflection, Async Together, and a real-time Conflict Copilot to de-escalate difficult moments.</li>
        <li>Designed with strict privacy-by-design architecture, ensuring sensitive responses are strictly user-scoped and encrypted via Google Firebase.</li>
    </ul>
</div>
<div class="project">
    <div class="project-title">Alice's Adventures Learner (Children's Education App)</div>
    <ul>
        <li>Created an immersive, offline-first literacy application for children ages 5–10, blending vocabulary, phonics, and creative play.</li>
        <li>Built interactive text-to-speech read-aloud modes, spaced-repetition flashcards, and six phonics mini-games.</li>
        <li>Ensured strict COPPA and GDPR-Kids compliance with no third-party child-tracking SDKs and a gated dashboard for parents.</li>
    </ul>
</div>

<h3 class="section-title">Work Experience</h3>
<div class="job">
    <div class="job-header">
        <div class="job-title-company">Principal Software Engineer | 10Pearls Pakistan</div>
        <div class="job-date-location">Jan 2025 - Present | Karachi, PK</div>
    </div>
    <ul>
        <li>Lead technical architecture and engineering strategy for enterprise AI and cloud projects across international clients.</li>
        <li>Architect enterprise RAG platforms, Agentic AI workflows, and conversational AI systems using Azure AI Search, Azure AI Foundry, Pinecone, and OpenAI APIs.</li>
        <li>Own end-to-end ML solutions by translating complex domain requirements into technical architectures, overseeing data sources, data pipelines, and production deployment.</li>
        <li>Build automated MLOps and LLMOps pipelines in the Azure ML workspace, managing the lifecycle from preprocessing triggers through to managed endpoint deployment.</li>
        <li>Drive data science initiatives by producing data quality reports, refining feature engineering, and utilizing Azure AutoML.</li>
    </ul>
</div>

<div class="job">
    <div class="job-header">
        <div class="job-title-company">Technical Lead | Turing.com (Contract)</div>
        <div class="job-date-location">Jul 2022 - Jan 2025 | Remote, US</div>
    </div>
    <ul>
        <li>Led the enterprise solution architecture for migrating a legacy monolith to a microservices-based SaaS platform.</li>
        <li>Designed application, integration, and infrastructure layers utilizing Azure cloud services, APIs, and Kubernetes orchestration.</li>
    </ul>
</div>

<div class="job">
    <div class="job-header">
        <div class="job-title-company">Senior Software Engineer | VentureDive</div>
        <div class="job-date-location">Sep 2020 - Apr 2022 | Remote</div>
    </div>
    <ul>
        <li>Delivered enterprise software utilizing .NET, Node.js, PostgreSQL, and event-driven architectures.</li>
        <li>Architected robust data pipelines and integrations with Kafka, Azure Service Bus, and AWS EventBridge.</li>
    </ul>
</div>

<div class="job">
    <div class="job-header">
        <div class="job-title-company">Senior Software Engineer | Stingray Technologies (Pvt) Ltd</div>
        <div class="job-date-location">Oct 2017 - Aug 2020 | Karachi, PK</div>
    </div>
    <ul>
        <li>Led technical teams in building distributed, CPU-intensive systems and APIs using C#, SQL, and MongoDB.</li>
    </ul>
</div>

<div class="job">
    <div class="job-header">
        <div class="job-title-company">Software Engineer | Techlogix</div>
        <div class="job-date-location">Dec 2016 - Oct 2017 | Karachi, PK</div>
    </div>
    <ul>
        <li>Developed highly scalable enterprise solutions for local and international clients, utilizing .NET Web API and SQL Server.</li>
    </ul>
</div>

<h3 class="section-title">Enterprise Projects</h3>
<div class="project">
    <ul>
        <li><strong>Tax Labs ML Solutions:</strong> Delivered end-to-end ML pipelines, including synthetic data generation, NLP anonymization (Azure Language NER, Document Intelligence), and automated Azure ML endpoint deployment.</li>
        <li><strong>International Audit Firm RAG Application:</strong> Designed an enterprise vector search solution (Azure AI Search, Pinecone, OpenAI) achieving 5x faster retrieval performance.</li>
        <li><strong>Conversational Database Interface:</strong> Developed Agentic workflows using the Model Context Protocol (MCP) to translate natural language into business insights.</li>
    </ul>
</div>

<h3 class="section-title">Education</h3>
<div class="job">
    <div class="job-header">
        <div class="job-title-company">Bachelor of Engineering (Computer Engineering)</div>
        <div class="job-date-location">2013 - 2016</div>
    </div>
    <div>NED University of Engineering and Technology | CGPA: 3.86/4.00</div>
</div>

</body>
</html>
"""

out_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(out_dir, "Naveed_Ahmed_AI_Solution_Architect_CV_B.html")
pdf_path = os.path.join(out_dir, "Naveed_Ahmed_AI_Solution_Architect_CV_B.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

HTML(filename=html_path).write_pdf(pdf_path)

print(pdf_path)