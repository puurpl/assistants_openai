from openai import OpenAI
client = OpenAI()

my_assistant = client.beta.assistants.create(
    instructions="You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
    name="Math Tutor",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4",
)
print(my_assistant)


"""Create assistantBeta
post https://api.openai.com/v1/assistants
Create an assistant with a model and instructions.

Request body
model
Required

ID of the model to use. You can use the List models API to see all of your available models, or see our Model overview for descriptions of them.
name
string or null
Optional

The name of the assistant. The maximum length is 256 characters.
description
string or null
Optional

The description of the assistant. The maximum length is 512 characters.
instructions
string or null
Optional

The system instructions that the assistant uses. The maximum length is 32768 characters.
tools
array
Optional
Defaults to []

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types code_interpreter, retrieval, or function.
file_ids
array
Optional
Defaults to []

A list of file IDs attached to this assistant. There can be a maximum of 20 files attached to the assistant. Files are ordered by their creation date in ascending order.
metadata
map
Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.
Returns

An assistant object."""



"""{
  "id": "asst_abc123",
  "object": "assistant",
  "created_at": 1698984975,
  "name": "Math Tutor",
  "description": null,
  "model": "gpt-4",
  "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
  "tools": [
    {
      "type": "code_interpreter"
    }
  ],
  "file_ids": [],
  "metadata": {}
}
"""