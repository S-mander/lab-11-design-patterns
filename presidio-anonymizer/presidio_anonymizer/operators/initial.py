"""Initial operator - This operator keeps the initial character of the input text"""

from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
	"""Return the first character of the provided text"""

	def operate(self, text: str = None, params: Dict = None) -> str:
		"""Return the initial character of the text or empty string"""
		if not text:
			return ""
		return text[0]

	def validate(self, params: Dict = None) -> None:
		"""No parameters are required for this operator"""
		pass

	def operator_name(self) -> str:
		"""Return operator name"""
		return "initial"

	def operator_type(self) -> OperatorType:
		"""Return operator type (Anonymize)"""
		return OperatorType.Anonymize

