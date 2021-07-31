import Hoevo
import Hoevo.Any
import Hoevo.SUBSCRIBE
import Hoevo.Subs
import Hoevo.Msg
import Hoevo.Flag
import Hoevo.QoS
import flatbuffers


class SendSubscribe:
    def __init__(self):
        self.topic = ""
        self.topic_1 = ""
        self.client_id = ""

    def send_subscribe(self):
        builder = flatbuffers.Builder(4096)
        client_id = builder.CreateString(str(self.client_id))
        topic = builder.CreateString(str(self.topic))
        topic_1 = builder.CreateString(str(self.topic_1))

        Hoevo.Subs.SubsStart(builder)
        Hoevo.Subs.SubsAddTopic(builder, topic)
        Hoevo.Subs.SubsAddQos(builder, Hoevo.QoS.QoS().AtMostOnce)
        server_subs = Hoevo.Subs.SubsEnd(builder)

        Hoevo.Subs.SubsStart(builder)
        Hoevo.Subs.SubsAddTopic(builder, topic_1)
        Hoevo.Subs.SubsAddQos(builder, Hoevo.QoS.QoS().AtMostOnce)
        server1_subs = Hoevo.Subs.SubsEnd(builder)

        Hoevo.SUBSCRIBE.SUBSCRIBEStartTopicFiltersVector(builder, 2)
        builder.PrependUOffsetTRelative(server_subs)
        builder.PrependUOffsetTRelative(server1_subs)
        subs = builder.EndVector()

        Hoevo.SUBSCRIBE.SUBSCRIBEStart(builder)
        Hoevo.SUBSCRIBE.SUBSCRIBEAddTopicFilters(builder, subs)
        Hoevo.SUBSCRIBE.SUBSCRIBEAddClientId(builder, client_id)
        subscribe = Hoevo.SUBSCRIBE.SUBSCRIBEEnd(builder)

        Hoevo.Msg.MsgStart(builder)
        Hoevo.Msg.MsgAddFlag(builder, subscribe)
        Hoevo.Msg.MsgAddFlagType(builder, Hoevo.Flag.Flag().SUBSCRIBE)
        msg = Hoevo.Msg.MsgEnd(builder)
        builder.Finish(msg)
        buf = builder.Output()

        return buf


