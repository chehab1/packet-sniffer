import argparse
from scapy.all import *
import socket
import json
import csv


class Sniffer:
    def __init__(self, interface, list_of_packets):
        # print(interface)
        self.interface = interface
        self.local_ip = self.get_local_ip()
        self.index = 0
        self.running = False
        self.json_file_path = 'sniffed_pkts.json'
        self.csv_file_path = 'sniffed_pkts.csv'
        self.list_of_packets = list_of_packets
        with open(self.json_file_path, 'w') as file:
            file.write('[\n')
        with open(self.csv_file_path, 'w') as file:
            file.write(
                'no, Protocol, SrcIP, SrcPrt, DstIP, DstPrt, status, dst, src, type, Payload\n')

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

        self.packet_to_json(protocol, src_ip, src_port, dest_ip,
                            dest_port, received_or_sent, src_mac, dest_mac, packet_load)

        self.packet_to_csv(self.index, protocol, src_ip, src_port, dest_ip,
                           dest_port, received_or_sent, src_mac, dest_mac, "IPv4", packet_load)
        self.index += 1
        # print(self.index)
        # time.sleep(0.2)

    def packet_to_json(self, *args):
        packet_record = {
            "no": self.index,
            "Protocol": args[0],
            "SrcIP": args[1],
            "SrcPrt": args[2],
            "DstIP": args[3],
            "DstPrt": args[4],
            "status": args[5],
            "Info": {
                "Ethernet": {"dst": args[7],
                             "src": args[6],
                             "type": "IPv4"
                             }
            },
            "Payload": str(args[8])
        }
        self.list_of_packets.append(packet_record)
         
        with open(self.json_file_path, 'a') as file:
            file.write(json.dumps(packet_record))
            file.write(',\n')

    def packet_to_csv(self, *args):
        with open(self.csv_file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(args)

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
        # time.sleep(duration)
        self.stop_sniffing()

    def capture_packets(self):
        while self.running:
            sniff(iface=self.interface,
                  prn=self.packet_handler, count=100, store=0)

    def stop_sniffing(self):
        self.running = False
        # time.sleep(3)
        with open(self.json_file_path, 'a') as file:
            file.write(']')


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-i', '--interface', type=str,
#                         required=True, help='network interface name')
#     args = parser.parse_args()
#     sniffer = Sniffer(args)

#     print("Started Sniffing on interface {}".format(args.interface))
#     sniffer.start_sniffing(10)
