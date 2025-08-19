# @@@SNIPSTART python-geocode-tutorial-run-worker
import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from activities import get_address_from_user, get_api_key_from_user, get_lat_long
from workflow import GeoCode


async def main():

    client = await Client.connect("localhost:7233", namespace="default")

    worker = Worker(
        client,
        task_queue="geocode-task-queue",
        workflows=[GeoCode],
        activities=[get_address_from_user, get_api_key_from_user, get_lat_long],
    )

    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
# @@@SNIPEND
