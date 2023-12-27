from openai import OpenAI
client = OpenAI()

run = client.beta.threads.create_and_run(
  assistant_id="asst_abc123",
  thread={
    "messages": [
      {"role": "user", "content": "Explain deep learning to a 5 year old."}
    ]
  }
)



"""Create thread and runBeta

post https://api.openai.com/v1/threads/runs

Create a thread and run it in one request.
Request body
assistant_id
string
Required

The ID of the assistant to use to execute this run.
thread
object
Optional
model
string or null
Optional

The ID of the Model to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.
instructions
string or null
Optional

Override the default system message of the assistant. This is useful for modifying the behavior on a per-run basis.
tools
array or null
Optional

Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.
metadata
map
Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.
Returns

A run object."""



"""{
  "id": "run_abc123",
  "object": "thread.run",
  "created_at": 1699076792,
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "queued",
  "started_at": null,
  "expires_at": 1699077392,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": null,
  "last_error": null,
  "model": "gpt-4",
  "instructions": "You are a helpful assistant.",
  "tools": [],
  "file_ids": [],
  "metadata": {}
}
"""