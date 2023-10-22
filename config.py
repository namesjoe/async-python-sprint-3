from pydantic import BaseSettings


class Settings(BaseSettings):
    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = 8000
    CLIENT_RECEIVE_MESSAGES: bool = True
    CLIENT_SEND_MESSAGE: str = "Hello world!"
    CLIENT_SEND_RECIPIENT: str = None
    CLIENT_SEND_COMMENT: str = "This is a test comment."
    CLIENT_SEND_FILE_PATH: str = "example.txt"
    MAX_MESSAGES: int = 20
    MESSAGE_LIFETIME: int = 3600
    MAX_MESSAGE_SIZE: int = 5 * 1024 * 1024  # 5MB

