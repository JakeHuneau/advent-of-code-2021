from functools import reduce

class BitStream:
    def __init__(self, fp):
        self.bit_stream = [int(i, 16) for i in open(fp).readline().strip()]
        self.bits = self.bit_generator()
        self.location = 0

    def bit_generator(self):
        for v in self.bit_stream:
            for bit in range(4):
                yield (v >> (3 - bit)) & 1

    def get_bit(self):
        self.location += 1
        return next(self.bits)

    def get_bits(self, n, binary_str=True):
        value = ''.join(str(self.get_bit()) for _ in range(n))
        if binary_str:
            return value
        return int(value, 2)

    def get_version(self):
        return self.get_bits(3)

    def get_type(self):
        return self.get_bits(3)

    def get_literal(self):
        value = ''
        last_value = 1
        while last_value == 1:
            last_value = self.get_bit()
            value += self.get_bits(4)
        return int(value, 2)

    def get_operator(self):
        length_type = self.get_bit()
        packets = []
        if length_type == 0:
            sub_packets_len = self.get_bits(15, False)
            start_location = self.location
            while True:
                packets.append(self.get_packet())
                if self.location >= start_location + sub_packets_len:
                    break
        else:
            num_sub_packets = self.get_bits(11, False)
            for _ in range(num_sub_packets):
                packets.append(self.get_packet())
        return packets

    def get_packet(self):
        version = self.get_bits(3, False)
        packet_type = self.get_bits(3, False)
        if packet_type == 4:
            # literal
            return version, packet_type, self.get_literal()
        else:
            # Operator
            return version, packet_type, self.get_operator()

    def get_packets(self):
        packets = []
        while True:
            try:
                packets.append(self.get_packet())
            except RuntimeError:
                return packets


def get_version_sum(version_sum, packets):
    for packet in packets:
        version_sum += packet[0]
        if packet[1] != 4:
            version_sum = get_version_sum(version_sum, packet[2])
    return version_sum


def get_packet_value(packet):
    match packet[1]:
        case 0:
            # sum
            return sum(get_packet_value(p) for p in packet[2])
        case 1:
            # product
            return reduce(lambda a, b: a * get_packet_value(b), packet[2], 1)
        case 2:
            # min
            return min(get_packet_value(p) for p in packet[2])
        case 3:
            # max
            return max(get_packet_value(p) for p in packet[2])
        case 4:
            # literal
            return packet[2]
        case 5:
            # greater than
            return 1 if get_packet_value(packet[2][0]) > get_packet_value(packet[2][1]) else 0
        case 6:
            # less than
            return 1 if get_packet_value(packet[2][0]) < get_packet_value(packet[2][1]) else 0
        case 7:
            # equals to
            return 1 if get_packet_value(packet[2][0]) == get_packet_value(packet[2][1]) else 0


def solve():
    bit_stream = BitStream('../input/day16')
    packets = bit_stream.get_packets()
    return get_version_sum(0, packets), get_packet_value(packets[0])