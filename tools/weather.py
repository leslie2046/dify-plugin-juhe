from typing import Any, Generator

import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class ToolInvokeError(Exception):
    pass


class WeatherTool(Tool):
    def _invoke(
        self, tool_parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage, None, None]:
        """
        调用天气查询工具
        """
        key = tool_parameters.get("apiKey", "")
        if not key:
            raise ToolProviderCredentialValidationError("请配置正确的 apiKey")

        city = tool_parameters.get("city", "")
        if not city:
            raise ToolInvokeError("请提供 city 参数")

        url = "http://apis.juhe.cn/simpleWeather/query"
        params = {
            "key": key,
            "city": city
        }

        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise ToolInvokeError(f"请求失败：{response.status_code} - {response.text}")
        yield self.create_text_message(response.text)

    def validate_credentials(self, parameters: dict[str, Any]) -> None:
        # 简单测试一下 key 是否有效
        parameters["city"] = "上海"
        for _ in self._invoke(parameters):
            break
