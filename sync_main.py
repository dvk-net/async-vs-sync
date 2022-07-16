from time import sleep, time


sensor_configs = [f"Sensor {i}" for i in range(30)]


def connect_to_sensor(config):
    sleep(0.5) # emulates network delay
    print(f"{config} is connected")
    return config

def poll_the_sensor(sensor):
    sleep(0.5) # emulates network delay
    print(f"{sensor} is ok")


def main():
    sensors = []
    # connect to all the sensors
    start_time = time()
    for sensor_config in sensor_configs:
        sensor = connect_to_sensor(sensor_config)
        sensors.append(sensor)
    connection_time = time() - start_time
    print(f"All sensors were connected in {connection_time} seconds.")
    
    while True:
        print(f"Start polling sensors...")
        start_time = time()
        for sensor in sensors:
            poll_the_sensor(sensor)
        poll_time = time() - start_time
        print(f"All sensors were polled in {poll_time} seconds.")


if __name__ == "__main__":
    main()