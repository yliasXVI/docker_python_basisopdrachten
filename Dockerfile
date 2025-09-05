FROM python:3.12

WORKDIR /app

# Installeer mysql connector
RUN pip install --no-cache-dir mysql-connector-python

# Eventueel requirements.txt support (optioneel)
COPY requirements.txt ./
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi
