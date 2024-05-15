FROM python:3-slim
WORKDIR /goldongo
RUN pip3 install --no-input -r req.txt

COPY . .
CMD ["uvicorn", api_users.main:app"]
