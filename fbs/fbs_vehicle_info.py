import Hoevo
import Hoevo.VehicleInfo
import Hoevo.Payload
import flatbuffers


class VehicleInfo:
    def __init__(self):
        self.uuid = ""
        self.player_id = ""
        self.device_id = ""
        self.engine_start = False
        self.hand_brake = False
        self.clutch_intensity = 0
        self.brake_pedal_intensity = 0
        self.throttle_intensity = 0
        self.safety_belt = False
        self.current_gear = 0
        self.add_gear_by_degrees = False
        self.sub_gear_by_degrees = False
        self.cornering_lamp_state = 0
        self.horn = False
        self.double_flash = False
        self.steering_wheel_angle = 0
        self.speed = 0
        self.training_program = 0
        self.timestamp = 0
        self.vehicle_body_hit = False
        self.vehicle_fl_wheel_hit = False
        self.vehicle_fr_wheel_hit = False
        self.vehicle_bl_wheel_hit = False
        self.vehicle_br_wheel_hit = False
        self.program_end = False
        self.flameout = False
        self.reverse_parking_left_count = 0
        self.reverse_parking_right_count = 0
        self.parking_trace = False
        self.in_parking_area = False
        self.pass_through_checkpoint_count = 0
        self.passing_through_checkpoint = False
        self.bridge1 = False
        self.bridge2 = False
        self.bridge3 = False
        self.bridge4 = False
        self.ramp_parking1 = False
        self.ramp_parking2 = False
        self.rpm = 0
        self.on_zebra_crossing = False
        self.can_vehicle_pass_through = False
        self.fl_wheel_hit_dotted_line = False
        self.fr_wheel_hit_dotted_line = False
        self.bl_wheel_hit_dotted_line = False
        self.br_wheel_hit_dotted_line = False
        self.wheel_hit_solid_line = False
        self.in_turn_around_area = False
        self.wiper_on = False
        self.is_head_lights_on = False
        self.wiper_state = 0
        self.headlights_state = 0
        self.fog_lamp_on = False
        self.width_indicator = False
        self.limit_door_checkpoint = False
        self.hit_people_or_car = False
        self.emergency_operation = False
        self.emergency_training=0
        self.on_right_road = False
        self.run_overbedge_of_the_road = False
        self.driving_through_rolling_road = False
        self.stop_on_emergency_vehicle_lane = False
        self.about_to_leave_the_tunnel = False
        self.decelerate_within_the_specified_range = False
        self.turn_according_to_the_rules = False
        self.gear_operation_correct = False
        self.stop_in_fifty_cm = False
        self.stop_in_thirty_cm = False
        self.alternate_use_light = False
        self.turn_after_three_second = False
        self.active_guidance_practice_successed = False
        self.turn_around_step1 = False
        self.turn_around_step2 = False
        self.turn_around_step3 = False
        self.turn_around_step4 = False

    def parser_vehicle_info(self, input_vehicle_data):
        self.uuid = str(input_vehicle_data.Uuid())
        self.player_id = str(input_vehicle_data.PlayerId())
        self.device_id = str(input_vehicle_data.DeviceId())
        self.engine_start = input_vehicle_data.EngineStart()
        self.hand_brake = input_vehicle_data.HandBrake()
        self.clutch_intensity = input_vehicle_data.ClutchIntensity()
        self.brake_pedal_intensity = input_vehicle_data.BrakePedalIntensity()
        self.throttle_intensity = input_vehicle_data.ThrottleIntensity()
        self.safety_belt = input_vehicle_data.SafetyBelt()
        self.current_gear = input_vehicle_data.CurrentGear()
        self.add_gear_by_degrees = input_vehicle_data.AddGearByDegrees()
        self.sub_gear_by_degrees = input_vehicle_data.SubGearByDegrees()
        self.cornering_lamp_state = input_vehicle_data.CorneringLampState()
        self.horn = input_vehicle_data.Horn()
        self.double_flash = input_vehicle_data.DoubleFlash()
        self.steering_wheel_angle = input_vehicle_data.SteeringWheelAngle()
        self.speed = input_vehicle_data.Speed()
        self.training_program = input_vehicle_data.TrainingProgram()
        self.timestamp = input_vehicle_data.Timestamp()
        self.vehicle_body_hit = input_vehicle_data.VehicleBodyHit()
        self.vehicle_fl_wheel_hit = input_vehicle_data.VehicleFlWheelHit()
        self.vehicle_fr_wheel_hit = input_vehicle_data.VehicleFrWheelHit()
        self.vehicle_bl_wheel_hit = input_vehicle_data.VehicleBlWheelHit()
        self.vehicle_br_wheel_hit = input_vehicle_data.VehicleBrWheelHit()
        self.program_end = input_vehicle_data.ProgramEnd()
        self.flameout = input_vehicle_data.Flameout()
        self.reverse_parking_left_count = input_vehicle_data.ReverseParkingLeftCount()
        self.reverse_parking_right_count = input_vehicle_data.ReverseParkingRightCount()
        self.parking_trace = input_vehicle_data.ParkingTrace()
        self.in_parking_area = input_vehicle_data.InParkingArea()
        self.pass_through_checkpoint_count = input_vehicle_data.PassThroughCheckpointCount()
        self.passing_through_checkpoint = input_vehicle_data.PassingThroughCheckpoint()
        self.bridge1 = input_vehicle_data.Bridge1()
        self.bridge2 = input_vehicle_data.Bridge2()
        self.bridge3 = input_vehicle_data.Bridge3()
        self.bridge4 = input_vehicle_data.Bridge4()
        self.ramp_parking1 = input_vehicle_data.RampParking1()
        self.ramp_parking2 = input_vehicle_data.RampParking2()
        self.rpm = input_vehicle_data.Rpm()
        self.on_zebra_crossing = input_vehicle_data.OnZebraCrossing()
        self.can_vehicle_pass_through = input_vehicle_data.CanVehiclePassThrough()
        self.fl_wheel_hit_dotted_line = input_vehicle_data.FlWheelHitDottedLine()
        self.fr_wheel_hit_dotted_line = input_vehicle_data.FrWheelHitDottedLine()
        self.bl_wheel_hit_dotted_line = input_vehicle_data.BlWheelHitDottedLine()
        self.br_wheel_hit_dotted_line = input_vehicle_data.BrWheelHitDottedLine()
        self.wheel_hit_solid_line = input_vehicle_data.WheelHitSolidLine()
        self.in_turn_around_area = input_vehicle_data.InTurnAroundArea()
        self.wiper_on = input_vehicle_data.WiperOn()
        self.is_head_lights_on = input_vehicle_data.IsHeadLightsOn()
        self.wiper_state = input_vehicle_data.WiperState()
        self.headlights_state = input_vehicle_data.HeadlightsState()
        self.fog_lamp_on = input_vehicle_data.FogLampOn()
        self.width_indicator = input_vehicle_data.WidthIndicator()
        self.limit_door_checkpoint = input_vehicle_data.LimitDoorCheckpoint()
        self.hit_people_or_car = input_vehicle_data.HitPeopleOrCar()
        self.emergency_operation = input_vehicle_data.EmergencyOperation()
        self.emergency_training = input_vehicle_data.EmergencyTraining()
        self.on_right_road = input_vehicle_data.OnRightRoad()
        self.run_overbedge_of_the_road = input_vehicle_data.RunOverbedgeOfTheRoad()
        self.driving_through_rolling_road = input_vehicle_data.DrivingThroughRollingRoad()
        self.stop_on_emergency_vehicle_lane = input_vehicle_data.StopOnEmergencyVehicleLane()
        self.about_to_leave_the_tunnel = input_vehicle_data.AboutToLeaveTheTunnel()
        self.decelerate_within_the_specified_range = input_vehicle_data.DecelerateWithinTheSpecifiedRange()
        self.turn_according_to_the_rules = input_vehicle_data.TurnAccordingToTheRules()
        self.gear_operation_correct = input_vehicle_data.GearOperationCorrect()
        self.stop_in_fifty_cm = input_vehicle_data.StopInFiftyCm()
        self.stop_in_thirty_cm = input_vehicle_data.StopInThirtyCm()
        self.alternate_use_light = input_vehicle_data.AlternateUseLight()
        self.turn_after_three_second = input_vehicle_data.TurnAfterThreeSecond()
        self.active_guidance_practice_successed = input_vehicle_data.ActiveGuidancePracticeSuccessed()
        self.turn_around_step1 = input_vehicle_data.TurnAroundStep1()
        self.turn_around_step2 = input_vehicle_data.TurnAroundStep2()
        self.turn_around_step3 = input_vehicle_data.TurnAroundStep3()
        self.turn_around_step4 = input_vehicle_data.TurnAroundStep4()

    def set_vehicle_info_to_data(self, input_vehicle_data):
        data = {
            'uuid': input_vehicle_data.Uuid().decode('UTF-8'),
            'player_id': input_vehicle_data.PlayerId().decode('UTF-8'),
            'device_id': input_vehicle_data.DeviceId().decode('UTF-8'),
            'bEngineStart': input_vehicle_data.EngineStart(),
            'bHandBrake': input_vehicle_data.HandBrake(),
            'ClutchIntensity': input_vehicle_data.ClutchIntensity(),
            'BrakePedalIntensity': input_vehicle_data.BrakePedalIntensity(),
            'ThrottleIntensity': input_vehicle_data.ThrottleIntensity(),
            'bSafetyBelt': input_vehicle_data.SafetyBelt(),
            'CurrentGear': input_vehicle_data.CurrentGear(),
            'bAddGearByDegrees': input_vehicle_data.AddGearByDegrees(),
            'bSubGearByDegrees': input_vehicle_data.SubGearByDegrees(),
            'CorneringLampState': input_vehicle_data.CorneringLampState(),
            'bHorn': input_vehicle_data.Horn(),
            'bDoubleFlash': input_vehicle_data.DoubleFlash(),
            'SteeringWheelAngle': input_vehicle_data.SteeringWheelAngle(),
            'Speed': input_vehicle_data.Speed(),
            'TrainingProgram': input_vehicle_data.TrainingProgram(),
            'TimeStamp': input_vehicle_data.Timestamp(),
            'bVehicleBodyHit': input_vehicle_data.VehicleBodyHit(),
            'bVehicleFLWheelHit': input_vehicle_data.VehicleFlWheelHit(),
            'bVehicleFRWheelHit': input_vehicle_data.VehicleFrWheelHit(),
            'bVehicleBLWheelHit': input_vehicle_data.VehicleBlWheelHit(),
            'bVehicleBRWheelHit': input_vehicle_data.VehicleBrWheelHit(),
            'bProgramEnd': input_vehicle_data.ProgramEnd(),
            'bFlameOut': input_vehicle_data.Flameout(),
            'ReverseParkingLeftCount': input_vehicle_data.ReverseParkingLeftCount(),
            'ReverseParkingRightCount': input_vehicle_data.ReverseParkingRightCount(),
            'bParkingTrace': input_vehicle_data.ParkingTrace(),
            'bIsInParkingArea': input_vehicle_data.InParkingArea(),
            'PassThroughCheckpointCount': input_vehicle_data.PassThroughCheckpointCount(),
            'bIsPassingThroughCheckpoint': input_vehicle_data.PassingThroughCheckpoint(),
            'bBridge1': input_vehicle_data.Bridge1(),
            'bBridge2': input_vehicle_data.Bridge2(),
            'bBridge3': input_vehicle_data.Bridge3(),
            'bBridge4': input_vehicle_data.Bridge4(),
            'bRampParking1': input_vehicle_data.RampParking1(),
            'bRampParking2': input_vehicle_data.RampParking2(),
            'RPM': input_vehicle_data.Rpm(),
            'bIsOnZebraCrossing': input_vehicle_data.OnZebraCrossing(),
            'bCanVehiclePassThrough': input_vehicle_data.CanVehiclePassThrough(),
            'bFLWheelHitDottedLine': input_vehicle_data.FlWheelHitDottedLine(),
            'bFRWheelHitDottedLine': input_vehicle_data.FrWheelHitDottedLine(),
            'bBLWheelHitDottedLine': input_vehicle_data.BlWheelHitDottedLine(),
            'bBRWheelHitDottedLine': input_vehicle_data.BrWheelHitDottedLine(),
            'bWheelHitSolidLine': input_vehicle_data.WheelHitSolidLine(),
            'bIsInTurnAroundArea': input_vehicle_data.InTurnAroundArea(),
            'bWiperOn': input_vehicle_data.WiperOn(),
            'bIsHeadLightsOn': input_vehicle_data.IsHeadLightsOn(),
            'WiperState': input_vehicle_data.WiperState(),
            'HeadlightsState': input_vehicle_data.HeadlightsState(),
            'bFogLampOn': input_vehicle_data.FogLampOn(),
            'bWidthIndicator': input_vehicle_data.WidthIndicator(),
            'bLimitDoorCheckPoint': input_vehicle_data.LimitDoorCheckpoint(),
            'bHitPeopleOrCar': input_vehicle_data.HitPeopleOrCar(),
            'bEmergencyOperation': input_vehicle_data.EmergencyOperation(),
            'EmergencyTraining': input_vehicle_data.EmergencyTraining(),
            'bOnRightRoad': input_vehicle_data.OnRightRoad(),
            'bRunOverbedgeOfTheRoad': input_vehicle_data.RunOverbedgeOfTheRoad(),
            'bDrivingThroughRollingRoad': input_vehicle_data.DrivingThroughRollingRoad(),
            'bStopOnEmergencyVehicleLane': input_vehicle_data.StopOnEmergencyVehicleLane(),
            'bAboutToLeaveTheTunnel': input_vehicle_data.AboutToLeaveTheTunnel(),
            'bDecelerateWithinTheSpecifiedRange': input_vehicle_data.DecelerateWithinTheSpecifiedRange(),
            'bTurnAccordingToTheRules': input_vehicle_data.TurnAccordingToTheRules(),
            'bGearOperationCorrect': input_vehicle_data.GearOperationCorrect(),
            'bStopInFiftyCm': input_vehicle_data.StopInFiftyCm(),
            'bStopInThirtyCm': input_vehicle_data.StopInThirtyCm(),
            'bAlternateUseLight': input_vehicle_data.AlternateUseLight(),
            'bTurnAfterThreeSecond': input_vehicle_data.TurnAfterThreeSecond(),
            'bActiveGuidancePracticeSuccessed': input_vehicle_data.ActiveGuidancePracticeSuccessed(),
            'bTurnAroundStep1': input_vehicle_data.TurnAroundStep1(),
            'bTurnAroundStep2': input_vehicle_data.TurnAroundStep2(),
            'bTurnAroundStep3': input_vehicle_data.TurnAroundStep3(),
            'bTurnAroundStep4': input_vehicle_data.TurnAroundStep4()
        }
        #print(data)
        return data

    def send_vehicle_info(self):
        builder = flatbuffers.Builder(flatbuffers.Builder.MAX_BUFFER_SIZE)
        topic_string = builder.CreateString(str("server"))
        device_uuid = builder.CreateString(str("vehicle_client"))
        uuid = builder.CreateString(str(self.uuid))
        player_id = builder.CreateString(str(self.player_id))
        device_id = builder.CreateString(str(self.device_id))
        Hoevo.VehicleInfo.VehicleInfoStart(builder)
        Hoevo.VehicleInfo.VehicleInfoAddUuid(builder, uuid)
        Hoevo.VehicleInfo.VehicleInfoAddPlayerId(builder, player_id)
        Hoevo.VehicleInfo.VehicleInfoAddDeviceId(builder, device_id)
        Hoevo.VehicleInfo.VehicleInfoAddEngineStart(builder, self.engine_start)
        Hoevo.VehicleInfo.VehicleInfoAddHandBrake(builder, self.hand_brake)
        Hoevo.VehicleInfo.VehicleInfoAddClutchIntensity(builder, self.clutch_intensity)
        Hoevo.VehicleInfo.VehicleInfoAddBrakePedalIntensity(builder, self.brake_pedal_intensity)
        Hoevo.VehicleInfo.VehicleInfoAddThrottleIntensity(builder, self.throttle_intensity)
        Hoevo.VehicleInfo.VehicleInfoAddSafetyBelt(builder, self.safety_belt)
        Hoevo.VehicleInfo.VehicleInfoAddCurrentGear(builder, self.current_gear)
        Hoevo.VehicleInfo.VehicleInfoAddAddGearByDegrees(builder, self.add_gear_by_degrees)
        Hoevo.VehicleInfo.VehicleInfoAddCorneringLampState(builder, self.cornering_lamp_state)
        Hoevo.VehicleInfo.VehicleInfoAddHorn(builder, self.horn)
        Hoevo.VehicleInfo.VehicleInfoAddDoubleFlash(builder, self.double_flash)
        Hoevo.VehicleInfo.VehicleInfoAddSteeringWheelAngle(builder, self.steering_wheel_angle)
        Hoevo.VehicleInfo.VehicleInfoAddSpeed(builder, self.speed)
        Hoevo.VehicleInfo.VehicleInfoAddTrainingProgram(builder, self.training_program)
        Hoevo.VehicleInfo.VehicleInfoAddTimestamp(builder, self.timestamp)
        Hoevo.VehicleInfo.VehicleInfoAddVehicleBodyHit(builder, self.vehicle_body_hit)
        Hoevo.VehicleInfo.VehicleInfoAddVehicleFlWheelHit(builder, self.vehicle_fl_wheel_hit)
        Hoevo.VehicleInfo.VehicleInfoAddVehicleFrWheelHit(builder, self.vehicle_fr_wheel_hit)
        Hoevo.VehicleInfo.VehicleInfoAddVehicleBlWheelHit(builder, self.vehicle_bl_wheel_hit)
        Hoevo.VehicleInfo.VehicleInfoAddVehicleBrWheelHit(builder, self.vehicle_br_wheel_hit)
        Hoevo.VehicleInfo.VehicleInfoAddProgramEnd(builder, self.program_end)
        Hoevo.VehicleInfo.VehicleInfoAddFlameout(builder, self.flameout)
        Hoevo.VehicleInfo.VehicleInfoAddReverseParkingLeftCount(builder, self.reverse_parking_left_count)
        Hoevo.VehicleInfo.VehicleInfoAddReverseParkingRightCount(builder, self.reverse_parking_right_count)
        Hoevo.VehicleInfo.VehicleInfoAddParkingTrace(builder, self.parking_trace)
        Hoevo.VehicleInfo.VehicleInfoAddInParkingArea(builder, self.in_parking_area)
        Hoevo.VehicleInfo.VehicleInfoAddPassThroughCheckpointCount(builder, self.pass_through_checkpoint_count)
        Hoevo.VehicleInfo.VehicleInfoAddPassingThroughCheckpoint(builder, self.passing_through_checkpoint)
        Hoevo.VehicleInfo.VehicleInfoAddBridge1(builder, self.bridge1)
        Hoevo.VehicleInfo.VehicleInfoAddBridge2(builder, self.bridge2)
        Hoevo.VehicleInfo.VehicleInfoAddBridge3(builder, self.bridge3)
        Hoevo.VehicleInfo.VehicleInfoAddBridge4(builder, self.bridge4)
        Hoevo.VehicleInfo.VehicleInfoAddRampParking1(builder, self.ramp_parking1)
        Hoevo.VehicleInfo.VehicleInfoAddRampParking2(builder, self.ramp_parking2)
        Hoevo.VehicleInfo.VehicleInfoAddRpm(builder, self.rpm)
        Hoevo.VehicleInfo.VehicleInfoAddOnZebraCrossing(builder, self.on_zebra_crossing)
        Hoevo.VehicleInfo.VehicleInfoAddCanVehiclePassThrough(builder, self.can_vehicle_pass_through)
        Hoevo.VehicleInfo.VehicleInfoAddFlWheelHitDottedLine(builder, self.fl_wheel_hit_dotted_line)
        Hoevo.VehicleInfo.VehicleInfoAddFrWheelHitDottedLine(builder, self.fr_wheel_hit_dotted_line)
        Hoevo.VehicleInfo.VehicleInfoAddBlWheelHitDottedLine(builder, self.bl_wheel_hit_dotted_line)
        Hoevo.VehicleInfo.VehicleInfoAddBrWheelHitDottedLine(builder, self.br_wheel_hit_dotted_line)
        Hoevo.VehicleInfo.VehicleInfoAddWheelHitSolidLine(builder, self.wheel_hit_solid_line)
        Hoevo.VehicleInfo.VehicleInfoAddInTurnAroundArea(builder, self.in_turn_around_area)
        Hoevo.VehicleInfo.VehicleInfoAddWiperOn(builder, self.wiper_on)
        Hoevo.VehicleInfo.VehicleInfoAddIsHeadLightsOn(builder, self.is_head_lights_on)
        Hoevo.VehicleInfo.VehicleInfoAddWiperState(builder, self.wiper_state)
        Hoevo.VehicleInfo.VehicleInfoAddHeadlightsState(builder, self.headlights_state)
        Hoevo.VehicleInfo.VehicleInfoAddFogLampOn(builder, self.fog_lamp_on)
        Hoevo.VehicleInfo.VehicleInfoAddWidthIndicator(builder, self.width_indicator)
        Hoevo.VehicleInfo.VehicleInfoAddLimitDoorCheckpoint(builder, self.limit_door_checkpoint)
        Hoevo.VehicleInfo.VehicleInfoAddHitPeopleOrCar(builder, self.hit_people_or_car)
        Hoevo.VehicleInfo.VehicleInfoAddEmergencyOperation(builder, self.emergency_operation)
        Hoevo.VehicleInfo.VehicleInfoAddEmergencyTraining(builder, self.emergency_training)
        Hoevo.VehicleInfo.VehicleInfoAddOnRightRoad(builder, self.on_right_road)
        Hoevo.VehicleInfo.VehicleInfoAddRunOverbedgeOfTheRoad(builder, self.run_overbedge_of_the_road)
        Hoevo.VehicleInfo.VehicleInfoAddDrivingThroughRollingRoad(builder, self.driving_through_rolling_road)
        Hoevo.VehicleInfo.VehicleInfoAddStopOnEmergencyVehicleLane(builder, self.stop_on_emergency_vehicle_lane)
        Hoevo.VehicleInfo.VehicleInfoAddAboutToLeaveTheTunnel(builder, self.about_to_leave_the_tunnel)
        Hoevo.VehicleInfo.VehicleInfoAddDecelerateWithinTheSpecifiedRange(builder, self.decelerate_within_the_specified_range)
        Hoevo.VehicleInfo.VehicleInfoAddTurnAccordingToTheRules(builder, self.turn_according_to_the_rules)
        Hoevo.VehicleInfo.VehicleInfoAddGearOperationCorrect(builder, self.gear_operation_correct)
        Hoevo.VehicleInfo.VehicleInfoAddStopInFiftyCm(builder, self.stop_in_fifty_cm)
        Hoevo.VehicleInfo.VehicleInfoAddStopInThirtyCm(builder, self.stop_in_thirty_cm)
        Hoevo.VehicleInfo.VehicleInfoAddAlternateUseLight(builder, self.alternate_use_light)
        Hoevo.VehicleInfo.VehicleInfoAddTurnAfterThreeSecond(builder, self.turn_after_three_second)
        Hoevo.VehicleInfo.VehicleInfoAddActiveGuidancePracticeSuccessed(builder, self.active_guidance_practice_successed)
        Hoevo.VehicleInfo.VehicleInfoAddTurnAroundStep1(builder, self.turn_around_step1)
        Hoevo.VehicleInfo.VehicleInfoAddTurnAroundStep2(builder, self.turn_around_step2)
        Hoevo.VehicleInfo.VehicleInfoAddTurnAroundStep3(builder, self.turn_around_step3)
        Hoevo.VehicleInfo.VehicleInfoAddTurnAroundStep4(builder, self.turn_around_step4)
        vehicle_info = Hoevo.VehicleInfo.VehicleInfoEnd(builder)


        Hoevo.Payload.PayloadStart(builder)
        Hoevo.Payload.PayloadAddAnyType(builder, Hoevo.Any.Any().VehicleInfo)
        Hoevo.Payload.PayloadAddAny(builder, vehicle_info)
        payload = Hoevo.Payload.PayloadEnd(builder)

        builder.Finish(payload)
        payload = builder.Output()

        payload_bytes = bytearray(payload)
        Hoevo.PUBLISH.StartPayloadVector(builder, len(payload_bytes))
        for i in reversed(range(0, len(payload_bytes))):
            builder.PrependByte(payload_bytes[i])
        payload = builder.EndVector()

        Hoevo.PUBLISH.PUBLISHStart(builder)
        Hoevo.PUBLISH.PUBLISHAddPayload(builder, payload)
        Hoevo.PUBLISH.PUBLISHAddPayloadType(builder, Hoevo.PayloadType.PayloadType().FBS)
        Hoevo.PUBLISH.PUBLISHAddTopic(builder, topic_string)
        Hoevo.PUBLISH.PUBLISHAddClientId(builder, device_uuid)
        PUBLISH = Hoevo.PUBLISH.PUBLISHEnd(builder)

        Hoevo.Msg.MsgStart(builder)
        Hoevo.Msg.MsgAddFlag(builder, PUBLISH)
        Hoevo.Msg.MsgAddFlagType(builder, Hoevo.Flag.Flag().PUBLISH)
        msg = Hoevo.Msg.MsgEnd(builder)
        builder.Finish(msg)
        buf = builder.Output()
        return buf
