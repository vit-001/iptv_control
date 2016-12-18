# -*- coding: utf-8 -*-
__author__ = 'Vit'

if __name__ == "__main__":

    file=open("out/test.m3u",mode='w')
    file.write('#EXTM3U\n')
    for i in range(256):
        # print(i)
        file.write('#EXTINF:-1,')
        file.write(str(i))
        file.write('\n')

        file.write('udp://@233.166.172.')
        file.write(str(i))
        file.write(':1234\n')

    file.close()