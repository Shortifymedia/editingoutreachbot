# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files from repo to container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the bot (no Flask, no exposed port)
CMD ["python", "bot.py"]
