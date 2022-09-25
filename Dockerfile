FROM python:3.9-slim as builder

RUN export nproc=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \
    && apt-get update \
    && apt-get install --no-install-recommends -y \
        tree \
        curl

WORKDIR /app

COPY requirements.txt .

RUN pip install -r ./requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "scripts/manage.py runserver"]
