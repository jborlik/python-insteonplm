from .messageBase import MessageBase
from insteonplm.constants import *
import binascii

class ButtonEventReport(MessageBase):
    """Insteon Button Event Report Message Received 0x54"""
    
    _code = MESSAGE_BUTTON_EVENT_REPORT_0X54
    _sendSize = MESSAGE_BUTTON_EVENT_REPORT_SIZE
    _receivedSize = MESSAGE_BUTTON_EVENT_REPORT_SIZE
    _description = 'INSTEON Standard Message Received'


    def __init__(self, event):
        self._event = event

        self._events = {0x02: 'SET button tapped',
                    0x03: 'SET button press and hold',
                    0x04: 'SET button released',
                    0x12: 'Button 2 tapped',
                    0x13: 'Button 2 press and hold',
                    0x14: 'Button 2 released',
                    0x22: 'Button 3 tapped',
                    0x23: 'Button 3 press and hold',
                    0x24: 'Button 3 released'}
        
    @classmethod
    def from_raw_message(cls, rawmessage):
            return ButtonEventReport(rawmessage[2])

    @property
    def event(self):
        return self._event

    @property
    def eventText(self):
        return self._events.get(self.event, None)

    def to_hex(self):
        return self._messageToHex(self._event)