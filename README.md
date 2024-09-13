# basic-shop

A basic online shop with an API and front-end

# How to build and run

## Development

```bash
cd backend
python -m venv venv
venv/Scripts/Activate.ps1  # venv/bin/activate
pip install -e ".[linting]"
cd ../backend/src/basic_shop
python manage.py migrate
python manage.py runserver
# available on http://localhost:8000/api/products
# Run back end and front end in separate terminals
cd frontend
npm install
npm run build
npm run preview
# and go to http://localhost:4173
```

# Notice

This project has the following dependencies

- `Django`
- `djangorestframework`
- and others
