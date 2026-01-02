# 🎬 Ngandus Media - Creative Studio Platform (South Africa)

**Ngandus Media** is a professional creative media studio based in South Africa, dedicated to helping content creators bring their vision to life.

## 🎯 What We Do

We provide comprehensive creative services for:

| Service | Description |
|---------|-------------|
| 📹 **Video Production** | YouTube content, podcasts, documentaries, and promotional videos |
| 📺 **TV Shows & Emissions** | Professional production for TV programs and web series |
| 📸 **Photo Shoots** | Studio photography, portraits, and professional headshots |
| 💒 **Weddings** | Complete wedding photography and videography coverage |
| 🎉 **Events** | Clubs, parties, corporate events, and celebrations |
| 🎬 **Films** | Short films, music videos, and cinema productions |
| 🎤 **Manifestations** | Concerts, festivals, and cultural events coverage |

---

## 🚀 Quick Start

### Backend Setup

```bash
cd Backend
python -m venv venv
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Access Admin: `http://localhost:8000/admin/`

### Frontend

Open `frontend/index.html` in your browser.

---

## 📂 Project Structure

```
NgandusMedia/
├── Backend/           # Django REST API
│   ├── content/       # Site content (hero, services, videos, etc.)
│   ├── bookings/      # Studio booking requests
│   └── contact/       # Contact messages & newsletter
├── frontend/          # HTML/CSS/JS website
└── README.md
```

## 🛠 Tech Stack

- **Backend**: Django 6.0, Django REST Framework
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Frontend**: HTML5, CSS3, Bootstrap, JavaScript

## 📡 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/admin/` | Admin panel |
| `/api/content/all/` | All site content |
| `/api/bookings/create/` | Submit booking |
| `/api/contact/send/` | Send message |

## 📄 License

Template by [Colorlib](https://colorlib.com) - CC BY 3.0
