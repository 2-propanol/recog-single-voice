import socket

from termcolor import cprint


HOST = "localhost"
PORT = 10500


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT))
    except ConnectionRefusedError as e:
        cprint("Could not connected to julius.", color="red")
        print("Run 'sh julius-start.sh'.")
        return 1

    data = ""
    cprint("Connected to julius.", color="green")

    try:
        while True:
            if "</RECOGOUT>\n." in data:
                spoken = ""
                for line in data.split("\n"):
                    index = line.find('WORD="')
                    if index != -1:
                        line = line[index + 6 : line.find('"', index + 6)]
                        spoken += str(line)

                print("Detected: " + spoken)
                if "録画開始" in spoken:
                    cprint("Sent recode start signal.", color='cyan')
                elif "録画終了" in spoken:
                    cprint("Sent recode stop signal.", color='magenta')

                data = ""

            else:
                data += str(sock.recv(1024).decode("utf-8"))

    except KeyboardInterrupt:
        cprint("\nKeyboardInterrupt", color='red')
        sock.close()


if __name__ == "__main__":
    main()
