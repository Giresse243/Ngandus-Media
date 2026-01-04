🎬 Ngandus Media – Studio Booking Platform

Ngandus Media is a creative media studio platform designed to support content creators, YouTubers, and digital artists in Africa.
The platform allows users to discover studio services, send booking requests, and contact the studio team, with future plans for online payments and user accounts.

🚀 Project Goals

Present Ngandus Media as a professional creative studio

Allow creators to request studio bookings online

Receive and manage client messages

Build a scalable backend for future features (payments, user accounts, dashboards)

🛠 Tech Stack
Backend

Django – Core backend framework

Django REST Framework – API development

PostgreSQL (production) / SQLite (development)

Django Admin – Internal management

Frontend

HTML5

CSS3

Bootstrap 5

JavaScript

📂 Project Structure
ngandus-media/
│
├── backend/
│   ├── config/              # Django project settings
│   ├── bookings/            # Booking management
│   ├── contact/             # Contact messages
│   ├── studio/              # Services, prices, images
│   ├── users/               # (Future) User accounts
│   ├── media/               # Uploaded images & files
│   ├── static/              # Static files
│   └── manage.py
│
├── frontend/
│   ├── index.html
│   ├── services.html
│   ├── booking.html
│   ├── contact.html
│   └── assets/
│
├── README.md
└── requirements.txt

📅 Core Features (MVP)

Studio service presentation

Booking request form

Contact form

Admin dashboard for managing requests

Image and content management

🔮 Future Features

Online payments (Paystack, Flutterwave, Payoneer)

User accounts (creators & admins)

Real-time availability calendar

Email notifications

Community features for creators

AI-assisted content tools