# Security!

import os
__all__ = [f[:-3] for f in os.listdir('./api/authorization') if f!="__init__.py" and f!="__pycache__"]
