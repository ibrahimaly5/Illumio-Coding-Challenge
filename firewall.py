import csv
import ipaddress

class Firewall:
    def __init__(self, fileName):
        self.directions = set()
        self.protocols = set()
        self.ports = {}
        self.ipAddrs = {}
        self.allPorts = False
        self.allIpAddrs = False
        self.allDirs = False
        self.allProtocols = False
        self.zeroAddr = ipaddress.IPv4Address('0.0.0.0')
        self.lastAddr = ipaddress.IPv4Address('255.255.255.255')

        with open(fileName) as csv_File:
            csv_reader = csv.reader(csv_File)
            for row in csv_reader:
                self.directions.add(row[0])
                self.protocols.add(row[1])
                
                if (not self.allPorts):
                    portRange = row[2].split("-")
                    self.check_ports(portRange)

                if (not self.allIpAddrs):
                    ipAddressRange = row[3].split("-")
                    # ipAddress = ipaddress.IPv4Address(row[3])
                    self.check_adresses(ipAddressRange)
                
                if (len(self.directions) == 2):
                    self.allDirs = True
                if (len(self.protocols) == 2):
                    self.allProtocols = True

                if (1 in self.ports):
                    if (self.ports[1] == 65535):
                        self.allPorts = True
                
                if (self.zeroAddr in self.ipAddrs):
                    if (self.ipAddrs[self.zeroAddr] == self.lastAddr):
                        self.allIpAddrs = True
                
                if (self.allDirs and self.allIpAddrs and self.allPorts and self.allProtocols):
                    break
    
    
    def check_ports(self, portRange):
        portsToDel = []
        if (len(portRange) > 1):
            fromPort = int(portRange[0])
            toPort = int(portRange[1])
            if fromPort in self.ports:
                self.ports[fromPort] = max(self.ports[fromPort], toPort)
            else:
                self.ports[fromPort] = toPort
                for port in self.ports:
                    if (fromPort < port < toPort):
                        self.ports[fromPort] = max(toPort, self.ports[port])
                        portsToDel.append(port)
                    elif (port < fromPort < self.ports[port]):
                        self.ports[port] = max(toPort, self.ports[port])
                        portsToDel.append(fromPort)
            
            if (fromPort == 1 and toPort == 65535):
                self.allPorts = True
        else:
            port = int(portRange[0])
            for fromPort in self.ports:
                if (port >= fromPort and port <= self.ports[fromPort]):
                    return
            self.ports[port] = port
    
        for port in portsToDel:
            del self.ports[port]

    def check_adresses(self, ipAddressRange):
        addressesToDel = []
        if (len(ipAddressRange) > 1):
            fromAddr = ipaddress.IPv4Address(ipAddressRange[0])
            toAddr = ipaddress.IPv4Address(ipAddressRange[1])
            if fromAddr in self.ipAddrs:
                self.ipAddrs[fromAddr] = max(self.ipAddrs[fromAddr], toAddr)
            else:
                self.ipAddrs[fromAddr] = toAddr
                for address in self.ipAddrs:
                    if (fromAddr < address < toAddr):
                        self.ipAddrs[fromAddr] = max(toAddr, self.ipAddrs[address])
                        addressesToDel.append(address)
                    elif (address < fromAddr < self.ipAddrs[address]):
                        self.ipAddrs[address] = max(toAddr, self.ipAddrs[address])
                        addressesToDel.append(fromAddr)
            if (fromAddr == self.zeroAddr and toAddr == self.lastAddr):
                self.allIpAddrs = True
        else:
            address = ipaddress.IPv4Address(ipAddressRange[0])
            for fromAddr in self.ipAddrs:
                if (address >= fromAddr and address <= self.ipAddrs[fromAddr]):
                    return
            self.ipAddrs[address] = address
        
        for address in addressesToDel:
            del self.ipAddrs[address]

    def accept_packet(self, direction, protocol, port, ipAddr):
        address = ipaddress.IPv4Address(ipAddr)
        inDirection = False
        inProtocol = False
        inPort = False
        inAddress = False
        
        if (self.allDirs):
            inDirection = True
        if (self.allProtocols):
            inProtocol = True
        if (self.allPorts):
            inPort = True
        if (self.allIpAddrs):
            inAddress = True
    
        if (not inDirection and direction in self.directions):
            inDirection = True
        if (not inProtocol and protocol in self.protocols):
            inProtocol = True
        if (not inPort):
            for fromPort in self.ports:
                if (fromPort <= port <= self.ports[fromPort]):
                    inPort = True
                    break
        if (not inAddress):
            for fromAddress in self.ipAddrs:
                if (fromAddress <= address <= self.ipAddrs[fromAddress]):
                    inAddress = True
                    break

        return (inAddress and inDirection and inPort and inProtocol)


if __name__ == "__main__":
    fw = Firewall("file1.csv")
    print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
    print(fw.accept_packet("inbound", "udp", 53, "192.168.2.1"))
    print(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"))