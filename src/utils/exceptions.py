class SecretSantaError(Exception):
    """Base exception for Secret Santa errors."""


class InvalidCSVError(SecretSantaError):
    """Raised when input CSV is missing or invalid."""


class AssignmentGenerationError(SecretSantaError):
    """Raised when a valid Secret Santa assignment cannot be generated."""