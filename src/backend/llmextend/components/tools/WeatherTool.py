from typing import Any

from langchain.tools import Tool

from langflow import CustomComponent


class WeatherToolHandle(CustomComponent):
    display_name: str = "查询天气"
    description: str = "当需要查看城市天气时，你可以使用该工具"

    def build(self) -> Tool:
        def query_weather(city: str):
            print("call me ......")
            return f"{city} 天气晴，气温29度"

        return Tool.from_function(func=query_weather, name="query_weather", description=self.description)
