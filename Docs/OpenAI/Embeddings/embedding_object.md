The embedding object

Represents an embedding vector returned by embedding endpoint.
index
integer

The index of the embedding in the list of embeddings.
embedding
array

The embedding vector, which is a list of floats. The length of vector depends on the model as listed in the embedding guide.
object
string

The object type, which is always "embedding".


{
  "object": "embedding",
  "embedding": [
    0.0023064255,
    -0.009327292,
    .... (1536 floats total for ada-002)
    -0.0028842222,
  ],
  "index": 0
}
