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

properties = [("id\tProperty", "id"),
              ("major\tProperty", "major"),
              ("inputtemplate\tProperty", "inputtemplate"),
              ("name\tProperty", "name"),
              ("securityparent\tProperty", "securityparent"),
              ("component\tProperty", "component"),
              ("ref\tProperty", "ref"),
              ("list\tProperty", "list"),
              ("publish\tProperty", "publish"),
              ("file\tProperty", "file"),
              ("template\tProperty", "template"),
              ("action\tProperty", "action")]

majors = [("majorconfig\tMajor","majorconfig"),
          ("article\tMajor","article"),
          ("department\tMajor","department"),
          ("content\tMajor","content"),
          ("layoutelement\tMajor","layoutelement"),
          ("workflowtype\tMajor","workflowtype"),
          ("workflow\tMajor","workflow"),
          ("referencemetadata\tMajor","referencemetadata"),
          ("inputtemplate\tMajor","inputtemplate"),
          ("outputtemplate\tMajor","outputtemplate"),
          ("appconfig\tMajor","appconfig"),
          ("userdata\tMajor","userdata"),
          ("community\tMajor","community")]

actions = [("approve\tWorkflow action","approve"),
           ("remove\tWorkflow action","remove"),
           ("draft\tWorkflow action","draft")]

def on_properties_completions(l):
    if(l == 'id:'): 
        return False
    elif(l == "major:"): 
        return False
    elif(l == "inputtemplate:"): 
        return False
    elif(l == "name:"): 
        return False
    elif(l == "securityparent:"): 
        return False
    elif(l == "component:"): 
        return False
    elif(l == "ref:"): 
        return False
    elif(l == "list:"): 
        return False
    elif(l == "publish:"): 
        return False
    elif(l == "file:"): 
        return False
    elif(l == "template:"): 
        return False
    elif(l == "action:"): 
        return False
    else:
        return True

class dotContentCompletions(sublime_plugin.EventListener):
    properties.sort()
    majors.sort()
    actions.sort()

    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "source.content"):
            return []

        loc = locations[0] - len(prefix)
        line = view.substr(sublime.Region(view.line(loc).begin(), loc))

        if line == 'major:':
            return (majors, sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
        elif line == 'action:':
            return (actions, sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
        elif on_properties_completions(line):
            return (properties, sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
        else:
          return []