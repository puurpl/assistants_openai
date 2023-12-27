The run step objectBeta

Represents a step in execution of a run.
id
string

The identifier of the run step, which can be referenced in API endpoints.
object
string

The object type, which is always thread.run.step.
created_at
integer

The Unix timestamp (in seconds) for when the run step was created.
assistant_id
string

The ID of the assistant associated with the run step.
thread_id
string

The ID of the thread that was run.
run_id
string

The ID of the run that this run step is a part of.
type
string

The type of run step, which can be either message_creation or tool_calls.
status
string

The status of the run step, which can be either in_progress, cancelled, failed, completed, or expired.
step_details
object

The details of the run step.
last_error
object or null

The last error associated with this run step. Will be null if there are no errors.
expired_at
integer or null

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.
cancelled_at
integer or null

The Unix timestamp (in seconds) for when the run step was cancelled.
failed_at
integer or null

The Unix timestamp (in seconds) for when the run step failed.
completed_at
integer or null

The Unix timestamp (in seconds) for when the run step completed.
metadata
map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.


{
  "id": "step_abc123",
  "object": "thread.run.step",
  "created_at": 1699063291,
  "run_id": "run_abc123",
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "type": "message_creation",
  "status": "completed",
  "cancelled_at": null,
  "completed_at": 1699063291,
  "expired_at": null,
  "failed_at": null,
  "last_error": null,
  "step_details": {
    "type": "message_creation",
    "message_creation": {
      "message_id": "msg_abc123"
    }
  }
}
