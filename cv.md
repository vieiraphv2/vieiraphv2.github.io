# Paulo Vieira Silva

**DevOps & Platform Engineer | IT Operations**
Vila Velha, Espírito Santo, Brazil · Remote, US hours · he/him
Email: paulo_sng@hotmail.com · LinkedIn: https://www.linkedin.com/in/paulo-vieira-phv/ · GitHub: https://github.com/vieiraphv2 · Web: https://vieiraphv2.github.io/

> Paulo Vieira Silva is a DevOps & Platform Engineer running Google Cloud, the data platform and internal products at Smarter Sorting, and IT for Pareto AI on a consulting contract. $600k/year in cloud savings delivered; 1.4 TB migrated with zero downtime.

## Highlights

- **$600k /year**: Google Cloud savings identified and delivered across BigQuery, GKE, Cloud SQL and vendor contracts.
- **1.4 TB**: Company-wide warehouse migration: 33 databases and every customer-facing Tableau report, zero downtime, sole engineer.
- **65k tickets**: In-house support platform built and live in 13 days; 65,003 tickets and 145,464 messages migrated before the Salesforce sunset.
- **50%**: Production Kubernetes bill halved, $9,483 to $4,745 a month, with nodes drained one at a time. Zero incidents.

## About

DevOps and platform engineer with 10+ years in IT.

My strength is finding out what is actually happening and working the solution, regardless of area, tool, complexity or size of the task.

That range comes from a career spanning the full width of technology operations, from network operations for global mining and ERP support to identity, security, cloud infrastructure, data platforms and internal product engineering.

The last twelve months, in numbers:
- Over $600k/year in cloud savings identified and delivered, using AI to build internal tools, systems and processes.
- Snowflake to BigQuery migration: 1.4 TB across 33 databases with no service interruption and ~35% lower compute cost; 30+ Tableau reports with 4,000+ Snowflake-specific SQL queries migrated.
- Salesforce Cases replaced by a support platform built in 13 days, now carrying 65,003 migrated tickets.
- Production Kubernetes bill cut by two-thirds, with zero incidents.

What the numbers do not show: I document what I build, teach the tools to whoever needs them, and leave every system easier to run than I found it. The growth of the team around me is part of the deliverable.

## Selected work

### GKE Cost Reduction — https://vieiraphv2.github.io/gke-cost-reduction/
Both Kubernetes clusters at Smarter Sorting, July to October 2026. Measure first, right-size reservations, retire what nothing calls, drain nodes one at a time, then a one-year committed-use agreement to close. $19,574/month starting point; ~$160k/year saved without a minute of downtime.
- 38 dead services shut down, each with the owner's sign-off and a documented way back
- 18 production machines down to 9, drained one at a time
- Staging on preemptible Spot capacity plus AMD: ~$83k/year

### Smarter Desk — https://support.smartersorting.com/
The support platform that replaced Salesforce Cases and support.smartersorting.com: scoped, built and live in 13 days, eight days before the Salesforce shutdown. Email-to-ticket intake over the Gmail API, public help center, knowledge base, assignment, RBAC, rich replies, attachments, live chat and CSAT. 65,003 tickets, 145,464 messages and 100 articles migrated from BigQuery snapshots.
- Priorities set from live usage data: 66% of inbound mail carries attachments, 4 agents own 88% of cases
- Three Cloud Run services and Cloud SQL, every deploy through Terraform

### Snowflake to BigQuery migration
Company-wide warehouse move by one engineer, July 2025 to the April 1, 2026 cutover: 1.4 TB, 33 databases, 451 workbooks inventoried, every customer-facing Tableau report. No service interruption, ~35% lower compute cost, and years of silently wrong data traced to the legacy ingestion pipeline and fixed (~2,000 ghost records).
- Tableau Migration Center: schema browser over 5,445 tables and 131K columns, SQL translator with 30+ conversions, one-click workbook converter (a Costco executive dashboard in ~15 minutes)
- Whole-database export procedure that cut a migration to three clicks
- Chrome extension so users could rescue their SQL worksheets before the shutdown
- Selected by leadership as the company's AI showcase and presented company-wide

### FileShare
Multi-tenant file portal built in two days after a national retailer refused SFTP, Dropbox and Drive custody. Serverless on Cloud Run with a public REST API: uploads up to 5 GB per file and 10,000 files per batch, hashed bearer tokens, SSRF protection, audit log, evergreen revocable URLs under the company domain.
- Adopted in production the week it shipped: 10,000 API calls in a single client run, and ~150 customer shipping documents hosted for a Costco deliverable
- 800+ documents served to a retailer under stable URLs; a bridge mode re-hosts third-party safety data sheets

### Tibbis — https://tibbis.com.br
Co-founder and CTO of a Brazilian marketplace for hiring local freelancers: PIX payment released when the job closes, identity verification with document OCR and face matching, real-time chat, disputes and ratings. Next.js, Supabase and Cloud Run, in production on Vercel.


## Experience

### DevOps Engineer · Smarter Sorting
*Jul 2025 – Present · Full-time · Boulder, Colorado, US · Remote*

Own cloud infrastructure, the data platform and internal products at a compliance-AI SaaS company, as its only platform engineer.

- Led the company-wide Snowflake to BigQuery migration as its only engineer, coordinating the cutover with every data-owning team: 1.4 TB across 33 databases and 30+ customer-facing Tableau reports (4,000+ Snowflake-specific SQL queries), zero downtime, ~35% lower compute cost. Traced years of silently wrong data to the legacy ingestion pipeline and fixed it.
- Built the tooling that made the migration possible: a schema-aware Snowflake-to-BigQuery SQL translator, a one-click Tableau workbook converter and a schema browser covering 5,400+ tables.
- Built the in-house support platform that replaced Salesforce Cases in 13 days: email-to-ticket intake, public help center, knowledge base, RBAC and attachments. 65,003 tickets and 145,464 messages migrated, live before the Salesforce sunset.
- Led the Google Cloud cost program, identifying and delivering over $600k/year in savings. Diagnosed a BigQuery misconfiguration costing ~$38,000/month and validated the fix against the billing export (98.4% reduction).
- Cut both GKE clusters from $19,574/month: right-sized dozens of services, retired 38 dead services with owner sign-off, drained 9 of 18 production nodes one at a time, moved staging to Spot capacity on AMD and closed with a one-year committed-use agreement, all without downtime or incidents. Production bill down two-thirds; ~$160k/year saved.
- Replaced third-party data replication with in-house pipelines: a Python ETL on Cloud Run syncing 196 Salesforce objects daily, Stripe API ingestion into BigQuery, and Datastream change data capture across four environments.
- Shipped a multi-tenant file-sharing portal with a public REST API (built in two days after a retailer refused SFTP, Dropbox and Drive) and a service granting read-only database access without distributing credentials.
- Root-caused months of failed production restore tests to 5.5 TB of WAL held by two dead replication slots, completed the first successful restore (407 GB) and launched point-in-time recovery, automated restore tests and WAL alerts on every production instance.
- Replaced the manual biweekly security log review with a Cloud Run job that analyzes Cloud Armor, firewall, database and Auth0 logs and files its own Jira tickets.
- Resolved production data incidents for enterprise retail customers: restored a business-critical reporting dashboard within 5 hours; corrected hazardous-materials data feeding a national retailer's logistics system.
- Wrote the company standard for programmatic AI access, replacing static API keys with Workload Identity Federation. Added automated AI review of failed CI builds.

Keywords: Google Cloud Platform, BigQuery, Snowflake, SQL, GKE, Kubernetes, Terraform, Cloud Run, Cloud SQL, Datastream, Python, TypeScript, Tableau, FinOps, Workload Identity Federation, CI/CD, Disaster recovery, Incident response, AI agents

### IT Consultant · Pareto AI
*Apr 2026 – Present · Contract · Remote*

Consulting contract alongside Smarter Sorting: building the IT function for a 150+ person AI company, from identity and device management to SOC 2 readiness.

- Led company-wide MFA enforcement across Google Workspace for 1,000+ accounts (external experts, employees and contractors), rolled out in three phased waves to limit disruption.
- Built a self-service /mfa-unblock Slack tool that delivers Google backup codes to users' recovery emails, cutting Support and Trust workload while keeping identity verification intact.
- Drove SOC 2 audit readiness: controls-tracking workbook and mapping of technical controls to audit criteria with Engineering; advised on FedRAMP and data-residency impact of Slack infrastructure changes.
- Own provisioning and deprovisioning across Google Workspace, Slack, Zendesk and other systems for employees, contractors and hybrid workers; automated the Ashby to IT ticket to Slack pipeline for new hires and offboarding tickets from Rippling terminations.
- Authoring and driving the MDM rollout to bring every company-issued device under central management; assessed data-security implications of contractor devices touching client platforms.
- Audited Slack licensing and surfaced ~100 idle paid seats; defined the guest model for hybrid workers and compiled the company-wide vendor inventory the procurement team was missing.

Keywords: Google Workspace, GAM, Slack, Rippling, Ashby, Zendesk, Bitwarden, SOC 2, MFA, MDM, Identity lifecycle, Automation, AI agents, Vendor management

### IT Operations Specialist · Smarter Sorting
*Jan 2024 – Jan 2025 · Full-time · Boulder, Colorado, US · Remote*

Built and ran the company's IT function as its only IT engineer.

- Ran frontline support and the full identity lifecycle for 100+ users across 30+ systems.
- Administered Okta SSO, Google Workspace, Jira Service Management and the device fleet on Jamf and SentinelOne. Integrated Okta with the HR platform and the company password manager, ending manual account provisioning.
- Defined the service-desk model and automated it in Jira: response and resolution targets by request type, escalation paths, ticket creation from Slack, and onboarding/offboarding workflows that record proof of account deactivation for audit.
- Supported the company's first SOC 2 Type 2 certification.
- Owned repository security and organization-wide Google Cloud IAM governance: enforced merge-blocking rules for unresolved security alerts across 16 repositories in two days; migrated 32 individual access grants to a group-based model.
- Replaced Finance's manual month-end reporting with a Stripe API integration, which also surfaced 1,496 records the manual process had been omitting.

Keywords: Okta, Google Workspace, Jamf, SentinelOne, Jira Service Management, SOC 2, IAM, Stripe API, Identity lifecycle, Retool, Proofpoint, GitHub, Automation

### PL/SQL Analyst · GB Agritech
*Mar 2025 – Oct 2025 · Contract · Vitória, Espírito Santo, Brazil · Hybrid*

Support for an ERP built on Oracle Forms.

- Requirements analysis and L3 support for escalated incidents.
- Analysis of Oracle database functions and routines in PL/SQL.
- Improved support processes; maintained agile workflows in Azure DevOps.

Keywords: PL/SQL, Oracle Forms, Azure DevOps, L3 support, Requirements analysis, Incident response, ITSM

### Senior IT Engineer · TheGuarantors
*Apr 2025 – Jul 2025 · Full-time · New York City, US · Remote*

Led the IT team.

- Owned user lifecycle, access control, automation and process documentation, building on the existing tooling rather than adding new platforms.
- Worked with Security, HR and Infrastructure to tighten security protocols and unblock critical operational issues.
- Optimized Okta, Jira, Google Workspace, Slack and Rippling; built API integrations in JavaScript, Bash and Python.

Keywords: Okta, Rippling, Google Workspace, JavaScript, Bash, Python, Team leadership, Jira, Slack, REST APIs

### Internal IT Support · Trustly
*Apr 2022 – Jan 2024 · Full-time · Vitória, Espírito Santo, Brazil · On-site*

- Bilingual (Portuguese/English) technical support for users across every US time zone.
- Managed user requests, asset management, onboarding/offboarding and internal IT process improvements.
- Built automation for IT tasks that cut response times.
- Led improvements in inventory control, vendor relations and security policy rollout.

Keywords: IT Service Management, Asset management, User lifecycle, Onboarding, Offboarding, Okta, Google Workspace, GAM, Jamf, MDM, Apple devices, Jira, Automation, Security, Vendor management

### Software Support Analyst · Quality WebPosto
*Mar 2021 – Apr 2022 · Full-time · Vila Velha, Espírito Santo, Brazil · Hybrid*

- Ran incident response and turned requests into use cases for the development team.
- Administered PostgreSQL databases.
- Led the support team and trained new hires and interns.

Keywords: PostgreSQL, Incident management, Team leadership, ERP, Training & mentoring

### NOC Analyst · Algar Tech
*Apr 2020 – Feb 2021 · Full-time · Vitória, Espírito Santo, Brazil · Remote*

- Bilingual network analyst for VALE S/A, supporting operations in 27 countries.
- Mesh, LTE and radio networks, BGP, MPLS, DMVPN, Cisco, CA Spectrum, BMC Remedy.

Keywords: Networks, BGP, MPLS, DMVPN, Cisco, CA Spectrum, BMC Remedy, NOC, ITIL, Incident management

### Software Support Analyst · Prosystem
*Oct 2017 – Apr 2020 · Full-time · Vitória, Espírito Santo, Brazil · Hybrid*

- ERP support, incident management and customer service.
- Improvement requests and incident analysis for the development team.
- MySQL administration and Windows network support.

Keywords: MySQL, ERP, ITIL, Customer support, Windows networks, Incident management

### Service Desk Technician · Hsibrasil Soluções Corporativas em TI
*Sep 2015 – Oct 2017 · Full-time · Vila Velha, Espírito Santo, Brazil · On-site*

- Windows, networks, CCTV and IT operations support for corporate and individual clients.

Keywords: Windows, Networks, CCTV, Service desk, ITIL

### Head of Operations · Ronicar Tecnologia Automotiva
*Dec 2012 – May 2015 · Full-time · Vila Velha, Espírito Santo, Brazil*

- Service and team management, finance and budgeting, inventory, customer relations, IT.

Keywords: Operations, Team management, Budgeting, Customer relations

### IT Instructor · Prepara Cursos, Viaensino, Microcamp Tecnologia
*May 2011 – Dec 2012 · Full-time · Vila Velha and Vitória, Espírito Santo, Brazil · On-site*

- Taught IT fundamentals, graphic design, Photoshop, and PC assembly and maintenance.

Keywords: Teaching, Photoshop, Hardware maintenance

### Technical Assistant · Automa Comércio e Serviços
*Dec 2010 – Jul 2011 · Full-time · Vila Velha, Espírito Santo, Brazil*

- Automatic gates, network printers, PC maintenance, CCTV, customer service.

Keywords: Field support, CCTV, Hardware maintenance

## What colleagues say (LinkedIn recommendations, verbatim)

> "Due to his strong commitment, sense of responsibility, great rapport with colleagues and ability to work well under pressure, Paulo demands little to no management. It was a pleasure working with Paulo, and I would definitely work with him again."
> — Gustavo Valente, CISSP, CISA, CFE, PMP, Global Information Security & Risk Leader, CISO (Managed Paulo directly, 2025-01)

> "His proactive approach to problem-solving set him apart. He consistently identified and addressed potential issues before they impacted operations. His easy-going nature and clear communication style made him effective with both technical and non-technical stakeholders."
> — Nicole Adams Kraus, Founder at BlueHouse, ex Chief Talent Officer (Senior to Paulo at SmarterX, 2025-01)

> "He was instrumental in the launch of our IT Ops program, streamlining our processes and enhancing our security posture. His ability to drive cross-functional collaboration significantly improved our overall efficiency. Paulo is a genuine and engaging colleague."
> — Jenelle Tortorella Kelly, Revenue & Customer Success Leader (Senior to Paulo at SmarterX, 2025-01)

> "With Paulo there is no bad time, he is always delivering great results. Paulo is a person you can count on with eyes closed. He contributed a lot with my development."
> — Henrique Faria, IT Analyst, IAM & SSO (Worked with Paulo on the same team, 2025-02)

## Skills

- **Cloud and infrastructure:** Google Cloud Platform, Cloud Run, GKE / Kubernetes, Cloud SQL, IAM and Workload Identity Federation, Terraform, Helm, Docker, FinOps
- **Data:** BigQuery, Snowflake, PostgreSQL, Oracle PL/SQL, MySQL, Datastream (CDC), ETL pipelines, Tableau
- **Languages and scripting:** Python, SQL, Bash, JavaScript / TypeScript, PowerShell, REST APIs
- **CI/CD and observability:** CircleCI, GitHub Actions, Datadog, Cloud Logging
- **AI engineering:** Claude and coding agents, Vertex AI, Agentic workflow design, AI access governance (WIF over static keys)
- **Identity and security:** Okta, Auth0, Google Workspace, Jamf, SentinelOne, SOC 2, Incident response
- **Service management:** Jira Service Management, SLA design, Escalation processes, Technical documentation

## Education and credentials

- Coursework toward BSc Software Engineering, UNOPAR, Brazil (2021 – 2024)
- 3rd place, Google Cloud Data Analytics Mentor-Led Hackathon (Dec 2025, Google Cloud): Two-person team; built an automated per-customer cloud cost allocation engine in a three-week sprint with Google mentors.

## Languages

- Portuguese: Native
- English: Fluent, professional working proficiency
- Spanish: Basic

---
Canonical: https://vieiraphv2.github.io/ · JSON Resume: https://vieiraphv2.github.io/resume.json · Updated 2026-09-18
