# PDF to Markdown Service

## Run the code

To run the code (in the current state)

``` sh
uvicorn app.main:app --reload
```

## Used dependencies

``` sh
pip install fastapi uvicorn python-multipart aiofiles
```

I am using vLLM in order to use a GLM-OCR local installation

``` sh
uv pip install vllm --torch-backend auto
```

## Docker

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