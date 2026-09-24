from fastapi import FastAPI,Depends,HTTPException,status
from contextlib import contextmanager,asynccontextmanager
from sqlmodel import SQLModel,Session,select
from schemas import location_of_obj,item,status_of_obj,item_update
from sessions import create_db_and_table,get_session
from models import Item

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db_and_table()
    yield 
app=FastAPI(lifespan=lifespan)

@app.post("/items")
def new_item(data:item,session:Session=Depends(get_session)):
    db_item = Item(**data.model_dump())
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

@app.get("/items")
def get_all_items(session:Session=Depends(get_session)):
    items=session.exec(select(Item)).all()
    return items


@app.get("/items/{item_id}")
def get_or_return404(item_id:int,session: Session = Depends(get_session)):
    item= session.get(Item,item_id)
    if item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no product with this id")
    return item

@app.put("/items/{item_id}")
def update_item(item_id:int,data:item_update,session:Session=Depends(get_session)):
    item=session.get(Item,item_id)
    item.sqlmodel_update(data.model_dump(exclude_unset=True))
    session.add(item)
    session.commit()
    session.refresh(item)
    if item is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no product with this id")
    return item

@app.delete("/items/{item_id}")
def remove_item(item_id:int,data:item,session:Session=Depends(get_session)):
    item=session.get(Item,item_id)
    if item is None:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no product with this id")
    session.delete(item)
    session.commit()
    return{"detail":f"item with {item_id} is deleted"}

@app.get("/items/status/{item_status}")
def return_item_of_status(item_status: status_of_obj,session: Session = Depends(get_session)):
    items = session.exec( select(Item).where(Item.status == item_status)).all()

    return items


@app.get("/items/category/{category}")
def return_item_of_category(category: location_of_obj,session: Session = Depends(get_session)):
    items = session.exec(select(Item).where(Item.category == category)).all()

    return items
