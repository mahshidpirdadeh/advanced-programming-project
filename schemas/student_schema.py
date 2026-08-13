from pydantic import BaseModel, Field, field_validator
import re


class StudentCreate(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50, examples=["Mahshid"])

    last_name: str = Field(..., min_length=2, max_length=50,examples=["Pirdadeh"])

    @field_validator("first_name", "last_name")
    @classmethod
    def validate_name(cls, value: str):
        # فقط حروف انگلیسی
        if not re.fullmatch(r"[A-Za-z]+", value):
            raise ValueError("Name must contain only English letters.")

        # حرف اول باید بزرگ باشد
        if not value[0].isupper():
            raise ValueError("The first letter must be uppercase.")

        return value
    student_number:str = Field(..., min_length=3, max_length=30,examples=["40411415030"])
    major:str = Field(..., min_length=2, max_length=80,examples=["Computer Engineering"])

from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional


class EmailTemplate(BaseModel):
    subject: str = Field(..., min_length=3, max_length=100)
    sender: EmailStr
    recipients: List[EmailStr]
    cc: Optional[List[EmailStr]] = None
    bcc: Optional[List[EmailStr]] = None
    body: str = Field(..., min_length=10)
    is_html: bool = False

class StudentUpdate(BaseModel):
    first_name: str | None= Field(default=None, min_length=2, max_length=50)

    last_name: str | None= Field(default=None, min_length=2, max_length=50)

    @field_validator("first_name", "last_name")
    @classmethod
    def validate_name(cls, value: str):
        # فقط حروف انگلیسی
        if not re.fullmatch(r"[A-Za-z]+", value):
            raise ValueError("Name must contain only English letters.")

        # حرف اول باید بزرگ باشد
        if not value[0].isupper():
            raise ValueError("The first letter must be uppercase.")

        return value
    student_number:str | None= Field(default=None, min_length=3, max_length=30)
    major:str | None= Field(default=None, min_length=2, max_length=80)

from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional


class EmailTemplate(BaseModel):
    subject: str = Field(default=None, min_length=3, max_length=100)
    sender: EmailStr
    recipients: List[EmailStr]
    cc: Optional[List[EmailStr]] = None
    bcc: Optional[List[EmailStr]] = None
    body: str = Field(..., min_length=10)
    is_html: bool = False