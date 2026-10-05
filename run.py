import hashlib, json, pathlib, platform, sys
from pdf_oxide import PdfDocument
fixtures={
 'production-repaired':'reports/production-pdfa4-2026-10-05/fixture-repaired2.pdf',
 'truetype-tagged':'/Users/quickwhitt/Documents/Codex/2026-10-05/referenced-chatgpt-conversation-this-is-an/outputs/pdf-engineering/truetype-tagged.pdf',
}
out={'tool':'pdf_oxide','version':'0.3.78','python':sys.version.split()[0],'platform':platform.platform(),'requested_target':'PDF/X-6 (ISO 15930-9:2020)','fixtures':{}}
for name,path in fixtures.items():
 p=pathlib.Path(path); d=PdfDocument(str(p)); row={'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 try:
  d.validate_pdf_x('6')
  row['pdfx6_attempt']={'status':'returned'}
 except Exception as e:
  row['pdfx6_attempt']={'status':'unsupported_or_error','exception_type':type(e).__name__,'message':str(e)}
 try:
  r=d.validate_pdf_x('4')
  row['pdfx4_control']={'status':'returned','repr':repr(r)}
 except Exception as e:
  row['pdfx4_control']={'status':'error','exception_type':type(e).__name__,'message':str(e)}
 out['fixtures'][name]=row
print(json.dumps(out,indent=2,sort_keys=True))
