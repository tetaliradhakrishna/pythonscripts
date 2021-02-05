import time

def check_pod_running_or_not(x):
	return x

while True:
    print("polling")
    time.sleep(10)
    pod_status = check_pod_running_or_not(1)
    print(pod_status)
    if pod_status:
	    print("success")
		
