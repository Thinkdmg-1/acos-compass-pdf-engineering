from pathlib import Path
from itertools import product
from functools import lru_cache
import json, hashlib, unicodedata
from pypdf import PdfReader
import pdfplumber

ROOT=Path.cwd()
OUT=ROOT/'outputs/acos-university-study'
OUT.mkdir(exist_ok=True)

# Teaching adaptation: contiguous indivisible blocks, no floating figures.
# Fixed objective: square unused capacity per non-final page; final page free.
# Preconditions: heights are strictly positive integers and capacity is positive.
# Inputs outside this teaching contract are not supported or validated here.
def dp(heights, cap):
    @lru_cache(None)
    def solve(i):
        if i==len(heights): return 0, ()
        best=(float('inf'), ())
        used=0
        for j in range(i+1,len(heights)+1):
            used+=heights[j-1]
            if used>cap: break
            rest,cuts=solve(j)
            cost=(0 if j==len(heights) else (cap-used)**2)+rest
            if cost<best[0]: best=(cost,(j,)+cuts)
        return best
    return solve(0)

def brute(heights,cap):
    best=float('inf')
    for mask in product((False,True),repeat=len(heights)-1):
        cuts=[i+1 for i,b in enumerate(mask) if b]+[len(heights)]
        starts=[0]+cuts[:-1]
        loads=[sum(heights[a:b]) for a,b in zip(starts,cuts)]
        if any(v>cap for v in loads): continue
        cost=sum((cap-v)**2 for v in loads[:-1])
        best=min(best,cost)
    return best

fixtures=[([3,3,3,3],10),([7,2,6,3,2],10),([4,5,1,6,2,3],10),([10,10,10],10),([11],10)]
# Exhaustive unfamiliar fixtures, independent enumerator rather than DP recurrence.
checks=[]
for n in range(1,7):
    for h in product((2,5,8),repeat=n):
        a=dp(h,10)[0];b=brute(h,10)
        assert a==b,(h,a,b)
        checks.append(h)
worked=[]
for h,c in fixtures:
    cost,cuts=dp(h,c)
    worked.append({'heights':h,'capacity':c,'cost':None if cost==float('inf') else cost,'cuts':cuts,'feasible':cost!=float('inf')})

# MIT MAS.962 ps1 question 1 adapted to contemporary CSS/print definitions.
units=[{'css_px':1056,'css_inches':1056/96,'predicted_pt':1056*72/96},
       {'css_px':816,'css_inches':816/96,'predicted_pt':816*72/96},
       {'font_css_px':24,'font_pt':24*72/96,'one_em_css_px':24}]
geometry=[]
for name in ('cff-untagged','truetype-untagged','truetype-tagged'):
    p=ROOT/'outputs/pdf-engineering'/f'{name}.pdf'
    r=PdfReader(p)
    with pdfplumber.open(p) as q:
        second=[q.pages[0].width,q.pages[0].height]
    first=[float(r.pages[0].mediabox.width),float(r.pages[0].mediabox.height)]
    assert max(abs(a-b) for a,b in zip(first,[792,612]))<=.01
    assert first==second
    text=' '.join(unicodedata.normalize('NFKC',r.pages[0].extract_text()).split())
    assert 'ffi fi fl Æ Ω → 0123456789.' in text
    geometry.append({'file':p.name,'pypdf_pt':first,'pdfplumber_pt':second,'user_unit':r.pages[0].get('/UserUnit',1),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'normalized_character_check':True})

results={'purpose':'Worked university-study exercises; synthetic examples are not client performance metrics',
         'preserved_failure':{'first_execution':'Character assertion failed because extraction inserted a line break before digits','diagnosis':'The assertion conflated semantic characters with line layout','repair':'Apply NFKC for ligatures and normalize whitespace for this semantic-preservation test','boundary':'This normalization cannot verify original spacing or reading order'},
         'typography_units':units,'geometry_independent_measurements':geometry,
         'pagination':{'model':'Contiguous indivisible block adaptation, not reproduction of the paper algorithm','objective':'Squared spare capacity on non-final pages; zero penalty for final page','unit':'synthetic integer height','exhaustive_fixture_count':len(checks),'dp_matches_independent_enumeration':True,'worked_examples':worked,'limits':'No floats, citation ordering, elastic whitespace, multi-column balancing, or subjective quality claim'},
         'course_reading_answers':{'typography':['Tighter leading makes the text field darker','Oldstyle and lining figures correspond to lowercase/uppercase treatment','100em paragraphs are not justified by the reading','Poor pair spacing can cause character recognition errors'],
                                  'layout':'Whitespace grouping applies proximity',
                                  'experiment_design':'Uncontrolled variables can affect measured outcomes',
                                  'experiment_analysis':'A p-value is not the probability a hypothesis is true; significance is not effect size; challenge the course simplifications with ASA guidance',
                                  'accessibility':'Walking and riding in a crowded moving subway are situational impairments; chronic conditions are a different classification'}}
(OUT/'exercise-results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'enumerated_pagination_fixtures':len(checks),'independent_pdf_geometry_checks':len(geometry),'all_executed_assertions_passed':True}))
