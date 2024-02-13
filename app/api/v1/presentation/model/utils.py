from pydantic import Field

SNOWFLAKE_FIELD = Field(pattern=r"^\d*$", min_length=17, max_length=19)
