from mycroft import MycroftSkill, intent_file_handler


class SimpleLocalLists(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('lists.local.simple.intent')
    def handle_lists_local_simple(self, message):
        self.speak_dialog('lists.local.simple')


def create_skill():
    return SimpleLocalLists()

