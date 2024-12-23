from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27419615"))
    API_HASH = getenv("API_HASH", "2f4b181296f0a2615a85471a1c72df44")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "Sigma_officials")
    CHID = int(getenv("CHID", "-1002106964059"))
    SUDO = list(map(int, getenv("1534632634").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://rohitl3031:CNHkZh4Nkgv0mUuJ@cluster0.cgmci.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
