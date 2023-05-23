import argparse
from scapy.all import *
import socket


class Sniffer:
    def __init__(self, args):
        self.args = args
        self.local_ip = self.get_local_ip()

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

        print("Protocol: {} SrcIP: {} SrcPrt: {} DstIP: {} DstPRT: {} {}".format(
            protocol, src_ip, src_port, dest_ip, dest_port, received_or_sent))
        # if (packet.haslayer(Raw)):
        #     print("Payload: {}".format(packet[Raw].load))
        # print(src_mac, dst_mac)
        # print("--------------------------------------------------")

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

    def get_local_ip(self):
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("8.8.8.8", 80))
        local_ip = temp_socket.getsockname()[0]
        temp_socket.close()
        return local_ip

    def sniff(self):
        sniff(iface=self.args.interface, prn=self.packet_handler, store=0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', default=False,
                        action='store_true', help='be more talkative')
    parser.add_argument('-i', '--interface', type=str,
                        required=True, help='network interface name')
    args = parser.parse_args()
    sniffer = Sniffer(args)

    print("Started Sniffing on interface {}".format(args.interface))
    sniffer.sniff()
