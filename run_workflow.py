# @@@SNIPSTART python-geocode-tutorial-run-workflow
import asyncio

from workflow import GeoCode
from temporalio.client import Client


async def main():
    # Create a client connected to the server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    lat_long = await client.execute_workflow(
        GeoCode.run, id="geocode-workflow", task_queue="geocode-task-queue"
    )

    print(f"Lat long: {lat_long}")


if __name__ == "__main__":
    asyncio.run(main())
# @@@SNIPEND
