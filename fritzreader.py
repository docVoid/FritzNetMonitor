from fritzconnection.lib.fritzhosts import FritzHosts

def get_connected_devices():
    fh = FritzHosts(address='fritz.box', user='fritz6772', password='PASSWORD')
    connected = []
    for device in fh.get_hosts_info():
        if device.get("status") == "1":  
            connected.append({
                "name": device.get("name", "Unbekannt"),
                "ip": device.get("ip"),
                "mac": device.get("mac"),
                "interface": device.get("interface_type", "unbekannt")
            })
    return connected