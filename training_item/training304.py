from training_item.basemode import Training

# 直角转弯


class Training304(Training):
    def __init__(self):
        super().__init__()
        print("直角转弯")
        self.program_name = '直角转弯'
        self.score_info['车轮轧道路边缘城'] = 0
        self.score_info['转弯时不使用或错误使用转同灯，转弯后不关闭转向灯'] = 0
        self.score_info['中途停车时间超过2s'] = 0

    def on_enter_running(self):
        super().on_enter_running()
        if not self.turn_around_check:
            self.score_down += 10
            print("转弯时不使用或错误使用转同灯，转弯后不关闭转向灯,扣10分")
            self.score_info['转弯时不使用或错误使用转同灯，转弯后不关闭转向灯'] = 10

    def on_enter_programEnd(self):
        super(Training304, self).on_enter_programEnd()
        if self.count_hit > 0:
            self.score_down += 100
            print("车轮轧道路边缘城，扣100分")
            self.score_info['车轮轧道路边缘城'] = 100




