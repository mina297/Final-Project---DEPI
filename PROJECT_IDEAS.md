# Project Idea
SentinelNet — Real-Time Network Intrusion & Threat Risk Scoring

### Business Objective

Classify malicious network traffic in real time to help a security team
prioritize threats that need immediate response.

### Machine Learning Task

- **Task:** Multi-class classification
- **Target variable:** `attack_type`
- **Target values:** `Normal`, `DoS`, `Probe`, `R2L`, `U2R`

### Primary Dataset and Messiness

[NSL-KDD dataset on Kaggle](https://www.kaggle.com/datasets/hassan06/nslkdd)

The dataset has several known data-quality challenges:

- Mixed categorical and numeric feature types
- Class imbalance across attack categories
- Documented redundant/duplicate records requiring explicit deduplication

### API Integration Plan

Query the [AbuseIPDB API](https://www.abuseipdb.com/api) for abuse and
reputation scores of IP addresses present in the traffic data. Enrich each
connection with a real-time "known malicious source" signal. The integration
will require rate-limit handling and IP-format normalization.

### Web Scraping Plan

Scrape a live CVE/vulnerability database, such as the
[National Vulnerability Database (NVD)](https://nvd.nist.gov/), for recently
disclosed vulnerabilities. Engineer a `recent_cve_activity` feature that
reflects the current threat landscape at prediction time.

---

 in
current market data.
