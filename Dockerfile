FROM python:3.9.9-slim-bullseye

EXPOSE 8080

# Add Tini
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/local/bin/tini
RUN chmod +x /usr/local/bin/tini

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

# Use tini to avoid PID 1 responsibilities (https://hynek.me/articles/docker-signals/)
ENTRYPOINT [ "tini", "--", "python", "app.py" ]
