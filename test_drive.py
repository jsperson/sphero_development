#!/usr/bin/env python3
"""Simple test script to verify RVR drive commands work."""
import asyncio
import sys
sys.path.insert(0, '/home/jsperson/source/sphero-sdk-raspberrypi-python')

import nest_asyncio
nest_asyncio.apply()

from sphero_sdk import SpheroRvrAsync, SerialAsyncDal

async def main():
    loop = asyncio.get_running_loop()
    dal = SerialAsyncDal(loop, port_id="/dev/ttyS0", baud=115200)
    rvr = SpheroRvrAsync(dal=dal)

    print("Waking RVR...")
    await rvr.wake()
    await asyncio.sleep(2)

    print("Resetting yaw...")
    await rvr.reset_yaw()
    await asyncio.sleep(0.5)

    print("Driving forward at speed 50 for 1 second...")
    await rvr.drive_with_heading(speed=50, heading=0, flags=0)
    await asyncio.sleep(1)

    print("Stopping...")
    await rvr.drive_stop()

    print("Closing connection...")
    await rvr.close()
    print("Done!")

if __name__ == "__main__":
    asyncio.run(main())
