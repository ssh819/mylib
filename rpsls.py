#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ���ʫ��
���ڣ�2019.11.14
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
   """
    ����Ϸ�����Ӧ����ͬ������
   """
   if name=="ʯͷ":
      return 0
   elif name=="ʷ����":
      return 1
   elif name=="ֽ":
      return 2
   elif name=="����":
      return 3
   elif name=="����":
      return 4
   
       
    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


   pass #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
   """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
   """
   if number==0: 
       return "ʯͷ"
   elif number==1:
       return "ʷ����"
   elif number==2 :
       return "ֽ"
   elif number==3:
       return "����"
   elif number==4:
       return "����"
          
   
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

   pass #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    print("--------") # ���"-------- "���зָ�
   # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
    
    player_choice_number = name_to_number(player_choice)# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
   
    comp_number = random.randrange(0,4)    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    comp_choice = number_to_name(comp_number)  # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    print("����ѡ��Ϊ��{}".format(player_choice))
    print("�������ѡ��Ϊ��{}".format(comp_choice))    # ����Ļ����ʾ�����ѡ����������
    
    
    if comp_number==player_choice_number:        # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
       print("���ͼ��������һ����")
    elif comp_number==0 and (player_choice_number==1 or player_choice_number==2):
       print("��Ӯ��")
    elif comp_number==1 and (player_choice_number==2 or player_choice_number==3):
       print("��Ӯ��")
    elif comp_number==2 and (player_choice_number==3 or player_choice_number==4):
       print("��Ӯ��")
    elif comp_number==3 and (player_choice_number==0 or player_choice_number==4):
       print("��Ӯ��")
    elif comp_number==4 and (player_choice_number==0 or player_choice_number==1):
       print("��Ӯ��")
    elif player_choice_number==0 and (comp_number==1 or comp_number==2):
       print("�����Ӯ��")
    elif player_choice_number==0 and (comp_number==2 or comp_number==3):
       print("�����Ӯ��")
    elif player_choice_number==0 and (comp_number==3 or comp_number==4):
       print("�����Ӯ��")
    elif player_choice_number==0 and (comp_number==0 or comp_number==4):
       print("�����Ӯ��")
    elif player_choice_number==0 and (comp_number==0 or comp_number==1):
       print("�����Ӯ��")
    elif player_choice_number!=0 or player_choice_number!=1 or player_choice_number!=2 or player_choice_number!=3 or player_choice_number!=4:
        print("Error: No Correct Name")
    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    pass #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)

