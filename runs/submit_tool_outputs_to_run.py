from openai import OpenAI
client = OpenAI()

run = client.beta.threads.runs.submit_tool_outputs(
  thread_id="thread_abc123",
  run_id="run_abc123",
  tool_outputs=[
    {
      "tool_call_id": "call_abc123",
      "output": "28C"
    }
  ]
)
print(run)



"""Submit tool outputs to runBeta

post https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}/submit_tool_outputs

When a run has the status: "requires_action" and required_action.type is submit_tool_outputs, this endpoint can be used to submit the outputs from the tool calls once they're all completed. All outputs must be submitted in a single request.
Path parameters
thread_id
string
Required

The ID of the thread to which this run belongs.
run_id
string
Required

The ID of the run that requires the tool output submission.
Request body
tool_outputs
array
Required

A list of tools for which the outputs are being submitted.
Returns

The modified run object matching the specified ID."""



"""{
  "id": "run_abc123",
  "object": "thread.run",
  "created_at": 1699075592,
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "queued",
  "started_at": 1699075592,
  "expires_at": 1699076192,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": null,
  "last_error": null,
  "model": "gpt-4",
  "instructions": "You tell the weather.",
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Determine weather in my location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state e.g. San Francisco, CA"
            },
            "unit": {
              "type": "string",
              "enum": [
                "c",
                "f"
              ]
            }
          },
          "required": [
            "location"
          ]
        }
      }
    }
  ],
  "file_ids": [],
  "metadata": {}
}
"""