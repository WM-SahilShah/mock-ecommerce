import logging

# Set up a basic logger with padding for module names
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)-5s - %(module)-10s - %(message)s'
    )

logger = logging.getLogger(__name__)
