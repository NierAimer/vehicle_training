import numpy as np
import importlib
import inspect
import state_trans
import training_item
from training_item.basemode import Training


# 加载训练项目判断规则类
def find_subclass(class_name):
    try:
        module = importlib.import_module(class_name)
        for x in dir(module):
            obj = getattr(module, x)
            if inspect.isclass(obj) and issubclass(obj, Training) and obj is not Training:
                return obj
    except ImportError:
        return None


model_object = None
program_num = -1
score = 100 # 初始成绩100分
connect = False


def vehicle_training(data):
    global score
    global program_num
    build_model(data)
    if model_object:
        model_object.set_environment(data['TimeStamp'])
        model_object.set_data(data)
        model_object.drive()
        print(model_object.state)
        if model_object.state == 'programEnd':
            score -= model_object.get_total_sub_score()#扣分
            score = max(score, 0)# 分数不低于0
            print("项目", program_num, "训练结束，得分：", score)
            # 重置
            program_num = -1 # 重置当前训练科目，否则，无法继续当前训练
            score = 100


# 定义如何加载判断规则
def build_model(data):
    global model_object
    global program_num
    # print(int(data['TrainingProgram']),program_num)
    # print(machine.models)
    # print(data['TrainingProgram'])
    if data['TrainingProgram'] != program_num:
        # print("新项目")
        model = find_subclass('training_item.training' + str(int(data['TrainingProgram'])))
        print(model)
        program_num = int(data['TrainingProgram'])
        if model:
            state_trans.machine.models.clear()
            model_object = model()
            state_trans.machine.add_model(model_object)
        else:
            model_object = None