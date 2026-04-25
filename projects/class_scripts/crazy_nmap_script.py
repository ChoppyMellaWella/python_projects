#!/usr/bin/python3
# note: before starting script- run:
# run this script with sudo
# msfdb init - initialize database
import os
import xml.etree.ElementTree as ET

# --- Scan type selection ---
scan_types = {
    1: '-sS',
    2: '-sT',
    3: '-sU',
    4: '-sV',
    5: '-O',
    6: '-A',
    7: '-sn',
    8: '-sN',
    9: '-sF',
    10: '-sX'
}

# --- Timing options ---
timing_types = {
    1: '-T0',
    2: '-T1',
    3: '-T2',
    4: '-T3',
    5: '-T4',
    6: '-T5'
}

def parse_nmap_xml(xml_file):
    """Extract hosts, ports, services, and versions from Nmap XML"""
    results = []

    tree = ET.parse(xml_file)
    root = tree.getroot()

    for host in root.findall('host'):
        addr = host.find('address')
        if addr is None:
            continue

        ip = addr.get('addr')
        services = []

        ports = host.find('ports')
        if ports is None:
            continue

        for port in ports.findall('port'):
            state = port.find('state')
            if state is None or state.get('state') != 'open':
                continue

            service = port.find('service')
            if service is None:
                continue

            name = service.get('name', '')
            product = service.get('product', '')
            version = service.get('version', '')

            full_service = " ".join(filter(None, [name, product, version]))
            services.append(full_service.strip())

        if services:
            results.append((ip, services))

    return results


try:
    # --- User input ---
    scan_choice = int(input(
        "Choose NMAP scan type:\n"
        "\tTCP SYN[1]\n\tTCP Connect[2]\n\tUDP Scan[3]\n\tVersion Detection[4]\n"
        "\tOS Detection[5]\n\tAggressive Scan[6]\n\tPing Scan[7]\n"
        "\tTCP NULL[8]\n\tTCP FIN[9]\n\tTCP Xmas[10]\n> "
    ))

    timing_choice = int(input(
        "Choose timing option:\n"
        "\tParanoid[1]\n\tSneaky[2]\n\tPolite[3]\n"
        "\tNormal[4]\n\tAggressive[5]\n\tInsane[6]\n> "
    ))

    target = input("Enter target ip/range (ex: 192.168.20.1-20): ")
    vuln_scan = input("Enable vulnerability scripts? (y/n): ").lower()

    st = scan_types.get(scan_choice)
    to = timing_types.get(timing_choice)

    if not st or not to:
        print("Invalid option selected.")
        exit(1)

    # --- File handling ---
    filename = target.replace('/', '_').replace('-', '_')
    xml_file = f"{filename}.xml"
    rc_file = f"{filename}.rc"

    # --- Build flags ---
    extra_flags = f"-oX {xml_file}"

    if st not in ['-sn', '-A', '-sV']:
        extra_flags += " -sV"

    if vuln_scan == 'y' and st != '-sn':
        extra_flags += " --script vuln"

    # --- Run Nmap ---
    command = f"nmap {target} {st} {to} {extra_flags}"
    print(f"\n[+] Running: {command}\n")
    os.system(command)

    # --- Parse results ---
    print("[+] Parsing Nmap XML results...")
    parsed_results = parse_nmap_xml(xml_file)

    # --- Generate Metasploit RC file ---
    with open(rc_file, "w") as f:
        f.write(f"db_import {xml_file}\n")
        f.write("hosts\nservices\nvulns\n")

        f.write("\necho ===== Targeted Exploit Searches =====\n")

        for ip, services in parsed_results:
            f.write(f"\necho --- Host: {ip} ---\n")

            for svc in services:
                # Avoid empty strings
                if not svc.strip():
                    continue

                # Escape quotes for msfconsole
                svc_clean = svc.replace('"', '')

                f.write(f"search type:exploit \"{svc_clean}\"\n")

    print(f"[+] Generated Metasploit resource script: {rc_file}")

    print("[+] Checking Metasploit database status...")

    status = os.system("msfdb status > /dev/null 2>&1")

    if status != 0:
        print("[+] Starting Metasploit database...")
        os.system("msfdb start")
    else:
        print("[+] Metasploit database already running.")

    # --- Launch Metasploit ---
    print("\n[+] Launching Metasploit...\n")
    os.system(f"msfconsole -r {rc_file}") 

except Exception as e:
    print(f"Error: {e}")