# -- coding: utf-8 --
import math
from file import File

'''
向量空间模型
计算文本相似度
'''


class VSM(object):
    def __init__(self, is_customize=False):
        self.__is_customize = is_customize
        if not is_customize:
            self.__dic = File.get_word_dic()

    def import_sef_customize_data(self, data):
        datas = []
        for d in data:
            datas.append(d[1])
        self.__text_total_num = len(datas)
        self.__text_content = datas

    # 基于VSM计算余弦相似度
    def calculate_cos_similarity(self, text1, text2):
        token1 = text1.split()
        token2 = text2.split()
        # 获取所有词汇的集合
        a = set(token1)
        b = set(token2)
        len1 = len(a)
        len2 = len(b)
        if a - b == a if len1 <= len2 else b - a == b:
            return 0
        word_set = a
        word_set |= b
        dict1 = {}
        dict2 = {}
        # # 获取文本数量
        # text_total_num = get_text_total_num()
        # 计算TF-IDF
        for word in word_set:
            if self.__is_customize:
                inverse_document_frequency = self.__calculate_IDF_customize(word)
            else:
                inverse_document_frequency = self.__calculate_IDF(word)
            dict1[word] = self.__calculate_TF(word, token1) * inverse_document_frequency
            dict2[word] = self.__calculate_TF(word, token2) * inverse_document_frequency
            # print word,':',calculate_TF(word, token1),'  ',inverse_document_frequency
        # 余弦相似度计算
        numerator = 0
        w1, w2 = 0, 0
        for word in word_set:
            numerator += dict1[word] * dict2[word]
            w1 += dict1[word] * dict1[word]
            w2 += dict2[word] * dict2[word]
        denominator = math.sqrt(w1 * w2)
        cos = numerator / denominator
        print(cos)
        return cos

    # 计算TF
    def __calculate_TF(self, word, token):
        count = 0
        for w in token:
            if w == word:
                count += 1

        term_frequency = count / len(token)
        return term_frequency

    # 计算IDF
    def __calculate_IDF(self, word):
        return self.__dic[word]

    # 计算自定义IDF
    def __calculate_IDF_customize(self, word):
        # 包含单词的文本数目
        word_num = 0
        for token in self.__text_content:
            tokens = token.split()
            for w in tokens:
                if w == word:
                    word_num += 1
                    break

        tmp = (self.__text_total_num + 1) / word_num
        inverse_document_frequency = math.log(tmp, 2)
        return inverse_document_frequency

        # # 计算文本距离
        # def calculate_distance(text1, text2):
        #     return 1 - calculate_cos_similarity(text1, text2)

        # # 获取文本数量
        # def __get_text_total_num(self, category):
        #     return file.get_text_num(category)
        #
        # # 包含单词的文本数目
        # def __get_text_num_contain_word(self, word, category):
        #     return file.get_text_num_contain_word(word, category)


# print calculate_cos_similarity('我 喜欢 看 电视 不 喜欢 看 电影', '我 不 喜欢 看 电视 也 不 喜欢 看 电影')
a = [2831 ,3739]
x = File.get_data_by_id(a[0])
y = File.get_data_by_id(a[1])
#
a = VSM()
d = a.calculate_cos_similarity(x,y )
print(d)
