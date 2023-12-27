from openai import OpenAI

async def create_assistant(instructions, name, tools, model):
    client = OpenAI()
    my_assistant = await client.beta.assistants.create(
    instructions=instructions,
    name=name,
    tools=tools,
    model=model,
    )
    return(my_assistant)

async def list_assistants(order, limit):
    client = OpenAI()
    assistants = await client.beta.assistants.list(order, limit)
    return(assistants)

async def retrieve_assistant(assistant_id):
    client = OpenAI()
    my_assistant = await client.beta.assistants.retrieve(assistant_id)
    return(my_assistant)

async def modify_assistant(assistant_id, description, name, instructions, tools, file_ids, model):
    client = OpenAI()
    my_assistant = await client.beta.assistants.update(
    assistant_id=assistant_id,
    description=description,
    name=name,
    instructions=instructions,
    tools=tools,
    file_ids=file_ids,
    model=model,
    )
    return(my_assistant)

async def delete_assistant(assistant_id):
    client = OpenAI()
    deleted_assistant = await client.beta.assistants.delete(assistant_id)
    return(deleted_assistant)

async def create_assistant_file(assistant_id, file):
    client = OpenAI()
    assistant_file = await client.beta.assistants.files.create(
    assistant_id=assistant_id,
    file=file,
    )
    return(assistant_file)

async def list_assistant_files(assistant_id, order, limit):
    client = OpenAI()
    assistant_files = await client.beta.assistants.files.list(
    assistant_id=assistant_id,
    order=order,
    limit=limit,
    )
    return(assistant_files)

async def retrieve_assistant_file(assistant_id, file_id):
    client = OpenAI()
    assistant_file = await client.beta.assistants.files.retrieve(
    assistant_id=assistant_id,
    file_id=file_id,
    )
    return(assistant_file)

async def delete_assistant_file(assistant_id, file_id):
    client = OpenAI()
    deleted_assistant_file = await client.beta.assistants.files.delete(
        assistant_id=assistant_id,
        file_id=file_id
    )
    return(deleted_assistant_file)

