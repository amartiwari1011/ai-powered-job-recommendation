# AI-Powered Job Recommendation System

An intelligent, LLM-powered job recommendation application built to match job seekers with the most relevant opportunities based on their skill sets, experiences, and preferences.

---

## 🚀 Features

- **Semantic Profiling:** Parses resumes and user backgrounds using advanced Language Models.
- **Intelligent Matching:** Moves beyond basic keyword matching to understand contextual relevance, implied skills, and career trajectories.
- **Automated Scraping/Sourcing:** Integrated with Apify tasks to dynamically source and fetch active job postings.
- **FastAPI / Flask Backend:** Clean and scalable Python architecture (`app.py`) built to handle asynchronous requests.

---

## 📂 Project Structure

```text
├── src/
│   ├── helper.py        # Utility scripts (parsing, text cleanup, formatting)
│   ├── job_api.py       # Integration endpoints for external job feeds/Apify
│   └── mcp_server.file  # Model Context Protocol configurations for tool integration
├── app.py               # Main application entry point & web server routes
├── requirement.txt      # Python package dependencies
└── .gitignore           # Excluded files and environment variables (.env)
```

---

## ⚙️ How It Works (Flow & Logic)

The project leverages a modern pipeline to orchestrate the semantic recommendation flow:

```text
[User Profile / Resume] ──> [src/helper.py (Parsing & Embedding)] ──┐
                                                                   ▼
[Job Feeds / Apify]    ──> [src/job_api.py (Data Ingestion)]   ──> [LLM / Vector Matcher] ──> [Recommended Jobs]
```

1. **Ingestion (`src/job_api.py`):** The application fetches live job posts via third-party web scrapers or API connectors.
2. **Text Processing (`src/helper.py`):** Raw resumes and job postings are cleaned, structured, and prepared for the Large Language Model.
3. **Application Control (`app.py`):** Acts as the central hub, receiving queries from users, executing the matching algorithms, and serving back data-driven suggestions.
4. **Integration (`src/mcp_server.file`):** Sets up custom tools or plugins allowing external systems to query your recommendation engine.

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com
cd ai-powered-job-recommendation
```

### 2. Configure Environment Variables
Create a `.env` file in the root folder and configure your sensitive access credentials:
```env
OPENAI_API_KEY=your_openai_api_key_here
APIFY_API_TOKEN=your_apify_api_token_here
```

### 3. Install Dependencies
```bash
pip install -r requirement.txt
```

### 4. Run the Application
```bash
python app.py
```

---

## 🛠️ Technologies Used

- **Python** (Core application programming)
- **Large Language Models (LLMs)** (OpenAI API semantic reasoning)
- **Apify** (Automated job search web scraping)
- **Model Context Protocol (MCP)** (Standardized LLM tool integration)
