from .start import register_start
from .help import register_help
from .application import register_application

def register_handlers(dp):
    register_start(dp)
    register_help(dp)
    register_application(dp)
