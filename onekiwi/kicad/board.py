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
    return str(pcbnew.GetBuildVersion())

def get_kicad_semantic_version():
    return str(pcbnew.GetSemanticVersion())

def get_kicad_major_minor_version():
    return str(pcbnew.GetMajorMinorVersion())

def get_kicad_version():
    version = str(pcbnew.Version())
    major = version.split(".")[0]
    minor = version.split(".")[1]
    patch = version.split(".")[2]

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

def get_onekiwi_path():
    # controller dir
    current_path = os.path.dirname(__file__)
    onekiwi_path = os.path.dirname(current_path)
    return onekiwi_path

def get_image_path():
    onekiwi_path = get_onekiwi_path()
    image_path = os.path.join(onekiwi_path, 'image')
    return image_path
