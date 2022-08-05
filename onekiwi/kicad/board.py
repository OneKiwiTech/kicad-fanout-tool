import pcbnew
import os
import re
import wx

PLUGIN_PATH = os.path.split(os.path.abspath(__file__))[0]

def get_wxWidgets_version():
    v = re.search(r"wxWidgets\s([\d\.]+)", wx.version())
    v = int(v.group(1).replace(".", ""))
    return v

def get_plugin_version():
    """READ Version from file"""
    if not os.path.isfile(os.path.join(PLUGIN_PATH, "VERSION")):
        return "unknown"
    with open(os.path.join(PLUGIN_PATH, "VERSION")) as f:
        return f.read()

def get_kicad_build_version():
    return pcbnew.GetBuildVersion()

def get_current_unit():
    unit = pcbnew.GetUserUnits()
    # pcbnew.EDA_UNITS_INCHES = 0
    if unit == pcbnew.EDA_UNITS_INCHES:
        return 'in'
    # pcbnew.EDA_UNITS_MILLIMETRES = 1
    elif unit == pcbnew.EDA_UNITS_MILLIMETRES:
        return 'mm'
    # pcbnew.EDA_UNITS_MILS = 5
    elif unit == pcbnew.EDA_UNITS_MILS:
        return 'mil'