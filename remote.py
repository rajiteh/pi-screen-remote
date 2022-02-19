#!/usr/bin/env python

from logger import get_logger
import RPi.GPIO as GPIO
import time


PIN_MAPPINGS = {
  "SCREEN_UP": 7,
  "SCREEN_DOWN": 13,
  "SCREEN_STOP": 11
}
_REVERSE_MAPPINGS = {v: k for k, v in PIN_MAPPINGS.items()}


logger = get_logger(__name__)

class ProjectorRemote(object):

  def __init__(self):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_MAPPINGS["SCREEN_UP"], GPIO.OUT)
    GPIO.setup(PIN_MAPPINGS["SCREEN_STOP"], GPIO.OUT)
    GPIO.setup(PIN_MAPPINGS["SCREEN_DOWN"], GPIO.OUT)

  def cleanup(self):
    GPIO.output(PIN_MAPPINGS["SCREEN_UP"], 0)
    GPIO.output(PIN_MAPPINGS["SCREEN_STOP"], 0)
    GPIO.output(PIN_MAPPINGS["SCREEN_DOWN"], 0)
    GPIO.cleanup()

  def _press(self, pin):
    GPIO.output(pin, 1)
    time.sleep(0.2)
    GPIO.output(pin, 0)
    logger.info(f"Triggered: {_REVERSE_MAPPINGS[pin]}")
    time.sleep(0.2)

  def down(self, seconds):
    self._press(PIN_MAPPINGS["SCREEN_STOP"])
    self._press(PIN_MAPPINGS["SCREEN_DOWN"])
    time.sleep(seconds)
    self._press(PIN_MAPPINGS["SCREEN_STOP"])

  def stop(self):
    self._press(PIN_MAPPINGS["SCREEN_STOP"])

  def up(self):
    self._press(PIN_MAPPINGS["SCREEN_UP"])
