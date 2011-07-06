# Copyright (c) 2011 Assembly Organizing
# See also LICENSE.txt

import asm.cms.edition
import asm.cms.redirect
import asm.cmsui.interfaces
import grok
import zope.component
import zope.publisher.interfaces.browser
import zope.traversing.browser.interfaces

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

class RedirectAbsoluteUrl(grok.MultiAdapter):
    grok.adapts(
        asm.cms.interfaces.IRedirect,
        zope.publisher.interfaces.browser.IBrowserRequest)
    grok.implements(zope.traversing.browser.interfaces.IAbsoluteURL)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        # XXX this is quite a hack but gets us what we want.
        # Namely we don't want to show the absolute URL in cmsui so that
        # we can actually click links to modify this object.
        if asm.cmsui.interfaces.ICMSSkin.providedBy(self.request):
            edition = asm.cms.edition.Edition()
            edition.title = self.context.title
            edition.tags = self.context.tags
            edition.__parent__ = self.context.__parent__
            edition.__name__ = self.context.__name__
            adapter =  zope.component.getMultiAdapter(
                (edition, self.request),
                zope.traversing.browser.interfaces.IAbsoluteURL)
            return adapter()
        return self.context.target_url
