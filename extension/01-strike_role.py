from docutils import nodes
from docutils.parsers.rst import roles

from nikola.plugin_categories import RestExtension


class Plugin(RestExtension):

    name = "strike_role"

    def set_site(self, site):

        def strike_role(role, rawtext, text, lineno, inliner,
                options={}, content=[]):
            return [nodes.raw('', '<del>{}</del>'.format(text),
                format='html')], []

        self.site = site
        roles.register_canonical_role('del', strike_role)
        return super(Plugin, self).set_site(site)
