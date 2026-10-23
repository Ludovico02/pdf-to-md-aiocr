# PDF to Markdown Service

Developing a PDF to markdown converter using GLM-OCR. The end goal is to install this service in a small server where multiple clients can send their PDF file and get the markdown version of it.

py --version
Python 3.13.15

## TODO

- [ ] Type annotations
- [ ] CLI Version
- [ ] Testing

## Dev

I'm using `python 3.13.15`

You need to have `python 3.13`  and `docker` installed in your system.

1. Setup the python environment

``` bash
python -m venv .venv
```

2. Install all dependencies, check [requirements](requirements.txt)

``` bash
pip install -r requirements.txt
```

3. Run the docker compose

If you are on a device without a dedicated Nvidia GPU run:

``` bash
docker compose up -d
```

If you have one run

``` bash
docker compose -f docker-compose.yml -f docker-compose.gpu.yml up -d
```

4. Run the code

``` bash
# /app
uvicorn main:app --reload
```

5. Test it on [localhost/docs](http://127.0.0.1:8000/docs)

### Update Requirements



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

## License
[Apache License Version 2.0, January 2004](./LICENSE)