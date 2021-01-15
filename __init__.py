from ovos_utils.waiting_for_mycroft.base_skill import killable_intent, MycroftSkill
from mycroft import intent_file_handler
from time import sleep


class Test(MycroftSkill):
    """
    send "mycroft.skills.abort_question" and confirm get_response is aborted
    send "mycroft.skills.abort_execution" and confirm the full intent is aborted
    """
    def handle_intent_aborted(self):
        self.speak("I am dead")

    @killable_intent(callback=handle_intent_aborted)
    @intent_file_handler("test.intent")
    def handle_test_abort_intent(self, message):
        while True:
            sleep(1)
            self.speak("still here")

    @intent_file_handler("test2.intent")
    def handle_test_get_response_intent(self, message):
        self.get_response("question", num_retries=9999)
        self.speak("question aborted")


def create_skill():
    return Test()
