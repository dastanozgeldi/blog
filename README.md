# Dositan's Homepage 🏠
~ A blog website of mine. [hosting soon]
![Site demo](app/static/demo.png)

---

### Why you've made this?
**Convenience.** More and more **Social Media** today have an option to provide a URL for your personal website. In addition, by the time passes, I'd like to record my adventure and share my thoughts with people.

---

### Run locally
**NOTE**: We assume that you have PostgreSQL set and running.

Clone the repository:

    git clone https://github.com/Dositan/blog.git

Change directory, spawn virtual environment and install dependencies:

    cd blog
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

Setting configuration - Put these into `.env` file and replace with your own credits:

    FLASK_ENV=development
    FLASK_RUN_PORT=8000

    # Really Secret
    SECRET_KEY=SOMETHING_REALLY_SECRET

    # Database
    DEV_DATABASE_URL=postgresql://USER:PASSWORD@localhost/blog



Run app with:

    flask run
