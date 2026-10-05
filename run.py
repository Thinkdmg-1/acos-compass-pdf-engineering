import hashlib,json,subprocess,sys,unicodedata
from pathlib import Path
from fontTools.ttLib import TTCollection,TTFont
import uharfbuzz as hb
fonts={
 'myanmar':'/System/Library/Fonts/NotoSerifMyanmar.ttc',
 'oriya':'/System/Library/Fonts/NotoSansOriya.ttc',
 'korean':'/System/Library/Fonts/AppleSDGothicNeo.ttc',
 'unicode':'/Library/Fonts/Arial Unicode.ttf',
}
samples={
 'combining_latin':('unicode','e\u0301'),
 'hebrew':('unicode','שלום'),
 'myanmar':('myanmar','မြန်မာ'),
 'oriya':('oriya','ଓଡ଼ିଆ'),
 'emoji_zwj':('unicode','👩🏽‍💻'),
}
def fc(path):
 return subprocess.check_output(['fc-query','-f','%{family}\n%{style}\n%{lang}\n',path],text=True).splitlines()[:3]
def fhash(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load_face(path,index=0):
 data=Path(path).read_bytes()
 return TTCollection(path).fonts[index] if data[:4]==b'ttcf' else TTFont(path)
def cmap_info(path,index):
 f=load_face(path,index)
 cmap={};
 for t in f['cmap'].tables: cmap.update(t.cmap)
 return {'glyph_names':len(f.getGlyphOrder()),'cmap_codepoints':len(cmap),'tables':sorted(f.keys()),'has_GSUB':'GSUB' in f,'has_GPOS':'GPOS' in f,'family':f['name'].getDebugName(1),'subfamily':f['name'].getDebugName(2)}
def shape(path,index,text):
 data=Path(path).read_bytes(); face=hb.Face(data,index); font=hb.Font(face); font.scale=(face.upem,face.upem)
 b=hb.Buffer(); b.add_str(text); b.guess_segment_properties(); hb.shape(font,b,{})
 return {'direction':b.direction,'script':b.script,'language':b.language,'glyphs':[{'gid':i.codepoint,'cluster':i.cluster,'flags':int(i.flags)} for i in b.glyph_infos],'positions':[{'x_advance':p.x_advance,'y_advance':p.y_advance,'x_offset':p.x_offset,'y_offset':p.y_offset} for p in b.glyph_positions]}
out={'tool_versions':{'fontTools':__import__('fontTools').__version__,'uharfbuzz':hb.__version__},'fonts':{},'samples':{}}
for key,path in fonts.items():
 out['fonts'][key]={'path':path,'sha256':fhash(path),'fc_query':fc(path),'faces':[]}
 data=Path(path).read_bytes(); count=len(TTCollection(path).fonts) if data[:4]==b'ttcf' else 1
 for idx in range(min(count,4)): out['fonts'][key]['faces'].append({'index':idx,'cmap':cmap_info(path,idx)})
for name,(font,text) in samples.items():
 path=fonts[font]; idx=0
 out['samples'][name]={'font':font,'text':text,'codepoints':['U+%04X'%ord(c) for c in text],'nfc_codepoints':['U+%04X'%ord(c) for c in unicodedata.normalize('NFC',text)],'harfbuzz':shape(path,idx,text)}
Path('/tmp/acos-font-lab-20261006/results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
