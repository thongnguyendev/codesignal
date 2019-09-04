def isIPv4Address(inputString):
    try:
        ips = list(map(int, inputString.split('.')))
        return len(ips) == 4 and max(*ips) <= 255 and min(*ips) >= 0
    except:
        return False
