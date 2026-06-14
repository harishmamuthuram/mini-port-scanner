import socket
import time


def banner():
    print("=" * 50)
    print("            MINI PORT SCANNER")
    print("=" * 50)


def resolve_target(target):
    try:
        return socket.gethostbyname(target)

    except socket.gaierror:
        return None


def validate_port(port):
    return 1 <= port <= 65535


def get_service(port):

    try:
        return socket.getservbyport(port)

    except:
        return "Unknown"


def scan_port(target_ip, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(0.5)

    result = sock.connect_ex((target_ip, port))

    sock.close()

    return result == 0


def save_results(target, target_ip, open_ports, elapsed_time):

    with open("results.txt", "w") as file:

        file.write("PORT SCAN REPORT\n")
        file.write("=" * 40 + "\n")

        file.write(f"Target: {target}\n")
        file.write(f"IP Address: {target_ip}\n\n")

        file.write("OPEN PORTS\n")
        file.write("-" * 20 + "\n")

        for port, service in open_ports:
            file.write(f"Port {port} - {service}\n")

        file.write("\n")
        file.write(f"Scan Time: {elapsed_time:.2f} seconds\n")

    print("\nResults saved to results.txt")


def perform_scan(target_ip, start_port, end_port):

    open_ports = []

    print("\nScanning...\n")

    for port in range(start_port, end_port + 1):

        if scan_port(target_ip, port):

            service = get_service(port)

            print(f"[OPEN] Port {port:<5} Service: {service}")

            open_ports.append((port, service))

    return open_ports


def display_summary(open_ports, elapsed_time):

    print("\n" + "=" * 50)

    print("              SCAN SUMMARY")

    print("=" * 50)

    print(f"Open Ports Found : {len(open_ports)}")

    print(f"Scan Duration    : {elapsed_time:.2f} seconds")


def main():

    banner()

    target = input("Enter IP Address or Hostname: ")

    target_ip = resolve_target(target)

    if target_ip is None:

        print("Invalid target.")

        return

    try:

        start_port = int(input("Start Port: "))
        end_port = int(input("End Port: "))

    except ValueError:

        print("Ports must be numbers.")

        return

    if not validate_port(start_port):

        print("Invalid start port.")

        return

    if not validate_port(end_port):

        print("Invalid end port.")

        return

    if start_port > end_port:

        print("Start port must be smaller than end port.")

        return

    start_time = time.time()

    open_ports = perform_scan(
        target_ip,
        start_port,
        end_port
    )

    end_time = time.time()

    elapsed_time = end_time - start_time

    display_summary(
        open_ports,
        elapsed_time
    )

    save_results(
        target,
        target_ip,
        open_ports,
        elapsed_time
    )


if __name__ == "__main__":
    main()