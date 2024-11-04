import os
import chainlit as cl
from dotenv import load_dotenv
from openai import AsyncOpenAI
# import gettext

# gettext.translation('my_app',localedir='locals', languages=['en']).install()


load_dotenv()
cl.instrument_openai()


token = os.getenv("TOKEN")
endpoint = "https://models.inference.ai.azure.com"

client =AsyncOpenAI(base_url=endpoint, api_key=token)

settings = {
    "model": "gpt-4o-mini",
    "temperature": 0,
  
}

@cl.on_message
async def on_message(message: cl.Message,):
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "You are a helpful bot. your job is to get a question from the user as well as a context. you are to answer the question based on the context provided this is very key do not go against protocol, do not add any additional information as to whether the context is right or wrong just answer.",
                "role": "system"
            },
            {
                "content": message.content,
                "role": "user"
            }
        ],
        **settings
       
    )
    await cl.Message(content=response.choices[0].message.content).send()