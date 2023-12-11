class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'minha_chave_secreta_development'
    JWT_SECRET_KEY = 'minha_chave_secreta_jwt_development'
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = True
    JWT_SECRET_KEY = 'b1d26781-f4b9-4800-9086-7f72168d2ef8'


class ProductionConfig(Config):
    SECRET_KEY = '0dce8154-2df8-4c41-8c1c-2964445bf6e4'
    WTF_CSRF_ENABLED = True
    JWT_SECRET_KEY = 'f6f18618-c762-4fa2-b949-6810dd7f6f2d'


# Mapeamento de ambientes para configurações
app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}

# Configuração padrão
default_config = 'development'
