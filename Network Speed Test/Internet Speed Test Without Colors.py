import speedtest
import socket
import time


IPaddress=socket.gethostbyname(socket.gethostname())
if IPaddress=="127.0.0.1":
    print(f"You are not connected to internet! Please check you connection.")
    time.sleep(6)
else:
    test = speedtest.Speedtest()

    print(f"Loading servers...")
    test.get_servers()
    print("Chosing best server...")
    best = test.get_best_server()
    print(f"Found: {best['host']} located in {best['name']}, {best['country']}")

    print()

    print(f"Performing download test...")
    download_result = round((test.download()/1024)/1024)

    print(f"Performing upload test...")
    upload_result = round((test.upload()/1024)/1024)

    print(f"Performing ping test...")
    ping_result = round(test.results.ping)

    print()
    print()

    print(f"Download speed is {download_result}MB/s")
    print(f"Upload speed is {upload_result}MB/s")
    print(f"ping is {ping_result}ms")
    time.sleep(10)

