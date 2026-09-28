import unittest, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from client import LegalClauseCrossReferenceResolver

class CoreTests(unittest.TestCase):
    def setUp(self):self.c=LegalClauseCrossReferenceResolver()

    def test_graph_and_cycle_path(self):
        graph=self.c.map_clause_dependencies({'Section 1':'See Section 2.','Section 2':'See Section 3.','Section 3':'See Section 2.'})
        self.assertEqual(self.c.detect_circular_references(graph)['cycles_detected'],[['Section 2','Section 3','Section 2']])
        self.assertTrue(self.c.detect_circular_references(self.c.map_clause_dependencies({'Section 1':'See Section 1.'}))['has_circular_references'])
    def test_definition_backslash_and_single_pass(self):
        out=self.c.resolve_and_expand_clause('Section 1',{'Section 1':'Affiliate Company'},{'Affiliate':r'Company C:\new','Company':'entity'})
        self.assertIn(r'Company C:\new',out['expanded_text'])
        self.assertEqual(out['terms_substituted'],['Affiliate','Company'])
