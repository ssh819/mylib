#coding=gbk
"""
ʵ�ֶԡ����������Ľֵ����ı��������ϵ����ȡ
�����ˣ���ʫ��
"""

import codecs
import jieba
import os
from jieba import posseg


class Earth(object):

    def __init__(self): # �����ֵ�
        self.names = {}        # ��ϵ�ֵ�
        self.relationships = {}# ÿ���������ϵ
        self.lineNames = []
def analyze_word(self):
        jieba.load_userdict("F:\��ѧ���������ʵ�鱨��\����4����ʫ������������9-2\name.txt")
        with codecs.open("F:\��ѧ���������ʵ�鱨��\����4����ʫ������������9-2\���������Ľֵ�.txt", "r", "utf-8") as f:
            for line in f.readlines(): # �ִʷ��ش���
                poss = posseg.cut(line) # Ϊ�¶�ȡ��һ����������ϵ
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
        with codecs.open("F:\��ѧ���������ʵ�鱨��\����4����ʫ������������9-2\���������Ľֵ�_node.csv", "w", "gbk") as f:
            f.write("Id Label Weight\r\n")
            for name, times in self.names.items():
                f.write(name + " " + name + " " + str(times) + "\r\n")

        # �����ϵ��(��)
        with codecs.open("F:\��ѧ���������ʵ�鱨��\����4����ʫ������������9-2\���������Ľֵ�_edge.csv", "w", "gbk") as f:
            f.write("Source Target Weight\r\n")
            for name, edge in self.relationships.items():
                for v, w in edge.items():
                    if w > 3:
                        f.write(name + " " + v + " " + str(w) + "\r\n")

