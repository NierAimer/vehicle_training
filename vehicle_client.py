import time
import socket
import websocket
import data_to_trainging
from fbs import fbs_subscribe, fbs_login, fbs_vehicle_info, fbs_connect
import Hoevo.VehicleInfo
import Hoevo
import Hoevo.Payload
import Hoevo.PUBLISH
import Hoevo.PayloadType
import Hoevo.Any
import Hoevo.Msg
import Hoevo.Flag

IP = socket.gethostbyname(socket.gethostname())

model_object = None
program_num = -1
score = 100
websocket_connect = False


#解析fbs数据
def on_message(ws, data):
    buf = bytearray(data)
    msg = Hoevo.Msg.Msg.GetRootAsMsg(buf)
    #print("收到数据")
    flag_type = msg.FlagType()
    if flag_type == Hoevo.Flag.Flag().PUBLISH:
        #print("进入PUBLISH")
        publish = Hoevo.PUBLISH.PUBLISH()
        publish.Init(msg.Flag().Bytes, msg.Flag().Pos)
        payload_type = publish.PayloadType()
        if payload_type == Hoevo.PayloadType.PayloadType().FBS:
            #print("进入FBS")
            payload_data = publish.PayloadAsNumpy()
            new_buf = bytearray(payload_data)
            #print(new_buf)
            payload = Hoevo.Payload.Payload.GetRootAsPayload(new_buf)
            any_type = payload.AnyType()
            #print(int(any_type))
            if any_type == Hoevo.Any.Any().VehicleInfo:
                #print("收到VehicleInfo")
                vehicle_info = Hoevo.VehicleInfo.VehicleInfo()
                vehicle_info.Init(payload.Any().Bytes, payload.Any().Pos)
                VehicleInfo = fbs_vehicle_info.VehicleInfo()
                data = VehicleInfo.set_vehicle_info_to_data(vehicle_info)
                #print(data)
                VehicleInfo.parser_vehicle_info(vehicle_info)
                trainging = data_to_trainging
                trainging.vehicle_training(data)
            if any_type == Hoevo.Any.Any().ActorData:
                pass
                #print("收到ActorData")
            if any_type == Hoevo.Any.Any().Login:
                pass
                #print("收到Login")
            if any_type == Hoevo.Any.Any().Command:
                pass
                #print("收到Command")


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")
    global websocket_connect
    websocket_connect = False


def send_connect(ws):
    print("### send connect ###")
    connect = fbs_connect.SendConnect()
    connect.client_id = "vehicle_client"
    data = connect.send_fbs_connect()
    ws.send(data, 0x2)
    global websocket_connect
    websocket_connect = True
    time.sleep(2)
    send_login(ws)
    time.sleep(2)
    send_subscribe(ws)


def send_login(ws):
    print("### send login ###")
    login = fbs_login.SendLogin()
    login.client_id = "vehicle_client"
    login.ip = "127.0.0.1"
    data = login.send_fbs_login()
    ws.send(data, 0x2)


def send_subscribe(ws):
    print("### send subscribe ###")
    subscribe = fbs_subscribe.SendSubscribe()
    subscribe.topic = "server/#"
    subscribe.topic_1 = "server"
    subscribe.client_id = "vehicle_client"
    data = subscribe.send_subscribe()
    ws.send(data, 0x2)



def ws_connect():

    global websocket_connect
    if not websocket_connect:
        print("本机ip",IP)
        #websocket.enableTrace(True)
        ws = websocket.WebSocketApp("ws://127.0.0.1:4001/ws/",
                                    on_message=on_message,

                                    on_close=on_close)
        ws.on_open = send_connect

        ws.run_forever()
    else:
        print("已连接")
