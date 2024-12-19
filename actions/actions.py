from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionRecommendProfessionalHelp(Action):
    def name(self) -> Text:
        return "action_recommend_professional_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Extract the entity from the user's message
        professional_type = next(tracker.get_latest_entity_values("professional_type"), None)

        # Define recommendations for different professionals
        recommendations = {
            "therapist": "You can find licensed therapists through platforms like BetterHelp or Talkspace.",
            "counselor": "Consider reaching out to local counseling centers or community mental health services.",
            "psychiatrist": "Psychiatrists can be found through referrals from your primary doctor or mental health clinics.",
            "psychologist": "Check out the American Psychological Association's website for a list of certified psychologists.",
            "life coach": "Explore platforms like LifeCoach.com or local directories for life coaching services."
        }

        # Prepare a response based on the professional type
        if professional_type in recommendations:
            response = recommendations[professional_type]
        else:
            response = (
                "I'm here to help, but I couldn't identify the professional you are looking for. "
                "Could you specify whether you need a therapist, counselor, psychiatrist, psychologist, or life coach?"
            )

        # Send the response
        dispatcher.utter_message(text=response)
        return []