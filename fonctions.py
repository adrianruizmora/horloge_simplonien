import time

def clock():
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    return result
