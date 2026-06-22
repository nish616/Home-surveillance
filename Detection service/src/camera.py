class Camera:
    def __init__(self, username, password, ip, port):
        self.username = username
        self.password = password
        self.ip = ip
        self.port = port
    
    def generate_rtsp_url(self):
        return f"rtsp://{self.username}:{self.password}@{self.ip}:{self.port}/"
