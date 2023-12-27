The assistant objectBeta

Represents an assistant that can call the model and use tools.
id
string

The identifier, which can be referenced in API endpoints.
object
string

The object type, which is always assistant.
created_at
integer

The Unix timestamp (in seconds) for when the assistant was created.
name
string or null

The name of the assistant. The maximum length is 256 characters.
description
string or null

The description of the assistant. The maximum length is 512 characters.
model
string

ID of the model to use. You can use the List models API to see all of your available models, or see our Model overview for descriptions of them.
instructions
string or null

The system instructions that the assistant uses. The maximum length is 32768 characters.
tools
array

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types code_interpreter, retrieval, or function.
file_ids
array

A list of file IDs attached to this assistant. There can be a maximum of 20 files attached to the assistant. Files are ordered by their creation date in ascending order.
metadata
map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.



{
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
