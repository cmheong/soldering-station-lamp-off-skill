from mycroft import MycroftSkill, intent_file_handler


class SolderingStationLampOff(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('off.lamp.station.soldering.intent')
    def handle_off_lamp_station_soldering(self, message):
        self.speak_dialog('off.lamp.station.soldering')


def create_skill():
    return SolderingStationLampOff()

