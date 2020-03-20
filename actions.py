from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class SymptomForm(FormAction):
    """Form that asks for symptoms"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "symptom_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["fever_present", "cough_present", "limb_pain_present", "sore_throat_present"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "fever_present": [
                self.from_entity(entity="fever_present", not_intent="chitchat"),
                self.from_intent(intent='affirm', value=True),
                self.from_intent(intent='deny', value=False)],
            "cough_present": [
                self.from_entity(entity="cough_present", not_intent="chitchat"),
                self.from_intent(intent='affirm', value=True),
                self.from_intent(intent='deny', value=False)],
            "limb_pain_present": [
                self.from_entity(entity="limb_pain_present", not_intent="chitchat"),
                self.from_intent(intent='affirm', value=True),
                self.from_intent(intent='deny', value=False)],
            "sore_throat_present": [
                self.from_entity(entity="sore_throat_present", not_intent="chitchat"),
                self.from_intent(intent='affirm', value=True),
                self.from_intent(intent='deny', value=False)]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        fever_present = tracker.get_slot("fever_present")
        cough_present = tracker.get_slot("cough_present")
        limb_pain_present = tracker.get_slot("limb_pain_present")
        sore_throat_present = tracker.get_slot("sore_throat_present")

        n_symptoms = sum(bool(s) for s in [fever_present, cough_present, limb_pain_present, sore_throat_present])
        symptoms_present = True if n_symptoms > 1 else False

        symptoms_list = [s for s, sp in zip(["fever", "cough", "limb pain", "sore throat"],
                                            [fever_present, cough_present, limb_pain_present, sore_throat_present])
                                            if sp]
        symptoms_list_text = ', '.join(symptoms_list)
        
        dispatcher.utter_message(f"You have {n_symptoms} symptoms {symptoms_present}")

        # utter submit template
        dispatcher.utter_message(template="utter_submit")
        return [SlotSet("symptoms_present", symptoms_present), SlotSet("symptoms_list", symptoms_list_text)]
