import sys, unittest, subprocess, tempfile, json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from check_evidence import check
class EvidenceTests(unittest.TestCase):
    def data(self): return {'before':{'n':30,'passed':12,'percent':40},'after':{'n':30,'passed':18,'percent':60},'source_status':'illustrative'}
    def test_valid(self): self.assertEqual(check(self.data()),[])
    def test_impossible(self):
        d=self.data();d['after']['passed']=32;self.assertIn('after: invalid counts',check(d))
    def test_zero(self):
        d=self.data();d['before']['n']=0;self.assertTrue(check(d))
    def test_percentage(self):
        d=self.data();d['after']['percent']=90;self.assertIn('after: percent mismatch',check(d))
    def test_attrition(self):
        d=self.data();d['after']={'n':28,'passed':14,'percent':50};self.assertIn('sample changed without attrition note',check(d))
        d['attrition_note']='2 absent; descriptive only';self.assertEqual(check(d),[])
    def test_provenance(self):
        d=self.data();del d['source_status'];self.assertTrue(check(d))
    def test_nan(self):
        d=self.data();d['after']['percent']=float('nan');self.assertTrue(check(d))
    def test_boolean(self):
        d=self.data();d['before']['n']=True;self.assertTrue(check(d))
    def test_oversized_percent(self):
        d=self.data();d['after']['percent']=10**1000;self.assertIn('after: percent mismatch',check(d))
    def test_non_object(self):
        for value in (None,[],42,'text'):
            with self.subTest(value=value):
                self.assertEqual(check(value),['input must be an object'])
    def test_non_object_phase(self):
        for value in (None,[],42,'text'):
            with self.subTest(value=value):
                d=self.data();d['after']=value
                self.assertIn('after: must be an object',check(d))
    def test_attrition_note_type(self):
        for note in (True,1,[],{},'   '):
            with self.subTest(note=note):
                d=self.data();d['after']['n']=28;d['after']['percent']=None;d['attrition_note']=note
                self.assertIn('sample changed without attrition note',check(d))
    def cli(self,text):
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'data.json';path.write_text(text,encoding='utf-8')
            return subprocess.run([sys.executable,str(Path(__file__).resolve().parents[1]/'scripts/check_evidence.py'),str(path)],text=True,capture_output=True)
    def test_cli_valid(self):
        r=self.cli(json.dumps(self.data()));self.assertEqual(r.returncode,0);self.assertEqual(json.loads(r.stdout)['errors'],[])
    def test_cli_impossible(self):
        d=self.data();d['after']['passed']=32
        r=self.cli(json.dumps(d));self.assertEqual(r.returncode,1);self.assertIn('after: invalid counts',json.loads(r.stdout)['errors'])
    def test_cli_non_object(self):
        r=self.cli('null');self.assertEqual(r.returncode,1);self.assertIn('input must be an object',json.loads(r.stdout)['errors'])
    def test_cli_duplicate_key(self):
        r=self.cli('{"before":{"n":30,"n":40}}');self.assertEqual(r.returncode,2);self.assertIn('duplicate JSON key',r.stdout)
    def test_cli_nonfinite(self):
        for value in ('NaN','Infinity','-Infinity'):
            with self.subTest(value=value):
                r=self.cli('{"percent":'+value+'}');self.assertEqual(r.returncode,2);self.assertIn('non-finite JSON',r.stdout)
    def test_cli_invalid_json(self):
        r=self.cli('{broken');self.assertEqual(r.returncode,2);self.assertIn('Invalid input',r.stdout)
if __name__=='__main__': unittest.main()
