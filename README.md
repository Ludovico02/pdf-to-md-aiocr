# PDF to Markdown Service

Developing a PDF to markdown converter using GLM-OCR. The end goal is to install this service in a small server where multiple clients can send their PDF file and get the markdown version of it.

py --version
Python 3.13.15

## TODO

- [ ] Type annotations
- [ ] CLI Version
- [ ] Testing
- [ ] Dockerfile

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

6. Check the logs if needed:

``` bash
docker compose logs -f ollama-ocr
```

## License
[Apache License Version 2.0, January 2004](./LICENSE)
