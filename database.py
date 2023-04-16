from beanie import init_beanie
import motor

from models import Note


async def init_db():
    client=motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://kamalesh-mongo:5DMJb9SVwxps38mE@cluster0.h5lf0.mongodb.net/?retryWrites=true&w=majority")
    await init_beanie(database=client.notes, document_models=[Note])