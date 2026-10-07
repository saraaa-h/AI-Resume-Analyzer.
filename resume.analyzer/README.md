# AI Resume Analytics & Job Matching System

A dynamic web application built with Flask, Pandas, and Ollama (Llama2) that analyzes candidate skills, provides AI-powered career recommendations, and matches skills with relevant job opportunities from a CSV dataset.

---

## Features
- Skill Input Interface: Clean, modern web form for candidates to submit technical skills.
- AI Career Recommendations: Integrated with a local LLM via Ollama (llama2) to generate tailored career feedback.
- Data Matching Engine: Uses Pandas to search and filter job openings based on candidate skills.
- Modern UI & Responsive Design: Styled with modern CSS cards, highlighted AI recommendation boxes, and interactive data tables.
- Dynamic Web Routing: Powered by Flask and Jinja2 templating for seamless layout rendering.

---

## Tech Stack
- Backend Framework: Flask
- Data Processing: Pandas
- AI Integration: Ollama (Llama2 model) via HTTP requests
- Frontend: HTML5, Custom CSS
- Templating Engine: Jinja2
- Data Source: CSV (jobs.csv)

---

## Project Structure
`text
resume-analyzer/
│
├── .gitignore          # Git exclusion rules for virtual environments
├── requirements.txt    # Python dependencies list
├── README.md           # Project documentation
├── app.py              # Main Flask application logic & routing
├── jobs.csv            # Job dataset containing titles, companies, and skills
└── templates/
    ├── index.html      # Home page form for submitting skills
    └── results.html    # Results page displaying AI advice and job matches