from openai import OpenAI
client = OpenAI()

assistant_file = client.beta.assistants.files.retrieve(
  assistant_id="asst_abc123",
  file_id="file-abc123"
)
print(assistant_file)


"""Retrieve assistant fileBeta

get https://api.openai.com/v1/assistants/{assistant_id}/files/{file_id}

Retrieves an AssistantFile.
Path parameters
assistant_id
string
Required

The ID of the assistant who the file belongs to.
file_id
string
Required

The ID of the file we're getting.
Returns

The assistant file object matching the specified ID."""



"""{
  "id": "file-abc123",
  "object": "assistant.file",
  "created_at": 1699055364,
  "assistant_id": "asst_abc123"
}
"""