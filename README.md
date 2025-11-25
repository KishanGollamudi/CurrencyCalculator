# 💱 CurrencyCalculator – FastAPI + Neon UI

A simple and elegant currency conversion web app built using:
- Python 3
- FastAPI (Backend API)
- HTML + CSS + JavaScript (Frontend UI)
- Pytest (Unit testing)
- Docker ready
- CI/CD ready with GitHub Actions

---

## 🚀 Features

✔ Convert between 10 major world currencies  
✔ Neon-themed UI  
✔ FastAPI backend  
✔ REST API endpoints  
✔ Automated pytest  
✔ Ready for Sonar scan  
✔ Ready for Nexus storage  
✔ Ready for Docker Hub deployment  
✔ Can be served via Nginx / Apache / Cloudflare  

---

## 🧪 API Endpoints

### GET `/api/currencies`
Returns supported currencies:
```json
["USD","EUR","INR","JPY","GBP","AUD","CAD","CNY","AED","SGD"]

POST /api/convert

Example:

{
  "from_currency": "INR",
  "to_currency": "USD",
  "amount": 1000
}


Response:

{
  "converted_amount": 12.03,
  "from_currency": "INR",
  "to_currency": "USD",
  "amount": 1000
}

🧠 Running Locally
uvicorn app:app --reload


Open UI in browser:

http://localhost:8000

🧪 Run Tests
pytest

🐳 Docker Build
docker build -t currencycalculator .

Run
docker run -p 8000:8000 currencycalculator

🔥 CI/CD Pipeline

GitHub Actions automatically:
✔ installs dependencies
✔ runs pytest
✔ builds docker image
✔ pushes to DockerHub

🙌 Author

Created by Kishan Gollamudi
GitHub: https://github.com/KishanGollamudi
