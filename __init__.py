from mycroft import MycroftSkill, intent_file_handler


class Horse(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('horse.intent')
    def handle_horse(self, message):
        self.speak_dialog('horse')


def create_skill():
    return Horse()

