# HOME-TAKER 🏠

> **AI-powered "External Brain" for caregivers**

There are over **53 million unpaid caregivers** in the US providing **$600 billion** in labor annually, with **61%** of them working full-time while managing complex health and home logistics. Globally, **1 in 5 adults** are informal caregivers, spending **20+ hours/week** managing medications, appointments, and care coordination for aging family members.

**HOME-TAKER** is an AI-powered "External Brain" that uses **graph-based memory** to proactively track and connect micro-details like medication changes, trusted service providers, and family milestones.

---

## Project Structure

```
home-taker/
├── backend/          # FastAPI backend with graph-based memory
│   ├── routes/       # API endpoints
│   ├── services/     # Business logic
│   ├── models.py     # Data models
│   ├── config.py     # Configuration
│   └── main.py       # Application entry point
├── frontend/         # React + Vite frontend
│   ├── src/          # React components
│   └── public/       # Static assets
├── pyproject.toml    # Python dependencies
└── README.md
```

---

## Setup Guide

### Prerequisites

- **Python 3.12+**
- **Node.js 18+** (for frontend)
- **uv** package manager (recommended) or pip

### 1. Clone the Repository

```bash
git clone <repository-url>
cd home-taker
```

### 2. Backend Setup

#### Install Python dependencies

Using **uv** (recommended):
```bash
uv sync
```

Or using **pip**:
```bash
pip install -e .
```

#### Configure Environment Variables

Create a `.env` file in the project root:

```bash
# API Keys
GOOGLE_API_KEY=your_google_api_key
OPENAI_API_KEY=your_openai_api_key  # Optional, if using OpenAI

# Application
API_TITLE=HOME-TAKER API
API_VERSION=0.1.0
```

#### Run the Backend

```bash
# From project root
uv run python -m backend.main

# Or with pip
python -m backend.main
```

The API will be available at `http://localhost:8000`

**Test the API:**
```bash
curl http://localhost:8000
```

### 3. Frontend Setup

#### Navigate to frontend directory

```bash
cd frontend
```

#### Install dependencies

```bash
npm install
```

#### Configure Environment (if needed)

Check `frontend/.env.example` (if available) or create `.env`:

```bash
VITE_API_URL=http://localhost:8000
```

#### Run the Development Server

```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/api/preferences` | GET/POST | Manage user preferences |
| `/api/logs` | GET/POST | Access and create logs |
| `/api/chat` | POST | Chat with AI assistant |

---

## Development

### Backend

```bash
# Run with auto-reload
uv run python -m backend.main

# Run tests (if available)
uv run pytest
```

### Frontend

```bash
# Development server with hot-reload
npm run dev

# Build for production
npm run build

# Lint code
npm run lint
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 💙 Support

HOME-TAKER is built to support caregivers everywhere. If you're using this project and need help, please open an issue.

**Remember: You're not alone in this caregiving journey.**
