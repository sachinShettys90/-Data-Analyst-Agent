# 🤖 AI Agent Project

A simple AI Agent project built with **Agno, OpenAI, Streamlit, DuckDB, Pandas, and web research tools**.

This project contains two AI applications:

1. 📊 **Data Analyst Agent**
2. 🔍 **Research Agent**

---

## 🚀 Live Demos

### 📊 Data Analyst Agent

https://eui8mbwzamzrrtyvegmwkh.streamlit.app/

Upload a CSV or Excel file and ask questions about your data using natural language.

### 🔍 Research Agent

https://76neyq2bh9dkojsxeewb6o.streamlit.app/

Research topics using HackerNews, DuckDuckGo web search, and online articles.

---

## 📊 1. Data Analyst Agent

The Data Analyst Agent allows users to upload **CSV or Excel files** and ask questions about their data using natural language.

### How it works

```text
CSV / Excel
     ↓
   Pandas
     ↓
   DuckDB
     ↓
  Agno Agent
     ↓
  OpenAI
     ↓
   Answer
```

### Example questions

```text
What is the total revenue?

Which product has the highest sales?

What are the top 10 customers?

What is the average sales amount?

Show sales by month.
```

### Technologies

* Python
* Agno
* OpenAI
* Pandas
* DuckDB
* Streamlit
* LangSmith

---

## 🔍 2. Research Agent

The Research Agent is a **multi-agent application** that researches topics using multiple sources.

It uses:

* HackerNews
* DuckDuckGo
* Online articles

### How it works

```text
                 Research Agent
                       │
                  Agno Team
                       │
       ┌───────────────┼───────────────┐
       ↓               ↓               ↓
 HackerNews        Web Search       Articles
 Researcher        Researcher        Reader
       │               │               │
       ↓               ↓               ↓
 HackerNews        DuckDuckGo       Newspaper4k
```

The agents work together and generate a final research summary.

### Example

```text
What are the latest trends in AI agents?
```

The research team can:

1. Search HackerNews.
2. Search the web.
3. Read relevant articles.
4. Combine the information.
5. Generate a research summary.

### Technologies

* Python
* Agno
* OpenAI
* HackerNews Tools
* DuckDuckGo Tools
* Newspaper4k
* Streamlit

---

## 🏗️ Project Structure

```text
-Data-Analyst-Agent/
│
├── DataAnalyst_Agent.py
├── Research_Agent.py
│
├── AgnoBasics/
│
├── README.md
├── requirements.txt
├── pyproject.toml
├── uv.lock
└── .python-version
```

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/sachinShettys90/-Data-Analyst-Agent.git
```

Go to the project:

```bash
cd -Data-Analyst-Agent
```

Install dependencies using `uv`:

```bash
uv sync
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=ai-agent-project
```

Do not upload your `.env` file to GitHub.

---

## ▶️ Run the Data Analyst Agent

```bash
streamlit run DataAnalyst_Agent.py
```

## ▶️ Run the Research Agent

```bash
streamlit run Research_Agent.py
```

---

## 🔎 LangSmith

The Data Analyst Agent uses **LangSmith** for tracing and debugging.

This helps monitor:

```text
User Query
    ↓
Agent
    ↓
Tools
    ↓
SQL / Analysis
    ↓
Response
```

---

## 🎯 What I Learned From This Project

This project helped me understand:

* AI Agents
* Multi-Agent Systems
* Agno
* Tool Calling
* OpenAI Models
* DuckDB
* Pandas
* SQL
* Web Search
* HackerNews Research
* Streamlit
* LangSmith
* Python dependency management with `uv`

---

## 🔮 Future Improvements

* Add chat history
* Display generated SQL
* Add charts and visualizations
* Improve LangSmith tracing
* Add more research sources
* Add multi-file data analysis
* Add downloadable reports

---

## 👨‍💻 Author

**Sachin Shetty**

GitHub:
https://github.com/sachinShettys90

---

⭐ If you find this project useful, feel free to star the repository.
