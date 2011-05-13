from setuptools import setup, find_packages


setup(name='asm.cmsui',
      version='0.1.7',
      description="Assembly CMS - CMS UI package",
      author="Webcrew",
      author_email="web@assembly.org",
      url="",
      license="ZPL 2.1",
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=['ZODB3',
                        'asm.cms',
                        'gocept.selenium',
                        'grok',
                        'hurry.query',
                        'hurry.resource',
                        'hurry.tinymce',
                        'lxml',
                        'magic',
                        'megrok.pagelet',
                        'setuptools',
                        'simplejson',
                        'transaction',
                        'z3c.flashmessage',
                        'zope.app.component',
                        'zope.app.container',
                        'zope.app.folder',
                        'zope.app.form',
                        'zope.app.publication',
                        'zope.app.testing',
                        'zope.component',
                        'zope.copypastemove',
                        'zope.event',
                        'zope.interface',
                        'zope.intid',
                        'zope.lifecycleevent',
                        'zope.security',
                        'zope.traversing'])
