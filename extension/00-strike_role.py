from docutils import nodes
from docutils.parsers.rst import roles

from nikola.plugin_categories import RestExtension


class Plugin(RestExtension):

    name = "strike_role"

    def set_site(self, site):

        # Insert logic here

        return super(Plugin, self).set_site(site)
