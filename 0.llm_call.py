from agno.models.groq import Groq
from agno.models.message import Message

from dotenv import load_dotenv
load_dotenv()

model = Groq(id="openai/gpt-oss-120b")

msg = Message(
    role="user",
    content="Explique o que é teste de software em português.",
)

assistant_message = Message(role="assistant")

response = model.invoke(
    messages=[msg],
    assistant_message=assistant_message,
)

print(response.content)



