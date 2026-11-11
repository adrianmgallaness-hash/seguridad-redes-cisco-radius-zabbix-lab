import unittest
from audit_cis import evaluate, report

class AuditTests(unittest.TestCase):
    def state(self, config, name):
        return next(r[1] for r in evaluate(config) if r[0] == name)
    def test_missing_lines_not_compliant(self):
        self.assertEqual(self.state("hostname R\nend\n","Timeout Consola"),"NO EVALUABLE")
        self.assertEqual(self.state("hostname R\nend\n","VTY exclusivamente SSH"),"NO EVALUABLE")
    def test_all_vty_ranges_checked(self):
        c = "line vty 0 4\n transport input ssh\nline vty 5 15\n transport input telnet ssh\nend\n"
        self.assertEqual(self.state(c,"VTY exclusivamente SSH"),"HALLAZGO")
    def test_zero_timeout_and_type5(self):
        c = "line con 0\n exec-timeout 0 0\n!\nusername u privilege 15 secret 5 <OCULTO>\nend\n"
        self.assertEqual(self.state(c,"Timeout Consola"),"HALLAZGO")
        self.assertEqual(self.state(c,"Algoritmos de credenciales"),"HALLAZGO")
    def test_secrets_not_echoed(self):
        c = "snmp-server community VALOR_PRIVADO RO 20\nenable secret 5 HASH_PRIVADO\n"
        self.assertNotIn("VALOR_PRIVADO",report(c))
        self.assertNotIn("HASH_PRIVADO",report(c))

if __name__ == "__main__":
    unittest.main()
