"""Initial operator - This operator keeps the initial character of the input text"""

from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
	"""Return the first character of the provided text"""

	def operate(self, text: str = None, params: Dict = None) -> str:
		"""Return the initials for the provided text or empty string"""
		if not text:
			return ""

		# Split on whitespace and ignore empty tokens
		tokens = [t for t in text.split() if t]
		if not tokens:
			return ""

		initials = [f"{t[0].upper()}." for t in tokens]
		return " ".join(initials)

	def validate(self, params: Dict = None) -> None:
		"""No parameters are required for this operator"""
		pass

	def operator_name(self) -> str:
		"""Return operator name"""
		return "initial"

	def operator_type(self) -> OperatorType:
		"""Return operator type (Anonymize)"""
		return OperatorType.Anonymize

