import logging

from common import get_rabbitmq_connection, get_rabbitmq_channel
from queue_config import queue_config as configurations


logger = logging.getLogger(__name__)


def setup_queues():
    rabbitmq_connection = get_rabbitmq_connection()
    try:
        for queue in configurations:
            get_rabbitmq_channel().queue_declare(queue=queue['queue_name'])
    except Exception as e:
        logger.warning(f'Failed to construct all queues: {e}')
    finally:
        rabbitmq_connection.close()


def main():
    setup_queues


if __name__ == '__main__':
    main()
