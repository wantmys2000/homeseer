import logging
import os

import debugpy
from homeassistant.core import HomeAssistant

_LOG = logging.getLogger(__name__)

#
# Start Debugger
#
async def start_debugger(hass: HomeAssistant):
    await hass.async_add_executor_job(_start_debugger)

def _start_debugger():
    _LOG.debug(f"Starting debugger...HA_DEBUG=[{os.getenv('HA_DEBUG')}]")

    ha_debug = os.getenv("HA_DEBUG")
    print(f"HA_DEBUG = {ha_debug}")

    if not ha_debug or ha_debug == "False":
        _LOG.debug("HA_DEBUG is not set...Debugging not available")
        return

    try:
        debugpy.listen(("0.0.0.0",5678))
        _LOG.debug("Debugger listening on 5678")
    except RuntimeError as e:
        _LOG.debug("Failed to call: debugpy.listen('0.0.0.0, 5678')", e)

    if not debugpy.is_client_connected():
        _LOG.warning("Waiting for debugger attach...")
        debugpy.wait_for_client()

        #debugpy.breakpoint()

    _LOG.debug("Debugger attached")

def breakpoint():
    if debugpy.is_client_connected():
        debugpy.breakpoint()
    else:
        _LOG.warning("Cannot set breakpoint: Debugger is not attached")