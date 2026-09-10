# Project Ideas

## Idea 1: Smart Traffic & Accident Risk Prediction for Cairo

### Business Objective

Predict accident risk severity (`Low`, `Medium`, or `High`) in specific areas to
help traffic authorities and drivers take preventive action and reduce
accident-related costs.

### Machine Learning Task

- **Task:** Classification
- **Target variable:** `accident_risk_level`
- **Target values:** `Low`, `Medium`, `High`
- **Target definition:** Derived by binning historical accident
  frequency/severity for a given area and time window.

### Primary Dataset and Messiness

[US Accidents dataset on Kaggle](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)

This countrywide traffic accident dataset contains millions of records and is
genuinely messy:

- Significant missing values in weather and lighting fields
- Inconsistent location and timestamp formatting
- Duplicate incident reports requiring deduplication before modeling

### API Integration Plan

Query the [OpenWeatherMap API](https://openweathermap.org/api) for temperature,
humidity, wind speed, precipitation, and visibility at the accident's location
and time. Timestamp alignment and unit normalization (metric versus imperial)
will be required before merging the API data with the historical dataset.

### Web Scraping Plan

Scrape a live traffic or road-conditions source, such as a local traffic-alert
or Department of Transportation page, to capture current road closures and
construction activity. Use this data to engineer a `road_condition_flag`
feature representing real-time road risk factors that are not present in the
historical dataset.

---

## Idea 2: AirGuard — Airline Passenger Experience & Risk Platform

### Business Objective

Predict passenger satisfaction and flag high-risk flights so airlines can
proactively manage service and delay issues.

### Machine Learning Task

- **Task:** Classification
- **Target variable:** `satisfaction`
- **Target values:** `Satisfied`, `Unsatisfied`
- **Target definition:** Taken directly from the passenger satisfaction
  dataset's labeled outcome.

### Primary Dataset and Messiness

[Airline Passenger Satisfaction dataset on Kaggle](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction)

The dataset has several data-quality challenges:

- Missing `Arrival Delay` values
- Inconsistent service-rating scales
- The value `0` is used both for "not applicable" and genuine zero ratings,
  requiring careful imputation and encoding

### API Integration Plan

Use a live flight-tracking API, such as [AviationStack](https://aviationstack.com/)
or [OpenSky](https://opensky-network.org/), to provide real-time delay and
aircraft data. Join this information with a weather API for current
departure/arrival conditions. Timestamp and airport-code alignment will be
required with the primary dataset.

### Web Scraping Plan

Scrape an airline review platform, such as Skytrax or AirlineQuality, for
recent ratings and complaint text. Engineer a `recent_complaint_rate` feature
that reflects current service sentiment trends.

---

## Idea 3: SentinelNet — Real-Time Network Intrusion & Threat Risk Scoring

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

## Idea 4: Egyptian Real Estate Fair-Price Predictor

### Business Objective

Predict fair market prices for property listings in Egypt to help buyers
detect overpriced listings and help agents price properties competitively.

### Machine Learning Task

- **Task:** Regression
- **Target variable:** `price_egp`
- **Target definition:** Continuous price in Egyptian Pounds

### Primary Dataset and Messiness

An Egyptian real estate listings dataset from Kaggle containing Cairo/Giza
property listings.

The dataset is expected to have several data-quality challenges:

- Inconsistent area units (`م²` versus `sqm`)
- Mixed Arabic and English text fields
- Missing bedroom and bathroom counts requiring imputation

> **Dataset URL:** Add the selected Cairo/Giza Kaggle dataset link once the
> specific dataset has been chosen.

### API Integration Plan

Use a currency and inflation API to normalize historical prices against EGP
inflation over time, allowing fair comparison of listings from different years.

### Web Scraping Plan

Scrape a live Egyptian property-listing site, such as
[Aqarmap](https://aqarmap.com.eg/), for current comparable asking prices in the
same neighborhood. Engineer a `local_market_price_index` feature grounded in
current market data.
