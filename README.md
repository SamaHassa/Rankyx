# 🔎 Rankyx — Multi-Agent AI Product Research & Price Comparison

**A multi-agent AI system that finds, scrapes, compares, and reports on products across online stores, so you can buy at the best value-for-money price.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![CrewAI](https://img.shields.io/badge/Framework-CrewAI-orange)
![LLM](https://img.shields.io/badge/LLM-gpt--oss--120b%20(Groq)-green)
![Status](https://img.shields.io/badge/Status-Moving%20to%20Production-yellow)

---

## 📌 Overview

Rankyx automates product price research. You give it a product name, a list of stores, and a target country. Four specialized AI agents then work in sequence to:

1. Generate smart search queries
2. Search the web for product pages
3. Extract structured product data (price, discount, specs)
4. Produce a professional HTML comparison report

No more opening 20 tabs to compare prices.

---

## ✨ Key Features

- **Multi-agent pipeline** built with [CrewAI](https://docs.crewai.com/) (sequential process)
- **Structured outputs** validated with Pydantic at every stage
- **Country-aware search** (only stores that sell in your target country)
- **Confidence filtering** with a configurable score threshold
- **Smart ranking** of the top N products with recommendation notes
- **Standalone HTML report** styled with Bootstrap, ready to open or share
- **Observability** with [AgentOps](https://www.agentops.ai/) for tracing agent runs
- **Intermediate outputs saved** to `agent-output/` for easy debugging

---

## 🧭 Workflow

### High-level pipeline

```mermaid
flowchart LR
    A([👤 User Input]) --> B[🧠 Agent 1<br/>Search Recommendation]
    B -->|search_queries.json| C[🔍 Agent 2<br/>Search Engine]
    C -->|search_engine_results.json| D[🕸️ Agent 3<br/>Scraping]
    D -->|scraping_results.json| E[📊 Agent 4<br/>Report Generation]
    E -->|product_report.html| F([📄 HTML Report])

    T1[(Tavily API)] -.-> C
    T2[(ScrapeGraphAI)] -.-> D
    L[(Groq LLM)] -.-> B
    L -.-> C
    L -.-> D
    L -.-> E
```

### Detailed data flow

```mermaid
sequenceDiagram
    participant U as User
    participant A1 as Search Recommendation Agent
    participant A2 as Search Engine Agent
    participant TV as Tavily
    participant A3 as Scraping Agent
    participant SG as ScrapeGraphAI
    participant A4 as Report Agent

    U->>A1: product, websites, country, language
    A1-->>A2: up to 3 search queries
    loop For each query
        A2->>TV: search(query, max_results=3)
        TV-->>A2: results with scores
    end
    A2-->>A3: filtered results (score >= threshold)
    loop For each product URL
        A3->>SG: extract(url, schema)
        SG-->>A3: title, price, discount, specs
    end
    A3-->>A4: Top N ranked products
    A4-->>U: Standalone HTML report
```

### Agent responsibilities

| # | Agent | Input | Output | Tool |
|---|-------|-------|--------|------|
| 1 | **Search Recommendation Agent** | Product, stores, country, language | Up to 3 search queries | None (LLM only) |
| 2 | **Search Engine Agent** | Search queries | Ranked search results | Tavily Search |
| 3 | **Scraping Agent** | Product page URLs | Structured product data | ScrapeGraphAI |
| 4 | **Report Generation Agent** | Extracted products | Full HTML report | None (LLM only) |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Agent framework | CrewAI |
| LLM | `gpt-oss-120b` via Groq (OpenAI-compatible API) |
| Web search | Tavily |
| Web scraping | ScrapeGraphAI |
| Data validation | Pydantic |
| Monitoring | AgentOps |
| Report styling | HTML, CSS, Bootstrap |

---

## 📁 Project Structure

```text
rankyx/
├── main.py                  # Agents, tasks, and crew definition
├── .env                     # API keys (never commit this)
├── requirements.txt
├── README.md
└── agent-output/            # Auto-generated outputs
    ├── search_queries.json
    ├── search_engine_results.json
    ├── scraping_results.json
    └── product_report.html
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/rankyx.git
cd rankyx
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install crewai agentops tavily-python scrapegraph-py python-dotenv pydantic
```

### 4. Set up environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
SCRAPGRAPH_API_KEY=your_scrapegraph_key
AGENTOPS_API_KEY=your_agentops_key
```

Get your keys here:
- [Groq Console](https://console.groq.com/)
- [Tavily](https://tavily.com/)
- [ScrapeGraphAI](https://scrapegraphai.com/)
- [AgentOps](https://www.agentops.ai/)

### 5. Run the project

```bash
python main.py
```

Open `agent-output/product_report.html` in your browser to see the report.

---

## ⚙️ Configuration

Edit the inputs at the bottom of `main.py`:

```python
crew.kickoff(
    inputs={
        "product_name": "iPhone 14",
        "websites_list": "Amazon, eBay, Walmart",
        "country_name": "Egypt",
        "no_keywords": 3,
        "language": "English",
        "score_threshold": 0.5,
        "top_recommendations_no": 5,
    }
)
```

| Parameter | Description |
|-----------|-------------|
| `product_name` | Product to research |
| `websites_list` | Target stores, comma-separated |
| `country_name` | Country where the product must be sold |
| `no_keywords` | Max number of search queries |
| `language` | Language of the search queries |
| `score_threshold` | Minimum Tavily relevance score (0 to 1) |
| `top_recommendations_no` | Number of top products in the final report |

---

## 📄 Example Output

The final report includes:

- Executive summary
- Product comparison table
- Key specifications
- Price analysis
- Advantages and disadvantages
- Evidence-based recommendations
- Data limitations and source links

---

Production Roadmap
The next development stage focuses on transforming Rankyx into a production-ready application.
- Code quality: Modular architecture, configuration validation, structured logging, and robust error handling.
- Testing: Pytest unit and integration tests, including mocked external API calls.
- API layer: FastAPI endpoints for creating comparisons, checking job status, and retrieving reports.
- Persistence: PostgreSQL and SQLAlchemy for storing jobs, product data, and comparison results.
- Containerization: Docker and Docker Compose for reproducible local development and deployment.
- Background processing: Redis and Celery for long-running workflows and controlled retries.
- CI/CD: GitHub Actions for automated tests, code quality checks, and image builds.
- Observability: Improved tracing, error monitoring, health checks, and execution metrics.
- Deployment: Cloud hosting and durable report storage.

---

## ⚠️ Limitations

- Results depend on search quality and on how scrapable each store is.
- Some sites block scrapers or load prices dynamically.
- Prices change fast, so reports are a snapshot in time.
- The agents are instructed never to invent missing data, and missing fields are flagged in the report.

---

## 🤝 Contributing

Contributions are welcome:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## 👤 Author

**Sama Hassan**
AI Engineer | Cairo, Egypt
[GitHub]((https://github.com/SamaHassa/Rankyx)) · [LinkedIn]((https://www.linkedin.com/in/sama-hassans/))
