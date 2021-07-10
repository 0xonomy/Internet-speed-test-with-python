import speedtest
import socket
import time


class bcolors:
    green = '\033[92m'
    yellow = '\033[33m'
    cyan = '\033[36m'
    reset = '\033[0m' # This resets color of next line to default


IPaddress=socket.gethostbyname(socket.gethostname())
if IPaddress=="127.0.0.1":
    print(f"{bcolors.yellow}You are not connected to internet! Please check you connection.{bcolors.reset}")
    time.sleep(6)
else:
    test = speedtest.Speedtest()

    print(f"{bcolors.cyan}Loading servers...")
    test.get_servers()
    print("Chosing best server...")
    best = test.get_best_server()
    print(f"Found: {best['host']} located in {best['name']}, {best['country']}{bcolors.reset}")

    print()

    print(f"{bcolors.yellow}Performing download test...{bcolors.reset}")
    download_result = round((test.download()/1024)/1024)

    print(f"{bcolors.yellow}Performing upload test...{bcolors.reset}")
    upload_result = round((test.upload()/1024)/1024)

    print(f"{bcolors.yellow}Performing ping test...{bcolors.reset}")
    ping_result = round(test.results.ping)

    print()
    print()

    print(f"{bcolors.green}Download speed is {download_result}MB/s")
    print(f"Upload speed is {upload_result}MB/s")
    print(f"ping is {ping_result}ms{bcolors.reset}")
    time.sleep(10)

