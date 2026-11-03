# Paulo Vieira Silva

**DevOps & Platform Engineer | IT Operations**
Vila Velha, Espírito Santo, Brazil · Remote, US hours · he/him
Email: paulo_sng@hotmail.com · LinkedIn: https://www.linkedin.com/in/paulo-vieira-phv/ · GitHub: https://github.com/vieiraphv2 · Web: https://vieiraphv2.github.io/

> Paulo Vieira Silva is a DevOps & Platform Engineer running Google Cloud, the data platform and internal products at Smarter Sorting. $600k/year in cloud savings delivered; 1.4 TB migrated with zero downtime.

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

### Search Platform
A self-managed Elasticsearch cluster on GKE, built to replace about $240k/year of managed Elastic Cloud spend at a projected $20k/year. Terraform builds it, Okta signs users in, Cloud Armor fronts it, and daily and hourly snapshots and alerting protect it, in its own GCP project. It holds 1.3 TB replicated from the four live Elastic Cloud deployments. Validated against the paid service in the data owners' tests; no production application has switched yet.
- 99,952 real requests replayed with zero errors, and 1,055 real queries replayed against both clusters: keyword results identical, and the top vector hit matched in 90 of 100 vector queries; from a user's laptop, 134 ms end to end against 270 ms on the paid service
- Compressed the vectors of one search index: disk from 70.9 GB to 22.2 GB, vector memory from 17.3 GB to 0.6 GB and median query time from 3.9 s to 88 ms, still finding 98% or more of the correct matches
- Moved the cluster to another region and deleted the old one through Terraform, every plan changing exactly the number of resources approved beforehand

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


### Encontre um Terapeuta — https://encontreumterapeuta.com/
*2024 – 2025*
Therapist directory designed and built on WordPress with WooCommerce, Elementor and HivePress: location-based search, messages between patients and therapists, reviews, a blog, and online payments through Asaas (PIX, boleto and card) and Stripe. Another person manages the site today.


## Experience

### DevOps Engineer · Smarter Sorting
*Jul 2025 – Present · Full-time · Boulder, Colorado, US · Remote*

Own cloud infrastructure, the data platform and internal products at a compliance-AI SaaS company, as its only platform engineer.

- Moved the company's data warehouse from Snowflake to BigQuery with zero downtime and ~35% lower compute cost, as the only engineer on the project: 1.4 TB across 33 databases and 30+ customer-facing Tableau reports (4,000+ Snowflake-specific queries migrated), with the cutover coordinated with every data-owning team. Found and fixed years of silently wrong data in the legacy ingestion pipeline along the way.
- Converted a customer executive Tableau dashboard in about 15 minutes with the migration tooling I built: a schema-aware SQL translator, a one-click workbook converter and a schema browser over 5,400 tables.
- Replaced Salesforce Cases with an in-house support platform built in 13 days and live eight days before the Salesforce shutdown: email-to-ticket intake, public help center, knowledge base, role-based access and attachments, with 65,003 tickets and 145,464 messages migrated.
- Identified and delivered over $600k/year in Google Cloud savings across BigQuery, GKE, Cloud SQL and vendor contracts, including a BigQuery misconfiguration costing ~$38,000/month, fixed and verified against the billing export (98.4% reduction).
- Cut both GKE clusters from $19,574/month to save ~$160k/year, the production bill down two-thirds, with no downtime or incidents: right-sized dozens of services, retired 38 dead ones with owner sign-off, halved the production node count (18 to 9) one node at a time, moved staging to Spot capacity and closed with a one-year committed-use agreement.
- Designed, built and validated a self-managed Elasticsearch platform on GKE to replace about $240k/year of managed Elasticsearch spend at a projected $20k/year: regional cluster with infrastructure as code, SSO, snapshots and alerting, replicated from the four live Elastic Cloud deployments (1.3 TB). Passed the data owners' tests, with 1,055 replayed queries matching the paid service on keyword search; vector quantization made one embedding index 40x faster on a third of the disk. Production cutover still ahead.
- Led the move of the company website from Webflow to Google Cloud, built and cut over in one day, one day before the target launch date: Terraform-managed production and staging projects, Cloud Run behind a global HTTPS load balancer with managed TLS, keyless CI/CD, and a low-TTL DNS cutover with a documented rollback.
- Replaced third-party data replication with in-house pipelines: a Python ETL on Cloud Run syncing 196 Salesforce objects daily, Stripe ingestion into BigQuery, and Datastream change data capture from four database environments.
- Built a multi-tenant file portal with a public API in two days after a national retailer refused SFTP, Dropbox and Drive (10,000 API calls in a single client run), and a read-only database access service that grants access without distributing credentials.
- Fixed months of failing production restore tests: traced them to 5.5 TB of write-ahead logs held by two dead replication slots, completed the first successful restore (407 GB) and put point-in-time recovery, automated restore tests and WAL alerts on every production instance.
- Automated the biweekly security log review with a Cloud Run job that reads Cloud Armor, firewall, database and Auth0 logs and files its own Jira tickets.
- Resolved production data incidents for enterprise retail customers, including a business-critical reporting dashboard restored within 5 hours and hazardous-materials data corrected in a national retailer's logistics feed.
- Wrote the company standard for programmatic AI access, replacing static API keys with Workload Identity Federation, and added automated AI review of failed CI builds.

Keywords: Google Cloud Platform, BigQuery, Snowflake, SQL, GKE, Kubernetes, Elasticsearch, Terraform, Cloud Run, Cloud SQL, Datastream, Python, TypeScript, Tableau, FinOps, Workload Identity Federation, CI/CD, Disaster recovery, Incident response, AI agents

### IT Consultant · Pareto AI
*Apr 2026 – Oct 2026 · Contract · Remote*

IT lead for an AI data company with a corporate team and an external expert workforce of about 1,000 accounts across seven Google Workspace tenants. Reported to the Head of People and owned IT end to end: security, identity, devices, vendors and support.

- Gave leadership and six teams (People, Legal, Procurement, Support, Trust and Safety, DevOps) the options and cost analyses behind endpoint management, laptop sourcing, MDM and SSO, and advised on SOC 2 scope, AI coding tool licensing, employee monitoring, data sharing controls and the access standard for hybrid workers.
- Turned a baseline security audit of Google Workspace and Slack into the company's IT roadmap: 76 tracked actions and a 32-point due-diligence readiness checklist.
- Brought 1,000+ accounts across seven Google Workspace tenants under 2-step verification in three phased waves coordinated across teams, with a Slack tool, a support runbook and an identity-verified recovery process that unblocked locked-out external users securely.
- Automated onboarding and offboarding with a Slack app connected to Ashby, Rippling and Linear: hiring and termination events open linked IT tickets and notify the right channels without manual entry.
- Put new company Macs under device management automatically by taking over Apple Business Manager and reconnecting it to the MDM.
- Wrote the security improvement plan (SOC 2, device management, policies, security awareness training) and answered the IT side of customer security reviews.
- Set up IT request and project tracking in Linear.
- Ran the day-to-day IT queue: access, account, mailbox and device requests across Google Workspace, Slack, Bitwarden, Zendesk, Dropbox, Coda and Linear.

Keywords: Google Workspace, GAM, Google Apps Script, Slack, Rippling, Apple Business Manager, MDM, Ashby, Linear, Zendesk, Bitwarden, SOC 2, MFA, IAM, Identity lifecycle, Automation, AI agents, Vendor management

### IT Operations Specialist · Smarter Sorting
*Jan 2024 – Jan 2025 · Full-time · Boulder, Colorado, US · Remote*

Built and ran the company's IT function as its only IT engineer.

- Ran frontline support and the full identity lifecycle for 100+ users across 30+ systems.
- Ended manual account provisioning by integrating Okta with the HR platform and the password manager; administered Okta SSO, Google Workspace, Jira Service Management and the device fleet on Jamf and SentinelOne.
- Defined the service-desk model and automated it in Jira: response and resolution targets by request type, escalation paths, tickets opened from Slack, and onboarding and offboarding workflows that record proof of account deactivation for audit.
- Supported the company's first SOC 2 Type 2 certification.
- Owned repository security and Google Cloud IAM governance: enforced merge-blocking rules for unresolved security alerts across 16 repositories in two days, and moved 32 individual access grants to a group-based model.
- Replaced Finance's manual month-end reporting with a Stripe integration that also surfaced 1,496 records the manual process had been missing.

Keywords: Okta, Google Workspace, Jamf, SentinelOne, Jira Service Management, SOC 2, IAM, Stripe API, Identity lifecycle, Retool, Proofpoint, GitHub, Automation

### PL/SQL Analyst · GB Agritech
*Mar 2025 – Oct 2025 · Contract · Vitória, Espírito Santo, Brazil · Hybrid*

Support for an ERP built on Oracle Forms.

- L3 support for escalated incidents on an Oracle Forms ERP, plus requirements analysis.
- Analysis of Oracle database functions and routines in PL/SQL.
- Improved support processes; maintained agile workflows in Azure DevOps.

Keywords: PL/SQL, Oracle Forms, Azure DevOps, L3 support, Requirements analysis, Incident response, ITSM

### Senior IT Engineer · TheGuarantors
*Apr 2025 – Jul 2025 · Full-time · New York City, US · Remote*

Led the IT team.

- Owned user lifecycle, access control, automation and process documentation, all on the existing tooling rather than adding new platforms.
- Worked with Security, HR and Infrastructure to tighten security protocols and unblock critical operational issues.
- Optimized Okta, Jira, Google Workspace, Slack and Rippling; built API integrations in JavaScript, Bash and Python.

Keywords: Okta, Rippling, Google Workspace, JavaScript, Bash, Python, Team leadership, Jira, Slack, REST APIs

### Internal IT Support · Trustly
*Apr 2022 – Jan 2024 · Full-time · Vitória, Espírito Santo, Brazil · On-site*

- Bilingual (Portuguese/English) technical support for users across every US time zone.
- Ran user requests, asset management and onboarding/offboarding, and improved the internal IT processes.
- Built automation for IT tasks that cut response times.
- Led improvements in inventory control, vendor relations and security policy rollout.

Keywords: IT Service Management, Asset management, User lifecycle, Onboarding, Offboarding, Okta, Google Workspace, GAM, Jamf, MDM, Apple devices, Jira, Automation, Security, Vendor management

### Software Support Analyst · Quality WebPosto
*Mar 2021 – Apr 2022 · Full-time · Vila Velha, Espírito Santo, Brazil · Hybrid*

- Led the support team and trained new hires and interns; ran incident response, turned requests into use cases for the development team and administered the PostgreSQL databases.

Keywords: PostgreSQL, Incident management, Team leadership, ERP, Training & mentoring

### NOC Analyst · Algar Tech
*Apr 2020 – Feb 2021 · Full-time · Vitória, Espírito Santo, Brazil · Remote*

- Bilingual network analyst for VALE S/A, supporting operations in 27 countries across mesh, LTE and radio networks, BGP, MPLS, DMVPN and Cisco, with CA Spectrum and BMC Remedy.

Keywords: Networks, BGP, MPLS, DMVPN, Cisco, CA Spectrum, BMC Remedy, NOC, ITIL, Incident management

### Software Support Analyst · Prosystem
*Oct 2017 – Apr 2020 · Full-time · Vitória, Espírito Santo, Brazil · Hybrid*

- ERP support, incident management and customer service, with incident analysis and improvement requests for the development team; MySQL administration and Windows network support.

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
Canonical: https://vieiraphv2.github.io/ · JSON Resume: https://vieiraphv2.github.io/resume.json · Updated 2026-11-03
