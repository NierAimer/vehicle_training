import time


class Training(object):
    def __init__(self):
        self.set_environment()
        self.count_hit = 0
        self.count_stop = 0
        self.count_flameOut = 0
        self.pre_state = 'asleep'
        self.score_down = 0
        self.score_info = {}
        self.program_name = ''
        self.line_change_down = 0
        self.vehicle_stop_time = 0

        # 是否压实线
        self.wheel_hit_solid_line = False
        # 变道是否正确打转向灯
        self.cornering_lamp_check = True
        # 掉头是否打转向灯
        self.turn_around_check = True
        # 各个轮是否压虚线
        self.fl_hit = False
        self.bl_hit = False
        self.fr_hit = False
        self.br_hit = False
        # 是否正确减速
        self.speed_down = True

    # 获得扣分总数
    def get_total_sub_score(self):
        return self.score_down

    # 记录当前timestamp
    def set_environment(self, timestamp=1234567):
        self.timestamp = timestamp

    # 保存socketio 传入的data
    def set_data(self, data):
        self.data = data

    # 打印测试当前状态
    def print_state(self):
        print("current program : %s , current state : %s" % (self.__class__.__name__, self.state))

    # 打火状态判断
    def is_engine_start(self):
        return self.data['bEngineStart']

    # 熄火状态判断
    def is_engine_stop(self):
        self.running_check()  # 驾驶过程中状态判断
        # print(self.data['bFlameOut'])
        return self.data['bFlameOut']

    # 驾驶状态进入判断
    def is_running(self):
        if abs(self.data['Speed']) > 1.5:
            return True
        else:
            return False

    # 训练项目结束判断
    def is_program_end(self):
        return self.data['bProgramEnd']

    # 流程结束判断
    def is_framework_over(self):
        return True

    # 刹车停车
    def is_normal_stop(self):
        self.running_check()  # 驾驶过程中状态判断
        if abs(self.data['Speed']) < 0.1 and self.data['BrakePedalIntensity'] >= 0.7:
            self.vehicle_stop_time = int(round(time.time() * 1000))
            return True
        else:
            return False

    # 进入初始状态
    def on_enter_asleep(self):
        pass

    # 进入着车状态
    def on_enter_start(self):
        self.pre_state = self.state

    # 进入起步熄火状态
    def on_enter_startFlameOut(self):
        self.count_flameOut += 1
        self.pre_state = self.state

    # 进入驾驶状态(没有发生熄火，即手刹、档位、离合、刹车、油门均操作正确)
    def on_enter_running(self):
        pass

    # 进入驾驶过程中熄火状态
    def on_enter_runningFlameOut(self):
        self.count_flameOut += 1
        # print("驾驶过程中熄火状态判断完成！")
        self.pre_state = self.state

    # 进入停车状态
    def on_enter_stop(self):
        # print("停车")
        self.count_stop += 1
        self.pre_state = self.state

    # 进入停车熄火状态
    def on_enter_stopFlameOut(self):
        self.count_flameOut += 1
        # print("驾驶过程中熄火状态判断完成！")
        self.pre_state = self.state

    # 项目结束，由子类重写
    def on_enter_programEnd(self):
        self.pre_state = self.state
        # print("项目结束")

    # 流程结束
    def on_enter_final(self):
        pass
        # print("流程结束")

    # 驾驶过程中状态判断
    def running_check(self):
        # 碰撞检测
        if self.data['bVehicleBLWheelHit'] or self.data['bVehicleBRWheelHit'] or self.data['bVehicleFLWheelHit'] or \
                self.data['bVehicleFRWheelHit'] or self.data['bVehicleBodyHit']:
            self.count_hit += 1

        # 压实线判断
        if self.data['bWheelHitSolidLine']:
            self.wheel_hit_solid_line = True

        # 变道检测
        self.line_change_check()

        # 掉头检测(在掉头区)
        if self.data['bIsInTurnAroundArea']:
            if self.data['CorneringLampState'] != -1:
                self.turn_around_check = False


        # 人行横道线检测(在横道线上切未打右转灯)
        if self.data['bIsOnZebraCrossing'] and self.data['CorneringLampState'] != 1:
            if self.data['Speed'] > 30:
                print('Speed大于30!!!')
                self.speed_down = False

            if not self.data['bCanVehiclePassThrough']:
                print('闯红灯了!!!')
                self.speed_down = False

    def line_change_check(self):
        # 压虚线时间记录
        if self.data['bFLWheelHitDottedLine']:
            self.fl_hit = True
        if self.data['bBLWheelHitDottedLine']:
            self.bl_hit = True
        if self.data['bFRWheelHitDottedLine']:
            self.fr_hit = True
        if self.data['bBRWheelHitDottedLine']:
            self.br_hit = True
        # 向左变道
        if (self.fl_hit and self.bl_hit) and not (self.fr_hit and self.br_hit):
            print("Left")
            if self.data['CorneringLampState'] != -1:
                self.cornering_lamp_check = False
        # 向右变道
        if not (self.fl_hit and self.bl_hit) and (self.fr_hit and self.br_hit):
            print("Right")
            if self.data['CorneringLampState'] != 1:
                self.cornering_lamp_check = False
        # 变道完成
        if self.fl_hit and self.bl_hit and self.fr_hit and self.br_hit:
            self.fr_hit = False
            self.br_hit = False
            self.fl_hit = False
            self.bl_hit = False
            print("转向完成，time:", self.data['TimeStamp'])
            self.line_change_down = self.data['TimeStamp'] + 2000
        # 关灯
        if self.data['TimeStamp'] > self.line_change_down and self.line_change_down != 0:
            if self.data['CorneringLampState'] != 0:
                self.turn_around_check = False
                print("未关闭转向灯")
            self.line_change_down = 0
            print("转向灯关闭检测")
