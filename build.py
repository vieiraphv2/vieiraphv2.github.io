#!/usr/bin/env python3
"""Render index.html, cv.md and llms.txt from resume.json. Stdlib only: python3 build.py"""
import json, html, datetime, pathlib, sys
LANG = sys.argv[1] if len(sys.argv) > 1 else 'en'

ROOT = pathlib.Path(__file__).parent
R = json.loads((ROOT / "resume.json").read_text())

def merge(base, over):
    if isinstance(base, dict) and isinstance(over, dict):
        for k, v in over.items(): base[k] = merge(base.get(k), v) if k in base else v
        return base
    if isinstance(base, list) and isinstance(over, list) and over and isinstance(over[0], dict):
        return [merge(b, o) for b, o in zip(base, over)] + base[len(over):]
    return over

if LANG == 'pt':
    R = merge(R, json.loads((ROOT / "resume.pt.json").read_text()))

UI = {
 'en': dict(html='en', country='Brazil', skip='Skip to content', about='About', now='Now', loc='Location',
   langs='Languages', exp='Experience', expand='Expand all', collapse='Collapse all', personal='Personal projects',
   skills='Skills', edu='Education &amp; credentials', projects='Projects', at='at', since='since', present='Present',
   open='Open', contact='Contact and formats', aiT='For AI tools and agents', aiB1='Same CV, machine-friendly:',
   aiB2='JSON Resume schema', aiB3='This page also carries schema.org <code>Person</code> data as JSON-LD.',
   updated='Updated', source='source', mdTitle='Plain Markdown version for AI tools',
   types={}, modes={}, places={}, mon=None, monfull=None, other='PT', otherHref='pt/', otherLang='pt-BR', oglocale='en_US'),
 'pt': dict(html='pt-BR', country='Brasil', skip='Pular para o conteúdo', about='Sobre', now='Agora', loc='Localização',
   langs='Idiomas', exp='Experiência', expand='Expandir tudo', collapse='Recolher tudo', personal='Projetos pessoais',
   skills='Habilidades', edu='Formação e credenciais', projects='Projetos', at='na', since='desde', present='Atual',
   open='Abrir', contact='Contato e formatos', aiT='Para ferramentas de IA e agentes', aiB1='O mesmo CV, legível por máquina:',
   aiB2='schema JSON Resume', aiB3='Esta página também carrega dados schema.org <code>Person</code> em JSON-LD.',
   updated='Atualizado em', source='código', mdTitle='Versão em Markdown para ferramentas de IA',
   types={'Full-time': 'Tempo integral', 'Contract': 'Contrato'},
   modes={'Remote': 'Remoto', 'On-site': 'Presencial', 'Hybrid': 'Híbrido'},
   places={'Boulder, Colorado, US': 'Boulder, Colorado, EUA', 'New York City, US': 'Nova York, EUA'},
   mon=['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'],
   monfull=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'],
   other='EN', otherHref='../', otherLang='en', oglocale='pt_BR'),
}
L = UI[LANG]
PREF = '' if LANG == 'en' else '../'
LANGJS = ("if(_l==='pt'||(!_l&&/^pt/i.test(navigator.language||'')))location.replace('pt/')" if LANG == 'en'
          else "if(_l==='en')location.replace('../')")
OTHERCODE = 'pt' if LANG == 'en' else 'en'
B, W, P, S, LG, H = R["basics"], R["work"], R["projects"], R["skills"], R["languages"], R["highlights"]
ED, AW, REFS = R.get("education", []), R.get("awards", []), R.get("references", [])
SITE = R["meta"]["canonical"]
CANON = SITE if LANG == 'en' else SITE + 'pt/'
UPDATED = R["meta"]["lastModified"]
e = html.escape

def month(iso):
    if not iso: return L['present']
    d = datetime.date.fromisoformat(iso + "-01")
    return f"{L['mon'][d.month-1]} {d.year}" if L['mon'] else d.strftime("%b %Y")

def span(w):
    return f"{month(w['startDate'])} – {month(w.get('endDate'))}"

def profile(net):
    return next(p for p in B["profiles"] if p["network"] == net)

# ---------- JSON-LD (schema.org ProfilePage > Person) ----------
current = W[0]
jsonld = {
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "dateModified": UPDATED,
  "inLanguage": "en" if LANG == "en" else "pt-BR",
  "mainEntity": {
    "@type": "Person",
    "name": B["name"],
    "url": SITE,
    "jobTitle": current["position"],
    "description": B["tagline"],
    "worksFor": {"@type": "Organization", "name": current["name"], "url": current.get("url")},
    "address": {"@type": "PostalAddress", "addressLocality": B["location"]["city"],
                "addressRegion": B["location"]["region"], "addressCountry": B["location"]["countryCode"]},
    "email": B.get("email"),
    "sameAs": [p["url"] for p in B["profiles"]],
    "alumniOf": [{"@type": "CollegeOrUniversity", "name": x["institution"]} for x in ED],
    "award": [x["title"] for x in AW],
    "knowsLanguage": [l["language"] for l in LG],
    "knowsAbout": [k for g in S for k in g["keywords"]],
    "hasOccupation": {"@type": "Occupation", "name": current["position"],
                      "skills": ", ".join(current["keywords"])},
  }
}
# Work history as Organization/Role list for parsers that read it
jsonld["mainEntity"]["hasOccupation"] = [
  {"@type": "Role", "roleName": w["position"], "startDate": w["startDate"], **({"endDate": w["endDate"]} if w.get("endDate") else {}),
   "worksFor": {"@type": "Organization", "name": w["name"]}} for w in W]

# ---------- HTML ----------
def chips(keys, inline=False):
    w, i = ("span", "span") if inline else ("ul", "li")
    return f'<{w} class="chips">' + "".join(f"<{i}>{e(k)}</{i}>" for k in keys) + f"</{w}>"

def project(p):
    hl = "".join(f"<li>{e(x)}</li>" for x in p.get("highlights", []))
    ext = f'<p><a class="ext" href="{e(p["url"])}" rel="noopener">{L['open']} {e(p["name"])} <span aria-hidden="true">↗</span></a></p>' if p.get("url") else ''
    return f'''
<details class="glass lift mini proj rise">
  <summary><span class="val">{e(p["name"])}</span><span class="tag">{e(" · ".join(p.get("roles", [])))}</span></summary>
  <div class="body">
    <p>{e(p["description"])}</p>
    {f'<ul class="hl">{hl}</ul>' if hl else ''}
    {chips(p.get("keywords", []))}
    {ext}
  </div>
</details>'''


def _ab(block):
    lines = block.split("\n")
    if any(l.startswith("- ") for l in lines):
        head = "".join(f"<p>{e(l)}</p>" for l in lines if not l.startswith("- "))
        items = "".join(f"<li>{e(l[2:])}</li>" for l in lines if l.startswith("- "))
        return f'{head}<ul class="hl">{items}</ul>'
    return f"<p>{e(block)}</p>"
about = "".join(_ab(p) for p in B["summary"].split("\n\n"))
skills = "".join(f'<div class="glass sgroup rise"><h3>{e(g["name"])}</h3>{chips(g["keywords"])}</div>' for g in S)
langs = ", ".join(f'{e(l["language"])} ({e(l["fluency"].split(",")[0].lower())})' for l in LG)
li, gh = profile("LinkedIn"), profile("GitHub")
desc = B["tagline"]

def workmode(w):
    *place, tail = w["location"].split(" \u00b7 ")
    if tail in ("Remote", "On-site", "Hybrid"): return " \u00b7 ".join(place), tail
    return w["location"], None

def role(w, i):
    end = w.get("endDate")
    place, mode = workmode(w)
    place = L['places'].get(place, place)
    etype = L['types'].get(w['type'], w['type']) + (f" &middot; {e(L['modes'].get(mode, mode))}" if mode else '')
    lgo = (ROOT / w["logo"]).read_text() if w.get("logo") else f'<span class="mono">{e(w["name"][0])}</span>'
    projs = [p for p in P if p.get("employer") == w["name"]] if i == next(k for k, x in enumerate(W) if x["name"] == w["name"]) else []
    pblock = f'<div class="nested"><p class="eyebrow">{L['projects']}</p><div class="minis">{"".join(project(p) for p in projs)}</div></div>' if projs else ''
    hl = "".join(f"<li>{e(x)}</li>" for x in w.get("highlights", []))
    name = f'<a href="{e(w["url"])}" rel="noopener">{e(w["name"])}</a>' if w.get("url") else e(w["name"])
    sub = f'<span class="rsub">{e(w["summary"])}</span>' if w.get("summary") else f'<span class="rsub rloc">{e(place)}</span>'
    return f'''
<details class="role glass rise{' current' if not end else ''}">
  <summary>
    <span class="lgo" aria-hidden="true">{lgo}</span>
    <span class="when"><time datetime="{e(w['startDate'])}">{e(month(w['startDate']))}</time> – <time{f' datetime="{e(end)}"' if end else ''}>{e(month(end))}</time><span class="etype">{etype}</span></span>
    <span class="who">
      <span class="ttl"><span class="pos">{e(w['position'])}</span> <span class="at">{L['at']}</span> <span class="org">{name}</span></span>
      {sub}
      {chips(w.get('keywords', []), inline=True) if w.get('keywords') else ''}
    </span>
    <span class="chev" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></span>
  </summary>
  <div class="rbody">
    {f'<p class="loc">{e(place)}</p>' if place else ''}
    {f'<ul class="hl">{hl}</ul>' if hl else ''}
    {pblock}
  </div>
</details>'''


INDEX = f'''<!doctype html>
<html lang="{L['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(B["name"])} · {e(current["position"])}</title>
<meta name="description" content="{e(desc)}">
<meta name="author" content="{e(B["name"])}">
<link rel="canonical" href="{CANON}">
<link rel="alternate" hreflang="en" href="{SITE}">
<link rel="alternate" hreflang="pt-BR" href="{SITE}pt/">
<link rel="alternate" hreflang="x-default" href="{SITE}">
<link rel="alternate" type="text/markdown" href="{SITE}cv.md" title="CV as Markdown">
<link rel="alternate" type="application/json" href="{SITE}resume.json" title="CV as JSON Resume">
<link rel="alternate" type="text/plain" href="{SITE}llms.txt" title="llms.txt">
<link rel="me" href="{e(li["url"])}"><link rel="me" href="{e(gh["url"])}">
<meta property="og:type" content="profile">
<meta property="og:title" content="{e(B["name"])} · {e(B["label"])}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{CANON}">
<meta property="og:locale" content="{L['oglocale']}">
<meta property="profile:first_name" content="{e(B["name"].split()[0])}"><meta property="profile:last_name" content="{e(" ".join(B["name"].split()[1:]))}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#F5F7FA">
<script>try{{var _l=localStorage.getItem('lang');{LANGJS}}}catch(e){{}}</script>
<script>try{{var t=localStorage.getItem('theme');if(t==='dark'){{document.documentElement.dataset.theme='dark';document.querySelector('meta[name=theme-color]').content='#090D14'}}}}catch(e){{}}</script>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23121B27'/%3E%3Cpath d='M9 23V9h6.5a4.5 4.5 0 0 1 0 9H12v5H9z' fill='%234C8DFF'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False, indent=1)}</script>
<style>
  /* Apple-flavoured glass. Light by default; dark keeps the GKE deck's stage. */
  :root{{
    color-scheme:light;
    --bg:#F5F5F7; --panel:#FFFFFF; --hair:rgba(0,0,0,.08);
    --ink:#1D1D1F; --ink2:#424245; --ink3:#6E6E73;
    --acc:#0A66FF; --acc-t:#0B5ED7; --acc2:#4F46E5; --acc2-t:#4338CA;
    --glass:rgba(255,255,255,.58); --glass-strong:rgba(255,255,255,.78); --glass-border:rgba(255,255,255,.85); --glass-border-h:rgba(255,255,255,1);
    --glass-inner:inset 0 1px 0 rgba(255,255,255,.95),inset 0 -1px 0 rgba(20,40,60,.04);
    --spec:rgba(255,255,255,.75); --rim-a:rgba(255,255,255,1); --rim-b:rgba(255,255,255,.35); --rim-c:rgba(255,255,255,.8);
    --shadow:0 24px 60px -28px rgba(30,40,60,.3),0 2px 6px rgba(30,40,60,.04);
    --shadow-h:0 32px 64px -28px rgba(30,40,60,.34),0 4px 10px rgba(30,40,60,.05);
    --nav:rgba(245,245,247,.72); --chip:rgba(255,255,255,.7); --chip-border:rgba(0,0,0,.08);
    --sel:#D6E4FF; --btn:#1D1D1F; --btn-ink:#FFFFFF;
    --ease:cubic-bezier(.22,1,.36,1);
    --disp:-apple-system,BlinkMacSystemFont,"SF Pro Display",Inter,"Helvetica Neue",Arial,sans-serif;
    --body:-apple-system,BlinkMacSystemFont,"SF Pro Text",Inter,"Helvetica Neue",Arial,sans-serif;
  }}
  :root[data-theme="dark"]{{
    color-scheme:dark;
    --bg:#090D14; --panel:#121B27; --hair:rgba(255,255,255,.09);
    --ink:#F2F5F8; --ink2:#AAB7C7; --ink3:#8392A6;
    --acc:#4C8DFF; --acc-t:#8EB8FF; --acc2:#7B7BFF; --acc2-t:#B4B8FF;
    --glass:linear-gradient(135deg,rgba(230,244,255,.14),rgba(170,195,223,.05) 43%,rgba(90,120,160,.09));
    --glass-strong:linear-gradient(135deg,#1C2735,#121A26);
    --glass-border:rgba(184,210,232,.15); --glass-border-h:rgba(191,218,237,.27);
    --glass-inner:inset 0 1px 0 rgba(244,250,255,.16),inset 0 -1px 0 rgba(153,180,213,.045);
    --spec:rgba(198,222,247,.10); --rim-a:rgba(214,232,246,.30); --rim-b:rgba(184,205,232,.07); --rim-c:rgba(184,205,232,.18);
    --shadow:0 18px 44px -18px rgba(0,0,0,.65),0 4px 12px rgba(0,0,0,.14);
    --shadow-h:0 28px 55px -20px rgba(0,0,0,.65),0 4px 12px rgba(0,0,0,.16);
    --nav:rgba(9,13,20,.62); --chip:rgba(18,27,39,.55); --chip-border:rgba(184,210,232,.12);
    --sel:#1E2F4F; --btn:#F2F5F8; --btn-ink:#090D14;
    --lgo-ink:#C6CEDA; --lgo-green:#4CEB96;
  }}
  :root[data-theme="dark"] .lg-ink{{fill:#C6CEDA}} :root[data-theme="dark"] .lg-green{{fill:#4CEB96}}
  .x-dummy{{
  }}
  *{{margin:0;box-sizing:border-box}}
  html{{scroll-behavior:smooth;scroll-padding-top:72px}}
  body{{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.47;letter-spacing:-.011em;
       -webkit-font-smoothing:antialiased;isolation:isolate;min-height:100vh;
       transition:background-color .5s ease,color .5s ease}}
  ::selection{{background:var(--sel);color:var(--ink)}}
  a{{color:var(--acc-t);text-decoration:none;transition:color .3s}}
  a:hover{{text-decoration:underline;text-underline-offset:3px}}
  a:focus-visible,button:focus-visible{{outline:2px solid var(--acc-t);outline-offset:3px;border-radius:6px}}
  .skip{{position:absolute;left:-999px;top:8px;background:var(--panel);padding:8px 14px;border-radius:8px;z-index:30}}
  .skip:focus{{left:8px}}

  /* The GKE deck's ambient stage, dark theme only: slow radial glows + vignette give the glass something to refract. */
  :root[data-theme="dark"] body::before,:root[data-theme="dark"] body::after{{content:"";position:fixed;inset:0;pointer-events:none;z-index:-1}}
  :root[data-theme="dark"] body::before{{inset:-12%;opacity:.85;
    background:radial-gradient(ellipse at 19% 18%,rgba(76,141,255,.30),transparent 46%),
               radial-gradient(ellipse at 85% 45%,rgba(125,125,255,.20),transparent 42%),
               radial-gradient(ellipse at 40% 100%,rgba(56,110,200,.26),transparent 56%);
    animation:ambient 26s ease-in-out infinite alternate}}
  :root[data-theme="dark"] body::after{{background:radial-gradient(ellipse at 50% 48%,transparent 38%,rgba(3,6,11,.48) 100%)}}
  @keyframes ambient{{to{{transform:translate3d(2%,-2%,0) scale(1.04);opacity:.88}}}}

  /* Thick glass, the recurring material: blurred colour behind, a specular corner, a lit edge that fades round the rim. */
  .glass{{position:relative;isolation:isolate;overflow:hidden;border:1px solid transparent;
          background:radial-gradient(120% 90% at 8% 0%,var(--spec),transparent 58%),var(--glass);
          box-shadow:var(--shadow),var(--glass-inner);
          -webkit-backdrop-filter:blur(36px) saturate(180%);backdrop-filter:blur(36px) saturate(180%);
          transition:box-shadow .6s ease,translate .7s var(--ease),background-color .5s}}
  .glass::before{{content:"";position:absolute;inset:0;border-radius:inherit;padding:1px;pointer-events:none;z-index:1;
          background:linear-gradient(135deg,var(--rim-a),var(--rim-b) 38%,var(--rim-b) 62%,var(--rim-c));
          -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);mask-composite:exclude}}
  @media (hover:hover) and (pointer:fine){{
    .glass.lift:hover{{translate:0 -4px;box-shadow:var(--shadow-h),var(--glass-inner)}}
  }}

  /* Sticky frosted bar, apple.com style. */
  .bar{{position:sticky;top:0;z-index:20;background:var(--nav);border-bottom:1px solid var(--hair);
        -webkit-backdrop-filter:saturate(180%) blur(20px);backdrop-filter:saturate(180%) blur(20px);transition:background-color .5s}}
  .bar .wrap{{display:flex;align-items:center;justify-content:space-between;height:52px;gap:16px}}
  .bar .brand{{font-family:var(--disp);font-weight:600;font-size:15px;letter-spacing:-.01em;color:var(--ink)}}
  .bar .brand:hover{{text-decoration:none}}
  .bar nav{{display:flex;gap:26px;font-size:13.5px;font-weight:500}}
  .bar nav a{{color:var(--ink2)}} .bar nav a:hover{{color:var(--ink);text-decoration:none}}
  .navr{{display:flex;align-items:center;gap:10px}}
  .langsw{{font:600 12px var(--disp);letter-spacing:.05em;color:var(--ink2);border:1px solid var(--hair);
          padding:7px 12px;border-radius:999px}}
  .langsw:hover{{color:var(--ink);text-decoration:none;border-color:var(--ink3)}}
  #theme{{width:34px;height:34px;border-radius:999px;cursor:pointer;display:grid;place-items:center;color:var(--ink);
          border:1px solid var(--hair);background:var(--glass);position:relative;transition:background-color .4s,border-color .4s,transform .4s var(--ease)}}
  #theme:hover{{transform:rotate(15deg);border-color:var(--ink3)}}
  #theme svg{{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}}
  #theme .moon{{display:none}} [data-theme="dark"] #theme .moon{{display:block}} [data-theme="dark"] #theme .sun{{display:none}}

  .wrap{{width:min(1024px,100% - 2*clamp(16px,5vw,64px));margin:0 auto}}
  header.hero{{padding:clamp(72px,13vh,140px) 0 clamp(36px,6vh,64px);text-align:center}}
  .eyebrow{{font-family:var(--disp);font-weight:600;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink3)}}
  h1,h2,h3{{font-family:var(--disp);text-wrap:balance;letter-spacing:-.03em}}
  h1{{font-size:clamp(42px,6.6vw,88px);font-weight:700;line-height:1.02;margin:22px auto 24px;max-width:13em}}
  h2{{font-size:clamp(30px,4vw,48px);font-weight:700;line-height:1.06;margin:0 0 12px}}
  .sub{{font-size:clamp(18px,1.6vw,23px);line-height:1.4;color:var(--ink2);max-width:34em;margin:0 auto;text-wrap:pretty}}
  .links{{display:flex;gap:12px 14px;flex-wrap:wrap;justify-content:center;align-items:center;margin-top:34px;font-family:var(--disp);font-weight:500;font-size:15px}}
  .links a{{display:inline-flex;align-items:center;gap:8px;padding:11px 20px;border-radius:999px;color:var(--ink)}}
  .links a:hover{{text-decoration:none}}
  .links a.primary{{background:var(--btn);color:var(--btn-ink);border:1px solid transparent;transition:transform .4s var(--ease),background-color .5s}}
  .links a.primary:hover{{transform:translateY(-2px)}}
  .links a svg{{width:16px;height:16px;fill:currentColor}}
  .links .ai{{color:var(--acc-t);padding:8px 6px;font-size:14px}}
  .links .ai::after{{content:"›";margin-left:5px;font-size:17px;line-height:0}}

  section{{padding:clamp(44px,7vh,88px) 0}}
  section > .wrap > h2,.xhead h2{{margin-bottom:26px}} .about-h,.edu-h{{font-size:clamp(24px,2.6vw,34px)}}
  .lede{{color:var(--ink2);font-size:clamp(17px,1.35vw,20px);max-width:38em;margin-bottom:36px;text-wrap:pretty}}

  .tile{{border-radius:28px;position:relative;isolation:isolate;overflow:hidden}}
  /* Chip -> card: closed, a pill exposing the essential; open, the full card. */
  .minis{{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-start}}
  .mini{{border-radius:999px}}
  .mini[open]{{flex-basis:100%;border-radius:24px}}
  .mini summary{{list-style:none;cursor:pointer;display:flex;align-items:baseline;gap:12px;padding:14px 24px;white-space:nowrap}}
  .mini summary::-webkit-details-marker{{display:none}}
  .mini summary:focus-visible{{outline:2px solid var(--acc-t);outline-offset:-4px;border-radius:inherit}}
  .mini summary::after{{content:"+";font:300 22px/1 var(--disp);color:var(--acc-t);align-self:center;margin-left:auto;padding-left:6px;transition:transform .4s var(--ease)}}
  .mini[open] summary::after{{transform:rotate(45deg)}}
  .mini .val{{font-family:var(--disp);font-weight:700;letter-spacing:-.03em;font-size:21px;color:var(--ink)}}
  .mini .u{{font-size:.62em;font-weight:600;color:var(--ink3);letter-spacing:0}}
  .mini .tag{{font-size:14px;color:var(--ink2)}}
  .proj .val{{font-size:18px}}
  .mini .body{{padding:2px 24px 22px;display:grid;gap:12px;white-space:normal}}
  .mini .body > p{{color:var(--ink2);font-size:15px;line-height:1.55;max-width:64em;text-wrap:pretty}}
  .mini .body .hl{{font-size:14.5px}}
  .ext{{font-family:var(--disp);font-weight:500;font-size:14px}}
  .nested{{display:grid;gap:10px;padding-top:14px;border-top:1px solid var(--hair)}}
  .nested .eyebrow{{font-size:11px}}
  @media(max-width:640px){{.mini{{flex-basis:100%}} .mini summary{{white-space:normal;flex-wrap:wrap;gap:4px 12px}} .mini summary::after{{margin-left:auto}}}}

  .about{{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(24px,5vw,72px);align-items:start}}
  .about .text p{{margin:0 0 1em;max-width:36em;text-wrap:pretty;color:var(--ink2)}}
  .about .text .hl{{margin:0 0 1.2em;max-width:36em}}
  .about .text p:first-child{{font-family:var(--disp);font-weight:600;font-size:clamp(21px,2vw,27px);line-height:1.3;letter-spacing:-.02em;color:var(--ink)}}
  .facts{{padding:26px 28px;font-size:15px;display:grid;gap:16px}}
  .facts dt{{font-family:var(--disp);font-weight:600;font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink3)}}
  .facts dd{{color:var(--ink);margin-top:3px;line-height:1.45}}
  .facts dd + dd{{margin-top:6px}}

  .cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,380px),1fr));gap:16px}}
  .cards > :last-child:nth-child(odd){{grid-column:1/-1}}
  .cards > :last-child:nth-child(odd) .hl{{columns:2;column-gap:28px}}
  @media(max-width:760px){{.cards > :last-child:nth-child(odd) .hl{{columns:1}}}}
  .card{{padding:30px;display:flex;flex-direction:column;gap:12px}}
  .card h3{{font-size:23px;font-weight:700;line-height:1.15;letter-spacing:-.025em}}
  .card h3 a{{color:var(--ink)}} .card h3 a:hover{{color:var(--acc-t);text-decoration:none}}
  .card p{{color:var(--ink2);font-size:15px;line-height:1.5}}
  .card .eyebrow{{font-size:11.5px}}
  .card .chips{{margin-top:auto;padding-top:8px}}
  .edu > :last-child:nth-child(odd){{grid-column:auto}} .edu .card{{gap:8px}}

  .chips{{list-style:none;display:flex;flex-wrap:wrap;gap:8px;padding:0}}
  .chips > *{{font-family:var(--disp);font-weight:500;font-size:12.5px;color:var(--ink2);padding:6px 12px;border-radius:999px;
            border:1px solid var(--chip-border);background:var(--chip);transition:background-color .5s,border-color .5s}}
  .hl{{padding-left:1.15em;display:grid;gap:9px;color:var(--ink2);font-size:15.5px;line-height:1.5}}
  .hl li::marker{{color:var(--acc)}}
  .card .hl{{font-size:14.5px;gap:6px}}

  .xhead{{display:flex;align-items:baseline;justify-content:space-between;gap:20px;flex-wrap:wrap}}
  #xall{{cursor:pointer;font:500 13.5px/1 var(--disp);color:var(--ink2);padding:11px 16px;border-radius:999px;flex-shrink:0}}
  #xall:hover{{color:var(--ink)}}
  /* Timeline list: a hairline rail on the left, one collapsible glass entry per role. */
  .roles{{position:relative;display:grid;gap:12px;padding-left:34px}}
  .roles::before{{content:"";position:absolute;left:5px;top:18px;bottom:18px;width:1px;
        background:linear-gradient(transparent,var(--hair) 6%,var(--hair) 94%,transparent)}}
  .role{{border-radius:22px;overflow:visible}}
  .role::after{{content:"";position:absolute;left:-32px;top:30px;width:11px;height:11px;border-radius:50%;
        background:var(--bg);border:2px solid var(--ink3);box-sizing:border-box;transition:border-color .4s,box-shadow .4s}}
  .role.current::after{{background:var(--acc);border-color:var(--acc);box-shadow:0 0 0 4px color-mix(in srgb,var(--acc) 20%,transparent),0 0 18px color-mix(in srgb,var(--acc) 45%,transparent)}}
  .role[open]::after{{border-color:var(--ink)}}
  .role.current[open]::after{{border-color:var(--acc)}}
  .role > summary{{list-style:none;cursor:pointer;display:grid;grid-template-columns:52px 150px minmax(0,1fr) 28px;gap:clamp(14px,2.6vw,30px);align-items:start;padding:22px 24px}}
  .lgo{{width:52px;height:52px;display:grid;place-items:center;color:var(--ink)}}
  .lgo svg{{max-width:100%;max-height:100%;width:auto;height:auto}}
  .mono{{font:600 24px var(--disp);color:var(--ink3);opacity:.55}}
  .role > summary .when{{padding-top:4px}} .role > summary .chev{{margin-top:2px}}
  .role > summary::-webkit-details-marker{{display:none}}
  .role > summary:focus-visible{{outline:2px solid var(--acc-t);outline-offset:-4px;border-radius:22px}}
  .when{{font-family:var(--disp);font-weight:600;font-size:13.5px;color:var(--ink2);font-variant-numeric:tabular-nums;white-space:nowrap}}
  .role.current .when{{color:var(--acc-t)}}
  .etype{{display:block;margin-top:3px;font-weight:500;font-size:12px;color:var(--ink3);letter-spacing:.01em}}
  .who{{display:grid;gap:3px;min-width:0}}
  .ttl{{font-family:var(--disp);font-weight:700;font-size:clamp(17px,1.5vw,20px);letter-spacing:-.02em;line-height:1.25;text-wrap:pretty}}
  .ttl .at{{color:var(--ink3);font-weight:500}}
  .ttl .org a{{color:var(--ink)}} .ttl .org a:hover{{color:var(--acc-t);text-decoration:none}}
  .rsub{{color:var(--ink2);font-size:14.5px;line-height:1.45;text-wrap:pretty}}
  .who .chips{{margin-top:8px;display:flex}}
  .chev{{width:28px;height:28px;border-radius:50%;display:grid;place-items:center;color:var(--ink3);border:1px solid var(--hair);transition:transform .45s var(--ease),color .3s,border-color .3s}}
  .chev svg{{width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}}
  .role[open] .chev{{transform:rotate(180deg);color:var(--ink);border-color:var(--ink3)}}
  .role > summary:hover .chev{{color:var(--ink);border-color:var(--ink3)}}
  .rbody{{padding:0 24px 24px;display:grid;gap:14px}}
  .rbody .loc{{color:var(--ink3);font-size:13.5px;margin-top:-4px;padding-top:14px;border-top:1px solid var(--hair)}}
  .rbody .loc a{{color:var(--ink2)}}
  .role .chips > *{{font-size:12px}}
  /* Open/close animation where the browser supports it; instant elsewhere. */
  @supports (interpolate-size: allow-keywords){{
    :root{{interpolate-size:allow-keywords}}
    .role::details-content,.mini::details-content{{block-size:0;overflow:clip;transition:block-size .5s var(--ease),content-visibility .5s allow-discrete}}
    .role[open]::details-content,.mini[open]::details-content{{block-size:auto}}
  }}

  .skills{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));gap:16px}}
  .sgroup{{padding:26px 28px;border-radius:24px}}
  .sgroup h3{{font-size:12px;letter-spacing:.06em;text-transform:uppercase;font-weight:600;color:var(--ink3);margin-bottom:14px}}

  footer{{padding:56px 0 64px;color:var(--ink3);font-size:14px}}
  footer .wrap{{display:grid;gap:22px}}
  footer .ai-box{{padding:22px 26px;border-radius:20px;display:grid;gap:8px;font-size:14.5px;color:var(--ink2)}}
  footer .ai-box strong{{font-family:var(--disp);color:var(--ink);font-weight:600}}
  footer .ai-box code{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13px;color:var(--acc-t)}}
  footer .row{{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;padding-top:18px;border-top:1px solid var(--hair)}}

  /* JS-only reveal; without JS everything is simply visible (crawlers, readers). */
  .js .rise{{opacity:0;transform:translate3d(0,16px,0);transition:opacity .7s ease,transform .9s var(--ease)}}
  .js .rise.in{{opacity:1;transform:none}}

  @media(max-width:760px){{
    .bar nav{{display:none}}
    .about{{grid-template-columns:1fr}}
    .roles{{padding-left:26px}} .role::after{{left:-24px;top:24px}}
    .role > summary{{grid-template-columns:44px minmax(0,1fr) 28px;gap:8px 14px;padding:18px 18px;align-items:center}}
    .when{{grid-column:2;font-size:12.5px}} .lgo{{grid-row:1/3;width:44px;height:44px}} .who{{grid-row:2;grid-column:2/4}} .chev{{grid-row:1;grid-column:3}}
    .rbody{{padding:0 18px 20px}}
    .stat,.card,.sgroup{{padding:24px 22px}}
    .links a.primary,.links a.glass{{padding:11px 18px}}
  }}
  @media(prefers-reduced-motion:reduce){{
    *,*::before,*::after{{animation:none!important;transition:none!important}}
    .js .rise{{opacity:1;transform:none}}
  }}
  @supports not ((backdrop-filter:blur(1px)) or (-webkit-backdrop-filter:blur(1px))){{
    .glass{{background:var(--glass-strong)}} .bar{{background:var(--bg)}}
  }}
  @media print{{
    :root,:root[data-theme="dark"]{{--bg:#fff;--ink:#111;--ink2:#333;--ink3:#555;--hair:#ccc;--acc-t:#0b3d91;--acc2-t:#3730a3;--chip:#fff;--chip-border:#ccc;--glass:#fff;--glass-border:#ddd;--shadow:none;--shadow-h:none;--glass-inner:none}}
    .bar,.links .ai,footer .ai-box{{display:none}}
    body{{font-size:11.5pt}} a{{color:#111}} a[href^="http"]::after{{content:" (" attr(href) ")";font-size:9pt;color:#555}}
    .links a.primary{{background:none;color:#111;border:1px solid #ccc}}
    header.hero,section{{padding:18pt 0}} .role{{break-inside:avoid}} h1{{font-size:28pt}} h2{{font-size:18pt}}
    .js .rise{{opacity:1;transform:none}} #xall,.chev,.roles::before,.role::after,.mini summary::after{{display:none}} .roles{{padding-left:0}}
    details::details-content{{content-visibility:visible!important;block-size:auto!important}}
    .mini{{flex-basis:100%;border-radius:12pt}}
  }}
</style>
</head>
<body>
<a class="skip" href="#about">{L['skip']}</a>

<div class="bar">
  <div class="wrap">
    <a class="brand" href="#top">{e(B["name"])}</a>
    <nav aria-label="Sections">
      <a href="#about">{L['about']}</a><a href="#experience">{L['exp']}</a><a href="#skills">{L['skills'].split(' ')[0] if LANG == 'pt' else L['skills']}</a>
    </nav>
    <div class="navr">
    <a class="langsw" href="{L['otherHref']}" hreflang="{L['otherLang']}" lang="{L['otherLang']}">{L['other']}</a>
    <button id="theme" type="button" aria-label="Switch to dark theme" aria-pressed="false" title="Toggle dark / light">
      <svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
      <svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
    </button>
  </div>
  </div>
</div>

<header class="hero" id="top">
  <div class="wrap">
    <h1>{e(B["name"])}</h1>
    <p class="sub">{e(B["label"])}</p>
    <nav class="links" aria-label="{L['contact']}">
      <a class="primary" href="{e(li["url"])}" rel="me noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.4 20.5h-3.6v-5.6c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9v5.7H9.3V9h3.4v1.6c.5-.9 1.7-1.8 3.4-1.8 3.6 0 4.3 2.4 4.3 5.5v6.2zM5.3 7.4a2.1 2.1 0 1 1 0-4.2 2.1 2.1 0 0 1 0 4.2zM7.1 20.5H3.5V9h3.6v11.5z"/></svg>LinkedIn</a>
      <a class="glass lift" href="{e(gh["url"])}" rel="me noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 .5a12 12 0 0 0-3.8 23.4c.6.1.8-.3.8-.6v-2c-3.3.7-4-1.6-4-1.6-.6-1.4-1.4-1.8-1.4-1.8-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1.1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.5.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.7 1.7.3 2.9.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0 0 12 .5z"/></svg>GitHub</a>
      <a class="glass lift" href="mailto:{e(B["email"])}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2 5.5A2.5 2.5 0 0 1 4.5 3h15A2.5 2.5 0 0 1 22 5.5v13a2.5 2.5 0 0 1-2.5 2.5h-15A2.5 2.5 0 0 1 2 18.5v-13zm2.3-.5 7.7 6.2L19.7 5H4.3zM20 7.1l-8 6.4-8-6.4V18.5c0 .3.2.5.5.5h15c.3 0 .5-.2.5-.5V7.1z"/></svg>Email</a>
      <a class="ai" href="{PREF}cv.md" title="{L['mdTitle']}">cv.md</a>
      <a class="ai" href="{PREF}resume.json" title="JSON Resume">resume.json</a>
    </nav>
  </div>
</header>

<section id="about">
  <div class="wrap">
    <h2 class="about-h">{L['about']}</h2>
    <div class="about">
      <div class="text">{about}</div>
      <dl class="glass lift tile facts rise">
        <div><dt>{L['now']}</dt><dd><ul class="hl">{"".join(f'<li>{e(w["position"])} {L['at']} {e(w["name"])}, {L['since']} {e(month(w["startDate"]))}</li>' for w in W if not w.get("endDate"))}</ul></dd></div>
        <div><dt>{L['loc']}</dt><dd>{e(B["location"]["city"])}, {e(B["location"]["region"])}, {L['country']} &middot; {e(B["location"]["remote"])}</dd></div>
        <div><dt>{L['langs']}</dt><dd>{langs}</dd></div>
      </dl>
    </div>
  </div>
</section>


<section id="experience">
  <div class="wrap">
    <div class="xhead"><h2>{L['exp']}</h2><button id="xall" type="button" class="glass">{L['expand']}</button></div>
    <div class="roles">{"".join(role(w, i) for i, w in enumerate(W))}
    </div>
  </div>
</section>

<section id="work">
  <div class="wrap">
    <h2>{L['personal']}</h2>
    <div class="minis">{"".join(project(p) for p in P if not p.get("employer"))}
    </div>
  </div>
</section>

<section id="skills">
  <div class="wrap">
    <h2>{L['skills']}</h2>
    <div class="skills">{skills}
    </div>
  </div>
</section>

<section id="education">
  <div class="wrap">
    <h2 class="edu-h">{L['edu']}</h2>
    <div class="cards edu">{"".join(f'<article class="glass lift tile card rise"><p class="eyebrow">{e(x["startDate"])} – {e(x["endDate"])}</p><h3>{e(x["studyType"])} {e(x["area"])}</h3><p>{e(x["institution"])}, {e(x["location"])}</p></article>' for x in ED)}{"".join(f'<article class="glass lift tile card rise"><p class="eyebrow">{e(month(x["date"]))} &middot; {e(x["awarder"])}</p><h3>{e(x["title"])}</h3><p>{e(x["summary"])}</p></article>' for x in AW)}
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="glass ai-box rise">
      <strong>{L['aiT']}</strong>
      <span>{L['aiB1']} <a href="{PREF}cv.md"><code>cv.md</code></a> (Markdown), <a href="{PREF}resume.json"><code>resume.json</code></a> ({L['aiB2']}), <a href="{PREF}llms.txt"><code>llms.txt</code></a>. {L['aiB3']}</span>
    </div>
    <div class="row">
      <span>&copy; {datetime.date.today().year} {e(B["name"])} &middot; <a href="mailto:{e(B["email"])}">{e(B["email"])}</a> &middot; <a href="{e(li["url"])}" rel="me">LinkedIn</a> &middot; <a href="{e(gh["url"])}" rel="me">GitHub</a></span>
      <span>{L['updated']} <time datetime="{UPDATED}">{e((lambda d: f"{L['monfull'][d.month-1]} {d.year}" if L['monfull'] else d.strftime("%B %Y"))(datetime.date.fromisoformat(UPDATED)))}</time> &middot; <a href="https://github.com/vieiraphv2/vieiraphv2.github.io">{L['source']}</a></span>
    </div>
  </div>
</footer>

<script>
  document.documentElement.classList.add('js');
  const io = new IntersectionObserver(es => es.forEach(x => {{ if (x.isIntersecting) {{ x.target.classList.add('in'); io.unobserve(x.target); }} }}), {{rootMargin:'0px 0px -8% 0px'}});
  document.querySelectorAll('.rise').forEach((el, i) => {{ el.style.transitionDelay = (i % 4) * 60 + 'ms'; io.observe(el); }});
  const root = document.documentElement, btn = document.getElementById('theme'), meta = document.querySelector('meta[name=theme-color]');
  const paint = () => {{ const d = root.dataset.theme === 'dark'; btn.setAttribute('aria-pressed', d); btn.setAttribute('aria-label', d ? 'Switch to light theme' : 'Switch to dark theme'); meta.content = d ? '#090D14' : '#F5F7FA'; }};
  btn.addEventListener('click', () => {{ const d = root.dataset.theme === 'dark'; if (d) delete root.dataset.theme; else root.dataset.theme = 'dark'; try {{ localStorage.setItem('theme', d ? 'light' : 'dark'); }} catch (e) {{}} paint(); }});
  paint();
  const roles = [...document.querySelectorAll('details.role')], xall = document.getElementById('xall');
  const label = () => xall.textContent = roles.every(d => d.open) ? '{L['collapse']}' : '{L['expand']}';
  xall.addEventListener('click', () => {{ const open = !roles.every(d => d.open); roles.forEach(d => d.open = open); label(); }});
  roles.forEach(d => d.addEventListener('toggle', label));
  addEventListener('beforeprint', () => document.querySelectorAll('details').forEach(d => d.open = true));
  document.querySelector('.langsw').addEventListener('click', () => {{ try {{ localStorage.setItem('lang', '{OTHERCODE}'); }} catch (e) {{}} }});
</script>
</body>
</html>
'''

# ---------- Markdown ----------
def md_role(w):
    out = [f"### {w['position']} · {w['name']}", f"*{span(w)} · {w['type']} · {w['location']}*", ""]
    if w.get("summary"): out += [w["summary"], ""]
    out += [f"- {h}" for h in w.get("highlights", [])]
    if w.get("keywords"): out += ["", f"Keywords: {', '.join(w['keywords'])}"]
    return "\n".join(out) + "\n"

CV_MD = f"""# {B['name']}

**{B['label']}**
{B['location']['city']}, {B['location']['region']}, Brazil · {B['location']['remote']} · {B['pronouns']}
Email: {B['email']} · LinkedIn: {li['url']} · GitHub: {gh['url']} · Web: {SITE}

> {B['tagline']}

## Highlights

{chr(10).join(f"- **{(h['value'] + ' ' + h['unit']).strip()}**: {h['label']}" for h in H)}

## About

{B['summary']}

## Selected work

{chr(10).join(f"### {p['name']}{' — ' + p['url'] if p.get('url') else ''}{chr(10)}{p['description']}{chr(10)}{chr(10).join('- ' + x for x in p.get('highlights', []))}{chr(10)}" for p in P)}
## Experience

{chr(10).join(md_role(w) for w in W)}
## What colleagues say (LinkedIn recommendations, verbatim)

{chr(10).join(f'> "{r["quote"]}"{chr(10)}> — {r["name"]}, {r["role"]} ({r["relation"]}, {r["date"]}){chr(10)}' for r in REFS)}
## Skills

{chr(10).join(f"- **{g['name']}:** {', '.join(g['keywords'])}" for g in S)}

## Education and credentials

{chr(10).join(f"- {x['studyType']} {x['area']}, {x['institution']}, {x['location']} ({x['startDate']} – {x['endDate']})" for x in ED)}
{chr(10).join(f"- {x['title']} ({month(x['date'])}, {x['awarder']}): {x['summary']}" for x in AW)}

## Languages

{chr(10).join(f"- {l['language']}: {l['fluency']}" for l in LG)}

---
Canonical: {SITE} · JSON Resume: {SITE}resume.json · Updated {UPDATED}
"""

LLMS = f"""# {B['name']}

> {B['label']}. {B['tagline']} Based in {B['location']['city']}, Brazil; remote on US hours. Portuguese and English.

This site is {B['name']}'s CV. Prefer the Markdown or JSON files below over scraping the HTML.

Current roles: {' · '.join(f"{w['position']} at {w['name']} (since {month(w['startDate'])})" for w in W if not w.get('endDate'))}.

## CV

- [Full CV (Markdown)]({SITE}cv.md): every role, achievement bullet and metric, plain text.
- [JSON Resume]({SITE}resume.json): the same data in the jsonresume.org schema; the source of truth for this site.
- [HTML page]({SITE}): human-facing version with schema.org Person JSON-LD.

## Featured

- [GKE Cost Reduction presentation](https://vieiraphv2.github.io/gke-cost-reduction/): the Kubernetes cost program, July to September 2026.

## Contact

- Email: {B['email']}
- [LinkedIn]({li['url']})
- [GitHub]({gh['url']})

## Optional

- Updated {UPDATED}. Numbers are from billing exports, invoices and ticket counts as of that date.
"""

if LANG == 'en':
    (ROOT / "index.html").write_text(INDEX)
    (ROOT / "cv.md").write_text(CV_MD)
    (ROOT / "llms.txt").write_text(LLMS)
    print("built index.html cv.md llms.txt")
else:
    (ROOT / "pt").mkdir(exist_ok=True)
    (ROOT / "pt" / "index.html").write_text(INDEX)
    print("built pt/index.html")
