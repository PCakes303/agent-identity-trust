import unittest
from tools.validate_principal import validate
V={"principal_id":"urn:example:agent:one","principal_type":"agent","issuer":"https://identity.example.test","created_at":"2026-11-01T12:00:00Z","status":"active"}
class Tests(unittest.TestCase):
 def test_valid(self): self.assertEqual(validate(V),[])
 def test_type(self): self.assertTrue(validate({**V,"principal_type":"robot"}))
 def test_issuer(self): self.assertTrue(validate({**V,"issuer":"http://identity.example.test"}))
 def test_timestamp(self): self.assertTrue(validate({**V,"created_at":"yesterday"}))
 def test_status(self): self.assertTrue(validate({**V,"status":"trusted"}))
if __name__=="__main__": unittest.main()
