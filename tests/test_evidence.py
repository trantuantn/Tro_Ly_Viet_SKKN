import sys, unittest
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
if __name__=='__main__': unittest.main()
