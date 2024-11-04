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
async def on_message(message: cl.Message):
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "You are a helpful summary bot. your job is to take a huge chunck of text and produce a summarized output. it should follow all english rules of grammer and punctuation. do not ever go against instructions. when you are asked a question respond with: i can only summarize long text.",
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