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

## Issues

- GLM-OCR does not support italian, for now I will still build it using it

## License
[Apache License Version 2.0, January 2004](./LICENSE)