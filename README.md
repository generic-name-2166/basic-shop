# basic-shop

A basic online shop with an API and front-end

# How to build and run

## With Docker 

```bash
docker compose up --build
```

## Development

```bash
cd backend
python -m venv venv
venv/Scripts/Activate.ps1  # venv/bin/activate
pip install -e ".[linting]"
cd src/basic_shop
python manage.py migrate
python manage.py runserver
# available on http://localhost:8000/api/products
# Run back end and front end in separate terminals
cd frontend
npm install
npm run dev
# and go to http://localhost:5173
```

# Notice

This project has the following dependencies

- `Django`
- `djangorestframework`
- `caddy`
- and others
