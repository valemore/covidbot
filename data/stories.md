## happy path, symptoms, no exposure
* greet
    - utter_greet
* check_symptoms
    - symptom_form
    - form{"name": "symptom_form"}
    - form{"name": null}
    - slot{"symptoms_present": true}
    - utter_slots_values
    - utter_ask_exposure
    * deny
    - utter_self_isolate
* thankyou
    - utter_noworries

## happy path, symptoms, no exposure
* greet
    - utter_greet
* check_symptoms
    - symptom_form
    - form{"name": "symptom_form"}
    - form{"name": null}
    - slot{"symptoms_present": true}
    - utter_slots_values
    - utter_ask_exposure
    * affirm
    - utter_seek_help
* thankyou
    - utter_noworries

## happy path, no symptoms
* greet
    - utter_greet
* check_symptoms
    - symptom_form
    - form{"name": "symptom_form"}
    - form{"name": null}
    - slot{"symptoms_present": false}
    - utter_slots_values
    - utter_safe
* thankyou
    - utter_noworries

## unhappy path
* greet
    - utter_greet
* check_symptoms
    - symptom_form
    - form{"name": "symptom_form"}
* chitchat
    - utter_chitchat
    - symptom_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## very unhappy path
* greet
    - utter_greet
* check_symptoms
    - symptom_form
    - form{"name": "symptom_form"}
* chitchat
    - utter_chitchat
    - symptom_form
* chitchat
    - utter_chitchat
    - symptom_form
* chitchat
    - utter_chitchat
    - symptom_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## stop but continue path
* greet
    - utter_greet
* check_symptoms
    - symptom_form
    - form{"name": "symptom_form"}
* stop
    - utter_ask_continue
* affirm
    - symptom_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## stop and really stop path
* greet
    - utter_greet
* check_symptoms
    - symptom_form
    - form{"name": "symptom_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## chitchat stop but continue path
* check_symptoms
    - symptom_form
    - form{"name": "symptom_form"}
* chitchat
    - utter_chitchat
    - symptom_form
* stop
    - utter_ask_continue
* affirm
    - symptom_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## stop but continue and chitchat path
* greet
    - utter_greet
* check_symptoms
    - symptom_form
    - form{"name": "symptom_form"}
* stop
    - utter_ask_continue
* affirm
    - symptom_form
* chitchat
    - utter_chitchat
    - symptom_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## chitchat stop but continue and chitchat path
* greet
    - utter_greet
* check_symptoms
    - symptom_form
    - form{"name": "symptom_form"}
* chitchat
    - utter_chitchat
    - symptom_form
* stop
    - utter_ask_continue
* affirm
    - symptom_form
* chitchat
    - utter_chitchat
    - symptom_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## chitchat, stop and really stop path
* greet
    - utter_greet
* check_symptoms
    - symptom_form
    - form{"name": "symptom_form"}
* chitchat
    - utter_chitchat
    - symptom_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## bot challenge
* bot_challenge
  - utter_iamabot
