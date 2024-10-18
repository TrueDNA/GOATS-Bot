from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    USE_RANDOM_DELAY_IN_RUN: bool = False
    RANDOM_DELAY_IN_RUN: list[int] = [0, 39915]

    REF_ID: str = "af9db1f7-e83d-43d0-b460-cee4dc465e5f"
    SLEEP_TIME: list[int] = [31600, 62400]
    
    USE_PROXY: bool = False


settings = Settings()


