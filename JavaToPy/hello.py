import json
import time
from numpy import *
import lightgbm as lgb
import numpy as np
from py4j.clientserver import ClientServer, JavaParameters, PythonParameters


class Demo(object):
    count = 0
    total_time = 0

    def timeclear(self):
        self.count = 0
        self.total_time = 0

    def timeaverage(self):
        print(self.total_time)
        return self.total_time * 1e3 / self.count

    def predict_proba1(self, x_val_in):
        """
        :param x_val_in: Java传入的字节数组
        :return: 返回给java的字符串
        """
        x_val_byte = json.loads(x_val_in)
        start = time.time()
        b = np.array(x_val_byte).reshape(1, 200)
        y_pared_val = model.predict_proba(b, pred_contrib=True).tolist()
        end = time.time()
        y_pared_val_bate = json.dumps(y_pared_val)
        self.total_time += end - start
        self.count += 1

        return y_pared_val_bate

    class Java:
        implements = ["main/java/jty.Predict_Proba"]


train_X = np.array(np.random.randint(0, 10, size=200000).reshape(1000, 200))
train_y = np.array(np.random.randint(0, 2, size=1000))
test_X = np.array(np.random.randint(0, 10, size=800).reshape(4, 200))

model = lgb.LGBMClassifier(boosting_type='gbdt',  # 提升树的类型
                           metric='auc',  #
                           num_leaves=31,  # 树的最大叶子数
                           reg_alpha=0.25,  # L1正则化系数
                           reg_lambda=0.25,  # L2正则化系数
                           max_depth=-1,  # 最大树的深度
                           n_estimators=30000,  # 拟合的树的棵树，相当于训练轮数
                           subsample=0.75,  # 训练样本采样率 行
                           colsample_bytree=0.75,  # 训练样本采样率 列
                           subsample_freq=1,  # 子样本频率
                           learning_rate=0.03,  # 学习率
                           min_child_weight=10,  # 分支节点的最小权重
                           random_state=2019,  # 随机种子数
                           n_jobs=8, )
model.fit(train_X, train_y)
print("f")
demo = Demo()

gateway = ClientServer(
    java_parameters=JavaParameters(),
    python_parameters=PythonParameters(),
    python_server_entry_point=demo)
