#coding:gbk
"""
���þ������㷨���з���
���ߣ�
���ڣ�
"""
import pandas as pd           # ������Ҫ�õĿ�
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sb
#%matplotlib inline
# ��������
df = pd.read_csv('frenchwine.csv')
df.columns = ['species', 'alcohol', 'malic_acid', 'ash', 'alcalinity ash','magnesium']
# �鿴ǰ5������
df.head()
print(df.head()) 
# �鿴����������ͳ����Ϣ
df.describe()
print(df.describe())

def scatter_plot_by_category(feat, x, y): #���ݵĿ��ӻ� 
    alpha = 0.5
    gs = df.groupby(feat)
    cs = cm.rainbow(np.linspace(0, 1, len(gs)))
    for g, c in zip(gs, cs):
        plt.scatter(g[1][x], g[1][y], color=c, alpha=alpha)

plt.figure(figsize=(20,5))
plt.subplot(131)
scatter_plot_by_category('species', 'alcohol', 'malic_acid')
plt.xlabel('alcohol')
plt.ylabel('malic_acid')
plt.title('species')
plt.show()

plt.figure(figsize=(20, 10)) #����seaborn���������Iris����ͬ����ͼ
for column_index, column in enumerate(df.columns):
    if column == 'species':
        continue
    plt.subplot(2, 3, column_index + 1)
    sb.violinplot(x='species', y=column, data=df)
plt.show()

# ���ȶ����ݽ����з֣������ֳ�ѵ�����Ͳ��Լ�
from sklearn.model_selection import train_test_split #����sklearn���н�����飬����ѵ�����Ͳ��Լ�
all_inputs = df[['alcohol','malic_acid',
                             'ash', 'alcalinity ash','magnesium']].values
all_species = df['species'].values

(X_train,
 X_test,
 Y_train,
 Y_test) = train_test_split(all_inputs, all_species, train_size=0.85,random_state=4)#80%������ѡΪѵ����

# ʹ�þ������㷨����ѵ��
from sklearn.tree import DecisionTreeClassifier #����sklearn���е�DecisionTreeClassifier������������
# ����һ������������
decision_tree_classifier = DecisionTreeClassifier()
# ѵ��ģ��
model = decision_tree_classifier.fit(X_train, Y_train)
# ���ģ�͵�׼ȷ��
print(decision_tree_classifier.score(X_test, Y_test)) 


# ʹ��ѵ����ģ�ͽ���Ԥ�⣬Ϊ�˷��㣬
# ����ֱ�ӰѲ��Լ�����������ó�������
a = np.array(X_test)
b = a.tolist()
b[0],b[1],b[2] =b[1],b[15],b[14]
X_test = np.array(b)
print(X_test[0:3])#����3�����ݽ��в��ԣ���ȡ3��������Ϊģ�͵������
list2 = model.predict(X_test[0:3])
list3 = np.array(list2)
list1 = list3.tolist()
for i in range(3):
	if i < 3:
		if (list1[0] == 'Zinfandel'):
			list1.remove('Zinfandel')
			list1.append('�ɷ���')
		elif (list1[0] == 'Syrah'):
			list1.remove('Syrah')
			list1.append('����')
		elif (list1[0] == 'Sauvignon'):
			list1.remove('Sauvignon')
			list1.append('��ϼ��')
print(list1)#������ԵĽ���������ģ��Ԥ��Ľ��
