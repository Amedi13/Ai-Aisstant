from app.speech.listen import transcribe
from app.speech.speak import speak 
from app.modules.gpt_handler import get_response


# This  function is what runs the Ai Aisstant#
def run_assistant(): 
    #indicatation that its running
    print("Aisstant is running. . .")
    #while loop to keep assistant running until user exits
    speak("Hello! How can I assist you today?")
    while True: 
       user_input = transcribe() #bug no response after transcribe
       #get the ai to respind to the user input
       ai_response = get_response(user_input)
       if "exit" in user_input.lower():
           speak("Goodbye!")
           break
       speak(ai_response)
      # response = get_response(user_input)
    