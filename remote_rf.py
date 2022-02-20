#!/usr/bin/env python

from contextlib import contextmanager
from logger import get_logger
from rpi_rf import RFDevice
import time

logger = get_logger(__name__)

RF_OP_CODES = {
  'DOWN': 3135044,
  'STOP': 3135048,
  'UP': 3135042
}

class InterruptedException(Exception):
  pass

class ProjectorRemoteRF(object):

  INTERRUPT = False

  def __init__(self, gpio):
    self.rfdevice = RFDevice(gpio)
    self.rfdevice.enable_tx()

    self.rfdevice.tx_repeat = 10
    self.protocol = 1
    self.length = 24
    self.pulselength = 190

  def _send_code(self, code: int):
    ProjectorRemoteRF.INTERRUPT = True
    self.rfdevice.tx_code(
      code,
      self.protocol,
      self.pulselength,
      self.length
    )

  def interruptible_sleep(self, duration):
    ProjectorRemoteRF.INTERRUPT = False
    while duration >= 0:
      duration -= 1
      if ProjectorRemoteRF.INTERRUPT:
        logger.info("Wait interrupted.")
        self.INTERRUPT = False
        raise InterruptedException("Interrupted")
      time.sleep(1)

  def up(self):
    logger.info("Triggering UP")
    self._send_code(RF_OP_CODES['UP'])

  def down(self, seconds):
    logger.info("Triggering Down")
    self._send_code(RF_OP_CODES['DOWN'])
    logger.info(f"Waiting for down timeout: {str(seconds)}")
    try:
      self.interruptible_sleep(seconds)
      logger.info("Down timeout reached.")
      self.stop()
    except InterruptedException:
      logger.info("Down timeout interrupted.")

  def stop(self):
    logger.info("Triggering STOP")
    self._send_code(RF_OP_CODES['STOP'])


