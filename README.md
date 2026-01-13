# Fintech QA Automation Framework

A comprehensive test automation framework simulating quality assurance practices for a cryptocurrency exchange environment. Built with modern Python stack to demonstrate skills relevant to Fintech QA roles.

## 🎯 Project Goals

*   Demonstrate proficiency in API, database, and potential UI testing in a financial context.
*   Showcase understanding of test architecture, CI/CD integration, and reporting.
*   Serve as a portfolio piece for targeting QA roles in Fintech/Crypto companies.

## 🏗️ Architecture & Tech Stack

| Layer              | Technology                          |
| ------------------ | ----------------------------------- |
| **Language**       | Python 3.11+                        |
| **Test Framework** | Pytest                              |
| **API Testing**    | `requests`, Pytest fixtures         |
| **API Mocking**    | FastAPI (for simulated exchange)    |
| **Database**       | SQLite / PostgreSQL (via Docker)    |
| **CI/CD**          | GitLab CI / GitHub Actions          |
| **Reporting**      | Allure Reports                      |
| **Load Testing**   | Locust                              |
| **Containerization**| Docker, Docker Compose             |

## 📁 Project Structure

```
fintech-qa-automation-2026/
├── tests/
│   ├── api/               # REST API tests (market data, order book simulation)
│   ├── database/          # Data integrity and SQL tests
│   └── web_ui/            # (Planned) POM-based UI tests
├── src/
│   ├── clients/           # API and WebSocket clients
│   ├── helpers/           # Data generators, validators, SQL queries
│   └── mocks/             # FastAPI mock server for exchange simulation
├── config/                # Configuration files (env, endpoints)
├── docs/                  # Additional documentation
├── docker-compose.yml     # Multi-container setup
├── .gitlab-ci.yml         # CI/CD pipeline definition
└── requirements.txt       # Python dependencies
```

## Quick Start

- git clone https://github.com/user04040404/fintech-qa-automation-2026.git
- cd fintech-qa-automation-2026
- python -m venv venv
- source venv/bin/activate  # Works for both bash and zsh!
- pip install -r requirements.txt
- pytest tests/api/test_smoke_public_api.py -v
  
