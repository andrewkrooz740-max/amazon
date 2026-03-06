# Luxury Feeling Collection - Django E-commerce

A premium home textiles e-commerce platform built with Django 5, featuring luxury bedding, bath linens, curtains, carpets, and decorative accents.

## Features

- **Product Catalog**: Browse products by category with filtering and search
- **Shopping Cart**: Session-based cart with add/remove/update functionality
- **Checkout**: Complete order flow with shipping information
- **User Accounts**: Registration, login, profile management, order history
- **Newsletter**: Email subscription system
- **Admin Panel**: Full Django admin for managing products, orders, and users
- **Responsive Design**: Mobile-first design with Tailwind CSS

## Tech Stack

- Python 3.12+
- Django 5.0
- SQLite (default) / PostgreSQL ready
- Tailwind CSS (CDN)
- WhiteNoise for static files

## Quick Start

### 1. Clone and Setup Virtual Environment

```bash
cd luxury_feeling_collection
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Load Sample Data (Optional)

```bash
python manage.py loaddata fixtures/initial_data.json
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the site.

## Admin Access

Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and login with your superuser credentials.

## Project Structure

```
luxury_feeling_collection/
├── manage.py
├── requirements.txt
├── fixtures/
│   └── initial_data.json
├── luxury_feeling_collection/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                    # Home page, search, static pages
├── shop/                    # Products and categories
├── cart/                    # Shopping cart
├── orders/                  # Checkout and order management
├── accounts/                # User authentication
├── newsletter/              # Email subscriptions
├── templates/
│   ├── base.html
│   ├── core/
│   ├── shop/
│   ├── cart/
│   ├── orders/
│   └── accounts/
└── static/
    └── css/
```

## Available URLs

| URL                      | Description          |
| ------------------------ | -------------------- |
| `/`                      | Home page            |
| `/shop/`                 | All products         |
| `/shop/<category-slug>/` | Products by category |
| `/shop/product/<slug>/`  | Product detail       |
| `/cart/`                 | Shopping cart        |
| `/checkout/`             | Checkout page        |
| `/accounts/login/`       | Login                |
| `/accounts/register/`    | Register             |
| `/accounts/profile/`     | User profile         |
| `/accounts/orders/`      | Order history        |
| `/search/`               | Search products      |
| `/admin/`                | Admin panel          |

## Environment Variables (Optional)

Create a `.env` file for custom settings:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgres://user:pass@localhost/dbname
```

## Switching to PostgreSQL

1. Install psycopg2:

```bash
pip install psycopg2-binary
```

2. Update `settings.py` DATABASES:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'luxury_feeling',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

3. Run migrations:

```bash
python manage.py migrate
```

## Production Deployment

1. Set `DEBUG=False` in settings
2. Configure `ALLOWED_HOSTS`
3. Set a strong `SECRET_KEY`
4. Configure static files with WhiteNoise (already set up)
5. Use a production database (PostgreSQL recommended)
6. Set up HTTPS

## Payment Integration (Mock)

The checkout currently uses a mock payment system. To integrate real payments:

1. **Stripe**: Install `stripe` package, add API keys to settings
2. **Flutterwave**: Install `flutterwave-python`, configure for African payments

## License

This project is for educational purposes.

---

Built with ❤️ by Luxury Feeling Collection
