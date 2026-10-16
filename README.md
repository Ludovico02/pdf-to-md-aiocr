# PDF to Markdown Service

Developing a PDF to markdown converter using GLM-OCR. The end goal is to install this service in a small server where multiple clients can send their PDF file and get the markdown version of it.

## Run the code

To run the code (in the current state)

``` sh
uvicorn app.main:app --reload
```

## Test the API endpoints

[localhost/docs](http://127.0.0.1:8000/docs)

## Used dependencies

Check [requirements](requirements.txt)

## Docker

In the current state I'm using ollama instead of vLLM for testing. My school laptop doesn't have a nvidia graphics card. I'm using ollama both because it can work without GPU but also because it's easier to setup on WSL and it uses the same OpenAI-compatible REST API.

1. Start the container

```sh
docker compose up -d
```

2. Pull the LLM model for testing

I first tested the code with qwen3 0.6b parameters because it's a very small model

```sh
docker exec -it ollama-ocr ollama pull qwen3:0.6b
```

3. Check the logs

```sh
docker compose logs -f ollama-ocr
```

## Issues

- GLM-OCR does not support italian, for now I will still build it using it

## License
[Apache License Version 2.0, January 2004](./LICENSE)