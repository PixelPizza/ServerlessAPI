from typing import Annotated

from fastapi import Depends

from .base import UserDAO
from .aws import AWSUserDAO
from .hardcoded import HardcodedUserDAO

UserDAODep = Annotated[UserDAO, Depends(AWSUserDAO)]
