import asyncio


async def worker(name, queue):
  while True:
    try:
      sleep_for = await queue.get()
      print("sleepfor: ", sleep_for)
      
      await asyncio.sleep(sleep_for)
      
      queue.task_done()
      
      print(f'{name} has slept for {sleep_for:.2f} seconds')
    except asyncio.QueueShutDown as e:
      raise asyncio.QueueShutDown("Queue shut down when empty or shut down immediately:", e)
    
async def main():
  queue = asyncio.Queue()
  
  task = asyncio.create_task(worker("worker", queue))
  await queue.put(task)
  print(f"Queued <{task}>")
    
  await queue.join()
  
asyncio.run(main())