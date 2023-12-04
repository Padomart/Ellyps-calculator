import re

import wx


class Numbers(wx.Validator):
    def __init__(self, style=0):
        wx.Validator.__init__(self)
        self.Bind(wx.EVT_CHAR, self.OnChar)
        self.Bind(wx.EVT_TEXT, self.OnText)

        self.Bind(wx.EVT_TEXT_PASTE, self.OnPaste)

        self.tool_tip = wx.ToolTip("Некорректный формат ввода: x, y")
        self._value = ""
        self._is_valid = True
        self._style = style

    def Clone(self):
        return Numbers(self._style)

    def Validate(self, win):
        return self._is_valid

    def TransferToWindow(self):
        text_ctrl = self.GetWindow()
        text_ctrl.SetValue(self._value)
        return True

    def TransferFromWindow(self):
        text_ctrl = self.GetWindow()
        self._value = text_ctrl.GetValue()
        return True

    def OnChar(self, event):
        key = event.GetKeyCode()
        if key < wx.WXK_SPACE or key > 255:
            event.Skip()
            return

        text_ctrl = self.GetWindow()
        current_value = text_ctrl.GetValue()
        key_code = chr(key)

        if key_code.isdigit() or key_code in "(),. []{}":
            event.Skip()
        else:
            pass
        return

    def OnText(self, event):
        text_ctrl = self.GetWindow()
        value = text_ctrl.GetValue()
        if self.IsValid(value):
            self._is_valid = True
            self._value = value
            text_ctrl.SetBackgroundColour(wx.NullColour)
            self.tool_tip.Enable(False)
        else:
            self._is_valid = False
            text_ctrl.SetBackgroundColour("pink")
            text_ctrl.SetToolTip(self.tool_tip)
            self.tool_tip.Enable(True)
            text_ctrl.Refresh()
        text_ctrl.Refresh()
        event.Skip()

    def OnPaste(self, event):
        clipboard = wx.TextDataObject()
        if wx.TheClipboard.Open():
            success = wx.TheClipboard.GetData(clipboard)
            wx.TheClipboard.Close()

            if success:
                pasted_text = clipboard.GetText()
                if not self.IsValid(pasted_text):
                    return
        event.Skip()

    def IsValid(self, value):
        pattern = r"\s*\(*\s*\d+\s*,\s*\d+\s*\)*\s*"
        return re.match(pattern, value) is not None
