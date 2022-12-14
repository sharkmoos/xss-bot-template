FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y wget &&  \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb

WORKDIR /tmp
COPY requirements.txt install_webdriver.py ./
RUN pip install -r requirements.txt

# easy way to install any webdriver for selenium
RUN python3 install_webdriver.py

WORKDIR /app
COPY src .

CMD ["python", "app.py"]
