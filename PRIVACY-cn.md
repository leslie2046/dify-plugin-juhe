## 聚合数据插件隐私政策

该插件作为客户端，用于向聚合数据API服务发送各类API请求。

**数据收集：**

为了正常运行，该插件需要用户在 Dify 设置过程中提供相关的凭证，每个API都有独立的 API KEY：

* `apiKey`：用于验证身份的 API 密钥。

在使用插件工具时，可能会处理并发送以下数据到聚合数据：

* 用户查询字段值（城市名、货币代码），用于查询天气、汇率。


**数据使用：**

* 收集的凭证（`apiKey`）仅用于聚合数据API的请求。
* 用户查询字段值（城市名、货币代码）会直接通过 API 发送到聚合数据。
* 插件本身不会在运行上下文之外持久存储任何用户数据或凭证。所有数据都仅用于执行请求时通过 API 传输。

**第三方服务 / 自建托管：**

* [聚合数据的隐私政策](https://www.juhe.cn/privacy)。


**联系方式：**

如有关于本插件隐私实践的疑问，请联系作者：[leslie2046](https://github.com/leslie2046)。关于 Juhe 本身的相关问题，请参考 https://www.juhe.cn/。