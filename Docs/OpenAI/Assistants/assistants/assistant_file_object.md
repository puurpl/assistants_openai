The assistant file objectBeta

A list of Files attached to an assistant.
id
string

The identifier, which can be referenced in API endpoints.
object
string

The object type, which is always assistant.file.
created_at
integer

The Unix timestamp (in seconds) for when the assistant file was created.
assistant_id
string

The assistant ID that the file is attached to.



{
  "id": "file-abc123",
  "object": "assistant.file",
  "created_at": 1699055364,
  "assistant_id": "asst_abc123"
}
