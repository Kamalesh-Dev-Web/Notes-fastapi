from fastapi import APIRouter,HTTPException
from models import Note,UpdateNote
from typing import List,Union
from beanie import PydanticObjectId

notes_router=APIRouter()

@notes_router.get('/')
async def get_all_notes():
    result = await Note.find_all().to_list()
    return result

@notes_router.post('/')
async def create_note(note:Note):
    await note.create()
    print(note)
    return note      
 

@notes_router.put('/{note_id}')
async def update_note(note:UpdateNote,note_id:PydanticObjectId) -> Note:
    result= await Note.get(note_id)
    if not result:
         raise HTTPException(status_code=404,detail='Item not found')
    if note.title!= None:
        result.title=note.title
    if note.created_date!= None:
        result.created_date=note.created_date
    if note.updated_date!= None:
        result.updated_date=note.updated_date
    if note.is_completed!= None:
        result.is_completed=note.is_completed
    await result.save()
    return result

@notes_router.delete('/{note_id}')
async def delete_note(note_id:PydanticObjectId):
    result=await Note.get(note_id)
    await result.delete()
    return {'Deleted succcessfully'}       
       
   

# @movies_router.post('/')
# async def createmovie(movie:Movie):
#     await movie.create()
    
#     return movie

# @movies_router.get('/{movie_id}')
# async def getmovie(movie_id:PydanticObjectId) -> Movie:
#     result=await Movie.get(movie_id)
#     return result

# @movies_router.put('/{movie_id}')
# async def updatemovie(movie:UpdateMovie,movie_id:PydanticObjectId) -> Movie:
#     print (movie)
#     result= await Movie.get(movie_id)
#     print (result)
#     if not result:
#         raise HTTPException(status_code=404,detail='Item not found')
    
#     if movie.year!=None:
#        result.year=movie.year
#     if movie.rating!=None:
#        result.rating=movie.rating
#     if movie.image_url!=None:
#        result.image_url=movie.image_url
#     if movie.thumbnail!=None:
#        result.thumbnail=movie.thumbnail
#     if movie.description!=None:
#        result.description=movie.description
#     if movie.genre!=None:
#        result.genre=movie.genre
       
#     await result.save()
#     return result

# @movies_router.delete('/{movie_id}')
# async def deletemovie(movie_id:PydanticObjectId):
#     result=await Movie.get(movie_id)
#     await result.delete()
#     return {'message':'The movie is deleted successfully'}