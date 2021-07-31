from transitions import Machine


states = ['asleep', 'start', 'startFlameOut', 'running', 'runningFlameOut', 'stop', 'stopFlameOut', 'programEnd', 'finish']

machine = Machine(states=states, initial='asleep')

# 点火
machine.add_transition('drive', 'asleep', 'start', conditions='is_engine_start')

# 起步熄火
machine.add_transition('drive', 'start', 'startFlameOut', conditions='is_engine_stop')
# 起步
machine.add_transition('drive', 'start', 'running', conditions='is_running')

# 行驶中熄火
machine.add_transition('drive', 'running', 'runningFlameOut', conditions='is_engine_stop')
# 停车
machine.add_transition('drive', 'running', 'stop', conditions='is_normal_stop')
# 项目训练结束
machine.add_transition('drive', 'running', 'programEnd',conditions='is_program_end')

# 停车后熄火
machine.add_transition('drive', 'stop', 'stopFlameOut', conditions='is_engine_stop')
# 重新起步
machine.add_transition('drive', 'stop', 'running', conditions='is_running')

# 项目训练结束
machine.add_transition('drive', 'startFlameOut', 'programEnd',conditions='is_program_end')
machine.add_transition('drive', 'runningFlameOut', 'programEnd',conditions='is_program_end')
machine.add_transition('drive', 'stopFlameOut', 'programEnd',conditions='is_program_end')
machine.add_transition('drive', 'asleep', 'programEnd',conditions='is_program_end')
machine.add_transition('drive', 'start', 'programEnd',conditions='is_program_end')
machine.add_transition('drive', 'stop', 'programEnd',conditions='is_program_end')

# 流程结束
machine.add_transition('drive', 'programEnd', 'finish',conditions="is_framework_over")
machine.add_transition('drive', 'finish', 'finish')

