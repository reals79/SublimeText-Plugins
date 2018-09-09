import sublime
import sublime_plugin

key_plugin = "ViewCharacterCode"

class ViewCharacterCode(sublime_plugin.EventListener):

    def on_selection_modified(self, view):
        text = "(Symbol: "
        sels = view.sel()
        #currentRegion = view.word(sels[0])
        pos = sels[0].begin()
        currentSymb = view.substr(pos)
        text += currentSymb
        text += " | ASCII: " + str(ord(currentSymb))
        text += " | HEX: " + hex(ord(currentSymb))
        text += ")"

        view.set_status(key_plugin, text)
