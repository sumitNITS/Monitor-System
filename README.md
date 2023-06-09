## Web App to Monitor Your System Health 

![monitorsystem](https://user-images.githubusercontent.com/37767537/232860146-e4475b3d-9f17-432e-ac0e-a6fc6003fde3.png)

### A Few features of this project include

- Monitors CPU Utilization ✔️
- Monitors Memory Utilization ✔️
- Monitors Disk Utilization ✔️
- Gives System Information including Hostname, CPU Count, and Disk Partitions as well as shows the message of CPU, Mem, and Disk metrics as normal when it is utilized below 80% and shows an alert message when utilized above 80% 😎

### Instructions to run this project locally

- Create a project directory called System Monitoring
- cd to System Monitoring
- Clone this project using the command
```bash
git clone https://github.com/sumitNITS/Monitor-System.git
```
- cd to Monitor-System
- Install all the dependencies for this project using the command
```bash
pip install -r app_requirement.txt
```
- Run the below command to start the application
```bash 
python app.py
```

Now visit the URL http://127.0.0.1:5000/ and explore the application 🚀

### Instructions to run this project as Docker container

- Clone this project using the command
```bash
git clone https://github.com/sumitNITS/Monitor-System.git
```
- cd to Monitor-System
- Build an image out of Dockerfile using the command 
```bash
docker build . -t <image-name>
```
- Start the container with the docker image using the command
```bash
docker run -d -p <port>:5000 --name monitorsystem <image-name> 
```
Now access the application using "localhost":"port" OR "ip-of-machine":"port" 🚀


### Instructions to run this project using dockerhub image

- Access the application using the command 
```bash
docker run -d -p <port>:5000 --name monitorsystem sumit0058/monitorsystem
```

### Instructions to run this project in local Kubernetes minikube 

- Clone this project using the command
```bash
git clone https://github.com/sumitNITS/Monitor-System.git
```
- Start minikube 
- cd to Monitor-System
- Run the below commands 
```bash
kubectl apply -f monitorsystem-deployment.yml
```

```bash
kubectl apply -f monitorsystem-service.yml
```

```bash
kubectl port-forward service/monitorsystem-deployment <port>:5000
```

Now access the application using "localhost":"port" OR "ip-of-machine":"port" 🚀

### Want to improve this application?

Please follow the [Contributing Guidelines](https://github.com/sumitNITS/Monitor-System/blob/main/CONTRIBUTING.md)