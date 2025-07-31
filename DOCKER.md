# 🐳 Docker Guide

This guide explains how to run the Bukowski 3D application using Docker.

## Quick Start

### Build the Image

```bash
docker build -t bukowski_3d .
```

### Run Different Interfaces

#### Streamlit Web App (Port 8501)
```bash
docker run --rm -p 8501:8501 bukowski_3d streamlit
```
Access at: http://localhost:8501

#### Gradio Web App (Port 7860)
```bash
docker run --rm -p 7860:7860 bukowski_3d gradio
```
Access at: http://localhost:7860

#### Command Line Interface
```bash
docker run --rm bukowski_3d cli
```

## Using Docker Compose

### Run Streamlit Web App
```bash
docker-compose --profile web up streamlit
```

### Run Gradio Web App
```bash
docker-compose --profile web up gradio
```

### Run CLI
```bash
docker-compose --profile cli up cli
```

### Development Mode (with hot reload)
```bash
docker-compose --profile dev up dev
```

## Environment Variables

### OpenAI API Key
To use OpenAI embeddings, set your API key:

```bash
export OPENAI_API_KEY="sk-your-api-key"
docker run --rm -e OPENAI_API_KEY bukowski_3d streamlit
```

Or with docker-compose:
```bash
export OPENAI_API_KEY="sk-your-api-key"
docker-compose --profile web up streamlit
```

## Volume Mounts

### Output Directory
Mount a local directory to save generated HTML files:

```bash
docker run --rm -v $(pwd)/output:/app/output bukowski_3d cli
```

### Development with Hot Reload
Mount the entire project for development:

```bash
docker run --rm -v $(pwd):/app -p 8501:8501 bukowski_3d streamlit
```

## Docker Compose Profiles

- `web`: Streamlit and Gradio services
- `cli`: Command line interface
- `dev`: Development environment with volume mounts

## Troubleshooting

### Port Already in Use
If port 8501 or 7860 is already in use, map to different ports:

```bash
docker run --rm -p 8502:8501 bukowski_3d streamlit
```

### Permission Issues
The container runs as a non-root user. If you encounter permission issues:

```bash
docker run --rm -u root bukowski_3d streamlit
```

### View Logs
```bash
docker logs <container_id>
```

## Production Deployment

For production deployment, consider:

1. Using a reverse proxy (nginx)
2. Setting up SSL certificates
3. Using Docker secrets for API keys
4. Implementing health checks
5. Setting resource limits

Example production docker-compose:

```yaml
version: '3.8'
services:
  streamlit:
    build: .
    ports:
      - "8501:8501"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 1G
          cpus: '0.5'
```