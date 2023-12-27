from openai import OpenAI
client = OpenAI()

message = client.beta.threads.messages.retrieve(
  message_id="msg_abc123",
  thread_id="thread_abc123",
)
print(message)



"""Retrieve messageBeta

get https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}

Retrieve a message.
Path parameters
thread_id
string
Required

The ID of the thread to which this message belongs.
message_id
string
Required

The ID of the message to retrieve.
Returns

The message object matching the specified ID."""



"""{
  "id": "msg_abc123",
  "object": "thread.message",
  "created_at": 1699017614,
  "thread_id": "thread_abc123",
  "role": "user",
  "content": [
    {
      "type": "text",
      "text": {
        "value": "How does AI work? Explain it in simple terms.",
        "annotations": []
      }
    }
  ],
  "file_ids": [],
  "assistant_id": null,
  "run_id": null,
  "metadata": {}
}
"""