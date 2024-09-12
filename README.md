# basic-shop

A basic online shop with an API and front-end

# How to build and run

## Development

```bash
cd backend
python -m venv venv
venv/Scripts/Activate.ps1  # venv/bin/activate
pip install -e ".[linting]"
# ...
cd src/basic_shop
python manage.py runserver
```

# Notice

This project has the following dependencies

- `Django`
- `djangorestframework`
- and others
