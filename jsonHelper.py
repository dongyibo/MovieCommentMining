import json
import const


def pre_process():
    fr = open(const.CFPL_OLD_ID_PATH, 'r')
    fw = open(const.CFPL_PATH, 'w')
    i = 0
    for line in fr.readlines():
        dic = json.loads(line)
        comment = dic['comment']
        content = '{"id":' + str(i) + ',"comment": "' + comment + '"}'
        fw.write(content + '\n')
        i += 1
    fr.close()
    fw.close()


def map_id():
    fc = open(const.XYFYP_OLD_ID_PATH, 'r')
    contents = fc.readlines()
    fc.close()

    f = open(const.XYFYP_CLUSTER_CENTER_PATH, 'r')
    fw = open(const.XYFYP_CLUSTER_MAP_PATH, 'w')
    for line in f.readlines():
        c = line.strip().split()
        s = ''
        for id in c:
            s += str(json.loads(contents[int(id)])['_id'])+' '
        fw.write(s.strip() + '\n')
    f.close()
    fw.close()

map_id()
