class InputRecognizer:
    def recognize(self, content: str, input_type: str) -> str:
        if input_type == "text":
            return f"Recognized text: {content}"
        elif input_type == "latex":
            return f"Recognized LaTeX: {content}"
        elif input_type == "image":
            return "Recognized image content: 2x + 3 = 7"
        else:
            return None

input_recognizer = InputRecognizer()