# -*- coding: utf8 -*-
#
# (c) Polopoly AB (publ).
# This software is protected by copyright law and international copyright
# treaties as well as other intellectual property laws and treaties.
# All title and rights in and to this software and any copies thereof
# are the sole property of Polopoly AB (publ).
# Polopoly is a registered trademark of Polopoly AB (publ).

import sublime
import sublime_plugin

# Modify from HTML completions
# Provide completions that match just after typing an hash
class PolopolyDirectivesCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        # Only trigger within Velocity Polopoly
        if not view.match_selector(locations[0], "source.vm.polopoly"):
            return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        if ch != '#':
            return []

        return ([
            ("file\tp.Directive", "file({\"filename\": \\$${1:path}, \"contentId\": \\$${2:content.contentId}, \"\":\"\"})"),

            ("render(outputTemplate)\tp.Directive", "render({\"outputTemplate\": \"${1:template}.ot\", \"\":\"\"})"),
            ("render(contentId)\tp.Directive", "render({\"contentId\": \\$${1:contentId}, ${2:\"params\": \\{\"mode\": \"link\", \"\":\"\"\\}, } \"\":\"\"})"),
            ("render(content)\tp.Directive", "render({\"content\": \\$${1:content}, ${2:\"params\":\\{\"view\":\"article\", \"\":\"\"\\}, } \"\":\"\" })"),

            ("link(path)\tp.Directive", "link({\"path\": \\$${1:parentIds}, 'htmlEncodeLink': 'true', \"\":\"\"})"),
            ("link(contentId)\tp.Directive", "link({\"contentId\": \\$${1:parentIds}, 'htmlEncodeLink': 'true', \"\":\"\"})"),
            ("link(path contentId)\tp.Directive", "link({\"path\": \\$${1:path}, \"contentId\": \\$${2:contentId}, 'htmlEncodeLink': 'true', \"\":\"\"})"),
            ("link(complex)\tp.Directive", "link({\"path\": \\$${1:path},\n\t\t\"contentId\": \\$${2:contentId},\n\t\t'htmlEncodeLink': 'true',\n\t\t${3:\"requestAttribs\": \\{\"localLinksEnabled\": \"false\"\\},}\n\t\t${4:\"contentParams\": \\{\\$${5:contentId} : \\{\"category\":\\$${6:categoryId}, \"dimension\":\\$${7:dimensionId}, \"\":\"\"\\}, \"\":\"\" \\},}\n\t\t\"\":\"\"})"),

            ("imageresource\tp.Directive", "imageresource({\"contentId\": \\$${1:contentId},\n\t\t\t\t\"derivative\": \"${2:landscape_490}\",\n\t\t\t\t\"alt\": ${3:\"\"},\n\t\t\t\t\"\":\"\"})")
        ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)