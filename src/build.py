import re, base64

tpl = open('template.html', encoding='utf-8').read()
styles = re.findall(r'<style>(.*?)</style>', tpl, re.S)
assert len(styles) == 4

fonts = {
    "1f6591a3-2965-49e0-af8f-3123799fad1f": "assets/1f6591a3-2965-49e0-af8f-3123799fad1f.ttf",
    "dc8f8a35-0c8f-4e8e-9aa7-c1e78db91e6c": "assets/dc8f8a35-0c8f-4e8e-9aa7-c1e78db91e6c.ttf",
}
css0 = styles[0]
for drop in ('6b7808d5-c26c-4df9-be4a-ffa4abdba36b', '5254c329-ce9b-4472-a535-3142492b009b'):
    css0 = re.sub(r'@font-face \{[^}]*?' + drop + r'[^}]*?\}\n?', '', css0, flags=re.S)
for uuid, path in fonts.items():
    css0 = css0.replace(uuid, "data:font/ttf;base64," + base64.b64encode(open(path,'rb').read()).decode())
styles[0] = css0

read = lambda p: open(p, encoding='utf-8').read()
sprite   = read('assets/sprite.svg')
data_js  = read('assets/6339cfb0-0337-4877-8adf-bbc0471d9a85.js')
comp_js  = read('build/components.js')
scrn_js  = read('build/screens.js')
react    = read('lib/react.min.js')
reactdom = read('lib/react-dom.min.js')
override = read('override.css')

def iife(js):
    return '(function () {\n' + js + '\n})();'

p = ['''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="light">
<meta name="theme-color" content="#16191B">
<title>Lucky Slip — Odds field</title>
''']
for s in styles:
    p.append('<style>' + s + '</style>\n')
p.append('<style>' + override + '</style>\n')
p.append('</head>\n<body class="pg">\n')
p.append('<div id="sprite-host" aria-hidden="true" style="position:absolute;width:0;height:0;overflow:hidden">' + sprite + '</div>\n')
p.append('<div id="app"></div>\n')
p.append('<script>window.__spriteReady = Promise.resolve();</script>\n')
p.append('<script>\n' + react + '\n</script>\n')
p.append('<script>\n' + reactdom + '\n</script>\n')
for js in (data_js, comp_js, scrn_js):
    p.append('<script>\n' + iife(js) + '\n</script>\n')
p.append('</body></html>\n')

out = ''.join(p)
open('build/lucky-slip.html','w',encoding='utf-8').write(out)
print('bytes', len(out.encode()))
