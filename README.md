# 🚆 IRCTC Tatkal AI-Copilot

A Python-based project to simplify train journey preparation by collecting travel details, understanding user preferences written in natural language, and recommending sample trains.

The long-term goal is to develop an AI-powered assistant that helps users prepare for Tatkal bookings through a guided, human-in-the-loop workflow.

> **Project status:** Work in progress. Train recommendations currently use sample data. Live IRCTC availability and booking are not implemented.

## 🎯 Project Objectives

- Collect and validate train journey details.
- Understand train preferences expressed in simple English.
- Recommend sample trains based on travel class, preferred train, and departure time.
- Save and reuse journey preferences.
- Explore LLM integration for more flexible natural-language understanding.
- Use browser automation for testing and future workflow development.

## ✨ Features Implemented

- **Journey input and validation:** Collects source, destination, travel date, and travel class.
- **Preference parsing:** Extracts train preferences, travel class, and departure time from simple English requests.
- **Sample train ranking:** Scores and sorts sample trains based on user preferences.
- **Preference persistence:** Saves and loads preferences using JSON.
- **Browser automation testing:** Uses Playwright for a basic browser automation smoke test.

## 🛠️ Technology Stack

- Python
- Playwright
- JSON
- Git and GitHub
- OpenAI API — planned for future integration

## 📁 Project Structure

```text
tatkal-ai-copilot/
├── app.py
├── main.py
├── journey.py
├── train_selector.py
├── preference_parser.py
├── preferences.py
├── .gitignore
└── README.md
```

### File Descriptions

| File | Purpose |
|---|---|
| `app.py` | Runs the main application workflow |
| `main.py` | Tests basic browser automation using Playwright |
| `journey.py` | Collects and validates journey details |
| `train_selector.py` | Ranks sample trains based on preferences |
| `preference_parser.py` | Parses natural-language preferences using rules |
| `preferences.py` | Saves and loads preferences using JSON |

## ⚙️ Getting Started

### Prerequisites

- Python installed on your system
- Git
- Visual Studio Code (recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/AdarshCloud1954/tatkal-ai-copilot.git
cd tatkal-ai-copilot
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script activation, use Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### 3. Install Dependencies

Install Playwright:

```bash
python -m pip install playwright
```

Install the browser required for the smoke test:

```bash
python -m playwright install chromium
```

### 4. Run the Application

Run the main application:

```bash
python app.py
```

To run the browser automation smoke test:

```bash
python main.py
```

## 💬 Example User Preference

```text
Prefer Rajdhani in 3A after 7 PM
```

The current rule-based parser can extract preferences such as:

- Preferred train: Rajdhani
- Travel class: 3A
- Departure after: 19:00

The application then ranks matching sample trains.

## 🗺️ Roadmap

- [x] Journey details collection and validation
- [x] Rule-based natural-language preference parsing
- [x] Sample train ranking
- [x] Save and reuse user preferences
- [x] Basic Playwright browser automation test
- [ ] Integrate an LLM for natural-language understanding
- [ ] Add automated tests and improve error handling
- [ ] Explore permitted live train information sources
- [ ] Develop a guided booking-assistance workflow

## 🔐 Security and Responsible Use

- Never commit API keys, passwords, access tokens, or other secrets.
- Keep local environment files and personal preferences out of the repository.
- Use authorized sources for train information.
- Respect IRCTC terms, access controls, CAPTCHA, OTP, and payment authentication.
- Keep booking decisions and sensitive authentication steps under the user's control.

## ⚠️ Current Limitations

- Train recommendations use dummy data, not live train schedules or seat availability.
- The current preference parser is rule-based; LLM integration is planned.
- The project does not currently book tickets or guarantee Tatkal availability.

## 👨‍💻 About This Project

This is a personal learning project focused on Python development, browser automation, natural-language processing, and practical AI integration.

The project is being developed incrementally, with a focus on testing each component and improving the workflow over time.

## 📌 Disclaimer

This project is an independent learning project and is not affiliated with, endorsed by, or officially connected to IRCTC or Indian Railways.
