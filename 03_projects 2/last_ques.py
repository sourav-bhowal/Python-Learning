import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "-- Wait time", wait_time)
    time.sleep(wait_time)   #system will sleep for 1 second
    wait_time = wait_time * 2   #increasing wait_time exponentially
    attempts += 1   #increment attempt by 1
