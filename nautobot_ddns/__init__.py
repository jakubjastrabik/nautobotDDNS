VERSION = '1.0.4'

try:
    from nautobot.extras.plugins import PluginConfig
except ImportError:
    # Dummy for when importing outside of Nautobot
    class PluginConfig:
        pass

class NautobotDDNSConfig(PluginConfig):
    name = 'nautobot_ddns'
    verbose_name = 'Dynamic DNS'
    version = VERSION
    author = 'Jakub Jastrabik && Sander Steffann'
    author_email = 'jastrabik.kubko@gmail.com'
    description = 'Dynamic DNS Connector for Nautobot'
    base_url = 'nautobot_ddns'
    required_settings = []
    default_settings = {}

    def ready(self):
        super().ready()

        from . import signals


config = NautobotDDNSConfig