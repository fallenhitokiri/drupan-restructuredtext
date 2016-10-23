# -*- coding: utf-8 -*-

"""
    drupan-restructuredtext

    Plugin that provides reStructuredText conversion using the docutils library
"""

from docutils.core import publish_parts


class Plugin(object):
    """convert entities content to reStructuredText"""
    def __init__(self, site, config):
        """
        Arguments:
            site: instance of drupan.site.Site
            config: instance of drupan.config.Config
        """
        self.site = site
        self.config = config

    def run(self):
        """run the plugin"""
        for entity in self.site.entities:
            if entity.raw:
                self.convert(entity)

    @staticmethod
    def convert(entity):
        """
        convert entity.raw to HTML and store it in entity.content

        Arguments:
            entity: instance of drupan.entity.Entity
        """
        entity.content = publish_parts(entity.raw, writer_name="html")["body"]
