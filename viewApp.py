from cefpython3 import cefpython as cef
from configuracao import Configuracao
from historicoProcessamento import HistoricoProcessamento

import os
import sys
import platform
import json
import logging
import base64
import time


WINDOWS = (platform.system() == "Windows")
LINUX = (platform.system() == "Linux")
MAC = (platform.system() == "Darwin")
WINDOWS_UTILS = cef.WindowUtils()

class Gui(object):

    def window(self):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)) + '/view/viewApp.html'), 'r') as htmlFile:
            data=htmlFile.read().replace('\n', '')
            browser = cef.CreateBrowserSync(url=html_to_data_uri(data), window_title="Sienge",)       
        
        set_javascript_bindings(browser)
        cef.MessageLoop()


def set_javascript_bindings(browser):
    bindings = cef.JavascriptBindings(bindToFrames=False, bindToPopups=False)
    bindings.SetFunction("buscarHistorico", buscarHistorico)
    browser.SetJavascriptBindings(bindings)


def buscarHistorico(callback=None):
    historicoProcessamento = HistoricoProcessamento()
    historicoProcessamento.carregar()
    if callback:
        callback.Call(historicoProcessamento.__dict__)
    else:
        return historicoProcessamento.__dict__


def html_to_data_uri(html, js_callback=None):
    html = html.encode("UTF-8", "replace")
    b64 = base64.b64encode(html).decode("UTF-8", "replace")
    ret = "data:text/html;base64,{data}".format(data=b64)
    return ret


def loadView():

    check_versions()
    sys.excepthook = cef.ExceptHook

    settings = {
        "product_version": "AutomatizacaoBancaria/1.00",
        "user_agent": "AutomatizacaoBancaria/1.00"
    }

    if WINDOWS:
        settings["auto_zooming"] = "system_dpi"
        cef.DpiAware.SetProcessDpiAware()

    cef.Initialize(settings=settings)

    app = Gui()
    app.window()

    sys.exit()


def check_versions():
    assert cef.__version__ >= "55.3", "CEF Python v55.3+ required to run this"