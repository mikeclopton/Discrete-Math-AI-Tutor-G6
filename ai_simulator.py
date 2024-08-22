class AISimulator:
    def generate_response(self, question: str) -> str:
        return f"Here's a step-by-step solution for '{question}':\n1. First, we need to...\n2. Then, we can...\n3. Finally, we conclude that..."

ai_simulator = AISimulator()