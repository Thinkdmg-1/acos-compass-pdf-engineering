from pathlib import Path
import hashlib,json
base=Path(__file__).parent
r=json.loads((base/'results.json').read_text())
checks={}
checks['tool_versions']=r['tool_versions']=={'fontTools':'4.60.2','uharfbuzz':'0.51.7'}
checks['font_hashes']=all(len(v['sha256'])==64 for v in r['fonts'].values())
checks['font_table_inspection']=all(any(f['cmap']['has_GSUB'] for f in v['faces']) and any(f['cmap']['has_GPOS'] for f in v['faces']) for v in r['fonts'].values() if v['path'].endswith(('.ttc','.ttf')) and 'unicode' not in v['path'].lower())
checks['combining_composition']=len(r['samples']['combining_latin']['nfc_codepoints'])==1 and len(r['samples']['combining_latin']['harfbuzz']['glyphs'])==1
h=r['samples']['hebrew']['harfbuzz']; checks['hebrew_rtl_clusters']=h['direction']=='rtl' and h['script']=='Hebr' and [x['cluster'] for x in h['glyphs']]==sorted([x['cluster'] for x in h['glyphs']],reverse=True)
m=r['samples']['myanmar']['harfbuzz']; checks['myanmar_detected']=m['script']=='Mymr' and len(m['glyphs'])==6
orv=r['samples']['oriya']['harfbuzz']; checks['oriya_detected']=orv['script']=='Orya' and len(orv['glyphs'])==4 and len(orv['glyphs'])<len(r['samples']['oriya']['codepoints'])
e=r['samples']['emoji_zwj']['harfbuzz']; checks['emoji_boundary']=any(x['gid']==0 for x in e['glyphs'])
checks['result_sha256']=hashlib.sha256((base/'results.json').read_bytes()).hexdigest()=='fd814b205eac4752fb9203dd909877399bc5891f91c8c2d9edc65d20614ccce8'
out={'checks':checks,'all_pass':all(checks.values())}
(base/'independent-check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
if not out['all_pass']: raise SystemExit(1)
