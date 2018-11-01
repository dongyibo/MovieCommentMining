import json
import const
import re
import math

'''
数据与逻辑接口
'''


class File(object):

    @staticmethod
    def get_data():
        data = []
        f = open(const.CFPL_PATH, 'r')
        for line in f.readlines():
            dic = json.loads(line)
            id = dic['id']
            comment = dic['comment']
            data.append((id, comment))
        f.close()
        return data

    @staticmethod
    def get_data_without_id():
        data = []
        f = open(const.CFPL_PATH, 'r')
        for line in f.readlines():
            dic = json.loads(line)
            comment = dic['comment']
            data.append(comment)
        f.close()
        return data

    @staticmethod
    def count():
        sum = 0
        i = 0
        f = open(const.CFPL_PATH, 'r')
        for line in f.readlines():
            dic = json.loads(line)
            comment = dic['comment']
            l = len(comment.split())
            sum += l
            i += 1
            print(l)
        f.close()
        return sum / i

    @staticmethod
    def word():
        s = set()
        f = open(const.CFPL_PATH, 'r')
        for line in f.readlines():
            dic = json.loads(line)
            comment = dic['comment']
            tmp = set(comment.split())
            s |= tmp
        f.close()

        fw = open(const.CFPL_WORD_PATH, 'w')
        data = File.get_data_without_id()
        for word in s:
            # print(word)
            word_num = 0
            for token in data:
                tokens = token.split()
                for w in tokens:
                    if w == word:
                        word_num += 1
                        break

            tmp = (len(data) + 1) / word_num
            inverse_document_frequency = math.log(tmp, 2)
            content = word + ' ' + str(inverse_document_frequency)
            fw.write(content + '\n')
            print(word + ':' + str(inverse_document_frequency))
        fw.close()
        # return data
        # print(len(s))

    @staticmethod
    def get_word_dic():
        dic = {}
        f = open(const.CFPL_WORD_PATH, 'r')
        for line in f.readlines():
            tmp = line.strip().split(' ')
            dic[tmp[0]] = float(tmp[1])
        f.close()
        return dic

    @staticmethod
    def record_clusters(lis):
        f = open(const.CFPL_CLUSTER_PATH, 'w')
        for cluster in lis:
            s = ''
            for c in cluster:
                s += (str(c) + ' ')
            f.write(s.strip() + '\n')
        f.close()

    @staticmethod
    def get_cluster():
        fc = open(const.CFPL_PATH, 'r')
        contents = fc.readlines()
        fc.close()

        lis = []
        f = open(const.CFPL_CLUSTER_PATH, 'r')
        for line in f.readlines():
            l = []
            c = line.strip().split()
            for id in c:
                l.append([int(id), File.get_content_by_id(contents[int(id)])])
            lis.append(l)
        f.close()
        return lis

    @staticmethod
    def get_content_by_id(line):
        l = json.loads(line)
        return l['comment']

    @staticmethod
    def record_cluster_with_center(lis):
        f = open(const.CFPL_CLUSTER_CENTER_PATH, 'w')
        for cluster in lis:
            s = ''
            for c in cluster:
                s += (str(c) + ' ')
            f.write(s.strip() + '\n')
        f.close()

    @staticmethod
    def get_data_by_id(id):
        f = open(const.CFPL_PATH, 'r')
        line = f.readlines()[id]
        dic = json.loads(line)
        return dic['comment']

# l  =  File.get_cluster()
# for a in l:
#     for b in a:
#         print(b,end=' ')
#     print()
# ff.count()
# d = ff.get_word_dic()

# ff.word()
# print(ff.count())
# # for d in ff.get_data():
#     a=d[1].split()
#     print(a)
