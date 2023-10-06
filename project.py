import pydantic_settings
import dotenv


class Config(pydantic_settings.BaseSettings):
    browserstack_username: str
    browserstack_accesskey: str
    remote_url: str = 'http://hub.browserstack.com/wd/hub'


config = Config(_env_file=dotenv.find_dotenv('.env'))
