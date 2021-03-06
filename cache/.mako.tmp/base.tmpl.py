# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1379964413.944341
_enable_loop = True
_template_filename = u'themes/reveal/templates/base.tmpl'
_template_uri = u'base.tmpl'
_source_encoding = 'utf-8'
_exports = [u'extra_head', u'custom_reveal', u'sourcelink', u'content', u'belowtitle', u'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 4
    ns = runtime.TemplateNamespace(u'reveal', context._clean_inheritance_tokens(), templateuri=u'reveal_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'reveal')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace(u'bootstrap', context._clean_inheritance_tokens(), templateuri=u'bootstrap_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'bootstrap')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'reveal')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'bootstrap')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        extra_head_data = _import_ns.get('extra_head_data', context.get('extra_head_data', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        def custom_reveal():
            return render_custom_reveal(context._locals(__M_locals))
        reveal = _mako_get_namespace(context, 'reveal')
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        bootstrap = _mako_get_namespace(context, 'bootstrap')
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        hide_sourcelink = _import_ns.get('hide_sourcelink', context.get('hide_sourcelink', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(unicode(set_locale(lang)))
        __M_writer(u'\n<!DOCTYPE html>\n<html lang="')
        # SOURCE LINE 7
        __M_writer(unicode(lang))
        __M_writer(u'">\n<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    ')
        # SOURCE LINE 10
        __M_writer(unicode(bootstrap.html_head()))
        __M_writer(u'\n    ')
        # SOURCE LINE 11
        __M_writer(unicode(reveal.html_reveal_head()))
        __M_writer(u'\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 13
        __M_writer(u'\n    ')
        # SOURCE LINE 14
        __M_writer(unicode(extra_head_data))
        __M_writer(u'\n</head>\n<body>\n\n<!-- Menubar -->\n<div class="navbar navbar-fixed-top" id="navbar">\n    <div class="navbar-inner">\n        <div class="container">\n\n        <!-- .btn-navbar is used as the toggle for collapsed navbar content -->\n        <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n        </a>\n\n            <a class="brand" href="')
        # SOURCE LINE 30
        __M_writer(unicode(abs_link('/')))
        __M_writer(u'">\n            ')
        # SOURCE LINE 31
        __M_writer(unicode(blog_title))
        __M_writer(u'\n            </a>\n            <!-- Everything you want hidden at 940px or less, place within here -->\n            <div class="nav-collapse collapse">\n                <ul class="nav">\n                    ')
        # SOURCE LINE 36
        __M_writer(unicode(bootstrap.html_navigation_links()))
        __M_writer(u'\n                </ul>\n')
        # SOURCE LINE 38
        if search_form:
            # SOURCE LINE 39
            __M_writer(u'                    ')
            __M_writer(unicode(search_form))
            __M_writer(u'\n')
        # SOURCE LINE 41
        __M_writer(u'                <ul class="nav pull-right">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        # SOURCE LINE 46
        __M_writer(u'\n')
        # SOURCE LINE 47
        if not hide_sourcelink:
            # SOURCE LINE 48
            __M_writer(u'                    <li>')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
                context['self'].sourcelink(**pageargs)
            

            __M_writer(u'</li>\n')
        # SOURCE LINE 50
        __M_writer(u'                </ul>\n            </div>\n        </div>\n    </div>\n</div>\n<!-- End of Menubar -->\n\n<div class="reveal"><div class="slides">\n    <section>\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 59
        __M_writer(u'\n    </section>\n</div></div>\n\n')
        # SOURCE LINE 63
        __M_writer(unicode(reveal.html_reveal_body()))
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'custom_reveal'):
            context['self'].custom_reveal(**pageargs)
        

        # SOURCE LINE 65
        __M_writer(u'\n\n<div class="navbar navbar-fixed-bottom">\n    <div class="navbar-inner">\n        <div class="footerbox">\n            ')
        # SOURCE LINE 70
        __M_writer(unicode(content_footer))
        __M_writer(u'\n        </div>\n    </div>\n</div>\n\n')
        # SOURCE LINE 75
        __M_writer(unicode(bootstrap.late_load_js()))
        __M_writer(u'\n')
        # SOURCE LINE 76
        __M_writer(unicode(base.html_social()))
        __M_writer(u'\n    <script type="text/javascript">jQuery("a.image-reference").colorbox({rel:"gal",maxWidth:"100%",maxHeight:"100%",scalePhotos:true});\n    $(window).on(\'hashchange\', function(){\n        if (location.hash && $(location.hash)[0]) {\n            $(\'body\').animate({scrollTop: $(location.hash).offset().top - $(\'#navbar\').outerHeight(true)*1.2 }, 1);\n        }\n    });\n    $(document).ready(function(){$(window).trigger(\'hashchange\')});\n    </script>\n   ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        # SOURCE LINE 85
        __M_writer(u'\n   ')
        # SOURCE LINE 86
        __M_writer(unicode(body_end))
        __M_writer(u'\n</body>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'reveal')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'bootstrap')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer(u'\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_custom_reveal(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'reveal')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'bootstrap')._populate(_import_ns, [u'*'])
        def custom_reveal():
            return render_custom_reveal(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'reveal')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'bootstrap')._populate(_import_ns, [u'*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'reveal')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'bootstrap')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'reveal')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'bootstrap')._populate(_import_ns, [u'*'])
        def belowtitle():
            return render_belowtitle(context)
        base = _mako_get_namespace(context, 'base')
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 42
        __M_writer(u'\n')
        # SOURCE LINE 43
        if len(translations) > 1:
            # SOURCE LINE 44
            __M_writer(u'                    <li>')
            __M_writer(unicode(base.html_translations()))
            __M_writer(u'</li>\n')
        # SOURCE LINE 46
        __M_writer(u'                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'reveal')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'bootstrap')._populate(_import_ns, [u'*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


