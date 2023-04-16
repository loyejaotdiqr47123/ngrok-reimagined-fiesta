
# 生成证书
echo "下载生成证书..."
cd ~/.cloudflared && wget https://raw.githubusercontent.com/loyejaotdiqr47123/ngrok-reimagined-fiesta/main/cert.pem
# 启动隧道
echo "正在启动 Cloudflare 隧道..."
cloudflared tunnel create up-codesandbox
cloudflared tunnel route dns up-codesandbox up-codesandbox.bobocdn.tk
cloudflared tunnel run 
#```

#在这个脚本中，我们只更改了 `LOCAL_PORT` 变量的值为 `3001`。如果您还需要更改其他变量，请根据您的需求进行修改。
