The run objectBeta

Represents an execution run on a thread.
id
string

The identifier, which can be referenced in API endpoints.
object
string

The object type, which is always thread.run.
created_at
integer

The Unix timestamp (in seconds) for when the run was created.
thread_id
string

The ID of the thread that was executed on as a part of this run.
assistant_id
string

The ID of the assistant used for execution of this run.
status
string

The status of the run, which can be either queued, in_progress, requires_action, cancelling, cancelled, failed, completed, or expired.
required_action
object or null

Details on the action required to continue the run. Will be null if no action is required.
last_error
object or null

The last error associated with this run. Will be null if there are no errors.
expires_at
integer

The Unix timestamp (in seconds) for when the run will expire.
started_at
integer or null

The Unix timestamp (in seconds) for when the run was started.
cancelled_at
integer or null

The Unix timestamp (in seconds) for when the run was cancelled.
failed_at
integer or null

The Unix timestamp (in seconds) for when the run failed.
completed_at
integer or null

The Unix timestamp (in seconds) for when the run was completed.
model
string

The model that the assistant used for this run.
instructions
string

The instructions that the assistant used for this run.
tools
array

The list of tools that the assistant used for this run.
file_ids
array

The list of File IDs the assistant used for this run.
metadata
map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.


{
  "id": "run_abc123",
  "object": "thread.run",
  "created_at": 1698107661,
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "completed",
  "started_at": 1699073476,
  "expires_at": null,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": 1699073498,
  "last_error": null,
  "model": "gpt-4",
  "instructions": null,
  "tools": [{"type": "retrieval"}, {"type": "code_interpreter"}],
  "file_ids": [],
  "metadata": {}
}
