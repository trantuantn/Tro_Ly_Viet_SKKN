"""Kiểm tra số học tổng hợp; không chứng thực nguồn hay quan hệ nhân quả."""
import json, math, sys

def check(data):
    if not isinstance(data, dict):
        return ['input must be an object']
    errors=[]
    for phase in ('before','after'):
        row=data.get(phase,{})
        if not isinstance(row, dict):
            errors.append(f'{phase}: must be an object'); continue
        n,k,p=row.get('n'),row.get('passed'),row.get('percent')
        if type(n) is not int or n<=0 or type(k) is not int or not 0<=k<=n:
            errors.append(f'{phase}: invalid counts'); continue
        if p is not None and (type(p) not in (int,float) or not 0<=p<=100 or not math.isfinite(p) or abs(p-100*k/n)>0.051):
            errors.append(f'{phase}: percent mismatch')
    before,after=data.get('before'),data.get('after')
    if isinstance(before,dict) and isinstance(after,dict) and before.get('n')!=after.get('n'):
        note=data.get('attrition_note')
        if not isinstance(note,str) or not note.strip():
            errors.append('sample changed without attrition note')
    if data.get('source_status') not in ('verified','user-provided','illustrative','missing'):
        errors.append('source status missing or invalid')
    return errors

def unique_object(pairs):
    result={}
    for key,value in pairs:
        if key in result:
            raise ValueError('duplicate JSON key: '+key)
        result[key]=value
    return result

def reject_constant(value):
    raise ValueError('non-finite JSON constant: '+value)

if __name__=='__main__':
    try:
        with open(sys.argv[1],encoding='utf-8') as source:
            d=json.load(source,object_pairs_hook=unique_object,parse_constant=reject_constant)
        e=check(d)
        print(json.dumps({'errors':e,'source_status':d.get('source_status') if isinstance(d,dict) else None,'warning':'Arithmetic only; not proof of impact'},ensure_ascii=False,indent=2))
        sys.exit(bool(e))
    except (ValueError,OSError,IndexError,AttributeError,TypeError) as exc:
        print('Invalid input: '+str(exc));sys.exit(2)
