import sublime, sublime_plugin

pfields = [("p.ArticleCategorization\tp.field","p.ArticleCategorization"),
           ("p.AssociatedUsers\tp.field","p.AssociatedUsers"),
           ("p.AutoContentCreator\tp.field","p.AutoContentCreator"),

           ("p.BatchOperation\tp.field","p.BatchOperation"),
           
           ("p.CategorizedSearch\tp.field","p.CategorizedSearch"),
           ("p.Checkbox\tp.field","p.Checkbox"),
           ("p.ContentCreator\tp.field","p.ContentCreator"),
           ("p.ContentFileSelect\tp.field","p.ContentFileSelect"),
           ("p.ContentList\tp.field","p.ContentList"),
           ("p.ContentListEntryContainer\tp.field","p.ContentListEntryContainer"),
           ("p.ContentListProperties\tp.field","p.ContentListProperties"),
           ("p.ContentName\tp.field","p.ContentName"),
           ("p.ContentSelect\tp.field","p.ContentSelect"),
           ("p.ContentSingleSelect\tp.field","p.ContentSingleSelect"),
           ("p.ContentTreeSelect\tp.field","p.ContentTreeSelect"),
           ("p.ContentTypeSelect\tp.field","p.ContentTypeSelect"),
           ("p.ContentVersionLimiter\tp.field","p.ContentVersionLimiter"),
           ("p.CustomContentList\tp.field","p.CustomContentList"),
           ("p.CustomContentListProperties\tp.field","p.CustomContentListProperties"),
           
           ("p.OptionalDateTime\tp.field","p.OptionalDateTime"),
           
           ("p.DeepCopy\tp.field","p.DeepCopy"),
           ("p.DeepCopyXML\tp.field","p.DeepCopyXML"),
           ("p.DeleteState\tp.field","p.DeleteState"),
           ("p.Duplicator\tp.field","p.Duplicator"),
      
           ("p.ExternalId\tp.field","p.ExternalId"),
           
           ("p.FCKEditor\tp.field","p.FCKEditor"),
           ("p.FileManager\tp.field","p.FileManager"),
           ("p.FileSelect\tp.field","p.FileSelect"),
           ("p.SimpleFileUpload\tp.field","p.SimpleFileUpload"),
           
           ("p.FormBuilder\tp.field","p.FormBuilder"),
           ("p.Hidden\tp.field","p.Hidden"),
           ("p.HomeDepartmentCreator\tp.field","p.HomeDepartmentCreator"),
           ("p.HttpImageManager\tp.field","p.HttpImageManager"),
           
           ("p.ImageEditor\tp.field","p.ImageEditor"),
           ("p.ImageManager\tp.field","p.ImageManager"),
           ("p.InheritWorkflow\tp.field","p.InheritWorkflow"),
  
           ("p.NameValue\tp.field","p.NameValue"),
           
           ("p.ModerationState\tp.field","p.ModerationState"),
           ("p.MultiTypeDuplicator\tp.field","p.MultiTypeDuplicator"),
           
           ("p.OutputTemplateSelect\tp.field","p.OutputTemplateSelect"),

           ("p.ParentSelect\tp.field","p.ParentSelect"),
           ("p.PropertyEditor\tp.field","p.PropertyEditor"),
           ("p.OnlineState\tp.field","p.OnlineState"),
           ("p.RadioButtonGroup\tp.field","p.RadioButtonGroup"),
           ("p.ReferringContentListing\tp.field","p.ReferringContentListing"),
           ("p.ResourceBundleManager\tp.field","p.ResourceBundleManager"),
           ("p.ResourceList\tp.field","p.ResourceList"),
           
           ("p.SecurityParentSelect\tp.field","p.SecurityParentSelect"),
           ("p.Select\tp.field","p.Select"),
           ("p.SelectableSubField\tp.field","p.SelectableSubField"),
           ("p.SingleValueSelect\tp.field","p.SingleValueSelect"),
           ("p.SimpleContentCreator\tp.field","p.SimpleContentCreator"),
           ("p.siteengine.Content.Categorization\tp.field","p.siteengine.Content.Categorization"),
           ("p.siteengine.layout.Slot.it\tp.field","p.siteengine.layout.Slot.it"),
           ("p.SiteSelect\tp.field","p.SiteSelect"),
           ("p.solr.LocalContentSearch\tp.field","p.solr.LocalContentSearch"),

           ("p.TextArea\tp.field","p.TextArea"),
           ("p.TextInput\tp.field","p.TextInput"),
           ("p.TextOutput\tp.field","p.TextOutput"),
           ("p.TimeState\tp.field","p.TimeState"),
           ("p.TimeStateFixedViewTime\tp.field","p.TimeStateFixedViewTime"),

           ("p.VersionDescription\tp.field","p.VersionDescription"),
           ("p.VirtualDomainCreator\tp.field","p.VirtualDomainCreator"),
           ("p.VirtualDomainEditor\tp.field","p.VirtualDomainEditor"),

           ("p.WebAliasCreator\tp.field","p.WebAliasCreator"),
           ("p.WebAliasEditor\tp.field","p.WebAliasEditor"),
           ("p.WorkflowAction\tp.field","p.WorkflowAction"),
           ("p.WorkflowSelect\tp.field","p.WorkflowSelect"),
           ("p.WorkflowToInheritSelect\tp.field","p.WorkflowToInheritSelect"),
           ("p.WorkflowTypeSelect\tp.field","p.WorkflowTypeSelect"),

           ("p.QuickCreator.Preferences\tp.field","p.QuickCreator.Preferences")]

playouts = [("p.Column\tp.layout","p.Column"),
            ("p.ColumnHolder\tp.layout","p.ColumnHolder"),
            ("p.Comment\tp.layout","p.Comment"),
            ("p.ExpandableNavSection\tp.layout","p.ExpandableNavSection"),
            ("p.Group\tp.layout","p.Group"),
            ("p.HorizontalGroup\tp.layout","p.HorizontalGroup"),
            ("p.Page\tp.layout","p.Page"),
            ("p.PageMenu\tp.layout","p.PageMenu"),
            ("p.AjaxPageMenu\tp.layout","p.AjaxPageMenu"),
            ("p.LabeledSection\tp.layout","p.LabeledSection")]

pguifields = [("p.WorkPaneHandler\tp.guifield","p.WorkPaneHandler"),
              ("p.PreviewControl\tp.guifield","p.PreviewControl"),
              ("p.PerspectiveControl\tp.guifield","p.PerspectiveControl")]

def all_fields_layouts():
    return pfields + playouts + pguifields

class pFieldsLayoutsCompletions(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "source.xml"):
            return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        if ch != '.':
            return []

        pfields_layouts = all_fields_layouts()
        pfields_layouts.sort()
        return (pfields_layouts, sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)