# from pydantic import BaseModel, RootModel
# from typing import List
# from datetime import datetime
#
#
# class TaskDue24OutputItem(BaseModel):
#     id: int
#     name: str
#     description: str
#     created_at: str
#     updated_at: str
#
#
# class TasksResponse(BaseModel):
#     tasks: List[TaskDue24OutputItem]
#
#


from pydantic import BaseModel
from datetime import datetime


# Define your Pydantic model
class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str
    created_at: datetime
    updated_at: datetime
    due_date: datetime
    project: int
