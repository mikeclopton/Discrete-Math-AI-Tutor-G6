from services import input_recognizer, ai_simulator

print("Input Recognizer:", input_recognizer)
print("AI Simulator:", ai_simulator)

print("Recognize method:", input_recognizer.recognize("test", "text"))
print("Generate response method:", ai_simulator.generate_response("test question"))