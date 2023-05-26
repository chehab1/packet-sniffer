import argparse
from scapy.all import *
import socket
import json


class Sniffer:
    def __init__(self, args):
        self.args = args
        self.local_ip = self.get_local_ip()
        self.index = 0
        self.running = False
        self.json_file_path = 'sniffed_pkts.json'
        with open(self.json_file_path, 'w') as file:
            file.write('[\n')

    def packet_handler(self, packet):
        if "IP" not in packet:
            return
        src_ip = ""
        dest_ip = ""
        src_port = 0
        dest_port = 0
        protocol = ""
        src_mac = ""
        dest_mac = ""
        received_or_sent = ""
        packet_load = ""

        # hexdump(packet)
        src_ip = packet["IP"].src
        dest_ip = packet["IP"].dst
        src_mac = packet["Ether"].src
        dest_mac = packet["Ether"].dst

        if src_ip == self.local_ip:
            received_or_sent = "Sent"
        else:
            received_or_sent = "Received"

        if "TCP" in packet:
            src_port, dest_port, protocol = self.TCP_packet_handler(packet)

        elif "UDP" in packet:
            src_port, dest_port, protocol = self.UDP_packet_handler(packet)

        packet_load = self.get_packet_load(packet)

        packet_record = {
            "no": self.index,
            "Protocol": protocol,
            "SrcIP": src_ip,
            "SrcPrt": src_port,
            "DstIP": dest_ip,
            "DstPrt": dest_port,
            "status": received_or_sent,
            "Info": {
                "Ethernet": {"dst": dest_mac,
                             "src": src_mac,
                             "type": "IPv4"
                             }
            },
            "Payload": str(packet_load)
        }
        with open(self.json_file_path, 'a') as file:
            file.write(json.dumps(packet_record))
            file.write(',\n')
        # time.sleep(0.3)
        print(self.index)
        self.index += 1

    def TCP_packet_handler(self, packet):
        source_port = packet["TCP"].sport
        destination_port = packet["TCP"].dport
        protocol = "TCP"
        return (source_port, destination_port, protocol)

    def UDP_packet_handler(self, packet):
        source_port = packet["UDP"].sport
        destination_port = packet["UDP"].dport
        protocol = "UDP"
        return (source_port, destination_port, protocol)

    def get_packet_load(self, packet):
        return packet["Raw"].load if "Raw" in packet else ""

    def get_local_ip(self):
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("8.8.8.8", 80))
        local_ip = temp_socket.getsockname()[0]
        temp_socket.close()
        return local_ip

    def start_sniffing(self, duration):
        self.running = True
        packet_capture_thread = threading.Thread(target=self.capture_packets)
        packet_capture_thread.start()

        time.sleep(duration)

        self.stop_sniffing()

    def capture_packets(self):
        while self.running:
            sniff(iface=self.args.interface,
                  prn=self.packet_handler, count=1, store=0)

    def stop_sniffing(self):
        #time.sleep(0.3)
        with open(self.json_file_path, 'a') as file:
            file.write(']')
        self.running = False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', type=str,
                        required=True, help='network interface name')
    args = parser.parse_args()
    sniffer = Sniffer(args)

    print("Started Sniffing on interface {}".format(args.interface))
    sniffer.start_sniffing(10)
