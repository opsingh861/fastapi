# from datetime import datetime
# from pydantic import BaseModel

# class User(BaseModel):
#     id: int | str
#     name: str = "John Doe"
#     signup_ts: datetime | None = None
#     friends: list[int] = []

# external_data = {
#     "id": "123",  # Ensure id is a single value of type int or str
#     "signup_ts": "2017-06-01T12:22",  # Ensure signup_ts is a valid datetime string
#     "friends": [1, 2, 3],  # Ensure friends list contains only int values
# }
# user = User(**external_data)
# print(user)
# print(user.id)
