import os

'''
定义一些常量
'''
BASE_DIR = os.path.dirname(__file__)[:len(os.path.dirname(__file__)) - 5] + '/venv/file'


XYFYP_OLD_ID_PATH = os.path.join(BASE_DIR, 'xyfyp2.json')
XYFYP_PATH = os.path.join(BASE_DIR, 'xyfyp3.json')
CFPL_OLD_ID_PATH = os.path.join(BASE_DIR, 'cfpl2.json')
CFPL_PATH = os.path.join(BASE_DIR, 'cfpl3.json')
XYFYP_WORD_PATH = os.path.join(BASE_DIR, 'xyfyp_word.txt')
CFPL_WORD_PATH = os.path.join(BASE_DIR, 'cfpl_word.txt')
XYFYP_CLUSTER_PATH = os.path.join(BASE_DIR, 'xyfyp_cluster_0.7.txt')
XYFYP_CLUSTER_CENTER_PATH = os.path.join(BASE_DIR, 'xyfyp_cluster_center.txt')
XYFYP_CLUSTER_MAP_PATH = os.path.join(BASE_DIR, 'xyfyp_cluster_map.txt')
CFPL_CLUSTER_PATH = os.path.join(BASE_DIR, 'cfpl_cluster_0.7.txt')
CFPL_CLUSTER_CENTER_PATH = os.path.join(BASE_DIR, 'cfpl_cluster_center.txt')
CFPL_CLUSTER_MAP_PATH = os.path.join(BASE_DIR, 'cfpl_cluster_map.txt')

# print(str(os.path.dirname(__file__)))
# print(BASE_DIR)c