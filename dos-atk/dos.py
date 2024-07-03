import asyncio
import httpx

num=1000

url = "https://moe-counter.glitch.me/get/@phi-plugin"

async def request_url():
    async with httpx.AsyncClient() as client:
        try:
             response = await client.get(url)
             print(response.status_code)  # 打印状态码
             if response.status_code == 429:  # 如果状态码为429
                 print("状态码429，暂停运行5分钟")  # 打印消息
                 await asyncio.sleep(300)  # 等待5分钟
        except Exception as e:
             print(e)
    await asyncio.sleep(0.1)  # 微小延迟

async def open_x_functions():
    while True:  # 无限循环
        tasks = []
        for _ in range(num):
            task = asyncio.create_task(request_url())
            tasks.append(task)
        await asyncio.gather(*tasks)
        print("已完成1000次请求，暂停60秒")  # 打印消息
        await asyncio.sleep(60)  # 每次请求1000次后等待60秒

# 运行异步函数
asyncio.run(open_x_functions())
