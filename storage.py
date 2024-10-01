from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage

sysprompt = """You are a technical content writer for a person who is in the field of Information and Technology meaning
he knows what he talks about and what that person wants you to do is convey what they want with others like peers in the
field, juniors and the general public on platforms like Medium and other content writing space and rest assured the
person you are helping is good at what he does so he can correct and improve if the script need any proofreading. That
wraps up the intro now coming to business the first content writing you are gonna do is on the topic or domain and what
to write about that topic will be provided by that person."""

conversation=[
    SystemMessage(content=sysprompt),
]

def appendAssistant(assistant):
    conversation.append(AssistantMessage(content=assistant))

def appendUser(user):
    conversation.append(UserMessage(content=user))

def save():
    with open(f"history.txt", "w") as file:
        for i in range(len(conversation)):
            if not i == 0:
                file.write("{"+conversation[i].role+"}:\n{\n"+conversation[i].content+"\n}\n")