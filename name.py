#coding=gbk
"""
实现对《黎明破晓的街道》文本中人物关系的提取
制作人：宋诗涵
"""

import codecs
import jieba
import os
from jieba import posseg


class Earth(object):

    def __init__(self): # 姓名字典
        self.names = {}        # 关系字典
        self.relationships = {}# 每段内人物关系
        self.lineNames = []
def analyze_word(self):
        jieba.load_userdict("F:\大学计算机基础实验报告\电信4班宋诗涵大计算机基础9-2\name.txt")
        with codecs.open("F:\大学计算机基础实验报告\电信4班宋诗涵大计算机基础9-2\黎明破晓的街道.txt", "r", "utf-8") as f:
            for line in f.readlines(): # 分词返回词性
                poss = posseg.cut(line) # 为新读取的一段添加人物关系
                self.lineNames.append([])
                for w in poss:
                    # print("%s:%s" % (w.word, w.flag))
                    if w.flag != "nr" or len(w.word) < 2:
                        continue
                    self.lineNames[-1].append(w.word)
                    if self.names.get(w.word) is None:
                        self.names[w.word] = 0
                        self.relationships[w.word] = {}
                    self.names[w.word] += 1
def analyze_relationship(self):
        for line in self.lineNames:
            for name1 in line:
                for name2 in line:
                    if name1 == name2:
                        continue
                    if self.relationships[name1].get(name2) is None:
                        self.relationships[name1][name2] = 1
                    else:
                        self.relationships[name1][name2] += 1
def generate_gephi(self):
        with codecs.open("F:\大学计算机基础实验报告\电信4班宋诗涵大计算机基础9-2\黎明破晓的街道_node.csv", "w", "gbk") as f:
            f.write("Id Label Weight\r\n")
            for name, times in self.names.items():
                f.write(name + " " + name + " " + str(times) + "\r\n")

        # 人物关系边(边)
        with codecs.open("F:\大学计算机基础实验报告\电信4班宋诗涵大计算机基础9-2\黎明破晓的街道_edge.csv", "w", "gbk") as f:
            f.write("Source Target Weight\r\n")
            for name, edge in self.relationships.items():
                for v, w in edge.items():
                    if w > 3:
                        f.write(name + " " + v + " " + str(w) + "\r\n")

