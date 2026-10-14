from ollama import ChatResponse, Client

client = Client(host="http://localhost:11434")

question = str(input("<- What is your question? "))

response: ChatResponse = client.chat(
    model="qwen3:0.6b",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

print(f"-> {response.message.content}\n--- Total duration: {response.total_duration}\n--- Tokens used: {response.eval_count + response.prompt_eval_count}")