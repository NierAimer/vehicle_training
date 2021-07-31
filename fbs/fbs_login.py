import Hoevo
import Hoevo.Any
import Hoevo.Msg
import Hoevo.Payload
import Hoevo.PayloadType
import Hoevo.Login
import Hoevo.Project
import Hoevo.PUBLISH
import Hoevo.Role
import Hoevo.Flag
import flatbuffers


class SendLogin:
    def __init__(self):
        self.client_id = ""
        self.ip = ""

    def send_fbs_login(self):
        builder = flatbuffers.Builder(flatbuffers.Builder.MAX_BUFFER_SIZE)
        client_id = builder.CreateString(str(self.client_id))
        ip = builder.CreateString(str(self.ip))
        meta = builder.CreateString(str(""))
        topic_string = builder.CreateString(str("server"))
        device_uuid = builder.CreateString(str("vehicle_client"))
        Hoevo.Login.LoginStart(builder)
        Hoevo.Login.LoginAddClientId(builder, client_id)
        Hoevo.Login.LoginAddIp(builder, ip)
        Hoevo.Login.LoginAddProject(builder, Hoevo.Project.Project().Vehicle)
        Hoevo.Login.LoginAddRole(builder, Hoevo.Role.Role().Client)
        Hoevo.Login.LoginAddMeta(builder, meta)
        login = Hoevo.Login.LoginEnd(builder)

        Hoevo.Payload.PayloadStart(builder)
        Hoevo.Payload.PayloadAddAnyType(builder, Hoevo.Any.Any().Login)
        Hoevo.Payload.PayloadAddAny(builder, login)
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
        Hoevo.PUBLISH.PUBLISHAddClientId(builder,device_uuid)
        Hoevo.PUBLISH.PUBLISHAddQos(builder, Hoevo.QoS.QoS().AtMostOnce)

        PUBLISH = Hoevo.PUBLISH.PUBLISHEnd(builder)
        Hoevo.Msg.MsgStart(builder)
        Hoevo.Msg.MsgAddFlag(builder, PUBLISH)
        Hoevo.Msg.MsgAddFlagType(builder, Hoevo.Flag.Flag().PUBLISH)
        msg = Hoevo.Msg.MsgEnd(builder)
        builder.Finish(msg)
        buf = builder.Output()
        return buf



