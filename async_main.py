import asyncio
from time import sleep, time



sensor_configs = [f"Sensor {i}" for i in range(30)]


async def connect_to_sensor(config):
    await asyncio.sleep(0.5) # emulates network delay
    print(f"{config} is connected")
    return config

async def poll_the_sensor(sensor):
    await asyncio.sleep(0.5) # emulates network delay
    print(f"{sensor} is ok")
    return f"{sensor} is ok"


async def main():
    connect_tasks = []
    # connect to all the sensors
    start_time = time()
    for sensor_config in sensor_configs:
        poll_task = asyncio.create_task(connect_to_sensor(sensor_config))
        connect_tasks.append(poll_task)
    sensors = await asyncio.gather(*connect_tasks)
    connection_time = time() - start_time
    print(f"All sensors were connected in {connection_time} seconds.")
    
    while True:
        print(f"Start polling sensors...")
        poll_tasks = []
        start_time = time()
        for sensor in sensors:
            poll_task =  asyncio.create_task(poll_the_sensor(sensor))
            poll_tasks.append(poll_task)
        poll_results = await asyncio.gather(*poll_tasks)
        poll_time = time() - start_time
        print(f"All sensors were polled in {poll_time} seconds.")


if __name__ == "__main__":
    asyncio.run(main())