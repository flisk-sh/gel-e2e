import re
import unittest
from pathlib import Path


class OpenApiContractTest(unittest.TestCase):
    def test_user_responses_document_the_email_field(self):
        spec = Path("api/openapi.yaml").read_text(encoding="utf-8")

        self.assertRegex(
            spec,
            re.compile(
                r'"200":\n'
                r"          description: List users\n"
                r"          content:\n"
                r"            application/json:\n"
                r"              schema:\n"
                r"                type: array\n"
                r"                items:\n"
                r"                  \$ref: '#/components/schemas/User'"
            ),
        )
        self.assertEqual(spec.count("$ref: '#/components/schemas/User'"), 3)
        self.assertRegex(
            spec,
            re.compile(
                r"User:\n"
                r"      type: object\n"
                r"      required:\n"
                r"        - id\n"
                r"        - email\n"
                r"      properties:\n"
                r"        id:\n"
                r"          type: integer\n"
                r"        email:\n"
                r"          type: string\n"
                r"          format: email"
            ),
        )


if __name__ == "__main__":
    unittest.main()
