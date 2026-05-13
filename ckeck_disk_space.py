#!/usr/bin/env python3

import shutil
import sys
import socket


def main():

    checks = [
            (check_root_full, "Root partition full"),
            (check_no_network, "No working network."),
            ]
            
    for check, msg in checks:
        if check():
            print(msg)
            sys.exit(1)

    # Check for at least 2 GB and 10% free
    if not check_disk_usage(disk="/", min_gb=2, min_percent=10):
        print("ERROR: Not enough disk space.")
        sys.exit(1)

    print("Everything ok.")
    sys.exit(0)




def check_disk_usage(disk, min_gb, min_percent):
    """Returns True if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    
    print(f"Free: {du.free}")
    print(f"Total: {du.total}")
    print(f"Gigabytes_free: {gigabytes_free}")
    print(f"2**30: {2**30}")
    print("MADE BY EXPERIMENTAL --------------------------")    
    print("MADE BY EXPERIMENTAL2 OOOOOOOOOKKKKKKKKKKKKKKKKKKKKKK !!!!!!!!!!!!! :)))))))")    
    
    if percent_free < min_percent or gigabytes_free < min_gb:
        return False
    return True

 

def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_usage(disk="/", min_gb=2, min_percent=10)

def check_no_network():
    """Returns True if it fails to resolve Google's URL, False otherwise."""    
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True

main()
