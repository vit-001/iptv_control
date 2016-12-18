# -*- coding: utf-8 -*-
__author__ = 'Vit'


def parce_m3u(input_file,output_file):
    with open(input_file, 'r') as fd:
        channels=list()

        ch_name = ''
        num = 0
        for line in fd:
            if line.startswith('#EXTM3U'):
                pass
            elif line.startswith('#EXTINF:'):
                ch_name = line.rpartition(',')[2].strip()
            elif line.startswith('udp://'):
                ch_udp = line.strip()
                if ch_name.isdecimal():
                    n = int(ch_name)
                else:
                    n = -1

                if n != num:
                    print(ch_name, ch_udp)
                    channels.append(dict(name=ch_name,udp=ch_udp))
                num += 1
        # print(channels)

        with open(output_file,'w') as fd:
            for item in channels:
                fd.write('{0:<30} {1}\n'.format(item['name'],item['udp']))

def encode_m3u(txt_file,m3u_file):
    channels = list()
    with open(txt_file,'r') as fd:


        for line in fd:
            if line.strip() is '':
                continue
            if line.startswith('#'):
                continue

            split=line.partition('udp://')
            channels.append(dict(name=split[0].strip(),udp=split[1]+split[2].strip()))

    with open(m3u_file,'w') as fd:
        fd.write('#EXTM3U\n')
        for item in channels:
            print(item)
            fd.write('#EXTINF:-1,{0}\n'.format(item['name']))
            fd.write('{0}\n'.format(item['udp']))


if __name__ == "__main__":
    # parce_m3u('Z:/zbox/iptv/test.m3u','Z:/zbox/iptv/channels.txt')
    encode_m3u('Z:/zbox/iptv/zbox.txt','Z:/zbox/iptv/zbox.m3u')