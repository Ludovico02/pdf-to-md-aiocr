import asyncio
import time

import httpx

URL = "http://localhost:8000/pdfToMarkdown/?download=false"
PDF_PATH = "../sample.pdf"
CONCURRENT_USERS = 4


async def simulate_user(client: httpx.AsyncClient, user_id: int, pdf_bytes: bytes):
    start = time.perf_counter()
    print(f"[User {user_id}] Sending PDF...")
    files = {"file": (f"user_{user_id}.pdf", pdf_bytes, "application/pdf")}
    response = await client.post(URL, files=files, timeout=300.0)
    elapsed = time.perf_counter() - start
    print(f"[User {user_id}] Status: {response.status_code} | Took: {elapsed:.2f}s")
    return response.status_code, elapsed


async def main():
    with open(PDF_PATH, "rb") as f:
        pdf_bytes = f.read()

    async with httpx.AsyncClient() as client:
        tasks = [
            simulate_user(client, i, pdf_bytes) for i in range(1, CONCURRENT_USERS + 1)
        ]
        results = await asyncio.gather(*tasks)

    successes = sum(1 for status, _ in results if status == 200)
    print(f"\nCompleted: {successes}/{CONCURRENT_USERS} succeeded.")


if __name__ == "__main__":
    asyncio.run(main())
