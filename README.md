# Microblog

A feature-rich microblogging web application built with Flask. Users can register, write short posts, follow other users, search posts, and read posts translated into their preferred language.

## Features

- **User authentication** – Register, login, logout, and password reset via email
- **Posts** – Create and browse short posts with pagination
- **Follow system** – Follow and unfollow other users; home feed shows posts from followed users
- **Explore** – Browse all posts across the platform
- **User profiles** – Avatar (via Gravatar), "About me" bio, and last-seen timestamp
- **Post translation** – Translate posts on the fly using Google Cloud Translate
- **Full-text search** – Search posts powered by Elasticsearch
- **Internationalization** – UI available in English, Spanish (`es`), and Hindi (`hi`)
- **Email notifications** – Password reset emails; error alerts to admins in production
- **Logging** – Rotating file-based logging in production

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Flask 3 |
| Database | SQLite (dev) / any SQLAlchemy-compatible DB |
| ORM & migrations | Flask-SQLAlchemy, Flask-Migrate (Alembic) |
| Auth | Flask-Login, Werkzeug password hashing, PyJWT |
| Forms | Flask-WTF, WTForms |
| Search | Elasticsearch |
| Translation | Google Cloud Translate API |
| Language detection | langdetect |
| i18n | Flask-Babel |
| Email | Flask-Mail |
| UI | Flask-Bootstrap, Flask-Moment |

## Project Structure

```
microblog/
├── app/
│   ├── auth/          # Authentication blueprint (login, register, password reset)
│   ├── errors/        # Error handler blueprint (404, 500)
│   ├── main/          # Main blueprint (index, explore, profile, follow, search, translate)
│   ├── templates/     # Jinja2 HTML templates
│   ├── translations/  # Babel translation catalogs
│   ├── models.py      # User and Post database models
│   ├── search.py      # Elasticsearch integration
│   ├── translate.py   # Google Cloud Translate integration
│   ├── emails.py      # Email helpers
│   └── cli.py         # Custom Flask CLI commands
├── migrations/        # Alembic database migrations
├── tests.py           # Unit tests
├── config.py          # Application configuration
├── microblog.py       # Application entry point
└── requirements.txt   # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.8+
- (Optional) Elasticsearch instance for full-text search
- (Optional) Google Cloud service account JSON for post translation

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Anish59312/microblog.git
   cd microblog
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Copy or create a `.env` file in the project root:

   ```ini
   SECRET_KEY=your-secret-key

   # Optional – defaults to sqlite:///app.db
   DATABASE_URL=sqlite:///app.db

   # Optional – email settings (for password reset and error alerts)
   MAIL_SERVER=localhost
   MAIL_PORT=8025

   # Optional – Elasticsearch (leave unset to disable search)
   ELASTICSEARCH_URL=http://localhost:9200
   ```

5. **Initialise the database**

   ```bash
   flask db upgrade
   ```

6. **Run the development server**

   ```bash
   flask run
   ```

   Open [http://localhost:5000](http://localhost:5000) in your browser.

## Configuration Reference

All settings live in `config.py` and are read from environment variables.

| Variable | Default | Description |
|---|---|---|
| `SECRET_KEY` | `you-will-never-guess` | Flask secret key |
| `DATABASE_URL` | `sqlite:///app.db` | SQLAlchemy database URI |
| `MAIL_SERVER` | – | SMTP server hostname |
| `MAIL_PORT` | `8025` | SMTP server port |
| `MAIL_USE_TLS` | off | Set any value to enable TLS |
| `MAIL_USERNAME` | – | SMTP auth username |
| `MAIL_PASSWORD` | – | SMTP auth password |
| `ELASTICSEARCH_URL` | – | Elasticsearch node URL |
| `POSTS_PER_PAGE` | `3` | Pagination page size |

## Running Tests

```bash
python tests.py
```

## Translations

Translations are managed with Flask-Babel. To compile existing catalogs:

```bash
flask translate compile
```

To add a new language (e.g., French):

```bash
flask translate init fr
# ... edit app/translations/fr/LC_MESSAGES/messages.po ...
flask translate compile
```

## Local Email Debugging

To test email-related features (password reset, etc.) without a real mail server, run the included debug SMTP daemon:

```bash
aiosmtpd -n -c aiosmtpd.handlers.Debugging -l localhost:8025
```

## License

This project is for educational purposes and does not currently carry an open-source license.
