# SignalWeave — SOC Detection & Correlation Engine

SignalWeave is a research-driven Security Operations Center (SOC) detection and correlation engine designed to ingest authentication logs, identify suspicious behavior patterns, calculate contextual risk, and determine whether an incident should be escalated.

Unlike traditional alert-heavy security tools, SignalWeave separates raw events from actionable signals and incidents, reducing false positives and demonstrating how modern SOC platforms operate in real-world environments.

---

## Abstract

Security Operations Centers often struggle with alert fatigue caused by isolated, uncorrelated security events. SignalWeave addresses this problem by implementing a multi-phase detection pipeline that correlates authentication activity over time, evaluates risk based on behavior patterns, and escalates incidents only when justified.

This project serves as both a functional SOC prototype and a research demonstration of detection engineering principles used in enterprise security platforms.

---

## Problem Statement

Most beginner security tools trigger alerts on every suspicious event, which does not reflect real SOC operations. In real environments:

- Not every failed login is an attack
- Detection requires context and time-based correlation
- Risk must be evaluated before escalating incidents

SignalWeave was built to model these real-world constraints and demonstrate professional SOC design.

---

## System Architecture

The architecture is designed as a pipeline, where each stage adds intelligence and context to the data:

Raw Authentication Logs
↓
Ingest API (FastAPI)
↓
Event Normalization
↓
Correlation Engine
↓
Signals (Suspicious Patterns)
↓
Risk Scoring
↓
Incident Decision


### Key Design Principle

**Detection ≠ Incident**

SignalWeave intentionally separates signals from incidents to prevent unnecessary escalation and reduce alert fatigue.

---

## Core Features

- REST-based authentication log ingestion
- Normalized security event schema
- Sliding time-window correlation logic
- Brute-force attack detection
- Risk scoring (LOW / MEDIUM / HIGH)
- Incident suppression when risk is insufficient
- Modular, extensible backend architecture

---

## Project Structure


SignalWeave/
├── backend/
│ ├── main.py
│ ├── ingest/
│ │ ├── ingest_api.py
│ │ └── parser.py
│ ├── correlate/
│ │ └── auth_rules.py
│ └── risk/
│ └── risk_engine.py
├── README.md


---

## How SignalWeave Works (End-to-End Flow)

1. A user or system sends an authentication event to the ingest API
2. The event is parsed and normalized into a standard schema
3. The correlation engine tracks repeated failed logins by entity (IP)
4. If thresholds are exceeded within a time window, a signal is generated
5. A risk score is calculated based on signal severity
6. An incident is created only if the risk meets escalation criteria

This approach mirrors how enterprise SOC platforms prioritize threats.

---

## API Usage Guide

### Start the Application

Run the following command from the project root:

```bash 
python -m uvicorn backend.main:app --reload

The server will be available at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs
Ingest Authentication Event

Endpoint

POST /ingest/auth

Request Body

{
  "timestamp": "2026-02-10T10:15:30Z",
  "event_type": "failed_login",
  "user": "admin",
  "ip": "192.168.1.100",
  "host": "server-01"
}

Successful Response Example

{
  "status": "ingested",
  "event_id": "auth-xxxx",
  "signals": [
    {
      "type": "brute_force",
      "confidence": "high",
      "entity": "ip:192.168.1.100",
      "window": "10m",
      "count": 17
    }
  ],
  "risk": {
    "risk_score": 50,
    "risk_level": "MEDIUM"
  },
  "incident": null
}

Detection & Correlation Logic
Events are correlated using a sliding time window
Failed authentication attempts are tracked per IP address
Threshold-based logic determines suspicious behavior
Signals represent patterns, not confirmed attacks
Risk scoring determines escalation severity
This logic aligns with real SOC detection engineering practices.

Use Cases

Brute-force attack detection
SOC analyst training and education
Detection engineering research
Security log analysis demonstrations
Academic and competition presentations

Technologies Used

Python
FastAPI
Uvicorn
REST APIs
Detection engineering concepts
Time-based correlation algorithms
