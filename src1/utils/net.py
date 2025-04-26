import winreg


def get_system_proxy():
    try:
        internet_settings = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
        )
        proxy_enable, _ = winreg.QueryValueEx(internet_settings, "ProxyEnable")
        if proxy_enable:
            proxy_server, _ = winreg.QueryValueEx(internet_settings, "ProxyServer")
            # 一般格式是 "127.0.0.1:8888" 或 "http=127.0.0.1:8888;https=127.0.0.1:8888"
            if "=" in proxy_server:
                proxies = dict(item.split("=") for item in proxy_server.split(";"))
                return proxies.get("http") or proxies.get("https")
            else:
                return proxy_server
    except FileNotFoundError:
        return None
