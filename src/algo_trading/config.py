from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "dev"
    broker: str = "dhan"
    log_level: str = "INFO"

    dhan_client_id: str = ""
    dhan_access_token: str = ""
    dhan_api_base_url: str = "https://api.dhan.co"

    max_daily_loss: float = 5000
    max_position_qty: int = 100
    risk_per_trade: float = 0.01

    slack_webhook_url: str = ""
    webhook_host: str = "0.0.0.0"
    webhook_port: int = 8080

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


settings = Settings()
