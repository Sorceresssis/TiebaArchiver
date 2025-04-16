import asyncio
from typing import TypeVar, Callable, Awaitable

T = TypeVar("T")


# The Producer Consumer Pattern
class PCP:
    def __init__(
            self,
            queue_maxsize: int,
            producers_num: int,
            consumer_num: int,
            consumer_await_timeout: int,
            producer: Callable[[], Awaitable[T]],
            consumer: Callable[[T], Awaitable[None]],
    ) -> None:
        self.queue_maxsize = queue_maxsize
        self.producers_num = producers_num
        self.consumer_num = consumer_num
        self.consumer_await_timeout = consumer_await_timeout

        self.tasks_queue = asyncio.Queue(maxsize=queue_maxsize)
        self.running_producers = self.producers_num

        self.producer = producer
        self.consumer = consumer

    async def producer_task(self) -> None:
        while True:
            data = await self.producer()
            if data is None:
                break
            await self.tasks_queue.put(data)
        self.running_producers -= 1
        if self.running_producers == 0:
            for _ in range(self.consumer_num):
                await self.tasks_queue.put(None)

    async def consumer_task(self):
        while True:
            try:
                data = await asyncio.wait_for(self.tasks_queue.get(), self.consumer_await_timeout)
                await self.consumer(data)
            except asyncio.TimeoutError:
                if self.running_producers == 0:
                    break

    async def run(self) -> None:
        tasks = []
        for i in range(self.producers_num):
            tasks.append(asyncio.create_task(self.producer_task()))
        for i in range(self.consumer_num):
            tasks.append(asyncio.create_task(self.consumer_task()))
        await asyncio.gather(*tasks)

# TODO 不够自由， 改进代码
#
