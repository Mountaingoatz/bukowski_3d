# Use Python 3.11 slim as base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create a non-root user for security
RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app /app
USER app

# Expose ports for web applications
EXPOSE 8501 7860

# Create entrypoint script
RUN echo '#!/bin/bash\n\
case "$1" in\n\
  "streamlit")\n\
    exec streamlit run gui/streamlit_app.py --server.port=8501 --server.address=0.0.0.0\n\
    ;;\n\
  "gradio")\n\
    exec python gui/gradio_app.py\n\
    ;;\n\
  "cli")\n\
    exec python -m bukowski_3d.main\n\
    ;;\n\
  *)\n\
    echo "Usage: docker run <image> [streamlit|gradio|cli]"\n\
    echo "  streamlit - Run Streamlit web app on port 8501"\n\
    echo "  gradio    - Run Gradio web app on port 7860"\n\
    echo "  cli       - Run command-line interface"\n\
    exit 1\n\
    ;;\n\
esac' > /app/entrypoint.sh && chmod +x /app/entrypoint.sh

# Set default command
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["streamlit"]
