# basic-shop

A basic online shop with an API and front-end

# How to build and run

## Development

```bash
cd backend
python -m venv venv
venv/Scripts/Activate.ps1  # venv/bin/activate
pip install -e ".[linting]"
cd ../frontend
bun install
bun run build
cd ../backend/src/basic_shop
python manage.py migrate
python manage.py runserver
# and go to http://localhost:8000/api/products
```

To develop the front end

```bash
# Run Django dev server in another terminal
cd backend
venv/Scripts/Activate.ps1
cd src/basic_shop
python manage.py runserver
#---#
cd frontend
bun run dev
# and go to http://localhost:5173
```

# Notice

This project has the following dependencies

- `Django`
- `djangorestframework`
- and others
