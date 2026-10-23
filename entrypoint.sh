#!/bin/bash

/bin/ollama serve &
pid=$!

sleep 5

echo "Retrieve glm-ocr:latest model..."
ollama pull glm-ocr:latest
echo "Done!"

wait $pid