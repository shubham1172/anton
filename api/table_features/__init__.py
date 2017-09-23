# We do things under the table

import os
__all__ = [f[:-3] for f in os.listdir('./api/table_features') if f!="__init__.py"]
