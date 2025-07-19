from client import chat_with_gemini

class Agent:
    def __init__(self, role_prompt):
        self.role_prompt = role_prompt
        self.messages = [{"role": "system", "content": role_prompt}]

    def run(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        response = chat_with_gemini(self.messages)
        self.messages.append({"role": "assistant", "content": response})
        return response
