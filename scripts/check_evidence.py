"""Kiểm tra số học tổng hợp; không chứng thực nguồn hay quan hệ nhân quả."""
import json, math, sys

def check(data):
    errors=[]
    for phase in ('before','after'):
        row=data.get(phase,{})
        n,k,p=row.get('n'),row.get('passed'),row.get('percent')
        if type(n) is not int or n<=0 or type(k) is not int or not 0<=k<=n:
            errors.append(f'{phase}: invalid counts'); continue
        if p is not None and (type(p) not in (int,float) or not math.isfinite(p) or abs(p-100*k/n)>0.051):
            errors.append(f'{phase}: percent mismatch')
    if data.get('before',{}).get('n')!=data.get('after',{}).get('n') and not data.get('attrition_note'):
        errors.append('sample changed without attrition note')
    if data.get('source_status') not in ('verified','user-provided','illustrative','missing'):
        errors.append('source status missing or invalid')
    return errors

if __name__=='__main__':
    try:
        d=json.load(open(sys.argv[1],encoding='utf-8')); e=check(d)
        print(json.dumps({'errors':e,'source_status':d.get('source_status'),'warning':'Arithmetic only; not proof of impact'},ensure_ascii=False,indent=2))
        sys.exit(bool(e))
    except (ValueError,OSError,IndexError,AttributeError,TypeError) as exc:
        print('Invalid input: '+str(exc));sys.exit(2)
