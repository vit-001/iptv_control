__author__ = 'Vit'

def getchannellist (filename):
    list=[]
    for s in open(filename):
        list+=[s.rstrip()]
    return list

def parcem3u (filename):
    udp_list={}
    f = open(filename)
    for s in f:
        if s.startswith('#EXTM3U'):continue
        if s.startswith('#EXTINF:'):
            chanel=s.rstrip().split(',')[1]
            udp=f.readline().rstrip()
            udp_list[chanel]=udp
    f.close()
    return udp_list

def m3utochanellist (filename):
    list=[]
    f = open(filename)
    for s in f:
        if s.startswith('#EXTM3U'):continue
        if s.startswith('#EXTINF:'):
            chanel=s.rstrip().split(',')[1]
            list+=[chanel]
    f.close()
    return list


def savepartialplaylist(chanellist,fullplaylist,filename):
    f=open(filename,'w')
    f.write('#EXTM3U\n')
    for chanel in chanellist:
        if chanel=='':
            f.write('\n')
            continue
        f.write('#EXTINF:-1,'+chanel+'\n')
        f.write(fullplaylist[chanel]+'\n')
    f.close()

# получить из инета новый плейлист
from urllib.request import urlretrieve
urlretrieve('http://iptv.smart/Playlist.m3u','new_playlist.m3u')

# проверить на появление новых/пропадание старых каналов
playlist=parcem3u('new_playlist.m3u')
oldchannellist=getchannellist('chanels.txt')

newchannel=list([x for x in playlist.keys() if x not in oldchannellist])
lostchanel=list([x for x in oldchannellist if x not in playlist.keys()])

print('Новые каналы   ',newchannel)
print('Утеряны каналы ',lostchanel)

# спросить "перезаписываем списки каналов и плейлист"
ans=input('Перезаписываем списки каналов и плейлист? (y/n) ')

# если да, то переписываем
if ans=='y':
    print ('Перезаписываем...')
    urlretrieve('http://iptv.smart/Playlist.m3u','playlist.m3u')
    playlist=parcem3u('playlist.m3u')
    chanellist=m3utochanellist('playlist.m3u')
    f=open('chanels.txt','w')
    for s in chanellist:
        f.write(s+'\n')
    f.close()

# загрузить список плейлистов
for s in open('playlists.txt'):
    filename=s.rstrip()
    print('Записываем плейлист '+filename+'.m3u')

# создаем плейлисты из списка
    savepartialplaylist(getchannellist(filename+'.txt'),playlist,'out/'+filename+'.m3u')

input('Нажмите Enter для выхода')

