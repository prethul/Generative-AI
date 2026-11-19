<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=200&section=header&text=Generative%20AI&fontSize=52&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=From%20LLM%20fundamentals%20to%20Multi-Agent%20Systems&descAlignY=60&descSize=16" alt="Generative AI banner" width="100%" />

### A hands-on learning journey through LLMs, LangChain and AI Agents

<p>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge" alt="LangChain" />
  <img src="https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter" />
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
</p>

<p>
  <img src="https://img.shields.io/github/last-commit/prethul/Generative-AI?style=flat-square&color=2c5364" alt="Last commit" />
  <img src="https://img.shields.io/github/repo-size/prethul/Generative-AI?style=flat-square&color=2c5364" alt="Repo size" />
  <img src="https://img.shields.io/github/stars/prethul/Generative-AI?style=flat-square&color=2c5364" alt="Stars" />
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square" alt="PRs welcome" />
</p>

[**About**](#about) |
[**Roadmap**](#learning-roadmap) |
[**Projects**](#featured-projects) |
[**Quick Start**](#quick-start) |
[**Author**](#about-the-author)

</div>

---

## About

This repository is my **structured, hands-on journey into Generative AI engineering**. It starts from the basics of Large Language Models and builds step by step toward production-style projects such as a **Multi-Agent Research System**.

Every module is organised in numbered folders, so you can follow it in order like a course, or jump straight to the topic you need.

> **Who is this for?** Students and developers who want to learn LangChain and GenAI by reading and running real code, not just theory.

---

## Learning Roadmap

| # | Module | What you will learn |
|:-:|--------|---------------------|
| 1 | [**LLMs**](./1.LLMS) | Working with Large Language Models and their core concepts |
| 2 | [**Chat Models**](./2.ChatModels) | Using chat models and handling conversations |
| 3 | [**Prompt Engineering**](./3.Prompt_engineering) | Writing effective prompts and prompt templates |
| 4 | [**Structured Output**](./4.%20Structured_Output) | Getting reliable, schema-based responses from LLMs |
| 5 | [**Output Parsers**](./5.%20Output_Parsers) | Parsing model output into usable formats |
| 6 | [**Chains**](./6.%20Chains) | Building multi-step workflows with chains |
| 7 | [**Runnables - Part 1**](./7.%20Runnable%20part%201) | LangChain Runnable interface fundamentals |
| 8 | [**Runnables - Part 2**](./8.%20Runnable%20part%202) | Advanced Runnable composition |
| 9 | [**Document Loaders**](./9.%20Document%20Loader) | Loading data from files and other sources |
| 10 | [**Text Splitters**](./10.%20Text%20splitters) | Splitting documents into chunks for LLM pipelines |
| 12 | [**Tools in LangChain**](./12.%20Tools%20in%20Langchain) | Giving LLMs the ability to use tools |

---

## Featured Projects

<table>
  <tr>
    <td width="33%" valign="top">
      <h3>Multi Agent Research System</h3>
      <p>A multi-agent pipeline that researches a topic and produces a structured report, built with LangChain, Gemini and Tavily search.</p>
      <a href="./Multi%20Agent%20Research%20System"><b>View project</b></a>
    </td>
    <td width="33%" valign="top">
      <h3>Chat-Bot</h3>
      <p>A conversational chatbot that puts the chat model and prompt concepts from the modules into practice.</p>
      <a href="./Chat-Bot"><b>View project</b></a>
    </td>
    <td width="33%" valign="top">
      <h3>Gen AI Projects</h3>
      <p>A collection of smaller GenAI experiments and mini-projects.</p>
      <a href="./Gen%20AI%20Projects"><b>View projects</b></a>
    </td>
  </tr>
</table>

---

## Repository Structure

```text
Generative-AI/
├── 1.LLMS/
├── 2.ChatModels/
├── 3.Prompt_engineering/
├── 4. Structured_Output/
├── 5. Output_Parsers/
├── 6. Chains/
├── 7. Runnable part 1/
├── 8. Runnable part 2/
├── 9. Document Loader/
├── 10. Text splitters/
├── 12. Tools in Langchain/
├── Chat-Bot/
├── Gen AI Projects/
├── Multi Agent Research System/
├── Runnable_in_Langchain.ipynb
├── Runnable_in_Langchain_2.ipynb
├── simple_app.py
├── template.json
├── test.py
└── requirements.txt
```

---

## Tech Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=python,git,github,vscode,jupyter&theme=dark" alt="Tech stack icons" />

</div>

| Category | Tools |
|----------|-------|
| **Language** | Python |
| **Frameworks** | LangChain, Streamlit |
| **LLM / Search** | Google Gemini, Tavily |
| **Environment** | Jupyter Notebook, VS Code, Git and GitHub |

---

## Quick Start

**1. Clone the repository**

```bash
git clone https://github.com/prethul/Generative-AI.git
cd Generative-AI
```

**2. Create a virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Add your API keys**

Create a `.env` file in the project root and add the keys for the providers you use:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

> **Note:** Never commit your `.env` file. Make sure it is listed in `.gitignore`.

**5. Run a notebook or app**

```bash
jupyter notebook          # open any module's notebook
streamlit run app.py      # for Streamlit-based projects
```

---

## Contributing

Suggestions and improvements are always welcome.

1. Fork the repository
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## About the Author

<div align="center">

<h3>Dipto Howlader Prethul</h3>

**Final-year CSE Student | AI/ML Engineer in the making**

Computer Science and Engineering, Uttara University, Gazipur, Bangladesh

</div>

I focus on **AI/ML engineering**, and my work spans:

- **ML model deployment:** taking models from notebooks to working apps
- **n8n automation workflows:** AI-powered business automation
- **Full-stack web development:** building complete, user-facing products

<div align="center">

<a href="https://github.com/prethul">
  <img src="https://img.shields.io/badge/GitHub-prethul-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
</a>
<a href="https://www.linkedin.com/in/dipto-howlader-prethul-603808333/">
  <img src="https://img.shields.io/badge/LinkedIn-Dipto%20Howlader%20Prethul-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
</a>

</div>

---

<div align="center">

### If this repository helped you, please give it a star.

<sub>Created by <a href="https://github.com/prethul">Dipto Howlader Prethul</a></sub>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,100:0f2027&height=100&section=footer" alt="Footer" width="100%" />

</div>
