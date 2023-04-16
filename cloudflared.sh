#好的，以下是将 `LOCAL_PORT` 变量改为 `3001` 的示例脚本：

#```bash
#!/bin/bash

# 定义变量
TUNNEL_NAME="up-codesandbox"
DOMAIN_NAME="up-codesandbox.bobocdn.tk"
LOCAL_PORT="3001"
CLOUDFLARED_CONFIG_FILE="${HOME}/.cloudflared/up-codesandbox.yml"

# 检查是否已安装 Cloudflared
if ! command -v cloudflared &> /dev/null
then
    echo "Cloudflared 未安装，请先安装 Cloudflared。"
    exit
fi

# 检查 Cloudflared 配置文件是否存在
if [ ! -f "$CLOUDFLARED_CONFIG_FILE" ]
then
    echo "Cloudflared 配置文件不存在，将创建新的配置文件。"
    mkdir -p ${HOME}/.cloudflared
    touch "$CLOUDFLARED_CONFIG_FILE"
fi

# 生成隧道配置
echo "正在生成 Cloudflare 隧道配置..."
cat > "$CLOUDFLARED_CONFIG_FILE" << EOF
tunnel: $TUNNEL_NAME
credentials-file: ${HOME}/.cloudflared/$TUNNEL_NAME.json
ingress:
  - hostname: $DOMAIN_NAME
    service: http://localhost:$LOCAL_PORT
EOF

# 生成证书
echo "下载生成证书..."
cd ~/.cloudflared && wget https://raw.githubusercontent.com/loyejaotdiqr47123/ngrok-reimagined-fiesta/main/cert.pem
# 启动隧道
echo "正在启动 Cloudflare 隧道..."
cloudflared tunnel --hostname up-codesandbox.bobocdn.tk --url http://localhost:3001 --origincert ~/.cloudflared/cert.pem
#```

#在这个脚本中，我们只更改了 `LOCAL_PORT` 变量的值为 `3001`。如果您还需要更改其他变量，请根据您的需求进行修改。
