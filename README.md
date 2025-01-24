# Creating LiteLLM Container

This repository is an educational project designed to teach developers how to build and run a lightweight REST API for LiteLLM using Docker containers. It provides a step-by-step guide to containerizing a Flask application that interfaces with OpenAI and Anthropic models.

---

## Features

- **Dynamic Model Selection**: Supports both OpenAI and Anthropic models based on user input.
- **Environment Configuration**: Utilizes a `.env` file for securely managing API keys.
- **Fully Dockerized**: Simplifies deployment and scalability with Docker containers.
- **Educational Focus**: Aimed at teaching developers modern AI integration and containerization techniques.

---

## Prerequisites

1. **Docker**: Install Docker on your system. [Download Docker](https://www.docker.com/get-started)
2. **API Keys**: Obtain API keys for:
   - [OpenAI](https://platform.openai.com/signup/)
   - [Anthropic](https://www.anthropic.com/)

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/creating-litellm-container.git
cd creating-litellm-container
```

### 2. Create a `.env` File
Create a `.env` file in the root directory to securely store your API keys:
```bash
touch .env
```

Add the following content to your `.env` file:
```
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
```

### 3. Build the Docker Image
Build the Docker container using the provided `Dockerfile`:
```bash
docker build -t litellm-container .
```

### 4. Run the Docker Container
Start the container with the `.env` file:
```bash
docker run -d -p 8080:8080 --env-file .env litellm-container
```

---

## Usage

### Test the API with `curl`

#### OpenAI Model Example
```bash
curl -X POST http://localhost:8080/completion \
-H "Content-Type: application/json" \
-d '{
  "model": "openai/gpt-4o",
  "messages": [{ "role": "user", "content": "Hello, how are you?" }]
}'
```

#### Anthropic Model Example
```bash
curl -X POST http://localhost:8080/completion \
-H "Content-Type: application/json" \
-d '{
  "model": "anthropic/claude-3-sonnet-20240229",
  "messages": [{ "role": "user", "content": "What are the benefits of AI in business?" }]
}'
```

### Expected Response
```json
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "AI provides benefits such as automation, better decision-making, and improved customer experiences."
      }
    }
  ]
}
```

---

## Educational Goals

This project is designed to help developers learn:
1. How to interface with large language models programmatically.
2. Best practices for building and deploying REST APIs using Flask.
3. Secure management of API keys using `.env` files.
4. Containerization techniques with Docker.

---

## Troubleshooting

### Common Issues

1. **Missing API Keys**:
   - Ensure `OPENAI_API_KEY` and `ANTHROPIC_API_KEY` are correctly set in the `.env` file or passed as environment variables.

2. **Docker Not Running**:
   - Verify that Docker is installed and running:
     ```bash
     docker info
     ```

3. **Check Container Logs**:
   - If the container doesn't work as expected, inspect the logs:
     ```bash
     docker logs <container-id>
     ```

---

## Contributing

We welcome contributions to improve this educational project. Feel free to submit pull requests or open issues for feedback or enhancements.

---

## License

This project is licensed under the [MIT License](LICENSE).

---
