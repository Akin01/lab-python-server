"""Scenes for the ext module
"""

from fastapi import APIRouter, Request

from ....db import session_context
from .... import logger

router = APIRouter(tags=["ext"])

@router.get("/echo")
async def echo(request: Request):
    """Echo back a response to say hello.

    Purpose of this endpoint is to echo back what was received, this merely
    validated that the server is up and running.
    """
    return {"message": "Hello, world!"}

@router.get("/healthcheck")
async def healthcheck(request: Request):
    """Check the health of the server.

    Purpose of this endpoint is to check the health of the server.
    We check for connection to the database, queue and logger
    """
    async with session_context() as session:
        return {"message": "ok"}


@router.get("/log")
async def log(request: Request):
    """Log a message.

    Purpose of this endpoint is to log a message to the logger.
    """
    logger.emit('follow', {'from': 'userA', 'to': 'userB'})
    return {"message": "ok"}