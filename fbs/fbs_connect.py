import Hoevo
import Hoevo.Any
import Hoevo.Msg
import Hoevo.Flag
import Hoevo.CONNECT
import flatbuffers


class SendConnect:
    def __init__(self):
        self.client_id = ""

    def send_fbs_connect(self):
        builder = flatbuffers.Builder(1024)
        client_id = builder.CreateString(str(self.client_id))
        Hoevo.CONNECT.CONNECTStart(builder)
        Hoevo.CONNECT.CONNECTAddClientId(builder, client_id)
        Hoevo.CONNECT.CONNECTAddCleanStart(builder, True)
        Hoevo.CONNECT.CONNECTAddKeepAlive(builder, True)
        CONNECT = Hoevo.CONNECT.CONNECTEnd(builder)
        Hoevo.Msg.MsgStart(builder)
        Hoevo.Msg.MsgAddFlag(builder, CONNECT)
        Hoevo.Msg.MsgAddFlagType(builder, Hoevo.Flag.Flag().CONNECT)
        msg = Hoevo.Msg.MsgEnd(builder)
        builder.Finish(msg)
        buf = builder.Output()
        return buf
