FROM python3.10-slim

WORKDIR /app

COPY C:\Users\lecou\Projet+Mise+en+prod+-+home-credit-default-risk\requirements.txt .

RUN pip install -r requirements.txt

COPY C:\Users\lecou\Projet+Mise+en+prod+-+home-credit-default-risk .

EXPOSE 8000

CMD ["uvicorn", "Fastapi:app", "--host", "0.0.0.0", "--port", "80"]