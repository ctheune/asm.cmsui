# Copyright (c) 2011 Assembly Organizing
# See also LICENSE.txt

import asm.cms.redirect
import grok

grok.context(asm.cms.redirect.Redirect)

class Edit(asm.cmsui.form.EditionEditForm):

    grok.layer(asm.cmsui.interfaces.ICMSSkin)
    grok.name('edit')

    main_fields = grok.AutoFields(asm.cms.redirect.Redirect).select(
        'title', 'target_url')

class Index(grok.View):

    grok.layer(grok.IDefaultBrowserLayer)
    grok.name('index')

    def update(self):
        self.redirect(self.context.target_url, trusted=True)

    def render(self):
        return '<a href="%s">%s</a>' % (self.context.target_url, self.context.target_url)
