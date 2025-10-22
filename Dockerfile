FROM python:3.12-slim  # 基于 Python 3.12 精简版镜像构建
WORKDIR /app           # 设置容器内工作目录为 /app
COPY requirements.txt . # 将本地依赖清单复制到容器工作目录
RUN pip install -r requirements.txt  # 安装项目依赖
COPY . .               # 将本地所有文件复制到容器工作目录
CMD ["python", "app.py"]  # 容器启动命令：运行应用主文件