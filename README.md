#  Simple Device Monitor

A **Django-based web app** for monitoring network devices in real-time. Built with DevOps best practices in mind, t's Dockerized, CI/CD-ready, and perfect for portfolio showcasing!

---

##  Features

- Add and view network devices in a Bootstrap-styled dashboard.
- See each device’s IP, status (up/down), and last checked time.
- Clean, dark-themed UI using HTML + Bootstrap.
- Dockerized for easy container deployment.
- Environment variables managed via `.env` file.
- CI/CD-ready with GitHub Actions support.

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, Bootstrap 5
- **Database:** SQLite (PostgreSQL-ready)
- **Containerization:** Docker + Docker Compose
- **DevOps:** GitHub Actions for CI/CD
- **Static Files:** Managed with Django’s staticfiles system

---

<pre> ## 📁 Project Structure ``` simple-device-monitor/ ├── devices/ # Django app (views, models, templates) │ ├── templates/ │ │ └── devices/ │ │ └── dashboard.html │ ├── models.py │ ├── views.py │ ├── urls.py │ ├── admin.py │ └── ... ├── monitor/ # Django project settings ├── static/ # Static files (CSS, JS, images) ├── Dockerfile # Docker image config ├── docker-compose.yml # For running app + services ├── requirements.txt # Python dependencies ├── .env # Environment variables └── manage.py # Django CLI entry point ``` </pre>


---

## 🔧 How to Run It

### 🐳 Option 1: Using Docker

```bash
docker-compose up --build

Visit: http://localhost:8000


 Option 2: Without Docker (for development)
 # Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver

 .env File Example

 DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1

Future Improvements
Add Prometheus/Grafana for monitoring metrics

Switch to PostgreSQL for production

Add user authentication & access control

Email or Slack alerts for device downtime




