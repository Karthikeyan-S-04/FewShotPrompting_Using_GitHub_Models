from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from env_set import secret_key
import storage as s

endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"
token = secret_key

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

user = input("##User:\n")

while not user.isspace():

    s.appendUser(user)

    response = client.complete(
        stream=True,
        messages= s.conversation,
        model=model_name,
        temperature=0.5,
        max_tokens=4096,
        top_p=1.0
    )

    res = ""
    print("\n##Assistant:")
    for update in response:
        if update.choices:
            if update.choices[0].delta.content is not None :
                res += update.choices[0].delta.content
                print(update.choices[0].delta.content or "", end="")

    s.appendAssistant(res)
    user = input("\n\n##User:\n")

s.save()