from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': os.environ.get('PG_NAME', 'dts_test_project'),
        'USER': os.environ.get('PG_USER'),
        'PASSWORD': os.environ.get('PG_PASSWORD'),
        'HOST': os.environ.get('PG_HOST'),
        'PORT': int(os.environ.get('PG_PORT')) if os.environ.get('PG_PORT') else None,
    }
}