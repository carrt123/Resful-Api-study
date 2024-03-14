主要对Restful Api学习，包括

api 绑定resource
resource、service编写风格
postman工具协助CRUD操作，上传和下载文件
flask-resful、flask-restful-swagger-3， 如何自动生成swagger.yaml风格文档和对应swagger-ui
设计schema函数：例如  @use_kwargs(BookRequestSchema, location='json')  # 在json里， 按照BookRequestSchema定义提取参数
                    @use_kwargs(TokenSchema, location='headers')      # 在headers 按照TokenSchema 定义提取参数
 flask_apispec  @doc(description="Update book's information", tags=['Book Requests']) # 在swagger 描述此函数的作用

ORM查询操作
jwt_token api访问限制

@wraps装饰器用法， 在执行一个函数前先执行@wrap定义的函数，如果没问题重新返回执行。

