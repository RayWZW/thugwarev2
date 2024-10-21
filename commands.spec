# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:\\SOFTWAREII\\thugware\\discordrat2\\commands.pyw'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['pyautogui'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['_lzma', '_multiprocessing', 'attrs', 'cryptography', 'cv2', 'numpy', 'PyQt5', 'win32', 'yaml', 'zstandard'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='commands',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['D:\\SOFTWAREII\\thugware\\discordrat2\\bonzee.ico'],
)
