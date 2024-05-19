FROM python:3-slim
WORKDIR /goldongo
COPY req.txt .
RUN pip3 install --no-input -r req.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "api_users.main:app", "--host", "0.0.0.0", "--port", "8000"]
