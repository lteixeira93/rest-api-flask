# Project info
## apt requirements (Docker, Python, Heroku)

```bash
sudo apt update && \
sudo apt install python3-virtualenv apt-transport-https ca-certificates curl software-properties-common && \
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null && \
sudo apt update && \
apt-cache policy docker-ce && \
sudo apt install docker-ce && \
sudo systemctl status docker && \
sudo usermod -aG docker ${USER} && \
curl https://cli-assets.heroku.com/install.sh | sh
```

## Commands
```bash
python3 -m venv .venv
source .venv/bin/activate
docker build -t restapi:0.1 .
docker run -P restapi:0.1
docker exec -it restapi:0.1 sh
netstat -ln
ip a
"0.0.0.0" -> Bind socket in all interfaces (* Running on all addresses (0.0.0.0) - Get container IP)
curl localhost:32772/users
```

## Links
```
https://flask.palletsprojects.com/en/1.1.x/quickstart/
https://flask-restful.readthedocs.io/en/latest/
```