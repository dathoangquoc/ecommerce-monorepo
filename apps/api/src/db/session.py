from sqlalchemy import create_engine, text

from .config import DBSettings

engine = create_engine(
    url=f"postgresql://{DBSettings.USERNAME}:{DBSettings.PASSWORD}@{DBSettings.HOST}:{DBSettings.PORT}/{DBSettings.DB_NAME}"
)

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())