from fbs import fbs_subscribe, fbs_login, fbs_connect
import time
import websocket
import flatbuffers
import Hoevo
import Hoevo.VehicleInfo
import Hoevo.Any
import Hoevo.Msg
import Hoevo.Payload
import Hoevo.PayloadType
import Hoevo.Login
import Hoevo.Project
import Hoevo.PUBLISH
import Hoevo.Role
import Hoevo.QoS
import Hoevo.Flag


def set_vehicle_info_to_data():
    data = {
        'uuid': "test_data",
        'player_id': "test_data",
        'device_id': "test_data",
        'bEngineStart': False,
        'bHandBrake': False,
        'ClutchIntensity': 0.5,
        'BrakePedalIntensity': 1,
        'ThrottleIntensity': 0.5,
        'bSafetyBelt': False,
        'CurrentGear': 1,
        'bAddGearByDegrees': False,
        'bSubGearByDegrees': False,
        'CorneringLampState': 1,
        'bHorn': False,
        'bDoubleFlash': False,
        'SteeringWheelAngle': 0.5,
        'Speed': 0.0,
        'TrainingProgram': 304,
        'TimeStamp': 1234567,
        'bVehicleBodyHit': False,
        'bVehicleFLWheelHit': True,
        'bVehicleFRWheelHit': False,
        'bVehicleBLWheelHit': False,
        'bVehicleBRWheelHit': False,
        'bProgramEnd': False,
        'bFlameOut': False,
        'ReverseParkingLeftCount': 1,
        'ReverseParkingRightCount': 1,
        'bParkingTrace': False,
        'bIsInParkingArea': False,
        'PassThroughCheckpointCount': 2,
        'bIsPassingThroughCheckpoint': False,
        'bBridge1': False,
        'bBridge2': False,
        'bBridge3': False,
        'bBridge4': False,
        'bRampParking1': False,
        'bRampParking2': False,
        'RPM': 1,
        'bIsOnZebraCrossing': False,
        'bCanVehiclePassThrough': False,
        'bFLWheelHitDottedLine': False,
        'bFRWheelHitDottedLine': False,
        'bBLWheelHitDottedLine': False,
        'bBRWheelHitDottedLine': False,
        'bWheelHitSolidLine': False,
        'bIsInTurnAroundArea': False,
        'bWiperOn': False,
        'bIsHeadLightsOn': False,
        'WiperState': 2,
        'HeadlightsState': 1,
        'bFogLampOn': False,
        'bWidthIndicator': False,
        'bLimitDoorCheckPoint': False,
        'bHitPeopleOrCar': False,
        'bEmergencyOperation': False,
        'EmergencyTraining': 23,
        'bOnRightRoad': False,
        'bRunOverbedgeOfTheRoad': False,
        'bDrivingThroughRollingRoad': False,
        'bStopOnEmergencyVehicleLane': False,
        'bAboutToLeaveTheTunnel': False,
        'bDecelerateWithinTheSpecifiedRange': False,
        'bTurnAccordingToTheRules': False,
        'bGearOperationCorrect': False,
        'bStopInFiftyCm': False,
        'bStopInThirtyCm': False,
        'bAlternateUseLight': False,
        'bTurnAfterThreeSecond': False,
        'bActiveGuidancePracticeSuccessed': False,
        'bTurnAroundStep1': False,
        'bTurnAroundStep2': False,
        'bTurnAroundStep3': False,
        'bTurnAroundStep4': False
    }

    builder = flatbuffers.Builder(flatbuffers.Builder.MAX_BUFFER_SIZE)
    topic_string = builder.CreateString(str("server"))
    device_uuid = builder.CreateString(str("vehicle_client_test"))
    uuid = builder.CreateString(str(data['uuid']))
    player_id = builder.CreateString(str(data['player_id']))
    device_id = builder.CreateString(str(data['device_id']))



    Hoevo.VehicleInfo.VehicleInfoStart(builder)
    Hoevo.VehicleInfo.VehicleInfoAddUuid(builder, uuid)
    Hoevo.VehicleInfo.VehicleInfoAddPlayerId(builder, player_id)
    Hoevo.VehicleInfo.VehicleInfoAddDeviceId(builder, device_id)
    Hoevo.VehicleInfo.VehicleInfoAddEngineStart(builder, data['bEngineStart'])
    Hoevo.VehicleInfo.VehicleInfoAddHandBrake(builder, data['bHandBrake'])
    Hoevo.VehicleInfo.VehicleInfoAddClutchIntensity(builder, data['ClutchIntensity'])
    Hoevo.VehicleInfo.VehicleInfoAddBrakePedalIntensity(builder, data['BrakePedalIntensity'])
    Hoevo.VehicleInfo.VehicleInfoAddThrottleIntensity(builder, data['ThrottleIntensity'])
    Hoevo.VehicleInfo.VehicleInfoAddSafetyBelt(builder, data['bSafetyBelt'])
    Hoevo.VehicleInfo.VehicleInfoAddCurrentGear(builder, data['CurrentGear'])
    Hoevo.VehicleInfo.VehicleInfoAddAddGearByDegrees(builder, data['bAddGearByDegrees'])
    Hoevo.VehicleInfo.VehicleInfoAddCorneringLampState(builder, data['CorneringLampState'])
    Hoevo.VehicleInfo.VehicleInfoAddHorn(builder, data['bHorn'])
    Hoevo.VehicleInfo.VehicleInfoAddDoubleFlash(builder, data['bDoubleFlash'])
    Hoevo.VehicleInfo.VehicleInfoAddSteeringWheelAngle(builder, data['bDoubleFlash'])
    Hoevo.VehicleInfo.VehicleInfoAddSpeed(builder, 10)
    Hoevo.VehicleInfo.VehicleInfoAddTrainingProgram(builder, data['TrainingProgram'])
    Hoevo.VehicleInfo.VehicleInfoAddTimestamp(builder, data['TimeStamp'])
    Hoevo.VehicleInfo.VehicleInfoAddVehicleBodyHit(builder, data['bVehicleBodyHit'])
    Hoevo.VehicleInfo.VehicleInfoAddVehicleFlWheelHit(builder, data['bVehicleFLWheelHit'])
    Hoevo.VehicleInfo.VehicleInfoAddVehicleFrWheelHit(builder, data['bVehicleFRWheelHit'])
    Hoevo.VehicleInfo.VehicleInfoAddVehicleBlWheelHit(builder, data['bVehicleBLWheelHit'])
    Hoevo.VehicleInfo.VehicleInfoAddVehicleBrWheelHit(builder, data['bVehicleBRWheelHit'])
    Hoevo.VehicleInfo.VehicleInfoAddProgramEnd(builder, data['bProgramEnd'])
    Hoevo.VehicleInfo.VehicleInfoAddFlameout(builder, data['bFlameOut'])
    Hoevo.VehicleInfo.VehicleInfoAddReverseParkingLeftCount(builder, data['ReverseParkingLeftCount'])
    Hoevo.VehicleInfo.VehicleInfoAddReverseParkingRightCount(builder, data['ReverseParkingRightCount'])
    Hoevo.VehicleInfo.VehicleInfoAddParkingTrace(builder, data['bParkingTrace'])
    Hoevo.VehicleInfo.VehicleInfoAddInParkingArea(builder, data['bIsInParkingArea'])
    Hoevo.VehicleInfo.VehicleInfoAddPassThroughCheckpointCount(builder, data['PassThroughCheckpointCount'])
    Hoevo.VehicleInfo.VehicleInfoAddPassingThroughCheckpoint(builder, data['bIsPassingThroughCheckpoint'])
    Hoevo.VehicleInfo.VehicleInfoAddBridge1(builder, data['bBridge1'])
    Hoevo.VehicleInfo.VehicleInfoAddBridge2(builder, data['bBridge2'])
    Hoevo.VehicleInfo.VehicleInfoAddBridge3(builder, data['bBridge3'])
    Hoevo.VehicleInfo.VehicleInfoAddBridge4(builder, data['bBridge4'])
    Hoevo.VehicleInfo.VehicleInfoAddRampParking1(builder, data['bRampParking1'])
    Hoevo.VehicleInfo.VehicleInfoAddRampParking2(builder, data['bRampParking2'])
    Hoevo.VehicleInfo.VehicleInfoAddRpm(builder, data['RPM'])
    Hoevo.VehicleInfo.VehicleInfoAddOnZebraCrossing(builder, data['bIsOnZebraCrossing'])
    Hoevo.VehicleInfo.VehicleInfoAddCanVehiclePassThrough(builder, data['bCanVehiclePassThrough'])
    Hoevo.VehicleInfo.VehicleInfoAddFlWheelHitDottedLine(builder, data['bFLWheelHitDottedLine'])
    Hoevo.VehicleInfo.VehicleInfoAddFrWheelHitDottedLine(builder, data['bFRWheelHitDottedLine'])
    Hoevo.VehicleInfo.VehicleInfoAddBlWheelHitDottedLine(builder, data['bBLWheelHitDottedLine'])
    Hoevo.VehicleInfo.VehicleInfoAddBrWheelHitDottedLine(builder, data['bBRWheelHitDottedLine'])
    Hoevo.VehicleInfo.VehicleInfoAddWheelHitSolidLine(builder, data['bWheelHitSolidLine'])
    Hoevo.VehicleInfo.VehicleInfoAddInTurnAroundArea(builder, data['bIsInTurnAroundArea'])
    Hoevo.VehicleInfo.VehicleInfoAddWiperOn(builder, data['bWiperOn'])
    Hoevo.VehicleInfo.VehicleInfoAddIsHeadLightsOn(builder, data['bIsHeadLightsOn'])
    Hoevo.VehicleInfo.VehicleInfoAddWiperState(builder, data['WiperState'])
    Hoevo.VehicleInfo.VehicleInfoAddHeadlightsState(builder, data['HeadlightsState'])
    Hoevo.VehicleInfo.VehicleInfoAddFogLampOn(builder, data['bFogLampOn'])
    Hoevo.VehicleInfo.VehicleInfoAddWidthIndicator(builder, data['bWidthIndicator'])
    Hoevo.VehicleInfo.VehicleInfoAddLimitDoorCheckpoint(builder, data['bLimitDoorCheckPoint'])
    Hoevo.VehicleInfo.VehicleInfoAddHitPeopleOrCar(builder, data['bHitPeopleOrCar'])
    Hoevo.VehicleInfo.VehicleInfoAddEmergencyOperation(builder, data['bEmergencyOperation'])
    Hoevo.VehicleInfo.VehicleInfoAddEmergencyTraining(builder, data['EmergencyTraining'])
    Hoevo.VehicleInfo.VehicleInfoAddOnRightRoad(builder, data['bOnRightRoad'])
    Hoevo.VehicleInfo.VehicleInfoAddRunOverbedgeOfTheRoad(builder, data['bRunOverbedgeOfTheRoad'])
    Hoevo.VehicleInfo.VehicleInfoAddDrivingThroughRollingRoad(builder, data['bDrivingThroughRollingRoad'])
    Hoevo.VehicleInfo.VehicleInfoAddStopOnEmergencyVehicleLane(builder, data['bStopOnEmergencyVehicleLane'])
    Hoevo.VehicleInfo.VehicleInfoAddAboutToLeaveTheTunnel(builder, data['bAboutToLeaveTheTunnel'])
    Hoevo.VehicleInfo.VehicleInfoAddDecelerateWithinTheSpecifiedRange(builder, data['bDecelerateWithinTheSpecifiedRange'])
    Hoevo.VehicleInfo.VehicleInfoAddTurnAccordingToTheRules(builder, data['bTurnAccordingToTheRules'])
    Hoevo.VehicleInfo.VehicleInfoAddGearOperationCorrect(builder, data['bGearOperationCorrect'])
    Hoevo.VehicleInfo.VehicleInfoAddStopInFiftyCm(builder, data['bStopInFiftyCm'])
    Hoevo.VehicleInfo.VehicleInfoAddStopInThirtyCm(builder, data['bStopInThirtyCm'])
    Hoevo.VehicleInfo.VehicleInfoAddAlternateUseLight(builder, data['bAlternateUseLight'])
    Hoevo.VehicleInfo.VehicleInfoAddTurnAfterThreeSecond(builder, data['bTurnAfterThreeSecond'])
    Hoevo.VehicleInfo.VehicleInfoAddActiveGuidancePracticeSuccessed(builder, data['bActiveGuidancePracticeSuccessed'])
    Hoevo.VehicleInfo.VehicleInfoAddTurnAroundStep1(builder, data['bTurnAroundStep1'])
    Hoevo.VehicleInfo.VehicleInfoAddTurnAroundStep2(builder, data['bTurnAroundStep2'])
    Hoevo.VehicleInfo.VehicleInfoAddTurnAroundStep3(builder, data['bTurnAroundStep3'])
    Hoevo.VehicleInfo.VehicleInfoAddTurnAroundStep4(builder, data['bTurnAroundStep4'])
    vehicle_info_data = Hoevo.VehicleInfo.VehicleInfoEnd(builder)


    Hoevo.Payload.PayloadStart(builder)
    Hoevo.Payload.PayloadAddAnyType(builder, Hoevo.Any.Any().VehicleInfo)
    Hoevo.Payload.PayloadAddAny(builder, vehicle_info_data)
    payload = Hoevo.Payload.PayloadEnd(builder)

    builder.Finish(payload)
    payload = builder.Output()

    payload_bytes = bytearray(payload)
    Hoevo.PUBLISH.StartPayloadVector(builder, len(payload_bytes))
    for i in reversed(range(0, len(payload_bytes))):
        print(payload_bytes[i])
        builder.PrependByte(payload_bytes[i])
    payload = builder.EndVector()


    Hoevo.PUBLISH.PUBLISHStart(builder)
    Hoevo.PUBLISH.PUBLISHAddPayload(builder, payload)
    Hoevo.PUBLISH.PUBLISHAddPayloadType(builder, Hoevo.PayloadType.PayloadType().FBS)
    Hoevo.PUBLISH.PUBLISHAddTopic(builder, topic_string)
    Hoevo.PUBLISH.PUBLISHAddClientId(builder, device_uuid)
    Hoevo.PUBLISH.PUBLISHAddQos(builder, Hoevo.QoS.QoS().AtMostOnce)
    PUBLISH = Hoevo.PUBLISH.PUBLISHEnd(builder)



    Hoevo.Msg.MsgStart(builder)
    Hoevo.Msg.MsgAddFlag(builder, PUBLISH)
    Hoevo.Msg.MsgAddFlagType(builder, Hoevo.Flag.Flag().PUBLISH)
    msg = Hoevo.Msg.MsgEnd(builder)


    builder.Finish(msg)
    data = builder.Output()

    return data





def send_connect(ws):
    print("### send connect ###")
    connect = fbs_connect.SendConnect()
    connect.client_id = "vehicle_client_test"
    data = connect.send_fbs_connect()
    ws.send(data, 0x2)
    global websocket_connect
    websocket_connect = True
    time.sleep(2)
    send_login(ws)
    time.sleep(2)
    send_subscribe(ws)
    while True:
        send_VehicleInfo(ws)


def send_login(ws):
    print("### send login ###")
    login = fbs_login.SendLogin()
    login.client_id = "vehicle_client_test"
    login.ip = "127.0.0.1"
    data = login.send_fbs_login()
    ws.send(data, 0x2)

def send_VehicleInfo(ws):
    print("### send send_VehicleInfo ###")
    data = set_vehicle_info_to_data()
    ws.send(data, 0x2)


def send_subscribe(ws):
    print("### send subscribe ###")
    subscribe = fbs_subscribe.SendSubscribe()
    subscribe.topic = "server/#"
    subscribe.topic_1 = "server"
    subscribe.client_id = "vehicle_client_test"
    data = subscribe.send_subscribe()
    ws.send(data, 0x2)

def send_test_data(ws):
    print("### send subscribe ###")



def ws_connect():
    #websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:4001/ws/")
    ws.on_open = send_connect
    ws.run_forever()

if __name__ == '__main__':
    while True:
        ws_connect()
