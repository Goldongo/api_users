![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

# api_users

Goldongo's API for handling user authentication.

## Dependencies

The API's dependencies can be found at the [requirements file](./requirements.txt), and they can be installed by running the following command:

```
pip3 install --no-input -r req.txt
```

## Usage

The program can be run by running:

```
uvicorn api_users.main:app
```

## Documentation

The API, built on the [FastAPI](https://fastapi.tiangolo.com) framework, uses [Swagger UI](https://swagger.io/tools/swagger-ui/) for endpoint documentation. It can be accesed using the `/docs` path.
