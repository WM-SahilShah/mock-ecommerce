import logging

# Set up a basic logger with padding for module names
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(module)-15s - %(levelname)-8s - %(message)s'
    )

logger = logging.getLogger(__name__)
