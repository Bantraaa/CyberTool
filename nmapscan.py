import nmap
from apptools import screen

def nmap_menu():
    menu = """
    1- Port scanner
    2- Network scanner
    3- Menu
    """
    # To test the code you can check your own IP address in cmd with ipconfing command in windows
    # or  you can enter 127.0.0.1 (local host address)
    key = 1
    nm = nmap.PortScanner()
    while key == 1:
        m_input = int(input(menu))
        screen.clear()
        if m_input == 1: # Port scanner
            try:
                while True:
                        
                    print("Port scanning may take some time depends on number of scanned port and open ports")
                    print("Press 'ctrl+C' to stop scanning\n")
                    target_IP = str(input("Enter target IP address: ")) # Take target IP address
                    first_port = int(input("Enter the beginning port: ")) # Take port range from user
                    last_port = int(input("Enter the last port: "))
                    for i in range(first_port,last_port+1):
                        status = nm.scan(target_IP,str(i))["scan"][target_IP]["tcp"][i]["state"]
                        if status != "closed":
                            print(f"port {i} is {status}")
                    break
            except KeyboardInterrupt: # Stop the scanning and back to nmap_menu
                pass
        
        if m_input == 2: # Network scanner
            
            IP_range = str(input("Enter IP range (example 192.168.1.0/24 this will scan 192.168.1.0 to 192.168.1.255): ")) # Take IP range

            nm.scan(hosts= IP_range, arguments='-n -sP -PE -PA21,23,80,3389') # Scan IP range

            for host in nm.all_hosts(): # Print open IP addresses
                if nm[host].state() == 'up':
                    print('Found host: %s' % host)

        if m_input == 3: # Go back to menu
            key = 0
    else:
        screen.clear()
        return True