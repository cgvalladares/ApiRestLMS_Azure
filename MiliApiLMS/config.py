import urllib

class JWT:
    #JWT
    JWT_SECRET_KEY  = 'fgjtd8973aac402d8761016e83767ba4'
    #eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiTGVjIn0.AOY8uoWhwCQkzugKoIoXrVDYuU5AYluaVWghUPzovzc
    
class Humbral:
    #humbral hash
    HUMBRAL_DHASH=6

class ConfigLocal:
    DEBUG=True
    TESTING=True
    #DB
    DB_SERVER = 'Progra2024-02\SQLSERVERLOCALM'
    DB_USER = 'sa'
    DB_PASSWORD = 'Geo4160150087.'
    DB_NAME = 'Fingerprintt'
    SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO=False
    
class ConfigTestDev:
    DEBUG= False
    TESTING= False
    #DB
    DB_SERVER = 'sdevtestlec.database.windows.net:1433'
    DB_USER = 'desarrollo'
    DB_PASSWORD = 'C0ntr0lT0t@l'
    DB_NAME = 'CT_Pruebas-2023_11_15-03_00_00'
    SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server&Encrypt=True&TrustServerCertificate=False&Connection Timeout=30&Authentication="Active Directory Default"'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO=False
    
class ConfigQa:
    DEBUG= True
    TESTING= False
    #DB
    DB_DRIVER='ODBC Driver 17 for SQL Server'
    DB_SERVER = 'pruebas-ct.database.windows.net:1433'
    DB_USER = 'desarrollo'
    DB_PASSWORD = 'C0ntr0lT0t@l'
    DB_NAME = 'CT_Pruebas-2024_02_09-03_00_00'
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver={DB_DRIVER}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO=True
    
class ConfigAzureGeo:
    DEBUG= False
    TESTING= False
    #DB
    #'mssql+pyodbc://geo22:Geo4160150087.@virtualpiserver.database.windows.net:1433/apirestlmsdb?driver=ODBC+Driver+17+for+SQL+Server'
    DB_SERVER = 'virtualpiserver.database.windows.net:1433'
    DB_USER = 'geo22'
    DB_PASSWORD = 'Geo4160150087.'
    DB_NAME = 'apirestlmsdb'
    SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver=ODBC Driver 17 for SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO=False
    
class ConfigAzurePrivado:
    #Server=tcp:virtualpiserver.database.windows.net,1433;Initial Catalog=privadodb;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;Authentication="Active Directory Default
    DEBUG= True
    TESTING= True
    #DB'
    DB_SERVER = 'virtualpiserver.database.windows.net:1433'
    DB_USER = 'geo22'
    DB_PASSWORD = 'Geo4160150087.'
    DB_NAME = 'privadodb'
    SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver 17 for SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO=True
    
class testAzure:
    DB_SERVER = 'virtualpiserver.database.windows.net:1433'
    DB_USER = 'geo22'
    DB_PASSWORD = 'Geo4160150087.'
    DB_NAME = 'privadodb'
    DB_DRIVER = "{ODBC Driver 17 for SQL Server}"
    conn = f"""Driver={DB_DRIVER};Server=tcp:{DB_SERVER},1433;Database={DB_NAME};
    Uid={DB_USER};Pwd={DB_PASSWORD};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"""

    params = urllib.parse.quote_plus(conn)
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?autocommit=true&odbc_connect={}'.format(params)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO=True

