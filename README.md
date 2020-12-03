# micro_service_demo

## rpc protobuf 使用
### protobuf编写参考文档
> https://www.jianshu.com/p/4443c28d4bf7

### python3 库安装配置命令
> pip install futures==3.1.1  
> pip install grpcio protobuf grpcio-tools

### python2 库安装配置命令
> pip install grpcio protobuf grpcio-tools

### rpc python 代码自动生成命令
> python -m grpc_tools.protoc -I. --python_out={输出路径} --grpc_python_out={输出路径} {接口文件定义路径}  
> 如 python -m grpc_tools.protoc -I. --python_out=./ --grpc_python_out=./ ./protos/micro_service.proto


## peewee 访问mysql数据库
### peewee 使用参考文档
> http://docs.peewee-orm.com/en/latest/index.html

### peewee 库安装命令
> pip install peewee

### peewee 运行demo
> tests/peewee_test.py


## consul服务注册、发现
### consul python库安装命令
> pip install python-consul

### python 使用代码参考
> tests/consul.py


## 容器命令使用
### 容器镜像配置
> 编写requirements.txt，如下格式为"{package_name}=={package_version}"，依赖包版本可以通过 "pip show {package_name}" 查看
```requirements.txt
peewee==3.13.3
futures==3.1.1
grpcio==1.32.0
protobuf==3.13.0
grpcio-tools==1.32.0
python-consul==1.1.0
redis==3.4.1
pymysql==0.9.3
ronglian_sms_sdk==1.0
```
> 编辑文件 Dockerfile（命令参考https://www.runoob.com/docker/docker-dockerfile.html），如下：
```dockerfile
FROM python:3.7
MAINTAINER Zhengjiaqi
RUN mkdir -p /service/src
WORKDIR /service/src
COPY requirements.txt /service/src
RUN pip install --no-cache-dir -r requirements.txt
COPY . /service/src
EXPOSE 31019
CMD ["python", "main.py"]
```

### 容器镜像创建命令
######## 创建镜像
> docker build -t '13070163997/micro_service_server:v1.0.1' .  
######## 镜像推送至镜像仓库
> docker push 13070163997/micro_service_server:v1.0.1

### 容器镜像本地docker测试相关命令（感兴趣的同学可以自学下 docker 的使用：https://www.runoob.com/docker/docker-tutorial.html）
######## 由镜像创建容器
> docker run -itd --name {容器名} -p {机器端口}:{容器端口} {镜像名}  
> 如：docker run -itd --name micro_service -p 30019:30019 13070163997/micro_service_server:v1.0.1
######## 查看容器id
> docker ps
######## 进入容器命令行
> docker exec -it {容器id} /bin/bash

### k8s 部署服务
######## 编写 kubernetes_yamls/micro_service.deployment.yml 
```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: micro-service
  namespace: exp-code
spec:
  replicas: 1
  template:
    metadata:
      labels:
        k8s-app: micro-service
    spec:
      hostNetwork: true
      containers:
      - name: micro-service
        image: 13070163997/micro_service_server:v1.0.1
        imagePullPolicy: "IfNotPresent"
        ports:
        - containerPort: 31019
```
######## 编写 kubernetes_yamls/micro_service.service.yml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: micro-service
  namespace: exp-code
  labels:
    k8s-app: micro-service
spec:
  type: NodePort
  ports:
  - port: 31019
    targetPort: 31019
    nodePort: 30019
  selector:
    k8s-app: micro-service
```
######## 部署deployment命令（或者 k8s-dashboard 界面执行）
> kubectl -f kubernetes_yamls/micro_service.deployment.yml  
######## 部署service命令（或者 k8s-dashboard 界面执行）
> kubectl -f kubernetes_yamls/micro_service.service.yml

