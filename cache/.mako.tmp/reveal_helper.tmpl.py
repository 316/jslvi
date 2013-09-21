# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1379748744.771707
_enable_loop = True
_template_filename = u'themes/reveal/templates/reveal_helper.tmpl'
_template_uri = u'reveal_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_reveal_body', 'html_reveal_head']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 17
        __M_writer(u'\n\n')
        # SOURCE LINE 44
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_reveal_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        transition = context.get('transition', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 19
        __M_writer(u'\n    <script src="/assets/reveal/lib/js/head.min.js"></script>\n    <script src="/assets/reveal/js/reveal.min.js"></script>\n    <script>\n    // Full list of configuration options available here: https://github.com/hakimel/reveal.js#configuration\n    Reveal.initialize({\n    controls: false,\n    progress: false,\n    history: false,\n    keyboard: false,\n    rollingLinks: false,\n    theme: Reveal.getQueryHash().theme, // available themes are in /css/theme\n    transition: Reveal.getQueryHash().transition || \'')
        # SOURCE LINE 31
        __M_writer(unicode(transition))
        __M_writer(u"', // default/cube/page/concave/linear/none\n    // Optional libraries used to extend on reveal.js\n    dependencies: [\n    { src: '/assets/reveal/lib/js/classList.js', condition: function() { return !document.body.classList; } }\n    ]\n    });\n    </script>\n    <script>\n    Reveal.addEventListener( 'slidechanged', function( event ) {\n    window.scrollTo(0,0);\n    MathJax.Hub.Rerender(event.currentSlide);\n    });\n    </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_reveal_head(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        subtheme = context.get('subtheme', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    <meta name="apple-mobile-web-app-capable" content="yes" />\n    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />\n    <link rel="stylesheet" href="/assets/reveal/css/reveal.css">\n    <!-- If you use another reveal.css, DO NOT forget to delete overflow: hidden from global variables -->\n    <link rel="stylesheet" href="/assets/reveal/css/theme/')
        # SOURCE LINE 8
        __M_writer(unicode(subtheme))
        __M_writer(u'.css" id="theme">\n    <!-- If the query includes \'print-pdf\', use the PDF print sheet -->\n    <script>\n    document.write( \'<link rel="stylesheet" href="/assets/reveal/css/print/\' + ( window.location.search.match( /print-pdf/gi ) ? \'pdf\' : \'paper\' ) + \'.css" type="text/css" media="print">\' );\n    </script>\n    <!--[if lt IE 9]>\n    <script src="/assets/reveal/lib/js/html5shiv.js"></script>\n    <![endif]-->\n    <link rel="stylesheet" href="/assets/css/custom_reveal.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


